# Long residual supports have nearby core anchors

15 November 2026. Partial-parity Hölder locality does not reduce every
residual support's span below quadratic order. It does give a useful
alternative: for a cutoff \(H=h^2/K\), long \(\Lambda_3\) and
\(\Lambda_4\) supports have opposite-parity core points within
\(O(K)\) columns. Long 6PT supports have nearby core points, without
an unconditional parity assertion, and both sea offsets are \(O(K)\).
Here \(K\) can be any fixed power of \(\log h\).

This local-anchor conclusion is not a bound on the number of long
supports. A same-offset 6PT family below has span \(\Theta(h^2)\)
while satisfying the locality, good-row, and occupied-slot hypotheses.
It is not claimed to embed in the exact random-cap order.

## 1. Hypotheses and span convention

All core points lie at columns in \(S\mathbb Z\), with at most one
point of each parity at any such column. All rows lie in \([1,h]\).
For same-parity core points assume
\[
 |y-y'|^2\le\kappa|x-x'|,
 \tag{1}
\]
where \(\kappa\) and \(S\) are fixed and \(S>\kappa\). This holds
for the occupied cap cores after the stated fixed stride enlargement.
The span here is the diameter of the core black-point columns. Adding
the associated white corners and sea points changes the long-span
statements only by fixed factors or \(O(h)\), as the proofs show.

The mixed-support conventions and parked-triangle equations are those
of the existing H7 reduction. In particular, a nondegenerate mixed
four-support has a nonvertical side, a nonzero perpendicular connector,
and its diagonal vector is not the side vector or its negative.

## 2. Lambda3: a long angle has a short cross-parity pair

Consider a tilted right-angle triple that is not all one parity. Its
unique same-parity pair is either a leg or the hypotenuse.

If it is a leg, write that leg as \((X,\delta)\) and the other as
\((\xi,m)\). Orthogonality and (1) give
\[
 X\xi=-\delta m,\qquad
 |\xi|\le h\sqrt{\kappa/|X|}\le C h.
 \tag{2}
\]
Both horizontal legs are nonzero, because the rectangle is tilted.
If the core span exceeds \(H\ge C_1h\), then \(|X|>H/2\).
Since \(|\delta|,|m|<h\), (2) now gives
\[
 |\xi|\le2h^2/H.
 \tag{3}
\]
This is the column distance of an opposite-parity pair.

If the same-parity pair is the hypotenuse, put its endpoints at
\((0,0),(X,\delta)\), with \(X>0\), and the right-angle vertex
at \((x,y)\). Then
\[
 x(X-x)=y(y-\delta).
 \tag{4}
\]
If \(x\) were outside \([0,X]\), its distance \(t\) from that
interval would satisfy \(tX\le\delta^2/4\), hence
\(t\le\kappa/4<S\), impossible for a distinct lattice column.
The endpoint cases are axis-aligned, so \(0<x<X\). The black span is
therefore \(X\). Since the right side of (4) is at most \(h^2\),
the nearer endpoint has column distance at most \(2h^2/X\).
It is of the opposite parity from the right-angle vertex, proving (3).

## 3. Lambda4: a long mixed support has a short pair

Write the side and diagonal vectors as
\(u=(x,y)\), \(v=(z,w)\), and their midpoint displacement as
\(t=(t_x,t_y)\). Translate the side endpoints to \(A=0,B=u\).
The diagonal endpoints are
\[
 C=(u-v)/2+t,\qquad D=(u+v)/2+t.
\]
The mixed equations are
\[
 x^2+y^2=z^2+w^2,\qquad xt_x+yt_y=0.
 \tag{5}
\]
All of \(|y|,|w|,|t_y|\) are at most \(h\).
The black span is at most \(2|x|+2|t_x|+h\). Thus if it exceeds
\(H\ge2h\), either \(|x|>H/8\) or \(|t_x|>H/8\).

In the latter case, (5) gives
\[
 |x|\le8h^2/H.
 \tag{6}
\]
If the side were same-parity, (1) would also give
\(|t_x|\le h\sqrt{\kappa/|x|}=O(h)\), since \(|x|\ge S\).
For \(H\ge C_2h\), the side must therefore be opposite-parity.

In the long-side case, orient \(x>0\) and swap the diagonal endpoints
so \(z\ge0\). Equation (5) gives
\[
 |x-z|\le h^2/x,\qquad |t_x|\le h^2/x.
\]
Consequently both corresponding pairs satisfy
\[
 |C_x-A_x|,\ |D_x-B_x|\le12h^2/H=:K_0.
 \tag{7}
\]
For \(H\ge C_3h^{4/3}\), at least one of these pairs is
opposite-parity. Otherwise (1) gives
\[
 |t_y|\le\sqrt{\kappa K_0},\qquad
 |y-w|\le2\sqrt{\kappa K_0}.
\]
Equations (5) then imply
\[
 |t_x|+|x-z|\le C_4 h^2/H^{3/2}.
 \tag{8}
\]
Choose \(C_3\) so the right side is less than \(1/2\).
As \(t_x\) is a half-integer and \(x-z\) is an integer, both
vanish. Equal norms now give \(w=\pm y\). If \(w=y\), then
\(v=u\), which is excluded. If \(w=-y\), perpendicularity gives
\(yt_y=0\); either \(y=0\) and again \(v=u\), or \(t=0\),
which is also excluded. This contradiction proves the cross-parity claim.

## 4. Long 6PT: both sea offsets are small

