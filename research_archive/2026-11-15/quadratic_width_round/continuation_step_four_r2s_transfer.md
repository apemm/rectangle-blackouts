# The R2s row bound transfers to the spacing-four refinement

15 November 2026. For the refined core of
[the spacing-four lemma](continuation_step_four_refinement.md),
mixed four-supports with two sea points at the same fixed low row have
only \(h^{5/6+o(1)}\) possible side-owner rows. The proof uses the existing
averaged divisor estimates. It rechecks their geometric hypotheses at
stride four, including the exceptional 45-degree seam pairs.

This is a same-sea-row counting result. It does not classify supports
whose two sea points have different rows, prove a complete low-sea
construction, or provide its end collars.

## 1. Exact geometry and the exceptional offsets

Fix a positive sea row \(s\le s_*\), where \(s_*\) is independent of
height. All core rows are greater than \(s_*\). Core columns are divisible
by four; sea points occupy other columns. For each fixed sea row, require
all its occupied columns to have one common parity, as in the four low
profiles. Write a side/diagonal mixed
support as
\[
 A=(0,y),\quad B=(U,s),\quad C=(X,y+\delta),\quad D=(X+V,s),
 \tag{1}
\]
where \(AB\) is the black side and \(CD\) the black diagonal.
Set \(m=s-y<0\) and \(T=2X+V-U\). Equal norms and the perpendicular
translation of the side give
\[
 TU=-m\delta,\qquad
 V^2-U^2=\delta(2m-\delta),\qquad
 2X=U+T-V.
 \tag{2}
\]
These identities are independent of the stride or sea congruence tests.
The displayed corners are
\[
 A+(T,\delta)/2,\qquad B+(T,\delta)/2.
 \tag{3}
\]
In particular, their rows are \(y+\delta/2\) and \(s+\delta/2\),
and both must be in \([1,h]\).

The two core points have the same parity: modulo two, equality of the
two squared norms in (1) forces their row parities to agree. Each parity
uses one fixed row residue modulo four. The refinement theorem therefore
gives either
\[
 \delta^2\le2|X|,
 \tag{4}
\]
or the exceptional case \(|X|=|\delta|=4\).

Nondegeneracy implies \(\delta\ne0\): otherwise (2) gives \(T=0\)
because \(U\ne0\), and (3) makes the side rectangle degenerate.
Also \(m,T,U\ne0\), and \(e=U-X\ne0\), since neither sea point
occupies a core column. Throughout, \(|m|<h\).

For any fixed finite set of nonzero offsets \(\delta\), the elementary
small-variable count from
[the R2s refinement](continuation_r2s_small_u_refinement.md)
gives \(O(\tau_*(h)\sqrt h)\) solutions of (2), where
\(\tau_*(h)=\max_{n\le h^2}\tau(n)\). This covers the exceptional
seam pairs. Under (4), bounded \(|X|\) also implies bounded
\(|\delta|\), so it is covered by the same estimate.

## 2. Uniform geometric bounds at stride four

Reflect horizontally if necessary and assume \(X\ge16\), and assume
(4). Rearranging (2) gives
\[
 4e(X-T)=T^2+\delta^2,
 \qquad e=U-X.
 \tag{5}
\]
Put \(d=|\delta|\).

If \(|e|\le X/2\), then \(|U|\ge X/2\). Since \(|e|\ge1\),
\[
 X\le |T|+(T^2+d^2)/4
       \le |T|+T^2/4+X/2.
\]
For \(X\ge16\), this gives \(|T|\ge\sqrt X/2\). Consequently,
\[
 X^{3/2}/4\le|TU|=|m\delta|\le h\sqrt{2X},
\]
so \(X\le4\sqrt2h\) and \(d\le4\sqrt h\). Moreover,
\[
 |T|\le 2hd/X\le4h/d.
 \tag{6}
\]

Now suppose \(|e|>X/2\). If \(|T|\le X/2\), (5) would imply
\(X^2<T^2+d^2\le X^2/4+2X\), impossible for \(X\ge16\).
Thus
\[
 |T|>X/2,\qquad |U|<2|m\delta|/X.
 \tag{7}
\]
There are three subcases.

* If \(|U|>X/2\), then \(X^2<4hd\le4h\sqrt{2X}\).
  Thus \(X<4h^{2/3}\), \(d<3h^{1/3}\), and (6) still holds.
