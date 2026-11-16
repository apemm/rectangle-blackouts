# Random offsets permit a near-linear half-factor cutoff

15 November 2026. The occupied good-cap construction admits a stronger
actual-P cleanup than the deterministic row-band count. For any
\(1\le A\le h\), the expected number of actual small-half-factor P
constraints with a retained genuine-double odd source is at most
\[
 \mathbb E I_A\le C h^{3/2}\sqrt A\log^4(2h).
 \tag{1}
\]
The finite union over all permutations inside blocks of a fixed size is
included. Erasing the implicated genuine odd sources preserves occupancy.
With an internal relocation factor \(T(h)^2\), \(T(h)=h^{o(1)}\),
one may take
\[
 A_h=\left\lfloor\frac{\eta h}{T(h)^4\log^{12}(2h)}\right\rfloor
 =h^{1-o(1)}.
 \tag{2}
\]
Combining this with the own-row-gap deletion leaves only actual genuine-
source P events with slot gap \(q\ge h^{1-o(1)}\).

Unlike the earlier uniform band count, this argument concerns actual
in-strip P candidates. It does not eliminate the out-of-strip candidate
graph or the exceptional forced odd-singleton source family.

## 1. Count a finite constraint union before choosing permutations

Use the random offsets and fixed good-row sets from
[`continuation_random_good_caps.md`](continuation_random_good_caps.md).
The two row classes are full residue classes of a fixed modulus in the
height-\(h\) strip, so the padded side and each offset range are
\(\Theta(h)\). Fix the profile, physical stride \(S\), and optional
local permutation block size \(k\), all independent of \(h\).

A retained genuine double is outside the selected caps and has two
original good coordinates. At its original rank \(r\), its odd row is
exactly
\[
 a_0+D(H_N(r)_0-U_0).
 \tag{3}
\]
This affine formula remains exact when its value equals the first or last
good odd row. It is not necessary to treat such a genuine source as a
constant clamped value in the probability calculation.

At a fixed possible even endpoint rank, its row is one of
\(O(\log(2h))\) forms: an original coordinate or a dyadic ancestor's
cap coordinate, shifted by \(U_1\) and clipped. An unclamped form is
affine in \(U_1\); a clamped form is one of two fixed boundary rows.
These possibilities include the full good virtual singleton palette from
[`continuation_virtual_cap_palettes.md`](continuation_virtual_cap_palettes.md).
All validity and cap-selection conditions can be omitted when taking an
upper bound.

For a fixed horizontal gap \(q\), set \(X=S q\). A P norm satisfies
\[
 X^2+Y^2=L^2.
 \tag{4}
\]
There are at most \(\tau(X^2)\) positive norm pairs \((Y,L)\).
Together with (3), each signed norm value fixes either \(U_0-U_1\)
or \(U_0\). Under the independent uniform offset law its probability
is \(O(1/h)\). This reasoning also covers two boundary-valued
endpoints: the source must still satisfy its genuine affine formula (3).

For fixed \(q\), there are \(O(h^2)\) possible source ranks and two
directions. Enumerating the target coordinate forms gives the bound
\[
 C h\tau((S q)^2)\log^2(2h).
 \tag{5}
\]
One logarithm is already sufficient here; the displayed conservative
bound also covers the finite coordinate unions without further notation.
For fixed block permutations, each final slot has at most \(k\)
possible originating ranks. Enumerating both origins changes only the
constant in (5). No independence among the resulting constraints is used.

## 2. Average the elementary divisor bound

If the smaller half-factor \(a=(L-Y)/2\) is at most \(A\), then
\[
 a(Y+a)=(S q/2)^2.
\]
An actual in-strip P has \(Y<h\) and \(L\le h-1\). For
\(A\le h\), every such event therefore has
\[
 q\le C_S\sqrt{Ah}=:Q.
 \tag{6}
\]

Let \(d_3(n)\) count ordered factorizations of \(n\) into three
positive integers. Prime by prime,
\[
 \tau((S q)^2)\le\tau(S^2)\tau(q^2)
 \le C_S d_3(q),
 \tag{7}
\]
because \(2e+1\le\binom{e+2}{2}\) for every \(e\ge0\).
Also,
\[
 \sum_{q\le Q}d_3(q)
 =\sum_{ab\le Q}\left\lfloor\frac Q{ab}\right\rfloor
 \le Q\left(\sum_{a\le Q}\frac1a\right)^2
 \le Q(1+\log Q)^2.
 \tag{8}
\]
Summing (5) over (6) proves (1). No maximal divisor factor or external
divisor-average theorem is required.

