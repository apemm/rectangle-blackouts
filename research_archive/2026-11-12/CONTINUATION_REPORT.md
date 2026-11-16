# Arc partitions: two deletion obstructions and exact certificates

12 November 2026. No source report or paper was changed, and nothing was
committed. This continues `arc_classes_monotone_partition.md`.

The proposed estimate for deletion to dissociation is false. The arc
construction itself remains open. The work here proves two obstructions,
strengthens the Riesz lemma, and verifies the numerical certificates through
height 16,384.

## 1. The original deletion target is false

Let `D_T(h)` denote the positive forbidden distances that actually fit on
the finite diagonal of offset `T`. If `beta_T` is the least deletion cost
for the bounded-coefficient dissociation required by the original lemma,
then

\[
\boxed{\sum_T\beta_T=\Theta(h\log h).}
\]

This is a theorem about the finite, sign-folded distance sets used by the
script. It is not an artifact of retaining distances too large for a
diagonal, or of counting both signs as separate frequencies.

The construction behind the lower bound is explicit. From each integer
right triangle
\[
(4a)^2+b^2=L_0^2,\qquad L_0\le h/100,\quad L_0\text{ odd},
\]
put
\[
T=5(b-2a),\qquad d=5a,\qquad e=3a+b.
\]
Both `d` and `e` are actual positive forbidden distances for `T`, and
`d-e=-T/5`. At a fixed offset these pairs form a graph of maximum degree
two. Two disjoint retained pairs give a relation with coefficients
`1,-1,-1,1`, so a dissociated set retains at most two edges. There are
`Omega(h log h)` distinct pairs altogether, by an elementary count of
primitive triangles and odd dilations.

The full proof, including all finite-diagonal bounds, is in
[the dissociation audit](continuation_arc_riesz_beta_audit.md).

## 2. A stronger Riesz lemma also has a deletion obstruction

Full dissociation is stronger than the Riesz argument needs. The same
conclusion holds if every zero relation
\[
\sum_{d\in D}c_d d=0,\qquad |c_d|\le m
\]
has **even coefficient sum**. The Fourier coefficients of the normalized
factor `sin^(2m)(pi x)` have sign `(-1)^c`. Under this weaker hypothesis,
every constant-term contribution is nonnegative. The full product integral
therefore dominates every factor-deleted integral, which is enough for the
bad-set estimate.

However, deletion to this weaker condition still cannot have linear total
cost. Define `gamma_T` using the coefficient cap `m(k)` from the four-arc
lemma, where `k` is the retained cardinality. Then, for sufficiently large
`h`,
\[
\boxed{\sum_T\gamma_T
 =\Omega\!\bigl(h\log\log\log\log h\bigr).}
\]
All logarithms in this asymptotic statement are natural. In particular,
`sum gamma_T / h` tends to infinity. The upper bound remains `O(h log h)`;
the exact order is not determined here.

The new obstruction uses the same paired distances differently. Their
difference is odd, so the two distances have opposite parity. Their
primitive two-term relation has odd coefficient sum. Restricting the
primitive triangle to a bounded hypotenuse bounds those two coefficients,
independently of the dilation.

The remaining ingredient is a density theorem: for almost every odd offset
in a fixed small central interval, the number of actual forbidden distances
tends to infinity. Each split prime dividing the offset supplies a distinct
distance, through an elementary norm-Euclidean argument in
`Z[(1+sqrt(5))/2]`. A prime-divisibility second moment makes this quantitative.
Consequently, either a retained set pays many deletions or its coefficient
cap grows enough to detect the two-term relations. Summing the bounded
primitive families gives the displayed lower bound.

See [the parity-sensitive Riesz lemma](continuation_arc_parity_riesz.md)
and [the odd-relation deletion obstruction](continuation_arc_odd_deletion_obstruction.md).
These proofs were independently checked. The obstruction does not disprove
a linear total number of arc classes.

The Riesz calculation also gives a criterion that permits odd relations.
Writing `Z_D` for the product integral, it is enough to prove
\[
2\sqrt m\,\sin^{2m}(\pi/M)
\sum_{d\in D}\frac{Z_{D\setminus\{d\}}}{Z_D}<1.
\]
No estimate giving a linear aggregate palette from these ratios is proved
here. The number `M` must be allowed to vary with the offset; four arcs do
not work uniformly even in the finite certificates.

## 3. The numerical evidence is now independently certified

An integer checker reconstructs every forbidden distance from primitive
Pythagorean triangles and odd dilations. Its completeness is proved. It
uses neither floating-point square roots nor the producer's stored gap
lists. As an implementation check, its enumeration agrees with a separate
integer-square-root enumeration at every height from 2 through 128.

All supplied certificates through 2048 pass. The three larger certificates
were reconstructed from the unchanged producer and independently checked:

| Height | Original total, now checked | Refined total |
|---:|---:|---:|
| 4,096 | 8,718 | |
| 8,192 | 17,777 | |
| 16,384 | 36,169 | 36,165 |

The largest check verifies 41,271 gap constraints covering 67,108,864 labels.
All declared classes are nonempty. The refined certificate improves four
rows of the original certificate.

An exact rational interval calculation also proves that at height 16,384:

| Offset | Minimum arcs for the uniform gap-separation condition |
|---:|---:|
| `+/-1045` | 11 |
| `+/-1595` | 9 |
| `+/-1705` | 10 |

These are minima for the sufficient condition `||theta d|| >= 1/M`, not
chromatic numbers or minima for arbitrary finite arc colorings. Each
infeasibility certificate is a chain of open rational intervals covering
all candidate rotations.

See [the certificate audit](continuation_arc_integer_certificate_audit.md),
[the integer checker](check_arc_certificates_integer.py), and
[the refined certificate](arc_certificate_h16384_refined.json).

The [odd-relation deletion computations](continuation_odd_relation_deletion_certificates.md)
also have exact certificates.
At height 16,384, a greedy construction deletes 16,532 frequencies in total.
An independent signed-coefficient dynamic program verifies all retained
sets at their required caps. These are feasible deletion counts, not
minimum deletion counts. Their small numerical ratios do not contradict
the very slow asymptotic lower bound.

## 4. Corrections and remaining work

The original no-right-angle proposition and Riesz proof pass the audit.
The exponent `m` must be an integer. For three arcs, its leading value is
`log(k)/log(4/3)`, approximately `3.476 log(k)`, rather than `2.4 log(k)`.
The original script reports feasible arc counts, which need not be minima.
Its distance statistics count positive finite-diagonal distances, not the
full signed Pell solution set.

The remaining tasks are:

1. Bound the aggregate arc cost directly, or find a different monotone
   P-free partition. The displayed deletion bounds cannot give a linear
   total by charging a constant number of colors per deleted distance.
2. Control cross-block right angles and mixed four-cell collisions.
3. Construct a compatible singleton sea and its boundary transitions.
4. Establish the quadratic threshold or a stronger threshold lower bound.

This work proves neither `m_h = O(h^2)` nor a general formula for the size
or number of optimal blackouts.
