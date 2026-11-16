# Opposite horizontal pairings in clustered P six-cycles

15 November 2026. A central genuine P six-cycle whose six signed
horizontal legs cancel in three opposite pairs has a subquadratic
incidence bound in the critical three-nearby-height-pair regime. The
horizontal pairs need not agree with the nearby-height pairs. Comparing
the two matchings supplies the missing arithmetic saving in that case.

For cluster radius \(r=h^{o(1)}\), the cross-matching contribution has
expected size \(h^{7/4+o(1)}\). The identical-matching contribution is
already covered by the stable Hilbert cross-rank theorem, under its
separate minimum-gap hypothesis. The unresolved arithmetic branch has
six signed horizontal legs summing to zero without an opposite-pair
partition. This is a result about directed-object P cycles, not a repair
of the older arithmetic energy conjecture.

## 1. Two matchings on the edge indices

Use the central genuine multiscale model and fixed bounded column
provenance. Let the six directed cycle edges have signed vectors
\((X_v,Y_v)\), where
\[
             Y_v=b_{v+1}-a_v,\qquad X_v=x_{v+1}-x_v.
             \tag{1}
\]
Every edge is an actual in-strip P: \(X_v\ne0\), \(Y_v\) is odd,
and
\[
                X_v^2+Y_v^2=L_v^2,\qquad L_v<h.
                \tag{2}
\]
In particular, both legs have magnitude at most \(h\).

Fix a perfect matching \(\mathcal H\) on the six edge indices. Its
pairs have edge-coordinate points \((i_v,j_{v+1})\) within raw distance
\(2r\), for \(1\le r\le C\sqrt h\). Bounded physical row gaps imply
\[
                   |Y_u-Y_v|\le C_1(r+1)
                   \quad(uv\in\mathcal H).          \tag{3}
\]
The argument below needs only (3), together with the central locality
bound
\[
                   |Y_u-Y_v|\le C_2\sqrt h
                   \quad\hbox{for every }u,v.        \tag{4}
\]
Indeed, the six actual horizontal gaps give an \(O(h)\) raw-rank
span. Hilbert locality gives an \(O(\sqrt h)\) raw-coordinate box,
and the two sampled row maps have uniformly bounded adjacent gaps.

Suppose a second perfect matching \(\mathcal X\) satisfies
\[
                         X_u=-X_v
                         \quad(uv\in\mathcal X).     \tag{5}
\]
There are only fifteen possibilities for each matching. They can be
fixed before counting and summed afterward. Repeated leg values may
admit more than one matching; a finite union only increases the bound.

If \(\mathcal X\ne\mathcal H\), their union is an alternating
multigraph with either one component of length six or two components
of lengths four and two. A common matching edge is represented by two
parallel edges, one from each matching. Write \(c\in\{1,2\}\) for
the number of components.

## 2. Enumerate full norm vectors along the overlay

For a fixed nonzero horizontal leg \(X\), there are \(h^{o(1)}\)
possible signed heights of an in-strip integral norm, by
\[
                         (L-Y)(L+Y)=X^2.             \tag{6}
\]
For a fixed nonzero odd height \(Y\), there are \(h^{o(1)}\)
possible signed horizontal legs, by
\[
                         (L-X)(L+X)=Y^2.             \tag{7}
\]
The bounds are uniform over the indicated ranges. All occurrences of
\(h^{o(1)}\) below absorb only a fixed number of divisor factors,
bounded provenance choices, and fixed powers of logarithms.

Break each alternating component at one \(\mathcal H\)-edge and
traverse the resulting path. Its first and last edges belong to
\(\mathcal X\). A component on \(2\ell\) vertices uses \(\ell\)
horizontal-pair steps and \(\ell-1\) nearby-height steps. Across all
components, the number of nearby-height steps is \(3-c\).

For the first component, choose the signed horizontal leg of its first
vertex in \(O(h)\) ways, then its height using (6). At an
\(\mathcal X\)-step, the new signed horizontal leg is fixed by (5),
and (6) gives divisor-many choices for its height. At an
\(\mathcal H\)-step, (3) gives \(O(r+1)\) choices for the new
height, and (7) then gives divisor-many horizontal legs.

If a second component exists, choose its first height within
\(O(\sqrt h)\) of the first component's root height, using (4).
Equation (7) supplies its first horizontal leg. Continue as above.
The unused closing \(\mathcal H\)-constraint in each component
can be discarded in an upper bound.

Thus the number of full six-vector tuples is at most
\[
             h^{1+(c-1)/2+o(1)}(r+1)^{3-c}.         \tag{8}
\]
This enumeration fixes all six signed heights and legs before testing
their sampled row equations. It makes no independence assumption about
the six edge events.

