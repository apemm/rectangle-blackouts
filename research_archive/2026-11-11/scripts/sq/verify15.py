import sys
sys.path.insert(0, '../v45')
from core import is_valid
cols = "16 56 45 14 4 1 47 12 34 67 23 1 36 27 25".split()
h, m = 7, len(cols)
S = {(x+1, int(ch)) for x, c in enumerate(cols) for ch in c}
print("width", m, "points", len(S), "expected", m + h*h//4, "valid for the 45-degree family:", is_valid(h, m, S)[0])
