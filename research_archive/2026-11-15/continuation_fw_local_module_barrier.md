# FW cuts, local row bands, and an obstruction to translating H7 seas

15 November 2026. This note studies the adaptive-module proposal suggested
by `h7_excursion_transfer.md`. It proves a geometric localization lemma
and identifies an obstruction to applying the existing H7 profile theorem
at the smaller height of an excursion. It does not construct a full board
or rule out a different local background.

Independent review: the two-case modular proof, the finite-run bound,
and the full parity-owner interpretation in Section 4 were checked
separately and passed. The explicit triangle and linear-run bound in
Section 5 were also checked independently and passed.

## 1. Why full arithmetic occupancy removes FW under its sign condition

Write a parked triangle as

\[
 A=(x_e,y),\qquad C=A+(X,\delta),\qquad
 B=A+(\xi,F-y),\qquad W=C+(\xi,F-y),
\]

where \(X\xi=-\delta(F-y)\). An FW event requires that the
\(F\)-point at column \(x_e+\xi\) remain present and that the column
\(x_f+\xi\) be occupied by a label.

Suppose \(y>F\) and \(\delta>0\), as in the original H7 bulk. Then
\(X\xi>0\), so the source column \(x_e+\xi\) lies strictly between
\(x_e\) and \(x_g=x_e+X+\xi\). If the occupied columns form a full
arithmetic interval, both endpoints being occupied imply that \(\xi\)
is a multiple of its step, and hence that the source is occupied too.
This removes that FW event when the substituted labels do not themselves
contain row \(F\). No extra boundary exception is needed under these
sign hypotheses.

This observation does not cover private choices, omitted or relocated
labels, or padding holes.
Those are places where the additive fourth column can be missing. The
positive sign condition must also be checked again in a vertically
translated profile: positivity of \(\delta\) in the original H7 proof
uses its small absolute value of \(F\). This is not a solution of the P
family. Full occupancy can be preserved by permuting labels within
bounded rank blocks, but proving P solvability in that different choice
model remains a separate problem.

## 2. Localization by the black rows

Let all black cells of a support have rows in an integer interval of
diameter \(R\ge1\). The following bounds concern the actual black
support, without assuming that its white corners remain in that interval.

1. **Three black corners of a tilted rectangle:** the full rectangle has
   horizontal span at most \(2R^2\). Indeed, its two perpendicular side
   vectors have nonzero integer horizontal components \(p,q\) and
   vertical components \(u,v\), with \(|u|,|v|\le R\). The three given
   corners determine both side differences, even when the missing corner
   is the right-angle vertex. Thus \(pq=-uv\), and each of \(|p|,|q|\)
   is at most \(R^2\). The fourth row lies within distance \(R\) of the
   given row interval.

2. **Two tilted rectangles sharing their white corner:** if their six
   black corners lie in the interval, their union has horizontal span at
   most \(4R^2\). Apply the preceding bound separately and use their
   common corner.

3. **A genuine mixed four-support with nonvertical black side:** its
   horizontal span is at most \(2R^2\). To prove this, write the black
   side vector as \((X,Y)\), the black diagonal vector as \((Z,W)\),
   and the common-corner translation as \((t,u)\). The common corners
   are integer cells, so \(t,u\) are integers. The equations give

   \[
   X^2+Y^2=Z^2+W^2,\qquad Xt=-Yu,
   \qquad |Y|,|W|,|u|\le R. \tag{1}
   \]

   Suppose \(|X|>R^2\). Then \(|t|<1\), hence \(t=0\). If
   \(Y\ne0\), then \(u=0\), which degenerates the side rectangle.
   If \(Y=0\), the difference-of-squares equation forces
   \(|Z|=|X|\) and \(W=0\): otherwise its absolute nonzero difference
   is at least \(2|X|-1>R^2\). In that case the black diagonal endpoints
   equal the two supposed common corners, also a degeneracy. Thus
   \(|X|\le R^2\). Equation (1) and integrality imply \(|Z|\le R^2\)
   as well, since \((R^2+1)^2>R^4+R^2\). Finally \(|t|\le R^2\).
   The side and diagonal projection intervals each have length at most
   \(R^2\), and their midpoints differ by \(t\). Their union has span
   at most \(2R^2\).

4. **An integral P pair:** its horizontal separation is less than
   \(R^2/2\). If that separation is \(X>0\) and the odd row difference
   is \(Y\), then \(X^2+Y^2=L^2\), with \(L\ge X+1\), gives
   \(2X+1\le Y^2\le R^2\).

