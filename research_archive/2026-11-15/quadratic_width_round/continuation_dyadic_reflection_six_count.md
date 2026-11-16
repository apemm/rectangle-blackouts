# Exact dyadic-reflection six-point resonances have few hubs

15 November 2026. The most direct Hilbert reflection resonance is a
small part of the long same-parity parked-six family. Its expected count
in the folded, capped, bounded-permutation candidate union is
\[
 O_{k,M}(hK^2\log^2(2h))
 \tag{1}
\]
for support span at least \(h^2/K\), when \(K\) is bounded by a fixed
power of \(\log h\). This is a count of a specifically defined resonance
subfamily. It is not a bound for arbitrary same-parity six-point supports.

## 1. Define the subfamily before using the symmetry

Use the spacing-four refinement of a padded Hilbert traversal of side
\(N=\Theta(h)\). Its fixed refinement factor is \(M\), and its
coarse genuine-object permutation blocks have fixed size \(k\).
The candidate value at fine rank \(t\) comes from one of a bounded
number of original coarse ranks \(v\) with
\[
 |v-\lfloor t/M\rfloor|\le k-1,
 \tag{2}
\]
followed by a bounded index displacement, a possible cap ancestor, and
one branch of the folding map. The constants below may depend on these
fixed choices.

Consider two parked triangles of one physical row parity. Let their
completion-end core ranks be \(r,r+t\), their other core ranks be
\(p_1,p_2\), and their signed sea offsets be \(\xi_1,\xi_2\).
Their common completion implies
\[
 \xi_1-\xi_2=4t.
\]
Restrict to the subfamily
\[
 \xi_2=-\xi_1\ne0,
 \qquad y(r+t)=y(r).
 \tag{3}
\]
The partner rows are then equal as well. The two parked-triangle equations
give the exact reflection identity
\[
 p_1+p_2=2r+t.
 \tag{4}
\]

Call such a candidate *dyadically reflected* if a choice of its two
original coarse partner ranks \(v_1,v_2\), satisfying (2), belongs to
one aligned Hilbert sub-square rank block \([a,a+B-1]\) and satisfies
\[
 v_1+v_2=2a+B-1.
 \tag{5}
\]
Here \(B\) is a power of four. We may overcount all such blocks and
all candidate-rank choices. We do not require that the relevant Hilbert
orientation actually preserves the coordinate under this reversal.
Any genuine symmetry realization is therefore included.

## 2. Long span leaves only O(K squared) possible hubs

Put \(H=h^2/K\). Assume the full six-point support span is at least
\(H\). In (3), the two core side lengths have equal absolute horizontal
component, since their partner rows and vertical increments agree.
The remaining offsets are bounded by
\[
 |\xi_i|\le CK,
 \qquad |t|\le CK,
 \tag{6}
\]
using the long-support anchor estimate. Consequently the two partner
positions are separated by at least \(cH\) for sufficiently large \(h\).
Equations (2) and (5) force
\[
 B\ge cH/M-C_{k,M}.
\]
The total number of aligned Hilbert blocks at all such scales is
\[
 O(N^2/H)=O(K).
 \tag{7}
\]
This follows by summing the geometric series \(N^2/B\) over the
eligible powers of four.

For each block and each \(\xi_1\), equations (2), (4), and (5) give
\[
 \big|2r+t-M(2a+B-1)\big|\le C_{k,M}.
 \tag{8}
\]
Thus there are only \(O_{k,M}(1)\) possible first hub ranks. There are
\(O(K)\) choices of \(\xi_1\) in (6), and (3) fixes \(\xi_2\)
and \(t\). The total number of hub/offset configurations is therefore
\(O_{k,M}(K^2)\).

For each, the first partner has \(O(h^2)\) possible fine positions;
(4) fixes the second. This bounds the number of positional candidates
by \(O_{k,M}(h^2K^2)\), before imposing any row or congruence tests.

## 3. A long triangle fixes the common row offset

Fix a positional candidate and the first triangle. Each of its two
row values belongs to \(O_{k,M}(\log h)\) possible folded raw/cap
branches. On a branch, its physical row is either
\[
 c+4U,\qquad c-4U,
 \quad\text{or}\quad b_*+e,
 \tag{9}
\]
where \(U\) is the offset of the shared parity, \(b_*\) is its one
fixed folded anchor, and \(e\) lies in a fixed bounded set.
This enumeration does not condition on which cap is eventually selected.

Writing the partner and hub rows as \(A(U),C(U)\), the triangle equation is
\[
 X\xi=(C(U)-A(U))(A(U)-s).
 \tag{10}
\]
The right side is a polynomial of degree at most two. If at least one
branch is affine, it is nonconstant unless the vertical increment is
identically zero, which does not define a parked triangle. Indeed:

* Equal nonzero slopes make the increment a nonzero constant and leave
  a nonzero linear coefficient.
* Opposite nonzero slopes, or an affine partner and a constant hub,
  give a nonzero quadratic coefficient.
* A constant partner and an affine hub give a nonzero linear coefficient,
  since the fixed partner row is distinct from the sea row.

If both branches are constant, their difference is bounded by a fixed
constant. That case cannot contribute here. The common side span is
\(\Omega(H)\), and (10), with \(|A(U)-s|<h\), gives
\[
 |C(U)-A(U)|\ge cH/h=ch/K.
\]
This tends to infinity for the stated polylogarithmic range of \(K\).
The use of a single fixed folded anchor per parity is important in
this argument; two unrelated fixed boundary values would not suffice.

Each branch pair therefore fixes at most two offset values. The offset
is uniform on an interval of \(\Theta(h)\) integers. A union over the
\(O_{k,M}(\log^2h)\) branch pairs gives probability at most
\(C_{k,M}\log^2h/h\). Any second-triangle test, cap-selection test,
or goodness requirement can only remove candidates. Combining with
Section 2 proves (1).

## 4. What remains in the affine-row correlation problem

The result controls exact reversal copies of aligned Hilbert sub-squares,
even after the stated bounded shifts and cap-candidate union. It does not
assert that every large row-section reflection arises this way. Reflections
about other rank centers, unequal sea-offset magnitudes, and the correction
term produced by unequal hub rows remain in the general affine correlation
problem of
[the raw reduction](continuation_same_parity_raw_6pt_reduction.md).

The estimate is an expectation over unconditioned row offsets. It can be
included in a joint nonnegative-objective selection, but it does not apply
after arbitrary conditioning on a chosen offset or residual configuration.
It also does not by itself supply an occupancy-preserving deletion rule.

Independent review: the complete written count passed a separate review
of the reflection identity, long-span block count, bounded rank errors,
all folded polynomial cases, and the constant-branch exclusion.
