# Subquadratic P incidence at the exceptional odd stubs

15 November 2026. In the random good-cap construction, offsets can be
chosen so that the total number of possible actual P constraints whose odd
source is an exceptional odd-only stub is
\[
 O\!\left(hb\,\mathcal D_h\log^2(2h)
       +h^{3/2}\sqrt{b+1}\,\mathcal D_h\log(2h)\right),
 \tag{1}
\]
where \(b\) is the total bad-row count and
\(\mathcal D_h=\max_{1\le n\le h}\tau(n^2)=h^{o(1)}\).
The same offsets have cap area \(O(hb\log(2h))\).
With the improved R2s input \(b=h^{5/6+o(1)}\), (1) is
\(h^{23/12+o(1)}=o(h^2)\).

This is an incidence theorem, not an unconditional repair. A P edge
between an odd singleton and an even singleton cannot be removed by
erasing one endpoint while keeping both slots occupied. Section 6 states
the exact conditional repair that the count does support.

## 1. Setting and the finite candidate family

Use
[`continuation_random_good_caps.md`](continuation_random_good_caps.md),
with the even preference at noncap nondouble ranks. The two genuine row
classes are complete residue classes of a fixed even modulus \(D\),
restricted to the height-\(h\) strip. Their sizes and the padded Hilbert
side \(N\) are \(\Theta(h)\), with constants depending on \(D\).
Their independent offsets \(U_0,U_1\) range over intervals of
\(\Theta(h)\) integers.

The good row sets are fixed before these offsets. Let \(J\) be the
odd-only singleton ranks created by padding, row filtering, or selected
caps. Later odd erasure at a genuine double creates an even stub and
does not enlarge \(J\).

A candidate counted here consists of an odd black source, an even black
endpoint in another slot, and an integral alternate vertical diagonal
whose two endpoints lie in the strip. The actual axis-owner test can only
remove candidates. Write its horizontal distance \(X=S q\), vertical
magnitude \(Y\), and hypotenuse \(L\). Then
\[
 X^2+Y^2=L^2,\qquad 0<X\le L\le h-1.
 \tag{2}
\]
For a fixed \(X\), there are at most \(\tau(X^2)\) possible positive
\((Y,L)\), by factoring \((L-Y)(L+Y)=X^2\).

At any fixed rank, the possible unclamped coordinate of a surviving point
is either its original Hilbert coordinate or the cap coordinate of one of
its dyadic ancestors. There are \(O(\log(2h))\) such deterministic
coordinates. Selection of the caps is not conditioned on below; instead
we union over these possibilities and the necessary bad-child witnesses.

## 2. Two unclamped endpoints

For any fixed choices of unclamped odd and even coordinates, the signed
physical row difference has the form
\[
 c+D(U_0-U_1),
 \tag{3}
\]
where \(c\) is deterministic. A norm solution in (2) therefore fixes
\(U_0-U_1\) to one value, or is impossible.

An odd-only noncap source requires that its original clipped even
coordinate be bad. Thus one offset, \(U_1\), belongs to a deterministic
set of at most \(b\) values. Combining this condition with (3) leaves
at most \(O(b\mathcal D_h)\) offset pairs for fixed ranks and a fixed
possible even cap coordinate. The probability is
\(O(b\mathcal D_h/h^2)\).

For an odd-cap source, fix its selected node \(Q\). It has a bad-cap
child. Union over the four children and their predetermined cap axes.
Badness again places one of \(U_0,U_1\) in a set of at most \(b\)
values. Equation (3) fixes the other offset, with the same probability
bound. This remains true whichever axis the bad child uses.

At each depth, the potential source intervals partition the \(N^2\)
ranks. There are \(O(h)\) possible signed horizontal gaps in (2).
Summing over depths, the partner's possible cap coordinates, and all
source ranks gives
\[
 \mathbb E I_{\rm uu}
 \le C hb\mathcal D_h\log^2(2h).
 \tag{4}
\]
All selection and occupancy conditions that were omitted only reduce
the actual family. No independence of the cap choices is asserted.

## 3. One clamped endpoint

Let \(B\) be the maximum distance of the four first/last good physical
rows from their corresponding strip edge, plus one. Since the genuine
row classes are complete residue classes and only \(b\) rows are bad,
\[
 B\le C_D(b+1).
 \tag{5}
\]

If one endpoint of an actual P has physical row \(a\) near the bottom
edge, the lower alternate vertical corner gives
\(L\le a+y-2\). Consequently its smaller half-factor obeys
\[
 \frac{L-|y-a|}{2}\le\min(a,y)-1\le a-1.
\]
Reflection gives the corresponding statement at the top edge. Therefore
an actual P touching a clamped boundary row satisfies
\[
 q\le C_S\sqrt{Bh}.
 \tag{6}
\]

