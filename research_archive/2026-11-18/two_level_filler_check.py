"""Check every two-level singleton sea for the retained height-127 core."""
from collections import defaultdict
from functools import cache
from itertools import combinations
from math import isqrt

from pysat.solvers import Cadical195

from core_mixed_witness import from_record
from one_filler_check import (
    core_pairs, mixed_masks, triangle_masks, virtual_vertical_masks,
)


def pair_implications(rows, h, levels, bounds=None):
    """Two true corners force a condition at the missing corner."""
    xs = sorted(rows)
    xmin, xmax = (xs[0], xs[-1]) if bounds is None else bounds
    lo, hi = levels
    clauses = set()

    def forbid(x, y):
        # Positive chooses hi; negating the event "chooses lo" is positive.
        return x+1 if y == lo else -(x+1)

    def check(a, b, f, w):
        fx, fy = f
        wx, wy = w
        if not all(xmin <= x <= xmax and 1 <= y <= h for x,y in (f,w)):
            return
        corners = {a,b,f,w}
        if len(corners) != 4:
            return
        if len({p[0] for p in corners}) == len({p[1] for p in corners}) == 2:
            return
        if fx in rows and fy not in rows[fx]:
            return
        premise = [] if fx in rows else [forbid(fx,fy)]
        if wx in rows:
            # When w is already black this clause alone does not decide
            # whether the fully black rectangle causes a collision.
            if wy not in rows[wx]:
                clauses.add(tuple(premise))
            return
        for row in levels:
            if (row-wy)%2:
                clauses.add(tuple(premise + [forbid(wx,row)]))

    for a,b in core_pairs(rows,h):
        ax,ay = a
        bx,by = b
        dx,dy = bx-ax,by-ay
        for fy in levels:
            if dx and dy:
                for u,v in ((a,b),(b,a)):
                    step_y = fy-u[1]
                    if step_y and (step_y * dy) % dx == 0:
                        step_x = -step_y*dy//dx
                        check(a,b,(u[0]+step_x,fy),(v[0]+step_x,v[1]+step_y))
            gap_y = 2*fy-ay-by
            rem = dx*dx + dy*dy - gap_y*gap_y
            if rem < 0:
                continue
            root = isqrt(rem)
            if root*root == rem and (ax+bx+root)%2 == 0:
                for sign in (-1,1):
                    fx = (ax+bx+sign*root)//2
                    check(a,b,(fx,fy),(ax+bx-fx,ay+by-fy))
    return clauses


def three_diameter_traps(rows,h):
    """Each trap is independent of the choices at other singleton sites."""
    lower, upper = min(rows), max(rows)

    @cache
    def directions(n):
        result = []
        for g in range(1,h,2):
            if g*g >= n:
                break
            t = isqrt(n-g*g)
            if t*t + g*g == n:
                result.append((t,g))
        return result

    traps = {}
    for a,b in core_pairs(rows,h):
        sx,sy = a[0]+b[0], a[1]+b[1]
        d = (a[0]-b[0])**2 + (a[1]-b[1])**2
        for t,g in directions(d):
            if (sx+t)%2 or (sy+g)%2:
                continue
            x,xx = (sx-t)//2,(sx+t)//2
            lo,hi = (sy-g)//2,(sy+g)//2
            if 1 <= lo < hi <= h and lower <= x < xx <= upper and x not in rows and xx not in rows:
                traps.setdefault((lo,hi),(a,b,x,xx))
    return traps


def main():
    h = 127
    labels = from_record(h,96,186)
    # In this certificate K<sqrt(127) means 27 does not divide the gap.
    rows = {x:(a,b) for x,a,b in labels if (a-b)%27}
    levels = range(1,h+1)
    masks = defaultdict(int)
    for tests in (triangle_masks(rows,h), mixed_masks(rows,h,levels),
                  virtual_vertical_masks(rows,h,levels)):
        for x,mask in tests.items():
            masks[x] |= mask
    sites = defaultdict(list)
    for x, mask in masks.items():
        while mask:
            bit = mask & -mask
            sites[bit.bit_length()-1].append(x)
            mask ^= bit

    survivors = [(lo,hi) for lo,hi in combinations(levels,2)
                 if not any(masks[x] >> hi & 1 for x in sites[lo])]
    print("individually feasible",len(survivors),survivors,flush=True)
    remaining = []
    for lo,hi in survivors:
        with Cadical195() as solver:
            for x in sites[lo]:
                solver.add_clause([x+1])
            for x in sites[hi]:
                solver.add_clause([-(x+1)])
            for clause in pair_implications(rows,h,(lo,hi)):
                solver.add_clause(clause)
            if solver.solve():
                remaining.append((lo,hi))
    print("after parked-corner implications",remaining,flush=True)
    traps = three_diameter_traps(rows,h)
    for pair in remaining:
        print("three-diameter witness",pair,traps.get(pair))
    assert len(survivors) == 22 and remaining == [(2,127)]
    assert all(pair in traps for pair in remaining)
    print("all",h*(h-1)//2,"two-row palettes excluded")


if __name__ == "__main__":
    main()

