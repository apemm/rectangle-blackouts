"""Exact normalized t=4 certificate; every common outer orientation is tested."""
from itertools import product
from pathlib import Path
import json
from check_aligned_dyadic_quadratic_k4 import strong_templates,BITS
from check_hilbert_quadratic_clique_exclusions import OPTIONS
from check_hilbert_odd_valuation_alignment import terminal


def run(j, epsilon, mask, theta, limit=250000, max_depth=120):
    assert j >= 1 and epsilon in (0,1)
    generator = 1 if theta == 1 else 3
    assert theta == 1 or (theta % 4 == 3 and -(1 << (j+1))+3 <= theta <= (1 << (j+1))-1)
    p=next(p for p in strong_templates() if p['mask']==mask)
    coeff,base=p['coeff'],p['base'];k=7+3*j+2*epsilon
    cur={(*o,0,0,0,*([0]*8),0,0,0) for g in range(4)
         for o in product((g,g^generator),repeat=4)}
    counts=[];ends=[]
    for depth in range(1,max_depth+1):
        nxt=set()
        for node in cur:
            os=node[:4];cr,c1,c2=node[4:7];carry=node[7:15];C,d,cp=node[15:]
            if depth<=k: cb=0
            else:
                s=depth-k;D=d//(1<<epsilon)
                denominator=(C << (j+1))+theta
                target=9*D*D*pow(denominator,-1,1<<s)%(1<<s)
                cb=target>>(s-1)
                assert ((cp>>k)-target)%(1<<(s-1))==0
            for bits in BITS:
                a,b,z,w=bits;rel=a+w-b-z+cr
                if rel%2:continue
                vals=[bits[base[i]]+coeff[i]*cb+carry[i] for i in range(8)]
                pq=[OPTIONS[os[i],vals[2*i]%2,vals[2*i+1]%2] for i in range(4)]
                pp=tuple(v[0] for v in pq);q=tuple(v[1] for v in pq)
                if depth==1 and ((q[1]-q[0])%4!=2 if epsilon else not (q[1]-q[0])%2):continue
                ac=q[0]-2*q[1]+q[2]+c1;bc=q[1]-2*q[2]+q[3]+c2
                if ac%4 or bc%4:continue
                Cn=C+(b-a)*(1<<(depth-1));dn=d+(q[1]-q[0])*(1<<(2*(depth-1)))
                cn=cp+(cb<<(depth-1))
                nxt.add((*pp,rel//2,ac//4,bc//4,*(v//2 for v in vals),Cn,dn,cn))
        cur=nxt;counts.append(len(cur))
        if not cur:
            return dict(j=j,epsilon=epsilon,mask=mask,theta=theta,status='empty',counts=counts,terminals=ends)
        for node in cur:
            if depth<=k or not terminal(node,base):continue
            C,d,c=node[15:];D=d//(1<<epsilon);b=c>>k
            aligned=(b*((C<<(j+1))+theta)-9*D*D)%(1<<(depth+j+1))==0
            divisible=9*D*D%b==0
            ends.append(dict(depth=depth,C=C,d=d,c=c,aligned=aligned,divisible=divisible))
            if aligned and divisible:
                return dict(j=j,epsilon=epsilon,mask=mask,theta=theta,status='aligned candidate',counts=counts,terminals=ends)
        if len(cur)>limit:
            return dict(j=j,epsilon=epsilon,mask=mask,theta=theta,status='memory cutoff',counts=counts,terminals=ends)
    return dict(j=j,epsilon=epsilon,mask=mask,theta=theta,status='depth cutoff',counts=counts,terminals=ends)


def audit():
    results=[]
    cases=[(13,theta) for theta in (1,7,3,-1,-5)]+[(17,theta) for theta in (3,-5)]
    for mask,theta in cases:
        result=run(2,0,mask,theta,limit=500000)
        results.append(result)
        print(mask,theta,result['status'],len(result['counts']),max(result['counts']),len(result['terminals']),flush=True)
        Path(__file__).with_suffix('.json').write_text(json.dumps(results,indent=2)+'\n')
    return results

if __name__=='__main__':
    result=audit()
    assert all(r['status']=='empty' and not r['terminals'] for r in result)
