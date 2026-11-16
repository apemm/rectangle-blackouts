"""Count violated constraints of simple explicit M=3 rules on the block system."""
import sys
import numpy as np
from diag_block import hilbert_array
from diag_fast import build

B, S, M, orient = int(sys.argv[1]), 32, 3, sys.argv[2]
n, E = build(B, S, M, orient)
xy = hilbert_array(B)
if orient == "swap":
    xy = xy[:, ::-1]
i, j = xy[:, 0], xy[:, 1]
r = np.arange(n)


def digsum4(r):
    s = np.zeros_like(r); t = r.copy()
    while t.any():
        s += t & 3; t >>= 2
    return s


def popc(r):
    s = np.zeros_like(r); t = r.copy()
    while t.any():
        s += t & 1; t >>= 1
    return s


rules = {
    "r mod 3": r % 3,
    "floor(r/2) mod 3": (r // 2) % 3,
    "base4 digit sum mod 3": digsum4(r) % 3,
    "popcount(r) mod 3": popc(r) % 3,
    "(i+j) mod 3": (i + j) % 3,
    "(i-j) mod 3": (i - j) % 3,
    "i mod 3": i % 3,
    "all zero": np.zeros(n, dtype=np.int64),
}
rng = np.random.default_rng(1)
rules["uniform random"] = rng.integers(0, 3, n)
print(f"B={B} {orient}: constraints={len(E)}")
for name, xi in rules.items():
    bad = int(np.sum(xi[E[:, 1]] - xi[E[:, 0]] == E[:, 2]))
    print(f"  {name:24s} violated={bad:7d} ({bad/len(E):.3f})")
