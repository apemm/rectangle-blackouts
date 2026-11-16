"""First-moment prediction of the P witness count in an H7 block: each triple
(X = S q', Y, L), each d in D_M(q'), each role and sign whose residue matches the
block contributes the number of earlier-label rows a with both rows in the bulk
and completion rows in [1, h] (the Hilbert z-offset distribution sums to 1).
usage: py p_first_moment.py h M lo bres"""
import sys, math
import p_h7
from h7common import block
h, M, lo, bres = map(int, sys.argv[1:5]); S = 6272
B = block(h, lo, bres=bres); c = bres - 17
def count_rows(res, Ysg, L):
    # rows y = res mod 28 with y, y+Ysg in [lo, h-lo] and 2y+Ysg in [L+2, 2h-L]
    lo_y = max(lo, lo - Ysg, -(-(L + 2 - Ysg) // 2)); hi_y = min(h - lo, h - lo - Ysg, (2 * h - L - Ysg) // 2)
    if lo_y > hi_y: return 0
    first = lo_y + ((res - lo_y) % 28)
    return 0 if first > hi_y else (hi_y - first) // 28 + 1
W = 0
for qq in range(1, (h - 1) // S + 1):
    tr = p_h7.triples(S * qq, h)
    nd = len({d for d in (qq // M, -(-qq // M)) if d >= 1})
    for Y, L in tr:
        for sg in (1, -1):
            if (sg * Y - c) % 28 == 0:   # role 1: odd(e) row a, even(f) row a + sgY
                W += nd * count_rows(17, sg * Y, L)
            if (sg * Y + c) % 28 == 0:   # role 2: even(e) row b, odd(f) row b + sgY
                W += nd * count_rows(bres, sg * Y, L)
print("h", h, "M", M, "lo", lo, "bres", bres, "predicted witnesses", W, "predicted mean incidence", 2 * W / B["labels"])
