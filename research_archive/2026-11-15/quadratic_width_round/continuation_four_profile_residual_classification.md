# Residual collision families for the four low two-row profiles

15 November 2026. Independently reviewed in full. This is a conditional classification for the profiles in
[the four-profile theorem](continuation_four_low_sea_profiles.md). It
does not construct a valid core or a collar. In particular, parked
triangles must be compared with each other; one-label validity does not
make their union valid.

## 1. Hypotheses and the three admitted sea-mediated triangles

Fix one of \((L,F)=(1,2),(1,4),(3,6),(3,8)\). Odd columns carry
row \(L\); columns \(2\pmod4\) carry row \(F\). Inserted columns
are divisible by four and have at most one point of each row parity.
Every inserted row exceeds \(2F\), and
\[
 a\equiv L+2\pmod4,\qquad b\equiv F+2\pmod4               \tag{1}
\]
for odd and even inserted rows. Actual doubles are distinct opposite-parity
row pairs. Singletons and empty inserted slots are allowed in this
classification. Occupying every slot is a separate counting requirement.

The four-profile theorem excludes a tilted right triangle with one odd
and one even inserted point and one sea point. It also describes all
triangles using at most one inserted point. Thus, apart from three
inserted corners, an admitted tilted black right triangle has one of
the following types.

1. **One even inserted point, two sea points.** Its right angle is at
   the \(F\) point. Its completion is at an odd sea column, with row
   \(b+L-F>L\).
2. **Two same-parity inserted points, label right angle.** Write the
   inserted side as \((X,\delta)\), with \(X\in4\mathbb Z\).
   If the sea point has row \(s\), the completion is its translate by
   \((X,\delta)\). It remains in the same sea-column residue, and
   \(\delta\in4\mathbb Z\setminus\{0\}\). It is therefore white
   and has the same row parity as the selected sea point.
3. **Two even inserted points, sea right angle.** The sea point must
   be at row \(F\). The completion has column \(2\pmod4\) and row
   \(b_1+b_2-F>F\), congruent to \(F\pmod4\).

For the second type, \(\delta=0\) would make the inserted side
horizontal and force the sea point into the inserted column, impossible.
For the third type, a right angle at an \(L\) point with two even
labels has dot product \(2\pmod4\); two odd labels give an odd dot
product at either sea type. The stated \(F\)/even case is the only one
left.

Every completion in this list is an ordinary sea column. It has the
same row parity as the black sea point already there. Thus no such
completion has an opposite-parity axis owner, and no completion falls
in an empty arithmetic slot. There is no FW-to-hole case for these
three families. This does not make repeated completions harmless.

If all tilted three-inserted-point right angles are excluded, there is
also no hidden tilted rectangle. A hidden rectangle with sea points
would contain one of the listed triples and would have its fourth
corner at the white sea completion just identified.

## 2. The mixed four-point sieve

Normalize column residues as
\[
 O=(0,a),\quad E=(0,b),\quad
 L_*=(\text{odd},L),\quad F_*=(2,F)\pmod4.
\]
Under (1), squared lengths have the following residues modulo sixteen:
\[
\begin{array}{c|c}
\text{endpoint types}&\text{squared length}\\ \hline
OO,\ EE&0\\
OE&1\text{ or }9\\
O L_*,\ O F_*&5\text{ or }13\\
E L_*&2\text{ or }10\\
E F_*&8\\
L_*F_*&2\text{ or }10 .
\end{array}                                             \tag{2}
\]
A mixed side/diagonal presentation requires equal black-pair lengths.

Consequently no mixed support uses exactly one sea point and three
inserted points. A support with two inserted points and two sea points
must use same-parity inserted points. The one-inserted-point cases are
already excluded by the four-profile theorem, including when a common
rectangle corner becomes black elsewhere: collision containment depends
only on the symmetric difference.

First suppose the inserted points form one whole black pair and the
sea points the other. Norm residues force the sea pair to be horizontal.
This grouped case is excluded by either of the following additional
hypotheses.