## 3. Choose offsets jointly and erase only odd points

Choose the offsets by a joint averaging argument. In addition to \(I_A\),
include the selected cap area and, if desired, the exceptional-stub
incidence cost from
[`continuation_cap_stub_p_incidence.md`](continuation_cap_stub_p_incidence.md).
The sum of their normalized nonnegative costs has bounded expectation.
Thus some offset pair makes each cost at most a fixed multiple of its
displayed bound. Selecting a cap-area minimizer alone is not sufficient.

After these offsets are fixed, form the entire finite candidate union over
the allowed local permutations and good singleton options. Erase the odd
point of every retained genuine double appearing as the odd source of a
candidate counted by \(I_A\), and relocate that complete pair. There
are at most \(I_A\) such labels. Every affected slot keeps its even
point, so good-row membership, full occupancy, same-parity locality, and
FW exclusion survive.

Set \(\Lambda=\log(2h)\) and choose \(A_h\) as in (2). Equations
(1) and (2) give
\[
 I_{A_h}T(h)^2\le C h^2/\Lambda^2=o(h^2).
 \tag{9}
\]
The cited external relocation and join conditions remain necessary. The
estimate concerns their internal label-dependent width cost.

## 4. The residual gap is near-linear

Also erase odd points of genuine doubles with own row gap at most
\[
 B_h=\left\lfloor\frac{\gamma h}{T(h)^2\Lambda^2}\right\rfloor
 \tag{10}
\]
in absolute value. This involves at most \(O(hB_h)\) labels and costs
another \(O(h^2/\Lambda^2)\) internally. This deletion can be included
before the small-factor source marking; either order only removes points.

A surviving actual P with a retained genuine odd source has \(a>A_h\).
Its even mate supplies the uniform same-parity comparison against the
actual even endpoint. Since \(q\le(h-1)/S\),
\[
 Y\ge B_h-C\sqrt h\ge c\frac h{T(h)^2\Lambda^2}.
 \tag{11}
\]
Consequently,
\[
 \begin{aligned}
 a&>\frac{c h}{T(h)^4\Lambda^{12}},\\
 q&=\frac{2\sqrt{a(Y+a)}}S
       \ge\frac{c h}{T(h)^3\Lambda^7}=h^{1-o(1)},\\
 L-X&=\frac{Y^2}{L+X}
       \ge\frac{c h}{T(h)^4\Lambda^4}=h^{1-o(1)}.
 \end{aligned}
 \tag{12}
\]
All constants are fixed-profile constants. The floors are harmless for
sufficiently large \(h\), because \(T(h)=h^{o(1)}\).

As in the earlier genuine-target conversion, the mate can later be erased
while retained as a counterfactual coordinate. The original geometric
inequality still holds against every surviving even point, uniformly
under the allowed object permutations. Thus (12) also holds for a filtered
genuine odd source subsequently converted to an odd singleton.

## 5. Optional singleton odd points and the exact residual scope

The same finite union can restrict optional singleton choices. At a
nondouble slot with both good virtual parities available, forbid its odd
option whenever that option has a small own virtual row gap or appears
as the odd source of an actual P candidate with \(a\le A_h\). Its
good even option remains, so this costs no occupancy and relocates no
additional genuine label. The total virtual even function supplies the
counterfactual-mate inequality. Every remaining optional odd source then
also satisfies (12).

These are further restrictions of the available options. Previously
deliberate erasures remain enforced: an odd point erased from an implicated
genuine source, or an even point erased at a target of \(J\), is not
reopened by treating its former coordinate as an optional choice.

At an intrinsically forced odd singleton, the even virtual option is bad
or unavailable. Its odd point cannot be suppressed by this operation.
Those sources remain in the explicitly bounded exceptional set \(J\),
whose actual P incidence has the separate subquadratic estimate. Erasing
even points at their surviving genuine-double targets gives the earlier
repair, but edges to already even-only singletons remain an obstruction.

The long P constraints in (12), the forced-stub obstruction, and the
higher-arity mixed constraints are all still open. The theorem supplies a
stronger occupied-core reduction, not a complete quadratic-width blackout.

Independent review: the complete written proof passed a separate audit,
including the source formula at clipping endpoints, the coordinate union
before choosing offsets, the summatory divisor bound, all relocation
exponents, joint offset selection, and monotone optional-point pruning.
The elementary average-divisor improvement was also independently derived.
