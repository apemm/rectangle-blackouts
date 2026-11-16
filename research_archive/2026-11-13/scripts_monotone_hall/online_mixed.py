# Sanity check only. Online left-to-right monotone P-free partition, classes may mix offsets.
# Label (i,j), 0<=i<A, 0<=j<K, offset T=2(j-i)+1. Label at slot i with offset T forbids slots i-d, d in S_T
# (full set: 20d^2+4Td+T^2=L^2, 0<L<h). Monotone: j nondecreasing in i, j'-j <= C(i'-i).
import sys, math, time, bisect

def kill_sets(h):
    S = {}
    u = 2
    while u * u + 1 < h:
        for v in range(1, u):
            if (u - v) % 2 == 0 or math.gcd(u, v) != 1:
                continue
            l0 = u * u + v * v
            if l0 >= h:
                break
            g = 1
            while g * l0 < h:
                d0 = g * u * v // 2
                w0 = g * (u * u - v * v)
                for sd in (1, -1):
                    for sw in (1, -1):
                        d = sd * d0
                        T = sw * w0 - 2 * d
                        S.setdefault(T, set()).add(d)
                g += 2
        u += 1
    return S

def brute(h, T):
    out = set()
    for d in range(-h, h + 1):
        if d == 0: continue
        v = 20 * d * d + 4 * T * d + T * T
        L = math.isqrt(v)
        if L * L == v and 0 < L < h:
            out.add(d)
    return out

def run(h, C, mixed, tries=10**9):
    A, K = (h + 1) // 2, h // 2
    S = kill_sets(h)
    # classes: last_i, last_j, occ(set), killed(set), offset (for constant-offset mode)
    last_i, last_j, occ, killed, off = [], [], [], [], []
    for i in range(A):
        used = set()
        for j in range(K):
            T = 2 * (j - i) + 1
            ST = S.get(T, ())
            pos = [d for d in ST if d > 0 and i - d >= 0]
            neg = [-d for d in ST if d < 0 and i - d < A]
            best = -1; bestj = -10**9
            cnt = 0
            for c in range(len(last_i)):
                if c in used: continue
                if mixed:
                    lj = last_j[c]
                    if lj > j or j - lj > C * (i - last_i[c]): continue
                else:
                    if off[c] != T: continue
                if i in killed[c]: continue
                o = occ[c]
                if any((i - d) in o for d in pos): continue
                if last_j[c] > bestj:
                    best = c; bestj = last_j[c]
            if best < 0:
                last_i.append(i); last_j.append(j); occ.append({i}); killed.append(set(i + d for d in neg)); off.append(T)
                used.add(len(last_i) - 1)
            else:
                c = best
                last_i[c] = i; last_j[c] = j; occ[c].add(i); killed[c].update(i + d for d in neg)
                used.add(c)
    return len(last_i)

if __name__ == "__main__":
    h0 = 40
    S = kill_sets(h0)
    for T in range(-h0 + 1, h0, 2):
        assert S.get(T, set()) == brute(h0, T), T
    print("kill sets match brute force at h=40")
    t0 = time.time()
    for h in [int(x) for x in sys.argv[1:]]:
        a = run(h, 70, True)
        b = run(h, 70, False)
        print(h, "mixed", a, round(a / h, 3), "const-offset", b, round(b / h, 3), "t", round(time.time() - t0, 1), flush=True)
