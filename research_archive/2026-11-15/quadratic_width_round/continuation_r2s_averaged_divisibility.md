# Averaging the divisor split improves the R2s row bound

15 November 2026. Retaining the divisor sum in the existing R2s argument
improves its exceptional-row exponent from \(10/11\) to \(7/8\):
\[
 |Y_{\rm R2s}|\le C\tau_*(h)h^{7/8}=h^{7/8+o(1)}.
 \tag{1}
\]
The constants may depend on the fixed profile. This is a refinement of the
counting input, not a new proof of the external relocation or gluing inputs.
In particular, the occupied good-cap construction then has
\(h^{15/8+o(1)}\) exceptional labels and odd-only singleton ranks.

The stronger small-variable argument in
[`continuation_r2s_small_u_refinement.md`](continuation_r2s_small_u_refinement.md)
improves these exponents to \(5/6\) and \(11/6\), respectively. The
averaged divisor estimate below is an input to that improvement.

## 1. Inputs and the divisor sum that was discarded

Use the notation and geometric regimes of
[`r2s_relocation_o_h2.md`](../../2026-11-14/r2s_relocation_o_h2.md).
Write \(\tau_*(h)=\max_{n\le h^2}\tau(n)\), and define
\[
 d_1(n)=\prod_{p^e\Vert n}p^{\lceil e/2\rceil},\qquad
 F(d)=\sum_{g\mid d}\min\{g^{-1},d_1(d/g)^{-1}\}.
 \tag{2}
\]
The proof of that source's Lemma B2, before its final worst-case estimate,
gives the sharper form
\[
 N(d;T_0)\le C\tau_*(h)\{T_0 F(d)+\tau(d)\}.
 \tag{3}
\]
Here \(N(d;T_0)\) counts the signed solutions at offset magnitude \(d\)
with \(|T|\le T_0\), under the original B2 hypotheses
\(T_0\ge d\) and \(9T_0^2+d^2\le h^2\).

The other inputs are unchanged. Lemma B1 gives
\[
 N(d)\le C\tau_*(h)(\sqrt{hd}+1).
 \tag{4}
\]
Outside the bounded-offset \((n+)\) regime, the source's geometric
reduction gives
\[
 d\le C_1\sqrt h,\qquad
 |T|\le T_0(d)=\max(4h/d,d),
 \tag{5}
\]
in a range where (3) applies. The \((n+)\) offsets form a fixed finite
set and contribute \(O(\tau_*(h)\sqrt h)\) by (4).
Signs, the fixed congruence restrictions on offsets, the finitely many
seas, and the two parity roles change only constants.

## 2. The dyadic average is square-root size

For every \(D\ge1\),
\[
 \sum_{D\le d<2D}F(d)\le C\sqrt D.
 \tag{6}
\]
To prove this, write \(d=g u v^2\), where \(u\) is squarefree. Then
\(d_1(d/g)=uv\). For fixed \(u,v\), the eligible \(g\)'s lie between
\(D/(uv^2)\) and \(2D/(uv^2)\). If this interval contains a positive
integer, then \(uv^2\le2D\), and its number of positive integers is
\(O(D/(uv^2))\). Each summand is at most
\(\min\{uv^2/D,1/(uv)\}\). Their total is therefore
\[
 O\!\left(\min\left\{1,\frac{D}{u^2v^3}\right\}\right).
 \tag{7}
\]
We can now discard squarefreeness and extend the sum over \(u\). For
every \(A>0\),
\[
 \sum_{u\ge1}\min\{1,A^2/u^2\}\le C A.
 \tag{8}
\]
For \(A\ge1\), split at \(u=A\). For \(A<1\), the sum is
\(O(A^2)\le O(A)\). Apply (8) with \(A=\sqrt D/v^{3/2}\), then sum
the convergent series \(\sum_v v^{-3/2}\). This proves (6).

Two weighted consequences, for \(1\le D_0\le X\), are
\[
 \sum_{D_0<d\le X}\frac{F(d)}d\le\frac{C}{\sqrt{D_0}},
 \qquad
 \sum_{d\le X}d F(d)\le C X^{3/2}.
 \tag{9}
\]
Both follow by summing (6) over dyadic intervals. Also,
\[
 \sum_{d\le X}\tau(d)
 =\sum_{a\le X}\left\lfloor X/a\right\rfloor
 \le X(1+\log X).
 \tag{10}
\]
No average divisor theorem is needed.

## 3. Balance the two offset ranges

Choose \(D_0=h^{1/4}\). The offsets up to \(D_0\), counted by (4),
contribute
\[
 C\tau_*(h)\sqrt h\sum_{d\le D_0}\sqrt d
 \le C\tau_*(h)h^{1/2}D_0^{3/2}
 =C\tau_*(h)h^{7/8}.
 \tag{11}
\]
For larger offsets use (3), (5), and (9), with \(X=C_1\sqrt h\):
\[
 \begin{aligned}
 \sum_{D_0<d\le X}N(d;T_0(d))
 &\le C\tau_*(h)\left(
 h\sum_{d>D_0}\frac{F(d)}d+
 \sum_{d\le X}d F(d)+\sum_{d\le X}\tau(d)\right)\\
 &\le C\tau_*(h)\left(
 hD_0^{-1/2}+h^{3/4}+\sqrt h\log(2h)\right)\\
 &\le C\tau_*(h)h^{7/8}.
 \end{aligned}
 \tag{12}
\]
Add the bounded-offset regime. Every side-owner row has at least one
counted solution, so (1) follows.

## 4. Construction consequences and scope

Let \(T(h)=h^{o(1)}\) denote the separately applicable positional
relocation factor. In
[`continuation_random_good_caps.md`](continuation_random_good_caps.md),
the bad-row count is now \(b=h^{7/8+o(1)}\), including the smaller
fixed-profile square-filter exclusions. Thus both the exceptional-label
count and the odd-only singleton count satisfy
\[
 n_E, |J|\le C h b\log(2h)=h^{15/8+o(1)}.
 \tag{13}
\]
Their internal relocation cost \(n_E T(h)^2\) is \(o(h^2)\).
The good-cap construction and its genuine-double factor cleanup retain
their other hypotheses and residual families. In particular, (13) alone
does not control P events incident to the odd-only singleton ranks.

Independent review: the complete written proof passed separate reviews.
These checked the sharpened form (3) against the source's B2 proof,
the short-interval endpoint in (7), both cases of (8), the weighted sums,
the large-height B2 hypotheses, and the single divisor factor in (1).
