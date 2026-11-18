# A joint counting bound from the shorter completed strip

Let \(a_h(m)\) count maximum blackouts on the labeled \(h\)-by-\(m\) grid. Write \(x=\inf_{a>0}(1+3^{a/2})/(1+a)<1.3108172\), and \(\Lambda=1+\log h\). For every fixed \(\varepsilon>0\),
\[
 \frac{a_h(m)^{1/m}}{h}\longrightarrow\frac12
 \quad\text{if}\quad h\longrightarrow\infty,\qquad
 \frac{m}{h^2\Lambda^{x+1+\varepsilon}}\longrightarrow\infty .
\]
This is a substitution of the current full-board bound into the earlier joint counting theorem. The earlier estimate had \(3+\varepsilon\) as the exponent of the logarithm.

To see the quantifiers, fix a stride menu with \(x_k<x+\varepsilon/2\). Its completed parity construction has width \(T_h\le C_\varepsilon h^2\Lambda^{x+\varepsilon}\) for large \(h\), absorbing the fixed power of \(\log\log h\). Its left exterior is entirely in row 1. Retain a row-1 collar of at least \(2W_h+1\) columns on the left, with \(W_h=1+\lfloor(h-1)^2/4\rfloor\). Prepend the buffered odd-row word on that side and retain the full completed block on the right. A join with matching row-1 exteriors passes all local tests. All remote-owner tests use the same full parity graph, and the new core contributes only singleton columns. Thus the constructed words still have \(m+q_h\) black cells. The buffered core can be recovered from the specified positions in the completed word. [Completed board](../../papers/extremal/drafts/upper_bound/part8_assembly.tex) and [buffer and container bounds, Sections 3–5](../2026-11-09/full_problem_push/joint_height_width_counting.md)

The cost in the logarithm of the count from reserving these \(O(T_h+h^2)\) columns is \(O_\varepsilon(h^2\Lambda^{x+1+\varepsilon})\). The core cost is \(O(m\Lambda^4/h)\), and the \(O(h^{7/4})\) boundary cost is absorbed by the reservation cost. In particular, for all sufficiently large \(h\) and \(m\ge C_\varepsilon h^2\Lambda^{x+\varepsilon}\), with \(C_\varepsilon\) large enough,
\[
 \log a_h(m)\ge m\log(h/2)
   -O_\varepsilon\!\left(m\Lambda^4/h+h^2\Lambda^{x+1+\varepsilon}\right).
\]
The container upper bound gives \(\limsup a_h(m)^{1/m}/h\le1/2\) at equality widths satisfying \(m/(h^2\log h)\to\infty\). This proves the limit. Taking ratios of logarithms instead gives \(\log a_h(m)/(m\log h)\to1\) already for \(m/(h^2\Lambda^{x+\varepsilon})\to\infty\).

These statements allow both height and width to grow. They leave the fixed-height multiplicative constant, polynomial degree, and possible dependence on the width residue to the fixed-height analysis.

The archived [stride-menu theorem, Sections B9 and S-6](../2026-11-13/consolidated_board_menu.md) also records the applicable width bound and exterior.
