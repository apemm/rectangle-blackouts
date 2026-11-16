# Five nearby source rows can block a growing target palette

15 November 2026. Same-parity square-root locality does not ensure a
P-safe target row, even in a growing palette and even when every
specified P pair has horizontal leg and smaller half-factor of order
\(h\). Two fixed Pythagorean directions suffice for a fully occupied
local obstruction.

This is a geometric background construction, not an embedding into the
sampled Hilbert cap model. It rules out a deterministic availability
theorem based only on locality, actual-good rows, and the number of
nearby source columns. It leaves coupled changes of the surrounding
points and genuine block permutations open.

## 1. Statement

Let \(K=K(h)\ge1\) be an integer with \(K=o(h)\). There is a locally
fully occupied spacing-four constant-sea configuration with the
following properties.

* Every nonarithmetic column has its single black point at sea row one.
* Every arithmetic column except zero has one odd black point in the
  five-row set
  \[
                         A,A+4,A+8,A+12,A+16.       \tag{1}
  \]
* Column zero must choose one even row from
  \[
                 b_j=A+Y_0+4j,\qquad 0\le j<K.    \tag{2}
  \]
* Every choice in (2) has a P rival against a fixed odd point.
  Its horizontal leg and smaller half-factor are both \(\Theta(h)\).
* The odd row-index function is one-Lipschitz and satisfies
  \[
        |z(r)-z(s)|^2\le |r-s|/2
                       \qquad\text{when }|r-s|\ge2. \tag{3}
  \]
  Its adjacent unit changes are isolated, with at least eight fine
  rank steps between their locations. Hence it has the same
  same-parity norm, triangle, and mixed-support exclusion geometry
  used by the spacing-four refinement.

Here \(A\equiv3\pmod4\), and all target rows are \(2\pmod4\).
The odd rows and target rows lie in a fixed bulk interval.

Given arbitrary forbidden sets \(B_O,B_E\), each of cardinality
\(o(h)\), the five rows in (1) can all avoid \(B_O\). Simultaneously,
\((1-o(1))K\) of the target choices avoid \(B_E\). Thus restricting
the palette to actual-good choices does not supply a safe choice.

If the completed board retains the required opposite-parity row-pair
owners, each P rival is an actual rectangle-presentation collision.
These owners need not lie in the displayed local strip. No statement
is made about all other collisions in this adversarial background.

## 2. Covering every target by two norm families

Choose
\[
  Y_0\in[h/20,h/20+60],\qquad Y_0\equiv15\pmod{60},
  \qquad .70h\le A\le .71h,\quad A\equiv3\pmod4.     \tag{4}
\]
The short interval in (4) contains a suitable \(Y_0\), with an
immaterial endpoint adjustment. All statements below hold for
sufficiently large \(h\).

First handle \(j=3n+e\) with \(e\in\{0,1\}\). Set
\[
 g=Y_0/3+4n,\qquad
 (X,Y,L)=(4g,3g,5g).                               \tag{5}
\]
Place the odd source in row \(A+4e\), at column \(-X\) if \(e=0\)
and at \(+X\) if \(e=1\). Its vertical displacement to \(b_j\) is
exactly \(3g\).

It remains to handle \(j\equiv2\pmod3\). Write \(j=5m+r\), where
\(0\le r<5\). The permitted remainders are
\[
\begin{array}{c|ccc}
 m\bmod3&0&1&2\\ \hline
 r&2&0,3&1,4.
\end{array}                                                       \tag{6}
\]
Set
\[
 g=Y_0/5+4m,\qquad
 (X,Y,L)=(12g,5g,13g).                             \tag{7}
\]
For the first remainder in each entry of (6), put the source in row
\(A+4r\) at \(-X\). For the second remainder, when present, put it
at \(+X\). Again its vertical displacement to \(b_j\) is exactly
the displayed \(Y\).

No two prescribed points demand different rows at the same column.
Within a family, different group indices give different columns.
The two signs separate the two remainders in a group. The absolute
column centers of the two families are
\[
                       4Y_0/3,\qquad 12Y_0/5,
\]
whose difference is \(\Theta(h)\). Their total variation is \(O(K)\),
so the four signed source bands are disjoint.

