# Three fixed Pythagorean directions can force a private-slot cycle

15 November 2026. A fixed direction palette does constrain short directed
cycles: their reciprocal slopes must sum to zero after the large own-gap
cutoff. But a three-direction resonance exists. It gives an explicit
three-object private-slot obstruction with distinct row pairs, no reverse
P edges, and linear-size P gaps and half-factors.

This is an arithmetic placement, not an actual Hilbert or folded-cap
embedding. Survival of the good-row filters and the other supports added
by a full filling is not asserted.

## 1. Short cycles require an exact reciprocal resonance

Fix a finite set of nonzero Pythagorean slopes, independent of height,
and a fixed cycle length bound \(k\). Suppose a directed P cycle uses
slopes \(\mu_1,\ldots,\mu_j\), \(j\le k\). Each edge is an
actual in-strip candidate, so its horizontal span is \(O(h)\).
Total same-parity square-root locality therefore puts every row in the
cycle within \(O_k(\sqrt h)\) of the corresponding parity row at its
first vertex. If that vertex's own gap is \(d\), then
\[
 b_{i+1}-a_i=d+O_k(\sqrt h).
\]
Summing the horizontal increments around the cycle gives
\[
 0=d\sum_{i=1}^j\frac1{\mu_i}+O_k(\sqrt h).              \tag{1}
\]
Assume \(|d|\ge B_h\) with \(B_h/\sqrt h\to\infty\).
There are only finitely many reciprocal sums of at most \(k\) members
of the fixed palette. Their nonzero magnitudes have a positive minimum.
Thus, for all sufficiently large heights, (1) forces
\[
 \sum_{i=1}^j\frac1{\mu_i}=0.                            \tag{2}
\]

For a two-cycle this says that the slopes are opposite. The two horizontal
spans are equal, so their absolute vertical increments and hypotenuses
are equal too. Consequently the equal-height template estimate applies
to every sufficiently large two-cycle within a fixed direction palette.
It does not apply uniformly to a palette whose directions vary with \(h\).

## 2. An explicit three-direction resonance

The integer triples
\[
 (624,715,949),\qquad(1428,715,1597),\qquad
 (2052,715,2173)                                         \tag{3}
\]
are Pythagorean, and \(624+1428=2052\). Hence the three distinct
signed slopes
\[
 \frac{715}{624},\quad\frac{715}{1428},\quad
 -\frac{715}{2052}
\]
satisfy (2). The first fraction reduces to \(55/48\); all three
are legitimate primitive Pythagorean directions after reduction.

Take an integer \(t\equiv1\pmod4\), \(t\ge33\), and set
\[
 h=4000t,\qquad a=2000t+3.
\]
Place three row-pair objects at columns \(0,624t,2052t\), with rows
\[
\begin{array}{c|cc}
 i&a_i&b_i\\\hline
 0&a&a+715t+8\\
 1&a+4&a+715t\\
 2&a+8&a+715t+4.
\end{array}                                             \tag{4}
\]
The odd rows are \(3\pmod4\), exceed \(h/2\), and the even rows
are \(2\pmod4\). These are the row restrictions of the low constant
sea \(L=1\). The three row pairs are distinct.

The edges \(0\to1\), \(1\to2\), \(2\to0\) each have positive
vertical increment \(715t\) and the horizontal spans from (3), scaled
by \(t\). Their vertical alternative endpoint rows are respectively
\[
 (1883t+3,2832t+3),\quad
 (1559t+7,3156t+7),\quad
 (1271t+11,3444t+11).                                    \tag{5}
\]
All lie in the strip. Their half-factors are \(117t,441t,729t\),
and the spacing-four slot gaps are \(156t,357t,513t\).
Thus both scales are \(\Theta(h)\), as are the objects' own gaps.
These particular edges are not removed solely by the numerical
\(h^{1-o(1)}\) cutoffs.

No reverse edge is Pythagorean for \(t\ge33\). Its vertical increment
is \(715t+\delta\), where \(\delta=4,-8,4\), respectively.
If its integer hypotenuse were \(zt+f\), norm Lipschitz continuity
would give \(|f|\le|\delta|\). Subtracting its forward norm gives
\[
 2t(zf-715\delta)=\delta^2-f^2.                          \tag{6}
\]
For \((z,\delta)=(949,4),(1597,-8),(2173,4)\),
\(zf=715\delta\) has no integer solution. The left coefficient
is therefore a nonzero integer, while the right side has absolute value
at most 64. Equation (6) would force \(t\le32\).

The same-parity row differences are at most eight. Their horizontal
distances are at least \(624t\), so they satisfy the strict strong
locality inequality \((\Delta y)^2<2|\Delta x|\).

## 3. Every private offset is blocked

Fix any odd private palette size \(M\), and choose
\(t=M n\equiv1\pmod4\), arbitrarily large. Put the three objects
at coarse ranks
\[
 r_0=0,\qquad r_1=156n,\qquad r_2=513n,
\]
with private columns \(4(Mr_i+j)\), \(0\le j<M\).
At each of these private slots allow a nonempty subset of its object's
two rows from (4). Require every object to have a double at some offset.

At every common offset \(j\), the three P edges of Section 2 remain
unchanged: the common shift \(4j\) cancels. If object 0 is double
at that offset, edge \(0\to1\) forces object 1 to be odd-only.
Then \(1\to2\) forces object 2 to be odd-only, and \(2\to0\)
contradicts the even point at object 0. The same argument starts at either
other object. No object can be double at any private offset.

Hence no such fully occupied own-row private filling exists, even though
the directed system has no two-cycle. This conclusion concerns these
P exclusions. When using them as genuine rectangle obstructions, their
opposite-parity owners from (5) must be present with the usual owner
conditions. They can be supplied outside the three blocks. No claim is
made that the original three objects occur at these ranks in Hilbert order.

For large \(t\) relative to the fixed \(M\), the full collection
of private options still has same-parity row displacement at most eight
between different objects and zero within one object. The same strong
locality bound therefore holds for those options. The construction is
stated for odd \(M\); it does not refute every even private palette or
an arbitrary relocation/reordering scheme.

## 4. Exact higher-support check and its restricted scope

The companion checker enumerates all triples and all side/diagonal pairings
of the six protected points in (4), at one common offset. Every dot
product and mixed equation is a polynomial of degree at most two in
\(t\). It computes all positive integer roots exactly.

There is no right-angle triple among those six points for any positive
integer \(t\), and no nondegenerate mixed four-support among them.
Thus the protected cycle is not automatically removed by the inserted
three- or four-point tests on those six points alone. This statement does
not cover triangles or mixed supports involving other private copies,
the sea, owners, or additional filler points. Those larger families, and
good-row membership, were not checked.

Files: [check_three_direction_p_cycle.py](check_three_direction_p_cycle.py)
and [its exact output](check_three_direction_p_cycle.json). The checker
also verifies the three norms, in-strip corners, and absent reverse norms
at five scales. The cycle argument and reverse-edge bound are the
analytical proofs above; the higher-support statement is the finite exact
polynomial certificate just described.

## Review status

The full written proof passed an independent review, including the norms,
in-strip corners, residue conditions, reverse-edge bound, and common-offset
propagation. The reviewer also reran the exact polynomial audit independently;
both root lists were empty. The stated embedding and extra-point limitations
remain essential.