The vertical-side mixed case is intentionally treated as a P pair with
an axis owner. The axis owner can be arbitrarily far away. Its presence
must be encoded by the full final row-pair graph, even for a local module.
Likewise, parking a three-black rectangle must be checked against the
actual final column at its fourth corner, including when that corner lies
outside the module's nominal row band.

## 3. The dyadic width budget really is quadratic

For \(Q=2^n\), let \(B_x=2^{v_2(x)}\), \(1\le x<Q\). Then

\[
 \sum_{x=1}^{Q-1}B_x^2
 =\sum_{k=0}^{n-1}\frac{Q}{2^{k+1}}4^k
 =\frac{Q(Q-1)}2. \tag{2}
\]

In particular,

\[
 \sum_{x=1}^{Q-2}(B_x+B_{x+1})^2<2Q^2. \tag{3}
\]

There is also a useful separation fact. For \(i<j\), put
\(B_* =\max_{i\le x\le j}B_x\). An interval of \(j-i+1\) consecutive
integers contains a multiple of every power of two not exceeding its
length. Therefore \(B_*\ge(j-i)/2\). For the natural index-row bands
\(I_x=[x-B_x,x+B_x]\),

\[
 \operatorname{diam}(I_i\cup I_j)
 \le j-i+B_i+B_j\le4B_*. \tag{4}
\]

Placing a gap \(C(B_x+B_{x+1})^2\) between successive modules provides,
somewhere between modules \(i\) and \(j\), a gap at least \(CB_*^2\).
Together with the preceding support-span bounds, this is the correct
quadratic budget for separating forbidden supports made only of module
points. Fixed physical row dilation changes only \(C\).

This is not yet a filled-board gluing theorem. Every intervening column
must contain a black cell, and a support can use those filler cells.
Their rows and their interactions with the modules still require a
proof. More basically, the existing H7 sea already has the following
local-height obstruction.

## 4. Every H7 three-row sea has an external P pair

Suppose

\[
 L<F<H,\quad F\equiv L\pmod2,\quad H\not\equiv L\pmod2,
\]
\[
 H-L\equiv g\ne0\pmod7,\qquad F-L\equiv3g\pmod7. \tag{5}
\]

The sea has row \(L\) at nonsquare nonzero columns modulo seven,
row \(H\) at square columns, and row \(F\) at zero columns. Columns
are measured relative to the profile's horizontal origin.

**Proposition.** This sea contains two opposite-parity black points with
an integral vertical alternative. Their horizontal separation is at most
\(((H-L)^2-1)/2\). Consequently the sea fails the full parity P test in
any ambient strip containing the two alternative rows. These black
points can be chosen away from all columns eligible for H7 substitutions.

**Proof.** For every positive odd \(d\), put

\[
 X_d=\frac{d^2-1}{2},\qquad K_d=\frac{d^2+1}{2}.
 \qquad X_d^2+d^2=K_d^2. \tag{6}
\]

For \(d>1\), \(X_d\) is a positive multiple of four and \(K_d\) is
odd. If black points in rows \(r<s\), with \(d=s-r\), have horizontal
separation \(X_d\), their integral vertical alternative has rows

\[
 u=\frac{r+s-K_d}{2},\qquad v=\frac{r+s+K_d}{2}. \tag{7}
\]

The rows \(u,v\) have opposite parity.

If \(g^2\not\equiv1\pmod7\), take \((r,s)=(L,H)\). Then
\(X_d\not\equiv0\pmod7\). The difference set

\[
 \{1,2,4\}-\{3,5,6\}=\{1,2,3,4,5,6\}\pmod7
\]

shows that a low column and a high column occur at separation \(X_d\).
Neither is eligible for a substitution, since both are nonzero modulo
seven. Here \(d>1\) follows already from \(g^2\ne1\).

If \(g^2\equiv1\pmod7\), take \((r,s)=(F,H)\). Then
\(d\equiv-2g\), so \(d^2\equiv4\) and \(X_d\equiv5\pmod7\).
Place the high point \(X_d\) columns to the left of a filler column:
its residue is \(-5=2\), a square. Here again \(d>1\). The filler
column can be chosen in \(7\mathbb Z\) but outside \(S\mathbb Z\),
because H7 has \(S\ge6272\) divisible by seven. Both endpoints then
survive every allowed label substitution. This proves the proposition.

