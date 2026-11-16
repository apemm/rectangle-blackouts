"""Bounded-register overgraph for normalized diagonal branches."""
from itertools import product
from collections import deque
from check_aligned_dyadic_quadratic_k4 import strong_templates,BITS
from check_hilbert_quadratic_clique_exclusions import OPTIONS
from check_hilbert_odd_valuation_alignment import step,terminal


def seed(j,mask=13,J=8):
    p=next(p for p in strong_templates() if p['mask']==mask)
    Dmod=1<<J; Cmod=1<<max(0,J-j-1)
    states={(*o,0,0,0,0,0) for g in range(4) for o in product((g,g^1),repeat=4)}
    for depth in range(1,8+3*j):
        nxt=set()
        for state in states:
            o=state[:4];cr,c1,c2,C,D=state[4:]
            for bits in BITS:
                a,b,z,w=bits;rel=a+w-b-z+cr
                if rel%2:continue
                xy=[bits[p['base'][i]] for i in range(8)]
                pq=[OPTIONS[o[i],xy[2*i],xy[2*i+1]] for i in range(4)]
                parent=tuple(v[0] for v in pq);q=tuple(v[1] for v in pq)
                if depth==1 and not (q[1]-q[0])%2:continue
                f=q[0]-2*q[1]+q[2]+c1;g=q[1]-2*q[2]+q[3]+c2
                if f%4 or g%4:continue
                Cn=(C+(b-a)*(1<<(depth-1)))%Cmod
                Dn=(D+(q[1]-q[0])*(1<<(2*(depth-1))))%Dmod
                nxt.add((*parent,rel//2,f//4,g//4,Cn,Dn))
        states=nxt
    return p,states


def finish(j,p,seed,J=8):
    grouped={}
    for s in seed:
        C,D=s[7:]
        b=9*D*D*pow((C<<(j+1))+1,-1,1<<J)%(1<<J)
        grouped.setdefault(b,set()).add((*s[:7],*([0]*8)))
    states=set()
    for b,current in grouped.items():
        for bit in range(J):
            current={n for s in current for n in step(s,p['coeff'],p['base'],(b>>bit)&1)}
            if not current:break
            # A finite early terminal would require its own smaller modulus;
            # this probe reports it instead of treating it as excluded.
            if any(terminal(s,p['base']) for s in current):
                return dict(status='early geometric terminal',bit=bit,seed_count=len(seed))
        states.update(current)
    todo=deque(states);seen=set(states)
    while todo:
        s=todo.popleft()
        if terminal(s,p['base']):
            return dict(status='geometric suffix accepts',seed_count=len(seed),after=len(states),visited=len(seen))
        for cb in (0,1):
            for n in step(s,p['coeff'],p['base'],cb):
                if n not in seen:seen.add(n);todo.append(n)
    return dict(status='closed without terminal',seed_count=len(seed),after=len(states),visited=len(seen))


if __name__=='__main__':
    for j in range(2,10):
        p,states=seed(j)
        print(j,finish(j,p,states),flush=True)
