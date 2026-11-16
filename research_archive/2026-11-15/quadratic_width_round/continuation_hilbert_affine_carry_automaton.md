# Affine row-section correlations from a finite carry automaton

15 November 2026. An exact four-state reverse Hilbert automaton gives
uniform digit losses for several small odd slopes. Slope 5 is a genuine
exception to a uniform worst-row loss, but it still has an averaged loss
over the row input. The estimates below concern raw row sections. Combining
them with the large divisibility progression in the six-point problem is
a separate unresolved step.

The finite arithmetic checks are in
[probe_hilbert_affine_carry.py](probe_hilbert_affine_carry.py), with output
[probe_hilbert_affine_carry.json](probe_hilbert_affine_carry.json).
The recurrence was checked against 2,520 direct finite section counts.
The block bounds are exhaustive integer computations on the stated finite
state space, not numerical spectral estimates.

## 1. Four section states and their exact reversal

Let `N=2^k`. Use the standard Hilbert recursion from the
[raw same-parity reduction](continuation_same_parity_raw_6pt_reduction.md).
There are four row-section states:

`0=X+`, `1=X-`, `2=Y+`, `3=Y-`.

Here `X+` means first coordinate equal to the specified row, and `X-`
means first coordinate equal to its reflection `N-1-row`. The two `Y`
states have the analogous meaning. A forward transition reads the next
row bit and chooses a base-four rank digit. Its output is the child state.

Reversing that table gives the following transitions. An entry `(d,P)`
means rank digit `d` and recovered parent state `P`.

| Child state | Row bit 0 | Row bit 1 |
|---|---|---|
| `X+` | `(1,X+), (0,Y+)` | `(2,X+), (3,Y-)` |
| `X-` | `(2,X-), (3,Y+)` | `(1,X-), (0,Y-)` |
| `Y+` | `(0,X+), (3,X-)` | `(1,Y+), (2,Y+)` |
| `Y-` | `(1,Y-), (2,Y-)` | `(3,X+), (0,X-)` |

Each child state and row bit permit exactly two distinct rank digits.
Thus processing digits from low to high does not introduce an exponential
orientation union. There are four initial leaf states. A complete path
is accepted only if it ends in the prescribed global section state.

## 2. Couple two sections by an arithmetic carry

Fix positive odd integers `a,b` and an integer `c`. Count rank pairs with

`a p - b q = c`.

At one base-four position, let `d1,d2` be the two rank digits, `e` the
digit of `c mod N^2`, and `z` the incoming carry. Then

`z'=(a d1-b d2-e+z)/4`.

The carry always lies in the finite range

`-b <= z <= a-1`.

Indeed, after any number of processed digits it is the corresponding
integer quotient of `a p_low-b q_low-c_low`. The strict bounds on those
three lower parts give this range.

Because `b` is odd, a choice of `d1` fixes `d2 mod4`. The second reverse
section table either accepts that digit or rejects it. A state
`(section1,section2,z)` therefore has at most two successors. There are
`16(a+b)` states. The initial carry is zero. The final carry is
`floor(c/N^2)`, which also handles negative translations exactly.

When the two rows have a common bit, the control is the pair consisting
of that bit and the translation digit `e`. Both are shared by all paths.
The script keeps this requirement. It does not optimize the translation
digit independently along different branches.

The same transition rule remains valid when the two row bits differ.
It still has at most two successors, but the common-bit block estimates
below are asserted only for common row bits.

## 3. Finite block certificates

For each row-bit word of the stated length, the checker enumerates every
translation-digit word and every starting state. It counts all surviving
paths, without imposing a final-state restriction. The exact maxima are:

| Slope `a/b` | Block length | Common row word | Maximum paths |
|---|---:|---|---:|
| `3` | 3 | `000,001,110,111` | 6 |
| `3` | 3 | `010,011,100,101` | 5 |
| `5` | 3 | `000,001,110,111` | 8 |
| `5` | 3 | `010,011,100,101` | 6 |
| `7` | 2 | every word | 3 |
| `5/3` | 2 | every word | 3 |

For example, every three-digit block at slope 3 loses at least two of
the eight potential paths. If both rank sets are sections of the same
row, this gives, uniformly in that row and in `c`,

`I_N(3,1;c) <= 16 * 2^(k mod3) * 6^floor(k/3)`.

Thus the intersection is `O(N^(log_2(6)/3))`, with exponent less than one.
At slopes 7 and `5/3`, the corresponding exponent is `log_2(3)/2`.
The estimate is uniform over both global section states.

The full-branch subset graph also gives a block loss at slopes `7/3`
and `9/5` in length 3, and at slope 9 in length 2. These latter statements
use the weaker certificate that a full binary block is impossible, so
their permitted path bounds are respectively 7 and 3.