For a finite uninterrupted profile run, length \(X_d+14\) columns
suffices to realize the indicated pair away from substitution columns:
in the filler case there are two candidate filler columns seven apart,
and at most one is a multiple of \(S\). Endpoints must of course remain
inside that run. A translated horizontal origin changes none of this.

If all final parity labels occur, the owner of \(\{u,v\}\) supplies
the axis rectangle with the same presentation as the tilted rectangle.
If the owner lies in the midpoint column itself, the tilted rectangle is
fully black instead; the established hidden-rectangle exclusion applies.
Thus this is a genuine full-board issue, not just a stronger candidate
test being imposed for convenience.

## 5. A stronger three-corner obstruction at linear range

There is a simpler necessary condition which does not disappear on
excursions larger than \(\sqrt h\). Keep the profile assumptions (5),
and put

\[
 p=H-L,\qquad q=H-F.
\]

Choose \(\epsilon\in\{1,-1\}\) so that
\(\chi(\epsilon p)=1\). This is possible because \(p\not\equiv0\)
and \(\chi(-1)=-1\) modulo seven. The three points

\[
 A=(\epsilon p,H),\quad B=(0,F),\quad
 C=(\epsilon(p+q),L) \tag{8}
\]

are black in the profile. Indeed \(q\equiv-2g\) and
\(p+q\equiv-g\), so \(A\) is in a high column and \(C\) is in a
low column. Their two side vectors at \(A\) are

\[
 (-\epsilon p,-q),\qquad(\epsilon q,-p),
\]

whose dot product is zero. Both horizontal and vertical components are
nonzero. The fourth corner is

\[
 W=(\epsilon q,L+F-H). \tag{9}
\]

Its column is low, since \(\chi(-2)=-1\) modulo seven. Its row has
the parity of \(H\), opposite to the low sea point. Thus it is an
unparked three-black tilted rectangle whenever its row is in the ambient
strip. The upper row bound is automatic because \(L+F-H<L\).

All four columns are distinct, and the horizontal span is \(p+q<2p\).
Translation by a multiple of seven preserves every sea type. Any
uninterrupted profile run of at least \(p+q+14\) columns admits two such
translations whose filler columns are seven apart. At most one can be
a multiple of the H7 substitution stride \(S\). Choose the other one.
The high and low columns are nonzero modulo seven, so they are never
substitution columns. The resulting obstruction therefore survives
arbitrary allowed substitutions throughout the run.

For example, \(L=101,F=125,H=130\) satisfies the profile congruences
and the same-parity mod-four alignment. The black points
\((29,130),(0,125),(34,101)\) complete to \((5,96)\), a low column
with the wrong row parity. The filler column can be translated away
from the substitution lattice as above.

Consequently, a necessary condition for reusing an H7 profile in the
full strip \([1,h]\), in a sufficiently long run, is

\[
 \boxed{L+F-H<1.} \tag{10}
\]

A genuinely local profile whose three rows are \(t+O(B)\), with
\(t\gg B\), violates (10). This obstruction persists after discarding
small excursions. Retaining the original nonlocal low rows near the
global boundary avoids this particular obstruction, but loses the
local-black-row diameter needed for the proposed quadratic gluing.
Vertically reflecting the profile reflects the obstruction to the
upper boundary; it does not make an interior band globally valid.

## 6. What an adaptive FW repair must change

Let \(R=H-L\). Formula (7) places both alternative rows within
\([L-R^2,H+R^2]\). Thus, for example, an H7 module translated into the
interior of a much taller strip with margins at least \(R^2\) has the
obstruction whenever its unaltered profile run is long enough. Local
validity in the strip \([L,H]\) does not imply validity after this
translation: the new white rows were unavailable in the smaller strip.

The dyadic sum (2) remains useful. To turn it into a full FW repair, one
needs local backgrounds and filled connectors that are valid against
the **full ambient parity graph**, rather than only against the local
height. Alternatively, the cross-parity sea P pairs in Section 4 must be
removed explicitly, with all newly created three- and four-corner
families checked. The current profile theorem supplies neither step.

The conclusion is limited to reusing the existing three-row periodic
profile. It does not obstruct a different background, a controlled
nonperiodic repair, or a direct choice proof for FW across excursions.

The number of labels in excursions of scale at most \(\sqrt h\) is
only \(O(h^{3/2})\), since their dyadic sum is
\(\sum_{B\le\sqrt h}O((h/B)B^2)\). An exceptional-label construction
could therefore absorb those scales under its existing hypotheses.
That observation can bypass some instances of the quadratic-range P
obstruction in Section 4. It does not bypass the linear-range
obstruction (8)--(10).
