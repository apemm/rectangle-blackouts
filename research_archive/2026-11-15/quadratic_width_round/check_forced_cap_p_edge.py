"""Sparse exact certificate for a forced P edge after the actual cap repair."""
from pathlib import Path
import json
from check_four_block_obstruction import point, rank, rectangle


def check():
    h, n, N, S = 65536, 32768, 131072, 96
    offsets = (15840, 17120)
    bad = (16976, 15695)
    assert 4*n <= N < 8*n
    assert all(1 <= u <= N-n-1 for u in offsets)
    assert all(0 < v < n-1 for v in bad)

    def clipped(r):
        p = point(N, r)
        return tuple(min(n-1, max(0, p[a]-offsets[a])) for a in (0, 1))

    crossing = tuple(offsets[a]+bad[a] for a in (0, 1))
    crossing_rank = rank(N, *crossing)
    # Each bad value is interior, so its preimage under clipping is one
    # coordinate line. There is exactly one doubly bad rank.
    assert clipped(crossing_rank) == bad
    length = 1
    ancestors = []
    while True:
        start = crossing_rank // length * length
        p, q = point(N, start), point(N, start+length-1)
        role = 0 if p[0] == q[0] else 1
        assert p[role] == q[role]
        value = clipped(start)[role]
        good = value != bad[role]
        ancestors.append(dict(start=start, length=length, role=role,
                              value=value, good=good, endpoints=[p, q]))
        if good:
            cap = (start, length, role, value)
            break
        length *= 4
    assert cap == (2147486548, 4, 0, 16977)

    def virtual(r):
        v = list(clipped(r))
        if cap[0] <= r < cap[0]+cap[1]:
            v[cap[2]] = cap[3]
        options = {a: v[a] for a in (0, 1) if v[a] != bad[a]}
        return v, options

    block = 2147485696
    assert point(N, block) == (32800, 32800)
    source, target = block+192, block+597
    assert point(N, source) == (32807, 32815)
    assert point(N, target) == (32816, 32831)
    sv, so = virtual(source)
    tv, to = virtual(target)
    assert sv == [16967, 15695] and so == {0: 16967}
    assert tv == [16976, 15711] and to == {1: 15711}
    source_row, target_row = 2*so[0]+1, 2*to[1]+2
    assert (source_row, target_row) == (33935, 31424)
    X, Y, L = S*(target-source), abs(target_row-source_row), 38961
    assert (X, Y, L) == (38880, 2511, 38961)
    assert X*X+Y*Y == L*L
    low = (source_row+target_row-L)//2
    high = (source_row+target_row+L)//2
    assert (low, high) == (13199, 52160)
    assert 1 < low < high < h

    owner = ((low-1)//2, high//2-1)
    assert owner == (6599, 26079)
    raw_owner = tuple(owner[a]+offsets[a] for a in (0, 1))
    owner_rank = rank(N, *raw_owner)
    assert owner_rank == 3721733056
    ov, oo = virtual(owner_rank)
    assert ov == list(owner) and oo == dict(enumerate(owner))
    assert not cap[0] <= owner_rank < cap[0]+cap[1]
    assert all(0 <= owner[a] < n and owner[a] != bad[a] for a in (0, 1))

    xa, xb, xo = S*source, S*target, S*owner_rank
    xm = (xa+xb)//2
    assert xm % S == S//2
    A, B = (xa, source_row), (xb, target_row)
    P, Q = (xm, low), (xm, high)
    U, V = (xo, low), (xo, high)
    tilted, axis = (A, P, B, Q), (U, P, Q, V)
    assert rectangle(tilted) and rectangle(axis)
    black = {A, B, U, V}
    assert set(tilted)-black == set(axis)-black == {P, Q}
    # Common-point occupancy cannot repair a collision whose entire
    # symmetric difference is black. Check all four common-point choices.
    for mask in range(4):
        extra = {z for k, z in enumerate((P, Q)) if mask & (1 << k)}
        assert set(tilted)-(black | extra) == set(axis)-(black | extra)

    return dict(status="PASS", height=h, row_class_size=n, padded_side=N,
                stride=S, offsets=offsets, bad_indices=bad,
                bad_physical_rows=[2*bad[0]+1, 2*bad[1]+2],
                crossing=crossing, crossing_rank=crossing_rank,
                first_good_ancestors=ancestors, selected_cap=cap,
                block_start=block, source_rank=source, target_rank=target,
                source_options=so, target_options=to,
                source_row=source_row, target_row=target_row,
                norm=[X, Y, L], common_rows=[low, high],
                owner_indices=owner, owner_raw=raw_owner,
                owner_rank=owner_rank, common_occupancy_cases=4,
                scope="Two arbitrary bad rows and fixed admissible offsets; "
                      "not the actual R2s bad set, all offsets, or block permutations.")


if __name__ == "__main__":
    result = check()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: result[k] for k in
                     ("status", "height", "selected_cap", "norm", "scope")}))
