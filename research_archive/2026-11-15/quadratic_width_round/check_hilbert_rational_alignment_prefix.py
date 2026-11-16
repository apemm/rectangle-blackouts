"""Finite exact prefix certificate for selected K4 orientation/valuation cases.

No prefix exhaustion means no theorem: status is explicit in every case.
The transition table can be replaced for an independent audit.
"""
from itertools import product
from pathlib import Path
import json
from check_aligned_dyadic_quadratic_k4 import strong_templates, BITS
from check_hilbert_quadratic_clique_exclusions import OPTIONS


def run(t, mask, max_depth=200, max_states=500000):
    template = next(x for x in strong_templates() if x['mask'] == mask)
    coeff, base = template['coeff'], template['base']
    k, first = 7 + 2*t, t//2 + 1
    cur = {(*o, 0, 0, 0, *([0]*8), 0, 0, 0)
           for o in product(range(4), repeat=4)}
    counts, canonical = [], []
    for depth in range(1, max_depth+1):
        nxt = set()
        for node in cur:
            os = node[:4]
            cr, c1, c2 = node[4:7]
            carry = node[7:15]
            Cd, dd, cp = node[15:]
            if depth <= k:
                cb = 0
            else:
                j = depth-k
                assert dd % (1 << t) == 0
                D = dd//(1 << t)
                target = 9*D*D*pow(2*Cd+1, -1, 1 << j) % (1 << j)
                cb = target >> (j-1)
                assert ((cp >> k)-target) % (1 << (j-1)) == 0
            for bits in BITS:
                aa, bb, z, w = bits
                rel = aa+w-bb-z+cr
                if rel % 2:
                    continue
                vals = [bits[base[i]]+coeff[i]*cb+carry[i] for i in range(8)]
                xy = [v % 2 for v in vals]
                pq = [OPTIONS[os[i], xy[2*i], xy[2*i+1]] for i in range(4)]
                pp, q = tuple(v[0] for v in pq), tuple(v[1] for v in pq)
                delta = (q[1]-q[0]) % 4
                if depth < first and delta:
                    continue
                if depth == first and (delta != 2 if t % 2 else not delta % 2):
                    continue
                ac, bc = q[0]-2*q[1]+q[2]+c1, q[1]-2*q[2]+q[3]+c2
                if ac % 4 or bc % 4:
                    continue
                newC = Cd+(bb-aa)*(1 << (depth-1))
                newd = dd+(q[1]-q[0])*(1 << (2*(depth-1)))
                newcp = cp+(cb << (depth-1))
                nxt.add((*pp, rel//2, ac//4, bc//4,
                         *(v//2 for v in vals), newC, newd, newcp))
        cur = nxt
        counts.append(len(cur))
        if not cur:
            return dict(t=t, mask=mask, status='empty', counts=counts,
                        canonical_states=canonical)
        for node in cur:
            if depth <= k or len(set(node[:4])) != 1 or any(node[5:7]):
                continue
            # Potential bases can be negative even though all coordinates
            # lie in the finite square.  Each final coordinate carry must
            # equal the same integer for every use of its base.  Subtracting
            # that integer times 2**depth from the base residue restores
            # the actual signed base.
            shifts = [set() for _ in range(4)]
            for i in range(8):
                shifts[base[i]].add(node[7+i])
            if any(len(values) != 1 for values in shifts):
                continue
            ka, kb, kz, kw = [next(iter(values)) for values in shifts]
            if node[4] != ka+kw-kb-kz:
                continue
            C, d, c = node[15:]
            D, b = d//(1 << t), c >> k
            congruent = (b*(2*C+1)-9*D*D) % (1 << (depth+1)) == 0
            divisible = b > 0 and 9*D*D % b == 0
            canonical.append(dict(depth=depth, C=C, d=d, c=c, b=b,
                                  base_shifts=[ka,kb,kz,kw],
                                  congruent=congruent, divisible=divisible))
            if congruent and divisible:
                return dict(t=t, mask=mask, status='aligned candidate',
                            counts=counts, canonical_states=canonical)
        if len(cur) > max_states:
            return dict(t=t, mask=mask, status='memory cutoff', counts=counts,
                        canonical_states=canonical)
    return dict(t=t, mask=mask, status='depth cutoff', counts=counts,
                canonical_states=canonical)


def audit():
    results = []
    for t in range(4):
        for temp in strong_templates():
            result = run(t, temp['mask'])
            results.append(result)
            print(t, temp['mask'], result['status'], len(result['counts']),
                  max(result['counts']), len(result['canonical_states']), flush=True)
    return dict(description='Exact prefix exhaustion; only empty cases are exclusions',
                cases=results)


if __name__ == '__main__':
    result = audit()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
