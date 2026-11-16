"""Sparse actual-Hilbert certificate for a twelve-vertex P path."""
from pathlib import Path
import json
from check_four_block_obstruction import point,rank

PATH=[218304,235197,252142,269119,286092,303065,
      320038,337063,354104,371149,388130,405139]


def audit():
    M,n,T=64,128,12669
    h=16*T
    N=524288
    I=J=3*N//8
    base=rank(N,I,J)//(n*n)*(n*n)
    odd0=h//2+3;even0=10
    n0=(h-1-odd0)//4+1
    n1=(h-8-even0)//4+1
    U0=I;U1=J-3*T+2
    larger=max(n0,n1)
    assert 8*larger<=N<16*larger
    assert all(larger<=u<=N-2*larger for u in (U0,U1))
    nodes=[]
    for v in PATH:
        r,u=divmod(v,M)
        i,j=point(n,r)
        assert point(N,base+r)==(I+i,J+j)
        ai=odd0+4*(I+i-U0)
        bi=even0+4*(J+j-U1)
        assert ai==8*T+3+4*i and bi==12*T+2+4*j
        assert 0<=I+i-U0<n0 and 0<=J+j-U1<n1
        assert ai%4==3 and bi%4==2 and h/2<ai<h and 0<bi<h
        nodes.append(dict(local_fine_rank=v,coarse_rank=r,private_offset=u,
                          local_cell=[i,j],global_coarse_rank=base+r,
                          global_fine_rank=M*(base+r)+u,odd=ai,even=bi))
    edges=[]
    for a,b in zip(nodes,nodes[1:]):
        q=b['global_fine_rank']-a['global_fine_rank']
        Y=b['even']-a['odd']
        assert q>0 and Y==3*q and (4*q)**2+Y*Y==(5*q)**2
        assert 5*q<=h-1 and q%2==1
        rows=((a['odd']+b['even']-5*q)//2,
              (a['odd']+b['even']+5*q)//2)
        assert (a['odd']+b['even']-5*q)%2==0
        assert 1<rows[0]<rows[1]<h
        midpoint=2*(a['global_fine_rank']+b['global_fine_rank'])
        assert midpoint%4==2
        edges.append(dict(gap=q,vertical=Y,hypotenuse=5*q,
                          half_factor=q,white_rows=rows,
                          white_column=midpoint))
    return dict(status='PASS',M=M,local_side=n,offset_difference=T,
                height=h,padded_side=N,block_origin=[I,J],block_start=base,
                offsets=[U0,U1],genuine_sizes=[n0,n1],nodes=nodes,edges=edges,
                scope='actual raw folded-profile embedding; good-row filters and Hall failure not certified')


if __name__=='__main__':
    result=audit()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({k:result[k] for k in ['status','M','local_side','height',
                     'padded_side','block_start','scope']}))
