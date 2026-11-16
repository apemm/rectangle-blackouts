# The remaining raw same-parity 6PT correlation

15 November 2026. This note gives an exact arithmetic reduction for
long 6PT collisions whose four core points use one raw Hilbert
coordinate. It explains the missing estimate after the
[opposite-parity count](continuation_hilbert_row_visit_energy.md).
The proved bound here is \(h^{2+o(1)}\), not subquadratic.

## 1. Eliminate the shared row offset

Let \(f(r)=H(r)_\alpha\), and write the physical row as
\[
 y(r)=\rho+D(f(r)-U).
\]
The stride \(S\), row step \(D\), and number of sea rows are fixed.
Let the completion-end core ranks be \(r,r+t\), and the sea
offsets \(\xi_1,\xi_2\ne0\). A common completion requires
\[
 \xi_1-\xi_2=St.
 \tag{1}
\]
The same-parity case has \(t\ne0\): two distinct points of one
parity cannot occupy the same core column.

Put
\[
 v=f(r+t)-f(r),\qquad \delta=D\ell\ne0.
\]
If \(p_1,p_2\) are the other two core ranks, their coordinate
requirements are
\[
 f(p_1)=f(r)-\ell,\qquad
 f(p_2)=f(r+t)-\ell.
 \tag{2}
\]
The parked-triangle equations, with common sea row \(s\), read
\[
 S\xi_i(r_i-p_i)=\delta(y(p_i)-s),
 \quad r_1=r,\quad r_2=r+t.
 \tag{3}
\]
Subtracting them eliminates \(U\) and gives
\[
 S\{\xi_1(r-p_1)-\xi_2(r+t-p_2)\}
       =-D^2\ell v.
 \tag{4}
\]
Thus a candidate \((r,\ell,p_1)\) fixes at most one second partner:
\[
 p_2=r+t-rac{S\xi_1(r-p_1)+D^2\ell v}{S\xi_2}.
 \tag{5}
\]
Nonintegral or out-of-range values are rejected. The first equation
in (3) fixes the single shared offset as
\[
 U=f(p_1)+\frac{\rho-s}{D}
                -\frac{S\xi_1(r-p_1)}{D^2\ell}.
 \tag{6}
\]
If this value is integral and belongs to the sampling interval,
and (2) and (4) hold, then both equations (3) hold. Thus these tests
are exact before the additional sea-color, in-strip, and
nondegeneracy checks.

The probability for a fixed accepted candidate is at most \(C/h\).
There is only one offset constraint. Using \(C/h^2\), as in the
opposite-parity proof, would be invalid.

## 2. A precise correlation target

For fixed \(\xi_1,\xi_2\), define \(\mathcal C\) to count
triples \((r,\ell,p)\) with the following properties:

1. The hub ranks are in range, \(0<|D\ell|<h\), and the first
   equality in (2) holds.
2. With \(d_\ell=|D\ell|/\gcd(|D\ell|,|S\xi_1|)\), one has
   \(p\equiv r\pmod {d_\ell}\).
3. The rank in (5) is integral, in range, and satisfies the second
   equality in (2).

Further geometric restrictions only decrease this count. The
row-visit energy estimate gives
\[
 \mathcal C\le C\tau(|S\xi_1|)h^3
       \max_{n\le C h^2}(1+\tau(n)).
 \tag{7}
\]
Indeed, discard the third requirement and apply equation (8) of
the opposite-parity note. Consequently, for sea offsets of size at
most a fixed power of \(\log h\), the expected total number of
these witnesses is at most \(h^{2+o(1)}\).

A bound
\[
 \mathcal C\le h^{3-\varepsilon+o(1)}
 \tag{8}
\]
uniformly over those offsets would give the desired subquadratic
expectation. This is the remaining concrete raw-coordinate target.
The third requirement, which correlates two coordinate rows under
the affine rank relation (5), must provide the saving.

## 3. What the long-span assumption adds

For core span greater than \(h^2/K\), the local-anchor theorem gives
\[
 |\xi_i|\le CK,\quad |t|\le CK,
 \quad |\ell|\ge c h/K,
 \quad |v|\le C\sqrt K.
 \tag{9}
\]
The implied constants can depend on \(S,D\). The last inequality
uses the Hilbert coordinate bound on the two nearby hub ranks.
Each individual partner count in its required rank progression is
at most \(C\sqrt h\,K\).

These facts do not themselves improve (7). When \(v=0\), (4)
becomes the exact dilation relation
\[
 \xi_1(r-p_1)=\xi_2(r+t-p_2),
\]
and the two distant partners lie in the same coordinate row.
When \(v\ne0\), their coordinate rows differ by the small known
amount \(v\), and (5) includes the linear correction in \(\ell\).
Neither case supplies a second independent random offset.

This reduction concerns raw coordinates. Cap-constant points need
their own counting argument. No claim is made that the same-parity
family is absent, that (8) holds, or that the current quadratic
expectation can be paid by the cited relocation bound.

## 4. Exact section recursions for a carry analysis

For the standard recursive Hilbert orientation, let \(X_N(y)\) and
\(Y_N(y)\) denote the rank sets at first-coordinate value \(y\)
and second-coordinate value \(y\), respectively. If \(N=2n\),
the four children have coordinates
\[
 (y,x),\quad (x,y+n),\quad (x+n,y+n),
 \quad (2n-1-y,n-1-x)
\]
and rank offsets \(0,n^2,2n^2,3n^2\). Therefore
\[
 X_{2n}(y)=
 \begin{cases}
 Y_n(y)\cup(n^2+X_n(y)),&0\le y<n,\\
 (2n^2+X_n(y-n))\cup(3n^2+Y_n(2n-1-y)),&n\le y<2n,
 \end{cases}
 \tag{10}
\]
and
\[
 Y_{2n}(y)=
 \begin{cases}
 X_n(y)\cup(3n^2+X_n(n-1-y)),&0\le y<n,\\
 (n^2+Y_n(y-n))\cup(2n^2+Y_n(y-n)),&n\le y<2n.
 \end{cases}
 \tag{11}
\]
All unions are disjoint. These identities reduce the coordinate tests
in (2) and (5) to finite orientation states and integer carries.

There are genuine large translation correlations. For every
\(n\le y<2n\), equation (11) supplies exactly \(n\) pairs of
visits in row \(y\) at rank difference \(n^2\), one from each
member of \(Y_n(y-n)\). Thus a proof cannot assume small row
correlations at every large displacement. It must combine these
recursions with the increment divisibility and the affine relation
(5). No spectral bound for that combined recursion is asserted here.
