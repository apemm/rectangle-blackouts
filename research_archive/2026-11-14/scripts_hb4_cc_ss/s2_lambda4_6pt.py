# (a) Lambda4 pattern count per role structure, by brute force on the geometric
#     definition: A=(0,0), B=(X,Y), C=(m,p), D=(X+n,Y+q) with rows (Y,p,q) fixed.
#     Mixed quadruple: |B-A|=|D-C|, (B-A).(C+D-A-B)=0, D-C != +-(B-A).
#     Unknowns X, m, n each in a window of w=2M-1 consecutive integers (S=1 units).
#     Claim: if |Y(p+q)| > 32 (M-1)^6 then at most 4 solutions.
# (b) 6PT-same: (x,x') with x*xi = -d*m, x'*xi = -d*m' for a common integer xi,
#     x in window W1, x' in window W2 (w values each). Claim: count <= floor((w-1)g/max(|m|,|m'|)) + 1.
import random, math, time
t0 = time.time()
random.seed(12345)

def count_l4(Y, p, q, X0, m0, n0, M):
    r = M - 1
    cnt = 0
    for X in range(X0 - r, X0 + r + 1):
        if X == 0:
            continue
        for m in range(m0 - r, m0 + r + 1):
            for n in range(n0 - r, n0 + r + 1):
                # perpendicular: X(m+n) + Y(p+q) = 0
                if X * (m + n) + Y * (p + q) != 0:
                    continue
                # equal length: |D-C|^2 = |B-A|^2, D-C = (X+n-m, Y+q-p)
                if (X + n - m) ** 2 + (Y + q - p) ** 2 != X * X + Y * Y:
                    continue
                if (X + n - m, Y + q - p) in ((X, Y), (-X, -Y)):
                    continue
                cnt += 1
    return cnt

def circle_points(cx, cy, R2, lim):
    pts = []
    R = int(math.isqrt(R2))
    for u in range(-R, R + 1):
        rem = R2 - u * u
        v = math.isqrt(rem)
        if v * v == rem:
            for vv in {v, -v}:
                pts.append((u + cx, vv + cy))
    return pts

res = {"above": [0, 0], "below": [0, 0]}  # [max count, trials]
for trial in range(4000):
    M = random.choice([2, 3, 4])
    X = random.randint(1, 60) * random.choice([1, -1])
    Y = random.randint(1, 60) * random.choice([1, -1])
    # s = m+n, t = p+q with X s + Y t = 0
    g = math.gcd(X, Y)
    k = random.randint(1, 6) * random.choice([1, -1])
    s, t = k * (-Y // g), k * (X // g)
    # u = n-m, v = q-p on circle (u+X)^2+(v+Y)^2 = X^2+Y^2
    pts = [(a, b) for (a, b) in circle_points(-X, -Y, X * X + Y * Y, 0)]
    pts = [(a, b) for (a, b) in pts if (a, b) != (0, 0) and (a, b) != (-2 * X, -2 * Y)
           and (a - s) % 2 == 0 and (b - t) % 2 == 0]
    if not pts:
        continue
    u, v = random.choice(pts)
    m, n = (s - u) // 2, (s + u) // 2
    p, q = (t - v) // 2, (t + v) // 2
    if p + q == 0:
        continue
    c = count_l4(Y, p, q, X, m, n, M)
    key = "above" if abs(Y * (p + q)) > 32 * (M - 1) ** 6 else "below"
    res[key][0] = max(res[key][0], c)
    res[key][1] += 1
print("Lambda4 brute force:", res)

# (b) 6PT-same line count
viol = 0
maxc = 0
trials = 0
for trial in range(20000):
    M = random.choice([2, 3, 5, 8])
    w = 2 * M - 1
    mm = random.randint(1, 40) * random.choice([1, -1])
    mp = random.randint(1, 40) * (1 if mm > 0 else -1)   # same sign (sea row on one side)
    if mp == mm:
        continue
    d = random.randint(1, 400)
    # plant: choose xi dividing d*m and d*m'
    cands = [xi for xi in range(1, 400) if (d * mm) % xi == 0 and (d * mp) % xi == 0]
    xi = random.choice(cands)
    x0, x0p = -d * mm // xi, -d * mp // xi
    lo1, lo2 = x0 - random.randint(0, w - 1), x0p - random.randint(0, w - 1)
    cnt = 0
    for x in range(lo1, lo1 + w):
        if x == 0 or (d * mm) % x != 0:
            continue
        xi2 = -d * mm // x
        if xi2 == 0 or (d * mp) % xi2 != 0:
            continue
        xp = -d * mp // xi2
        if lo2 <= xp < lo2 + w:
            cnt += 1
    g = math.gcd(mm, mp)
    bound = (w - 1) * g // max(abs(mm), abs(mp)) + 1
    trials += 1
    maxc = max(maxc, cnt)
    if cnt > bound or cnt > M:
        viol += 1
print("6PT-same line count: trials", trials, "max count", maxc, "violations", viol)
print("time %.1f s" % (time.time() - t0))
