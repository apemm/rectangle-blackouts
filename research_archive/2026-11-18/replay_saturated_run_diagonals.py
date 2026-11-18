"""Independent fixed-partition replay of a run of double columns.

Uses an ambient run of the given width and tests only its central slice.
Rows and columns are zero-based internally. Mirrors and part complementation
are applied only when they preserve all tested clauses.
"""
import argparse
import hashlib
import json
from itertools import combinations

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Solver


from saturated_slice_diagonals import geometry


def geometry_with_parts(h, k, run_width):
    width, left, base, rivals = geometry(h, k, run_width)
    if width != run_width:
        raise ValueError("wrong ambient run")
    pool = IDPool(start_from=h*k+h+1)
    parts = [1+h*k+y for y in range(h)]
    clauses = list(base)
    for a,b,u,v in rivals:
        clauses.extend(((u,v,-parts[a],parts[b]),(u,v,parts[a],-parts[b])))
    for x in range(k):
        points = [1+h*x+y for y in range(h)]
        clauses.extend(CardEnc.equals(points, 2, vpool=pool, encoding=EncType.seqcounter).clauses)
        for a,b in combinations(range(h),2):
            prefix = (-points[a],-points[b])
            clauses.extend(((*prefix,parts[a],parts[b]),(*prefix,-parts[a],-parts[b])))
    return clauses, parts, left


def representatives(h):
    desired = (h+1)//2
    masks = []
    all_rows = (1<<h)-1
    for chosen in combinations(range(h),desired):
        mask = sum(1<<r for r in chosen)
        mirror = sum(1<<(h-1-r) for r in chosen)
        orbit = {mask,mirror}
        if h%2==0: orbit |= {all_rows^a for a in orbit}
        if mask == min(orbit):
            masks.append(mask)
    return sorted(masks)


def main():
    ap = argparse.ArgumentParser()
    for name in ("height","slice_width","run_width"):
        ap.add_argument(name,type=int)
    ap.add_argument("--shards", type=int, default=1)
    ap.add_argument("--shard", type=int, default=0)
    args = ap.parse_args()
    if not 0<=args.shard<args.shards:
        ap.error("invalid shard")
    all_masks = representatives(args.height)
    masks = all_masks[args.shard::args.shards]
    clauses,parts,left = geometry_with_parts(args.height,args.slice_width,args.run_width)
    digest=hashlib.sha256()
    print(json.dumps({"partitions":len(all_masks),"shard":args.shard,"count":len(masks),
                      "base_clauses":len(clauses),"left":left}),flush=True)
    with Solver(name="cadical195",bootstrap_with=clauses) as solver:
        for j,mask in enumerate(masks,1):
            assumptions=[part if mask>>i&1 else -part for i,part in enumerate(parts)]
            if solver.solve(assumptions=assumptions):
                print("SAT",mask,flush=True)
                return 1
            digest.update((str(mask)+"\n").encode("ascii"))
            if j%40==0: print("checked",j,"of",len(masks),flush=True)
    print(json.dumps({"all_unsat":True,"shard":args.shard,"count":len(masks),
                      "mask_sequence_sha256":digest.hexdigest()}),flush=True)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
