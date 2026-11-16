# The aligned zero-gain graph: an odd cycle and a large cyclic block

These observations concern the original private-slot candidate systems
with stride 32 and three choices. They do not fill the unused columns
or verify a blackout board.

For labels of ranks \(r<s\), a zero-gain constraint is an exact square
norm with horizontal leg \(96(s-r)\). It forbids equal private choices.
Thus its ordinary graph must be properly three-colored by any solution.

## 1. An aligned triangle

The zero-gain graph need not be bipartite. Take a Hilbert square of side
32, offset \(T=-832=-26\cdot32\), and outer coordinate-swap orientation.
The three labels are

| Rank | Cell \((i,j)\) |
|---:|---:|
| 662 | \((31,25)\) |
| 777 | \((13,28)\) |
| 951 | \((2,21)\) |

Each of their three pairs has a zero-gain Pythagorean constraint:

| Ranks | Odd endpoint | Even endpoint | \(X\) | Signed \(Y\) | \(L\) |
|---|---:|---:|---:|---:|---:|
| 662,777 | 777 | 662 | 11040 | -1639 | 11161 |
| 777,951 | 777 | 951 | 16704 | -1647 | 16785 |
| 662,951 | 662 | 951 | 27744 | -1683 | 27795 |

In every row,

\[
 X=96|s-r|,\qquad
 Y=2T+1+2(j_e-i_o),\qquad X^2+Y^2=L^2.
\]

The exact coordinate and norm certificate is
`aligned_zero_gain_triangle.json`. It shows that some aligned
three-choice systems require all three colors already on their
zero-gain subgraph. It says nothing about the differently spaced
two-choice system, whose zero-gain horizontal leg would be \(64(s-r)\).

A companion canonical-orientation example at side 32 and
\(T=-256=-8\cdot32\) has the seven-cycle

\[
719, 728, 737, 342, 587, 640, 666, 719.
\]

Its exact roles and norms are saved in
`aligned_zero_gain_odd_cycle.json`. The replay checker
`check_aligned_zero_gain_witnesses.py` uses an independent recursive
coordinate-to-rank formula and direct integer norm identities. The
displayed witnesses were verified during generation; the saved replay
checker has not been separately rerun or independently reviewed at this
stopping point.

## 2. The saved side-1024 system

The complete saved array
`aligned_private_side1024_minus2048_events.npy` has 1,019,611 zero-gain
edges on 1,048,576 labels. A union-find decomposition gives:

- 188,075 connected components, including 155,812 isolated labels;
- one component with 808,525 vertices and 967,633 edges, of cycle rank
  159,109;
- every other component has at most 27 vertices;
- only one other component is cyclic: it has 17 vertices and 17 edges.

There are 1,149,719 nonzero-gain events. Of these, 691,579 join labels
inside the same zero-gain component, and 458,140 join different
zero-gain components. Consequently, choosing a single color
permutation for each zero-gain component leaves a large internal
constraint problem in the largest component.

The largest component is not a tree of small cycles. An iterative
edge-stack decomposition gives one biconnected block with

\[
465390\text{ vertices},\qquad624469\text{ edges},\qquad
159080\text{ independent cycles}.
\]

All other cyclic blocks are small cycles. Across the graph there are
395,044 bridges and 31 cyclic blocks. The union-find component sizes and
edge counts agree with the independently implemented edge-stack
traversal's component accounting.

The data are saved in
`aligned_zero1024_component_summary.json`,
`aligned_zero1024_components.npy`, and
`probe_zero_gain_blocks.py/.json`. These are exact computations on the
saved graph, not an asymptotic theorem. The graph's zero-gain 3-core is
empty, as checked in the parent computation. The small aligned scan
also found empty zero-gain 3-cores for every \(T=ms\),
\(-16\le m\le16\), both outer classes, and \(s=16,32,64\).
Neither observation proves uniform two-degeneracy.

No side-2048 run was started before the requested stopping point.

## 3. Why two-degeneracy alone cannot settle integer choices

There is a small abstract obstruction, separate from the Pythagorean
geometry. Let \(a,b,c,z\) take values in \(\{0,1,2\}\). On the three
pairs among \(a,b,c\), forbid difference zero. On each pair joining
\(z\) to one of \(a,b,c\), forbid both differences \(-1,+1\).

This system has no solution. The first triangle must use all three
values. If \(z=1\), it conflicts with a vertex colored zero or two.
If \(z=0\) or two, it conflicts with the vertex colored one.

Its zero-difference graph is just a triangle and an isolated vertex,
so it is two-degenerate. Each pair has at most two forbidden integer
differences, and every three-variable induced subsystem is solvable.
Thus an argument based solely on an empty zero-gain 3-core and a
two-difference bound per pair is insufficient.

This is **not** an actual Hilbert or Pythagorean obstruction. Realizing
it would require three zero-gain norms and two appropriate nonzero
norms on each of the other three pairs. Whether the arithmetic excludes
that configuration is open here.

## 4. What remains

The aligned zero-gain graph is neither always bipartite nor, in the
large saved example, assembled from small cyclic blocks. Uniform
two-degeneracy remains unproved. Even a proof of that property would
need an additional argument for the nonzero integer-difference
constraints. The exact integer certificates show substantial freedom
beyond modular gain colorings, but no general extension theorem has
been established.