The smaller half-factors are
\[
              t=(L-Y)/2=g\quad\text{in (5)},\qquad
              t=4g\quad\text{in (7)}.               \tag{8}
\]
Thus \(X,t=\Theta(h)\), uniformly over all \(j<K\). The two directions
are fixed; the construction does not use a growing direction set.

## 3. Filling every arithmetic column with the required locality

Use fine rank \(r=x/4\), and express an odd row as \(A+4z(r)\).
The negative and positive source bands from (5) require the constant
values zero and one, respectively.

On the negative band from (7), the required row indices are
\(2,0,1\), periodically, as the group index \(m\) increases.
Their actual ranks decrease by twelve. Define the coordinate in the
following period in the reverse horizontal direction.

Let \(f\) be period thirty-six on the integer line, with
\[
 f(t)=
 \begin{cases}
 2,&t\bmod36\in[0,1]\cup[28,35],\\
 1,&t\bmod36\in[2,9]\cup[18,27],\\
 0,&t\bmod36\in[10,17].
 \end{cases}                                                       \tag{9}
\]
Then \(f(12m)\) is \(2,0,1\), as required. Set \(t\) equal to
minus the actual rank, plus the fixed shift aligning the first source.
Every adjacent change in (9) is a unit change. Successive change
locations are separated by eight or ten. Points with values zero and
two have rank distance at least nine. Therefore (3) holds in this band.

On the positive band from (7), groups \(m\equiv1,2\pmod3\) require
values three and four. Use the period-thirty-six profile that equals
three for residues \(0,\ldots,17\), and four for residues
\(18,\ldots,35\), with the appropriate rank translation. It takes
the required values at ranks \(12m\). Its unit seams are separated
by eighteen.

Omit any source band with no required point. Restrict each remaining
periodic profile to the interval between its first and last needed
source. Outside that interval, initially extend its
endpoint value constantly. The four source intervals have pairwise
distance \(\Theta(h)\). Join these constant endpoint values by unit
steps separated by at least sixty-four, also keeping every new step
at least sixty-four from a source interval. Choose either endpoint
value on an unbounded tail.

This produces a function with values in \(\{0,1,2,3,4\}\). To check
(3), if \(|r-s|\ge32\), use
\(|z(r)-z(s)|^2\le16\le |r-s|/2\). If \(|r-s|<32\), the pair is
inside a single periodic band with constant endpoint extensions,
or sees only one of the added unit steps. Constant extension preserves
the band's inequality by comparing to its nearest endpoint.
The one-step case has row difference at most one, so (3) follows for
rank distance at least two. All adjacent changes remain isolated.

At column zero omit the odd point and select one row from (2).
There is only one even point in this local configuration, so its
partial same-parity condition is vacuous. Every column remains occupied.
A sufficiently long finite interval contains every source and the
connecting profiles. Translate that interval by a multiple of four
if positive column indices are required.

## 4. The common cells are white and in the required strip

For a source row \(a=A+4r\) and a target row \(a+Y\), the common
vertical pair is at half the source column, in rows
\[
                           a-t,\qquad a+Y+t.        \tag{10}
\]
In family (5), \(g\equiv1\pmod4\). Hence the lower row in (10)
is even and \(2\pmod4\), and the upper row is odd and \(3\pmod4\).
In family (7), \(g\equiv3\pmod4\) and \(t=4g\). The lower row is
odd and \(3\pmod4\), and the upper row is even and \(2\pmod4\).

The numerical choices in (4), together with \(K=o(h)\), place all
rows in (10) in a fixed interior portion of the strip. In particular,
their odd member is above \(h/2\). Their distances from the five
background rows (1) are \(\Theta(h)\).

The midpoint column is even and nonzero. If it is \(2\pmod4\), its
only black point is sea row one. If it is \(0\pmod4\), its only black
point belongs to (1). In either case both cells in (10) are white.
Changing the singleton at column zero cannot affect them.

