# Exact-history queue experiments

11 November 2026. These are finite certificates and bounded heuristic probes,
not a proof of a linear partition at all heights.

The correlated queue model is described in
[the periodic-routing note](continuation_monotone_periodic_routing.md).
With capacity \(C\), it uses at most \(CK+A-1\) classes, all satisfying
\(0<j'-j\le i'-i\).

## Exact checks and the local dynamic program

For a label \(v=(i,j)\), let \(B(v)\) be the set of odd indices \(i'\ne i\)
for which its even row and the odd row at \(i'\) satisfy the P test, with odd
hypotenuse less than \(h\). A token stores its occupied odd indices \(I\)
and the union \(F\) of \(B(v)\) over its entire history.
Serving that token at \(v\) is legal precisely when

\[
i\notin F,\qquad B(v)\cap I=\varnothing.
\]

The two tests cover both directed cross-pair orientations.

If row \(j\) serves token \(s_j\), its next queue consists of its unserved
tokens and the newly served token from row \(j-1\). Consequently, requiring
every next queue to contain a legal token couples only choices \(s_{j-1}\)
and \(s_j\). A dynamic program with at most \(C\) states per row finds an
optimal service vector for any additive row/adjacent-row score, or certifies
that no one-step-viable vector exists for the current histories. Its
combinatorial cost is \(O(KC^2)\), in addition to history bitset operations.
This does not establish indefinite viability.

The probe tried oldest-first, youngest-first, random scores, and a score that
rewards the number of legal tokens left in the next queue. Every saved success
was checked again by enumerating all pairs in every class, independently of
the history-bitset legal-service test. The check also confirms exact grid
coverage and the Lipschitz inequality.

## Selected successful certificates

The table gives the smallest number of classes among the saved runs, not a
minimum over all schedules.

| Height | Queue capacity | Classes | Longest class |
| ---: | ---: | ---: | ---: |
| 32 | 3 | 61 | 6 |
| 48 | 4 | 116 | 12 |
| 64 | 5 | 149 | 26 |
| 96 | 6 | 252 | 38 |
| 128 | 6 | 347 | 51 |
| 192 | 6 | 559 | 77 |
| 256 | 8 | 774 | 102 |
| 384 | 8 | 1244 | 152 |
| 512 | 10 | 1725 | 205 |

Height 64 also has a capacity-four certificate with 156 classes. Heights
256, 384, and 512 all have capacity-eight successful schedules. The table
chooses fewer classes rather than the smallest tested capacity.

The complete compact certificates are in
[continuation_monotone_queue_certificates.json](continuation_monotone_queue_certificates.json).
The small settings/outcomes index, including hashes of the original logs, is
[continuation_monotone_queue_summary.json](continuation_monotone_queue_summary.json).
The reproducible code is
[continuation_monotone_queue_probe.py](continuation_monotone_queue_probe.py).
Larger original logs remain in this workspace; they are not needed to check
the selected certificates.

## Failed searches and limits

The initial greedy/one-step-DP runs did not find capacity-two solutions at
height 32 or above, capacity-three solutions at height 48 or above, or
capacity-four solutions at height 96 or above. A beam search retaining 128
states and sampling twelve successors per state exhausted at column 7 for
\((h,C)=(32,2)\). A beam search retaining 256 states with the same branching
exhausted at column 20 for \((64,3)\). Both columns are zero-based.

These are heuristic failures. The beam retained only a subset of feasible
states and sampled service vectors, so neither failure is an unsatisfiability
certificate. No lower bound on queue capacity follows.

The positive evidence is that coordinated history-aware choices preserve
linear-length monotone chains, unlike independent palette thinning. What
remains unproved is a service rule with an absolute capacity, or a variable
capacity rule that starts only \(O(h)\) token colors in total.
