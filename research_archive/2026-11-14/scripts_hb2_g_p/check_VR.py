import math
# exact V_R = #{(q,Y): Y odd in [ylo, yhi], (S q)^2 + Y^2 = L^2, L <= h-1} via T1 (k, e', O)
def VR_exact(S, h, ylo, yhi):
    cnt = 0
    k = 1
    while k * (S * S // 4 + 1) <= h - 1:
        ep = 1
        while k * ((S * ep // 2) ** 2 + 1) <= h - 1:
            E = S * ep // 2
            O = 1
            while k * (E * E + O * O) <= h - 1:
                if math.gcd(ep, O) == 1:
                    Y = k * abs(E * E - O * O)
                    if ylo <= Y <= yhi:
                        cnt += 1
                O += 2
            ep += 1
        k += 2
    return cnt

def VR_bound(S, h, l):
    b_over = 3 * l
    K1 = max(1, (4 * (h - 1)) // (S * S))
    main = (3 * l / S) * (3.87 + 0.71 * max(0.0, math.log(h / (6 * l)))) * (1 + 0.5 * math.log(K1))
    err = (2 * math.sqrt(h) / S) * (1 + math.sqrt(K1))
    return main + err

for (S, h, l) in [(32, 2**16, 2**13), (32, 2**16, 2**11), (32, 2**18, 2**14), (32, 2**18, 2**12),
                  (64, 2**18, 2**14), (16, 2**16, 2**12), (32, 2**20, 2**17), (32, 2**20, 2**15)]:
    v = VR_exact(S, h, l // 2, 3 * l)
    bd = VR_bound(S, h, l)
    v0 = VR_exact(S, h, 1, 3 * l)
    print(S, h, l, "exact", v, "exact(Y>=1)", v0, "bound", round(bd, 1), "ratio", round(v0 / bd, 3),
          " exact*S/l", round(v * S / l, 2))
