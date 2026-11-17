# All-double boards through a near-quadratic range of widths

Research note, 11 November 2026. This extends
[the regular-square local-lemma construction](continuation_regular_square_local_lemma.md).
No source manuscript or earlier theorem is changed. The proof received an independent audit.

**Theorem.** There are absolute constants \(c>0\) and \(h_0\) such that, for every \(h\ge h_0\), every integer
\[
 h\le m\le \frac{c h^2}{(1+\log h)^2},             \tag{1}
\]
and every prescribed balanced partition \(A\sqcup B=[h]\), a valid \(h\times m\) blackout exists with exactly one black row from each part in every column.

The row degrees can be prescribed to differ by at most one within each part. More precisely, for each \(P\in\{A,B\}\), choose integers
\[
 d_r\in\{\lfloor m/|P|\rfloor,\lceil m/|P|\rceil\},
 \qquad \sum_{r\in P}d_r=m.
\]
The construction has exactly \(d_r\) black points in row \(r\).

Consequently
\[
 f(h,m)\ge2m
\]
throughout (1). These are actual valid all-double boards, not merely placements of labels or corner-free scaffolds.

## 1. The clone probability space

Give each row \(r\) exactly \(d_r\) labeled clones. There are \(m\) clones in each row part. Independently choose a uniform bijection from the \(m\) columns to the clones in \(A\), and another to the clones in \(B\). Erase the clone labels.

Every column has exactly two black points, one in each part. Every row has its prescribed degree. Put
\[
 D=\max_r d_r.
\]
Since \(m\ge h\) and the partition is balanced,
\[
 D\le4m/h.                                        \tag{2}
\]

A geometric support of \(k\) distinct cells is encoded by choosing a clone for each cell. The row part determines the permutation coordinate. Inconsistent partial bijections are discarded. Every surviving canonical event has probability
\[
 p_E=\frac1{(m)_{k_A}(m)_{k_B}}
 \le C m^{-k},\qquad k_A+k_B=k\le6,               \tag{3}
\]
uniformly for sufficiently large \(m\).

