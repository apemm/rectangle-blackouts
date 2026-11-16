# A seam-safe adjacent-row replacement for odd singleton intervals

15 November 2026. An odd singleton at row \(a\) can sometimes be
replaced by the even singleton at row \(a-1\). The replacement
creates no P edge to any surviving odd point. Its even-row geometry
is controlled by an explicit existing guard. No new columns or
double labels are required.

For a whole constant odd-only interval, the same move fills a
central subinterval using its two existing even boundary anchors.
It does not require a new guard of height-squared width outside
that interval. The hypotheses are quantitative and can fail when
the odd common row is far from both even boundary rows.

## 1. Fine-grid hypotheses

Index arithmetic columns by \(r\), with physical column \(4r\).
Let \(O,E\) be the old occupied odd and even rank sets, with physical
row functions \(a_r,b_r\). Assume their separate additive bounds
\[
 |a_r-a_s|^2\le |r-s|+16,\qquad
 |b_r-b_s|^2\le |r-s|+16.                            \tag{1}
\]
These are the physical-row versions of the slow fine-menu estimate.
The old same-parity sets also retain the isolated-seam geometry
proved in
[the fine multi-anchor construction](continuation_fine_multi_anchor_compatibility.md).

Consider a set \(J\subset O\setminus E\) of odd singleton ranks.
Require the following short-range agreement:
\[
 a_s=a_r
 \quad\text{whenever }r\in J,\ s\in O,\ 0<|r-s|\le3. \tag{2}
\]
This is a local row condition, not a P test. In a constant odd-only
interval it holds at every rank at least four steps from the ends.
It also excludes the old isolated unit seams that can otherwise
produce a \(3\)-\(4\)-\(5\) P edge after this replacement.

At each \(r\in J\), replace the old odd singleton by
\[
                            (4r,a_r-1).             \tag{3}
\]
Require \(a_r-1\) to be in the strip, in the allowed even residue
class, and literally R2s-good. For the odd-\(3\bmod4\),
even-\(2\bmod4\) profile the residue condition is automatic.
Literal goodness of \(a_r\) alone does not imply goodness of
\(a_r-1\).

## 2. No P edge is created by a new even point

Fix \(r\in J\) and any surviving odd point at rank \(s\ne r\).
Put \(q=|r-s|\). If \(q\le3\), (2) makes their vertical difference
exactly one. If \(q\ge4\), (1) gives
\[
 \bigl|a_s-(a_r-1)\bigr|^2
       \le \bigl(\sqrt{q+16}+1\bigr)^2
       \le8q.                                      \tag{4}
\]
The last inequality holds at \(q=4\), and its right-minus-left
derivative is positive thereafter.

Their horizontal distance is \(X=4q\). Thus the vertical square
is at most \(2X\), strictly below the gap
\((X+1)^2-X^2=2X+1\). The distance cannot be an integer, so this
pair is not a P source pair. At rank \(r\), the old odd point has
been removed, so there is no vertical pair there.

This applies simultaneously to all ranks in \(J\). New points
are all even, and their mutual vertical differences are unchanged
from the corresponding old odd points. In particular, for
\(q\le3\) these differences vanish, and for \(q\ge4\) they satisfy
the same-parity norm gap.

Every old P edge whose odd source was in \(J\) is destroyed, and
no new P edge is introduced. This conclusion concerns P itself
and does not require a bound on the number or directions of its
old incident edges.

## 3. A nearest-anchor condition for even geometry

Suppose \(E\ne\varnothing\). For each \(r\in J\), choose a nearest
old even rank \(s_0\), and put
\[
 q_0=|r-s_0|,\qquad g=|a_r-1-b_{s_0}|.
\]
A sufficient condition is
\[
                         q_0\ge\max\{16,4g^2\}.    \tag{5}
\]
For any old even rank \(s\), let \(q=|r-s|\ge q_0\). Equation (1)
gives
\[
 \begin{aligned}
 |a_r-1-b_s|
 &\le g+\sqrt{|s-s_0|+16}\\
 &\le {1\over2}\sqrt q+\sqrt{q+q_0+16}\\
 &\le (1/2+\sqrt3)\sqrt q.
 \end{aligned}
\]
The square of the final constant is less than eight. Thus every
new/old even pair has vertical square strictly below \(8q=2X\).
The same-parity horizontal cone condition follows as well.

