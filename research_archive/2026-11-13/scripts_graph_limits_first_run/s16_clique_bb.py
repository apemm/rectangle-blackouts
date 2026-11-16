# Large cliques in the constraint graph H (non-monotone or P-conflict) by bitset branch and bound with a time limit.
# Any clique found is a valid lower bound for the number of monotone P-free classes. Under 60 s.
import sys, time
from math import isqrt

def build(h):
    A = (h + 1)//2; K = h//2
    labels = [(i, j) for i in range(A) for j in range(K)]
    idx = {l: k for k, l in enumerate(labels)}
    n = len(labels)
    # sees[i][j] = set of slots ip whose odd point is at odd integer distance < h from the even point of (i,j)
    def V(i, j, ip):
        q = 16*(i - ip)**2 + (2*(j - ip) + 1)**2
        L = isqrt(q)
        return L*L == q and L % 2 == 1 and 0 < L < h
    sees = {}
    for (i, j) in labels:
        sees[(i, j)] = set(ip for ip in range(A) if ip != i and V(i, j, ip))
    adj = [0]*n
    for a in range(n):
        i, j = labels[a]
        for b in range(a + 1, n):
            ip, jp = labels[b]
            if i == ip or j > jp or (ip in sees[(i, j)]) or (i in sees[(ip, jp)]):
                adj[a] |= 1 << b; adj[b] |= 1 << a
    return labels, adj, A, K

def max_clique(adj, n, tlimit, t0):
    best = [0, 0]
    def color_sort(P):
        # greedy colouring bound; returns list of (vertex, colour bound) in increasing colour order
        order = []; col = 0
        Q = P
        while Q:
            col += 1
            R = Q
            while R:
                v = (R & -R).bit_length() - 1
                R &= ~(1 << v); R &= ~adj[v]
                Q &= ~(1 << v)
                order.append((v, col))
        return order
    sys.setrecursionlimit(10000)
    def expand(R, size, P):
        if time.time() - t0 > tlimit: return
        order = color_sort(P)
        for v, c in reversed(order):
            if size + c <= best[0]: return
            Rv = R | (1 << v)
            Pv = P & adj[v]
            if Pv:
                expand(Rv, size + 1, Pv)
            elif size + 1 > best[0]:
                best[0] = size + 1; best[1] = Rv
            P &= ~(1 << v)
    expand(0, 0, (1 << n) - 1)
    return best

t0 = time.time()
h = int(sys.argv[1]); tl = float(sys.argv[2])
labels, adj, A, K = build(h)
n = len(labels)
tb = time.time() - t0
best = max_clique(adj, n, tl, t0)
cl = [labels[v] for v in range(n) if best[1] >> v & 1]
done = (time.time() - t0) < tl
print("h", h, "K", K, "clique found", best[0], "ratio", round(best[0]/h, 4), "2h/3", round(2*h/3, 2), "complete search:", done, "build %.1fs total %.1fs" % (tb, time.time() - t0))
bycol = {}
for (i, j) in sorted(cl): bycol.setdefault(i, []).append(j)
print("  by slot:", bycol)
