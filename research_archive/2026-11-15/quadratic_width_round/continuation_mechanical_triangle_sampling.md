# Two-parameter sampling for a parked triangle

15 November 2026. A continuous mechanical stretch and an independent
integer index offset give a uniform two-parameter probability bound for
a prescribed parked triangle. The bound applies to any two prescribed
nonconstant fold branches, including central cap-coordinate candidates.
Fixed physical anchors are excluded.

## 1. Sampling law and physical fold formulas

Fix a physical residue-row interval

`rho + D j`, for `0 <= j < H`,

where `D` is fixed and `H=Theta(h)`. Sample `theta` uniformly from
`[1/3,2/3]`. Choose either of the two complementary occurrence lists
of the mechanical word, and insert a fixed number of prescribed anchor
indices when needed, as in
[the anchor-insertion note](continuation_mechanical_anchor_insertion.md).
Write the resulting increasing list as `p_i(theta)`, of length `n_theta`.
Uniformly in its index and the parameter,

`p_i(theta)=alpha i+O(1)`,

where `3/2 <= alpha <= 3` and alpha has a bounded probability density.
The gaps of the list are at most three. Its endpoint count also gives

`alpha(n_theta-1)=H-1+O(1)`.                         (1)

Indeed the original one-class count is `theta H+O(1)`, or
`(1-theta)H+O(1)` for the complementary class. A bounded number of
insertions changes it by `O(1)`.

Independently sample an integer `U` uniformly from a fixed interval of
length `Theta(h)`. Its range, and the padded Hilbert side, are fixed
using a bound on all possible class lengths. They do not depend on
theta.

Apply the scalar folded-anchor map to `k-U`, then the occurrence list.
On its three nonconstant branches the physical value has the form

`Y(k)=C_b + sigma_b D alpha(k-U)+O(1)`,               (2)

where the branch constants can be chosen independently of theta:

| Branch | sigma_b | C_b |
| --- | ---: | ---: |
| Central | +1 | rho |
| Left reflection | -1 | rho |
| Right reflection | -1 | rho+2D(H-1) |

For the right reflection, substitute its index
`2(n_theta-1)-(k-U)` and use (1). All errors in (2) are bounded by
one fixed constant. Branch-eligibility conditions can be discarded in
an upper bound.

The entire scalar composition, including its fixed anchor plateaus, is
uniformly Lipschitz in the raw index:

`|Y(k_1)-Y(k_2)| <= 3D |k_1-k_2|`.                 (3)

A fixed bounded perturbation of either displayed physical row changes
the right side of (3) by only `O(1)`. This covers the stated finite
candidate unions for bounded local permutations and interpolation.
The originating raw or ancestor indices must be specified before
sampling.

## 2. Two prescribed physical values

Fix deterministic indices `k_1,k_2`, nonconstant branch choices, and
integer target rows `A_1,A_2`. Allow bounded errors in those row targets.
Suppose the two candidate values use the same mechanical class and
the same offset `U`.

Multiplying (2) by its sign and subtracting the two row equations
eliminates the offset:

`D alpha(k_1-k_2)
 = sigma_1(A_1-C_1)-sigma_2(A_2-C_2)+O(1)`.          (4)

If `k_1 != k_2`, this restricts alpha to an interval of length
`O(1/|k_1-k_2|)`. Its probability has the same bound because the
density of alpha is bounded. For each fixed theta, either nonconstant
row equation restricts `U` to `O(1)` integer values: its coefficient
in (2) has absolute value at least `3D/2`. Thus

`Pr(two prescribed rows)
 <= C/[h max(1,|k_1-k_2|)]`.                        (5)

This proof does not treat the bounded errors as independent. The
events are contained in the strip (4), and their conditional offset
fibers have uniformly bounded cardinality. Integrating these fibers
over theta proves (5).

If the prescribed physical difference has magnitude at least `d`,
(3) implies `|k_1-k_2| >= c d` for large `d`. Therefore

`Pr(two prescribed rows with difference >= d) <= C/(h d)`.
                                                               (6)

The conclusion remains valid when the indices are cap endpoint
coordinates of specified dyadic nodes. Those coordinates are fixed
integers. Their selection as actual caps is an additional condition
that can be discarded. No conditioning on cap selection is used.

## 3. Prescribed parked triangles

Fix the two core columns, their horizontal difference `X`, a nonzero
sea offset `xi`, and the sea row `s`. Let `A` be the partner row and
let `delta` be the nonzero hub-minus-partner row difference. The exact
right-angle equation is

`X xi = delta(A-s)`.                                (7)

For a fixed signed divisor `delta` of the nonzero integer `X xi`,
equation (7) prescribes both rows exactly:

`A=s+X xi/delta`, and `A+delta`.                     (8)

If `|delta| >= d`, the nonconstant-branch estimate gives

`Pr(first triangle with this delta) <= C/(h d)`.     (9)

Summing over the signed divisors gives the uniform unconditioned bound

`Pr(first triangle with |delta| >= d)
 <= C tau(|X xi|)/(h d)`.                           (10)

All in-strip, good-row, parity, cap-selection, and genuine-label
conditions can be retained or discarded without enlarging the bound.
The fixed sea row and the candidate coordinate indices must precede
the sampled parameters.

For the long-support regime, `|X|=O(h^2)`, `|xi|<=C K`,
`|delta|>=c h/K`, with `K` polylogarithmic. The elementary divisor
bound then gives

`P_h <= C K h^(-2) max_(n<=C K h^2) tau(n)
      = h^(-2+o(1))`.                               (11)

When a physical-divisor candidate list already fixes delta, use (9),
not (10). No second divisor factor is necessary.

## 4. Consequences and remaining limitations

Equation (11) supplies the probability hypothesis in
[the raw stretched six-point count](continuation_stretched_partner_divisor_count.md)
and [the central-cap extension](continuation_central_cap_six_count.md).
Those notes still need their respective deterministic partner-count
hypotheses. In particular, (5) for unequal fold branches does not by
itself show that physically close partners have nearby raw indices.

If one row is a fixed physical anchor, its equation supplies no stretch
strip. A specified nonconstant other row can then have probability
`Theta(1/h)` throughout a positive-measure set of stretch parameters.
If both are fixed anchors, there may be no probability gain at all.
Consequently fixed anchors cannot be included in (9)--(11) without a
separate counting or geometric argument.

This is a sampling lemma, not a full-board construction theorem.
It does not assign singleton parities, repair implicated supports,
or prove the remaining mixed-family exclusions.

Independent review: the full written proof passed a separate review of
the occurrence-list approximation, fixed right-fold intercept, signed
offset elimination, bounded-density strip estimate, conditional offset
fibers, large-increment reduction, and prescribed-divisor improvement.
The fixed-anchor limitation remains part of the theorem's scope.
