# Valid regular squares from two random permutations

Research note, 11 November 2026. This continuation answers the proposed minimum-row-degree obstruction for arbitrary all-double boards. It does not settle saturated equality boards. The proof and counting refinements received an independent audit.

**Theorem.** For every sufficiently large integer \(n\), there is a valid \(n\times n\) blackout with exactly two black cells in every row and every column.

In particular, valid all-double squares need not have a row of degree at most one. The negative searches at heights eight and nine do not extend to all heights.

## 1. A complete forbidden-support family

Let a rectangle mean a nondegenerate lattice rectangle contained in the actual \(n\times n\) board. Corners may form an axis or tilted rectangle.

Use the following geometric supports.

1. Every four-corner rectangle.
2. Every four-cell symmetric difference of two rectangles with exactly two common corners, where that common pair is a side of one rectangle and a diagonal of the other.
3. Every six-cell symmetric difference of two rectangles with exactly one common corner.

All supports are deduplicated. For the estimates, counting their geometric descriptions instead only gives an upper bound.

Avoiding these supports is sufficient for validity. If two distinct rectangles have the same white presentation, their symmetric difference is black. They cannot have three common corners. If they have no common corner, each is hidden, so the first family applies. If they have one common corner, the third family applies.

If they have two common corners, the mixed side/diagonal case is the second family. In the remaining cases their symmetric difference is itself a rectangle. Two complementary sides to a shared side are parallel and their displacement is perpendicular to them. Two complementary diagonals to a shared diagonal have the same midpoint and length. Thus the first family covers both cases.

This classification allows the common corners to have either color. It does not assume that a common point or pair is actually white.

## 2. Rectangle shapes through a fixed cell

Write two perpendicular nonzero integer side vectors as
\[
 U=k(a,b),\qquad V=\ell(-b,a),
\]
where \((a,b)\) is primitive, \(k\ge1\), and \(\ell\ne0\). Signs and axis directions cost only an absolute factor. Put
\[
 s=\max(|a|,|b|).
\]
Since each side's coordinate differences are at most \(n-1\),
\[
 k,|\ell|\le n/s.
\]
There are \(O(s)\) primitive directions of maximum norm \(s\). Hence
\[
 D_n:=\sup_P\#\{R:P\text{ is a corner of }R\}
 \le C\sum_{s\le n}s(n/s)^2
 \le Cn^2(1+\log n).                              \tag{1}
\]
Here \(P\) is a fixed physical cell. Choosing it as a corner fixes the translation. Axis rectangles are included.

The number of first-family supports through \(P\) satisfies the same bound.

## 3. Mixed four-cell supports

First choose the rectangle in which the common pair is a side. Its opposite black side has displacement \(U\), and the connector to the common side is perpendicular to \(U\). The preceding shape count is \(O(n^2\log n)\).

The other rectangle uses the common side as a diagonal. Its complementary black diagonal has an integer displacement \(W\) with
\[
 |W|^2=|U|^2\le2n^2.
\]
The number of possible \(W\) is
\[
 r_2(|U|^2)\le4\tau(|U|^2)=O_\eta(n^\eta)          \tag{2}
\]
for every fixed \(\eta>0\), after rescaling the exponent in the usual divisor bound.

For completeness, the first inequality follows by factorization in the Gaussian integers: a split prime of exponent \(e\) gives at most \(e+1\) allocations between the two conjugate factors, while inert and ramified primes contribute no larger factor. The units contribute four. The bound \(\tau(N)=O_\varepsilon(N^\varepsilon)\) follows by separating finitely many small primes from the primes for which \(e+1\le p^{\varepsilon e}\).

Once the relative shape and the role of \(P\) among the four black points are specified, the translation is fixed. Integrality or containment failures are discarded. Therefore, absorbing the logarithm into \(\eta\), the number of mixed four-supports through any fixed cell is
\[
 O_\eta(n^{2+\eta}).                              \tag{3}
\]
This estimate also covers vertical and horizontal common sides. Using an integral connector between two actual side endpoints avoids a half-integral-midpoint issue.

