# Exact decision of the abstract M=3 system on Z for a gap set Q (all candidate constraints present):
# gap q: for d in {floor(q/3), ceil(q/3)}, d>=1, forbid xi(r+d)-xi(r) == q-3d.
# Solvable on Z iff the window graph (words of length D) has a cycle.
import itertools, sys
M=3
def cons(Q):
    c=set()
    for q in Q:
        for d in {q//M, -(-q//M)}:
            if d>=1 and abs(q-M*d)<=M-1: c.add((d,q-M*d))
    return sorted(c)
def solvable(Q):
    C=cons(Q); D=max(d for d,_ in C)
    def ok(w):  # word length D+1, check all constraints inside
        n=len(w)
        for d,de in C:
            for i in range(n-d):
                if w[i+d]-w[i]==de: return False
        return True
    words=[w for w in itertools.product(range(M),repeat=D) if ok(w)]
    S=set(words)
    out={w:[] for w in words}; inn={w:0 for w in words}
    for w in words:
        for x in range(M):
            w2=w[1:]+(x,)
            if w2 in S and ok(w+(x,)):
                out[w].append(w2); inn[w2]+=1
    alive=set(words); changed=True
    outc={w:len(out[w]) for w in words}
    # prune
    pred={w:[] for w in words}
    for w in words:
        for v in out[w]: pred[v].append(w)
    stack=[w for w in words if outc[w]==0 or inn[w]==0]
    dead=set()
    while stack:
        w=stack.pop()
        if w in dead: continue
        dead.add(w)
        for v in out[w]:
            if v not in dead:
                inn[v]-=1
                if inn[v]==0: stack.append(v)
        for u in pred[w]:
            if u not in dead:
                outc[u]-=1
                if outc[u]==0: stack.append(u)
    return len(dead)<len(words)
Qmax=int(sys.argv[1])
two_bad=[Q for Q in itertools.combinations(range(1,Qmax+1),2) if not solvable(Q)]
print("two-gap unsolvable:",two_bad)
three_bad=[Q for Q in itertools.combinations(range(1,Qmax+1),3) if not solvable(Q)]
print("three-gap unsolvable count",len(three_bad))
mixed=[Q for Q in three_bad if len({q%3==0 for q in Q})==2]
print("all-div:",[Q for Q in three_bad if all(q%3==0 for q in Q)])
print("mixed:",len(mixed),mixed[:60])
print("none-div:",[Q for Q in three_bad if all(q%3 for q in Q)])