Together with a retained axis owner for the row pair (10), the tilted
rectangle and the axis rectangle have the same presentation. The
owner must be outside the specified singleton background. Retaining
it elsewhere is the full row-pair accounting hypothesis, not a claim
about this local filling.

## 5. Literal-good row choices

For fixed \(Y_0\), let \(\mathcal I\) be the possible values of \(A\)
in (4). It has \(\Theta(h)\) elements. Excluding any \(A\) for which
one of \(A,A+4,\ldots,A+16\) belongs to \(B_O\) removes at most
\(5|B_O|=o(h)\) values.

Moreover,
\[
 \sum_{A\in\mathcal I}
      \#\{0\le j<K:A+Y_0+4j\in B_E\}
       \le K|B_E|.                                  \tag{11}
\]
For each fixed \(j\), the map \(A\mapsto A+Y_0+4j\) is injective.
After the odd-row exclusions, there is therefore a remaining \(A\)
with at most \(O(K|B_E|/h)=o(K)\) forbidden target rows.

The entire selected odd background is actual-good for this \(A\).
Every remaining actual-good target choice is still forbidden by its
specified P pair. This argument does not assume independence of source
rows or of the good-row sets.

## 6. What this blocks

The construction applies, in particular, to \(K=\lfloor h^\epsilon\rfloor\)
for any fixed \(0<\epsilon<1\). It also leaves every specified P edge
outside sublinear horizontal-gap and smaller-half-factor cutoffs.
Thus a growing same-parity palette at a sparse singleton cannot be
certified from square-root locality and literal-good rows alone.

The positive guarded move in
[the third-row note](continuation_third_row_p_repair.md) remains valid
when all incoming constraints belong to one norm fiber. Here there
are many fibers, but only two rational directions and five source rows.
Useful additional structure must come from the actual joint placement
law, a coupled modification of the sources, or a block permutation.
No obstruction to those stronger mechanisms is asserted.

## 7. A positive availability bound when there are few fibers

There is a useful converse counting statement. Let a target palette
lie in a real vertical interval of width \(w\), and suppose every
potential source has absolute horizontal distance at least \(H>0\).
If
\[
                               w^3<8H,              \tag{12}
\]
one source forbids at most two candidate rows, even if the candidates
are not consecutive.

To prove this, fix its nonzero horizontal displacement \(X\), and
write the potential norm as
\[
        f(y)=\sqrt{X^2+y^2},\qquad
        0<f''(y)={X^2\over(X^2+y^2)^{3/2}}\le{1\over|X|}.
\]
If three integer vertical gaps \(y_1<y_2<y_3\) had integer norms
\(L_i=f(y_i)\), their determinant
\[
 D=(y_2-y_1)(L_3-L_1)-(y_3-y_1)(L_2-L_1)
\]
would be a strictly positive integer. Put
\(a=y_2-y_1\), \(b=y_3-y_2\). The second divided-difference bound gives
\[
       0<D\le {ab(a+b)\over2|X|}
              \le{w^3\over8|X|}
              \le{w^3\over8H}<1,
\]
a contradiction.

Consequently, if there are at most \(m\) distinct norm fibers
\((|X|,a)\), any palette of more than \(2m\) actual-good rows in
such an interval contains a P-safe target row. This is deterministic
and does not assume independent sources. Sources with the same
absolute horizontal distance and row count as one fiber.

In the spacing-four profile, the constant improves. All target rows
have one residue modulo four, the source has opposite parity, and
\(X\in4\mathbb Z\). Therefore the \(y_i\)'s differ by multiples
of four and each integral \(L_i\) is odd. The positive determinant
\(D\) is consequently divisible by eight. The same proof excludes
three norm points whenever
\[
                                w^3<64H.             \tag{13}
\]
The conclusion about more than \(2m\) actual-good choices holds under
this weaker inequality in the stated profile.

