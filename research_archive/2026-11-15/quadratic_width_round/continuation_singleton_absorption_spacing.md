# A spacing criterion for replacing odd stubs by good even rows

15 November 2026. Nearest-anchor extension gives a controlled way to add
good even rows at selected odd-only slots. It requires a spacing condition
on those slots. A large gap in the set of good rows explains why a mere
bound on the number of inserted points cannot replace that condition.

This is a geometric and counting reduction. It does not prove that the
exceptional P sources in the cap construction satisfy the condition, or
that the added even points avoid P and the mixed supports.

## 1. Extension from separated insertion ranks

Let \(E\) be a nonempty set of integer ranks carrying even rows
\(f:E\to G\), where \(G\) is any prescribed set of good even rows.
Assume
\[
 |f(e)-f(e')|\le C\sqrt{|e-e'|}.                           \tag{1}
\]
For an insertion rank \(r\notin E\), let
\(\delta_r=\operatorname{dist}(r,E)\), and choose a nearest anchor
\(e_r\in E\). Assign the new even row
\[
 \widetilde f(r)=f(e_r).                                  \tag{2}
\]
Every inserted value is good. For an old rank \(e\),
\[
 |e_r-e|\le\delta_r+|r-e|\le2|r-e|,
\]
so the old/new Hölder constant is at most \(\sqrt2C\).

If the insertion set \(R\) satisfies, for some fixed \(c>0\),
\[
 |r-s|\ge c\max(\delta_r,\delta_s)
       \qquad(r,s\in R,\ r\ne s),                       \tag{3}
\]
then
\[
 |e_r-e_s|\le|r-s|+\delta_r+\delta_s
             \le(1+2/c)|r-s|.
\]
Thus the extension on \(E\cup R\) has Hölder constant
\[
 C'=C\max\{\sqrt2,\sqrt{1+2/c}\}.                        \tag{4}
\]
No bound on the gaps of \(G\) is needed. The stride can be enlarged
by the corresponding fixed squared factor before constructing the core.

## 2. Dense local clusters are also permitted

Partition \(R\) into clusters \(R_j\). Put
\(\delta_j=\operatorname{dist}(R_j,E)\), and suppose
\[
 \operatorname{diam}(R_j)\le\eta\delta_j,
 \qquad
 \operatorname{dist}(R_j,R_k)
       \ge c\max(\delta_j,\delta_k)\quad(j\ne k).         \tag{5}
\]
Choose \(r_j\in R_j\) and \(e_j\in E\) realizing
\(|r_j-e_j|=\delta_j\), and give all of \(R_j\) the row
\(f(e_j)\). Then every \(r\in R_j\) has
\(|r-e_j|\le(1+\eta)\delta_j\), while
\(\operatorname{dist}(r,E)\ge\delta_j\). The same comparisons
as in Section 1 give
\[
 C'=C\max\left\{\sqrt{2+\eta},
                 \sqrt{1+2(1+\eta)/c}\right\}.            \tag{6}
\]
Within one cluster the added even row is constant. This permits arbitrary
insertion density inside a cluster, but it does not permit clusters to
bridge a long missing-row transition without separation.

## 3. A necessary barrier at a gap in the good rows

Suppose \(G\) contains no row strictly between \(a<b\), and write
\(g=b-a\). Any \(C'\)-Hölder extension at occupied even ranks has
\[
 |r-s|\ge g^2/(C')^2                                     \tag{7}
\]
whenever its value at \(r\) is at most \(a\) and its value at
\(s\) is at least \(b\).

In particular, let two retained even anchors have values on opposite
sides of this good-row gap. Sort every rank that will carry an even point
between those anchors. Somewhere two consecutive ranks in this sorted
list cross from one side of the row gap to the other. Their rank gap is
at least \(\lceil g^2/(C')^2\rceil\). Therefore at least
\[
 \max\{0,\lceil g^2/(C')^2\rceil-1\}                     \tag{8}
\]
consecutive intervening slots must remain without an even point.

This barrier already occurs with just two allowed even rows \(G=\{a,b\}\).
In that case it is exact: form a graph on the proposed occupied even ranks
by joining ranks at distance less than \(g^2/(C')^2\). A completion exists
if and only if no connected component contains fixed anchors of both
values. Assign each component one of the two values, respecting its fixed
anchors. In the sorted rank order, the components are separated precisely
by consecutive rank gaps at least \(g^2/(C')^2\).

Consequently, even a subquadratic set of proposed insertions can obstruct
a fixed Hölder constant. Its total size does not control the local gaps
in (7). Filling every rank with an even point is impossible whenever it
must cross a good-row gap larger than \(C'\).

## 4. What an absorption operation must still count

At an odd-only slot with row \(a\), replacing that point by a chosen
good even row \(b\) preserves occupancy and leaves the number of black
points unchanged. It destroys every P event using that old odd point.
It can create P events in which the new point is the even endpoint.
It can also create new mixed supports. The same-parity geometric bound
alone does not exclude these new events.

If the complete row-pair construction needs the pair \((a,b)\) to have
a designated owner elsewhere, relocating that pair requires a separate
excess count. Removing a double from its former slot leaves one fewer
point there; adding that double in the external region restores exactly
that unit of excess. If several replacements choose the same pair,
relocate the pair only once. If its owner has already been relocated,
there is no additional pair to relocate. These bookkeeping operations
do not remove the new P incidences automatically.

Applied to the cap construction, (3) or (5) would provide a valid
good-row extension at selected exceptional odd stubs. A useful repair
must additionally show that the chosen rows create only a controllable
family of incoming P events, and that any subsequent erasure leaves all
slots occupied. Those requirements remain open.

Independent review checked both extension constants, the good-row-gap
barrier and integer ceiling, the exact two-value criterion, and the
separate excess and support qualifications. The complete written note
passed that review on 15 November 2026.
