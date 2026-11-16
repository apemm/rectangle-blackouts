"""Certify complete infinite-graph components containing the saved R2s cycles.

The census is not extended.  A separate divisor-of-n*delta generator
checks every possible neighbor of the finitely many component vertices.
"""
from math import isqrt
from pathlib import Path
from collections import deque
import json
import time


HERE = Path(__file__).resolve().parent


def primes_to(limit):
    prime = bytearray(b'\x01') * (limit + 1)
    prime[:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if prime[p]:
            prime[p*p::p] = b'\x00' * (((limit-p*p)//p)+1)
    return [p for p in range(2,limit+1) if prime[p]]


def divisors(value, primes):
    result = [1]
    for p in primes:
        if p*p > value:
            break
        if value % p:
            continue
        old = result[:]
        power = 1
        while value % p == 0:
            value //= p
            power *= p
            result.extend(x*power for x in old)
    if value > 1:
        result += [x*value for x in result]
    return result


def pair_witness(n, delta, primes):
    for U in divisors(n*delta, primes):
        T = n*delta // U
        if T % 2:
            continue
        square = U*U-2*n*delta-delta*delta
        if square < 0:
            continue
        root = isqrt(square)
        if root*root != square:
            continue
        for V in {root,-root}:
            if (U+T-V) % 2:
                continue
            X = (U+T-V)//2
            if X <= 0 or X % 4 or U % 4 == 0 or (X+V) % 4 == 0:
                continue
            if delta*delta > 2*X:
                continue
            # These bounds follow from the equations; do not use them
            # to filter the independent pair enumeration.
            assert 0 < T < X < U <= n
            assert delta*delta < 2*n
            A, B = (0,n+1), (U,1)
            C, D = (X,n+delta+1), (X+V,1)
            P, Q = (T//2,n+1+delta//2), (U+T//2,1+delta//2)
            assert len({A,B,C,D,P,Q}) == 6
            assert 1 <= Q[1] < P[1] < C[1]
            assert U*T == n*delta
            assert (C[0]+D[0],C[1]+D[1]) == (P[0]+Q[0],P[1]+Q[1])
            assert (C[0]-D[0])**2+(C[1]-D[1])**2 == (P[0]-Q[0])**2+(P[1]-Q[1])**2
            return (X,U,T,V)
    return None


def neighbors(vertex, primes):
    result = {}
    # Outgoing delta^2 < 2*vertex. Incoming deltas obey the same
    # weaker bound, since their lower endpoint is below vertex.
    for delta in range(4,isqrt(2*vertex)+1,4):
        for lower in (vertex,vertex-delta):
            if lower <= 0:
                continue
            witness = pair_witness(lower,delta,primes)
            if witness is not None:
                other = lower+delta if lower == vertex else lower
                result[other] = dict(n=[lower,lower+delta],XUTV=witness)
    return result


def audit():
    start = time.monotonic()
    source = json.loads((HERE/'r2s_row_pair_graph_262144.json').read_text())
    height = source['n_bound']
    max_product = height * isqrt(2*height)
    primes = primes_to(isqrt(max_product)+1)
    visited = set()
    components = []
    for cycle in source['cycle_blocks']:
        seed = cycle['n'][0]
        if seed in visited:
            continue
        found = {seed}
        todo = deque([seed])
        edges = {}
        while todo:
            vertex = todo.popleft()
            assert vertex + isqrt(2*vertex) < height
            for other, record in neighbors(vertex,primes).items():
                edges[tuple(record['n'])] = record
                if other not in found:
                    found.add(other)
                    todo.append(other)
        visited.update(found)
        contained = [c['n'] for c in source['cycle_blocks'] if set(c['n']) <= found]
        assert len(contained) == 1
        assert len(edges) == len(found)  # connected and unicyclic
        components.append(dict(vertices=sorted(found),
                               edges=[edges[e] for e in sorted(edges)],
                               unique_cycle=contained[0],
                               neighbor_upper_bound=max(v+isqrt(2*v) for v in found)))
    assert len(components) == 7
    return dict(status='PASS', components=components,
                total_vertices=sum(len(c['vertices']) for c in components),
                total_edges=sum(len(c['edges']) for c in components),
                seconds=round(time.monotonic()-start,3),
                scope='Complete components of the positive sea-one R2s row graph, '
                      'with the stated column residues and strong norm gap.')


if __name__ == '__main__':
    result = audit()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'components'}))
