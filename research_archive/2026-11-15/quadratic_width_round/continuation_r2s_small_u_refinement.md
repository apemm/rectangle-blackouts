# A symmetric small-variable count gives the R2s exponent 5/6

15 November 2026. The R2s side-owner row count improves further to
\[
 |Y_{\rm R2s}|\le C\tau_*(h)h^{5/6}=h^{5/6+o(1)}.
 \tag{1}
\]
The new step is a small-\(U\) counterpart to the source's small-\(T\)
divisor count. Together with the averaged divisor estimate in
[`continuation_r2s_averaged_divisibility.md`](continuation_r2s_averaged_divisibility.md),
it replaces the low-offset cost \(\sqrt h D^{3/2}\) by \(\sqrt h D\).
The resulting occupied good-cap exceptions and odd-only singleton ranks
number \(h^{11/6+o(1)}\). Their remaining P constraints are not resolved
by this count.

## 1. The small-U branch

Use the source equations
\[
 TU=-m\delta,\qquad
 V^2-U^2=\delta(2m-\delta),\qquad 1\le|m|<h,
 \tag{2}
\]
with nonzero \(T,U,\delta\). Put \(d=|\delta|\) and
\(R=\sqrt{hd}\). Since \(|TU|\le hd\), every solution has
\(|T|\le R\) or \(|U|\le R\).

Suppose \(|U|\le R\). If \(d\le h\), (2) gives
\(|V|\le2R\). Define
\[
 A=U-V,\qquad B=U+V.
\]
Then
\[
 AB=d^2+2TU,\qquad d\mid AB,\qquad U\mid A^2+d^2.
 \tag{3}
\]
The divisibility \(d\mid AB\) uses \(d\mid TU\). The last
divisibility follows from \(U\mid V^2+d^2\) and
\(A\equiv-V\pmod U\).

Fix \(g=\gcd(A,d)\), and put \(n=d/g\). Equation (3) implies
\(n\mid B\). There are two independent ways to count this class.

* The integer \(A\) is a multiple of \(g\), with \(|A|\le3R\).
  Once \(A\) is chosen, \(U\) is a signed divisor of the positive
  integer \(A^2+d^2\). The values \(V=U-A\),
  \(T=(U^2-V^2-d^2)/(2U)\), and \(m=-TU/\delta\) are determined.
* Write \(B=nk\), with \(|k|\le3R/n\). As \(V=B-U\),
  \(U\mid n^2k^2+d^2\). A choice of \(k\) and of a signed divisor
  \(U\) again determines the whole solution.

In both counts the positive divisor argument is at most
\(9R^2+d^2\). Consequently, whenever this is at most \(h^2\),
\[
 N_U(d;R)\le C\tau_*(h)
       \left\{R G(d)+\tau(d)\right\},\qquad
 G(d)=\sum_{g\mid d}\min\{g^{-1},g/d\}.
 \tag{4}
\]
Integrality, the remaining equations, and the exact gcd condition can
only remove candidates. The cases \(A=0\) or \(B=0\) are covered by
the additive one in each parameter count, hence by \(\tau(d)\).
The divisor arguments stay nonzero because \(d>0\).

## 2. Average both small-variable bounds

For every \(D\ge1\),
\[
 \sum_{D\le d<2D}G(d)\le C\sqrt D.
 \tag{5}
\]
Indeed, write \(d=gn\). For fixed \(n\le2D\), the eligible \(g\)'s
number \(O(D/n)\), and each term is at most
\(\min\{n/D,1/n\}\). Their sum is
\(O(\min\{1,D/n^2\})\). Summing over \(n\) proves (5).

The preceding note gives the parallel estimate
\[
 F(d)=\sum_{g\mid d}\min\{g^{-1},d_1(d/g)^{-1}\},\qquad
 \sum_{D\le d<2D}F(d)\le C\sqrt D,
 \tag{6}
\]
and the source's small-\(T\) count is
\[
 N_T(d;R)\le C\tau_*(h)\{R F(d)+\tau(d)\}.
 \tag{7}
\]
For \(d\le D_0=h^{1/3}\) and sufficiently large \(h\), the required
hypotheses hold: \(R\ge d\) and \(9R^2+d^2\le h^2\).
Equations (4) and (7) cover every solution by the small-variable split.
On a dyadic interval \(D\le d<2D\), their total is at most
\[
 C\tau_*(h)\left\{\sqrt{hD}\sqrt D+D\log(2D)\right\}
 \le C\tau_*(h)\{\sqrt h D+D\log(2D)\}.
 \tag{8}
\]
Here the additive term uses
\(\sum_{d\le X}\tau(d)\le X(1+\log X)\).
Summing the dyadic intervals up to \(D_0\) gives
\[
 C\tau_*(h)\{\sqrt h D_0+D_0\log(2D_0)\}
 =O(\tau_*(h)h^{5/6}).
 \tag{9}
\]

## 3. The larger offsets

The inherited geometric reduction is unchanged. Apart from a fixed finite
offset set, every admissible R2s solution satisfies
\[
 d\le C_1\sqrt h,\qquad |T|\le\max(4h/d,d).
 \tag{10}
\]
For \(d>D_0=h^{1/3}\), the source B2 hypotheses hold for all
sufficiently large \(h\). Apply (6) with the same weighted dyadic sums
as in the preceding note. The count is at most
\[
 C\tau_*(h)\left\{hD_0^{-1/2}+h^{3/4}
                      +\sqrt h\log(2h)\right\}
 =O(\tau_*(h)h^{5/6}).
 \tag{11}
\]
The fixed finite offset set is already included in the small-offset range
once \(h\) is large. Signs, sea choices, and roles cost fixed factors.
Every side-owner row admits a counted solution, proving (1).

## 4. Consequences and remaining scope

This improves the counting input used by
[`continuation_random_good_caps.md`](continuation_random_good_caps.md).
Its fixed-profile square filters remove only \(O(\sqrt h)\) additional
rows, so the total bad-row count is \(b=h^{5/6+o(1)}\). Therefore
\[
 n_E, |J|=O(hb\log(2h))=h^{11/6+o(1)}.
 \tag{12}
\]
For a separately applicable relocation factor \(T(h)=h^{o(1)}\),
the internal exceptional-label width is still \(o(h^2)\).
The external relocation, collars, and all residual P and mixed-support
conditions retain their stated hypotheses. In particular, an upper bound
on \(|J|\) is not itself an occupancy-preserving repair of its incident P
events.

The source's geometric displacement regimes are used as inputs, exactly as
in the preceding note. No new claim about their practical numerical
constants is made. The complete written proof passed two independent
reviews, including both signed-divisor parameterizations, the zero cases,
the small-variable covering, the divisor-argument bounds, and the dyadic
exponent balance. The inherited geometric and relocation scope remains
explicit.
