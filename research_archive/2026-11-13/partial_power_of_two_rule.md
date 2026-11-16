# A partial power-of-two rule, and where the divisor load comes from

13 November 2026. Problem 001, fixed height `h`, least equality width `m_h`.

**Outcome. `m_h = O(h^2)` is not proved here.** The attack of this day
went through the rigid placements and came out at the same wall as before.
This note records one new lemma, what it shows about the wall, and two
leads.

Status labels: **[proved]** means a complete argument is given here, with
no independent audit. **[checked]** means a script tested the statement
from the definition. **[heuristic]** means a count with no proof.

It continues `../2026-11-11/quadratic_threshold_reattack.md` (Stuck step 2)
and `../2026-11-12/arc_classes_monotone_partition.md`.

## 1. What was already known

I first derived again a placement that the archive already has. Put the
label `(i, j)` at the column `4n` with `n = i` modulo a prime `p > 10h`
and `n = j` modulo a power of two `N >= K`. Then no three label points
form a tilted right angle. This is
`../2026-11-09/full_problem_push/continuation_power_two_filler_coupling.md`
and rows T19 to T22 of the ledger. Its defects are also on file:

- The position of a label is fixed modulo `pN`. Two labels of one
  diagonal at a forbidden distance must go to different copies of the
  period ("layers"). The number of layers is the largest chromatic number
  of the distance graphs `G_T` (row T22). It is at least 6, and I expect
  it to be unbounded (Section 5).
- Four labels can still form a mixed collision (row T21).

So read rows T17 to T22, T31 and T34 before any new attempt with a
congruence scaffold.

## 2. The partial rule [proved], [checked]

Setting. The label `(i, j)`, `0 <= i < A`, `0 <= j < K`, has its odd
point at `(4n, 2i+1)` and its even point at `(4n, 2j+2)`, for an integer
`n = n(i, j)`, and distinct labels have distinct `n`. Let `r >= 0`.
Assume

    n(i, j) - j  is constant modulo 2^r.                          (R)

For `2^r >= K` this is the power-of-two half of the rigid placement. For
smaller `r` it leaves the label a choice of `n` in a residue class.

**Lemma 1.** Assume (R). Let `V` be the even point of a label, and let a
right angle at `V` have the ends `P` and `Q`, where `Q` is the even point
of another label.

1. If `P` is an odd point, put `a = n_P - n_V`, `b = row(P) - row(V)`
   and `e = j_Q - j_V`. Then the angle is axis-aligned, or `a != 0`,
   `e != 0`, and

       2^(r+3) divides e   and   |e| >= 2^(r+3) |a| / gcd(a, b).

2. If `P` is an even point, then one of the two legs joins even points
   whose indices `j` differ by at least `2^(r+1)`.

Hence there is no tilted right angle of the first kind when
`2^(r+3) >= K`, and none of the second kind when `2^(r+1) >= K`.

Proof. Put `f = n_Q - n_V`, so `f != 0`. By (R), `f = e + D` with `2^r`
dividing `D`.

Item 1. Here `b` is odd, and the angle is right when `8 a f = -b e`. If
`a = 0`, then `e = 0` and the angle is axis-aligned. If `e = 0`, then
`a = 0`. Otherwise `e (8a + b) = -8 a D`. Let `g = gcd(a, b)`. Since `b`
is odd, `gcd(8a, 8a + b) = g`, so the odd number `(8a + b)/g` divides `D`.
Write `D = l (8a + b)/g`. Then `l != 0`, `2^r` divides `l`, and
`e = -8 (a/g) l`.

Item 2. Let the legs have `a_k = n_k - n_V` and `e_k = j_k - j_V`,
`k = 1, 2`. The angle is right when `4 a_1 a_2 = -e_1 e_2`, and no factor
is zero. If the 2-adic valuation of `e_k` is below `r`, then `a_k` has the
same valuation. If this held for both legs, the two sides would have
valuations that differ by 2. So some `e_k` is divisible by `2^r`. If the
other one is not, then `v(e_k) = 2 + v(a_k) >= r + 2`. If both are, then
`v(e_1) + v(e_2) = 2 + v(a_1) + v(a_2) >= 2r + 2`, so one of them is
divisible by `2^(r+1)`. []

`check_partial_rule.py` places all labels at random columns that satisfy
(R) and tests every right angle with an even vertex. At `h = 24`
(`K = 12`), 12 placements for each `r`:

| `r` | first kind | second kind | violations of Lemma 1 |
| ---: | ---: | ---: | ---: |
| 0 | 147 | 628 | 0 |
| 1 | 0 | 567 | 0 |
| 2 | 0 | 57 | 0 |
| 3, 4, 5 | 0 | 0 | 0 |

The zeros start where the lemma says: `2^(r+3) >= 12` at `r = 1`, and
`2^(r+1) >= 12` at `r = 3`.

## 3. Constant-offset blocks [proved]

Use the one-prime scaffold `n = i + p c` with a prime `p > 10h`, so that
blocks are more than `36h` columns apart and no tilted right angle has an
odd vertex. Let block `c` hold labels of one diagonal `j = i + s_c`
(offset `T_c = 2 s_c + 1`). Rule (R) reads `p c = s_c` modulo `2^r`.

