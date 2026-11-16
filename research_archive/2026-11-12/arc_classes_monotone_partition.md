# Arc classes for the monotone P partition

12 November 2026. Problem 001, fixed height `h`, least equality width `m_h`.

**Outcome. `m_h = O(h^2)` is not proved, and the linear monotone P-free
partition is not proved either.** This note gives a construction that needs
about `2.1 h` classes at every height I tested, a lemma that explains why,
and the exact statement that would make the count linear.

Status labels: **[proved]** means a complete argument is given here, with no
independent audit. **[checked]** means a separate script tested the object
from the definition. **[computed]** means one script produced the number.
**[heuristic]** means a count with no proof.

It continues `../2026-11-11/quadratic_threshold_reattack.md` (Stuck step 1),
`../2026-11-11/monotone_p_palette_progress.md` and
`../2026-11-11/continuation_monotone_queue_experiments.md`.

## 1. Setting

Labels are `(i, j)`, `0 <= i < A = ceil(h/2)`, `0 <= j < K = floor(h/2)`.
The label has odd row `2i+1`, even row `2j+2` and offset `T = 2(j-i)+1`.
A class has distinct `i` and sits in one block, the label `(i, j)` at
column `4i` of the block. Two labels of a class are in P conflict when the
odd point of one and the even point of the other are at an odd integer
distance `L < h`:

    16 (i - i')^2 + (2 (j - i') + 1)^2 = L^2.

With `d = i - i'` this reads `20 d^2 + 4 T d + T^2 = L^2`, where `T` is the
offset of the label that owns the even point. Put

    S_T = { d != 0 : 20 d^2 + 4 T d + T^2 is a square L^2, L < h }.

So the label at slot `i` with offset `T` forbids the slots `i - d`,
`d in S_T`, in its class. The known facts are `sum_T |S_T| = O(h log h)`
and `|S_T| = h^(o(1))` (`../2026-11-09/full_problem_push/global_P_linear_coloring.md`).

## 2. Arc classes [proved]

Fix an offset `T`, a real `theta` and an integer `M >= 1`. The arc classes
of the diagonal `T` are

    C_c = { (i, i + s) : floor(M frac(theta i)) = c },   c = 0, ..., M-1,

with `s = (T-1)/2`.

**Proposition 1.** Suppose `||theta d|| >= 1/M` for every `d in S_T` (here
`||x||` is the distance to the nearest integer). Then every class `C_c`

1. has `j` increasing in `i` with slope exactly 1,
2. has no P conflict,
3. has no right angle at all among its black points, tilted or not.

Proof. Item 1 is clear. For item 2, two slots of one class differ by an `x`
with `||theta x|| < 1/M`, so `x` and `-x` are not in `S_T`. For item 3, the
odd points and the even points of the block lie on two parallel lines of
direction `(2, 1)`, at vertical distance `T`. Take a vertex and two ends.
Two vectors along a line have dot product `20 d1 d2`. A vector along a line
and a vector across have dot product `2 d1 (10 d2 +- T)`, which is not zero
because `T` is odd. Two vectors across have an odd dot product. []

Let `M_T` be the least `M` for which such a `theta` exists. Then the labels
split into `sum_T M_T` classes that are monotone, have slope 1 and are P-free.
The union bound gives `M_T <= 2 |S_T| + 1`, so `sum_T M_T = O(h log h)`.
That is the order already known. The gain is in the constant and, I expect,
in the logarithm.

## 3. Certificates

`arc_classes/arc_partition.py` searches `theta = a/q` and writes
`(s, a, q, M)` for each diagonal. `arc_classes/check_arc_partition.py`
rebuilds the classes from these four numbers and tests coverage, monotonicity
and the P norm in both orders for every pair in a class.