Choose the first physical column in \(O(h^2)\) ways. The six legs
then determine all subsequent columns. For fixed bounded provenance,
there are only a bounded number of originating raw objects at each
column. Reject invalid, repeated, nonclosing, or out-of-strip candidates.
The resulting upper bounds on rank-and-height candidates are
\[
 \begin{array}{c|c}
 c&\text{number of candidates}\\ \hline
 2& h^{7/2+o(1)}(r+1),\\
 1& h^{3+o(1)}(r+1)^2.
 \end{array}                                       \tag{9}
\]
The opposite horizontal matching already enforces total horizontal
closure. Discarding the other consistency requirements causes no loss
of validity in these upper bounds.

## 3. Balance arithmetic enumeration against the coordinate count

Fix the two sorted raw-coordinate orders and dyadic bins for their ten
adjacent-gap weights. As in the
[mixed-tree note](continuation_mixed_path_tree_probability.md), let
\(Q_0,Q_1\) be the two path products, \(\tau\) the minimum product
of a spanning tree in their union, and
\[
                         K=Q_0Q_1/\tau.
\]
All products use the bin's lower dyadic representatives. Replacing
actual weights by these representatives changes constants only.

The reviewed point-mass kernel bounds every fixed rank-and-height
candidate by
\[
                             {h^{o(1)}\over hK}.    \tag{10}
\]
Independently, the direct coordinate enumeration in the
[height-first note](continuation_height_first_five_cycle_bound.md),
Section 1, applies to six indices too and gives
\[
                    \mathbb E N_{\rm bin}
                         \le h^{1+o(1)}\tau
                         \le h^{1+o(1)}K.           \tag{11}
\]
For the last inequality, \(\tau\le\min(Q_0,Q_1)\), hence
\(\tau^2\le Q_0Q_1\). The direct count includes all actual
six-cycles in the bin, so it also bounds either matching subclass.

Combining (9)--(11), the two-component subclass has expectation at most
\[
 h^{o(1)}\min\left\{hK,{h^{5/2}(r+1)\over K}\right\}
              \le h^{7/4+o(1)}\sqrt{r+1}.           \tag{12}
\]
The one-component subclass has expectation at most
\[
 h^{o(1)}\min\left\{hK,{h^2(r+1)^2\over K}\right\}
              \le h^{3/2+o(1)}(r+1).                \tag{13}
\]
Both balances hold for every positive \(K\); no critical-bin
assumption such as \(K\asymp h\) is needed. The number of bins is
\(h^{o(1)}\). Summing the bins, coordinate orders, and matchings
preserves the bounds. For \(r\le C\sqrt h\), (12) dominates (13)
up to a constant.

Consequently, all cross-matching cycles admit the incidence bound
\[
       \mathbb E N_{\mathcal X\ne\mathcal H}
                    \le h^{7/4+o(1)}\sqrt{r+1}.      \tag{14}
\]
This probabilistic bound uses genuine central rows, bounded provenance,
and actual in-strip P legs. It does not require a minimum P gap.

## 4. Combine with the identical-matching branch

When \(\mathcal X=\mathcal H\), the two horizontal legs cancel
within each raw edge-coordinate pair. The stable
[Hilbert cross-rank theorem](continuation_hilbert_cross_rank_order.md),
Section 5, meets every such cycle with a deterministic boundary set of
size
\[
                       h^{7/4+\delta/2+o(1)}        \tag{15}
\]
when \(r=h^\delta\), \(0\le\delta<1/2\), and the minimum
surviving P gap is \(q_*=h^{1-o(1)}\). Its fixed-provenance
hypotheses must also hold. This is an additional geometric input, not
a consequence of the overlay enumeration.

Mark all genuine vertices of the cycles counted in (14), and add the
deterministic set from (15). The expected marking cost has the order
in (15). It can be included in the existing joint nonnegative-cost
objective. In particular, for \(r=h^{o(1)}\), a set of
\(h^{7/4+o(1)}\) genuine objects meets every clustered six-cycle
whose horizontal legs can be partitioned into opposite pairs.

After this reduction, a surviving cycle in the same clustered regime
must satisfy a genuinely non-pairwise relation
\[
                           X_0+\cdots+X_5=0:
\]
there is no perfect matching with \(X_u=-X_v\). Unequal
representations within one height pair do not by themselves put a cycle
in this remaining class; they may exchange their opposite legs across
different height pairs, and those exchanges are covered by (14).

The result does not bound all six-cycle incidences, all cycle lengths,
or singleton reachability. Safe erasure and relocation of the marked
genuine pairs remain separate requirements. It also does not prove the
arithmetic energy estimate called E in the older archive: those sums
range over a different incidence structure.

## 5. One cross-type norm coincidence already saves a power