The negative dependency graph joins events sharing a domain or clone-image resource in either permutation. The explicit swap proof in Section 6 of the regular-square note applies without change. It is a product-space version of the canonical-event principle in
[Lu and Székely, Theorem 1](https://people.math.sc.edu/lu/papers/randinj.pdf).
Their Lemma 3 supplies the asymmetric local lemma and its product lower bound.

## 2. Which supports need to be excluded

As in the regular-square proof, it suffices to exclude:

- all four-corner rectangles;
- mixed four-supports from a pair of rectangles sharing two corners, where the shared pair is a side in one and a diagonal in the other;
- six-supports from two rectangles sharing exactly one corner.

The same-side and same-diagonal four-support cases reduce to a four-corner rectangle. Disjoint collisions contain hidden rectangles. Three common corners force the rectangles to be equal. Common cells are not assigned a color.

One large six-support family is impossible in the present probability space. Two distinct axis rectangles sharing just \((x,a)\) have other columns \(y,z\) and other rows \(b,c\). Their symmetric difference requires the three row pairs
\[
 \{b,c\}\text{ at }x,\qquad
 \{a,b\}\text{ at }y,\qquad
 \{a,c\}\text{ at }z.
\]
They form a triangle on the rows. They cannot all cross the bipartition \(A,B\). Therefore a feasible six-support has at least one tilted rectangle.

This exclusion is essential when \(m/h\) grows.

## 3. Relative rectangle-shape counts

Let \(\Lambda=1+\log h\). Count relative shapes before translation.

For a tilted rectangle, orient its primitive side directions as
\[
 U=k(a,b),\qquad V=\ell(-b,a),
 \qquad a,b,k,\ell>0,\quad\gcd(a,b)=1.
\]
Signs and corner choices cost an absolute factor. The vertical span restriction implies
\[
 kb+\ell a\le h-1,
\]
so \(k\le h/b\) and \(\ell\le h/a\). Dropping the remaining restrictions gives
\[
 D_t\le C\sum_{a,b\le h}\frac{h^2}{ab}
 \le C h^2\Lambda^2.                              \tag{4}
\]
This bound is independent of \(m\).

Axis rectangle shapes satisfy
\[
 D_a\le Cmh.                                      \tag{5}
\]

For six-supports with at least one tilted rectangle, choose both shapes and their common corner. Therefore the number of relative shapes is
\[
 S_6\le C(D_aD_t+D_t^2)
 \le C(mh^3\Lambda^2+h^4\Lambda^4).               \tag{6}
\]
A specified black support point and its role fix the translation.

## 4. Four-supports, including the axis-side case

Hidden rectangles contribute \(O(D_a+D_t)\).

For a mixed side/diagonal support, first choose the rectangle in which the common pair is a side. The complementary black diagonal of the other rectangle has the same length as that side.

If the first rectangle is tilted, (4) gives its shape count. Its side length squared is at most \(m^2+h^2\). Under (1), \(m\le h^2\), so the elementary bound
\[
 r_2(N)\le4\tau(N)=O_\eta(h^\eta),\qquad N\le2h^4
\]
gives
\[
 S_{4,t}\le C_\eta h^{2+\eta}\Lambda^2.            \tag{7}
\]
Here \(\eta>0\) is fixed and the exponent in the divisor estimate is rescaled accordingly.

If the first rectangle is axis-aligned and the common side is horizontal of length \(L\), there are \(O(h)\) connector choices and \(r_2(L^2)\) choices for the other diagonal. For a vertical common side, there are \(O(m)\) connector choices. Thus
\[
 S_{4,a}
 \le C\left(h\sum_{L\le m}r_2(L^2)
          +m\sum_{L\le h}r_2(L^2)\right).         \tag{8}
\]

The needed average is elementary:
\[
 \tau(L^2)=\sum_{d\mid L}2^{\omega(d)}
 \le\sum_{d\mid L}\tau(d),
\]
and therefore
\[
 \sum_{L\le X}r_2(L^2)
 \le4X\sum_{d\le X}\frac{\tau(d)}d
 \le4X(1+\log X)^2.                              \tag{9}
\]
Because \(m\le h^2\), equations (8)–(9) give \(S_{4,a}=O(mh\Lambda^2)\).

Combining these counts,
\[
 S_4\le C_\eta(mh\Lambda^2+h^{2+\eta}\Lambda^2).   \tag{10}
\]
All side vectors and connectors join actual corners, so there is no uncontrolled half-integral translation parameter. Integrality and containment filters can only reduce these upper bounds.

## 5. The clone powers cancel

A fixed domain resource specifies a column in one permutation coordinate. Choose which of the \(k\) support points uses it. Its row has at most \(h\) choices, its relative shape has at most \(S_k\) choices, and all cells together have at most \(D^k\) clone assignments. Using (2) and (3), its incident event mass is at most
\[
 C h S_k\frac{D^k}{m^k}
 \le C\frac{S_k}{h^{k-1}}.                       \tag{11}
\]

A fixed image resource specifies one particular clone of one row. The corresponding support point has at most \(m\) column choices. Its own clone is fixed, leaving at most \(D^{k-1}\) assignments. Its incident mass is at most
\[
 C m S_k\frac{D^{k-1}}{m^k}
 \le C\frac{S_k}{h^{k-1}}.                       \tag{12}
\]
Repeated row or column restrictions are handled by discarding inconsistent canonical events. They do not increase either count.

Equations (6), (10), (11), and (12) give the uniform resource load
\[
 \rho\le C_\eta\left(
 \frac{m}{h^2}\Lambda^2
 +h^{-1+\eta}\Lambda^2
 +\frac{\Lambda^4}{h}
 \right).                                        \tag{13}
\]

Fix \(\eta=1/2\). Choose the absolute constant \(c\) in (1) sufficiently small, and then choose \(h_0\) sufficiently large. This makes \(24\rho\le1/2\).

Each event uses at most twelve resources. Set \(x_E=2p_E\). Then
\[
 x_E\prod_{F\sim E}(1-x_F)
 \ge2p_E\left(1-\sum_{F\sim E}x_F\right)\ge p_E.
\]
The negative-dependency local lemma gives positive probability of avoiding every forbidden support. Section 2 then gives actual validity. This proves the theorem.

## 6. Counting the prescribed-degree family

Let \(B_{h,m,\pi,\mathbf d}\) count the valid boards with the specified row partition and row degrees. The probability space has \((m!)^2\) outcomes. Every physical board has exactly
\[
 \prod_{r=1}^h d_r!
\]
clone realizations.

There are \(4m\) resources. The bounded load (13) implies \(\sum_Ep_E=O(m)\). Since the event probabilities tend uniformly to zero, the product conclusion of the local lemma is at least \(\exp(-Cm)\). Hence
\[
 e^{-Cm}\frac{(m!)^2}{\prod_r d_r!}
 \ \le B_{h,m,\pi,\mathbf d}\le
 \frac{(m!)^2}{\prod_r d_r!}.                      \tag{14}
\]
The upper expression counts all boards with those degree and row-part restrictions.

If
\[
 h\le m=o\!\left(h^2/\Lambda^2\right),
\]
then the resource load \(\rho\) in (13) tends to zero. The same argument improves the loss in (14) to \(\exp(-O(m\rho))=\exp(-o(m))\). Therefore
\[
 \log B_{h,m,\pi,\mathbf d}
 =2\log(m!)-\sum_r\log(d_r!)+o(m).                \tag{15}
\]
This limit is uniform in the balanced partition and the prescribed floor/ceiling allocation.

This is a count of the constructed all-double family. It is not a count of maximum blackouts.

## 7. What the theorem leaves open

The largest allowed widths in (1) have order \(h^2/\log^2h\). Their row degrees have order \(h/\log^2h\). Thus arbitrary all-double validity persists well beyond bounded row degree and beyond fixed aspect ratio.

The saturated equality problem requires
\[
 m=q_h\sim h^2/4
\]
and every edge of the balanced complete bipartite row graph. The load term \((m/h^2)\Lambda^2\) is then no longer bounded by a small constant. The proof therefore does not establish a saturated construction or disprove \(m_h>q_h\).

The construction permits tilted rectangles with three black corners when their singleton presentations remain unique. It does not refute the separate corner-free conjecture considered in the follow-up notes.