Combining the first two families, every fixed physical row or column meets
\[
 O_\eta(n^{3+\eta})                               \tag{4}
\]
four-supports. Sum the fixed-cell bound over the \(n\) cells on that row or column.

## 4. Six-cell supports

For a fixed black support point \(P\), choose the first rectangle through \(P\), choose its common corner \(W\), and choose the second rectangle through \(W\). Either rectangle may contain \(P\), which costs only a factor of two. Equation (1) gives
\[
 O(D_n^2)=O(n^4(1+\log n)^2)                       \tag{5}
\]
descriptions through \(P\).

The intersection-one restriction only reduces this count. Thus every fixed physical row or column meets
\[
 O(n^5(1+\log n)^2)                               \tag{6}
\]
six-supports.

All these bounds concern rectangles in the actual square. No unbounded-strip or finite-end convention is used.

## 5. The probability space and canonical events

Choose independent uniform permutations \(\pi_1,\pi_2\) of \([n]\), and set
\[
 S=\{(x,\pi_1(x)):x\in[n]\}
 \cup\{(x,\pi_2(x)):x\in[n]\}.                     \tag{7}
\]

For every \(x,y\), forbid the coincidence event
\[
 \pi_1(x)=y=\pi_2(x).                              \tag{8}
\]
After avoiding these events, every row and column has exactly two black cells.

For each geometric support \(F\) of size \(k=4\) or \(6\), assign each of its cells a color in \(\{1,2\}\). The associated canonical event requires
\[
 \pi_c(x)=y
\]
for every cell \((x,y)\) assigned color \(c\). Discard assignments that prescribe two different images for one domain, or the same image for two domains, within either permutation.

If \(k_c\) assignments remain in color \(c\), the event probability is exactly
\[
 p_E=\frac1{(n)_{k_1}(n)_{k_2}}
 \le Cn^{-k},\qquad k_1+k_2=k\le6.                \tag{9}
\]
A coincidence event has \(k=2\) and probability \(n^{-2}\).

If a geometric support is black, some compatible color assignment realizes it. Therefore avoiding all canonical events excludes every support in Section 1.

## 6. The negative dependency graph, including the product space

A resource is either a domain \(x\) or an image \(y\), together with its permutation color. Join two canonical events if they use a common resource. Each event uses at most twelve resources.

This is a negative dependency graph. Here is a direct swap proof, so the use of two independent permutations does not rely on an unproved independence assertion.

Fix a canonical event \(E\). Start with the independent uniform permutations. Force its prescribed assignments one at a time. To force \(\pi_c(a)=b\), exchange the images at \(a\) and \(\pi_c^{-1}(b)\). Earlier assignments remain fixed because the partial assignment defining \(E\) is injective. The result is uniform conditional on the newly forced assignments: every permutation satisfying them has the same number of preimages under the swap map. Performing this separately in both colors gives precisely the law conditional on \(E\).

Let \(F\) be a nonneighbor of \(E\). If \(F\) occurs before a swap, it still occurs afterward. The forced domain \(a\) is absent from \(F\). The other swapped domain cannot be prescribed by an occurring \(F\), since its current image is \(b\), and \(F\)'s images avoid the images prescribed by \(E\).

Thus the coupling can create nonneighbor events but cannot destroy an occurring one. For any family \(\mathcal J\) of nonneighbors,
\[
 \Pr\!\left(\bigcap_{F\in\mathcal J}\overline F\mid E\right)
 \le
 \Pr\!\left(\bigcap_{F\in\mathcal J}\overline F\right).
\]
Bayes' rule gives the required conditional upper bound for \(E\).

