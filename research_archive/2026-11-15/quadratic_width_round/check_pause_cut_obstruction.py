"""Sparse exact checks for the Pell two-vector Hilbert cut obstruction."""
from pathlib import Path
import json


def point(n, d):
    x = y = 0
    s = 1
    while s < n:
        rx = (d // 2) & 1
        ry = (d ^ rx) & 1
        if ry == 0:
            if rx:
                x, y = s - 1 - x, s - 1 - y
            x, y = y, x
        x += s * rx
        y += s * ry
        d //= 4
        s *= 2
    return x, y


def rank(n, x, y):
    if n == 1:
        return 0
    s = n // 2
    if x < s and y < s:
        return rank(s, y, x)
    if x < s:
        return s*s + rank(s, x, y-s)
    if y >= s:
        return 2*s*s + rank(s, x-s, y-s)
    return 3*s*s + rank(s, s-1-y, 2*s-1-x)


def crossing(a, d):
    assert 1 <= d <= a*a
    def value(u):
        return point(a, a*a-d+u)[1] - point(a, u)[0]
    lo, hi = 0, d-1
    assert value(lo) >= 0 and value(hi) <= 0
    if value(lo) in (0, 1):
        return a*a-d+lo, lo, value(lo)
    if value(hi) == 0:
        return a*a-d+hi, hi, 0
    while hi-lo > 1:
        mid = (lo+hi)//2
        z = value(mid)
        if z in (0, 1):
            return a*a-d+mid, mid, z
        if z > 0:
            lo = mid
        else:
            hi = mid
    assert value(lo) == 1 and value(hi) == -1
    return a*a-d+lo, lo, 1


def rectangle(v):
    a, b, c, d = v
    return (len(set(v)) == 4
            and a[0]+c[0] == b[0]+d[0]
            and a[1]+c[1] == b[1]+d[1]
            and sum((a[k]-c[k])**2 for k in (0, 1))
            == sum((b[k]-d[k])**2 for k in (0, 1)))


def check(S, extra):
    assert S >= 128 and S & (S-1) == 0
    Z, w = 2, 1
    for _ in range(S.bit_length()-2+extra):
        Z, w = Z*Z+3*w*w, 2*Z*w
    assert Z*Z-3*w*w == 1 and Z % 8 == 1
    X = 3*w
    assert X % S == 0
    q = X//S
    a = 1
    while a*a <= q:
        a *= 2
    assert a*a//4 <= q < a*a and Z > 100*a
    A, B, h = 5*Z+2, 6*Z, 8*Z
    N = 8*a
    while N < 128*Z:
        N *= 4
    I, J = N//4, 3*N//4
    U0, U1 = I-(Z-1)//4, J-(3*Z-1)//2
    R = rank(N, I, J)
    assert R % (4*a*a) == 0
    assert point(N, R) == (I, J)
    cases = []
    for k in sorted({0, 1, q//8, q//3, q//2, q-2, q-1}):
        d = q-k
        t, s, f = crossing(a, d)
        xt, yt = point(a, t)
        xs, ys = point(a, s)
        assert f == yt-xs and f in (0, 1)
        r0, r1 = R+a*a+t, R+2*a*a+s
        left_cell = (I+xt, J+a+yt)
        right_cell = (I+a+xs, J+a+ys)
        assert point(N, r0) == left_cell
        assert point(N, r1) == right_cell
        assert rank(N, *left_cell) == r0
        assert rank(N, *right_cell) == r1
        left = (S*r0, B+4*(a+yt))
        right = (S*(r1+k), A+4*(a+xs))
        assert left[1] % 4 == 2 and right[1] % 4 == 3
        Y, L = Z-2+4*f, 2*Z-1+2*f
        assert right[0]-left[0] == X
        assert left[1]-right[1] == Y
        assert X*X+Y*Y == L*L
        half = (L-Y)//2
        lo, hi = right[1]-half, left[1]+half
        assert 4*Z < lo < hi < 7*Z < h
        assert (left[0]+right[0]) % 2 == 0
        middle = (left[0]+right[0])//2
        if f == 0:
            K = 3*(Z-1)//8
            owner = (I+a+xs+K, J+a+xs-K)
            odd_row, even_row = hi, lo
        else:
            K = (Z-1)//8
            owner = (I+a+xs-K, J+a+xs+1+K)
            odd_row, even_row = lo, hi
        assert odd_row % 4 == 3 and even_row % 4 == 2
        assert odd_row > h//2
        assert U0 <= owner[0] < U0+Z
        assert U1 <= owner[1] < U1+2*Z
        assert 4*Z+3+4*(owner[0]-U0) == odd_row
        assert 2+4*(owner[1]-U1) == even_row
        assert not (I <= owner[0] < I+2*a and J <= owner[1] < J+2*a)
        rr = rank(N, *owner)
        assert point(N, rr) == owner
        assert not R <= rr < R+4*a*a
        cut = R+2*a*a
        ox = S*(rr + (k if rr >= cut else 0))
        assert ox != middle
        P, Q = (middle, lo), (middle, hi)
        O0, O1 = (ox, lo), (ox, hi)
        tilted, axis = (left, P, right, Q), (O0, P, Q, O1)
        assert rectangle(tilted) and rectangle(axis)
        black = {left, right, O0, O1}
        for mask in range(4):
            extended = black | ({P} if mask&1 else set()) | ({Q} if mask&2 else set())
            assert set(tilted)-extended == set(axis)-extended
        cases.append({"pause":k, "original_gap":d, "cross_value":f,
                      "left_local_rank":t, "right_local_rank":s,
                      "owner":owner, "common_rows":[lo,hi]})
    long_cases = []
    left_rank = R+2*a*a-1
    aL, aR, bL = A+4*(a-1), A+4*a, B+4*a
    assert point(N,left_rank) == (I+a-1,J+a)
    for k in (q,q+1,2*q,h//S+1):
        assert k >= q
        pause_rank = left_rank+q
        assert R+2*a*a <= pause_rank < R+2*a*a+k
        for pause_row in (aL,aR,bL):
            if pause_row == aR:
                Y, L, half = Z-2, 2*Z-1, (Z+1)//2
                oddrow, evenrow = aR, bL
                K = 3*(Z-1)//8
                owner = (I+a+K,J+a-K)
                lo,hi = oddrow-half,evenrow+half
            else:
                Y, L, half = Z+2, 2*Z+1, (Z-1)//2
                oddrow,evenrow = aL,bL
                K = (Z-1)//8
                owner = (I+a-1-K,J+a+K)
                lo,hi = oddrow-half,evenrow+half
            first_row = aL if pause_row == bL else bL
            P0,P1 = (S*left_rank,first_row),(S*pause_rank,pause_row)
            assert abs(P0[1]-P1[1]) == Y
            assert X*X+Y*Y == L*L
            assert 4*Z < lo < hi < 7*Z
            assert U0 <= owner[0] < U0+Z
            assert U1 <= owner[1] < U1+2*Z
            owner_odd = 4*Z+3+4*(owner[0]-U0)
            owner_even = 2+4*(owner[1]-U1)
            assert {owner_odd,owner_even} == {lo,hi}
            rr = rank(N,*owner)
            assert point(N,rr) == owner
            assert not R <= rr < R+4*a*a
            ox = S*(rr+(k if rr >= R+2*a*a else 0))
            middle = S*left_rank+X//2
            assert ox != middle
            C0,C1 = (middle,lo),(middle,hi)
            O0,O1 = (ox,lo),(ox,hi)
            tilted,axis = (P0,C0,P1,C1),(O0,C0,C1,O1)
            assert rectangle(tilted) and rectangle(axis)
            black = {P0,P1,O0,O1}
            for mask in range(4):
                extended = black | ({C0} if mask&1 else set()) | ({C1} if mask&2 else set())
                assert set(tilted)-extended == set(axis)-extended
            long_cases.append({"pause":k,"singleton_row":pause_row,
                               "owner":owner,"common_rows":[lo,hi]})
    return {"S":S, "extra_squarings":extra, "Z":Z, "X":X,
            "q":q, "child_side":a, "height":h, "padded_side":N,
            "cases":cases,"long_pause_cases":long_cases}


def main():
    small = 0
    for a in (2,4,8,16,32):
        for d in range(1,a*a+1):
            t,s,f = crossing(a,d)
            assert a*a+s-t == d
            assert point(a,t)[1]-point(a,s)[0] == f
            assert f in (0,1)
            small += 1
    cases = [check(S,e) for S,e in ((128,0),(128,1),(256,0))]
    count = sum(len(z["cases"]) for z in cases)
    long_count = sum(len(z["long_pause_cases"]) for z in cases)
    result = {"status":"PASS", "small_crossings":small,
              "sparse_short_pause_cases":count,"long_pause_filler_cases":long_count,
              "common_corner_colorings":4*(count+long_count),
              "scope":"One cut with frozen ordinary child traversals; all endpoint-pair pause lengths fail; no simultaneous inner-pause theorem.",
              "cases":cases}
    Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="cases"}))


if __name__ == "__main__":
    main()
