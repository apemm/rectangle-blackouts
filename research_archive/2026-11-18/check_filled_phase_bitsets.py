"""Exhaust tilted rectangles and shared-corner presentations with integer bitsets."""
from collections import defaultdict
from itertools import combinations
from math import gcd
import argparse
import base64
import hashlib
import json
from pathlib import Path
import zlib

from core_mixed_witness import from_record
from fiber_translation_search import group_key


def templates(h):
    # The bottom corner is unique. The two upward sides point to the
    # right and left, and their primitive directions are (a,b),(-b,a).
    choices = defaultdict(set)
    count = 0
    for a in range(1,h):
        for b in range(1,h-a):
            if gcd(a,b) != 1:
                continue
            for k in range(1,(h-1-a)//b+1):
                for j in range(1,(h-1-k*b)//a+1):
                    x,y = k*a,k*b
                    u,v = -j*b,j*a
                    pts = ((0,0),(x,y),(u,v),(x+u,y+v))
                    count += 1
                    for i,n in combinations(range(4),2):
                        p,q = sorted((pts[i],pts[n]))
                        black = sorted(pts[t] for t in range(4) if t not in (i,n))
                        first,second = black
                        shift = (first[0]-p[0],first[1]-p[1],
                                 second[0]-p[0],second[1]-p[1],i+n == 3)
                        choices[q[0]-p[0],q[1]-p[1]].add(shift)
    return choices,count


def assigned_doubles(rec,old):
    if "source_window" in rec:
        source = Path(__file__).resolve().parent/rec["source_window"]
        initial = json.loads(source.read_text())
        assert initial["levels"] == rec["levels"] and initial["height"] == rec["height"]
        cols = sorted(assigned_doubles(initial,old))
        first = prev = cols[0][0]
        loss = 0
        result = []
        for x,a,b in cols:
            loss += max(0,x-prev-rec["max_true_gap"])
            result.append((x-first-loss+rec["halo"],a,b))
            prev = x
        return result
    base = rec["base"]
    groups = rec.get("groups")
    if groups is None:
        groups = [(rec["group"],rec.get("columns"),0)]
    cols = []
    for group,selected,shift in groups:
        subset = None if selected is None else set(selected)
        source = [(x,a,b) for x,a,b in old
                  if group_key(a,b)[:3] == tuple(group) and (subset is None or x in subset)]
        if subset is not None:
            assert {x for x,a,b in source} == subset
        cols.extend((x+shift-base,a,b) for x,a,b in source)
    assert len({x for x,a,b in cols}) == len(cols)
    return cols


def audit(rec, sparse_index=False):
    h, width, base = rec["height"],rec["width"],rec["base"]
    low,high = rec["levels"]
    data = zlib.decompress(base64.b64decode(rec["high_zlib_base64"]))
    assert hashlib.sha256(data).hexdigest() == rec["high_sha256"]
    upper = int.from_bytes(data,"little")
    assert len(data) == (width+7)//8 and upper.bit_length() <= width
    all_columns = (1<<width)-1
    # Load just the old doubles. The check below uses the geometric
    # positions and the bit word, independently of the solver's clauses.
    cols = assigned_doubles(rec,from_record(h,96,186))
    assert len(cols) == rec["doubles"] and all(0 <= x < width for x,a,b in cols)
    double_sites = sum(1<<x for x,a,b in cols)
    assert not upper & double_sites
    B = [0]*(h+1)
    B[low] = all_columns ^ (upper | double_sites)
    B[high] = upper
    owners = {}
    for x,a,b in cols:
        assert a%2 != b%2 and tuple(sorted((a,b))) not in owners
        owners[tuple(sorted((a,b)))] = x
        B[a] |= 1<<x
        B[b] |= 1<<x
    return audit_rows(B,owners,width,base,sparse_index=sparse_index)


def sparse_chords(rows, width):
    # For two sparse black rows, a possible horizontal spacing can be tested
    # before allocating and shifting a bitset as wide as the whole board.
    h = len(rows)-1
    reach = 1+(h-1)**2//4
    sparse = [bits.bit_count() <= max(64,width//256) for bits in rows]
    choices = [[set() if x and y else None for y in sparse] for x in sparse]
    points = []
    for y,original in enumerate(rows):
        if not sparse[y]:
            continue
        bits = original
        while bits:
            bit = bits & -bits
            points.append((bit.bit_length()-1,y))
            bits ^= bit
    points.sort()
    for i,(x,a) in enumerate(points):
        choices[a][a].add(0)
        for j in range(i+1,len(points)):
            zx,b = points[j]
            difference = zx-x
            if difference > reach:
                break
            choices[a][b].add(difference)
            if not difference:
                choices[b][a].add(0)

    def possible(a,b,spacing):
        if spacing < 0:
            a,b,spacing = b,a,-spacing
        values = choices[a][b]
        return values is None or spacing in values
    return possible


def audit_rows(B, owners, width, base=0, sparse_index=False):
    h = len(B)-1
    all_columns = (1<<width)-1
    double_sites = sum(1<<x for x in owners.values())
    odd,even = 0,0
    for row in range(1,h+1):
        if row%2:
            odd |= B[row]
        else:
            even |= B[row]
    assert (odd|even) == all_columns and (odd&even) == double_sites
    # The axis-only row-pair graph is simple and bipartite. An axis
    # singleton rival exists at any white point with an opposite-parity
    # black row in its column, using its final owner wherever placed.
    one_visible = [0]*(h+1)
    for row in range(1,h+1):
        one_visible[row] = (even if row%2 else odd) & ~B[row]

    possible = sparse_chords(B,width) if sparse_index else None
    shapes, count = templates(h)
    parked = projections = 0

    def shifted(mask,step):
        return mask >> step if step >= 0 else mask << -step

    for (dx,dy),options in shapes.items():
        if dx >= width:
            continue
        limit = all_columns >> dx
        ymin,ymax = max(1,1-dy),min(h,h-dy)
        seen = [0]*(h+1)
        if dx and dy:
            # This visible pair can be the diagonal of an axis rectangle.
            for y in range(ymin,ymax+1):
                if possible is None or possible(y+dy,y,dx):
                    seen[y] = B[y+dy] & (B[y]>>dx)
        elif dx:
            # At most one row can contain a black pair of given columns,
            # since a second would repeat a double label.
            across = 0
            for y in range(1,h+1):
                if possible is not None and not possible(y,y,dx):
                    continue
                pair = B[y] & (B[y]>>dx)
                assert not across & pair
                seen[y] = pair
                across |= pair
            for y in range(1,h+1):
                seen[y] ^= across
        elif dy%2:
            for y in range(ymin,ymax+1):
                owner = owners.get(tuple(sorted((y,y+dy))))
                seen[y] = limit if owner is None else limit ^ (1<<owner)
        for ax,ay,bx,by,diagonal in options:
            begin,end = max(ymin,1-ay,1-by),min(ymax,h-ay,h-by)
            for y in range(begin,end+1):
                if possible is not None and not possible(y+ay,y+by,bx-ax):
                    continue
                left,right = B[y+ay],B[y+by]
                if not left or not right:
                    continue
                placed = limit & shifted(left,ax) & shifted(right,bx)
                if not placed:
                    continue
                overlap = placed & seen[y]
                if overlap:
                    return ("repeated pair",base+(overlap&-overlap).bit_length()-1,y,dx,dy)
                seen[y] |= placed
                projections += placed.bit_count()
                if diagonal:
                    p,q = B[y], B[y+dy]>>dx
                    hidden = placed & p & q
                    if hidden:
                        return ("hidden",base+(hidden&-hidden).bit_length()-1,y,dx,dy)
                    # Each triple is counted once, using the black corner
                    # opposite its sole white corner.
                    for wy,mask in ((y,placed & q & ~p),(y+dy,(placed & p & ~q)<<dx)):
                        collision = mask & one_visible[wy]
                        if collision:
                            return ("repeated singleton",base+(collision&-collision).bit_length()-1,wy)
                        one_visible[wy] |= mask
                        parked += mask.bit_count()
    return ("pass",h,width,len(owners),count,len(shapes),projections,parked)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate",type=Path)
    parser.add_argument("--sparse-index",action="store_true")
    args = parser.parse_args()
    result = audit(json.loads(args.certificate.read_text()),sparse_index=args.sparse_index)
    print(*result,flush=True)
    if result[0] != "pass":
        raise SystemExit(1)