If only a consecutive group of `L` row bits is common, apply the loss
inside that group. Every other processed digit contributes at most a
factor of two. Bounded changes to the affine translation do not affect
any of these bounds.

## 4. An exact slope-five resonance

For every `N=2^k`, `k>=1`, let `y=N/2-1`. Then

`#{p in X_N(y): 5p+1 in X_N(y)} = ceil(N/6)`.

Here `X_N` is the actual global first-coordinate section, with no freedom
to change orientations. This proves that a uniform sublinear intersection
bound at slope 5 is false.

To prove the formula, put `N=2n` and `j=log_2(n)`. The section recursion is

`X_(2n)(n-1) = Y_n(n-1) union (n^2 + X_n(n-1))`.

A matched `p` must lie in the first part, and `5p+1` in the second.
Indeed, `p>=n^2` makes its image exceed the full rank range. Conversely,
the minimum element of `Y_n(n-1)` shows that its image cannot lie in
the first part. The case `n=1` is immediate. Therefore count the pairs

`p in Y_n(n-1)`, `q in X_n(n-1)`, `5p-q=n^2-1`.

All `j` row bits and translation digits are respectively 1 and 3.
The complete coaccessible state set is

```
A = (Y+, X+, 0),
B = (Y+, X-, 2),
C = (Y+, Y-, 1).
```

Their transitions are

`A -> A,C`, `B -> B,C`, `C -> A,B`.

The reverse transition table and carry equation show that every
predecessor of these three states under control `(1,3)` lies in the same
set. Only `A` has the initial carry zero and can lead to the required
final state `A`. Thus the count is the `AA` entry of the `j`th power of

```
T = [1 0 1]
    [0 1 1]
    [1 1 0].
```

The eigenvalues are `2,1,-1`, and direct diagonalization gives

`(T^j)_AA = 2^j/3 + 1/2 + (-1)^j/6 = ceil(N/6)`.

This particular row lies in the dyadic boundary tube used by the
boundary reduction. The theorem identifies a real exceptional row, not
an error caused by counting orientations too many times.

## 5. Persistent branching has a restricted row input

The full-branch subset graph at slope 5 has exactly four cyclic strongly
connected components. Each is a single subset with one self-loop. The
controls on those loops are `(row bit, translation digit)` equal to

`(0,0)`, `(0,3)`, `(1,0)`, or `(1,3)`.

The exact state subsets are recorded in the JSON certificate. In
particular, the three-digit table already shows that a change between
the first two row bits, followed by any third bit, prevents full binary
branching. Persistent full branching therefore requires an eventually
constant row-bit input. A constant multiplier can preserve a large row
section, but the row input matters.

For a quantitative consequence, divide the `k` row bits into disjoint
three-bit blocks, read from low to high. Let `J(y)` count blocks whose
first two bits differ. The table gives, uniformly in `c`,

`I_N(y;5,1;c) <= 16 N (3/4)^J(y)`.

This also allows the translation to be chosen separately for every row.
Summing over all row words yields

`sum_(0<=y<N) max_c I_N(y;5,1;c) <= C N^(log_2(56)/3)`.

The exponent is about `1.9358`, strictly below the trivial exponent 2.
For each full block, four words have path bound 8 and four have bound 6,
so their total weight is 56. The at most two remaining bits affect only
the absolute constant. This is a uniform averaged row-section saving,
despite the linear-sized exceptional section from Section 4.

## 6. What this proves for the six-point investigation

In the constant-sea setting, the two sea offsets are congruent modulo
four and neither is divisible by four. Their common 2-adic valuation is
therefore zero or one. After reducing their ratio, both numerator and
denominator are odd, as required by the carry automaton.

A negative rank slope can be made positive by reversing one rank. The
identity

`H_N(N^2-1-r)=(N-1-H_N(r)_x, H_N(r)_y)`

changes only the relevant top coordinate-complement state. Since the
block estimates allow all state pairs, this adds no new orientation cost.
Absolute slope 1 remains a genuine symmetry case.

If every endpoint is an original coarse anchor with physical stride
divisible by 16, the sea-offset difference is divisible by that stride.
For distinct hubs this rules out absolute ratios 1 and 5: their nonzero
differences have 2-adic valuation at most three. This observation does
not apply automatically to fine interpolated endpoints.

The raw six-point target also imposes a large modulus depending on the
row increment. A row-section saving cannot simply be multiplied into
the existing divisor-energy upper bound. The proof still needs a joint
estimate that retains this progression, the hub row, and the affine
partner relation. Arbitrary cap constants and unequal folded branches
are additional cases. No subquadratic bound for the complete same-parity
six-point family follows from this note alone.