This is the canonical-event method of
[Lu and Székely, *Using Lovász Local Lemma in the Space of Random Injections*, Theorem 1](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v14i1r63).
Their Lemma 3 states the asymmetric local lemma for a negative dependency graph, including the positive product lower bound. The [author-hosted original PDF](https://people.math.sc.edu/lu/papers/randinj.pdf) was checked directly.

## 7. The local-lemma calculation

For one fixed resource, coincidence events have total probability \(O(n^{-1})\). Equations (4), (6), and (9), with at most \(2^k\) color assignments per support, give
\[
 \sum_{E\text{ using the resource}}p_E
 \le C_\eta\left(
 n^{-1}+n^{-1+\eta}+\frac{(1+\log n)^2}{n}
 \right)=:\rho_n.                                 \tag{10}
\]
Fix \(0<\eta<1\). Then \(\rho_n\to0\).

Take \(x_E=2p_E\). Since an event uses at most twelve resources,
\[
 \sum_{F\sim E}x_F\le24\rho_n\le\tfrac12
\]
for all sufficiently large \(n\). Therefore
\[
 x_E\prod_{F\sim E}(1-x_F)
 \ge2p_E\left(1-\sum_{F\sim E}x_F\right)
 \ge p_E.
\]
The negative-dependency local lemma gives positive probability of avoiding every event. Equations (7) and (8) then give exactly two black points in every row and column, while Section 1 gives validity. This proves the theorem.

## 8. Scope and a fixed-degree extension

The theorem disproves the broad assertion that every valid all-double board has a row of degree at most one. It gives no explicit small threshold for \(n\), and does not reinterpret the completed height-eight and height-nine exclusions.

It does not prove or disprove a leaf-type statement under the stronger condition that every tilted rectangle has at most two black corners. The constructed valid boards can have tilted singleton presentations that have no competing axis owner.

It also does not settle the saturated equality problem. The theorem has \(n\) doubles with a two-regular row-pair graph. Saturation at height \(n\) requires \(q_n\) doubles and the complete balanced row family.

The same proof works for any fixed number \(d\) of independent permutations. Forbid pairwise coincidences and use \(d^k\) color assignments for each support. The constants in (10) then depend on \(d\), while \(\rho_n\to0\) still holds. Thus for every fixed \(d\), all sufficiently large squares admit a valid blackout with exactly \(d\) black cells in every row and column.

## 9. Every balanced row partition at even height

There is a uniform stronger version for even \(n\). Fix any partition \(A\sqcup B=[n]\) with \(|A|=|B|=n/2\).

Split the columns into two sets \(L,R\) of size \(n/2\). Independently choose one uniform bijection from each of \(L,R\) to each of \(A,B\). This gives four independent permutation coordinates.

Every column has exactly one black row in \(A\) and one in \(B\). Every row occurs once in \(L\) and once in \(R\), so every row has degree two. Coincidences are impossible.

Each physical cell belongs to one fixed permutation coordinate. A geometric support therefore has either an impossible assignment or a canonical event of probability \(O(n^{-k})\), because each permutation has size \(n/2\) and \(k\le6\). The same resource counts and swap proof apply, with absolute constant changes. The local-lemma criterion is uniform in the chosen partition.

**Corollary.** For every sufficiently large even \(n\), and every prescribed balanced partition of its rows, a valid \(n\times n\) board exists with exactly two black points per row and column and one point from each row part in every column.

In particular this holds for the physical odd/even partition. It rules out a general obstruction based only on parity labels, use of every row, and minimum row degree two. Complete coverage of all \(q_n\) labels is still absent.

The restriction to even \(n\) is necessary for this two-regular bipartite form. In any two-regular bipartite row graph the two parts have equal size.

## 10. Counting valid two-regular squares

Let \(B_n\) count valid \(n\times n\) boards with exactly two black cells in every row and every column. For every fixed \(\eta>0\),
\[
 (n!)^2\exp(-O_\eta(n^\eta))
 \ \le B_n\le(n!)^2.                              \tag{11}
\]
In particular,
\[
 \log B_n=2n\log n-2n+o(n).                       \tag{12}
\]

The product conclusion of the local lemma proves that the probability of a good ordered permutation pair is at least \(\exp(-C_\eta n^\eta)\). Indeed, the total probabilities of the coincidence, four-support, and six-support events are respectively \(O(1)\), \(O_\eta(n^\eta)\), and \(O((1+\log n)^2)\), after choosing a smaller geometric exponent and absorbing logarithms. Also \(x_E=2p_E=o(1)\), so
\[
 \prod_E(1-x_E)\ge \exp(-C_\eta n^\eta).
\]

The ordered-pair count is not the board count. For
\[
 \tau=\pi_1^{-1}\circ\pi_2,
\]
each cycle of \(\tau\) is one alternating component of the uncolored two-regular board. If it has \(c\) components, it has exactly \(2^c\) ordered decompositions into two permutations.

For a uniform permutation,
\[
 \mathbb E[2^{c(\tau)}]=n+1.                       \tag{13}
\]
This follows from the insertion recurrence
\(\mathbb E[t^{c(\tau)}]=t(t+1)\cdots(t+n-1)/n!\).
Choose \(K=M_\eta n^\eta\), with \(M_\eta\log2>C_\eta+1\). Markov's inequality gives
\[
 \Pr(c(\tau)>K)\le(n+1)2^{-K}
 =o\bigl(\exp(-C_\eta n^\eta)\bigr).
\]
Thus at least half the good ordered pairs have at most \(K\) components. Each corresponding board is counted at most \(2^K\) times, proving the lower bound in (11). The upper bound follows because every two-regular bipartite incidence graph decomposes into two permutations. Stirling's formula gives (12).

This counts regular squares with \(2n\) black cells. It is not a statement about the number \(a_n(n)\) of maximum blackouts, and it does not count saturated equality boards.

## 11. The clone model: prescribed row degree in all-double rectangles

Fix an integer \(d\ge2\). Let \(h\) be even, put
\[
 m=dh/2,
\]
and fix any balanced partition \(A\sqcup B=[h]\). Then, for all sufficiently large \(h\), there is a valid \(h\times m\) board with two black points in every column, one from each part, and exactly \(d\) black points in every row.

Give each physical row \(d\) labeled clones. Each row part has exactly \(m\) clones. Independently choose a uniform bijection from the \(m\) columns to the clones of \(A\), and another to the clones of \(B\). Erase the clone labels to obtain the black cells.

Every column receives one row from each part. Every physical row occurs in exactly \(d\) different columns. No coincidence event is needed.

For each geometric support, choose one of the \(d\) clones for each of its cells. Its row part specifies which permutation coordinate is used. Discard inconsistent partial bijections. A surviving \(k\)-cell event has probability \(O_d(h^{-k})\), because both permutations have size \(m=\Theta_d(h)\) and \(k\le6\).

The support estimates remain valid with constants depending on \(d\). One may bound every side coordinate by \(m+h=O_d(h)\), anchor the specified physical cell, and repeat Sections 2–4. A physical row or column meets
\[
 O_{d,\eta}(h^{3+\eta})\quad\text{four-supports},\qquad
 O_d(h^5(1+\log h)^2)\quad\text{six-supports}.
\]
There are at most \(d^k\) clone assignments per support. Thus the probability mass through any domain or clone-image resource is \(O_{d,\eta}(h^{-1+\eta})+O_d(h^{-1}\log^2h)\), which tends to zero. The same swap coupling and local lemma prove the claim. The estimate is uniform in the balanced row partition.

This shows that no fixed bound on minimum row degree can rule out valid all-double boards. It does not cover the saturated regime, where \(d\) grows on the order of \(h\).

There is an exact multiplicity count in this model. Let \(B_{h,d,\pi}\) denote the number of valid boards with these fixed row and column degrees and prescribed row partition \(\pi\). Each physical board has exactly \((d!)^h\) clone realizations, since its \(d\) occurrences in each row can be assigned that row's \(d\) clone labels arbitrarily. The local-lemma product bound consequently gives, for every fixed \(\eta>0\),
\[
 \frac{(m!)^2}{(d!)^h}\exp(-O_{d,\eta}(h^\eta))
 \ \le B_{h,d,\pi}\le
 \frac{(m!)^2}{(d!)^h}.                           \tag{14}
\]
The upper expression counts all boards with those degree and row-part restrictions, before requiring geometric validity.

For \(d=2\), this yields a sharper count for the fixed-partition square subclass:
\[
 \log B_{n,2,\pi}
 =2n\log n-(2+\log2)n+o(n)                        \tag{15}
\]
at even heights. The unrestricted count in (12) and the prescribed-partition count in (15) refer to different families.




