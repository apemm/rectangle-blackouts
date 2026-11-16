"""Finite invariant check for lifting affine reverse-section embeddings.

Each path state retains its lowest source-rank digit. This permits exact
testing of a noncanonical next base-four digit of the affine multiplier.
"""
from itertools import product
import json
from pathlib import Path

REV = {
    (0,0): ((1,0),(0,2)), (0,1): ((2,0),(3,3)),
    (1,0): ((2,1),(3,2)), (1,1): ((1,1),(0,3)),
    (2,0): ((0,0),(3,1)), (2,1): ((1,2),(2,2)),
    (3,0): ((1,3),(2,3)), (3,1): ((3,0),(0,1)),
}


def step(states, a, b, bit, digit, lift=0, initialize=False):
    # A nonzero lift is only an existence test at the new final digit.
    # Its carry is deliberately neither constructed nor propagated.
    target = set()
    inv = pow(b, -1, 4)
    for left, right, carry, low_digit in states:
        allowed = dict(REV[right, bit])
        for d1, p1 in REV[left, bit]:
            d2 = ((a*d1-digit+carry+b*lift*low_digit)*inv) % 4
            if d2 not in allowed:
                return None
            p2 = allowed[d2]
            if lift == 0:
                nc = (a*d1-b*d2-digit+carry)//4
                assert -b <= nc < a
                target.add((p1,p2,nc,d1 if initialize else low_digit))
    return True if lift else frozenset(target)


def analyze(a, b):
    controls = list(product(range(2), range(4)))
    first = set()
    for left, right in product(range(4), repeat=2):
        for bit, digit in controls:
            result = step({(left,right,0,0)}, a,b,bit,digit, initialize=True)
            if result is not None:
                first.add(result)
    starts = set()
    for state in first:
        for bit, digit in controls:
            result = step(state,a,b,bit,digit)
            if result is not None:
                starts.add(result)

    states = list(starts)
    seen = set(starts)
    cursor = 0
    edges = 0
    tests = 0
    while cursor < len(states):
        state = states[cursor]
        for bit, digit in controls:
            for lift in (1,2,3):
                tests += 1
                alternative = step(state,a,b,bit,digit,lift=lift)
                if alternative is not None:
                    return dict(a=a,b=b,status='NONCANONICAL_LIFT',
                                states=[list(x) for x in sorted(state)],
                                control=[bit,digit],lift=lift,
                                reached_nodes=len(states))
            result = step(state,a,b,bit,digit)
            if result is not None:
                edges += 1
                if result not in seen:
                    seen.add(result)
                    states.append(result)
        cursor += 1
    return dict(a=a,b=b,status='PASS',initial_two_digit_states=len(starts),
                invariant_nodes=len(states),canonical_edges=edges,
                forbidden_lift_tests=tests,
                maximum_node_size=max(map(len,states), default=0),
                certificate_nodes=[[list(x) for x in sorted(node)]
                                   for node in sorted(states,key=lambda z: tuple(sorted(z)))])


def section(child, bits):
    current = [(0,child)]
    for place, bit in enumerate(bits):
        current = [(rank+digit*4**place,parent) for rank,state in current
                   for digit,parent in REV[state,bit]]
    return frozenset(rank for rank,_ in current)


def base_case():
    ratios = set()
    for bits in product(range(2), repeat=2):
        sections = [section(state,bits) for state in range(4)]
        for source,target in product(sections,repeat=2):
            for multiplier in range(1,16,2):
                for translation in range(16):
                    if frozenset((multiplier*x+translation)%16 for x in source)==target:
                        ratios.add(multiplier)
    assert ratios == {1,3,5,11,13,15}
    return sorted(ratios)


def main():
    result = dict(base_modulus=16,base_ratios=base_case(),
                  lifting=[analyze(a,b) for a,b in ((1,1),(5,1),(1,5))])
    certificate=Path(__file__).with_name('hilbert_affine_lifting_certificate.json')
    certificate.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for item in result['lifting']:
        item.pop('certificate_nodes',None)
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':
    main()
