"""Cross-checks of rectcore: rectangle counts, verifier agreement, counter agreement."""
import random
from rectcore import *

# rectangle counts: 3x3 -> 10, 3x4 -> 20 (hand-checked values in solver/enumerate.py)
assert len(rects_by_sides(3, 3)) == 10 and len(set(rects_by_sides(3, 3))) == 10
assert len(rects_by_sides(3, 4)) == 20
for h, m in [(4, 4), (5, 7), (8, 8), (9, 6)]:
    rs = rects_by_sides(h, m)
    assert len(rs) == len(set(rs))
    ok, n, k, c = verify_board(h, m, [])
    assert n == len(rs), (h, m, n, len(rs))
    assert verify_plain(h, m, [])[1] == n
print('rectangle counts agree')

rng = random.Random(1)
nvalid = 0
for trial in range(400):
    h, m = rng.choice([(4, 4), (5, 5), (6, 6), (5, 8), (7, 7)])
    k = rng.randint(2, h + m + 2)
    cells = rng.sample(range(h * m), k)
    st = State(h, m, cells)
    s = st.summary()
    b = brute_counts(h, m, cells)
    for key in ('M4', 'M6', 'full_black', 'right_angles_completing_inside'):
        assert s[key] == b[key], (h, m, cells, s, b)
    v1 = verify_board(h, m, cells, full=True)[0]
    v2 = verify_board(h, m, cells, full=False)[0]
    v3 = verify_plain(h, m, cells)[0]
    v4 = b['bad_pairs'] == 0
    v5 = s['M4'] == 0 and s['M6'] == 0 and s['full_black'] <= 1
    assert v1 == v2 == v3 == v4 == v5, (h, m, cells, v1, v2, v3, v4, v5)
    nvalid += v1
    # removal returns the tallies to zero
    for x in cells:
        st.remove(x)
    assert st.tot.sum() == 0 and st.nP.sum() == 0 and st.tp.sum() == 0
print('counters and verifiers agree on 400 random sets,', nvalid, 'valid')
