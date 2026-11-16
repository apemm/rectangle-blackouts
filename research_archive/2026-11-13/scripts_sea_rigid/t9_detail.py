import sys
exec(open('t8_block.py').read().split("t0 = time.time()")[0])
for (a, b, c, d, p, q) in mixed(S, h):
    print('M', [(Q, tag(Q), Q[0]//4 % 4) for Q in (a, b, c, d)], 'p', p, 'q', q)
for (c, d, j) in rivals(S, h):
    print('R', c, d, j, tag(c), tag(d))
print('M_block', M, 'R', R, 'rho', rho)
