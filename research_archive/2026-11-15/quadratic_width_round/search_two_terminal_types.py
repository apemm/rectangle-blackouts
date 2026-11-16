"""Targeted exact K2,t integer-CSP search in every small offset type.

Original ranks are retained. Constraints are candidate P constraints,
without strip or owner tests. Pairs with more than two forbidden integer
differences are excluded from the tested subsystem, but labels are not
yet removed by the exceptional-band rule.
"""

import argparse
import json
import math
import time
from collections import defaultdict
from itertools import combinations
from pathlib import Path

from search_zero_offset_types import curve, odd_vertical_legs


def full_events(side, stride=32, choices=3, orient="id"):
    pts = curve(side)
    if orient == "swap":
        pts = [(y, x) for x, y in pts]
    count = len(pts)
    for d in range(1, count):
        by_u = defaultdict(set)
        for r in range(count-d):
            x, y = pts[r]
            xx, yy = pts[r+d]
            by_u[yy-x].add(r)
            by_u[y-xx].add(r)
        for delta in range(1-choices, choices):
            q = choices*d+delta
            for vertical in odd_vertical_legs(stride*q):
                for sign in (-1, 1):
                    total_u = (sign*vertical-1)//2
                    residue = total_u % side
                    for local_u in (residue, residue-side):
                        rs = by_u.get(local_u)
                        if rs:
                            yield (total_u-local_u)//side, d, delta, rs


def signed_forbidden(edges, x, y):
    """Forbidden values of choice(y)-choice(x)."""
    if x < y:
        return edges[(x,y)]
    return {-d for d in edges[(y,x)]}


def relation(edges, a, b, c):
    """Nine-bit relation on a,b after existentially choosing c."""
    fa = signed_forbidden(edges, a, c)
    fb = signed_forbidden(edges, b, c)
    return sum(1 << (3*x+y) for x in range(3) for y in range(3)
               if any(z-x not in fa and z-y not in fb for z in range(3)))


def search(side, orient, drop_local_multiple=False):
    start = time.monotonic()
    types = defaultdict(lambda: defaultdict(set))
    for k, d, delta, rs in full_events(side, orient=orient):
        for r in rs:
            types[k][(r,r+d)].add(delta)
    witnesses = []
    relation_counts = defaultdict(int)
    module_count = 0
    common_diagonal = 0b100010001
    bad_common_diagonal = []
    central_exclusions = []
    deleted_incident_labels = 0
    pts = curve(side)
    if orient == "swap":
        pts = [(y,x) for x,y in pts]
    for k, original in types.items():
        removed = set()
        if drop_local_multiple:
            for (r,s), ds in original.items():
                if len(ds)<2:
                    continue
                x,y=pts[r]; xx,yy=pts[s]
                for u in (side*k+yy-x,side*k+y-xx):
                    Y=abs(2*u+1)
                    count=0
                    for delta in ds:
                        X=32*(3*(s-r)+delta)
                        z=math.isqrt(X*X+Y*Y)
                        count += z*z==X*X+Y*Y
                    if count>1:
                        removed.update((r,s))
            deleted_incident_labels += len(removed)
        edges = {uv: ds for uv,ds in original.items() if len(ds)<=2}
        if removed:
            edges = {uv: ds for uv,ds in edges.items()
                     if not (set(uv)&removed)}
        adj = defaultdict(set)
        for a,b in edges:
            adj[a].add(b); adj[b].add(a)
        leaves = defaultdict(list)
        for c, ns in adj.items():
            for a,b in combinations(sorted(ns),2):
                leaves[(a,b)].append(c)
        for (a,b), cs in leaves.items():
            allowed = 511
            used = []
            for c in cs:
                rr = relation(edges,a,b,c)
                relation_counts[rr] += 1
                module_count += 1
                common_diagonal &= rr
                if not (rr&16) and len(central_exclusions)<10:
                    central_exclusions.append({"offset":k,"anchors":[a,b],
                        "leaf":c,"relation":rr,"edges":[
                        [min(a,c),max(a,c),sorted(edges[tuple(sorted((a,c)))])],
                        [min(b,c),max(b,c),sorted(edges[tuple(sorted((b,c)))])]]})
                if not (rr & 0b100010001) and len(bad_common_diagonal)<5:
                    bad_common_diagonal.append([k,a,b,c,rr])
                if (allowed & rr) != allowed:
                    used.append(c)
                    allowed &= rr
                if not allowed:
                    # Remove redundant leaves for a small exact certificate.
                    for cc in used[:]:
                        others = [x for x in used if x != cc]
                        test = 511
                        for x in others:
                            test &= relation(edges,a,b,x)
                        if not test:
                            used = others
                    witnesses.append({"offset":k,"anchors":[a,b],"leaves":used,
                        "edges":[[u,v,sorted(edges[(u,v)])]
                                 for u,v in edges if (u in (a,b) and v in used)
                                 or (v in (a,b) and u in used)]})
                    break
            if witnesses:
                break
        if witnesses:
            break
    return {"side":side,"orientation":orient,"offset_types":len(types),
        "modules_checked":module_count,"distinct_relations":len(relation_counts),
        "common_diagonal_bits":common_diagonal,
        "drop_local_multiple":drop_local_multiple,
        "deleted_incident_labels":deleted_incident_labels,
        "central_anchor_exclusions":central_exclusions,
        "modules_excluding_all_equal_anchors":bad_common_diagonal,
        "witnesses":witnesses,"seconds":time.monotonic()-start}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sides",nargs="+",type=int,default=[8,16])
    ap.add_argument("--output",type=Path)
    ap.add_argument("--drop-local-multiple",action="store_true")
    args=ap.parse_args()
    results=[]
    for side in args.sides:
        for ori in ("id","swap"):
            result=search(side,ori,args.drop_local_multiple)
            results.append(result)
            print(json.dumps(result),flush=True)
    if args.output:
        args.output.write_text(json.dumps(results,indent=2)+"\n")


if __name__=="__main__":
    main()