All new/new even comparisons were already handled in Section 2.
Old/old comparisons are unchanged. Hence the replacement preserves
the norm-gap and cone inputs used to exclude nonhorizontal
same-parity integral distances and their geometric support
families. This argument does not assert that the enlarged even
function still satisfies the original numerical bound (1).

If there are no old even points, no old/new even check is needed.

## 4. Fill the middle of an existing odd-only interval

Here is a coupled version with explicit bounds. Suppose \(u<v\)
are consecutive old even ranks, with rows \(B_0,B_1\), and every
rank \(u<r<v\) has only the odd point at the same row \(A\).
Let \(B=A-1\), and require it to be an allowed literal-good even row.
Set
\[
 g_i=|B-B_i|,\qquad
 L_i=\left\lceil {g_i^2\over4}+4\right\rceil
 \quad (i=0,1).                                    \tag{6}
\]
Replace every odd singleton in
\[
              J=[u+L_0,v-L_1]\cap\mathbb Z           \tag{7}
\]
by the even singleton at row \(B\), if this interval is nonempty.

Equation (2) is automatic because \(L_i\ge4\). For an old even
point at rank \(s\le u\), put \(z=u-s\). Then
\[
 \begin{aligned}
 |B-b_s|^2
 &\le \bigl(g_0+\sqrt{z+16}\bigr)^2\\
 &\le2g_0^2+2z+32\\
 &\le8L_0+8z
 \le8(r-s).
 \end{aligned}                                    \tag{8}
\]
The right side is \(2X\), still strictly below the next square.
The argument for \(s\ge v\) is identical. There are no old even
points between \(u,v\). New even points have equal rows. Thus
(7) is an explicit simultaneous P repair with valid even geometry.

The number of odd singleton ranks left in this interval is at most
\[
                         L_0+L_1-2.                \tag{9}
\]
No new physical width is used. A one-sided tail has the same
conclusion using only its existing even boundary anchor.

If \(B\) lies between \(B_0,B_1\), then
\[
             g_0+g_1=|B_1-B_0|,\qquad
             g_0^2+g_1^2\le|B_1-B_0|^2.
\]
This can make (7) substantial inside a long facing-anchor gap.
There is no unconditional fraction bound. In an actual cap the
odd common row and even boundary rows can differ by order \(h\);
then \(L_0+L_1\) can exceed the whole existing interval.

Repeating the same shadow value does not automatically remove the
remaining end intervals. Their row discrepancy with the unchanged
outer even anchor is still present.

## 5. Existing flat plateaus permit long-P repair

The preceding guards are too strong for the principal long-P
problem. Under (5), the old odd point already has nonintegral
distance to every old even point: adding one to the preceding
bound gives
\[
 |a_r-b_s|\le(3/4+\sqrt3)\sqrt q<\sqrt{8q}.
\]
For the interval rule (6), Cauchy instead gives
\[
 |A-b_s|\le\sqrt{5(q+12)}+1.
\]
Its square is at most \(8q\) for \(q\ge30\). Thus that interval
rule can only destroy old P edges of physical horizontal length
at most \(116\).

The actual fine cap menu has more structure: long constant
plateaus immediately outside each odd-only bridge gap. They
permit a weaker guard.

Assume the setting of Section 4. For each \(i=0,1\), suppose the
old even row is constantly \(B_i\) on the outward interval of
length \(R_i\) from its endpoint. Include an old even point at
the far end of that plateau. Define
\[
 L_i=\max\left\{4,\left\lceil {g_i^2\over8}\right\rceil\right\},
 \qquad R_i\ge L_i+4.                                \tag{10}
\]
Replace the same central interval (7), using these smaller \(L_i\).

For an old even point on the left plateau, its row difference
from the new value is \(g_0\), and
\[
                        g_0^2\le8L_0\le8(r-s).
\]
For an old even point a further \(z\) ranks beyond that plateau,
compare it with the far plateau endpoint. Equation (1) gives
\[
 \begin{aligned}
 |B-b_s|^2
 &\le(g_0+\sqrt{z+16})^2\\
 &\le2g_0^2+2z+32\\
 &\le8(L_0+R_0+z)
 \le8(r-s).
 \end{aligned}                                      \tag{11}
\]
The right side is again \(2X\). The right plateau has the same
proof. Section 2 still excludes every new P edge. Thus (10)
gives a simultaneous occupancy-preserving P repair with the same
row and label requirements.

