"""Find mixed presentations among doubled columns, using a bounded side length."""
from collections import defaultdict
from itertools import combinations
import argparse
import json

import numpy as np
from fiber_translation_search import HERE, Layout


def from_record(h, stride, seed):
    record = json.loads((HERE / f'fiber_search_{h}_{stride}_{seed}.json').read_text())
    layout = Layout(h, stride)
    shifts = {tuple(v[:4]): v[4] for v in record['translations']}
    labels, _ = layout.place(np.array([shifts.get(k, 0) for k in layout.keys]))
    return [(int(x),int(a),int(b)) for x,a,b in labels]


def witness(labels, h, max_leg):
    by_norm = defaultdict(list)
    for i, (x,a,b) in enumerate(labels):
        if b != a and abs(b-a) <= max_leg:
            by_norm[(b-a)**2].append(((x,a),(x,b)))
        j = i+1
        while j < len(labels) and labels[j][0]-x <= max_leg:
            xx, aa, bb = labels[j]
            for y in (a,b):
                for yy in (aa,bb):
                    norm = (xx-x)**2 + (yy-y)**2
                    if norm <= max_leg**2:
                        by_norm[norm].append(((x,y),(xx,yy)))
            j += 1
    xmin, xmax = labels[0][0], labels[-1][0]
    black = {(x,y) for x,a,b in labels for y in (a,b)}
    for norm in sorted(by_norm):
        pairs = by_norm[norm]
        by_direction = defaultdict(list)
        for a,b in pairs:
            u,v = b[0]-a[0],b[1]-a[1]
            if u == 0 and v < 0:
                v = -v
            by_direction[u,v].append((a,b))
        for (u,v), sides in by_direction.items():
            projections = defaultdict(list)
            for other, diags in by_direction.items():
                if other != (u,v):
                    for c,d in diags:
                        key = u*(c[0]+d[0])+v*(c[1]+d[1])
                        projections[key].append((c,d))
            for a,b in sides:
                for c,d in projections.get(u*(a[0]+b[0])+v*(a[1]+b[1]), ()):
                    tx,ty = c[0]+d[0]-a[0]-b[0], c[1]+d[1]-a[1]-b[1]
                    if tx%2 or ty%2 or (tx==0 and ty==0):
                        continue
                    p = a[0]+tx//2, a[1]+ty//2
                    q = b[0]+tx//2, b[1]+ty//2
                    if not all(xmin<=x<=xmax and 1<=y<=h for x,y in (p,q)):
                        continue
                    r1, r2 = {a,b,p,q}, {c,d,p,q}
                    if len(r1)!=4 or len(r2)!=4 or r1==r2:
                        continue
                    assert r1-black == r2-black
                    return dict(side=(a,b),diag=(c,d),common=(p,q), squared_length=norm)
    return None


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('h', type=int)
    p.add_argument('max_leg', type=int)
    p.add_argument('--stride', type=int, default=96)
    p.add_argument('--seed', type=int, default=186)
    args = p.parse_args()
    labels = from_record(args.h, args.stride, args.seed)
    print(json.dumps(witness(labels, args.h, args.max_leg)))
