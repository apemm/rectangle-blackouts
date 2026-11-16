# Constant even slot fillers create one-label mixed collisions

15 November 2026. Putting row one at every nonarithmetic column and
a shallow even row at unused arithmetic columns does remove some
opposite-parity P constraints. It nevertheless has an immediate
one-label mixed obstruction. Every constant even filler row has such
an obstruction for every sufficiently deep even label row.

This is a finite-support obstruction. It applies when the indicated
arithmetic filler points are present and all displayed columns fit
inside the board. It does not rule out occupying those slots with
other doubles, or choosing filler rows adaptively by column.

## 1. Setting and the valid row-two P exclusion

Use sea row one outside \(4\mathbb Z\). At unused arithmetic columns,
put a singleton in row two. A used arithmetic column has a genuine
double with odd row \(a\equiv3\pmod4\) and even row
\(b\equiv2\pmod4\).

There is no in-strip vertical P rival between a row-two filler and
an odd label point in row \(a\). Indeed, write \(X\in4\mathbb Z\)
for their horizontal displacement and \(Y=a-2>0\). If their norm
is integral, put \(t=(\sqrt{X^2+Y^2}-Y)/2\). An in-strip lower
alternative row requires \(2-t\ge1\), so \(t=1\). But then
\[
                     X^2=4t(Y+t)=4(a-1)\equiv8\pmod{16},
\]
contradicting \(X\in4\mathbb Z\).

The obstruction below uses a same-parity even label/filler pair,
so this valid P exclusion does not address it. Its horizontal white
chord is paired with a horizontal black side.

## 2. A universal two-rectangle template

Let the constant filler row be any fixed positive even \(f\), and
let the inserted even label have row \(b>f\). Write
\[
                           d=(b-f)/2.
\]
For an integer \(p>0\) dividing \(d^2\), set
\[
\begin{split}
 E&=(0,b),&
 C&=(d^2/p-p,f),\\
 P&=(-p,f+d),&
 Q&=(d^2/p,f+d).
\end{split}                                                     \tag{1}
\]
The legs from \(E\) to \(P,Q\) are
\[
                     (-p,-d),\qquad(d^2/p,-d),
\]
and their dot product is zero. Thus \(E,P,C,Q\) form a tilted
rectangle. If black points
\[
                         A=(-p,s),\qquad B=(d^2/p,s) \tag{2}
\]
are available at one common sea or filler row \(s\ne f+d\),
then \(A,P,Q,B\) form an axis rectangle.

If \(E,C,A,B\) are black and \(P,Q\) are white, these two distinct
rectangles have exactly the same presentation \(\{P,Q\}\).
There is no remote-owner hypothesis: the axis rectangle is already
inside this displayed support.

The following choices make all black points automatic except the
specified unused arithmetic slots.

| Condition on \(d\) | \(p\) | Horizontal black-side row \(s\) | Required filler columns |
|---|---:|---:|---|
| \(d\) odd | \(1\) | \(1\) | \(d^2-1\) |
| \(d\equiv2\pmod4\) | \(2\) | \(1\) | \(d^2/2-2\) |
| \(4\mid d\) | \(4\) | \(f\) | \(-4,\ d^2/4-4,\ d^2/4\) |

In the first case, the two common columns \(-1,d^2\) are odd,
and \(d^2-1\in4\mathbb Z\). In the second, the two common columns
are \(2\pmod4\), and \(d^2/2-2\in4\mathbb Z\). Hence their black
side points in (2) are automatic row-one sea points.

In the third case, all three required filler columns are divisible
by four. The two common columns have only their row-\(f\) filler
point, so the common cells at row \(f+d\) are white.

The construction is nondegenerate when \(d>p\). In particular,
\(b-f\ge10\) suffices in all three cases. All displayed rows lie
between \(1\) and \(b\), so they lie in the strip whenever \(b\le h\).

A finite board needs room for \(p\) columns to the left of the label
and \(d^2/p\) to its right. Horizontal reflection exchanges those
requirements. The horizontal span is \(O(h^2)\).

## 3. Both row-two label residues fail

