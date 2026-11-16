# exponent bookkeeping: theta(a) = (E(a)+1)/(1+a), E(a) = (1+3^a)/2
best = min(((3 + 3**a) / (2 * (1 + a)), a) for a in [i / 100000 for i in range(50000, 150000)])
print("theta* = %.6f at a = %.5f" % best)
t = best[0]
print("y range for H0 = Lambda^y: (%.4f, %.4f]" % (3 * (2 - t), 1.5 * t))
a = 0.91; E = (1 + 3**a) / 2
for x in [1.4967, 1.5]:
    print(x, "old max:", max(x, E + 1 - a * x, 3 - x), " new max (y=2):", max(x, E + 1 - a * x, 4 / 3))
