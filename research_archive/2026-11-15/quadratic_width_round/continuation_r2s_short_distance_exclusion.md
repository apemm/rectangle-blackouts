# Short column distances cannot support a bulk R2s collision

15 November 2026. In a row-one sea, a crossed R2s support has an exact
cubic lower bound on the separation of its two core columns. Consequently,
a fixed-width permutation block has no internal R2s constraints once its
rows are sufficiently far above the sea. This removes the internal-pair
qualification from an external matching argument in that specific regime.
It does not bound the external constraints or solve simultaneous moves.

## 1. Exact distance bound

Write the black support as

\[
 A=(0,y),\quad B=(U,1),\quad
 C=(X,y+\delta),\quad D=(X+V,1),
\]

where the two core points use one fixed row residue modulo four and
their columns belong to `4Z`. The sea points are outside `4Z`.
Assume `y>1`. The common rows are `y+delta/2` and `1+delta/2`.
After choosing the lower core point as the black-side owner, a
nondegenerate in-strip support therefore has `delta>0`, divisible by four.
Reflect horizontally to make `X>0`. Put `n=y-1` and
`T=2X+V-U`. The exact equations are

\[
 TU=n\delta,\qquad
 V^2-U^2=-2n\delta-\delta^2,\qquad
 2X=U+T-V.
 \tag{1}
\]

Eliminating V gives

\[
          4U(X-T)=(2X-T)^2+\delta^2.
 \tag{2}
\]

The right side is positive. Because `TU=n delta>0`, U and T have
the same sign. Equation (2) then forces `0<T<X`: negative T would
make U negative while `X-T` remains positive.

Set `a=X-T`. Both X and T are even, so `a>=2`. In these variables,

\[
 n\delta={ (X-a)((X+a)^2+\delta^2)\over4a}
 ={1\over4}\left(
 {X(X^2+\delta^2)\over a}+X^2-Xa-a^2-\delta^2
 \right).
 \tag{3}
\]

For fixed X and delta, the last expression strictly decreases with
positive a. Hence every such support satisfies

\[
        n\delta\le
        {(X-2)((X+2)^2+\delta^2)\over8}.
 \tag{4}
\]

If the lower core row is `3 mod4`, then `n=2 mod4`.
Since delta is divisible by four and `U` is not divisible by four,
`TU=n delta` forces T to be divisible by four. Thus `a>=4`, and
the sharper bound is

\[
        n\delta\le
        {(X-4)((X+4)^2+\delta^2)\over16}.
 \tag{5}
\]

These bounds require neither a row filter nor a Hilbert order.
Exact divisibility can make them strict. They are necessary geometric
conditions, not sufficient tests for a support.

## 2. Consequences under the same-parity norm gap

Suppose `delta^2<=2X`. Since `delta>=4`, (4) gives

\[
 y-1\le {(X-2)(X^2+6X+4)\over32}.
 \tag{6}
\]

For lower rows `3 mod4`, (5) instead gives

\[
 y-1\le {(X-4)(X^2+10X+16)\over64}.
 \tag{7}
\]

In particular, core-column separation is `Omega(y^(1/3))`.
The isolated spacing-four seam exception has `X=delta=4`.
Even without the norm gap, (4) then gives `y-1<=13/4`.
Thus these exceptions do not create bulk R2s supports.

The exponent and leading constant in the odd-row bound are sharp
asymptotically. The family in
[the actual Hilbert domino obstruction](continuation_r2s_hilbert_domino_obstruction.md)
has

\[
 X=4q,\quad\delta=4,\quad T=X-4,\quad
 y-1=q^3+q^2-2.
\]

It attains (5) exactly for every even `q>=2`. Its two core columns
are only of order `h^(1/3)` apart, although the complete sea support
has horizontal span of order `h^(2/3)`.

## 3. A complete R2s matching conclusion for a fixed bulk block

Take a permutation block of physical width at most W, where W is
fixed independently of height. Assume every proposed same-parity
pair satisfies the norm gap, apart from isolated seam pairs as above.
If every row in the block exceeds

\[
  5+\max\left(0,{(W-2)(W^2+6W+4)\over32}\right),
 \tag{8}
\]

there is no internal crossed R2s support, for any permutation.
For W below the minimum possible nonzero core separation, the
conclusion is immediate. Otherwise (6) and the seam bound prove it.

Therefore an external perfect matching, such as the explicit two-sided
degree criterion in
[the forbidden-row reduction](continuation_r2s_stride_and_permutation_reduction.md),
avoids every crossed R2s support involving at least one label in this
block, provided the fixed outside board is held unchanged. If the
separate same-parity geometry also excludes grouped two-core/two-sea
mixed supports, this covers the whole two-core/same-sea mixed family.

This conclusion is local to R2s. P, three-core supports, four-core
supports, and parked-triangle coincidences remain separate constraints.
The external Hall hypothesis can fail, as the actual domino and
arbitrary-boundary examples demonstrate.

Independent written review passed the exact expansion and strict
monotonicity, the two divisibility thresholds, both cubic bounds,
the seam exception, and the fixed-width matching consequence with
the outside labels held fixed.