A block has no right angle (Proposition 1 of the note of 12 November). A
right angle that meets two blocks has an even vertex `V`, an odd end `P`
in the block of `V`, and an even end `Q` in another block
(`../2026-11-11/quadratic_threshold_reattack.md`, Section 3). Let `d_1`
be the slot difference from `V` to `P`. Then `a = d_1` and
`b = 2 d_1 - T`, so `gcd(a, b) = gcd(d_1, T)`. Lemma 1 gives:

**Corollary 2.** Under `p c = s_c` modulo `2^r`, every tilted right angle
among the label points has

    |d_1| / gcd(d_1, T)  <=  (K - 1) / 2^(r+3),

and the two blocks have `p (c' - c) - (s' - s) = l (10 d_1 - T) / gcd(d_1, T)`
with `2^r` dividing `l` and `8 |d_1 l| / gcd(d_1, T) < K`.

So the only dangerous pairs of slots in a class of the diagonal `T` are
at a distance `g d'`, where `g` divides `T` and `d'` is small. The leg
from `V` to `P` is then `g` times a short vector. A short direction has
many perpendicular lattice vectors, and this is why these pairs produce
right angles.

## 4. The load of the surviving angles [heuristic]

Let `R = K / 2^r`. A label then has about `R` times as many admissible
blocks as in the rigid placement, and the surviving angles at a label of
offset `T` are counted by

    sum over g | T, over d' < R/8 with g d' a slot difference of its class,
    of 1/d'.

At block density `rho` this is about `c rho^3 tau(T) log R` fatal angles
per label, with `tau` the number of divisors. Without any rule the same
count is `c rho^3 tau(T) log h`, which is the `log^2 h` load of
Section 5 of the note of 11 November after averaging over `T`.

Consequences.

- A label can absorb a load up to the logarithm of its number of
  admissible positions. With `R` admissible blocks this needs
  `rho^3 tau(T)` bounded. If each diagonal is given its own density,
  the width is about `h^2` times the mean of `tau(T)^(1/3)`, which is
  `h^2 (log h)^(2^(1/3) - 1)`, about `h^2 (log h)^0.26`.
- The rule removes the factor `log h` for every `R`, but never the
  factor `tau(T)`. Only `R <= 8` removes it, and then the placement is
  rigid.
- So the obstruction to `O(h^2)` in this family is the offsets with many
  divisors. An offset with boundedly many divisors has a load of order
  `rho^3 log R`, which is harmless.

## 5. The diagonals that carry the mass [proved in part]

**Remark 3 [proved].** Let `D` be `k` positive integers below `N`. If
`(m+1)^k > k m N + 1`, two of the sums `sum c_d d` with `0 <= c_d <= m`
are equal, so `D` has a nonzero relation with coefficients of absolute
value at most `m`. So Lemma 2 of the note of 12 November applies only to
sets with `k <= log(k m N) / log(m + 1)`.

For the diagonal sets this means `|D_T| < c log h`. The sizes behave like
`3^w`, with `w` the number of prime factors of `T` that split in
`Q(sqrt 5)`. The typical size is a power of `log h` below 1, but the
sum of the sizes, which is of order `h log h`, comes from diagonals with
`|D_T|` near `(log h)^1.65` [heuristic]. At `h = 16384` the diagonals with
more than 10 distances are 5 percent of all diagonals and carry
30 percent of the distances [computed, table of 12 November].

So even a perfect treatment of the typical diagonals leaves the bound
`sum_T M_T = O(h log h)` unchanged. An improvement has to beat the greedy
bound `|D_T| + 1` on diagonals with far more than `log h` distances, and
no hypothesis about missing relations can hold there. A random set of
that size has an arc partition with about `2 |D_T| / ln h` classes, but
the proof for random sets uses the randomness.

The same count explains the layers of Section 1. If `G_T` behaves like a
random circulant graph, its chromatic number is about
`1 + |D_T| / ln h`, which is unbounded over `T`. I have no proof of
either direction.

## 6. Leads

1. **The row split is free.** The equality theorem of the paper asks only
   that the row pairs of the doubles form a complete bipartite graph with
   balanced parts. Every construction in the threshold program takes odd
   rows against even rows. With another split the rival pairs and the
   right angles obey other arithmetic. I did not find a split with a
   better structure, and a split in which both parts carry a 2-adic rule
   is impossible, because all pairs occur. Low rows against high rows
   lose the parity arguments and gain nothing that I could see.
2. **Regions.** Every obstruction lies in `2 W_h + 1` consecutive columns
   (Section 5 of the paper). So a bounded number of regions separated by
   gaps of `h^2/2` columns do not interact. This allows a main region and
   a region for exceptional labels. It does not help by itself: in every
   scheme above the exceptional labels are too many for the method of the
   paper, which costs `tau*(h)^2` columns for each label.

## 7. Where I am stuck

1. A bound for the chromatic number of `G_T`, or for the number of arc
   classes, that beats `|D_T| + 1` when `|D_T|` is much larger than
   `log h`.
2. A rule that removes the angles of Corollary 2 for offsets with many
   divisors and still leaves each label a polynomial number of positions.
3. The sea, as in the notes of 11 and 12 November. Nothing here touches
   it.

## 8. Files

- `check_partial_rule.py`: the test of Lemma 1. Run
  `py check_partial_rule.py 24 12`. It takes a few minutes.
