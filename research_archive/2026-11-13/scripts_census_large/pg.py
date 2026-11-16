import sys, runpy, checker
from census_v2_tables import divisor_table32
h = int(sys.argv[1]); checker._DIV[h * h] = divisor_table32(h * h)
runpy.run_path('pure_gap.py', run_name='__main__')