For the proposed filler \(f=2\), the relevant label rows satisfy
\(b\equiv2\pmod4\), so \(d\) is even.

If \(b=2+8z\), \(z\ge2\), take
\[
 \begin{gathered}
 E=(0,b),\quad C=(4(z^2-1),2),\\
 A=(-4,2),\quad B=(4z^2,2),\\
 P=(-4,2+4z),\quad Q=(4z^2,2+4z).
 \end{gathered}                                                   \tag{3}
\]
This needs three unused arithmetic filler slots.

If \(b=2+4z\) with odd \(z\ge3\), take
\[
 \begin{gathered}
 E=(0,b),\quad C=(2(z^2-1),2),\\
 A=(-2,1),\quad B=(2z^2,1),\\
 P=(-2,2+2z),\quad Q=(2z^2,2+2z).
 \end{gathered}                                                   \tag{4}
\]
Only \(C\)'s arithmetic slot needs to be unused. Both other black
points are permanent row-one sea points.

These are the vertical reflections of the two mixed certificates in
[the earlier checkerboard-sea obstruction](continuation_checkerboard_sea_obstruction.md).
The second certificate uses a horizontal side in the odd sea, rather
than three row-two filler points. Restricting to \(b\equiv6\pmod8\)
therefore does not avoid the problem.

Every bulk row \(b\equiv2\pmod4\), \(b\ge14\), belongs to one of
(3)--(4). The original odd point in the label's column can have any
allowed row; it does not remove either support.

Likewise, changing the constant filler from two to six only changes
which row of the table in Section 2 applies. A finite menu of constant
even filler heights assigned by row profile does not avoid all these
supports. This does not address a filler height chosen separately
at each arithmetic column.

## 4. The signed parked-triangle family

The proposed parked triples do exist, with a sign qualification.
For \(b=2+4t\), let \(k\) be a nonzero signed divisor of \(t\)
with \(k\not\equiv0\pmod4\). At a label column \(x\), use
\[
 \begin{split}
 E&=(x,b),\\
 F&=(x+4t/k,2),\\
 A&=(x+4t/k-k,1).
 \end{split}
\]
When the arithmetic column of \(F\) is unused, these points make a
right angle at \(F\). Its completion is
\[
                              W=(x-k,b-1).           \tag{5}
\]
The restriction on \(k\) ensures that \(A\) is an ordinary sea
column. The completion has the same odd row parity as its sea point.

Both signs of \(k\) are possible when the board has room.
For two labels at the same even row, equality of these completion
columns requires
\[
                              x_2-x_1=k_2-k_1.
\]
Its absolute value can be as large as \(2t=(b-2)/2\).
Thus spacing greater than \(h/4\) does not exclude the full signed
family. Spacing greater than \(h/2\) does exclude this particular
same-row completion coincidence.

For example, at \(h=b=26\), put the two labels at columns zero
and twelve. Their row-two fillers at \(-4,16\), and row-one sea
points at \(2,10\), give two triples with common completion
\[
                                W=(6,25).
\]
The label separation is twelve, larger than \(h/4\).
A common horizontal translation makes all columns positive.

## 5. Placement implications and limitations

Spacing labels with the same even row does not prevent the one-label
mixed supports (3)--(4). To avoid (4) at an interior label, its specific
arithmetic column at distance \(2(z^2-1)\), in either usable horizontal
direction, must fail to carry the row-two filler. The analogous
requirements in the other table rows involve one or three filler
positions.

These are concrete placement or filler-choice obligations. They may
be useful for deriving a further closure obstruction, but no such
global theorem is asserted here. In particular, a used arithmetic
slot can destroy the displayed support by removing its shallow filler
point, and a short finite board may not contain the far endpoint.

The template also gives a broader limitation. It uses only that \(b\)
and \(f\) have the same parity, not that both are even. Thus any constant
filler row has this mixed obstruction against a sufficiently separated
label point of its own parity. If \(b<f\), replace the common white
row \(f+d\) by \(f-d\), where \(d=(f-b)/2\); the two tilted legs
then have vertical component \(+d\). The same column-residue table
applies. The common row \((b+f)/2\) is strictly above one whenever
\(b,f\ge1\) and \(|b-f|\ge10\).

