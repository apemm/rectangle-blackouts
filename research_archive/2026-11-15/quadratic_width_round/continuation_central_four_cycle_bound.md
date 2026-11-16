# All-direction central P four-cycles have subquadratic incidence

15 November 2026. Under the multiscale complementary row sampling, the
expected number of central genuine P four-cycles is
\(h^{43/22+o(1)}\). The proof uses the mixed spanning-tree probability
bound and a close-height arithmetic count. Repeated raw coordinates are
included. No fixed direction palette or minimum-P-gap hypothesis is
needed, apart from the existing exclusion of bounded copies when those
are present in the provenance model.

This is an incidence theorem. It does not assign the parities of the
remaining singleton points, bound cycles through arbitrary caps or
anchors, or control cycles of growing length.

## 1. Inputs and precise scope

Use the independent parity fields and offsets of
[the multiscale sampling note](continuation_multiscale_row_sampling.md).
The four distinct genuine central objects have raw cells
\((i_v,j_v)\), indexed in directed cycle order \(v\pmod4\). Their
fixed signed norm-height requirements are
\[
                      b_{v+1}-a_v=Y_v.              \tag{1}
\]
Actual P edges have horizontal span below \(h\). Thus all four objects
lie in an \(O(h)\) rank interval and an \(O(\sqrt h)\) raw-coordinate
box. The physical row functions have uniformly bounded successive gaps
and uniformly bounded-error central representations.

As in [the mixed-path note](continuation_mixed_path_tree_probability.md),
let \(P_0\) order the vertices by \(i_v\), and let \(P_1\) order them
by \(j_{v+1}\). The latter is the even order after the cyclic shift in
(1). Each consecutive edge has weight one plus its raw-coordinate gap.
Let \(Q_0,Q_1\) be the products of the three weights in the two paths.
Their minimum-product union-tree value is \(\tau\). For specified
norm heights,
\[
             \Pr((1))\le {h^{o(1)}\tau\over hQ_0Q_1}
                    \le {h^{o(1)}\over h\max(Q_0,Q_1)}.        \tag{2}
\]

The same fixed bounded provenance and target-error qualifications as in
that note apply. All candidates are enumerated before sampling. The two
complementary classes in one parity are treated separately and then
combined by a finite union. Independent sampled anchor insertion is
allowed; constant-anchor objects themselves are not part of this theorem.

## 2. Discard the outer product ranges

For each fixed \(\varepsilon>0\), the elementary low-product and
arithmetic high-product bounds in
[the product-gap reduction](continuation_repeated_coordinate_cycle_reduction.md)
give
\[
 \mathbb E\#\{\min(Q_0,Q_1)\le h^{1-\varepsilon}\}
                   \le h^{2-\varepsilon+o(1)},
\]
\[
 \mathbb E\#\{\max(Q_0,Q_1)\ge h^{1+\varepsilon}\}
                   \le h^{2-\varepsilon+o(1)}.        \tag{3}
\]
The first estimate counts small product-gap tuples in one parity and
harmonically sums the other parity. The second uses the all-direction
\(h^{4+o(1)}\) rank-and-height candidate count and (2).
It remains to treat
\[
                    h^{1-\varepsilon}<Q_0,Q_1<h^{1+\varepsilon}.
                                                               \tag{4}
\]

## 3. Close edge-coordinate points give close heights

Associate to each directed edge its coordinate point
\[
                           E_v=(i_v,j_{v+1}).        \tag{5}
\]
These are not the raw cells of the original objects. If two such points
satisfy \(\|E_u-E_v\|_\infty\le R\), bounded row gaps imply
\[
                         |Y_u-Y_v|\le C(R+1).       \tag{6}
\]
Indeed \(Y_u-Y_v=(b_{u+1}-b_{v+1})-(a_u-a_v)\), and each physical
row difference is at most a fixed multiple of its raw-coordinate
difference, plus the permitted bounded error.

For \(1\le R\le C\sqrt h\), the number of rank-and-height candidates
with at least one close pair as in (5) is at most
\[
                              h^{7/2+o(1)}R.         \tag{7}
\]
To see this, take a finite union over the six pairs. By cyclically rotating
the four edges, and exchanging the two members of the selected pair if
necessary, arrange that one member is edge 2 and the other is edge 0 or 1.
For adjacent edges place the later member at edge 2; for opposite edges
place either member at edge 2. This costs only a fixed factor.

