# Fill intervals between good pairs without additional good-label deletion

15 November 2026. For the geometric occupancy problem alone, arbitrary
bad-row sets do not require a run-energy hypothesis. One may retain
every both-good double in its original curve position and fill each
intervening interval with two endpoint singleton rows. The partial
same-parity Hölder constant increases by only \(\sqrt2\).

This replaces no good label. Its limitation is arithmetic: the nearest
both-good endpoints depend on the sampled good sets and do not have
the logarithmic deterministic provenance menu of dyadic caps. No
existing cap incidence theorem is transferred here.

## 1. An abstract interval lemma

Let the original ranks be \(0,\ldots,M-1\). At each rank \(r\)
there are two coordinate values \(f_0(r),f_1(r)\), with
\[
                   |f_\alpha(r)-f_\alpha(s)|
                         \le C\sqrt{|r-s|}.
                   \tag{1}
\]
Let \(G\) be a nonempty set of ranks at which both original values
are good. Retain the original double at every rank in \(G\).

For consecutive \(u<v\) in \(G\), fill an intermediate rank \(r\)
by
\[
 \begin{cases}
 \text{the parity-zero singleton }f_0(u),
       &r-u\le (v-u)/2,\\
 \text{the parity-one singleton }f_1(v),
       &r-u>(v-u)/2.
 \end{cases}
 \tag{2}
\]
Before the first rank in \(G\), use its parity-one value. After
the last rank in \(G\), use its parity-zero value. Every rank is
occupied and every selected row is good.

For either parity, every pair of selected values satisfies
\[
                  |\widetilde f_\alpha(r)
                          -\widetilde f_\alpha(s)|
                         \le \sqrt2 C\sqrt{|r-s|}.
                  \tag{3}
\]
Here each function is defined only at ranks where that parity is
selected. There is no assertion that two good total functions exist.

To prove (3) for parity zero, associate every selected rank in the
first half of a gap with its left endpoint, and every retained rank
with itself. The terminal tail is associated with the last retained
rank. Two points in the same gap have the same associated value.
Otherwise take \(r<s\). If \(r\) is in a gap \((u,v)\), its
first-half condition gives
\[
                         r-u\le v-r\le s-r.
\]
The associated rank of \(s\) is at most \(s\). Therefore the
distance between the two associated ranks is at most \(2(s-r)\).
If \(r\) is retained, or both points are in the terminal tail, the
bound is immediate. Apply (1). The parity-one proof is the
time-reversed argument, including the initial tail.

## 2. Good-row Cartesian labels

Suppose the original curve visits the full \(n_0\)-by-\(n_1\)
Cartesian family of row labels, once each. If \(b_\alpha\) rows
in parity \(\alpha\) are bad, the number of labels with at least
one bad endpoint is exactly
\[
               n_1b_0+n_0b_1-b_0b_1.
               \tag{4}
\]
Remove these doubles from the core label list and use their original
slots for the singleton rule (2). Every label with both rows good
remains at its original rank. Thus, when \(n_\alpha=O(h)\), only
\(O(h(b_0+b_1))\) labels require external placement.

For ordinary Hilbert ranks with a fixed horizontal stride, the width
is unchanged at \(O(h^2)\), and (3) preserves a uniform partial
same-parity square-root locality bound. The same assertion holds
when (1) comes from a sampled bounded-gap row map. It does not
require a bound on the largest bad-row run or on the sum of
squared consecutive good-row gaps.

The external placement and its collisions remain separate. The
lemma is an occupied-core geometry statement, not a valid blackout
construction.

## 3. Longest interval and the provenance issue

In a complete side-\(N\) Hilbert square, suppose at most \(b\) raw
coordinate indices are bad in each axis. Let \(L\) be the least
power of two strictly greater than \(b\), and suppose \(L\le N\).
Every aligned side-\(L\) square contains a good coordinate in each
axis and therefore a both-good cell. Its rank interval has length
\(L^2\). Any rank interval of length \(2L^2\) contains a complete
aligned rank interval of length \(L^2\). Consequently every gap with no
both-good rank has length at most
\[
                       2L^2\le 8(b+1)^2.
                       \tag{5}
\]
The initial and terminal gaps satisfy the same upper bound. If
\(L>N\), the trivial bound \(N^2\) applies.

Equation (5) limits the displacement of a copied endpoint, but it
does not give an \(h^{o(1)}\)-sized deterministic menu for that
endpoint. A fixed rank may have many possible nearest both-good
neighbors as the row fields and offsets vary. Summing all such
possibilities could lose the incidence savings.

The dyadic cap construction avoids this problem by using ancestor
boundary coordinates, of which there are only \(O(\log h)\) per
rank. The interval filling here improves the number of original
labels preserved, while giving up that immediately available
arithmetic provenance. A comparison between these two properties is
needed before using it in a counting or repair argument.

## 4. A row-run energy bound for the copied intervals

Let \(g_i\) list all maximal consecutive bad raw-coordinate runs
in the two axes. Let \(\ell_j\) list the maximal rank intervals
with no both-good cell. Then
\[
                \sum_j \ell_j^{3/2}
                         \le C N\sum_i g_i^2.
                \tag{6}
\]
This concerns bad runs in the actual raw coordinate lists. It does
not identify those runs with bad physical-row runs after an arbitrary
sampled subsequence.

