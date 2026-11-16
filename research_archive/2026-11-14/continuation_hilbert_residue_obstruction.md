# A dyadic-residue obstruction in the Hilbert P graph

14 November 2026. This concerns the constant-stride Hilbert placement in
[the placement note](continuation_hilbert_placement.md).

For every fixed number of low coordinate and rank bits, there is an actual
P-conflict whose two labels agree on all those bits. Consequently a bounded
palette that is a function only of those residues cannot resolve the
Hilbert P graph at every height.

This does not rule out a bounded coloring using higher-level or nonlocal
information. It gives no growing chromatic-number lower bound.

## 1. The explicit labels

Fix a stride \(S=2^e\), \(e\ge5\), and let \(q=2^k\), \(k\ge1\).
Set
\[
 N=\frac{S^2q^3}{16},\qquad Q=8qN,\qquad h=2Q=16qN=S^2q^4.
 \tag{1}
\]
Both \(N\) and \(Q\) are powers of two.
Use the full label grid \(\{0,\ldots,Q-1\}^2\), with label \((i,j)\)
in column \(S H_Q^{-1}(i,j)\), and black rows \(2i+1,2j+2\).

Consider the labels
\[
 e=(6q,\ 2qN+6q-1),\qquad
 f=(7q,\ 2qN+6q-1).
 \tag{2}
\]
Their Hilbert ranks \(r_e,r_f\) satisfy
\[
 r_f-r_e=q^2,\qquad
 r_e=\frac{44q^2N^2-88q^2-1}{3}.
 \tag{3}
\]
In particular,
\[
 e\equiv f\pmod q\quad\text{coordinatewise},\qquad
 r_e\equiv r_f\pmod{q^2}.
 \tag{4}
\]

Here and below, the Hilbert order is exactly the recursive order in the
placement note, not an arbitrary orientation convention.

## 2. Why these ranks have the claimed orientation

Partition the \(Q\)-square into aligned squares of side \(2q\).
The square containing (2) has macro-coordinate
\[
 (I,J)=(3,N+2)
\]
in the macro-grid of side \(4N\). Its internal Hilbert orientation is the
identity.

This can be checked directly from the four recursion maps.
At size \(4N\), the macro-cell is in the first quadrant, giving a coordinate
swap and local coordinates \((N+2,3)\).
At size \(2N\), it is in the fourth quadrant, giving a negative swap and
local coordinates \((N-4,N-3)\).
The combined linear orientation is now minus the identity.
Successive third quadrants reduce this pair to \((0,1)\) at size four,
without changing the orientation. The first quadrant at size four gives
a swap; the fourth quadrant at size two gives a negative swap.
Their combined contribution is again minus the identity.
The final orientation is therefore the identity.

The macro-cell's rank is
\[
 R_0=3N^2+2\sum_{j=2}^{\log_2N-1}4^j+3
     =\frac{11N^2-23}{3}.
 \tag{5}
\]
Inside the \(2q\)-square, the second and third \(q\)-quadrants have the same
identity orientation. In each, select internal coordinate \((0,q-1)\).
Its \(q\)-square rank is
\[
 v=(q^2-1)/3.
 \]
Thus
\[
 r_e=4q^2R_0+q^2+v,\qquad
 r_f=4q^2R_0+2q^2+v,
 \]
which proves (2)--(4).

## 3. The actual immutable collision

Take the odd point of \(e\) and the even point of \(f\):
\[
 C=(Sr_e,\ 12q+1),\qquad
 D=(Sr_f,\ 4qN+12q).
 \tag{6}
\]
Their horizontal and vertical separations are
\[
 X=S q^2,\qquad y=4qN-1.
 \]
By (1), \(X^2=16qN\), so
\[
 X^2+y^2=(4qN+1)^2.
 \tag{7}
\]
The vertical diagonal with the same midpoint has endpoints
\[
 P=\left(\frac{S(r_e+r_f)}2,\ 12q\right),\qquad
 Z=\left(\frac{S(r_e+r_f)}2,\ 4qN+12q+1\right).
 \tag{8}
\]
All coordinates are integral. Both rows lie strictly within the height
range in (1). Equal diagonal lengths and the common midpoint make
\(\{C,D,P,Z\}\) a nondegenerate tilted rectangle.

The complete label family contains the owner of the row pair in (8):
\[
 g=(2qN+6q,\ 6q-1).
 \tag{9}
\]
Its column differs from the midpoint column in (8).
Indeed, the midpoint rank lies between \(r_e\) and \(r_f\), hence inside
the same aligned \(2q\)-square. The label \(g\) lies outside that square.

Let \(x_g=S H_Q^{-1}(g)\). The axis rectangle
\[
 \{P,Z,(x_g,12q),(x_g,4qN+12q+1)\}
 \]
has the same presentation as the tilted rectangle:
their symmetric difference consists of \(C,D\) and the two owner points,
all black. This conclusion is independent of the colors assigned to
the common points \(P,Z\), and independent of every other filler choice.

Thus \(e,f\) form an actual edge of the Hilbert placement's P-conflict
graph, not merely an integral-distance candidate whose completion leaves
the strip.

## 4. Consequence for fixed low-bit colorings

Fix nonnegative integers \(a,b,c\), and consider any palette of the form
\[
 {\cal C}(i,j)=
 F_h\bigl(i\bmod2^a,\ j\bmod2^b,\
             H_Q^{-1}(i,j)\bmod2^c\bigr).
 \tag{10}
\]
The function \(F_h\) may depend on the height; no restriction on its output
labels is needed.
Choose \(k\) so that \(k\ge a,b\) and \(2k\ge c\).
Equations (4) make the inputs in (10) identical for \(e\) and \(f\).
Equation (8) supplies their actual P-conflict.
Therefore (10) cannot be a proper coloring at the height (1).

The same statement allows any finite list of dyadic coordinate/rank
residues, since they can be replaced by their largest moduli.
It does not cover a coloring that reads arbitrarily high bits or uses a
nonlocal feature of the Hilbert path.

## 5. Verification

The recursive rank formula, the orientation, and the collision arithmetic
were independently checked in
[the Hilbert extensions audit](audit_hilbert_extensions.md). The script
[check_hilbert_residue_obstruction.py](check_hilbert_residue_obstruction.py)
checks 30 cases with \(S\in\{32,64,128\}\) and \(1\le k\le10\).
It uses exact integer arithmetic and sparse recursive rank lookups, so it
does not construct the full board. In each case it verifies both rectangles
and compares their actual presentations under full-family membership.
The largest checked height is \(18014398509481984\).
Results are saved in
[check_hilbert_residue_obstruction.json](check_hilbert_residue_obstruction.json).
