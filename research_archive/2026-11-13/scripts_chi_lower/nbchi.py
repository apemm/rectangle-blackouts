# chi of Gamma_T restricted to vertex sets built from S_T (exact, via SAT)
import sys, time
from sinf import S, adj
from pysat.solvers import Glucose4
import networkx as nx
def build(T,B,mode):
    s=S(T,B); Sp=set(s)
    if mode=="out": V=sorted(Sp)                 # out-neighbourhood S_T (signed)
    elif mode=="nb": V=sorted(Sp|{-d for d in Sp})  # N(0)
    G=nx.Graph(); G.add_nodes_from(V)
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            if adj(T,V[j]-V[i]): G.add_edge(V[i],V[j])
    return G
def chi(G,kmax=12):
    nodes=list(G.nodes()); idx={v:i for i,v in enumerate(nodes)}
    cl=max(nx.find_cliques(G),key=len) if G.number_of_edges() else nodes[:1]
    for k in range(max(1,len(cl)),kmax+1):
        s=Glucose4(); var=lambda v,c: idx[v]*k+c+1
        for v in nodes: s.add_clause([var(v,c) for c in range(k)])
        for u,v in G.edges():
            for c in range(k): s.add_clause([-var(u,c),-var(v,c)])
        for c,v in enumerate(cl): s.add_clause([var(v,c)])
        r=s.solve(); s.delete()
        if r: return k,len(cl)
    return None,len(cl)
if __name__=="__main__":
    B=int(float(sys.argv[1])); mode=sys.argv[2]
    for T in map(int,sys.argv[3:]):
        t0=time.time(); G=build(T,B,mode)
        k,w=chi(G)
        # remove hub -T/5 if present for 'out'
        print("T",T,mode,"|V|",G.number_of_nodes(),"E",G.number_of_edges(),"omega",w,"chi",k,"t=%.1f"%(time.time()-t0),flush=True)