| `h` | arc classes | per `h` | queue certificates of 11 November | status |
| ---: | ---: | ---: | ---: | --- |
| 32 | 51 | 1.59 | 61 | [checked] |
| 64 | 106 | 1.66 | 149 | [checked] |
| 128 | 239 | 1.87 | 347 | [checked] |
| 256 | 488 | 1.91 | 774 | [checked] |
| 512 | 1014 | 1.98 | 1725 | [checked] |
| 1024 | 2080 | 2.03 | | [checked] |
| 2048 | 4290 | 2.09 | | [checked] |
| 4096 | 8718 | 2.13 | | [computed] |
| 8192 | 17777 | 2.17 | | [computed] |
| 16384 | 36169 | 2.21 | | [computed] |

The height 2048 check tested 349,202,082 ordered pairs. The lower bound for
any monotone P-free partition is `2h/3 - O(1)`.

How `M_T` depends on `|S_T|`, at `h = 16384` [computed]:

| `|S_T|` | diagonals | mean `|S_T|` | mean `M_T` |
| --- | ---: | ---: | ---: |
| 0 | 6105 | 0 | 1.00 |
| 1 to 2 | 5202 | 1.44 | 2.11 |
| 3 to 5 | 2968 | 3.89 | 3.38 |
| 6 to 10 | 1308 | 7.60 | 3.70 |
| over 10 | 800 | 15.34 | 5.25 |

In each band the mean `M_T` falls or stays as `h` grows (band 6 to 10:
4.40, 4.02, 3.80, 3.70 at `h = 512, 2048, 8192, 16384`). The total grows
because more diagonals reach the higher bands.

## 4. A lemma for sets without small relations [proved]

**Lemma 2.** Let `D` be a set of `k` nonzero integers and `m >= 1`. Suppose
that `sum c_d d != 0` for every nonzero integer vector `c` with all
`|c_d| <= m`. If `0 < delta <= 1/2` and

    2 k sqrt(m) sin^(2m)(pi delta) < 1,

then some `theta` has `||theta d|| >= delta` for every `d in D`.

Proof. Put `g(x) = sin^(2m)(pi x) / mu`, with `mu` the mean of
`sin^(2m)(pi x)` over a period, so `mu = binom(2m, m) / 4^m >= 1/(2 sqrt m)`.
Then `g >= 0`, and `g` is a trigonometric polynomial with frequencies
`|c| <= m` and constant term 1. Let `G(theta) = prod_d g(theta d)`. The
integral of `G` over a period is the sum of the products of coefficients
over all `c` with `sum c_d d = 0`, which is 1 by the hypothesis. The same
holds for every subproduct. On the set where `||theta d0|| < delta` the
factor of `d0` is at most `sin^(2m)(pi delta) / mu`, so the integral of `G`
over that set is at most `2 sqrt(m) sin^(2m)(pi delta)`. If these `k` sets
covered the circle, the integral of `G` would be less than 1. []

With `delta = 1/4` the condition is `2 k sqrt(m) < 2^m`, so
`m = log2 k + O(log log k)` is enough, and then 4 arcs suffice. With
`delta = 1/3` it needs `m` about `2.4 ln k`.

**Corollary 3.** Let `beta_T` be the least number of elements whose removal
from `S_T` leaves a set that satisfies the hypothesis of Lemma 2 with
`delta = 1/4`. Then the diagonal `T` splits into at most `4 (beta_T + 1)`
classes with the three properties of Proposition 1. (Color by the arc of
the reduced set and by a proper coloring of the distance graph of the
removed elements.) Hence

    chi_mon,P(h) <= 4 sum_T (beta_T + 1).

So a linear partition would follow from `sum_T beta_T = O(h)`.

**Correction, same day. That estimate is false.** `CONTINUATION_REPORT.md`
proves `sum_T beta_T = Theta(h log h)`. Each right triangle
`(4a)^2 + b^2 = L0^2` gives the offset `T = 5(b - 2a)` with the two
forbidden distances `5a` and `3a + b`, which differ by `T/5`. I checked the
two substitutions: both give `20 d^2 + 4 T d + T^2 = 25 L0^2`. Two such
pairs at one offset give a relation with coefficients `1, -1, -1, 1`. The
report also weakens the hypothesis of Lemma 2 to "every relation has even
coefficient sum" and shows that deletion to that condition costs
`Omega(h log log log log h)` in total. So Corollary 3 is true but cannot
give a linear bound. Lemma 2 and the certificates stand.

