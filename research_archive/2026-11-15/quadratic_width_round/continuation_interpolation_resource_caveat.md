# Interpolated alternatives need not form a direction matching

15 November 2026. The resource-matching step of
[the finite-direction permutation theorem](continuation_finite_direction_permutation_lll.md)
cannot simply be applied to every fine interpolated point. Distinct
fine points on one line can be mutually exclusive alternatives of a
single coarse slot. The following exact calculation makes the loss
quantitative.

## 1. One source and many mutually exclusive target resources

Fix a large positive integer \(c\) divisible by four, and put
\[
 h=16c,\qquad a=9c+3,\qquad b_j=12c+6+4j,
                  \quad 0\le j<k,                   \tag{1}
\]
where \(k\) is fixed and \(c\) is sufficiently large relative to \(k\).
The odd source is \(A=(0,a)\). A target coarse slot has the \(k\)
possible even rows \(b_j\). Suppose that, when row \(b_j\) is chosen,
the interpolation keeps it constant at the fine columns
\[
 4t,\qquad c+1\le t\le c+1+\lceil4(k-1)/3\rceil.      \tag{2}
\]
This is only an \(O(k)\)-long plateau in fine ranks.

For every \(j\equiv0\pmod3\), set
\[
                         t_j=c+1+4j/3.
\]
Then
\[
 b_j-a=3t_j,\qquad
 (4t_j)^2+(b_j-a)^2=(5t_j)^2.                         \tag{3}
\]
Thus the even alternative \((4t_j,b_j)\) lies on the same
Pythagorean line of slope \(3/4\) through \(A\).
There are \(\Theta(k)\) such alternatives.

They cannot coexist: each comes from a different row choice at the
same coarse slot. Consequently their common line does not contradict
the uniform same-parity distance exclusion for actual permutations.
This is exactly where the coexistence proof of the matching property
ceases to apply.

The rows in (1) have the standard constant-sea residues
\(a\equiv3\pmod4\), \(b_j\equiv2\pmod4\), and \(a>h/2\).
The vertical alternative rows are
\[
                         a-t_j,\qquad a+4t_j,
 \tag{4}
\]
both strictly inside \([1,h]\) for large \(c\).
Also \(t_j\) is odd, so the midpoint column is \(2t_j\equiv2\pmod4\).
In a constant row-one sea the two midpoint corners are white.
The horizontal gaps and smaller half-factors are \(\Theta(h)\).
An actual presentation collision additionally requires the corresponding
axis owner; no owner placement or complete Hilbert embedding is asserted
by this local resource calculation.

## 2. Consequence for an atomic partner count

In a \(k\times k\) Cartesian label block, each possible even row is
realized by \(k\) labels. For one fixed atomic assignment providing
the odd source \(A\), the alternatives above therefore create
\(\Theta(k^2)\) target atomic assignments with a fine P candidate.
The coarse theorem had only \(O(k)\) partners per fixed direction.

The plateau hypothesis is compatible with a fixed-mesh interpolation
that leaves an \(O(k)\) interval around an anchor unchanged before its
first unit step. It is not claimed that every interpolation rule or
every sampled core contains this precise arrangement.

Therefore a transfer through interpolation needs a new aggregate
conflict estimate or a different event representation. Merely counting
the fine points attached to an assignment as a bounded set is
insufficient: the bound may grow with \(k\), and the required coarse
stride and interpolation length already grow with \(k\). A condition
of the form \(k\gg dS\) would be circular when \(S\) is of order
\(k^2\).

This is a limitation of the naive local-lemma transfer. It is not a
counterexample to simultaneous fine-core permutations or to a
quadratic-width construction.

Independent review: the full written calculation passed a separate
check of the norm identity, residues, midpoint and strip inequalities,
half-factor size, atomic partner multiplicity, and the conditional
plateau and owner scope.
