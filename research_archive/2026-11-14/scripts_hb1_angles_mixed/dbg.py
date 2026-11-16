import sys
sys.argv=['x']
from angles import *
D = setup(32, 2, 1, 1)
e = set(('cross',)+t for t in enumerate_angles(D))
b = {t for t in brute(D) if t[0]=='cross'}
miss = sorted(b - e)[:5]
S=2
for _, v, p, f, g in miss:
    V = (S*D['slot'][v], D['odd'][v] if p==0 else D['even'][v])
    F = (S*D['slot'][f], D['odd'][f] if p==0 else D['even'][f])
    G = (S*D['slot'][g], D['even'][g] if p==0 else D['odd'][g])
    print(v,p,f,g, V, F, G, 'F-V', (F[0]-V[0], F[1]-V[1]), 'G-V', (G[0]-V[0], G[1]-V[1]))
print(len(e - b))
