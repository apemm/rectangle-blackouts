"""Exact odd-relation DP and greedy deletion certificates for finite P gaps."""
from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache, reduce
import hashlib
import json
import math
from pathlib import Path
import time


def all_gaps(h):
    """Regenerate every absolute finite-diagonal gap by integer triangles."""
    A, K = (h + 1) // 2, h // 2
    gaps = {2*s+1: set() for s in range(-(A-1), K)}
    H = h - 1
    for u in range(2, math.isqrt(H) + 1):
        for v in range(1, u):
            hyp = u*u + v*v
            if hyp > H or (u+v) % 2 == 0 or math.gcd(u, v) != 1:
                continue
            for q in range(1, H//hyp + 1, 2):
                a, b = q*u*v//2, q*(u*u-v*v)
                for d in (a, -a):
                    for vertical in (b, -b):
                        T = vertical - 2*d
                        if T not in gaps:
                            continue
                        s = (T-1)//2
                        n = min(A, K-s) - max(0, -s)
                        if a < n:
                            gaps[T].add(a)
    return {T: tuple(sorted(ds)) for T, ds in gaps.items()}


def degree(k):
    """Least positive integer m with 2*k*sqrt(m) < 2**m."""
    m = 1
    while 4*k*k*m >= 4**m:
        m += 1
    return m


def chunks(limit):
    out, power = [], 1
    while limit:
        take = min(power, limit)
        out.append(take)
        limit -= take
        power *= 2
    return out


@lru_cache(maxsize=100000)
def odd_relation_normalized(ds, m):
    """Return c with dot(c,ds)=0 and odd sum, or None, by exact DP."""
    k = len(ds)
    if not ds or all(d % 2 for d in ds):
        return None
    target = m*sum(ds)
    wanted_parity = (1-m*k) % 2
    mask = (1 << (target+1)) - 1
    even, odd = 1, 0
    before = []
    copies = chunks(2*m)
    for d in ds:
        before.append((even, odd))
        for count in copies:
            shift = count*d
            if count % 2:
                even, odd = ((even | (odd << shift)) & mask,
                             (odd | (even << shift)) & mask)
            else:
                even, odd = ((even | (even << shift)) & mask,
                             (odd | (odd << shift)) & mask)
    if not ((even if wanted_parity == 0 else odd) >> target) & 1:
        return None

    # Reconstruct by whole bounded-count items, preferring coefficient zero.
    coefficients = [0]*k
    left, parity = target, wanted_parity
    order = sorted(range(2*m+1), key=lambda z: (abs(z-m), z))
    for i in range(k-1, -1, -1):
        prev = before[i]
        for z in order:
            residue = left-z*ds[i]
            if residue < 0:
                continue
            new_parity = parity ^ (z % 2)
            if (prev[new_parity] >> residue) & 1:
                coefficients[i] = z-m
                left, parity = residue, new_parity
                break
        else:
            raise AssertionError("DP reconstruction failed")
    assert left == 0 and parity == 0
    assert sum(c*d for c, d in zip(coefficients, ds)) == 0
    assert sum(coefficients) % 2 == 1
    assert max(map(abs, coefficients)) <= m
    return tuple(coefficients)


def odd_relation(ds, m):
    if not ds:
        return None
    g = reduce(math.gcd, ds)
    normalized = tuple(d//g for d in ds)
    return odd_relation_normalized(normalized, m)


def delete_to_good(T, original):
    kept = list(original)
    deleted, witnesses = [], []
    while kept:
        m = degree(len(kept))
        witness = odd_relation(tuple(kept), m)
        if witness is None:
            break
        center = abs(T)//5 if T % 5 == 0 else 0
        if center in kept:
            remove = center
        else:
            remove = min(d for d, c in zip(kept, witness) if c)
        witnesses.append(dict(m=m, relation=[[d, c] for d, c in
                                              zip(kept, witness) if c],
                              removed=remove))
        kept.remove(remove)
        deleted.append(remove)
    m = degree(len(kept))
    assert odd_relation(tuple(kept), m) is None
    return dict(T=T, original=list(original), retained=kept, deleted=deleted,
                m=m, relation_witnesses=witnesses,
                odd_relation_free=True)


def verify_result(result):
    h = result["h"]
    gaps = all_gaps(h)
    assert len(result["diagonals"]) == h-1
    seen, deletions, bound = set(), 0, 0
    for row in result["diagonals"]:
        T = row["T"]
        assert T not in seen
        seen.add(T)
        assert row["original"] == list(gaps[T])
        kept, deleted = set(row["retained"]), set(row["deleted"])
        assert kept.isdisjoint(deleted)
        assert kept | deleted == set(gaps[T])
        assert row["m"] == degree(len(kept))
        assert odd_relation(tuple(sorted(kept)), row["m"]) is None
        current = list(gaps[T])
        for step in row["relation_witnesses"]:
            m = degree(len(current))
            assert m == step["m"]
            rel = step["relation"]
            assert all(d in current and 0 < abs(c) <= m for d, c in rel)
            assert len({d for d, c in rel}) == len(rel)
            assert sum(d*c for d, c in rel) == 0
            assert sum(c for d, c in rel) % 2
            assert step["removed"] in current
            current.remove(step["removed"])
        assert current == row["retained"]
        deletions += len(deleted)
        bound += 1 if not gaps[T] else 4*(len(deleted)+1)
    assert seen == set(gaps)
    assert deletions == result["total_deleted"]
    assert bound == result["product_class_bound"]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--heights", default="128,256,512,1024,2048")
    p.add_argument("--seconds", type=float, default=180)
    p.add_argument("--prefix", default="odd_relation_deletion")
    p.add_argument("--verify")
    args = p.parse_args()
    if args.verify:
        result = json.loads(Path(args.verify).read_text(encoding="utf-8"))
        verify_result(result)
        print(json.dumps(dict(h=result["h"], independent_process_check="PASS",
                              total_deleted=result["total_deleted"])))
        return
    begun = time.monotonic()
    summaries = []
    for h in map(int, args.heights.split(",")):
        start = time.monotonic()
        gaps = all_gaps(h)
        rows = []
        for T, ds in gaps.items():
            if time.monotonic()-begun > args.seconds:
                print(json.dumps(dict(status="wall_cap", h=h,
                                      completed_diagonals=len(rows))), flush=True)
                return
            rows.append(delete_to_good(T, ds))
        deleted = sum(len(row["deleted"]) for row in rows)
        product = sum(1 if not row["original"] else
                      4*(len(row["deleted"])+1) for row in rows)
        result = dict(h=h, method="exact bounded parity DP, greedy deletion",
                      scope="an upper bound, not minimum deletion count",
                      total_gaps=sum(map(len, gaps.values())),
                      total_deleted=deleted, product_class_bound=product,
                      seconds=time.monotonic()-start, diagonals=rows)
        verify_result(result)
        path = Path(f"{args.prefix}_h{h}.json")
        path.write_text(json.dumps(result, separators=(",", ":"))+"\n",
                        encoding="utf-8")
        summary = {k: v for k, v in result.items() if k != "diagonals"}
        summary["certificate"] = path.name
        summary["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        summary["deleted_per_h"] = deleted/h
        summary["classes_per_h"] = product/h
        summary["max_deleted"] = max(len(r["deleted"]) for r in rows)
        summary["deletion_histogram"] = dict(Counter(len(r["deleted"]) for r in rows))
        summaries.append(summary)
        Path(f"{args.prefix}_summary.json").write_text(
            json.dumps(summaries, indent=2)+"\n", encoding="utf-8")
        print(json.dumps(summary), flush=True)


if __name__ == "__main__":
    main()
