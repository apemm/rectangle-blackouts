# sanity exploration: T2-only (45-degree corner triples, 4th corner in the full board) saturated boards, all balanced partitions
import sys, itertools, time
from f45_T2only import search
h=int(sys.argv[1]); tl=float(sys.argv[2])
k=h//2
parts=[A for A in itertools.combinations(range(1,h+1),k) if not (h%2==0 and 1 not in A)]
t0=time.time()
for A in parts:
    res,best,nodes,el,q=search(h,A,tl/len(parts),1)
    print('h',h,'A',A,'q',q,'saturated T2-only board:', 'FOUND '+' '.join('%d%d'%p for p in res) if res else 'none', '| best depth',best,'nodes',nodes,'sec',round(el,1), '' if el<tl/len(parts)-0.01 or res else 'TIMEOUT')