Choose the first object in \(O(h^2)\) ways and the second in \(O(h)\).
The first fixed horizontal leg has divisor-many signed heights \(Y_0\).
Locality gives \(|Y_1-Y_0|=O(\sqrt h)\), so \(Y_1\) has
\(O(\sqrt h)\) possibilities, each with divisor-many horizontal legs
and hence third columns. Now (6) allows only \(O(R)\) values for
\(Y_2\), since its close partner height is already known. Its norm
factorization fixes the fourth column up to a divisor factor. The closing
horizontal gap has divisor-many heights \(Y_3\). This proves (7).
Invalid, repeated-column, out-of-strip, and wrong-residue candidates may
be discarded. No independence between heights is assumed.

Set
\[
                             R=h^{1/2-\eta},         \tag{8}
\]
where \(0<\eta<1/2\) is fixed. In the critical range (4), (2) costs
at most \(h^{-2+\varepsilon+o(1)}\). Equations (7)--(8) therefore
bound all close-pair cycles by
\[
                             h^{2-\eta+\varepsilon+o(1)}.      \tag{9}
\]

## 4. If no pair is close, a tree exchange gives the gain

Choose a minimum-weight edge \(uv\) of \(P_0\), with weight \(e\).
There are three path edges, so
\[
                             e\le Q_0^{1/3}.         \tag{10}
\]
This holds also when coordinates repeat: then a zero gap simply gives
weight one. No distinct-coordinate case split is needed.

Assume
\[
                       {1+\varepsilon\over3}<\frac12-\eta.    \tag{11}
\]
Then (4), (8), and (10) imply \(|i_u-i_v|<R\) for sufficiently large
\(h\). If the pair is not already covered by Section 3, it must satisfy
\[
                            |j_{u+1}-j_{v+1}|>R.     \tag{12}
\]
The unique path between these two vertices in \(P_1\) has at most
three edges and total raw-coordinate gap equal to the difference in
(12). One of its edge weights is therefore greater than \(R/3\).
Insert the edge \(uv\) into \(P_1\), and delete such a largest edge.
The resulting tree has product at most \(3Q_1e/R\). Thus
\[
                       \tau\le3Q_1e/R,
\]
and (2), (10) give the uniform probability bound
\[
 \Pr((1))\le {h^{o(1)}e\over hQ_0R}
                \le {h^{o(1)}\over hQ_0^{2/3}R}.     \tag{13}
\]
There are at most \(h^{4+o(1)}\) rank-and-height candidates in all
directions. Using the lower bound for \(Q_0\) in (4), the expected
contribution of (12) is at most
\[
                           h^{11/6+\eta+2\varepsilon/3+o(1)}. \tag{14}
\]
Repeated coordinates either supply an even smaller replacement edge or
fall into the close-height case. They introduce no additional exception.

## 5. Balance the exponents

Choose
\[
                         \varepsilon={1\over22},
                         \qquad\eta={1\over11}.     \tag{15}
\]
Condition (11) holds, since \(23/66<9/22\). The three exponents in
(3), (9), and (14) all equal
\[
                  2-\varepsilon
                   =2-\eta+\varepsilon
                   ={11\over6}+\eta+{2\varepsilon\over3}
                   ={43\over22}<2.                 \tag{16}
\]
Every central genuine four-cycle belongs to one of those cases. Therefore
\[
           \mathbb E\#\{\text{central genuine P four-cycles}\}
                          \le h^{43/22+o(1)}.        \tag{17}
\]
The same bound applies to their incident genuine objects. It can enter
a joint nonnegative-cost averaging argument and remains subquadratic
after the existing \(h^{o(1)}\) relocation factor, provided the separate
support-erasure and occupancy hypotheses of that relocation step hold.

The mixed-path hierarchy by itself left aligned small-gap patterns.
Those patterns necessarily offer the close edge-coordinate pair used in
Section 3, so they do not remain an exception for four-cycle incidence.
This argument does not yet give a uniform estimate for longer cycles,
because after using one close-height relation more free heights remain.
It also leaves the stated folded/cap/singleton choice questions open.

## Review status

The mixed-tree input was independently audited. The close-height count,
repeated-coordinate treatment, tree-exchange dichotomy, and optimized
exponents were independently derived in parallel. The complete saved
proof then passed a final independent written review, including the
rotation of the selected height pair, the weight-one cases, and all three
exponents in (16).