* If \(|U|\le X/2\) and \(m\delta<0\), equation (2) gives
  \(|U|\ge\sqrt{2|m\delta|}\). Together with (7), this yields
  \(X<\sqrt{2hd}\), hence \(X<2h^{2/3}\) and \(d<2h^{1/3}\).
  Also \(|T|\le\sqrt{hd/2}\le2h/d\).
* If \(|U|\le X/2\) and \(m\delta>0\), then \(m<0\) implies
  \(\delta<0\). The second row in (3) is at least one, so
  \(d\le2(s-1)\le2(s_*-1)\). This is a bounded-offset case.

After absorbing all bounded offsets, every remaining solution satisfies
\[
 d\le4\sqrt h,\qquad |T|\le4h/d.
 \tag{8}
\]
The fixed stride 6272 from the original H7 formulation is unnecessary
for these asymptotic bounds. Here small horizontal distances were
handled explicitly before applying (5).

## 3. Apply the averaged divisor counts

The arithmetic counting argument depends only on (2), not on the sea
residue classes. Define
\[
 F(d)=\sum_{g\mid d}\min\{g^{-1},d_1(d/g)^{-1}\},\qquad
 G(d)=\sum_{g\mid d}\min\{g^{-1},g/d\},
\]
where \(d_1(n)\) is the least positive integer whose square is divisible
by \(n\). The audited estimates are
\[
 \sum_{D\le d<2D}F(d)+\sum_{D\le d<2D}G(d)\le C\sqrt D.
 \tag{9}
\]
For \(d\le D_0=h^{1/3}\), put \(R=\sqrt{hd}\). Equation (2)
forces \(|T|\le R\) or \(|U|\le R\). The two divisor
parameterizations bound their union by
\[
 C\tau_*(h)\{R(F(d)+G(d))+\tau(d)\}.
\]
On summing dyadically with (9), the total is
\[
 O\bigl(\tau_*(h)(\sqrt h D_0+D_0\log(2D_0))\bigr)
 =O(\tau_*(h)h^{5/6}).
 \tag{10}
\]
The divisor arguments are at most \(9hd+d^2<h^2\) for all
sufficiently large \(h\), as required.

For \(D_0<d\le4\sqrt h\), take
\(T_0=\max(4h/d,d)\). This covers (8), satisfies \(T_0\ge d\),
and has \(9T_0^2+d^2<h^2\) for large \(h\). The small-\(T\)
count and (9) give a total at most
\[
 C\tau_*(h)\{hD_0^{-1/2}+h^{3/4}+\sqrt h\log(2h)\}
 =O(\tau_*(h)h^{5/6}).
 \tag{11}
\]
Signs and the fixed number of sea rows change only the constant.
Every solution fixes its side-owner row \(y=s-m\). Hence the union
\(Y\) of all possible such rows satisfies
\[
 |Y|\le C_{s_*}\tau_*(h)h^{5/6}=h^{5/6+o(1)}.
 \tag{12}
\]
The candidate set can drop all exact sea-type and rank tests. It is
therefore defined before choosing the cap offsets or the refined order.
If every selected core row avoids \(Y\), no same-actual-sea-row mixed
support of the form (1) survives.

## 4. What this does and does not transfer

For the four proposed low profiles, \(s_*\le8\), so (12) is uniform
across them. Using these rows as bad rows in a separately applicable
good-cap construction requires only \(h^{5/6+o(1)}\) row deletions.
The corresponding label count remains \(h^{11/6+o(1)}\).

For these profiles, a mixed support with two core points and one sea
point at each of \(L,F\) is impossible by column parity. The sum of its
four black column coordinates would be odd. In a mixed support,
\(C+D-A-B=2t\), where \(t\) is the integral side-translation vector,
so that sum must be even. The separate
[profile classification](continuation_four_profile_residual_classification.md)
also excludes the grouped two-core/two-sea assignment using the
nonintegral-distance conclusion of the refinement theorem. Thus the
crossed same-row family counted here is the only two-core/two-sea
mixed family left in those profiles.

This transfers the R2s arithmetic count, including its independence
from the eventual rank order. It does not transfer the old H7 sea
classification, its fixed-profile filters, or its relocation and collar
theorems. The other residual families, including the new parked-triangle
collisions in the profile classification, still need control.

Independent review: the complete written transfer proof passed a separate
review, including all constants in the geometric regimes, the bounded
seam offsets, the strip cutoff, and the two divisor-counting ranges.
