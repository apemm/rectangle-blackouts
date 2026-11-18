"""A second check of the capped height-127 board, written separately from the main verifier.

It rebuilds the board bytes as assemble_capped_127.py does, compares the hash, and then
uses only those bytes. It checks 3 things.

1. Every column has 1 or 2 black points, the doubles have distinct row pairs, and the
   pair graph is bipartite.
2. No tilted rectangle has 4 black corners.
3. The tilted rectangles with 3 black corners show different white corners, and none
   shows the same white corner as an axis-aligned rectangle with 3 black corners.

This covers every collision in which some rectangle has at most 1 white corner. It does
not cover a collision between 2 rectangles that share 2 white corners, where the shared
pair is a side of one and a diagonal of the other. The main verifier covers that case.

Usage:  python -B research_archive/2026-11-18/check_127_three_black.py
The run takes about 13 minutes.
"""
import hashlib, json, time
from math import gcd

import assemble_compact_127 as board

FILES = ("1_122_1024", "1_124_256", "1_126_256", "2_127_512")
SHA256 = "b1576b8b526428ff89b175143efcd9804c4cb3fffa0daab46f8d8853a6105bfe"


def shapes(h):
    """Tilted rectangles by lowest corner Z, with sides g(a,b) and t(-b,a), gcd(a,b)=1."""
    out = []
    for b in range(1, h):
        for a in range(1, h):
            if gcd(a, b) != 1:
                continue
            g = 1
            while g*b <= h-1:
                t = 1
                while g*b + t*a <= h-1:
                    out.append(((0, 0), (g*a, g*b), (-t*b, t*a), (g*a-t*b, g*b+t*a)))
                    t += 1
                g += 1
    return out


def tilted_heavy(rows, h, m):
    """rows[y] has bit c set when (c, y) is black. Yields (corners, black flags) with 3 or 4 black."""
    for sh in shapes(h):
        low = min(d[0] for d in sh)
        span = max(d[0] for d in sh) - low
        if span > m-1:
            continue
        mask = (1 << (m-span)) - 1
        top = sh[3][1]
        sft = [d[0]-low for d in sh]
        for y in range(1, h-top+1):
            s0 = rows[y] >> sft[0]
            s1 = rows[y+sh[1][1]] >> sft[1]
            s2 = rows[y+sh[2][1]] >> sft[2]
            s3 = rows[y+top] >> sft[3]
            p01 = s0 & s1
            p23 = s2 & s3
            if not (p01 or p23):
                continue
            hit = ((p01 & (s2 | s3)) | (p23 & (s0 | s1))) & mask
            while hit:
                bit = hit & -hit
                hit ^= bit
                x = bit.bit_length()-1
                cs = [(x+sft[i], y+sh[i][1]) for i in range(4)]
                yield cs, [(rows[c[1]] >> c[0]) & 1 for c in cs]


def build():
    recs = [json.loads((board.HERE/f"phase_127_capped_{n}.json").read_text()) for n in FILES]
    raw, old_cuts, _ = board.build(recs)
    pad = board.R+1
    trim = pad-4001
    core = bytearray()
    for i, (left, right) in enumerate(zip([0]+old_cuts, old_cuts+[len(raw)//2])):
        l, r = left+(pad if i == 0 else trim), right-(pad if i == 3 else trim)
        if i == 3:
            core.extend(bytes((1, 0))*405)
            core.extend(bytes((127, 0))*599)
        core.extend(raw[2*l:2*r])
    assert hashlib.sha256(core).hexdigest() == SHA256
    return bytes(core)


def check(core, h):
    m = len(core)//2
    cols = [tuple(sorted(y for y in core[2*i:2*i+2] if y)) for i in range(m)]
    assert all(1 <= len(c) <= 2 for c in cols)
    doubles = [c for c in cols if len(c) == 2]
    pairs = set(doubles)
    assert len(pairs) == len(doubles)
    adj = {}
    for a, b in doubles:
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    side = {}
    for start in adj:
        if start in side:
            continue
        side[start] = 0
        stack = [start]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in side:
                    side[v] = 1-side[u]
                    stack.append(v)
                else:
                    assert side[v] != side[u]
    rows = [0]*(h+2)
    for x, c in enumerate(cols):
        for y in c:
            rows[y] |= 1 << x
    whites = set()
    three = four = 0
    bad = []
    for cs, bl in tilted_heavy(rows, h, m):
        if sum(bl) == 4:
            four += 1
            bad.append(("fully black", cs))
            continue
        three += 1
        w = cs[bl.index(0)]
        if w in whites:
            bad.append(("2 tilted rectangles show only", w))
        whites.add(w)
        for other in cols[w[0]]:
            if tuple(sorted((other, w[1]))) in pairs:
                bad.append(("a tilted and an axis-aligned rectangle show only", w))
    part = sum(side.values())
    return dict(width=m, black=sum(map(len, cols)), doubles=len(doubles),
                parts=sorted((part, len(side)-part)), tilted_three_black=three,
                tilted_four_black=four, collisions=len(bad)), bad


if __name__ == "__main__":
    start = time.time()
    result, bad = check(build(), 127)
    print(result, "seconds", round(time.time()-start))
    print("PASS" if not bad else ("FAIL", bad[:5]))