* Every nonhorizontal same-parity inserted pair has nonintegral
  Euclidean length. The horizontal sea pair then forces
  \(\Delta y=0\), and the resulting two horizontal pairs make the
  alternative presentation degenerate. The strict bound
  \((\Delta y)^2<2|\Delta x|\) is one sufficient condition. The
  [spacing-four refinement](continuation_step_four_refinement.md)
  also supplies precisely the needed conclusion, including its isolated
  slope-\(\pm1\) seam pairs.
* Within each parity, inserted rows have one fixed residue modulo
  \(32\). If they form the black side and have nonzero vertical gap,
  the lower common white row is at most \(F-16<1\). If they form the
  black diagonal, put \(X=\Delta x\), \(Y=\Delta y\), and let
  \(V\) be the sea-side horizontal length. Then
  \(V^2=X^2+Y^2\), \(4\mid X\), \(32\mid Y\).
  Hence \(4\mid V\), and division by sixteen modulo two gives
  \(V\equiv X\pmod8\). The common horizontal white pair has columns
  \((x_1+x_2\pm V)/2\), both divisible by four. Those columns must
  also be the sea black-side columns, a contradiction. Zero vertical
  gap again degenerates.

It remains to consider crossed pairs, each consisting of one inserted
point and one sea point. For even inserted points, (2) prevents the two
sea levels from differing. For odd inserted points and different sea
levels, orient the side from an odd label to the \(L\) point and the
diagonal from another odd label to the \(F\) point. Modulo four,
\[
 U=(\ell,2),\qquad C+D-A-B=(2-\ell,F-L),\quad \ell\text{ odd}.
\]
Their dot product is
\(\ell(2-\ell)+2(F-L)\equiv3\pmod4\), contradicting
perpendicularity. Reversing which sea level is on the side gives the
same nonzero obstruction.

Thus the only two-inserted/two-sea mixed family left is:

> Two same-parity inserted points and two sea points at the same
> actual row, with both black pairs crossed.

This is the same-sea crossed family; it is not automatically excluded
by the residue sieve or by full occupancy. Its incidence or row-removal
bounds require their own geometric hypotheses.

## 3. A sufficient residual list

Assume one of the grouped-pair exclusions in Section 2. For an internal
one-profile core, every collision is prevented if the following are
excluded:

* tilted right angles on three inserted points;
* mixed four-inserted-point supports, including the vertical-side P
  case when appropriate;
* crossed same-parity two-inserted/two-same-sea supports;
* two distinct triples from Section 1 with the same completion and
  six distinct black points.

If the full final parity-pair graph is present elsewhere, the vertical-side
P case can equivalently be imposed as the usual in-strip opposite-parity
integral-diagonal condition, with its remote axis owner. Removing this
family requires that actual owner hypothesis when asserting necessity.

Here is why the list is sufficient. Two-white collisions of the same
kind (diagonal/diagonal or side/side) force a hidden black rectangle.
Mixed collisions are covered by Section 2. Two rectangles with a common
singleton completion and a shared black corner give a four-point
symmetric-difference support, hence reduce to the preceding cases.
If they share no black corner, their six black points are distinct.

Axis rectangles have no hidden or repeated presentations when the
actual doubles are distinct opposite-parity edges. For a singleton
presentation, the unique opposite-parity partner at its column and its
unique double owner determine the axis rectangle. A tilted completion
from Section 1 cannot match it, because the sea point at that completion
has the same row parity. The remaining all-inserted tilted triples were
excluded explicitly. Three common white corners determine a rectangle.

The six-point entry is genuinely broader than the old label-vertex PT
family. Type 1 can meet type 1 or type 2 at an \(L\)-column completion.
Type 2 at an \(F\)-column can meet type 2 or type 3; type 3 can meet
type 3. In particular, there are six-point families with two inserted
points and four sea points, with three inserted points and three sea
points, and with four inserted points and two sea points.

The classification does not supply a collar theorem, an occupancy rule
for a sparse core, or a simultaneous solution of these residual systems.

## 4. Every bulk even row has a two-inserted/four-sea obstruction

