from seam_shift import bad_pairs, right_ok, left_ok, report, h_by_case
for hm, r0, D0, best in report:
    k, bads, R, L = best
    if bads or k: print("h=%d mod 4, r0=%d, D0=%2d, k=%d, bad(o,kap,j)=%s, right phases=%s, left phases=%s" % (hm, r0, D0, k, bads, R, L))
