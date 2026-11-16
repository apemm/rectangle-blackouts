# Periodic routing cannot give a linear monotone P partition

11 November 2026. This is an obstruction to fixed periodic chain templates,
not to arbitrary correlated palettes or to the desired linear partition.

Put \(A=\lceil h/2\rceil\), \(K=\lfloor h/2\rfloor\). A chain consists of
labels \((i,j)\in[0,A)\times[0,K)\), with strictly increasing \(i\) and
nondecreasing \(j\). Its forbidden pairs include either orientation of

\[
16(i-i')^2+[2(j-i')+1]^2=L^2,
\qquad L\text{ odd},\quad 0<L<h.                 \tag{1}
\]

The existing elementary upper bound is \(O(h\log h)\), with slope-one
chains. The argument below rules out one natural way to remove the logarithm:
using a fixed periodic local routing rule to coordinate long chains.

## 1. Precise template model

Fix an integer \(M\ge1\). Let \(f\) be a partially defined injective map on
\(\mathbb Z^2\), satisfying

\[
f(v+Mu)=f(v)+Mu\qquad(u\in\mathbb Z^2),             \tag{2}
\]

including invariance of its domain. Whenever \(f(i,j)=(i',j')\), require

\[
i'>i,\qquad j'\ge j.                              \tag{3}
\]

The components of the directed edges \(v\to f(v)\) are monotone paths.
Intersect them with the finite label grid. Monotonicity ensures that a path
segment between two in-grid vertices remains in the grid, so these intersections
are again paths. The template partition means this partition into path
components; merging its components afterward is an additional operation not
covered by the theorem.

The phase graph has the \(M^2\) residues modulo \(M\mathbb Z^2\) as vertices.
It is a partial permutation: injectivity of \(f\) implies injectivity on phases,
since two targets in the same phase can be made equal by an \(M\mathbb Z^2\)
translation of one source.

**Theorem.** A fixed template has one of the following two properties.

1. Its phase graph has no directed cycle. Every chain has at most \(M^2\)
   vertices, so its partition of the grid has at least \(AK/M^2\) classes.
2. Its phase graph has a directed cycle. For every sufficiently large \(h\),
   one of its in-grid chains contains a forbidden pair (1). The alternative
   vertical white pair also lies in rows \(1,\ldots,h\).

Consequently, no fixed periodic template gives P-free monotone partitions with
\(O(h)\) classes for all sufficiently large heights. This remains true when
each template step is required to obey a fixed Lipschitz bound.

## 2. The exact Pythagorean pair on a periodic path

Choose a phase on a directed cycle and let one complete traversal displace a
vertex by \((D,E)\). Thus \(D\ge1\), \(E\ge0\), and both coordinates are
divisible by \(M\). Choose a representative
\((i_0,j_0)\) of that phase and write

\[
T_0=2(j_0-i_0)+1\pmod {2M}.
\]

Choose the unique positive odd \(s\le2M-1\) such that

\[
s\equiv-T_0\pmod {2M}.
\]

Take \(n=s\) traversals and put

\[
d=nD,\quad e=nE,\quad
v=\frac{4d^2}{s}-s,\quad
L=\frac{4d^2}{s}+s,\quad T=v+2d.                    \tag{4}
\]

Here \(d\) is divisible by \(Ms\), so all quantities are integers, \(v,L\)
are positive odd integers, and

\[
L^2-v^2=16d^2,\qquad T\equiv-s\equiv T_0\pmod {2M}.
                                                               \tag{5}
\]

Choose \(i\in\{0,\ldots,M-1\}\) in the prescribed first-coordinate phase,
and set \(j=i+(T-1)/2\). The congruence in (5) gives the prescribed second
phase. Thus this point is an \(M\mathbb Z^2\) translate of the chosen cycle
vertex. Its path contains both

\[
(i,j),\qquad(i+d,j+e).
\]

Use the even row \(b=2j+2\) of the first label and the odd row
\(a'=2(i+d)+1\) of the second. Their difference is

\[
b-a'=2(j-i-d)+1=T-2d=v.
\]

Their horizontal separation is \(4d\), and (5) proves (1). The alternative
vertical diagonal has midpoint column \(4i+2d\) and rows

\[
a'-s,\qquad a'+\frac{4d^2}{s}.                     \tag{6}
\]

Both are integral and their difference is the odd integer \(L\). The lower
row is positive because \(d\ge s\) and \(i\ge0\). By choosing \(h\) larger
than the finitely many indices and rows in (4)--(6), both labels, every
intermediate path vertex, and both white rows lie in the required grid/strip,
and \(L<h\). Therefore the obstruction is not an artifact of dropping the
white-containment condition.

This proves the cyclic case. In the acyclic case, a path cannot repeat any
phase, so it has at most \(M^2\) vertices, proving the other case.

## 3. A quantitative version for bounded steps

Suppose every defined step has

\[
1\le i'-i\le B,\qquad0\le j'-j\le B,
\]

where \(B\ge1\). A phase cycle has length at most \(M^2\), hence
\(D,E\le M^2B\). In (4),

\[
d,e\le2M^3B,\qquad
\frac{4d^2}{s}=4sD^2\le8M^5B^2.
\]

The pair and its white rows therefore fit, with \(L<h\), whenever

\[
h\ge24M^5B^2.                                    \tag{7}
\]

The constant is deliberately loose. For example, all required upper bounds
are smaller than
\(8M^5B^2+8M^3B+4M+3\le23M^5B^2\).

If a height-dependent family of such templates supplies at most \(Ch\)
classes, then its period cannot stay bounded. More precisely, either its phase
graph is acyclic and \(M^2\ge AK/(Ch)\), or it has a cycle and
\(h<24M^5B^2\). For bounded \(B,C\), this forces

\[
M=\Omega_{B,C}(h^{1/5}).
\]

This is only a restriction on this periodic routing model. It does not impose
a period requirement on arbitrary chain colorings, adaptive queue policies,
or global matchings.

## 4. A correlated queue model that remains open

There is a simple correlated construction with the correct class budget and
Lipschitz property before P is imposed. Start with \(C\) distinct tokens in
each even-index row \(j\in[0,K)\). At each odd-index column \(i\), select one
token from each row, assign it the label \((i,j)\), and simultaneously move it
to row \(j+1\). Discard the departing token at the top and inject one new token
at row zero before the next column. Every queue always has \(C\) tokens.

A token's assigned labels have successive \(j\)-values and strictly increasing
\(i\)-values. Therefore each resulting class satisfies

\[
0<j'-j\le i'-i,
\]

and the number of classes is at most \(CK+A-1\). The unsolved requirement is
to choose the served tokens so that each token avoids P conflicts with its
entire previous history. Avoiding only the preceding label is insufficient.
The theorem above excludes fixed periodic successor templates as a uniform
solution, but does not exclude adaptive or height-dependent service choices.

No linear monotone P partition is claimed here, and no conclusion is drawn
about mixed collisions or filler compatibility in a full rectangle construction.
