"""Audit individual singleton insertions in a certified parity core.

With --cut-scale, missing opposite-parity double labels are assigned outside
the retained core interval. Their vertical competitors remain in force.
"""
import argparse
from bisect import bisect_left, bisect_right
from collections import defaultdict
from functools import cache
from math import gcd, isqrt

from core_mixed_witness import from_record


def core_pairs(rows, height):
    xs = sorted(rows)
    bound = 1 + (height - 1) ** 2 // 4
    for i, x in enumerate(xs):
        a, b = rows[x]
        yield (x, a), (x, b)
        for j in range(i + 1, len(xs)):
            xx = xs[j]
            if xx - x > bound:
                break
            for y in (a, b):
                for yy in rows[xx]:
                    yield (x, y), (xx, yy)


def triangle_masks(rows, height, bounds=None):
    xs = sorted(rows)
    lower, upper = (xs[0], xs[-1]) if bounds is None else bounds
    masks = defaultdict(int)

    def forbid(fx, fy, wx, wy):
        if not lower <= fx <= upper or fx in rows:
            return
        if wx not in rows or wy in rows[wx]:
            return
        if 1 <= fy <= height and 1 <= wy <= height:
            masks[fx] |= 1 << fy

    for (x, y), (xx, yy) in core_pairs(rows, height):
        dx, dy = xx - x, yy - y
        # The two true vertices form a side.
        if dx and dy:
            divisor = gcd(dx, dy)
            for sign in (1, -1):
                u, v = -sign * dy // divisor, sign * dx // divisor
                if v > 0:
                    steps = (height - max(y, yy)) // v
                else:
                    steps = (min(y, yy) - 1) // -v
                for k in range(1, steps + 1):
                    forbid(x + k*u, y + k*v, xx + k*u, yy + k*v)
                    forbid(xx + k*u, yy + k*v, x + k*u, y + k*v)

        # If they form a diagonal, look for true columns that can hold its
        # other white endpoint. Horizontal and vertical diagonals count.
        norm = dx*dx + dy*dy
        largest = isqrt(norm)
        rem = max(0, norm - (height - 1)**2)
        smallest = isqrt(rem)
        smallest += smallest**2 < rem
        sum_x, sum_y = x + xx, y + yy
        for first, last in ((-largest, -max(1,smallest)), (smallest,largest)):
            left = bisect_left(xs,(sum_x + first + 1)//2)
            right = bisect_right(xs,(sum_x + last)//2)
            for wx in xs[left:right]:
                fx = sum_x - wx
                if fx in rows or not lower <= fx <= upper:
                    continue
                rem = norm - (2*wx - sum_x)**2
                root = isqrt(rem)
                if root**2 != rem or (sum_y + root) % 2:
                    continue
                for step in (root,-root):
                    wy = (sum_y + step)//2
                    forbid(fx,sum_y - wy,wx,wy)
    return masks


def mixed_masks(rows, height, levels, bounds=None):
    lower, upper = (min(rows), max(rows)) if bounds is None else bounds
    by_row = defaultdict(list)
    for x, ys in rows.items():
        for y in ys:
            by_row[y].append(x)
    masks = defaultdict(int)

    @cache
    def directions(norm):
        # The unknown pair contains a new point and a true point, so its
        # horizontal difference cannot be zero.
        result = set()
        for b in range(min(height - 1,isqrt(norm)) + 1):
            a = isqrt(norm - b*b)
            if a*a + b*b == norm and a > 0:
                for vx in (-a,a):
                    for vy in (-b,b):
                        result.add((vx,vy))
        return tuple(result)

    def forbid(a, b, c, d, new):
        if not lower <= new[0] <= upper or new[0] in rows:
            return
        tx, ty = c[0]+d[0]-a[0]-b[0], c[1]+d[1]-a[1]-b[1]
        if (tx == 0 and ty == 0) or tx % 2 or ty % 2:
            return
        p = a[0] + tx//2, a[1] + ty//2
        q = b[0] + tx//2, b[1] + ty//2
        if not all(lower <= x <= upper and 1 <= y <= height for x,y in (p,q)):
            return
        if len({a,b,p,q}) != 4 or len({c,d,p,q}) != 4 or {a,b} == {c,d}:
            return
        assert (b[0]-a[0])*tx + (b[1]-a[1])*ty == 0
        masks[new[0]] |= 1 << new[1]

    for a, b in core_pairs(rows,height):
        ux, uy = b[0]-a[0], b[1]-a[1]
        sx, sy = a[0]+b[0], a[1]+b[1]
        for vx, vy in directions(ux*ux+uy*uy):
            if ux*vy == uy*vx or (vx-ux)%2 or (vy-uy)%2:
                continue
            for fy in levels:
                cy = fy - vy
                if not 1 <= cy <= height:
                    continue
                # Known pair is the black side. Projection determines cx,
                # except for a vertical side, where it determines cy.
                if ux:
                    num = ux*(sx-vx) + uy*(sy-cy-fy)
                    if num % (2*ux) == 0:
                        cx = num//(2*ux)
                        if cy in rows.get(cx, ()):
                            c, f = (cx,cy), (cx+vx,fy)
                            forbid(a,b,c,f,f)
                elif cy + fy == sy:
                    for cx in by_row[cy]:
                        c, f = (cx,cy), (cx+vx,fy)
                        forbid(a,b,c,f,f)

                # Known pair is the black diagonal.
                num = vx*(sx-vx) + vy*(sy-cy-fy)
                if num % (2*vx) == 0:
                    cx = num//(2*vx)
                    if cy in rows.get(cx, ()):
                        c, f = (cx,cy), (cx+vx,fy)
                        forbid(c,f,a,b,f)
    return masks


def virtual_vertical_masks(rows, height, levels, bounds=None):
    # Owners of missing pairs will be outside this core interval. An owner
    # at the center would coincide with the common side and is excluded.
    retained = {tuple(sorted(ys)): x for x,ys in rows.items()}
    lower, upper = (min(rows), max(rows)) if bounds is None else bounds
    masks = defaultdict(int)
    for x, ys in rows.items():
        for y in ys:
            for fy in levels:
                if (y-fy)%2 == 0:
                    continue
                left, right = sorted((y,fy))
                for j in range(1,min(left-1,height-right)+1):
                    z = j*(right-left+j)
                    d = isqrt(z)
                    if d*d != z:
                        continue
                    pair = left-j, right+j
                    for sign in (-1,1):
                        fx, center = x+2*sign*d, x+sign*d
                        if lower <= fx <= upper and fx not in rows and retained.get(pair) != center:
                            masks[fx] |= 1 << fy
    return masks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--height",type=int,default=127)
    parser.add_argument("--cut-scale",type=int)
    parser.add_argument("--boundary",action="store_true")
    parser.add_argument("--levels",type=int,nargs="+")
    args = parser.parse_args()
    h = args.height
    labels = from_record(h,96,186)
    rows = {}
    for x,a,b in labels:
        scale = 1
        while (a-b) % (3*scale) == 0:
            scale *= 3
        if args.cut_scale is None or scale < args.cut_scale:
            rows[x] = (a,b)
    levels = sorted(set(args.levels)) if args.levels else ([1,h] if args.boundary else list(range(1,h+1)))
    if not levels or levels[0] < 1 or levels[-1] > h:
        parser.error("levels must lie inside the strip")
    tested = sum(1 << k for k in levels)
    angles = triangle_masks(rows,h)
    mixed = mixed_masks(rows,h,levels)
    virtual = virtual_vertical_masks(rows,h,levels) if args.cut_scale is not None else {}
    masks = {x:(angles.get(x,0) | mixed.get(x,0) | virtual.get(x,0)) & tested
             for x in set(angles) | set(mixed) | set(virtual)}
    bad = sorted(x for x in masks if masks[x] == tested)
    print("height",h,"labels",len(rows),"singleton sites with an exclusion",
          sum(bool(v) for v in masks.values()))
    print("complete palette excluded",len(bad),bad[:50],
          "largest number of excluded rows",max(v.bit_count() for v in masks.values()))
    for y in sorted(set(levels) & {1,4,75,113,118,125,h}):
        print("row",y,"angles",sum(v >> y & 1 for v in angles.values()),
              "mixed",sum(v >> y & 1 for v in mixed.values()),
              "virtual vertical",sum(v >> y & 1 for v in virtual.values()),
              "union",sum(v >> y & 1 for v in masks.values()))
    if h == 127 and len(levels) == h:
        for palette in ((1,127),(4,125),(1,118),(1,118,75),(1,118,113)):
            bits = sum(1 << y for y in palette)
            lost = sorted(x for x,v in masks.items() if (v&bits) == bits)
            print("palette",palette,"unavailable sites",len(lost),lost[:20])


if __name__ == "__main__":
    main()

