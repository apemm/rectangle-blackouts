# Good caps with prescribed endpoint anchors

15 November 2026. Independently reviewed in full. Folding the padding
coordinates allows a good cap core to start and end at a prescribed good
even row. Genuine labels are unchanged. The cap area and exceptional-label
counts retain their previous orders.

This is intended for the constant-odd-sea cores. The endpoint row can have
prime difference from the sea row, which is useful for a separate collar
argument. No complete collar or residual choice theorem is asserted here.

## 1. A folded extension of one coordinate

For a genuine coordinate interval `0,...,n-1` and a good anchor `a` in
that interval, define on all integers

\[
 \phi_a(z)=
 \begin{cases}
 \min(-z,a),&z<0,\\
 z,&0\le z\le n-1,\\
 \max(2(n-1)-z,a),&z>n-1.
 \end{cases}
 \tag{1}
\]

This map is 1-Lipschitz and leaves the genuine interval fixed. It equals
`a` for `z<=-n` and for `z>=2n`. Every value other than `a` has at most
three preimages. In particular, if `B` is a set of bad indices and the
anchor is good, then

\[
 |\phi_a^{-1}(B)|\le3|B|.
 \tag{2}
\]

Let `n=max(n_0,n_1)` and choose a power of two `8n<=N<16n`. Independently
choose each offset uniformly from the integer interval

\[
 2n\le U_\alpha\le N-3n.
 \tag{3}
\]

Compose the two raw Hilbert coordinates with
`phi_(a_alpha)(H_N(r)_alpha-U_alpha)`. Each coordinate retains the raw
square-root locality bound and has adjacent index increments at most one.
Both extreme raw coordinates zero and `N-1` map to the chosen anchor.
In fact every raw coordinate within `n` of either extreme maps to that
anchor. The left margin is at least `U_alpha-a_alpha>=n`; the corresponding
right margin follows from `U_alpha<=N-3n` and `n_alpha<=n`.

For every fixed raw coordinate, its folded value is bad for at most
`3b_alpha` offset choices. The offset range has order `h` in the intended
row blocks. Thus the bad-cap probability remains `O(b/h)`.

## 2. Cap area, occupancy, and endpoints

Apply the first-good-ancestor cap construction to these functions. The
root is good-cap, since either common endpoint coordinate has its good
anchor value. The bad-child area charge is unchanged. Hence the expected
selected cap area is `O(h b log h)`, and all but `O(h b log h)` genuine
labels remain doubles.

The genuine rectangle embeds unchanged in the padded square. At a padding
rank, folded coordinates can both be bad; unlike ordinary clipping, there
is no automatic good outside coordinate. Such ranks are still covered by
the same first-good-ancestor construction: its input is EVERY rank with
two bad values, including padding. Every selected cap has a bad child,
so the same area bound covers these additional ranks without a new cost.

The two total virtual cap functions retain their locality and adjacent
increment bounds. Each rank has at least one good option. Choosing even
whenever possible makes an odd-only rank require an unavailable even
virtual value. An even cap supplies a good value; outside even caps the
even virtual value is the folded raw coordinate. Therefore

\[
 |J|\le3N b_1,
 \tag{4}
\]

because each bad even index has at most three raw-coordinate preimages,
each occurring at exactly `N` Hilbert ranks. This deterministic count is
independent of the selected cap areas.

Orient the Hilbert square so its two endpoint corners share the even
coordinate. Its two endpoint even values are then the prescribed anchor
`a_1`. Caps preserve these endpoint values. The default selection at both
endpoints is even, since the anchor is good. Constant continuation at that
same even row preserves all same-parity locality inequalities by comparison
with the facing endpoint.

The first and last aligned Hilbert sub-squares of dyadic side comparable
to `n` lie in these corner neighborhoods. They contain only padding and
have both virtual options constant at their anchors. A selected cap can
either lie inside such a block or contain it, by dyadic laminarity. An
inside cap changes nothing there; a containing cap retains the anchor
value by comparison with the common endpoint. Thus each end has a constant
even selected region of `Theta(h^2)` coarse ranks. Further fixed-length
`O(h^2)` constant-even guards can be appended if a particular locality
bound requires a larger coefficient.

