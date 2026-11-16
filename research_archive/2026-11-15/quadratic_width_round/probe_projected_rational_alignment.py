"""Finite-register overgraph. Acceptance is not an aligned certificate."""
from itertools import product
from collections import deque
from check_aligned_dyadic_quadratic_k4 import strong_templates, BITS
from check_hilbert_quadratic_clique_exclusions import OPTIONS


def terminal(node, base):
    if any(node[:4]) or any(node[5:7]):
        return False
    shifts = [set() for _ in range(4)]
    for i in range(8):
        shifts[base[i]].add(node[7+i])
    if any(len(v) != 1 for v in shifts):
        return False
    a,b,z,w = [next(iter(v)) for v in shifts]
    return node[4] == a+w-b-z


def run(t, mask, J, limit=200000):
    p = next(x for x in strong_templates() if x['mask'] == mask)
    coeff, base = p['coeff'], p['base']
    k, first, modulus = 7+2*t, t//2+1, 1 << J
    cur = {(*o,0,0,0,*([0]*8),0,0) for o in product(range(4),repeat=4)}
    def successors(node, depth, cb):
        os=node[:4]; cr,c1,c2=node[4:7]; carry=node[7:15]; C,D=node[15:]
        for bits in BITS:
            a,b,z,w=bits
            rel=a+w-b-z+cr
            if rel%2: continue
            vals=[bits[base[i]]+coeff[i]*cb+carry[i] for i in range(8)]
            xy=[v%2 for v in vals]
            pq=[OPTIONS[os[i],xy[2*i],xy[2*i+1]] for i in range(4)]
            pp=tuple(v[0] for v in pq); q=tuple(v[1] for v in pq)
            if depth<first and q[1]!=q[0]: continue
            if depth==first and ((q[1]-q[0])%4!=2 if t%2 else not (q[1]-q[0])%2): continue
            ac=q[0]-2*q[1]+q[2]+c1; bc=q[1]-2*q[2]+q[3]+c2
            if ac%4 or bc%4: continue
            Cn=(C+((b-a) << (depth-1)))%modulus if depth<=J else C
            if depth<first: Dn=D
            elif 2*(depth-1)<t: Dn=(D+(q[1]-q[0])//2)%modulus
            elif 2*(depth-1)-t<J: Dn=(D+((q[1]-q[0]) << (2*(depth-1)-t)))%modulus
            else: Dn=D
            yield (*pp,rel//2,ac//4,bc//4,*(v//2 for v in vals),Cn,Dn)
    counts=[]
    for depth in range(1,k+J+1):
        nxt=set()
        for node in cur:
            C,D=node[15:]
            if depth<=k: cb=0
            else:
                j=depth-k
                target=9*D*D*pow(2*C+1,-1,1<<j)%(1<<j)
                cb=target>>(j-1)
            nxt.update(successors(node,depth,cb))
        cur=nxt; counts.append(len(cur))
        if not cur: return dict(status='empty prefix',t=t,mask=mask,J=J,counts=counts)
        if depth>k and any(terminal(v,base) for v in cur):
            return dict(status='accepted projected prefix',t=t,mask=mask,J=J,counts=counts)
        if len(cur)>limit: return dict(status='memory cutoff',t=t,mask=mask,J=J,counts=counts)
    seen=set(cur); todo=deque(cur)
    while todo:
        node=todo.popleft()
        for cb in (0,1):
            for nxt in successors(node,k+J+1,cb):
                if terminal(nxt,base):
                    return dict(status='accepted projected suffix',t=t,mask=mask,J=J,counts=counts,visited=len(seen))
                if nxt not in seen:
                    seen.add(nxt);todo.append(nxt)
        if len(seen)>limit:
            return dict(status='memory cutoff',t=t,mask=mask,J=J,counts=counts,visited=len(seen))
    return dict(status='closed without acceptance',t=t,mask=mask,J=J,counts=counts,visited=len(seen))


if __name__=='__main__':
    for J in (10,12,16):
        for t,mask in ((0,13),(1,6),(2,13)):
            print(run(t,mask,J),flush=True)
