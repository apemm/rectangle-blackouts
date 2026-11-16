# Full permutation blocks can avoid every fixed direction palette

15 November 2026. A sufficiently large fixed Cartesian block can avoid
all variable-variable P constraints in any prescribed finite palette
of Pythagorean directions, simultaneously across arbitrarily many
blocks. No bound on the degree of the graph of interacting blocks is
needed. The key is that a fixed direction pairs potential point
placements, and the permutation local lemma uses label and slot
resources rather than whole blocks.

The theorem concerns the placed block points. Fixed outside stubs,
new points produced by interpolation, and other support families have
separate requirements, stated below.

## 1. The geometric hypothesis and theorem

Each block has \(k^2\) slots at distinct integer columns and the complete
set of \(k^2\) labels
\[
                   (a_i,b_j),\qquad 1\le i,j\le k,     \tag{1}
\]
where the \(a_i\) are distinct odd rows and the \(b_j\) are distinct
even rows. Row lists may differ between blocks. Every block may use
an arbitrary bijection between its labels and slots.

Assume that **every simultaneous choice of those block permutations**
has no nonhorizontal integral distance between two points of the same
parity. This is a hypothesis about the entire allowed permutation
family, not about one selected realization.

Let \(\mathcal D\) be a prescribed set of \(d\ge1\) nonhorizontal
Pythagorean line directions. A direction has primitive vector
\((p,q)\), with \(p>0\), \(q\ne0\), and \(p^2+q^2\) an integer
square. Opposite signs of \(q\) count as different directions.

**Theorem.** If
\[
                              k\ge32d+1,             \tag{2}
\]
the blocks have simultaneous permutations with no cross-parity pair
on any line of a direction in \(\mathcal D\). In particular all
actual variable-variable P exclusions in this palette are avoided.
Every block is fully occupied and every original label is used once.

The assertion excludes the whole line-incidence overgraph. It need
not test in-strip vertical alternatives or axis owners.

## 2. A direction matches point-placement resources

An odd point resource is a pair \((s,a_i)\), where \(s\) is a slot;
an even point resource is \((s,b_j)\). A resource is not a complete
label placement. Exactly \(k\) labels can realize each such resource.

For a direction \((p,q)\), use its line parameter
\[
                              \lambda(x,y)=py-qx.    \tag{3}
\]
Each odd resource has at most one even resource with the same
parameter, and conversely.

To prove this, suppose two distinct even resources have the same
parameter. If they are at the same slot, their distinct rows already
give different parameters, a contradiction. If they are at distinct
slots in different blocks, choose both placements independently. If
they are in the same block, they can still be realized simultaneously:
when they use the same even row, choose different odd coordinates,
possible since \(k\ge2\); otherwise choose any two distinct labels
with the required even coordinates. Extend these assignments to a
permutation of the block.

The two resulting even points lie on a nonhorizontal Pythagorean line.
Their integer displacement is an integer multiple of the primitive
vector \((p,q)\), so its length is integral. This contradicts the
uniform geometric hypothesis. The odd argument is identical.

Thus, for each direction, the conflict relation is a partial matching
between the odd and even point resources over the entire board.
This statement concerns all candidate resources before permutations
are chosen.

## 3. Atomic assignments and canonical bad events

Write \(n=k^2\). Independently sample a uniform permutation of the
\(n\) labels into the \(n\) slots of every block.
An atomic assignment specifies one label at one slot. It realizes
one odd and one even point resource.

For each matched point-resource pair, forbid every compatible pair
of atomic assignments realizing it. Ignore impossible prescriptions,
such as placing one label at two slots in one permutation. Ignore
same-slot pairs, since a nonhorizontal line with \(p>0\) cannot join
two points in one column. Deduplicate identical canonical events.

One atomic assignment has at most
\[
                               2dk                 \tag{4}
\]
conflicting atomic partners: two point roles, at most one matched
opposite resource per direction, and \(k\) labels realizing that
resource. This is the bound that would be lost by treating a whole
block as one dependency variable.

Each surviving event specifies exactly two compatible assignments.
Its probability is
\[
 p_E=
 \begin{cases}
  1/[n(n-1)],&\text{within one block},\\
  1/n^2,&\text{in two blocks}.
 \end{cases}                                                \tag{5}
\]

A permutation resource means a fixed label or a fixed slot, together
with its block. A resource belongs to \(n\) atomic assignments. By
(4), at most \(2dkn\) canonical bad events use it. Hence
\[
 \sum_{E\text{ using a given resource}}p_E
       \le {2dk\over n-1}
       ={2dk\over k^2-1}
       =:\rho.                                      \tag{6}
\]
This includes both internal and external conflicts.

## 4. The product-permutation local lemma

Join two canonical events when they share a permutation resource.
This is a negative dependency graph. A direct argument also covers
the product of the block permutation spaces.