A related upper bound needs only one norm coincidence. Fix two edge
indices belonging to different pairs of \(\mathcal H\), and suppose
either
\[
                    |X_u|=|X_v|\quad\hbox{or}\quad L_u=L_v.
                    \tag{16}
\]
No condition on the horizontal signs and no pairing of the other four
legs is needed. Then
\[
 \mathbb E N_{\text{one cross-type coincidence}}
                    \le h^{7/4+o(1)}(r+1)^{3/2}.    \tag{17}
\]

To see this, join the three disjoint edges of \(\mathcal H\) by
the one additional edge in (16). The result has two tree components,
one on four vertices and one on two. Choose a first root horizontal leg
in \(O(h)\) ways and its norm height in divisor-many ways. Choose
the other component's root height within \(O(\sqrt h)\) of it,
then its horizontal leg in divisor-many ways. Traverse all three
\(\mathcal H\)-edges, each costing \(O(r+1)\) times a divisor
factor. The extra edge costs a divisor factor alone. For equal
absolute horizontal legs this follows from (6). For equal hypotenuses,
the number of integer representations
\(X^2+Y^2=L^2\) is at most \(4\tau(L^2)=h^{o(1)}\), by factoring
in the Gaussian integers: each split prime's exponent can be assigned
between a factor and its conjugate in at most one plus that exponent
ways, and the four units supply the factor four.

The full vector count is therefore
\(h^{3/2+o(1)}(r+1)^3\). After choosing the first column and using
(10), it gives \(h^{5/2+o(1)}(r+1)^3/K\). Balance this with
\(h^{1+o(1)}K\), exactly as in Section 3, to obtain (17).
There are only a bounded number of choices of the two edge indices.

For \(r=h^{o(1)}\), marking the genuine vertices in these incidences
has expected cost \(h^{7/4+o(1)}\). Thus the remaining clustered
six-cycle branch can be restricted further: distinct nearby-height
pairs share neither an absolute horizontal leg nor a hypotenuse. This
does not remove coincidences within one nearby-height pair. Those were
the different case addressed by Sections 2--4 and the
[paired-leg reduction](continuation_paired_leg_six_cycle_reduction.md).
For a power radius \(r=h^\delta\), (17) remains subquadratic only
when \(\delta<1/6\); the stronger range for a full opposite matching
in Section 4 is unchanged.

## 6. All ratios of bounded arithmetic height

The same argument can sum a growing collection of coincidences. Say
that a positive rational number has arithmetic height at most \(B\)
when its reduced numerator and denominator are both at most \(B\).
For \(1\le B\le h\), the expected number of clustered cycles
having two edges in different \(\mathcal H\)-pairs with either
\[
           {|X_u|\over|X_v|}={m\over n}
           \quad\hbox{or}\quad {L_u\over L_v}={m\over n},
           \qquad \max(m,n)\le B,
           \tag{18}
\]
is at most
\[
                       h^{7/4+o(1)}B^{1/2}(r+1)^{3/2}.
                       \tag{19}
\]
The coprime positive pair \((m,n)\) is allowed to vary.

For a fixed ratio, start the four-vertex tree component of Section 5
at one endpoint of the extra edge. The absolute horizontal legs are
\(mt,nt\), so the root multiplier has at most
\(h/\max(m,n)\) possibilities. Its signed norm height has
divisor-many choices; the other endpoint's horizontal leg is then
fixed, up to its sign. The rest of the traversal is unchanged.
For hypotenuses, start with \(L_u=mt,L_v=nt\) instead and use the
same sum-of-two-squares bound. Thus the fixed-ratio full vector count
is bounded by
\[
       {h^{3/2+o(1)}(r+1)^3\over\max(m,n)}.          \tag{20}
\]
It is important to sum (20) before balancing it against the direct
coordinate count. The elementary estimate
\[
        \sum_{1\le m,n\le B}{1\over\max(m,n)}
        \le 2B                                                   \tag{21}
\]
follows by grouping pairs according to their maximum. Requiring
coprimality can only decrease it. Consequently the arithmetic bound
for a bin is \(h^{5/2+o(1)}B(r+1)^3/K\), while (11) still
bounds the entire union by \(h^{1+o(1)}K\). Their balance proves
(19).

For \(r=h^{o(1)}\) and any fixed \(\varepsilon>0\), taking
\(B=h^{1/2-\varepsilon}\) gives an expected marking cost
\(h^{2-\varepsilon/2+o(1)}\). After marking these incidences,
cross-type horizontal pairs satisfy
\[
       {\max(|X_u|,|X_v|)\over\gcd(|X_u|,|X_v|)}
                              >h^{1/2-\varepsilon},              \tag{22}
\]
and the analogous statement holds for hypotenuses. In particular,
since each leg is at most \(h\), a common horizontal divisor of
size at least \(h^{1/2+\varepsilon}\) is excluded. No claim is
made that the resulting six-term additive relation is rare enough;
(22) is a proved arithmetic restriction on the remaining branch.

