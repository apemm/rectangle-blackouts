"""Integer min-conflicts search. Output is a positive certificate only on zero."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import numpy as np
from numba import njit
from integer_star import pairs, HERE


@njit(cache=False)
def violated(edge, colors, ends, masks):
    a,b = ends[edge]
    return (masks[edge] & (1 << (colors[b]-colors[a]+2))) != 0


@njit(cache=False)
def solve(n, ends, masks, seed, budget):
    np.random.seed(seed)
    offsets = np.zeros(n+1,np.int32)
    for a,b in ends:
        offsets[a+1] += 1
        offsets[b+1] += 1
    offsets = np.cumsum(offsets)
    cursor = offsets[:-1].copy()
    incidence = np.empty(2*len(ends),np.int32)
    for e in range(len(ends)):
        for v in ends[e]:
            incidence[cursor[v]] = e
            cursor[v] += 1
    colors = np.random.randint(0,3,n).astype(np.int8)
    # cost[v,c] counts violated incident pairs if v takes c.
    cost = np.zeros((n,3),np.int32)
    bad = np.empty(len(ends),np.int32)
    pos = np.full(len(ends),-1,np.int32)
    nb = 0
    for e in range(len(ends)):
        a,b = ends[e]
        m = masks[e]
        for c in range(3):
            cost[a,c] += bool(m & (1 << (colors[b]-c+2)))
            cost[b,c] += bool(m & (1 << (c-colors[a]+2)))
        if violated(e,colors,ends,masks):
            bad[nb] = e
            pos[e] = nb
            nb += 1
    best = nb
    for it in range(budget):
        if nb == 0:
            return colors, it, nb, best
        e = bad[np.random.randint(nb)]
        best_score = 1 << 20
        ties = 0
        random_move = np.random.randint(100) < 4
        v = new = -1
        for a in ends[e]:
            for c in range(3):
                if c == colors[a]:
                    continue
                # Only consider moves that repair the selected violation.
                partner = ends[e,0] if a == ends[e,1] else ends[e,1]
                d = c-colors[partner] if a == ends[e,1] else colors[partner]-c
                if masks[e] & (1 << (d+2)):
                    continue
                score = 0 if random_move else cost[a,c]-cost[a,colors[a]]
                if score < best_score:
                    ties = 0
                    best_score = score
                if score == best_score:
                    ties += 1
                    if np.random.randint(ties)==0:
                        v, new = a, c
        if v < 0:
            # Necessary only if both ends require a joint move.
            v = ends[e,np.random.randint(2)]
            new = (colors[v]+1+np.random.randint(2))%3
        old = colors[v]
        colors[v] = new
        for j in range(offsets[v],offsets[v+1]):
            f = incidence[j]
            a,b = ends[f]
            m = masks[f]
            o = b if a==v else a
            for c in range(3):
                d0 = c-old if a==v else old-c
                d1 = c-new if a==v else new-c
                cost[o,c] += int(bool(m & (1 << (d1+2))))-int(bool(m & (1 << (d0+2))))
            hit = violated(f, colors, ends, masks)
            if hit and pos[f] < 0:
                bad[nb]=f
                pos[f]=nb
                nb+=1
            elif not hit and pos[f] >= 0:
                nb-=1
                z = bad[nb]
                bad[pos[f]]=z
                pos[z]=pos[f]
                pos[f]=-1
        best = min(best,nb)
    return colors, budget, nb, best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('side',type=int)
    ap.add_argument('--moves',type=int,default=10000000)
    args = ap.parse_args()
    side = args.side
    edges,masks = pairs(side)
    print(f'Generated {len(edges)} actual constrained pairs',flush=True)
    colors,steps,remaining,best = solve(side**2,edges,masks,123, args.moves)
    for start in range(0,len(edges),1000000):
        e = edges[start:start+1000000]
        ds = colors[e[:,1]]-colors[e[:,0]]+2
        hits = np.count_nonzero(np.bitwise_and(masks[start:start+len(e)],np.left_shift(1,ds)))
        if not remaining:
            assert hits == 0
    out = dict(side=side, choices=3,stride=32,offset=-2*side,seed=123,
               steps=int(steps),final_violations=int(remaining),minimum_seen=int(best))
    if not remaining:
        out['sha256'] = sha256(colors.tobytes()).hexdigest()
        np.savez_compressed(HERE/f'integer_slots_{side}.npz',colors=colors)
    print(json.dumps(out),flush=True)
    (HERE/f'integer_search_{side}.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__ == '__main__':
    main()