### Transfer to an aligned facing-anchor bridge

In the saved fine menu, let two even endpoint rows have physical
gap \(g_*=|B_1-B_0|>0\). With \(\epsilon_0=1/64\) and physical
row step four, its odd-only gap has endpoint distance
\[
                         v-u=g_*^2.
\]
Each adjacent constant plateau has length at least \(g_*^2\).
Choose the even option on these offered plateaus, as under the
even-preference filling.

If the literal-good shadow row \(B=A-1\) lies between \(B_0,B_1\),
then \(g_0,g_1\le g_*\). Since \(g_*\ge4\), both plateau inequalities
in (10) hold automatically. Also
\[
 L_0+L_1\le{g_0^2+g_1^2\over8}+10
               \le{g_*^2\over8}+10.
\]
The move therefore converts at least
\[
                       {7\over8}g_*^2-9            \tag{12}
\]
ranks of this particular gap, leaving at most
\(g_*^2/8+8\) odd singleton ranks. These are per-bridge bounds
under the actual physical bracketing condition. They do not
give a proportion of all caps or all forced singleton sources.

The bracketing is additional information. Independent odd and
even row origins can place the common odd row far outside the
even endpoint interval. Literal goodness of the shadow row must
also be checked. It is not enough that the odd common row is good.

### A genuine long norm edge allowed by the weaker guard

The rule is not restricted to already-safe old points. Let
\(k\ge2\), choose an odd row \(A\equiv3\pmod4\), and put
\[
 B=A-1,\qquad B_0=A-4k-1,\qquad B_1=A+4k-1.
\]
Take the even boundary rank \(u=0\), a gap of endpoint distance
\(64k^2\), and constant outward plateaus of that length.
The new guard starts at \(L_0=2k^2\). At rank
\[
                         r=2k^2+k
\]
the old odd point and the left even boundary point have
\[
 X=8k^2+4k,\qquad Y=4k+1,\qquad
 \sqrt{X^2+Y^2}=X+1.                                \tag{13}
\]
The smaller half-factor is \(4k^2\). This old P norm edge lies
inside the repaired interval and is destroyed by the shadow
replacement. Taking \(k\) proportional to \(\sqrt h\), with a
small fixed proportionality constant, makes its horizontal
length and half-factor both of order \(h\).

The common white rows for the corresponding vertical-axis rival
are \(A+4k^2\) and \(B_0-4k^2\). Choosing \(A\) in a fixed central
upper-half interval keeps these rows in the strip. If the required
axis owner is present, as in the complete row-pair family, the
norm edge gives the actual P collision. The midpoint lies inside
the odd-only gap and has row \(A\), or is a sea column, so neither
common white row is black there.

At sufficiently large height, a finite list of these shifted rows
can all be chosen literal-good whenever each relevant bad-row set
has cardinality \(o(h)\). Avoid the finitely many translated bad
sets while choosing \(A\) in an interval of length proportional
to \(h\).

This example verifies the local geometry and nonvacuity of the
repair. It is not an asserted embedding of this bridge into a
particular sampled Hilbert cap.

## 6. Accounting, provenance, and remaining supports

Only singleton columns are changed. Every arithmetic column stays
occupied, the black-point count is unchanged, and every genuine
double label is retained. The complete labels previously moved
out of these singleton slots remain in their existing locations.
The operation adds no double label or repeated row pair.

With the literal-goodness check and the profile restrictions,
the old constant-sea occupancy and same-parity geometric sieves
remain available. P edges are handled by Section 2 directly.

The other residual mixed and parked-six families require their
own checks. In particular, the new even value \(a_r-1\) inherits
an odd-field origin. One must not apply an old two-independent-
parity sampling argument to it merely because its physical row
is even. A finite raw-face origin menu remains finite after this
shift, but that fact alone does not preserve the original joint
probability estimates.

This is a constructive guarded replacement, not an all-cap repair
or a substitute for controlling the remaining collision families.

The complete saved proof passed independent written review. A separate
review checked the weaker flat-plateau guard, the exact facing-bridge
count, the long-P identity and common white cells, and the scope of
the good-row choice and sampling limitation.

