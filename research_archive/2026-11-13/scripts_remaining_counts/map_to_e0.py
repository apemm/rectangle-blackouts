# For every df=0 N_e solution (M=N', A=N'+A', w, k) with Dx >= 78H, check that (e,n1,X,Y)=(N',k,Dx-2k,w-k)
# is an E0(Q) witness with Q = A' + 2N':  XY = e^2+n1^2, n1(X+Y+2n1) = e(Q-2e), X,Y >= 1, e < Q/2.
import sys
src = open('ne_count.py').read().replace('cnt += 1; out.append((M,A,w,k,j,Dx/H))', 'cnt += 1; out.append((M,A,w,k,j,Dx))')
sys.argv = ['x', '0', sys.argv[1]]
g = {}; exec(src, g)
bad = 0
for (M, A, w, k, j, Dx) in g['out']:
    e, n1, Ap = M, k, A - M
    X, Y = Dx - 2*k, j
    Q = Ap + 2*e
    ok = X >= 1 and Y >= 1 and X*Y == e*e + n1*n1 and n1*(X+Y+2*n1) == e*(Q-2*e) and 2*e < Q
    bad += (not ok)
print("solutions", len(g['out']), "failed witness checks", bad)
