"""Bounded structural search for the one exceptional six-gap menu."""
from collections import defaultdict, deque
from pathlib import Path
import json

GAPS = ((20,1),(21,1),(25,0),(33,1),(34,1),(44,2),(45,2),(107,1),(108,1),(116,0))


def solve_period(n, budget=2000):
    masks = defaultdict(lambda: [7, 7, 7])
    for r in range(n):
        for d, gain in GAPS:
            s = (r + d) % n
            if s == r:
                if gain == 0:
                    return {'period': n, 'status': 'UNSAT self-edge', 'nodes': 0}
                continue
            for a in range(3):
                b = (a + gain) % 3
                masks[r,s][a] &= ~(1 << b)
                masks[s,r][b] &= ~(1 << a)
    adjacency = [[] for _ in range(n)]
    for r,s in masks:
        adjacency[r].append(s)
    nodes = 0
    def propagate(dom, queue):
        while queue:
            r,s = queue.popleft()
            new = sum(1 << a for a in range(3)
                      if dom[r] & (1 << a) and masks[r,s][a] & dom[s])
            if not new:
                return False
            if new != dom[r]:
                dom[r] = new
                queue.extend((t,r) for t in adjacency[r] if t != s)
        return True
    def search(dom, queue):
        nonlocal nodes
        nodes += 1
        if nodes > budget:
            raise RuntimeError('budget')
        if not propagate(dom, queue):
            return None
        candidates = [v for v in range(n) if dom[v].bit_count() > 1]
        if not candidates:
            return [d.bit_length()-1 for d in dom]
        r = min(candidates, key=lambda v: (dom[v].bit_count(), -len(adjacency[v])))
        for a in range(3):
            if dom[r] & (1 << a):
                nxt = dom[:]
                nxt[r] = 1 << a
                result = search(nxt, deque((t,r) for t in adjacency[r]))
                if result is not None:
                    return result
        return None
    dom = [7] * n
    dom[0] = 1
    try:
        sol = search(dom, deque(masks))
    except RuntimeError:
        return {'period': n, 'status': 'BUDGET', 'nodes': nodes}
    if sol is not None:
        assert all((sol[(r+d)%n]-sol[r])%3 != g for r in range(n) for d,g in GAPS)
    return {'period':n, 'status':'SAT' if sol else 'UNSAT', 'nodes':nodes,
            'assignment':sol}


results = []
for n in range(1, 97):
    result = solve_period(n)
    results.append(result)
    if result['status'] == 'SAT':
        break
folder = Path(__file__).resolve().parent
(folder/'private_six_gap_periods.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'tested':len(results), 'last':results[-1],
                  'budget_cases':sum(r['status']=='BUDGET' for r in results)}))
