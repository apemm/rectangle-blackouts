"""FastWinBoard: same board as classify.WinBoard (no seam), built by slicing a 16-periodic template.
rows() returns {r0} U filler rows U label rows, which equals np.unique of the board whenever the
window has >= 16 columns of each phase (checked against WinBoard.rows by the driver)."""
import numpy as np
from classify import WinBoard


class Template:
    def __init__(self, tp, rho0, Lmax):
        X = np.arange(16, dtype=np.int64)
        pat = np.where(X % 4 != 0, tp['r0'], tp['Ts'] - 24 + 8 * ((X // 4 - rho0) % 4)).astype(np.int64)
        self.base = np.tile(pat, Lmax // 16 + 2)
        self.minus = np.full(Lmax + 32, -1, dtype=np.int64)
        self.tp = tp; self.rho0 = rho0


class FastWinBoard(WinBoard):
    def __init__(self, h, X0, Wd, tp, rho0, labels, tmpl):
        assert tmpl.tp is tp and tmpl.rho0 == rho0
        self.h = h; self.X0 = X0; self.Wd = Wd; self.tp = tp; self.rho0 = rho0
        self.labels = labels; self.seam = None; self.g = None
        o = X0 % 16
        R1 = tmpl.base[o:o + Wd].copy()
        R2 = tmpl.minus[:Wd].copy()
        for nn, (i, j) in labels.items():
            x = 4 * nn - X0
            assert 0 <= x < Wd
            R1[x] = 2 * i + 1; R2[x] = 2 * j + 2
        self.R1 = R1; self.R2 = R2
        s = {tp['r0']} | set(tp['Ts'] - 24 + 8 * o for o in range(4))
        for (i, j) in labels.values():
            s.add(2 * i + 1); s.add(2 * j + 2)
        self._rows = np.array(sorted(s), dtype=np.int64)

    def rows(self):
        return self._rows
