"""Search-independent verification of a geometric residue witness, not a P clique."""
from pathlib import Path
import json


def rank(n, x, y):
    if n == 1:
        return 0
    m = n//2
    if x < m and y < m:
        return rank(m, y, x)
    if x < m:
        return m*m+rank(m, x, y-m)
    if y >= m:
        return 2*m*m+rank(m, x-m, y-m)
    return 3*m*m+rank(m, m-1-y, 2*m-1-x)


def point(n, r):
    x = y = 0
    m = 1
    while m < n:
        a, b = (r//2) & 1, (r ^ (r//2)) & 1
        if not b:
            if a:
                x, y = m-1-x, m-1-y
            x, y = y, x
        x, y = x+m*a, y+m*b
        r //= 4
        m *= 2
    return x, y


def check():
    N, b, c = 22, 421, 53888
    points = [(536906, 668149), (953259, 506485),
              (791595, 90132), (1384363, 506485)]
    ranks = [612580740983, 829719411574, 1046858082165, 1263996752756]
    C, D = -231222, 217138670591
    edges = [(1,0), (0,2), (3,0), (2,1), (1,3), (2,3)]
    assert c == 128*b
    assert [rank(1 << N, *p) for p in points] == ranks
    assert [point(1 << N, r) for r in ranks] == points
    assert all(ranks[i+1]-ranks[i] == D for i in range(3))
    assert D % 2
    assert all(points[v][1]-points[u][0]+c*(v-u)**2 == C for u,v in edges)
    difference = b*(2*C+1)-9*D*D
    valuation = (abs(difference) & -abs(difference)).bit_length()-1
    assert valuation == 9
    assert 9*D*D % b == 335
    assert difference % (1 << (N+1)) != 0
    return dict(status='PASS: geometric witness only; norm and full alignment fail',
                N=N, b=b, c=c, C=C, D=D, points=points, ranks=ranks, edges=edges,
                norm_difference=difference, norm_difference_v2=valuation,
                odd_divisibility_remainder=9*D*D % b,
                residues_mod64=dict(b=b % 64, D=D % 64, two_C_plus_one=(2*C+1) % 64))


if __name__ == '__main__':
    result = check()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