Replication or an independently proved fine interpolation then gives
occupied spacing-four cores with those endpoint anchors. Only actual
genuine labels remain doubles; all padding, cap, and added guard columns
are singletons.

## 3. Choose anchors suitable for constant-sea boundaries

For a low odd sea `L`, take the even anchor `b_*` in a fixed upper-strip
interval, for example `3h/4<b_*<7h/8`, with

\[
 b_*-L\text{ prime}.
 \tag{5}
\]

It must have the fixed even row residue of that core and avoid its bad
rows. The prime number theorem in fixed arithmetic progressions supplies
order `h/log h` candidates in the required odd residue modulo four. The
bad-row bound `h^(5/6+o(1))` removes fewer candidates, so such a good anchor
exists for all sufficiently large heights. This uses only the classical
fixed-modulus consequence; a primary modern treatment is
[Thorner and Zaman, *Refinements to the prime number theorem for arithmetic
progressions*](https://arxiv.org/abs/2108.10878).

Choose the odd anchor to be the last good odd row near the TOP strip edge.
Its distance from that edge is `O(b+1)`. This remains within the allowed
upper-half odd row interval.

For a high odd sea `H=h-O(1)`, reflect these choices: take a good even
anchor in a fixed lower-strip interval with `H-b_*` prime, and take the
odd anchor near the BOTTOM strip edge. The odd anchor stays in the allowed
lower-half odd interval. The original genuine even interval includes the
chosen anchor in both cases; the finite bulk exclusions do not affect it.

## 4. The exceptional-source P incidence survives

This section concerns the virtual-cap default with EVEN preference, so
every exceptional odd source requires a bad raw folded even value.
It does not use the older rule that always selected an odd cap's own row.

Each candidate coordinate is one of three affine branches of a raw or
ancestor coordinate, with offset coefficient `+1` or `-1`, or its fixed
anchor. Enumerating these branches multiplies earlier candidate counts by
only a constant.

If the odd source is nonconstant, its own offset has nonzero coefficient.
Badness of its even option restricts the independent even offset to at
most `3b_1` values. For a fixed norm solution, the odd offset is then fixed,
whether the target even coordinate is affine or equals its anchor. This
gives the same `O(b D_h/h^2)` point-pair bound as the two-unclamped case.

If the odd source equals its fixed anchor, it is within `O(b+1)` of a
strip edge. The in-strip alternate corners therefore restrict the slot
gap to `O(sqrt((b+1)h))`. If the even target is nonconstant, a norm solution
fixes its offset, giving the previous one-offset bound. If it is constant,
the two fixed rows admit only divisor-many gaps; charge these to `|J|`.

Thus the previous exceptional-source bound retains the order

\[
 O\bigl(hb D_h\log^2 h+
 h^{3/2}\sqrt{b+1}\,D_h\log h\bigr)
 =h^{23/12+o(1)}.
 \tag{6}
\]

Select offsets jointly with the cap-area objective. The even anchor need
not lie near a strip edge: the two-offset argument handles an anchored
even target. The odd anchor's proximity to an edge is essential in the
remaining one-offset case.

The genuine-source small-factor count likewise survives because its odd
row is affine in the odd offset; every target option is affine in the
independent even offset or constant. This retains the nearly linear P
gap after the same sparse source erasure, for a fixed finite refinement
union whose candidate rows have these affine forms. A new interpolation
must verify that finite-union hypothesis separately.

Independent review checked the folded map and three-preimage bound, bad
padding coverage, deterministic forced-odd count, prescribed endpoints,
constant corner guards, the fixed-modulus prime count, and both P incidence
transfers. The argument passed on 15 November 2026. The remaining residual
constraint solvability is not part of this review conclusion.
