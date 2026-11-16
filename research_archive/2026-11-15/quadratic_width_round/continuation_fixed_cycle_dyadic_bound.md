# A dyadic product-gap bound for fixed central P cycles

15 November 2026. The mixed-tree and close-height arguments give, for
every fixed \(k\ge3\),
\[
 \mathbb E\#\{\text{central genuine P \(k\)-cycles}\}
 \le h^{\,1+(2k-1)(k-1)/(2(4k-5))+o(1)}.             \tag{1}
\]
In particular the three-cycle exponent improves from \(7/4\) to
\(12/7\). The four-cycle exponent is \(43/22\), agreeing with
[the direct four-cycle proof](continuation_central_four_cycle_bound.md).
For five-cycles this argument gives \(11/5\), so it does not settle
longer cycles or the singleton occupancy problem.

## 1. Inputs and scope

Use the genuine central multiscale model of
[the product-gap reduction](continuation_repeated_coordinate_cycle_reduction.md).
The fixed cycle has \(k\) distinct objects, signed norm heights
\(b_{v+1}-a_v=Y_v\), and two weighted paths on its edge indices:
the odd coordinate order and the cyclically shifted even coordinate
order. Consecutive weights are one plus the corresponding raw gap.
Write their products as \(Q_0,Q_1\), and put \(Q=\max(Q_0,Q_1)\).

All objects lie in an \(O_k(h)\) rank interval, hence their raw
coordinate extents are \(O_k(\sqrt h)\). Therefore
\[
                   1\le Q\le C_k h^{(k-1)/2}.         \tag{2}
\]
The reviewed input estimates are:
\[
 \mathbb E\#\{\min(Q_0,Q_1)\le T\}\le h^{1+o(1)}T,
                                                               \tag{3}
\]
\[
 \#\{\text{rank-and-height candidates}\}
                    \le h^{k/2+2+o(1)},              \tag{4}
\]
and the [mixed-tree probability bound](continuation_mixed_path_tree_probability.md)
\[
 \Pr(\text{fixed heights})
       \le {h^{o(1)}\tau\over hQ_0Q_1}
       \le {h^{o(1)}\over hQ},                        \tag{5}
\]
where \(\tau\) is the minimum product over spanning trees in the union
of the two weighted paths.

The estimates concern all actual in-strip P directions. They retain
the fixed bounded genuine-provenance qualifications of the cited
notes. They do not include arbitrary cap or anchor objects, or cycles
whose length grows with \(h\).

## 2. One close edge-coordinate pair saves a height choice

For each cycle edge set \(E_v=(i_v,j_{v+1})\). If
\(\|E_u-E_v\|_\infty\le R\), bounded row gaps give
\[
                         |Y_u-Y_v|\le C_k(R+1).      \tag{6}
\]
For every fixed \(k\ge3\) and \(1\le R\le C_k\sqrt h\), the number
of rank-and-height candidates with such a pair is at most
\[
                         h^{k/2+3/2+o(1)}R.         \tag{7}
\]

Here is the rotation detail. Of the two directed cyclic distances
between the selected edge indices, at least one is at most \(k-2\).
Orient the selected pair using that distance and rotate the cycle so
its later member is edge \(k-2\). The other member is now among
edges \(0,\ldots,k-3\). Thus its height has already been enumerated
when \(Y_{k-2}\) is chosen.

The usual count chooses the first two objects and \(Y_0\), then
enumerates the \(k-2\) further free heights in intervals of
length \(O_k(\sqrt h)\). Each norm factorization fixes the next
horizontal leg up to \(h^{o(1)}\) choices; the final closing height
also has divisor-many choices. Equation (6) replaces one free
\(\sqrt h\) factor by \(O_k(R)\). This proves (7), including repeated
edge-coordinate points.

## 3. A bin with product gap of order \(Z\)

Fix a dyadic bin \(Z\le Q<2Z\). Choose the parity path whose product
equals \(Q\), and let \(e\) be its smallest edge weight. Then
\[
                            e\le Q^{1/(k-1)}.        \tag{8}
\]
Choose, with a sufficiently large fixed constant depending on \(k\),
\[
                  R=C_k h^{1/4} Z^{1/(2(k-1))}.       \tag{9}
\]
Equation (2) implies \(e\le R\) and \(R\le C'_k\sqrt h\).

If the endpoints of that edge are also within \(R\) in the other
coordinate, (7) and (5) give a contribution at most
\[
 {h^{k/2+3/2+o(1)}R\over h Z}
 =h^{k/2+3/4+o(1)}
                    Z^{-(2k-3)/(2k-2)}.              \tag{10}
\]

Otherwise their other-coordinate difference exceeds \(R\).
The other path contains a bottleneck edge of weight at least
\(R/(k-1)\). Insert the edge of weight \(e\) into that path and
delete a largest edge on the resulting cycle. The mixed-tree bound
then gives
\[
 \Pr(\text{fixed heights})
       \le {C_k h^{o(1)}\over
                         hR Q^{(k-2)/(k-1)}}.        \tag{11}
\]
Combining this with (4) yields exactly the order in (10).
Zero coordinate gaps have weight one and need no separate treatment.
No minimum surviving P gap is used.

## 4. Optimize the low-product cutoff

Apply (3) to \(\min(Q_0,Q_1)\le T\). In its complement, \(Q>T\).
The exponent of \(Z\) in (10) is negative, so summing its dyadic
bins gives
\[
 \mathbb E N_k
 \le h^{1+o(1)}T+
 h^{k/2+3/4+o(1)}T^{-(2k-3)/(2k-2)}.                 \tag{12}
\]
Set
\[
 T=h^{t_k},\qquad
 t_k={ (2k-1)(k-1)\over2(4k-5)}.                     \tag{13}
\]
This lies between \(1\) and the upper product range in (2), in the
sense \(0<t_k<(k-1)/2\). The two powers of \(h\) in (12) agree,
proving (1). For the first three relevant lengths:

| Cycle length | Cutoff exponent \(t_k\) | Expected-count exponent |
| --- | --- | --- |
| 3 | \(5/7\) | \(12/7\) |
| 4 | \(21/22\) | \(43/22\) |
| 5 | \(6/5\) | \(11/5\) |

The same orders bound the number of incident genuine objects for fixed
\(k\). These estimates can be included in a joint averaging objective.
They do not by themselves justify deleting a chosen point while
maintaining occupancy, or assigning the remaining singleton parities.

Independent review: the complete written proof passed a separate check
of the cyclic rotation, bin-dependent radius, minimum-edge exchange,
optimization, repetitions, and absence of a fixed-direction restriction.
For \(k\le5\), the subsequent
[height-first theorem](continuation_height_first_five_cycle_bound.md)
gives stronger bounds.
