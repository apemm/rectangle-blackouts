import numpy as np
from core import _divcount, _divfill


def divisor_table32(NMAX):
    cnt = np.zeros(NMAX + 1, dtype=np.int64)
    _divcount(NMAX, cnt)
    dstart = np.zeros(NMAX + 2, dtype=np.int64)
    np.cumsum(cnt, out=dstart[1:])
    del cnt
    dlist = np.zeros(dstart[-1], dtype=np.int32)
    _divfill(NMAX, dstart, dlist)
    return dstart, dlist


