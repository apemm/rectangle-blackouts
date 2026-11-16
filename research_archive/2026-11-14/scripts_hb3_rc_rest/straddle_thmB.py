# Theorem B configurations: largest m' whose adjacent pairs P_p, P_(p+1) can all be separated by
# lines of the 2^l grid (4^l <= a/M - 1), as any quadtree order requires (straddle lemma).
import math
for (S, M, a) in [(8,1,200001), (8,2,200001), (8,3,200003), (16,1,2000001), (8,1,10**9+1), (32,1,10**12+1)]:
    K = S*S//2
    m = 1
    while ((m)*M*K + 1)**2 < 4*(m*a/M - 2): m += 1      # m-1 = largest n with f(n) < 0
    l = int(math.floor(math.log(a/M - 1, 4)))
    while 4**(l+1) <= a/M - 1: l += 1
    while 4**l > a/M - 1: l -= 1
    g = 2**l
    i0 = (m-1)*M*K
    best = 1
    for mp in range(2, m+1):
        j0 = i0 + (a-1)//2
        ch = (i0 // g) - ((i0 - (mp-1)*M*K) // g) + (j0 // g) - ((j0 - (mp-1)*M*K) // g)
        if mp - 1 <= ch: best = mp
    print("S=%d M=%d a=%d: Theorem B m=%d; quadtree-compatible m' <= %d (bound 68)" % (S, M, a, m, best))
