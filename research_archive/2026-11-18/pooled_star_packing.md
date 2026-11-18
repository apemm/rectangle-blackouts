# Pooling the star P systems in quadratic width

**Theorem.** For every height \(h\), place the \(\lfloor h^2/4\rfloor\) opposite-parity labels in distinct columns of \(8\mathbb Z\), in width \(O(h^2)\), with no in-strip vertical rival between labels. The construction below keeps all labels of the same odd row and dyadic tier in their own interval. Labels in different intervals can approach within the range of a P collision. The argument controls those collisions too.

The earlier archive already gives a quadratic P-only placement by a linear palette. This proof uses the slots in their physical order and gives a different grouping into star intervals. Neither the mixed-support nor the singleton conditions follow from the P conclusion. We include the proof because its grouping and the freedom to match labels to slots could also be used for additional constraints.

## Choosing the tier

Measure slots in units of eight columns. For an even row \(e\) and odd anchor \(o\), let
\[
 D(e,o)=\{d\ge1:(8d)^2+(e-o)^2=L^2,\ 1\le L<h\}.
\]
The divisor and primitive-triple estimates in [the matching lemma](weighted_star_slot_matching.md) apply with the even row fixed as well. Uniformly in \(e\), the sum of \(|D(e,o)|\) over all odd rows is at most \(Ch\log h\). The maximum list size and, for fixed \(o,d\), the number of \(e\) with \(d\in D(e,o)\), are \(h^{o(1)}\).

Let \(b=\lceil h/2\rceil\) and randomly permute the \(b\) odd rows on a circle. At each position, read first its own anchor, then the anchor one position left, one right, two left, two right, and so on, skipping an anchor already visited. For fixed \(e\) and fixed starting position this is a uniform random permutation of the odd rows. Write \(V_i=|D(e,o_i)|/\log h\). The average of all the \(V_i\) is at most an absolute \(C_0\). Let \(T\) be the first \(n\ge1\) for which
\[
 \sum_{i=1}^n V_i\le A n,\qquad A=8(C_0+1).
\]
Such an \(n\) exists by the full-population bound. The choice may depend on the label.

Put \(b_0=\lfloor b/2\rfloor\). While reading the first \(b_0\) anchors, the conditional expectation of every next \(V_i\) is at most \(2C_0\), since at least half the population remains. For \(\tau=\min(T,b_0)\) the stopped sum \(\sum_{i\le\tau}(V_i-A)\) is at least \(-A\). Before the first nonpositive partial sum this is immediate, and the final increment is at least \(-A\). On taking expectations and conditioning term by term we get
\[
 -A\ \le\ \mathbb E\!\sum_{i\le\tau}(V_i-A)
       \ \le\ -(A-2C_0)\mathbb E\tau.
\]
Consequently \(\mathbb E T\le \mathbb E\tau+b\Pr(T>b_0)=O(1)\).

One can also arrange that every \(T\) is \(h^{o(1)}\). Put \(J=\max(1,\max_{e,o}|D(e,o)|/\log h)\), and \(R=\lceil J(\log h)^2\rceil\). For sufficiently large \(h\), \(R\le b_0\). Conditional on the preceding anchors,
\(\mathbb E e^{V_i/J}\le 1+(e_{\rm nat}-1)2C_0/J\), with \(e_{\rm nat}=\exp(1)\). Iteration and Markov's inequality give
\[
 \Pr(T>R)\le\Pr\!\left(\sum_{i\le R}V_i>AR\right)
 \le \exp\!\left(-(A-2(e_{\rm nat}-1)C_0)R/J\right).
\]
A union bound over \(O(h^2)\) labels and Markov's inequality for their sum yield one permutation satisfying
\[
 \max_{e,o}T(e,o)\le R=h^{o(1)},\qquad \sum_{e,o}T(e,o)=O(h^2).
\]
The permutation is shared by all even rows. Linearity of expectation suffices.