## 5. Why the count should be linear [heuristic]

- The elements of `S_T` are `d = (X - T)/10` for the solutions of
  `X^2 - 5 L^2 = -4 T^2`. They form one Pell orbit per ideal of norm `T^2`
  in `Z[(1+sqrt 5)/2]`. A typical `T` has about `3^w` orbits, `w` the number
  of prime factors of `T` that are `1` or `4` modulo 5. So the typical
  `|S_T|` tends to infinity, like a power of `log h` below 1. The mean is
  of order `log h` and comes from few offsets with many such prime factors.
- For `k` integers with no special relation, a `theta` with all
  `||theta d|| >= 1/3` has probability about `3^(-k)`, and one exists when
  `3^k` is below the number of slots. Beyond that the count is about
  `2k / ln h`. This is the behavior of a random Cayley graph. It gives
  `M_T` bounded for most offsets and `sum_T M_T = O(h)`.
- Any class system in which a label with `k` forbidden slots meets
  independent random slots pays a factor that grows with `k`. Monotone
  classes of bounded slope leave only boundedly many candidate classes per
  label, so the Hall argument of the linear palette cannot be reused. The
  arc structure is what replaces it.

## 6. Relations that do exist [proved, by direct substitution]

Lemma 2 does not apply to `S_T` as it stands.

- `T` is in `S_T` when `5|T| < h`, and `-3T` when `13|T| < h`. In general
  `S_T` contains `T` times the set `S_1 = {1, -3, -20, 52, 357, -935, ...}`.
- If `5 | T`, then `-T/5` is in `S_T`, and `S_T` is symmetric: `d` is in
  `S_T` exactly when `-d - T/5` is. This gives the triples
  `d + d' = -T/5` and many four-term relations. At `h = 16384` the offsets
  divisible by 5 have mean `M_T = 3.03`, the others `2.00` [computed].
- Small elements have small relations for trivial reasons. For example
  `S_11` contains `2, -3, 5`.

A proof of `sum_T M_T = O(h)` has to treat the scales separately (the
orbits are lacunary) and has to bound the relations between different
orbits at one scale. I do not have that bound.

## 7. A remark on the sea [proved]

Let `a, b` be coprime, `j >= 1`, `u = j a^2`, `v = j b^2`. Let `nu` be the
2-adic valuation of `j`. Then two of `u`, `v`, `v - u` have valuation
exactly `nu` and the third has valuation at least `nu + 2`. (If `a, b` are
odd, the third is `v - u`. Otherwise it is the one with the even square.)

Consequence. In the one-label collisions with a row-1 sea
(`../2026-11-11/quadratic_threshold_reattack.md`, Section 6) the three sea
columns are `c - u`, `c + v - u`, `c + v`. If `c` is divisible by 4, one of
them is divisible by 4. So if every column that is not divisible by 4
carries a row-1 singleton, and no column divisible by 4 is black in row 1,
this family of collisions is empty. The columns divisible by 4 that hold no
double then need a singleton in another row, and the same question returns
for that row at the next scale. I did not solve that.

## 8. What this does not give

- A bound on `m_h`. A valid board also needs the cross-block right angles
  with an even vertex, one odd end in the same block and one even end in
  another block, the mixed four-point collisions, and a sea.
- A proof that `sum_T M_T = O(h)`.
- Any lower bound for `m_h`.

## 9. Files

- `arc_classes/arc_partition.py`, `arc_classes/check_arc_partition.py`.
- `arc_classes/arc_certificate_h32.json` to `arc_certificate_h2048.json`.
  Each row is `s`, `a`, `q`, `M` and the blocked differences of the diagonal.