For a dyadic \(L\le N\), every rank interval of length
\(\ell\ge4L^2\) contains at least \(\ell/(2L^2)\) complete
aligned rank blocks of length \(L^2\). Their side-\(L\) squares
contain no both-good cell. Because the good cells form a Cartesian
product, at least one coordinate interval of each such square must
be entirely bad.

The number of aligned entirely bad length-\(L\) coordinate intervals
is at most \(\sum_i\lfloor g_i/L\rfloor\). Each can occur in
only \(N/L\) side-\(L\) squares. The maximal invalid rank
intervals are disjoint, so their complete blocks are distinct.
Consequently
\[
 \sum_{\ell_j\ge4L^2}\ell_j
   \le 2NL\sum_i\lfloor g_i/L\rfloor
   \le 2N\sum_{g_i\ge L}g_i.
   \tag{7}
\]
For every \(\ell\ge4\), the sum of dyadic \(L\) with
\(4L^2\le\ell\) is comparable to \(\sqrt\ell\). Multiply
(7) by \(L\) and sum dyadically. Interchanging sums gives
\[
 \sum_j\ell_j^{3/2}
   \le C N\sum_i g_i
                    \sum_{\substack{L\ {\rm dyadic}\\L\le g_i}}L
   \le C'N\sum_i g_i^2.
\]
Runs of length less than four contribute at most a constant times
the total number of invalid ranks, which is at most
\(N\sum_i g_i\le N\sum_i g_i^2\). This proves (6).

More generally, the same tail calculation gives, for every fixed
\(\gamma>1\),
\[
 \sum_j\ell_j^{(\gamma+1)/2}
                    \le C_\gamma N\sum_i g_i^\gamma.
                    \tag{6a}
\]
Multiply (7) by \(L^{\gamma-1}\) and sum dyadically. On the
left, the coefficient of \(\ell_j\) is comparable to
\(\ell_j^{(\gamma-1)/2}\); on the right, the inner sum over
\(L\le g_i\) is \(O_\gamma(g_i^{\gamma-1})\).
The short rank runs are covered as before.

In particular, a planted good-anchor estimate
\(\sum_i g_i^\gamma\ll h(\log h)^A\), with \(N=O(h)\),
implies an invalid-rank moment of order
\(\beta=(\gamma+1)/2\) bounded by \(O_\gamma(h^2(\log h)^A)\).
The semigroup input with fixed \(1<\gamma<3/2\) supplies
\(1<\beta<5/4\). It does not reach the \(3/2\)-moment in (6).

The same complete-square argument improves (5) to
\[
                 \max_j\ell_j
                       \le C(1+\max_i g_i)^2.
                 \tag{8}
\]
Thus a squared row-run energy of order \(h\) would give a
copied-interval \(3/2\)-moment of order \(h^2\). Neither premise
is established for the actual R2s bad-row set by its current
cardinality estimate.

There is also a deterministic endpoint witness. The first retained
both-good rank immediately after a nonempty invalid interval has a
predecessor differing in exactly one raw Hilbert coordinate. That
predecessor is invalid, while the endpoint is good in both coordinates.
Hence the changed predecessor coordinate is bad. The same statement
holds for the last retained rank before the interval and its successor.
If the original row map has adjacent increments at most \(D\),
at least one physical row of either endpoint lies within \(D\)
of a bad physical row. The enlarged physical witness set has size
at most \((2D+1)b\). This supplies a small target set, but still
does not specify the endpoint's raw rank before sampling.

One cannot ignore the adaptive selection in a point-mass estimate.
Already in one dimension, let the bad physical rows be
\(\{1,\ldots,g\}\), shift a fixed raw query by a uniform offset
from an interval of length \(\Theta(h)\), and return the first
good row above that query. Every query falling in the bad interval
returns the same row \(g+1\). Its atom is therefore
\(\Theta(g/h)\), when those offsets are in the sampling interval.
This is a selector-level example, not an asserted lower bound for
the filled Hilbert scaffold. It explains why the old \(O(1/h)\)
prescribed-row estimate cannot be applied after a nearest-good
selection without a separate multiplicity argument.

## 5. What variable-speed ordering would still add

This lemma does not answer whether a different ordering and a
nonuniform horizontal clock can make the intervening singleton
regions easier to repair. It shows that their mere existence, and
partial square-root locality, are not the obstruction.

In particular, making both endpoint parities simultaneously available
through a long bad run is a stronger task. Assigning each gap rank
both rows of its nearest good endpoint creates a jump at the
midpoint, which can violate (3) over adjacent ranks. Rule (2)
avoids that jump by leaving one parity absent on each half.
Neither a good-row run-energy bound nor a way to remove these
forced interfaces is proved here.

## Review status

Sections 1--4 passed an independent written review, including both
endpoint tails, the exact bad-label count, the partial-function
qualification, the aligned-block bound, the row-run energy estimate
and its general moment extension, and the deterministic endpoint
witness. The adaptive-selector warning was also checked.
