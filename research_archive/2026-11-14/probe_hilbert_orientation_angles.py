"""Bounded search for three-black angles within one leaf-orientation class."""
import argparse
import json
from collections import defaultdict
from functools import lru_cache


@lru_cache(None)
def point_orientation(side, rank):
    if side == 1:
        return 0, 0, 0, 0
    n = side//2
    digit, offset = divmod(rank, n*n)
    x, y, swap, negative = point_orientation(n, offset)
    if digit == 0:
        return y, x, swap ^ 1, negative
    if digit == 1:
        return x, y+n, swap, negative
    if digit == 2:
        return x+n, y+n, swap, negative
    return 2*n-1-y, n-1-x, swap ^ 1, negative ^ 1


def probe(stride, half_side, radius, modulus=1):
    side = 2*half_side
    center = 2*half_side*half_side
    early = [(r, point_orientation(side, r)) for r in range(radius)]
    late = [(r, point_orientation(side, r))
            for r in range(center-radius, center+radius)]
    grouped = defaultdict(list)
    for rc, pc in late:
        ic, jc, oc1, oc2 = pc
        grouped[(oc1, oc2, rc % modulus, ic % modulus, jc % modulus)].append((rc, pc))
    tested = 0
    past = defaultdict(list)
    for rb, (ib, jb, ob1, ob2) in early:
        key = (ob1, ob2, rb % modulus, ib % modulus, jb % modulus)
        for ra, (ia, ja, oa1, oa2) in past[key]:
            p = rb-ra
            candidates = grouped[(oa1, oa2, ra % modulus, ia % modulus, ja % modulus)]
            for rc, (ic, jc, oc1, oc2) in candidates:
                if jc <= jb:
                    continue
                tested += 1
                value, remainder = divmod(stride*stride*p*(rc-rb), 2*(jc-jb))
                if remainder or value % 2 != 1:
                    continue
                origin_difference = (value+1)//2-ia+jb
                if origin_difference > 0 and origin_difference % side == 0:
                    return dict(stride=stride, local_side=side,
                                local_ranks=[ra, rb, rc],
                                points=[point_orientation(side, r) for r in (ra, rb, rc)],
                                origin_difference=origin_difference, tested=tested)
        past[key].append((rb, (ib, jb, ob1, ob2)))
    return dict(stride=stride, local_side=side, tested=tested, found=False)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--stride", type=int, default=32)
    p.add_argument("--radius", type=int, default=128)
    p.add_argument("--modulus", type=int, default=1)
    p.add_argument("--exponents", type=int, nargs="+", default=[8, 9, 10])
    args = p.parse_args()
    for e in args.exponents:
        result = probe(args.stride, 2**e, args.radius, args.modulus)
        print(json.dumps(result), flush=True)
        if result.get("found") is not False:
            break
