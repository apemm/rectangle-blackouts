# What dyadic capacity and short relations cannot prove

14 November 2026. This is an abstract limitation of a coloring method,
not a lower bound for the Pell distance sets.

For a set of positive integer distances \(D\), write
\[
 M(D)=\sup_{x>0}|D\cap[x,2x]|.
\]
Even complete exclusion of every relation of a prescribed bounded length
does not permit a polynomial saving over \(M(D)\) in a general coloring
theorem.

**Theorem.** Fix an integer \(g\ge3\). For all sufficiently large integers
\(\Delta\), there is a finite distance set \(D\) such that
\[
 M(D)\le2\Delta,\qquad
 \chi(\operatorname{Cay}(\mathbb Z,D))
 \ge c\frac{\Delta}{\log\Delta},
 \tag{1}
\]
and
\[
 \sum_{d\in D}c_dd=0,\quad
 \sum_{d\in D}|c_d|\le g
 \quad\Longrightarrow\quad c_d=0\ \text{for every }d.
 \tag{2}
\]
The constant \(c>0\) is absolute; the lower cutoff for \(\Delta\) can
depend on \(g\).

Thus these two invariants cannot imply a bound \(C_g M(D)^\alpha\) with
fixed \(\alpha<1\). The theorem does **not** rule out a bound in the total
cardinality \(\kappa=|D|\), nor a better bound for the actual Pell sets.
Here \(\kappa\) is much larger than \(\Delta\).

## 1. A graph with high girth and many required colors

Put \(n=\lceil\Delta^{g+2}\rceil\) and \(p=\Delta/n\).
In the random graph \(G(n,p)\), the expected number of cycles of length
at most \(g\) is \(O_g(\Delta^g)=o(n)\).
Markov's inequality therefore makes that number at most \(n/4\) with
probability tending to one.

For each vertex, the exponential-moment bound gives
\[
 \mathbb P\{\deg(v)\ge2\Delta\}
 \le 2^{-2\Delta}\mathbb E2^{\deg(v)}
 \le(e/4)^\Delta.
\]
After a union bound, the maximum degree is at most \(2\Delta\), with
probability tending to one.

Finally set \(a=\lceil4n\log\Delta/\Delta\rceil\).
The expected number of independent \(a\)-sets is at most
\[
 \binom na(1-p)^{\binom a2}
 \le
 \exp\left(a\log(en/a)-\frac{pa(a-1)}2\right)
 =o(1).
\]
Choose a graph with all three properties. Delete one vertex from each
cycle of length at most \(g\), obtaining a graph \(H\) with at least
\(3n/4\) vertices, maximum degree at most \(2\Delta\), and girth greater
than \(g\). Its independence number is less than \(a\), so
\[
 \chi(H)\ge\frac{|V(H)|}{a}
 \ge c\Delta/\log\Delta.
 \tag{3}
\]
All these estimates follow directly from the displayed elementary
probabilistic bounds.

## 2. Encoding the graph by integer distances

Index the vertices of \(H\) by distinct integers \(0,\ldots,N-1\).
Choose an integer \(B>2g+2\), and put
\[
 x_i=B^i,\qquad
 D=\{B^i-B^j:\ \{i,j\}\in E(H),\ i>j\}.
 \tag{4}
\]
The distances in (4) are distinct. The map \(i\mapsto x_i\) embeds \(H\)
as a subgraph of \(\operatorname{Cay}(\mathbb Z,D)\), proving the
chromatic lower bound.

Distances whose larger endpoint has index \(i\) lie in
\[
 [(1-1/B)B^i,\,B^i].
\]
The ratio between consecutive such intervals is at least \(B-1>2\).
A dyadic interval therefore meets at most one of them.
That interval contains at most \(\deg_H(i)\le2\Delta\) distances.
This proves the capacity bound in (1).

## 3. Every short relation is a short circulation

Suppose a relation as in (2) exists. Orient each edge in (4) from its
smaller to its larger index, and give it signed weight \(c_d\).
Expanding (4) gives
\[
 0=\sum_{i=0}^{N-1}z_iB^i,\qquad |z_i|\le g,
 \tag{5}
\]
where \(z_i\) is the net incoming weight at vertex \(i\).
The choice \(B>2g+2\) forces every \(z_i\) to vanish.
Indeed, the largest nonzero term would have magnitude at least \(B^j\),
while all smaller terms together have magnitude at most
\(g(B^j-1)/(B-1)<B^j\).

A nonzero integral circulation contains a directed cycle after edges
with negative weight are reversed. Its length is at most the sum of
absolute edge weights, hence at most \(g\).
This contradicts the girth of \(H\), proving (2).

One can make \(D\) infinite while retaining these conclusions. Add
positive distances recursively, each greater than four times the
previous maximum and greater than \(g\) times the sum of all previous
distances. A new largest term cannot participate in a relation of
length at most \(g\). Each new dyadic window contains at most one added
distance. The original embedded graph still gives the lower bound.

## 4. Scope for the diagonal problem

For any fixed support bound \(r\) and coefficient cap \(b\), choose
\(g=rb\). The construction then excludes every nontrivial relation
with at most \(r\) terms and coefficients of magnitude at most \(b\),
while retaining (1).

This applies to a proposed black-box theorem based only on dyadic
capacity and bounded-order relation counts. It does not model the
quadratic norm equation, the shared Pell recurrence, or the variation
of the arithmetic parameter \(T\).

In particular, it gives no lower bound for
\(\chi(\operatorname{Cay}(\mathbb Z,D_T))\), and no obstruction to a
polynomial saving in the finite total \(\kappa_T\).
A successful saving for the actual diagonals must use additional
arithmetic structure.
