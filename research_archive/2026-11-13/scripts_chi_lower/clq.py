import sys, time
from sinf import S, adj
import networkx as nx
def run(T,B):
    t0=time.time()
    s=S(T,B); V=sorted(set(s)|{-d for d in s})
    G=nx.Graph(); G.add_nodes_from(V)
    for i in range(len(V)):
        x=V[i]
        for j in range(i+1,len(V)):
            if adj(T,V[j]-x): G.add_edge(x,V[j])
    best=max(nx.find_cliques(G), key=len) if G.number_of_edges() else [V[0]]
    print("T",T,"B",B,"|V|",len(V),"E",G.number_of_edges(),"omega",len(best)+1,"clique",sorted([0]+best),"t=%.1f"%(time.time()-t0),flush=True)
for T in map(int,sys.argv[2:]): run(T,int(float(sys.argv[1])))
