# What remains after multiple-leg pairs are removed

15 November 2026. The sparse deletion theorem leaves at most two
forbidden integer differences per pair. That condition alone does not
give a three-choice theorem, even with a bipartite graph of ordinary
degeneracy two. The examples below identify the missing structural
input. They are abstract constraint systems, not claimed P configurations.

All variables take values in \(\{0,1,2\}\).

## 1. The smallest abstract obstruction has four labels

Take four labels and forbid difference zero on every pair. This is the
proper-colouring problem for \(K_4\) with three colours, so it is
unsatisfiable. It has only one forbidden difference per pair.

By [the three-label lemma](continuation_three_label_integer_lemma.md),
every system on at most three labels with at most two forbidden
differences per pair is satisfiable. Thus four is the smallest possible
number of labels for an obstruction in this abstract class.

This does not assert that a corresponding \(K_4\) of zero-offset
P constraints occurs in the Hilbert geometry. Excluding or constructing
such a realization is an additional arithmetic-geometric problem.

## 2. Ordinary two-degeneracy and bipartiteness do not suffice

Take two anchor variables \(a,b\) and three leaves \(c_1,c_2,c_3\).
Forbid the following differences:

| Leaf | Forbidden values of \(c_i-a\) | Forbidden values of \(c_i-b\) |
|---|---|---|
| \(c_1\) | \(\{0,2\}\) | \(\{0,1\}\) |
| \(c_2\) | \(\{0,1\}\) | \(\{-1,0\}\) |
| \(c_3\) | \(\{0,1\}\) | \(\{-2,-1\}\) |

There are no other constraints. The underlying graph is \(K_{2,3}\),
which is bipartite and has ordinary degeneracy two.

The first leaf permits the following anchor values:
\[
\begin{array}{c|c}
a&\text{permitted }b\\ \hline
0&\{2\}\\
1&\{0,1,2\}\\
2&\{1,2\}.
\end{array}
\]
The second permits
\[
\begin{array}{c|c}
a&\text{permitted }b\\ \hline
0&\{0,1\}\\
1&\{2\}\\
2&\{0,2\}.
\end{array}
\]
Their intersection forces \(b=2\) and \(a\in\{1,2\}\).
The third leaf then has \(c_3-b\notin\{-2,-1\}\), so \(c_3=2\).
But \(c_3-a\notin\{0,1\}\) requires \(c_3<a\) for either of the
remaining anchor values. This is impossible.

Thus even a series-parallel underlying graph with at most two forbidden
integer differences per pair need not admit three choices. A proof
based on ordinary vertex degree, bipartiteness, or small separators
needs additional information about the actual constraint relations.

## 3. The valid peeling statement

Weighted peeling remains valid: a vertex with at most two incident
forbidden-difference constraints in total can be removed and restored
after its neighbours are assigned. Each such constraint excludes at
most one of its three values. The \(K_{2,3}\) example has weighted
degree four at every leaf, so it does not contradict this rule.

For the Hilbert P problem, the sparse deletion theorem therefore reduces
the multiplicities but does not dispose of the remaining cores. The
next input must use more of their geometry or arithmetic, or control
their full boundary relations under a recursive decomposition.