Assign the label to the largest dyadic \(k\) with \(2k-1\le T\). Then \(T<4k-1\) and \(k\le T\). For each tier \(k\), partition the (linearized) permutation into consecutive clusters of \(k\) anchors, with a possibly shorter final cluster. Every other anchor of that label's cluster is among its first \(2k-1\) sampled anchors. Thus the augmented list
\[
 D_{e,o}^{\rm aug}=\bigcup_{s\ {\rm in\ its\ cluster}}D(e,s)
 \quad\text{satisfies}\quad |D_{e,o}^{\rm aug}|\le4A k\log h.
\]
A fixed slot distance occurs in at most \(k^2 h^{o(1)}\) augmented lists of one cluster. Indeed at most \(k h^{o(1)}\) distinct even rows qualify, and each can occur with at most \(k\) anchors. In particular these list sizes and incidences are \(h^{o(1)}\) uniformly.

## Allocating the star intervals

Separate consecutive nonempty clusters, including a change of tier, by \(h\) blank slots. A mixed-parity P diagonal with length \(<h\) cannot cross this gap. Counting all potential clusters gives guard cost
\[
 O\!\left(h\sum_{k\ {\rm dyadic},\,k\le R}\lceil b/k\rceil\right)
 =O(h^2).
\]
A blank slot here means a column unused by a double. Constructing valid singleton entries in all such columns is a further problem.

Within a cluster place disjoint consecutive intervals, one per nonempty odd star. Write \(n\) for its number of labels and \(n'=\max(n,\lceil h^{1/3}\rceil)\). Sample a single Bernoulli set of slots for the entire cluster, with \(p=1/(C_1 k)\), using an absolute \(C_1\) large compared with \(A\). Give the star \(\lceil8n'/p\rceil\) candidate slots. As in the matching lemma a candidate is available if it is sampled and no sampled slot is at a distance in its label's augmented list, with fictitious independent sites permitted outside the cluster. The edges again have weights \((1-p)^{-2|D_{e,o}^{\rm aug}|}\le h^{1/32}\), on increasing \(C_1\) if necessary.

For each label the expected weighted degree is at least \(8n'\). For a sampled slot the expected total weight is \(n\), since only labels of its own star are allowed to match it. The two dependency-graph bounds in the matching lemma are \(h^{o(1)}\) here. The probability that a given row sum is below \(4n'\), or a given slot sum exceeds \(2n'\), is \(\exp(-h^{1/3-1/32-o(1)})\) or smaller. For the slot bound with \(n<n'\), use the same exponential-moment upper bound with \(n'\) in place of \(n\). All constraints for the cluster therefore hold simultaneously for some sampled set. Weighted Hall gives a matching in every star interval.

The sum of interval lengths is bounded by a constant times
\[
 \sum_{e,o} k(e,o) +
  h^{1/3}\sum_{k\ {\rm dyadic},\,k\le R} bk
 = O(h^2)+h^{4/3+o(1)}.
\]
If two labels belong to one cluster, the even point of either label was protected against the odd row of the other one by its augmented list and the shared sampled set. Pairs in different clusters are protected by the guards. Restoring the factor of eight proves the theorem.

One can also guarantee a minimum gap of \(k\) slots between chosen points at tier \(k\). For a candidate to be available, additionally require all sites at nonzero distance at most \(k\) from it to be unsampled. In the slot concentration argument condition first on the candidate being sampled and these common sites being unsampled. The residual lists use distances exceeding \(k\), and have the previous incidence bound. Use weights computed from these residual lists. The row means acquire a factor \((1-p)^{2k}\), bounded below by an absolute constant, so enlarging the interval constant restores Hall's inequalities. This version still permits arbitrary matching within each star interval.

The random star order is used only for the mean and maximum stopping-time estimates. A natural-order version of those estimates, or a different angle-preserving star schedule, could connect this packing to tilted-corner control. The theorem itself establishes only the stated P placement.

