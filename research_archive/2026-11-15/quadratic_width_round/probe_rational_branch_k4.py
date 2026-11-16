"""Exact finite-prefix probe; no conclusion from a memory/depth cutoff."""
from itertools import product
from pathlib import Path
import json
from check_aligned_dyadic_quadratic_k4 import strong_templates, BITS
from check_hilbert_quadratic_clique_exclusions import OPTIONS

CASES = ((0, 13), (1, 6))
results = []
for t, mask in CASES:
    temp = next(x for x in strong_templates() if x['mask'] == mask)
    coeff, base = temp['coeff'], temp['base']
    k, first = 7 + 2*t, t//2 + 1
    # Fifteen automaton entries, C prefix, d prefix, c prefix.
    cur = {(*o, 0, 0, 0, *([0]*8), 0, 0, 0)
           for o in product(range(4), repeat=4)}
    maps, counts, total = [], [], 0
    status = 'depth cutoff'
    for depth in range(1, 201):
        nxt = {}
        for node in cur:
            st = node[:15]
            Cd, dd, cp = node[15:]
            os, (cr, c1, c2), carry = st[:4], st[4:7], st[7:]
            if depth <= k:
                cb = 0
            else:
                j = depth-k
                assert dd % (1 << t) == 0
                D = dd//(1 << t)
                modulus = 1 << j
                target = 9*D*D*pow(2*Cd+1, -1, modulus) % modulus
                cb = target >> (j-1)
                # Already chosen lower c bits must agree with the rational branch.
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
                ns = (*pp, rel//2, ac//4, bc//4,
                      *(v//2 for v in vals), newC, newd, newcp)
                nxt.setdefault(ns, (node, bits, q, cb))
        cur = set(nxt)
        maps.append(nxt)
        counts.append(len(cur))
        total += len(cur)
        print('state', t, mask, depth, len(cur), flush=True)
        if not cur:
            status = 'empty'
            break
        for end in cur:
            if depth <= k or any(end[:15]):
                continue
            C, d, c = end[15:]
            D, b = d//(1 << t), c >> k
            if not b or (9*D*D) % b:
                continue
            if (b*(2*C+1)-9*D*D) % (1 << (depth+1)):
                continue
            node, bases, ranks = end, [0]*4, [0]*4
            for level in range(depth-1, -1, -1):
                prev, bits, q, cb = maps[level][node]
                for i in range(4):
                    bases[i] += bits[i] << level
                    ranks[i] += q[i] << (2*level)
                node = prev
            pts = [(bases[base[2*i]]+coeff[2*i]*c,
                    bases[base[2*i+1]]+coeff[2*i+1]*c) for i in range(4)]
            B0 = 9*D*D//b
            result = dict(t=t, mask=mask, depth=depth, b=b, c=c, d=d,
                          D=D, C=C, bases=bases, points=pts, ranks=ranks,
                          B0=B0, T=(B0-1)//2-C)
            results.append(dict(status='aligned candidate', certificate=result))
            Path(__file__).with_suffix('.json').write_text(json.dumps(results, indent=2)+'\n')
            print('ALIGNED', json.dumps(result), flush=True)
            raise SystemExit
        if len(cur) > 100000 or total > 250000:
            status = 'memory cutoff'
            break
    results.append(dict(t=t, mask=mask, status=status, counts=counts))
Path(__file__).with_suffix('.json').write_text(json.dumps(results, indent=2)+'\n')