For the two parked triangles sharing a completion, let \(s\) be their
common sea row and \(\delta\ne0\) their common same-parity row
increment. Write their core displacements and sea offsets as
\(X_i,\xi_i\), for \(i=1,2\). The exact equations are
\[
 X_i\xi_i=-\delta m_i,\qquad
 |m_i|<h,\qquad \delta^2\le\kappa|X_i|.
 \tag{9}
\]
The nonzero integral offsets obey \(|\xi_i|\le C h\), by the
same estimate as (2). Relative to the common completion, the four core
columns are \(-\xi_i\) and \(-\xi_i-X_i\). If their span exceeds
\(H\ge C_5h\), one \(|X_i|\) exceeds \(H/4\). As
\(|\xi_i|\ge1\), (9) implies
\[
 |\delta|\ge H/(4h).
\]
Apply (9) to both triangles to obtain
\[
 |\xi_1|,|\xi_2|\le\frac{\kappa h}{|\delta|}
       \le4\kappa h^2/H,
 \qquad
 |X_1|,|X_2|\ge H^2/(16\kappa h^2).
 \tag{10}
\]
The two completion-end core points have column distance
\(|\xi_1-\xi_2|\le8\kappa h^2/H\). When the offsets are equal,
these distinct points share one column, so they must be of opposite
parity and form a genuine double. For distinct offsets they can have the
same parity; no cross-parity conclusion is asserted. Full slot occupancy
also rules out a parked triangle with its sea source at an occupied
lattice slot, so offsets that would create that situation remain excluded.

For \(H=h^2/K\), (10) leaves only \(O(K)\) possible integral sea
offsets for each triangle, and an \(O(K)\)-column core-point anchor.
This does not yet bound how many far endpoints can attach to that anchor.

## 5. A quadratic-span 6PT family compatible with the local hypotheses

Fix a positive nonlattice sea offset \(\xi\) of low sea type, for
example \(\xi=3\) in the standard normalized H7 core. Let \(L\)
be that fixed low sea row. Choose a sufficiently small fixed
\(\varepsilon>0\), and choose
\(\delta\in\xi S\mathbb Z\) with \(\delta\sim\varepsilon h\).
Choose good odd/even rows
\[
 u\in[h/3,5h/12],\qquad v\in[2h/3,3h/4],
\]
such that \(u-\delta,v-\delta\) are also good. This is possible
in fixed full residue classes after excluding any \(o(h)\) bad rows:
each interval has \(\Theta(h)\) candidates, and two translates of
the bad set still have size \(o(h)\).

Put
\[
 X=\delta(u-\delta-L)/\xi,\qquad
 X'=\delta(v-\delta-L)/\xi.
 \tag{11}
\]
Both are multiples of \(S\), and
\(X,X',X'-X=\Theta(h^2)\). Place the three distinct doubles
\[
 0:\{u,v\},\qquad
 -X:\{u-\delta,v\},\qquad
 -X':\{u,v-\delta\}.
 \tag{12}
\]
The odd parked triangle uses the sea point \((-X+\xi,L)\), and
the even triangle uses \((-X'+\xi,L)\). Their common fourth corner
is
\[
 W=(\xi,L+\delta).
 \tag{13}
\]
The dot products vanish by (11). The sea points have the chosen low
column type, while \(W\) is white and lies inside the strip. Thus the
two distinct rectangles have the same singleton presentation.

The lattice interval can be fully occupied while preserving (1). Let
\(R\) be a multiple of \(S\) just above \(2\delta^2/\kappa\).
Fill lattice slots within distance \(R\) of \(-X\) by even row \(v\),
and every other lattice slot by odd row \(u\). At the three columns
in (12), add the other indicated point. Choose \(\varepsilon\) small
enough that \(X,X'-X>3R\). The only unequal same-parity row values
then differ by \(\delta\), and their closest horizontal separation
is larger than \(R\). Hence (1) holds, with room to spare. All slots
are occupied by good bulk rows; no filler-row point is restored.

This supplies a quadratic-span forbidden support consistent with the
listed local hypotheses and distinct double labels. It does not claim
that this entire filling is valid, that it realizes the random-cap order,
or that its genuine labels survive every other cleanup. Its purpose is
to rule out a span-only argument based solely on those hypotheses.

The distinct-offset case can also have all four core corners of one
parity. Take \(\xi_1=3\), \(\xi_2=3+S\), a good odd row \(a\),
and a positive \(\delta\sim\varepsilon h\) divisible by
\(S\xi_1\xi_2\), with \(a+\delta\) good. Put
\(X_i=\delta(a-L)/\xi_i\). Relative to the common completion,
the core points are \((-\xi_i,a+\delta)\) and
\((-\xi_i-X_i,a)\). Translate horizontally by \(\xi_1\) so all
core columns lie on the original lattice. Both sea offsets have low
type. The nearby completion-end points have the same row, while every
unequal-row distance is \(\Theta(h^2)\). Choosing \(\varepsilon\)
small makes (1) hold. This explains why Section 4 retains both parity
possibilities when the sea offsets differ.

The actionable alternative is the local-anchor description in Sections
2–4: for a cutoff just below quadratic scale, long residual events attach
to a bounded or polylogarithmic column window through explicit arithmetic
parameters. Counting or solving those anchored constraints remains open.

Independent review: the complete written reductions and the occupied
quadratic-span example passed a separate audit after the distinct-offset
6PT parity correction. The audit checked the Lambda4 half-integrality
step and the nearest unequal-row distances in the explicit filling.
The source parity in distinct-offset 6PT remains unrestricted.