Suppose exactly one endpoint has a clamped boundary value. There are only
two boundary values for its parity. At the other endpoint, enumerate its
\(O(\log(2h))\) possible raw or cap coordinates. Each norm value \(Y\)
fixes that endpoint's own offset to at most one value, with either sign
allowed. Thus, for fixed ranks and horizontal gap, the probability is
\[
 O(\mathcal D_h\log(2h)/h).
 \tag{7}
\]
This bound ignores all bad-row and cap-selection conditions, so it does
not rely on a second independent bad-row probability. That is essential
when the bad-child witness uses the same offset as the unclamped endpoint.

There are \(O(h^2)\) source ranks and, by (6),
\(O(\sqrt{Bh})\) possible partner gaps. Hence even counting all such
one-clamped P candidates, rather than only those with source in \(J\),
gives
\[
 \mathbb E I_{\rm one}
 \le C h^{3/2}\sqrt{b+1}\mathcal D_h\log(2h).
 \tag{8}
\]
The in-strip alternate-corner condition is used in (6). The larger
out-of-strip candidate graph is not covered by (8).

## 4. Two clamped endpoints and simultaneous offset selection

When both endpoints are clamped, their two physical rows are one of four
fixed pairs. For each pair, factoring
\((L-X)(L+X)=Y^2\) gives \(O(\mathcal D_h)\) possible horizontal
gaps. Thus, deterministically,
\[
 I_{\rm cc}\le C|J|\mathcal D_h.
 \tag{9}
\]
The cap argument gives \(\mathbb E|J|=O(hb\log(2h))\).
Combining (4), (8), and (9) proves the expected bound (1).

The selected cap area also has expectation \(O(hb\log(2h))\).
Apply Markov's inequality to the two normalized nonnegative costs and
choose offsets where both are at most a fixed multiple of their
respective bounds. If \(b=0\), the exceptional source set is empty.
This joint selection is required: minimizing cap area alone need not
give the incidence estimate.

Using
[`continuation_r2s_small_u_refinement.md`](continuation_r2s_small_u_refinement.md),
the first term of (1) is \(h^{11/6+o(1)}\) and the second is
\(h^{23/12+o(1)}\). All constants are uniform in the offsets and height
for fixed profile data.

## 5. Fixed block permutations

The same bound holds for the union of candidates over all permutations
within blocks of a fixed size \(k\), after choosing the larger fixed
stride and the weakened R2s locality parameter specified in the cap note.
For a fixed pair of final slots, each originating object has at most
\(k\) possible original ranks. Enumerating these \(O(k^2)\) choices
before the preceding count is a constant-factor change. Each row still
comes from a raw coordinate or a dyadic ancestor of that original rank.
The number of candidate source objects remains \(|J|\).

Thus the chosen offsets control the entire finite constraint union for
these local permutations. The estimate does not require choosing the
permutations first or conditioning on their eventual solution.

## 6. What this count can repair

For every surviving genuine double that appears as the even target of a
counted P from \(J\), erase its even point and relocate its complete pair.
At most the number in (1) of labels are converted, and every slot remains
occupied. This kills every \(J\)-to-double edge, whether or not there
are also edges to fixed even singletons. Such stub-to-stub edges remain.
The operation is pure erasure, so the other positive-support families
inside the core only shrink. The internal relocation cost remains
\(h^{23/12+o(1)}=o(h^2)\) after a subpolynomial relocation factor.

If the genuine doubles had already undergone the uniform own-gap and
factor-band filtering, their new odd-only points keep the corresponding
long-gap property. Their former even mates can be retained as
counterfactual coordinates: the earlier uniform same-parity inequality
against every surviving even point is unchanged by deleting that mate.
The counterfactual mate moves with the same object under a block
permutation. These converted odd sources therefore need not be added to
the unfiltered exceptional source family. Thus all remaining unfiltered
P events are exactly those from an original exceptional odd stub in
\(J\) to an already even-only singleton. If there are no such edges,
the unfiltered P family is completely removed; the long-gap P family and
the other residual constraints still require their separate solution.

There is also an exact general criterion for a prescribed finite target
graph. Include every genuine double incident to that graph in the set to
be converted. Give each converted object a variable \(x_v\in\{0,1\}\),
where 1 means retain its odd point and 0 means retain its even point.
Original odd/even singletons have fixed values 1/0. A directed P edge
from the odd point of \(u\) to the even point of \(v\) is avoided
exactly when
\[
 x_u\le x_v.
 \tag{10}
\]
All these constraints can be satisfied if and only if there is no
directed path from a fixed odd singleton to a fixed even singleton.
Necessity follows by propagating (10). For sufficiency, assign 1 to the
vertices reachable from fixed odd singletons and 0 to every other
unfixed vertex. Relocate each converted full pair externally, subject
to the existing relocation and join hypotheses.

An incidence bound alone does not exclude these forced paths. In
particular, a single direct edge between fixed opposite-parity stubs is
already an obstruction to this erasure-only repair. Establishing that a
useful target graph avoids these paths, or modifying its occupied stubs
while preserving the geometric exclusions, remains open.

Independent review: the complete written proof passed a separate review,
including all three incidence cases, joint offset selection, the constant
block-size union, even erasure at genuine-double targets, the
counterfactual-mate bound, and the exact directed-path criterion. The
remaining fixed-stub obstruction is not assumed absent.