The first six-point family already prevents long constant-even-row
fillings. Fix an eligible bulk row \(b\), and set
\[
 C=(F-L)(b-F)=2n.
\]
Here \(n>1\) is odd: \(F-L\) is odd, \(b-F\equiv2\pmod4\),
and \(b>2F\). Choose \(e\in\{1,-1\}\) with \(en\equiv1\pmod4\).
At
\[
 W=(1,b+L-F)
\]
take the two divisor pairs
\[
 (u,v)=(1,2n),\qquad (u,v)=(en,2e).
\]
For either pair, the three black points are
\[
 E_u=(1-u,b),\qquad
 F_u=(1-u-v,F),\qquad L_u=(1-v,L).                        \tag{3}
\]
The sea point \(F_u\) is the right-angle vertex:
\[
 (E_u-F_u)\cdot(L_u-F_u)
 =uv+(b-F)(L-F)=0.
\]
The fourth corner is \(W\). Both \(E_u\) columns are divisible by
four, both \(F_u\) columns are \(2\pmod4\), and both \(L_u\)
columns are odd. The two inserted points are distinct, and so are the
two sea points at each level. Indeed equality of the two \(F_u\)
columns would require \(u_1u_2=C\), impossible since the left side
is odd and the right side is even. Thus this is a genuine six-black
collision, not a duplicated presentation of one rectangle.

The two inserted columns have gap \(n-1\) or \(n+1\), and the entire
witness has span \(O_{L,F}(b)\). Every row lies in the strip whenever
\(b\le h\), since \(0<b+L-F<b\). A horizontal translation by a multiple
of four preserves the profile.

This applies to singleton stubs as well as even endpoints of doubles.
It is not an assertion that the two required positions occur in a
particular Hilbert or random-cap order. It does show that full occupancy
and a constant even-row plateau do not, by themselves, provide a valid
filler for these seas. The failure can occur for \(b\) near the top of
the strip, where the separate type-3 completion \(2b-F\) lies outside
the strip.

## 5. A fixed-gap trap for repeated even rows

More generally, two odd divisors \(u,u+d\) of \(C\), with \(4\mid d\),
produce the same collision from (3), with the two even inserted columns
separated by \(d\). Translate the formulas so these columns are
\(0,-d\); the common white column is then \(u\). Taking \(u=1\)
shows that the collision occurs whenever
\[
 1+d\mid (b-F)/2.                                       \tag{4}
\]
For \((L,F)=(1,2)\) and adjacent inserted slots \(d=4\), this
includes every \(b\equiv12\pmod{20}\). Thus repeating an even virtual
value at consecutive fine slots is not automatically safe, even when
that value is close to the top of the strip.

There is also a finite-palette limitation. Fix \(4\mid d>0\) and
finitely many profiles \((L_i,F_i)\) compatible with one even residue
\(b\equiv\beta\pmod4\), so \(F_i\equiv\beta-2\pmod4\).
There are infinitely many such \(b\) for which a repeated pair of even
row \(b\) at columns \(0,-d\) is bad in every one of these profiles.

Choose positive \(u_i\equiv1\pmod4\) so the odd integers
\(r_i=u_i(u_i+d)\) are pairwise coprime. At each step avoid residues
\(0,-d\) modulo every odd prime dividing the preceding \(r_j\),
and choose \(u_i\) coprime to \(d\). Each prime has at least one
allowed residue; the Chinese remainder theorem supplies a positive
choice. Now impose
\[
 b\equiv\beta\pmod4,\qquad b\equiv F_i\pmod{r_i}
 \quad\text{for all }i.                                 \tag{5}
\]
The moduli are coprime, so arbitrarily large solutions exist. In profile
\(i\), both \(u_i,u_i+d\) divide \((F_i-L_i)(b-F_i)\), which has
valuation one at two. Their complementary divisors are therefore
\(2\pmod4\), as the sea positions require. Formula (3) supplies the
collision in each profile. For large \(b\), all rows are positive and
at most \(b\).

This does not prevent rearranging the repeated points, using an available
odd stub instead, or changing the background beyond this finite family.
It rules out repairing an arbitrary fixed-gap repeated even pair solely
by choosing from a fixed finite list of these seas.