Since a genuine double contains both row parities, no constant filler
height is uniformly one-label-safe merely through a parity choice.
This is still a finite-support statement with the same filler-slot
and finite-width hypotheses.

## 6. One unused slot can defeat a whole fixed even palette

Fix a finite set \(\mathcal F\) of positive even filler rows.
There is a local configuration of \(|\mathcal F|\) genuine doubles
for which an arithmetic slot at zero cannot use any row in
\(\mathcal F\), irrespective of the fillings at other arithmetic slots.

The genuine doubles can have distinct even rows \(b_f\equiv2\pmod4\)
in \([.78h,.82h]\), one common odd row \(A\equiv3\pmod4\) in
\([.70h,.71h]\), and pairwise column separation greater than \(h\).
Their same-parity squared row differences are smaller than twice their
column differences. Thus the obstruction does not depend on a P pair
between the genuine doubles or on closely repeated even rows.

Choose a parameter \(Z\) in an interval of length \(\Theta(h)\) so that
\(4Z\in[.39h,.40h]\). Enumerate the fixed palette and choose distinct
fixed positive shifts \(c_f\), spaced sufficiently far apart, with
\[
 c_f\text{ odd if }f\equiv0\pmod4,\qquad
 c_f\equiv2\pmod4\text{ if }f\equiv2\pmod4.
\]
Their spacing can exceed \(16+\max\mathcal F\). Put
\[
 d_f=4Z+c_f,\qquad
 p_f=\begin{cases}1,&f\equiv0\pmod4,\\2,&f\equiv2\pmod4,\end{cases}
 \qquad
 b_f=f+2d_f,\qquad
 x_f=-\left(d_f^2/p_f-p_f\right).                    \tag{6}
\]
Then \(b_f\equiv2\pmod4\), \(x_f\in4\mathbb Z\), and the
\(b_f\)'s can be made distinct by the spacing of the shifts.
Insert the label \((A,b_f)\) at \(x_f\).

If the target slot chooses row \(f\), apply (1) after translating its
label column to \(x_f\). Its second black diagonal point is exactly
\((0,f)\), while its two row-one black side points are at columns
\[
                         -d_f^2/p_f,\qquad p_f.       \tag{7}
\]
Both columns are nonarithmetic, as proved in the table. Their common
white row is \(f+d_f>1\). Therefore that choice of filler produces
the same immutable two-white collision. No other arithmetic filler
point is used.

For equal \(p_f\), distinct \(x_f\)'s are separated by
\[
 |d_f-d_{f'}|\,(d_f+d_{f'})/p_f>h
\]
once the fixed shifts have the stated separation and \(h\) is large.
Different \(p_f\)'s give separated bands of order \(h^2\).
Within each parity the inserted rows differ by only \(O_{\mathcal F}(1)\),
so their same-parity norm-gap inequalities follow. A nonhorizontal
actual P pair between distinct genuine columns would have norm greater
than \(h\), hence could not have both vertical alternatives in the strip.

The even rows can all avoid a given literal bad set of size \(o(h)\).
Each \(b_f=8Z+(f+2c_f)\) is an injective function of \(Z\), so the
finitely many bad-row exclusions remove only \(o(h)\) parameter choices.
Choose the common odd row \(A\) outside its own \(o(h)\) bad set.
The construction occupies only a fixed number of genuine columns in
an interval of width \(O_{\mathcal F}(h^2)\).

This is an adversarial local placement. It does not show that an
arbitrary row-major arrangement contains these columns, or that a
height-dependent filler palette must fail. It does show that a fixed
even palette at an unused slot is not guaranteed to work by genuine
source separation and same-parity geometry alone.


Independent written review: all sections passed a separate
check of the universal template, all three column-residue cases,
nondegeneracy, both row-two certificates, the signed parked example,
and the odd-filler and downward-reflected extensions. The finite
column margins and presence of the required filler slots were
retained explicitly. Section 6 was also checked for both residue cases,
distinct source rows and columns, source separation, automatic sea
supports, common white corners, and the bad-row averaging step.

