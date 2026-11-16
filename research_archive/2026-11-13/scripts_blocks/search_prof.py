from blib import profile_ok, row_ok, Wh
for h in (111, 113, 125, 127, 129):
    best = []
    for L in range(1, 15):
        for g in range(1, 7):
            for H in range(h - 10, h + 1):
                for F in range(L + 1, 40):
                    if profile_ok(h, L, F, H, g):
                        prof = (L, F, H, g)
                        rows = [r for r in range(1, h + 1) if row_ok(h, prof, r)]
                        odd = sum(r % 2 for r in rows); ev = len(rows) - odd
                        best.append((L >= 3 and h - H >= 2, odd * ev, prof, odd, ev))
                        break
    best.sort(key=lambda t: (t[0], t[1]), reverse=True)
    print(h, 'W_h', Wh(h), best[:4])
