"""Small exact positive-delta R2s census; not an asymptotic proof."""
from math import isqrt
import json
from pathlib import Path


def divisors(n):
    lo, hi = [], []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            lo.append(d)
            if d * d != n:
                hi.append(n // d)
    return lo + hi[::-1]


def find_support(n):
    # Every positive-delta support has d<=4sqrt(n), or the d=4 seam.
    for d in range(4, 4 * isqrt(n) + 5, 4):
        for u in divisors(n * d):
            if u % 4 == 0:
                continue
            t = n * d // u
            if t % 2:
                continue
            v2 = u * u - 2 * n * d - d * d
            if v2 < 0:
                continue
            v = isqrt(v2)
            if v * v != v2:
                continue
            # Simultaneous horizontal reflection permits u>0.
            for vs in {v, -v}:
                twice_x = u + t - vs
                if twice_x % 8:
                    continue
                x = twice_x // 2
                if not x:
                    continue
                if d * d <= 2 * abs(x) or abs(x) == d == 4:
                    return {"d": d, "u": u, "t": t, "v": vs, "x": x}
    return None


def main():
    bound = 2048
    bad = {n: w for n in range(1, bound + 1) if (w := find_support(n))}
    square_bad = {n: w for n, w in bad.items() if isqrt(n) ** 2 == n}
    cube_bad = {n: w for n, w in bad.items() if any(k ** 3 == n for k in range(1, 14))}
    runs = []
    start = None
    for n in range(1, bound + 2):
        if n in bad and start is None:
            start = n
        elif n not in bad and start is not None:
            runs.append([start, n - 1])
            start = None
    result = {"bound": bound, "bad_count": len(bad), "bad": bad,
              "bad_squares": square_bad, "bad_cubes": cube_bad,
              "max_run": max((v - u + 1 for u, v in runs), default=0),
              "runs": runs, "scope": "Exact positive-delta algebraic candidate superset; strip height and full board omitted."}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ('bound', 'bad_count', 'bad_squares', 'bad_cubes', 'max_run')}))


if __name__ == '__main__':
    main()
