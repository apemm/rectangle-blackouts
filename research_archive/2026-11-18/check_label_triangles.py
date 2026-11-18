"""Look for a three-label tilted rectangle that forces a collision for every sea."""
from bisect import bisect_right
from math import gcd
import sys

from check_ternary_placement import columns


def obstruction(h, shear=0, stride=96):
    labels = sorted(columns(h, stride, shear))
    occupied = {x: (a, b) for x, a, b in labels}
    xs = sorted(occupied)
    black = {(x, y) for x, a, b in labels for y in (a, b)}
    demands = {}
    triangles = 0
    for k, x in enumerate(xs):
        for xx in xs[k + 1:bisect_right(xs, x + (h - 1)//2, lo=k + 1)]:
            dx = xx - x
            for y in occupied[x]:
                for yy in occupied[xx]:
                    dy = yy - y
                    if dy == 0:
                        continue
                    g = gcd(dx, abs(dy))
                    px, py = -dy//g, dx//g
                    for vx, vy, wx, wy in ((x, y, xx, yy), (xx, yy, x, y)):
                        for sgn in (-1, 1):
                            step_x, step_y = sgn*px, sgn*py
                            max_step = ((h - max(vy, wy))//step_y if step_y > 0
                                        else (min(vy, wy) - 1)//(-step_y))
                            for length in range(1, max_step + 1):
                                zz, zy = vx + length*step_x, vy + length*step_y
                                fx, fy = wx + length*step_x, wy + length*step_y
                                if (zz, zy) not in black or not xs[0] <= fx <= xs[-1]:
                                    continue
                                # Count a triple once if both legs tie or are short.
                                if (abs(zz-vx), zz, zy) < (abs(wx-vx), wx, wy):
                                    continue
                                triangles += 1
                                rect = ((vx, vy), (wx, wy), (zz, zy), (fx, fy))
                                if fx in occupied:
                                    return 'completion in a double', triangles, rect
                                if fx in demands:
                                    parity, earlier = demands[fx]
                                    if parity != fy % 2:
                                        return 'opposite singleton demands', triangles, (earlier, rect)
                                else:
                                    demands[fx] = fy % 2, rect
    return 'no obstruction of these two types', triangles, len(demands)


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        h = int(arg)
        print(h, obstruction(h), flush=True)
