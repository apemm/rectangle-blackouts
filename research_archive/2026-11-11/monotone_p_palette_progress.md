# Monotone P-free classes: bounds and a palette obstruction

11 November 2026. The requested O(h) partition is not proved here. This note gives an elementary O(h log h) upper bound, a new clique lower bound of 2h/3-O(1) for the stated stronger P graph, and a probabilistic obstruction to adding monotonicity directly to the archived independently thinned palette. The last result concerns that implementation, not every correlated palette construction.

Put A=ceil(h/2) and K=floor(h/2). Vertices are labels (i,j), with 0<=i<A and 0<=j<K. A permitted class has distinct i and nondecreasing j as i increases. It must also avoid both orientations of every cross pair satisfying

    16(i-i')^2+[2(j-i')+1]^2=L^2,    L odd, 0<L<h.           (1)

The problem explicitly excludes equal i through the distinct-i rule. All P bounds below apply to (1), without assuming that the alternative white rows fit the height strip. A separate lower bound is given when that containment condition is restored.

## 1. The exact monotonicity-only cost is K

The K constant-j classes are permitted monotone classes before P is imposed. Conversely, the K labels at any fixed i require different classes. Thus the minimum is exactly K.

Equivalently, order labels by (i,j)<(i',j') when i<i' and j<=j'. An antichain has size at most K: different i groups in an antichain have strictly descending, disjoint j sets. One fixed-i group attains K. The A+K-1 constant-offset diagonals give a useful cover, but they are not a minimum chain partition.

## 2. A clique of size 2h/3-O(1)

Consider the graph whose edges encode either failure of monotonicity or a P conflict. Let

    i_0=floor((K-1)/2),    D=floor((K-3)/3).

Include all K vertices (i_0,j), 0<=j<K. For every positive odd d<=D, also include

    R_d=(i_0+d, i_0-(3d+1)/2),
    L_d=(i_0-d, i_0+(3d-1)/2).                              (2)

For large h these indices lie in the grid. The vertices in (2), sorted by increasing i, have strictly decreasing j. Hence they form an antichain and therefore a clique in the constraint graph.

Each such vertex is P-adjacent to every vertex of the fixed-i_0 clique. Its even index satisfies

    2(j-i_0)+1=+3d or -3d,

so the relevant norm is 16d^2+9d^2=(5d)^2. The length 5d is odd and less than h. This test uses the odd point at i_0 and is independent of its even mate j.

The entire set is therefore a clique of size

    K+2 floor((D+1)/2) = (4/3)K-O(1) = 2h/3-O(1).           (3)

In particular, adding P rules prevents a monotone partition with only h/2+o(h) colors. It does not rule out C h colors for a larger absolute constant C. The lower bound also applies if each class must satisfy any additional Lipschitz condition.

For actual in-strip vertical rivals, write a=2i_0+1 and restrict d further by

    4d<=min(a-1,h-a).

The white rows are (a-4d,a+d) for R_d and (a-d,a+4d) for L_d. They then fit in the strip. This retains a clique of size

    K+h/8-O(1) = 5h/8-O(1).                                (4)

Thus the improvement over the monotonicity-only cost is not solely an artifact of dropping white containment.

## 3. An elementary O(h log h) upper bound

Partition the grid by the constant offset s=j-i, or equivalently by the odd integer T=2s+1. Each diagonal is already monotone and has slope exactly one. On this diagonal, a signed difference x of odd indices can be a P witness only if

    (4x)^2+(T-2x)^2=L^2,    x!=0,    0<L<h.                 (5)

Let S_T be the set of positive absolute differences arising from either sign of x in (5). Color the finite diagonal in increasing i order. At most one previous vertex occurs at each difference in S_T, so |S_T|+1 colors suffice.

Sum over T. A signed solution (T,x) of (5) determines an integer right triangle with positive even leg 4|x|, positive odd leg |T-2x|, and hypotenuse less than h. Conversely, a fixed triangle gives at most four signed choices of x and T-2x, hence at most four pairs (T,x). If T_H denotes the number of integer right triangles with hypotenuse at most H=h-1, then

    sum_T |S_T| <= 4T_H.

The primitive Pythagorean parametrization, with coprimality and parity restrictions dropped for an upper bound, gives

    T_H <= sum_(2<=u<=sqrt(H)) sum_(1<=v<u) floor(H/(u^2+v^2))
         <= H sum_(2<=u<=sqrt(H)) 1/u
         = O(h log h).

There are A+K-1 offset diagonals. Using disjoint color palettes on them therefore proves

    chi_monotone,P(h) <= A+K-1+4T_(h-1) = O(h log h).        (6)

This proof does not use an unverified formula for the smallest P gap on a diagonal. Its output classes are monotone, P-free in both orientations, and have Lipschitz constant one. The remaining gap is a logarithmic factor between (3) and (6).

## 4. Independent thinning destroys long eligible monotone chains

Here is a general probabilistic fact. Suppose each candidate vertex/color incidence requires a private independent coin whose success probability is at most theta. Any other eligibility tests may be imposed, and may be arbitrarily correlated. If there are polynomially many colors and theta h^2 tends to infinity sufficiently quickly, then, with probability tending to one, every eligible monotone class has size O(h sqrt(theta)).

For a fixed color, the number of monotone classes of length ell is at most

    binom(A,ell) binom(K+ell-1,ell)
      <= [2e^2 h^2/ell^2]^ell.                             (7)

The first factor chooses its distinct odd indices. The second counts its nondecreasing even indices, allowing repetitions. A prescribed class needs ell independent successful private coins, so its probability is at most theta^ell, regardless of the other eligibility tests. Taking

    ell=ceil(8h sqrt(theta))

makes the union bound at most exp(-c ell). This also holds after conditioning on all nonprivate eligibility randomness. A polynomial union over colors completes the claim whenever ell grows faster than log h.

In the large-band construction of the archived [linear-level palette](../2026-11-09/full_problem_push/global_P_linear_levels.md),

    p=1/(64R),    q=h^(-1/8),
    theta_v=q/(1-p)^{|B(v)|} <= h^(-1/16).

The last inequality follows from the proved blocker bound (1-p)^{|B(v)|}>=h^(-1/16). Applying (7) with theta=h^(-1/16) shows that, with probability tending to one, every eligible monotone color class has at most O(h^(31/32)) vertices.

There are Theta(h^2) labels. The small arithmetic bands contain only h^(4/3+o(1)) labels, so they cannot account for a positive fraction of the grid. Covering the remaining labels by monotone eligible classes would require Omega(h^(33/32)) colors on this high-probability event. The archived O(h)-color budget cannot do so.

This identifies a precise obstruction to running the same independent-thinning experiment and then asking its final matching to be monotone. It does not exclude a rare palette realization, remove the original P-only theorem, or show that every random-row-set palette fails. In particular, the unthinned Hall proof retains correlations between neighboring labels that the private coins destroy. A successful linear monotone palette would need to exploit such correlations or use a different coordinated chain-selection rule.

## 5. What remains open

The proved bounds are

    2h/3-O(1) <= chi_monotone,P(h) <= O(h log h)

for the stated strong graph. The actual in-strip version has the lower bound 5h/8-O(1). Neither lower bound is superlinear. The archived P-only O(h) list theorem does not address the added inversion edges, and the thinning argument cannot be transferred unchanged.

No claim here resolves the remaining even-odd-even right angles, mixed four-cell collisions, or filler compatibility for a full identifying construction. Even a positive answer to this monotone coloring question would be one step toward that construction.