## 7. Separated heights, legs, and hypotenuses in the remainder

The same two-component traversal also treats a cross-type near
coincidence. If two indices in different \(\mathcal H\)-pairs satisfy
any one of
\[
 \begin{split}
 |Y_u-Y_v|&\le T,\\
 \bigl||X_u|-|X_v|\bigr|&\le T,\\
 |L_u-L_v|&\le T,
 \end{split}                                                    \tag{23}
\]
then their cycle incidence is bounded by
\[
                 h^{7/4+o(1)}(T+1)^{1/2}(r+1)^{3/2}.             \tag{24}
\]
Here \(0\le T\le C\sqrt h\), and all three cases can be
summed with a constant factor. The extra forest edge now costs
\(O(T+1)\) choices of the specified height, absolute leg, or
hypotenuse, followed by a divisor factor for the other norm data.
The vector bound becomes
\(h^{3/2+o(1)}(T+1)(r+1)^3\). The same direct-coordinate balance
proves (24).

For \(r=h^{o(1)}\), set \(T=h^{1/2-\varepsilon}\). Marking
these incidences costs \(h^{2-\varepsilon/2+o(1)}\). Together
with Section 6, the remaining arithmetic problem can therefore be
restricted to three height clusters with all cross-type signed heights,
absolute horizontal legs, and hypotenuses separated by more than
\(h^{1/2-\varepsilon}\), and with cross-type horizontal and
hypotenuse ratios of arithmetic height greater than that threshold.
All signed heights still lie in a common \(O(\sqrt h)\) interval.
These conditions are compatible; no contradiction or final additive
count is asserted.

## 8. A fixed-length forest formulation

The mechanism extends to any fixed cycle length \(k\). Partition its
edge-coordinate points into \(m\) prescribed clusters of raw diameter
at most \(2r\). Within each cluster, signed norm heights differ by
\(O_k(r+1)\). Add a prescribed collection of cross-cluster norm
relations, each of which determines one endpoint's horizontal leg,
height, or hypotenuse from the known norm at the other endpoint with
at most a bounded number of possibilities, in either traversal
direction. Examples are a fixed nonzero rational ratio of absolute
horizontal legs or hypotenuses, and a fixed difference of signed
heights. The relations must be fixed before counting; an unrestricted
choice of their constants is not free.

Suppose the resulting graph of clusters has \(c\) components.
Choose a tree inside each raw cluster and a spanning forest of the
cluster-relation graph. The resulting forest on edge indices uses
\(k-m\) nearby-height edges and \(m-c\) norm-relation edges.
All heights are in a common \(O_k(\sqrt h)\) interval by locality.
Exactly as in Sections 2 and 5, its full norm-vector count is at most
\[
             h^{(c+1)/2+o(1)}(r+1)^{k-m}.            \tag{25}
\]
The first root norm costs \(O(h)\) times a divisor factor, each
further root height costs \(O_k(\sqrt h)\) times such a factor,
and the \(k-m\) nearby-height steps supply the displayed power of
\(r+1\). At a prescribed norm-relation step, the remaining norm
data have only divisor-many possibilities.

After the first-column choice and the mixed kernel, balance the
arithmetic bound with the direct \(h^{1+o(1)}K\) bound. The
expected incidence is at most
\[
                h^{(c+5)/4+o(1)}(r+1)^{(k-m)/2}.    \tag{26}
\]
For \(r=h^{o(1)}\), every fixed pattern with \(c\le2\) is
subquadratic: the exponents are \(3/2\) and \(7/4\), respectively.
Three unrelated norm components give the first quadratic exponent in
this argument. A fixed or \(h^{o(1)}\)-sized predetermined menu of
relation patterns can be summed without changing these exponents.

Formula (26) is an incidence statement for each fixed cycle length.
It does not assert that every cycle has the required norm relations,
or that their component count is bounded. In particular, it supplies
no general estimate for the genuinely additive branch left above.

## Review status

The constituent mixed-tree kernel, direct coordinate count, and stable
cross-rank theorem were independently reviewed. The complete saved proof
also passed a separate written review: the alternating-component count,
the root-height choices, the fixed-target probability order, both
arithmetic/coordinate balances, and the separate minimum-gap hypothesis
for the identical matching were checked again. No correction was needed.
The additional one-coincidence result in Section 5 also passed a separate
written review, including the common-hypotenuse case. The saved growing-
ratio extension in Section 6 and near-coincidence extension in Section 7
then passed a separate review: the ratios are summed before balancing,
and each of the three norm statistics has the claimed traversal cost.
The saved fixed-length forest formulation in Section 8 also passed
independent review: the expanded forest has the stated numbers of both
edge types, the norm relations work in either traversal direction, and
the root count gives the exponent \((c+5)/4\).