For a near-linear lower gap \(H=h^{1-o(1)}\), every fixed palette
width \(h^\epsilon\), \(\epsilon<1/3\), satisfies (12). Failure of
availability then requires at least half as many distinct fibers as
candidate rows. Sections 1--5 use one fiber per target and show that
this linear scale cannot be improved using locality alone.

The distance assumption concerns all potential partners of the new
row choices. It cannot be imported from a cutoff proved only for the
previously selected rows. A proof applying it after retuning must
compile or separately check the complete candidate palette.

## 8. A direction-density availability bound

There is a different positive bound that permits many source fibers.
Suppose the possible odd sources all have one residue modulo four
and lie on a partial row function \(a(x)\) satisfying
\[
                 |a(x)-a(x')|\le C\sqrt{|x-x'|}.       \tag{14}
\]
Consider a palette of \(K\) consecutive rows in one even residue class
modulo four, at column zero. Sources may lie both above and below it.

Fix one primitive Pythagorean direction with positive horizontal leg
\(u\) and positive odd vertical leg \(v\). Thus \(u\in4\mathbb Z\)
and \(v\ge3\). Use a signed integer scale \(t\ne0\), so a norm partner
in this direction has source column \(x=\pm u|t|\) and target row
\[
                            b=a(x)+vt.              \tag{15}
\]
The fixed source and target row residues require \(t\) to lie in one
residue class modulo four.

For one horizontal sign, let \(t_-,t_+\) be the least and greatest
signed scales that produce target rows in the palette, and set
\(d=t_+-t_-\). The source columns have distance
\(u\bigl||t_+|-|t_-|\bigr|\le ud\). Writing \(w=4(K-1)\),
(14)--(15) therefore give
\[
                   vd\le w+C\sqrt{ud}.
\]
Solving the quadratic inequality in \(\sqrt d\) yields
\[
 d\le {w\over v}
       +{2C\sqrt{uw}\over v^{3/2}}+{C^2u\over v^2}.
\]
Consequently this horizontal sign can forbid at most
\[
 {K\over v}+{C\sqrt{uK}\over v^{3/2}}
                   +{C^2u\over4v^2}+1
\]
rows. It is enough to count scales; repeated target rows only lower
the number of forbidden choices. Both signs together forbid at most
\[
             {2K\over v}+O_{C,u,v}(\sqrt K+1).        \tag{16}
\]

For a fixed finite set \(\mathcal D\) of such direction magnitudes,
the union therefore forbids at most
\[
      2K\sum_{(u,v)\in\mathcal D}{1\over v}
                       +O_{C,\mathcal D}(\sqrt K+1). \tag{17}
\]
If the actual-good choices outnumber this bound, a P-safe choice exists.
In particular, if all palette rows are actual-good and
\[
                     2\sum_{\mathcal D}{1\over v}<1,
\]
then every sufficiently large palette has a safe choice. For one
direction, at least \(K/3-O(\sqrt K)\) choices are norm-safe.
The two directions in Sections 2--3 have
\(2/3+2/5=16/15\), so (17) does not contradict that obstruction.

The signed-scale argument already includes both vertical signs.
Only the two horizontal signs contribute the leading factor two.
The constants in (17) are not uniform over a height-dependent
direction set.

For completeness, the same-parity geometry of a retuning can be
preserved by an already selected opposite-parity guard. If the row
index changes by at most \(K\), and there are no other selected even
points within \(6(K^2+1)\) fine ranks, the base bound
\(|\Delta z|^2\le q/16+1\) gives
\[
 |\Delta z_{\rm new}|^2\le q/8+2+2K^2\le q/2.
\]
Thus a safe choice supplied by (17) gives a genuine one-column P move
when all its possible P partners are in the stated direction set.
The guard must already be occupied by selected odd points. Creating
it, or controlling the other support families after retuning, still
requires a separate argument.

Independent written review: Sections 1--8 passed a separate full
check of both arithmetic families, the reflected periodic profile,
the four-band joins, white midpoint cells and owner scope, literal-good
averaging, the determinant divisibility, signed-scale direction counting,
and the guarded-retuning inequality. The review explicitly checked
that the result is not a sampled-cap embedding or a full repair theorem.
