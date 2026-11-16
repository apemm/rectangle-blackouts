from layout import build
h=131; W=1600; phi=(0,1,3,2); Y=75
S,k = build(h,W,1,[],lambda n: Y+16*phi[n%4])
nA=200; A=(4*nA,Y+16*phi[nA%4]); B=(4*(nA+1),Y+16*phi[(nA+1)%4])
nC=nA-32; C=(4*nC,Y+16*phi[nC%4]); D=(4*(nC+1),Y+16*phi[(nC+1)%4])
print(A,B,C,D, all(q in S for q in (A,B,C,D)))
U=(B[0]-A[0],B[1]-A[1]); V=(D[0]-C[0],D[1]-C[1]); print('U',U,'V',V)
N2=(C[0]+D[0]-A[0]-B[0], C[1]+D[1]-A[1]-B[1]); print('2N',N2, 'dot', N2[0]*U[0]+N2[1]*U[1], U[0]**2+U[1]**2, V[0]**2+V[1]**2)
