# Exact finite certificates for odd-relation deletion

12 November 2026. Exact integer computations produced and independently
checked retained distance sets through height \(16\,384\). The deletion
rule is greedy. Its totals are certified upper bounds for the minimum
deletion cost, not exact minima.

For every diagonal, the retained set satisfies the finite-cap condition
in [the parity-sensitive Riesz lemma](continuation_arc_parity_riesz.md).
The [analytical obstruction](continuation_arc_odd_deletion_obstruction.md)
separately proves that the minimum total deletion cost is superlinear.
The finite table is not used to prove that asymptotic statement.

## Results

Here the gap total sums the positive, deduplicated, finite-diagonal sets.
The class bound assigns four arc classes and at most one additional
greedy factor per deleted gap: \(4(\gamma_T+1)\) on each nonempty
original distance set, and one class on an empty original set.

| Height \(h\) | Total gaps | Greedy deletions | Deletions divided by \(h\) | Product class bound |
|---:|---:|---:|---:|---:|
| 128 | 151 | 36 | 0.281250 | 475 |
| 256 | 339 | 99 | 0.386719 | 1,053 |
| 512 | 788 | 254 | 0.496094 | 2,376 |
| 1,024 | 1,763 | 589 | 0.575195 | 5,143 |
| 2,048 | 3,956 | 1,417 | 0.691895 | 11,366 |
| 4,096 | 8,707 | 3,264 | 0.796875 | 24,522 |
| 8,192 | 19,055 | 7,376 | 0.900391 | 52,827 |
| 16,384 | 41,271 | 16,532 | 1.009033 | 113,345 |

The last class bound is approximately \(6.91803h\). It is an existence
bound supplied by the Riesz lemma and greedy coloring; the certificates
do not contain explicit real arc angles or a complete coloring.

The summaries, including certificate filenames and SHA-256 hashes, are
[the first five heights](odd_relation_deletion_summary.json) and
[the three larger heights](odd_relation_deletion_large_summary.json).
Each individual certificate records every diagonal's original gaps,
retained gaps, deleted gaps, final cap, and relation witnesses encountered.

## Exact relation search

The [generator](continuation_odd_relation_deletions.py) enumerates all
gap sets through primitive integer right triangles, retaining both
orientations and enforcing both \(L<h\) and \(|d|<n_T\).
No floating-point square or endpoint tests are used.

For a current set of \(k\) distances, the positive cap \(m(k)\) is
computed by the integer inequality
\[
 4k^2m<4^m.
\]
To detect a relation \(\sum c_i d_i=0\) with \(|c_i|\le m\) and odd
\(\sum c_i\), write \(z_i=c_i+m\). The exact bounded subset-sum target is
\[
 \sum z_i d_i=m\sum d_i,\qquad
 0\le z_i\le2m,\qquad
 \sum z_i\equiv1-mk\pmod2.
\]
Two Python integer bitsets track the two parities. Binary splitting
encodes bounded multiplicities, and sums above the target are discarded
because all \(z_i d_i\) are nonnegative. Per-distance states permit
backtracking an explicit odd relation.

When a relation exists, the procedure deletes \(|T|/5\) if that distance
is present; otherwise it deletes the smallest distance occurring in the
witness. It then recomputes the cap from the new cardinality. The
procedure stops only after an exact negative relation test.

## Independent checks

The [second verifier](continuation_verify_odd_deletions.py) uses a
different recurrence: it directly propagates every signed coefficient
\(-m,\ldots,m\), retaining separate parity bitsets on a fixed signed-sum
interval. It checks every final retained set, replays every stored
relation witness, regenerates every gap set, and verifies diagonal
coverage and the reported totals.

Two additional comparisons passed:

* Both parity dynamic programs agree with brute-force coefficient
  enumeration on 486 cases with at most four distances from
  \(\{1,\ldots,8\}\) and caps one, two, and three.
* The triangle-based gap enumeration agrees with a direct integer
  square test at every height from four through eighty.

The [independent result file](odd_relation_deletion_independent_check.json)
records PASS for all eight certificate files, including all \(16\,383\)
diagonals at height \(16\,384\). These checks validate the finite
upper bounds and retained sets; they do not certify greedy optimality.
