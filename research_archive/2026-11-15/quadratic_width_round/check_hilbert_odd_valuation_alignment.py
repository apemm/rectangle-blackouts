"""Uniform odd-valuation certificate after common-residue normalization."""
from itertools import product
from collections import deque
from pathlib import Path
import json
from check_aligned_dyadic_quadratic_k4 import strong_templates, advance, BITS
from check_hilbert_quadratic_clique_exclusions import OPTIONS


def step(state, coeff, base, scale_bit):
    out = set()
    for bits in BITS:
        a,b,z,w = bits
        rel = a+w-b-z+state[4]
        if rel % 2:
            continue
        values = [bits[base[i]]+coeff[i]*scale_bit+state[7+i]
                  for i in range(8)]
        pq = [OPTIONS[state[i], values[2*i] % 2, values[2*i+1] % 2]
              for i in range(4)]
        parent = tuple(v[0] for v in pq)
        q = tuple(v[1] for v in pq)
        first = q[0]-2*q[1]+q[2]+state[5]
        second = q[1]-2*q[2]+q[3]+state[6]
        if first % 4 or second % 4:
            continue
        out.add((*parent, rel//2, first//4, second//4,
                 *(v//2 for v in values)))
    return frozenset(out)


def terminal(state, base):
    if len(set(state[:4])) != 1 or any(state[5:7]):
        return False
    shifts = [set() for _ in range(4)]
    for i in range(8):
        shifts[base[i]].add(state[7+i])
    if any(len(v) != 1 for v in shifts):
        return False
    a,b,z,w = [next(iter(v)) for v in shifts]
    return state[4] == a+w-b-z


def audit():
    cases = []
    for template in strong_templates():
        coeff, base = template['coeff'], template['base']
        spreads = [max(c for c,b in zip(coeff,base) if b == i)
                   -min(c for c,b in zip(coeff,base) if b == i)
                   for i in range(4)]
        assert max(spreads) >= 3
        for generator in (1,3):
            initial = frozenset((*o,0,0,0) for g in range(4)
                                for o in product((g,g ^ generator), repeat=4))
            after_first_rank = advance(initial, template['positions'], mode='two')
            # j=1 has k'=12 zero scale bits. The first rank digit
            # has already been read, leaving eleven ordinary steps.
            current = advance(after_first_rank, template['positions'], n=11)
            orbit, seen = [], {}
            while current not in seen:
                seen[current] = len(orbit)
                seed = frozenset((*s,*([0]*8)) for s in current)
                first = frozenset(n for s in seed for n in step(s,coeff,base,1))
                second_bit = int(generator == 3)
                second = frozenset(n for s in first
                                   for n in step(s,coeff,base,second_bit))
                reachable = set(second)
                todo = deque(second)
                while todo:
                    state = todo.popleft()
                    assert not terminal(state,base)
                    for cb in (0,1):
                        for nxt in step(state,coeff,base,cb):
                            if nxt not in reachable:
                                reachable.add(nxt)
                                todo.append(nxt)
                orbit.append(dict(zero_scale_states=sorted(current),
                                  after_first_bit=sorted(first),
                                  after_second_bit=sorted(second),
                                  suffix_states=sorted(reachable)))
                current = advance(current,template['positions'],n=3)
            cases.append(dict(mask=template['mask'], generator=generator,
                              initial_states=sorted(initial),
                              first_rank_states=sorted(after_first_rank),
                              preperiod=seen[current],
                              period=len(orbit)-seen[current], orbit=orbit))
    return dict(status='PASS: every odd t>=3, every odd scale factor', cases=cases)


if __name__ == '__main__':
    result = audit()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'])
    print('Cases:',len(result['cases']))
    print('Largest suffix:',max(len(o['suffix_states']) for c in result['cases'] for o in c['orbit']))