Fix an event \(E\). Force its assignments one at a time: to force
label \(\ell\) into slot \(s\), swap its present slot with \(s\).
Previously forced assignments remain fixed. Each resulting
permutation has the same number of preimages, so after the swaps
the product law is uniform conditional on \(E\).

An occurring nonneighbor event cannot be destroyed by a swap. It uses
neither the forced label nor forced slot. If it used the other
swapped label, that label would currently occupy the forced slot,
contradicting the nonneighbor event's prescribed slot. Thus forcing
\(E\) can create, but cannot destroy, occurring nonneighbors.
This coupling gives the required lopsided conditional probability
inequality.

This is the canonical-event method of
[Lu and Székely, Theorem 1 and Lemma 3](https://people.math.sc.edu/lu/papers/randinj.pdf).
Their original paper was checked directly. The same product coupling
also appears in the earlier
[regular-square proof](../../2026-11-11/continuation_regular_square_local_lemma.md).

Each event uses four permutation resources. Set \(x_E=2p_E\).
Equation (6) gives
\[
                  \sum_{F\sim E}x_F\le8\rho.
 \tag{7}
\]
Condition (2) implies \(32dk\le k^2-1\), so \(\rho\le1/16\)
and the last sum is at most \(1/2\). Consequently
\[
 x_E\prod_{F\sim E}(1-x_F)
 \ge 2p_E\left(1-\sum_{F\sim E}x_F\right)\ge p_E.
 \tag{8}
\]
The local lemma gives positive probability of avoiding all events.
This proves the theorem.

## 5. A boundary-list version

Suppose fixed outside information additionally forbids some individual
label-slot assignments. For each label and each slot, let at most
\(u\) of its \(n\) assignments be forbidden. These are unary
canonical events, each of probability \(1/n\).

The same proof works whenever
\[
                   {u\over k^2}+{2dk\over k^2-1}
                         \le {1\over16}.            \tag{9}
\]
A fixed outside P point may generate such a forbidden list, but (9)
must be checked; it does not follow from the number of directions
alone. Arbitrary fixed singleton boundaries can forbid an entire
coordinate row of placements, so a boundary hypothesis is necessary.

The theorem does not condition on already chosen permutations or on
avoiding unrelated support families. If other canonical bad events
are included, their resource probability mass must be added to (9).

## 6. How the uniform geometry can be obtained

For a raw Hilbert order with coordinate locality at most
\(4\sqrt{|r-s|}\), suppose the physical row maps have fixed Lipschitz
constant \(D\). Arbitrary permutations inside consecutive blocks of
\(k^2\) ranks move each original rank by at most \(k^2-1\).
For two distinct new slots at rank gap \(q\ge1\), the old gap is at most
\[
 q+2(k^2-1)\le(2k^2-1)q.
 \tag{10}
\]
Their same-parity physical row difference therefore has square at most
\[
                          16D^2(2k^2-1)q.
 \tag{11}
\]
Place columns at stride \(S\), with
\[
                             S\ge8D^2(2k^2-1).
 \tag{12}
\]
For a nonzero vertical difference, (11) is at most twice the horizontal
difference \(Sq\). Its squared length lies strictly between
\((Sq)^2\) and \((Sq+1)^2\), so it is not integral.
This establishes the uniform hypothesis for all block permutations.
Increasing \(S\) to meet fixed residue requirements is harmless.

In an aligned raw square of side \(k\), the labels are exactly the
Cartesian product required in (1). Taking \(k\) to be a power of two
at least \(32d+1\) permits these blocks in a Hilbert decomposition.
Bounded nonuniform physical row gaps are allowed through \(D\).
For fixed \(d\), both \(k\) and \(S\) are constants independent of \(h\);
the width cost is therefore a fixed factor.

## 7. Exact scope in the current construction

This is a simultaneous finite-direction theorem for full permutation
blocks, rather than a repeated private palette or a local Hall
extension with a bounded number of earlier block neighbors.

The original four canonical per-scale P systems include directions
whose Pythagorean factors grow with height. They are not a fixed
finite palette, so the present theorem does not solve them.
It does solve every prescribed fixed finite subset under the stated
placement and geometry hypotheses.

In the finer constant-sea scaffold, interpolated points can depend
on several nearby label placements. They are not automatically the
single atomic point resources used in Section 2. Fixed caps and
singleton stubs also create boundary constraints. A transfer to that
full model requires controlling these new events and their resource
loads; no such transfer is claimed here.

Independent review: the complete written theorem passed a separate
check of resource coexistence, primitive-line integrality, event
probabilities and resource loads, the product coupling, the explicit
threshold, uniform stride geometry, and the unary boundary extension.
That review also checked Theorem 1 and Lemma 3 in the primary source.
