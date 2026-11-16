# Exhaustive residue check of the 3L1F norm lemma (mod 2^K).
# Pair P1 = {label L, filler F}: column diff = 4o (mod 16), row diff F-L:
#   L odd : 8(o+c) (mod 64)
#   L even: 8(o+c) - T0 (mod 32)
# Pair P2 = {L', L''}: column diff = 0 (mod 16), row diff:
#   odd-odd 0 mod 64, even-even 0 mod 32, odd-even  T0 mod 32 (sign irrelevant for squares)
# Parity forces: L odd -> P2 same parity; L even -> P2 mixed.
K = 1024
def sqset(res, mod):
    # all x^2 mod K with x = res (mod mod)
    return {((res + mod*t) ** 2) % K for t in range(K // mod)}
bad = 0
for c in (1, 3):
    for T0 in range(1, 32, 2):
        # SAW* rule: c = 1 iff T = 3 mod 4, c = 3 iff T = 1 mod 4
        if (T0 % 4 == 3) != (c == 1):
            continue
        for o in range(4):
            colF = sqset(4*o, 16)
            col0 = sqset(0, 16)
            # case L odd
            rowF = sqset(8*(o+c) % 64, 64)
            n1 = {(a+b) % K for a in colF for b in rowF}
            for name, rr, mm in (("oo", 0, 64), ("ee", 0, 32)):
                n2 = {(a+b) % K for a in col0 for b in sqset(rr, mm)}
                if n1 & n2:
                    bad += 1; print("SOLVABLE", c, T0, o, "Lodd", name)
            # case L even, partner mixed
            rowF = sqset((8*(o+c) - T0) % 32, 32)
            n1 = {(a+b) % K for a in colF for b in rowF}
            n2 = {(a+b) % K for a in col0 for b in sqset(T0 % 32, 32)}
            if n1 & n2:
                bad += 1; print("SOLVABLE", c, T0, o, "Leven mixed")
print("cases with a solvable norm congruence mod", K, ":", bad)
# control: drop the column-offset coupling (filler column 0 mod 16 always)
ctrl = 0
for c in (1,3):
    for T0 in range(1,32,2):
        if (T0 % 4 == 3) != (c == 1): continue
        for o in range(4):
            colF = sqset(0,16); col0 = sqset(0,16)
            rowF = sqset(8*(o+c) % 64, 64)
            n1 = {(a+b)%K for a in colF for b in rowF}
            n2 = {(a+b)%K for a in col0 for b in sqset(0,64)}
            if n1 & n2: ctrl += 1
print("control (coupling removed), solvable cases:", ctrl)
