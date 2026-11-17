# Equal-height bidirectional P templates have few genuine endpoints

15 November 2026. In the random folded-cap core, equal-hypotenuse
bidirectional P templates incident to surviving genuine doubles have only
\(h^{3/2+o(1)}\) genuine endpoints for suitable offsets. This includes
the equal-height mechanism in the earlier private-slot two-cycle examples.
It does not control bidirectional pairs with different hypotenuses, and
does not solve the remaining singleton parity system.

## 1. Setting and the equal-height alternative

Use the folded good-cap construction and a fixed-size spacing refinement.
The padded Hilbert side, both genuine coordinate interval lengths, and
both independent offset ranges are \(\Theta(h)\). The physical row
step \(D\), refinement size, and locality constants are fixed.
At a retained genuine object \(r\), the two rows have the exact forms
\[
 a_r=a_0+D(i_r-U_0),\qquad b_r=b_0+D(j_r-U_1),             \tag{1}
\]
where \((i_r,j_r)\) is its raw Hilbert cell. Its own gap satisfies
\[
 |b_r-a_r|\ge B_h,\qquad B_h/\sqrt h\longrightarrow\infty.\tag{2}
\]
Use all good virtual options at a potential partner object \(s\),
whether or not both are ultimately selected. At most one of its two
coordinates is replaced by a selected cap. Before selecting caps, union
over its raw coordinate and its dyadic ancestor cap coordinates.

An equal-hypotenuse bidirectional template consists of an actual horizontal
distance \(0<X\le h-1\), a common integer \(Z\le h-1\), and
\[
 X^2+(b_s-a_r)^2=Z^2=X^2+(b_r-a_s)^2.                    \tag{3}
\]
The phrase equal-hypotenuse is essential. Two integral distances with the
same horizontal component need not have the same hypotenuse.

Equation (3) has two alternatives. The negative-sign alternative gives
\[
 (b_r-a_r)+(b_s-a_s)=0.
\]
Actual P has rank separation \(O(h)\). Total virtual same-parity
locality therefore makes the difference of these own gaps \(O(\sqrt h)\).
This contradicts (2). Hence every surviving template satisfies
\[
 a_r+b_r=a_s+b_s.                                        \tag{4}
\]

## 2. A capped anti-diagonal level-set bound

Fix a source raw rank \(r\), and an interval \(I_r\) of \(O(h)\)
possible partner raw ranks. Hilbert locality puts its raw cells in a box
of side \(O(\sqrt h)\). At any fixed cap depth and for either cap
coordinate, the number of possible partner ranks satisfying
\[
 c_Q+H_N(s)_\beta=K                                     \tag{5}
\]
is \(O(\sqrt h)\), uniformly in the integer \(K\). Here \(Q\)
is the dyadic node at that depth containing \(s\), \(c_Q\) is its
common endpoint coordinate in the other axis, and \(\beta\) is the
uncapped coordinate. An uncapped partner has the same bound with
\(H_N(s)_0+H_N(s)_1=K\).

To prove (5), let the dyadic side be \(\ell\). If
\(\ell\le\sqrt h\), the qualifying squares in the raw box lie in
a strip of width \(O(\ell)\) about the line \(x+y=K\): the cap
coordinate is one of the two boundary coordinates of its square. There
are \(O(\sqrt h/\ell+1)\) such aligned squares, each contributing
at most \(\ell\) cells on the required coordinate row. If
\(\ell>\sqrt h\), the rank interval meets only \(O(1)\) such
nodes, and each fixed coordinate row has \(O(\sqrt h)\) cells in
the raw box. Both cases prove the bound. Summing over the
\(O(\log h)\) depths gives \(O(\sqrt h\log h)\) candidates.

## 3. Separate the folded coefficient cases

Each possible target row is either a fixed good anchor or one of its
folded affine branches. Write
\[
 a_s=c_0+D\sigma_0U_0,\qquad
 b_s=c_1+D\sigma_1U_1,
 \qquad \sigma_0,\sigma_1\in\{-1,0,1\}.                 \tag{6}
\]
The constants are deterministic once its raw/cap coordinate forms and
branches are chosen. All selection conditions may be omitted in an upper
bound. There are \(O(\log h)\) forms, since only one coordinate is
capped at a given object, and only constantly many branch choices.

For each fixed norm solution \((Y,Z)\) of \(X^2+Y^2=Z^2\),
equation (4) and \(b_s-a_r=\pm Y\) are two linear equations in
the offsets. Apart from fixed factors, their coefficient determinant is
\[
 \sigma_0\sigma_1-1.                                   \tag{7}
\]
If this is nonzero, at most one offset pair solves both equations. Its
probability is \(O(h^{-2})\).

If \(\sigma_0=\sigma_1=-1\), both target coordinates use their
central branches. Equation (4) reduces to the raw or capped sum condition
\[
 i_r+j_r=c_Q+H_N(s)_\beta
\]
or its uncapped version. Section 2 restricts the possible partner ranks to
\(O(\sqrt h\log h)\). The remaining norm equation fixes the offset
difference, with probability \(O(h^{-1})\) for each signed norm value.

The last singular case is \(\sigma_0=\sigma_1=1\). At least one
target coordinate is uncapped. That coordinate uses a reflected branch,
so its raw value lies outside its genuine coordinate interval (or exactly
at its boundary). Since the source is genuine and its raw rank is only
\(O(h)\) away, that genuine source lies within \(O(\sqrt h)\) of
a boundary of the genuine rectangle. Uniformly in the offsets, there are
only \(O(h^{3/2})\) such genuine cells. Remove all of them from the
double set for purposes of this estimate. This handles the singular
reflected case without any offset probability claim.

## 4. Count and scope of the resulting deletion

Put
\[
 \mathcal D_h=\max_{1\le n\le h}\tau(n^2)=h^{o(1)}.
\]
For each horizontal \(X\), factoring
\((Z-Y)(Z+Y)=X^2\) gives at most \(\mathcal D_h\) positive
norm pairs. In the nonsingular case there are \(O(h^2)\) source
ranks, \(O(h)\) possible partner ranks, and \(O(\log h)\) coordinate
forms. Its expected template count is therefore
\[
 O(h\mathcal D_h\log h).
\]
The central singular case instead has
\(O(h^2)\) source ranks and \(O(\sqrt h\log h)\) partners per
source. Its expected count is
\[
 O(h^{3/2}\mathcal D_h\log h).                            \tag{8}
\]
Repeated copies in a fixed-size refinement, or a finite union of bounded
origin displacements, change only the constants in this counting statement.
No new geometric permission to permute the refined core is asserted.

Combining (8) with the deterministic boundary set, some offsets have at
most \(h^{3/2+o(1)}\) genuine endpoints incident to these templates.
Their normalized count can be included in the same averaging objective
as cap area, small-factor incidence, and the other established costs.

Relocating every such genuine pair removes all genuine doubles from this
particular unavoidable-template obstruction. Each old slot can retain one
of its good points, and the internal pair-dependent relocation cost is
still \(h^{3/2+o(1)}\). This is a count of a justified exceptional set,
not a solution for the retained singletons: a bidirectional template
between singleton options can still constrain their parity choices, and
a unidirectional P event can remain after an erasure. Additional actual P
supports with unequal hypotenuses, forced paths, and all higher-arity
constraints remain outside the conclusion.

## Review status

The proof passed an independent written audit, recorded in
continuation_equal_height_p_two_cycles_independent_audit.md.
In particular,
the target-form union uses one selected cap coordinate per object. A
different interpolation with two independently capped coordinates would
require a new level-set bound.
