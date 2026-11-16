"""(1) Block rules at a divisible by 486 (the case full_comp left open).
(2) a=1: longest interval with a mod-3-certified solution (DFS), by b."""
import sys
sys.setrecursionlimit(10000)
from check_twogap import block_combine, block_search, check

bad = 0; n = 0
for a in (486, 972, 1458, 2916):
    for b in list(range(0, 60)) + list(range(700, 760)) + list(range(2180, 2200)) + [4373, 4374, 4375, 8747]:
        for s in (1, 2):
            for f, P in (block_combine(a, b, s), block_search(a, b, s)):
                n += 1
                if not check(f, P, a, b, s, True): bad += 1
print('486|a block checks', n, 'bad', bad)

def longest_mod3(b, s, cap):
    # values y_r in Z/3; y[r+1]!=y[r]; y[r+b]-y[r] != s mod 3 (b>=1); y[r+b+1]-y[r] != s mod 3
    best = [0]
    y = [0]
    def ok(r):
        if y[r] == y[r - 1]: return False
        if b >= 1 and r - b >= 0 and (y[r] - y[r - b]) % 3 == s % 3: return False
        if r - b - 1 >= 0 and (y[r] - y[r - b - 1]) % 3 == s % 3: return False
        return True
    def dfs():
        L = len(y)
        if L > best[0]: best[0] = L
        if L >= cap: return True
        for val in range(3):
            y.append(val)
            if ok(L) and dfs(): return True
            y.pop()
        return False
    dfs()
    return best[0]

for b in range(0, 20):
    for s in (1, 2):
        print('a=1 b=%d s=%d longest mod3-certified interval: %d' % (b, s, longest_mod3(b, s, 60)))
