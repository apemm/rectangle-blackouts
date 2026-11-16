"""Independent finite check using U | n*delta, not the a,b enumeration."""
from math import isqrt
from pathlib import Path
import json
from probe_r2s_row_pair_graph import enumerate_graph


def signed_norm_enumeration(H):
    supports=set()
    for n in range(1,H):
        for delta in range(4,H-n+1,4):
            value=n*delta
            factors=[]
            for a in range(1,isqrt(value)+1):
                if value%a==0:
                    factors.append(a)
                    if a*a!=value:factors.append(value//a)
            for U in factors:
                if U%4==0:continue
                T=value//U
                if T%2:continue
                square=U*U-2*value-delta*delta
                if square<0:continue
                root=isqrt(square)
                if root*root!=square:continue
                for V in {root,-root}:
                    if (U+T-V)%2:continue
                    X=(U+T-V)//2
                    if X<=0 or X%4 or (X+V)%4==0:continue
                    if delta*delta>2*X:continue
                    supports.add((n,n+delta,X,U,T,V))
    return supports


def main():
    checks=[]
    for H in (64,128,256,512):
        direct=signed_norm_enumeration(H)
        edges,count,_=enumerate_graph(H)
        assert set(edges)=={z[:2] for z in direct}
        assert count==len(direct)
        assert all((u,v,*data) in direct for (u,v),data in edges.items())
        checks.append(dict(n_bound=H,edges=len(edges),supports=count))
    result=dict(status='PASS',method='Independent positive U divisors, all delta up to H-n, both norm-root signs.',checks=checks)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':main()
