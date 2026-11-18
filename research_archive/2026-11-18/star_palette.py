"""Compute star colorings for a common dyadic permutation and in-strip integer distances."""
import argparse
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path

import numpy as np
from numba import njit

HERE = Path(__file__).resolve().parent


def leg_table(h):
    legs = [set() for _ in range(h)]
    for u in range(2, isqrt(h-1)+1):
        for v in range(1, u):
            if gcd(u,v) != 1 or (u-v)%2 == 0:
                continue
            hyp = u*u+v*v
            dx, dy = 2*u*v, u*u-v*v
            if dx%8:
                continue
            for k in range(1, (h-1)//hyp+1, 2):
                legs[k*dy].add(k*dx//8)
    offsets = np.array([0]+[len(v) for v in legs], np.int64).cumsum()
    entries = np.array([dx for values in legs for dx in sorted(values)], np.int64)
    return offsets, entries


@njit(cache=False)
def solve_stars(h, perm, offsets, entries):
    n = h//2
    inverse = np.full(len(perm), -1, np.int64)
    for i in range(n):
        inverse[perm[i]] = i
    colors = np.full(((h+1)//2,n), -1, np.int16)
    edge_count = 0
    for star in range((h+1)//2):
        odd = 2*star+1
        off = np.zeros(n+1,np.int64)
        for i in range(n):
            y = abs(2*i+2-odd)
            for t in range(offsets[y],offsets[y+1]):
                for sign in (-1,1):
                    at = perm[i]+sign*entries[t]
                    if 0<=at<len(inverse) and inverse[at]>=0:
                        oi = inverse[at]
                        off[i+1]+=1
                        off[oi+1]+=1
                        edge_count+=1
        off = np.cumsum(off)
        cur = off[:-1].copy()
        adj = np.empty(off[-1], np.int64)
        for i in range(n):
            y = abs(2*i+2-odd)
            for t in range(offsets[y],offsets[y+1]):
                for sign in (-1,1):
                    at = perm[i]+sign*entries[t]
                    if 0<=at<len(inverse) and inverse[at]>=0:
                        oi = inverse[at]
                        adj[cur[i]] = oi
                        adj[cur[oi]] = i
                        cur[i]+=1
                        cur[oi]+=1
        deg = off[1:]-off[:-1]
        order = np.argsort(deg)[::-1]
        forbidden = np.zeros(n+1,np.int64)
        for clock in range(n):
            i = order[clock]
            for t in range(off[i], off[i+1]):
                c = colors[star,adj[t]]
                if c>=0:
                    forbidden[c] = clock+1
            c = 0
            while forbidden[c] == clock+1:
                c+=1
            colors[star,i] = c
        for i in range(n):
            for t in range(off[i],off[i+1]):
                assert colors[star,i] != colors[star,adj[t]]
    return colors,edge_count


def permutation(size, mode):
    if mode == 'linear':
        return np.arange(size, dtype=np.int64)
    if mode == 'wrapped':
        b = (isqrt(2*size)+1)|1
        return np.array([(b*i)%size for i in range(size)],dtype=np.int64)
    # At each binary prefix independently use a reproducible swap of its two children.
    perm = np.zeros(size,dtype=np.int64)
    for bit in range(size.bit_length()-1):
        mask = (1<<bit)-1
        for i in range(size):
            swap = hashlib.blake2s(f'{bit},{i&mask}'.encode()).digest()[0]&1
            perm[i] |= (((i>>bit)&1)^swap)<<bit
    return perm


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('heights', type=int, nargs='+')
    ap.add_argument('--mode', choices=('linear','wrapped','tree'), default='wrapped')
    ap.add_argument('--save', action='store_true')
    args = ap.parse_args()
    for h in args.heights:
        n = h//2
        size = 1<<(n-1).bit_length()
        perm = permutation(size,args.mode)
        assert len(np.unique(perm)) == size
        colors,events = solve_stars(h,perm,*leg_table(h))
        counts = colors.max(axis=1)+1
        base = 1<<(32*h).bit_length()
        width_bound = base*(int(counts.sum())+(h+1)//2)+8*size
        rec = dict(height=h,mode=args.mode,stars=len(counts),palette_histogram=np.bincount(counts).tolist(),
                   max_colors=int(counts.max()),mean_colors=float(counts.mean()),
                   oriented_norm_events=int(events),width_upper_bound=width_bound,
                   color_sha256=hashlib.sha256(colors.astype('<i2', copy=False).tobytes()).hexdigest())
        print(json.dumps(rec),flush=True)
        if args.save:
            with (HERE/f'star_palette_{args.mode}_{h}.json').open('x') as f:
                json.dump(rec,f,indent=2)
                f.write('\n')


if __name__ == '__main__':
    main()
