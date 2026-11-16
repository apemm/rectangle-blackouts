"""Class-slot sublayer of LAD rescaled by 64: eta~(X) = X mod N (N = 2^E').  Search four-point mixed quadruples."""
import sys, numpy as np
from quad4 import run
for N in map(int, sys.argv[1:]):
    E = np.arange(N, dtype=np.int64)
    out, no = run(E, N)
    print('strip N=%d: shapes %d' % (N, no)); 
    for r in out[:5]: print('  ', list(r))
