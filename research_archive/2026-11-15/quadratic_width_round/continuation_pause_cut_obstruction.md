# A single Hilbert cut can forbid a quadratic-size pause menu

15 November 2026. Bounded pauses give more placement freedom than the
archived private choices x_r=S(Mr+xi_r). Their cumulative displacement
need not stay within a bounded distance of an affine clock. However,
repairing one cut while its two child traversals remain fixed does not
have a small universal forbidden-shift set.

The construction below blocks every pause k=0,...,q-1, where q is between
one quarter and one times the child area. It uses two Pythagorean norm
vectors and an elementary crossing argument. Every longer pause also
fails if its singleton rows come from either endpoint virtual pair.
Thus no length or singleton parity choices repair this cut with that
filler rule. New guard rows and simultaneous pauses inside the children
are outside the obstruction.

## 1. The elementary crossing lemma

Write H_a(t)=(x_t,y_t), 0<=t<a^2, for the ordinary Hilbert traversal of
a dyadic side-a square. Its first and last cells are(0,0) and(a-1,0),
and consecutive cells are nearest neighbors.

Fix any integer d with1<=d<=a^2. Pair the suffix and prefix indices

\[
 t=a^2-d+u,\qquad s=u,\qquad0\le u<d.
 \tag{1}
\]

The integer function f(u)=y_t-x_s starts nonnegative and ends
nonpositive. Its successive increments have absolute value at most2.
It therefore takes a value in{0,1}. If neither endpoint is zero, take
the last positive value before a sign crossing; it is at most1 unless
the next value is zero.

Only the endpoint and nearest-neighbor properties are used. No
monotonicity of f is assumed. A binary search preserving opposite signs
finds such a pair without enumerating the square.

## 2. Two neighboring vertical legs

Fix a power-of-two stride S>=128. There are arbitrarily large positive
integers Z,w such that

\[
 Z^2-3w^2=1,\qquad S\mid3w,\qquad Z=1\pmod8.
 \tag{2}
\]

For example, repeatedly square2+sqrt(3). Starting from the second
power, Z is odd, and each further squaring sends w to2Zw, increasing
its2-adic valuation by one. After enough squarings S divides3w, and
Z stays1 modulo8.

Put X=3w and q=X/S. The two exact norm identities are

\[
 X^2+(Z-2)^2=(2Z-1)^2,
 \qquad X^2+(Z+2)^2=(2Z+1)^2.
 \tag{3}
\]

Let a be the least dyadic integer with a^2>q. Then

\[
                         a^2/4\le q<a^2.
 \tag{4}
\]

The q here is a multiple of3, so it cannot be a power of4. All parameters
can be taken large enough that a=o(Z).

## 3. Every pause below q is forbidden

In an identity-oriented Hilbert parent square of side2a, its two middle
children have coordinates and ranks

\[
 (x_t,a+y_t),\quad a^2+t;
 \qquad (a+x_s,a+y_s),\quad2a^2+s.
 \tag{5}
\]

Use affine row lists with step4 and bases

\[
              A=5Z+2,\quad B=6Z,\quad h=8Z.
 \tag{6}
\]

All protected odd rows are3 modulo4 and above h/2. The even rows are2
modulo4. Their O(a) variation leaves fixed linear margins to the strip
boundaries.

Put the labels on columns Sr. At the cut between the two middle
children, insert k additional S-spaced columns, shifting the right
child and everything after it by Sk. Fix any0<=k<q and set d=q-k.
Choose t,s from the crossing lemma, so that a^2+s-t=d and
f=y_t-x_s belongs to{0,1}.

Take the even point in the left child and the odd point in the right
child. Their actual horizontal separation is

\[
 S(a^2+s-t+k)=Sq=X,
 \tag{7}
\]

while their even-minus-odd row difference is

\[
 B-A+4(y_t-x_s)=Z-2+4f.
 \tag{8}
\]

Thus one of (3) supplies an integral diagonal for every k in this
entire menu. There are q=Theta(a^2) forbidden pause lengths. In
particular, every O(a)-length menu is blocked for sufficiently large a.

The smaller half-factors are(Z+1)/2 when f=0 and(Z-1)/2 when f=1.
They are Theta(h), as are the original label own-row gaps. The paused
horizontal leg X is also Theta(h), with constants depending on S.
This obstruction is not removed by discarding only witnesses whose
own gap or half-factor is sublinear.

## 4. The in-strip alternatives and their owners

Let a_star=A+4(a+x_s) be the selected odd row and let b_star be the
selected even row. The alternative vertical pair has rows

\[
 a_\star-t_f,\quad b_\star+t_f,
 \qquad t_0=(Z+1)/2,\quad t_1=(Z-1)/2.
 \tag{9}
\]

For large parameters both rows lie between4Z and7Z. The odd one
remains above h/2, and the even one lies in the even pool. Their
residues are again odd3 and even2 modulo4. Hence their owner is a
required label of the same full physical profile.

Relative to the parent origin, that owner has row coordinates

\[
 \begin{cases}
 (a+x_s+3(Z-1)/8,\ a+x_s-3(Z-1)/8),&f=0,\\
 (a+x_s-(Z-1)/8,\ a+x_s+1+(Z-1)/8),&f=1.
 \end{cases}
 \tag{10}
\]

It is outside the protected parent because its coordinate displacement
has order Z, whereas the parent side is O(sqrt(Z)). In a full profile
placed by the same hierarchical order, its column is outside the
parent's contiguous interval. The common midpoint column lies between
the two selected endpoints, so it is different from the owner's column.

The tilted rectangle and the axis rectangle supplied by this owner
therefore have a symmetric difference consisting entirely of black
points. Their presentations agree regardless of any filling of the
two common corners. Adding singleton points at the cut cannot repair
the particular collision selected by (1).

An exact padded embedding is available. Choose N=8a4^m large compared
with Z. The address1,2 followed by2m zero-quadrants gives an
identity-oriented side2a parent with origin(I,J)=(N/4,3N/4).
Use the odd pool4Z+3,4Z+7,...,8Z-1 and the even pool2,6,...,8Z-2,
with offsets

\[
 U_0=I-(Z-1)/4,\qquad U_1=J-(3Z-1)/2.
 \tag{11}
\]

The parent and both owner forms (10) lie inside the corresponding
genuine rectangle for large parameters. Its cells retain their normal
Hilbert ranks, except for the one inserted pause.

## 5. Locality and the occupied pause

Increasing column separations preserves the existing same-parity
distance bound. A pause can repeat the virtual pair at the last label
of the left child and retain only its even point in each new arithmetic
slot. The last left and first right cells are adjacent and share the
same even row B+4a. Their odd rows differ by4. The repeated virtual
pair therefore preserves the same Hölder bound, and exactly one
occurrence of each genuine label remains a double.

This verifies occupancy and same-parity geometry on the coarse S-lattice.
It is not a proof for all filler triangles, mixed supports, six-cell
supports, or a particular interpolation at every fine4Z column.
The P obstruction survives any added filling that retains the displayed
endpoint points and their owner doubles.

There is a stronger failure of precisely this endpoint-pair filler rule.
The last left-child double and first right-child double have rows

\[
 (a_L,b_L)=(A+4(a-1),B+4a),\qquad
 (a_R,b_R)=(A+4a,B+4a).
 \tag{12}
\]

Their even row is common. The two possible row gaps are
b_L-a_L=Z+2 and b_L-a_R=Z-2. Suppose k>=q. The arithmetic slot exactly
Sq=X to the right of the last left double is one of the inserted slots.
If its singleton row is b_L, it forms the high-leg norm in (3) with
the odd point a_L of the left double. If its row is a_L or a_R, it
forms respectively the high-leg or low-leg norm with the even point
b_L of that double.

All three options therefore fail. Their common vertical alternatives
and owner rows are the same in-strip profile rows already checked in
Section4. The owner remains outside the expanded parent interval,
whereas the common midpoint lies inside the pause. This argument even
allows the pause to switch arbitrarily between the two endpoint pairs.

Combining this with Section3 proves:

**Endpoint-pause obstruction.** For these two frozen Hilbert children,
no nonnegative integer pause length k and no filling of its S-lattice
slots by singleton rows from{a_L,a_R,b_L} avoids P, provided the two
endpoint doubles and all required row-pair owners remain present.

It is enough to retain one actual pause point at the slot used in the
argument. Adding the other point cannot remove the collision.

The archived gap-mixing notes concern bounded private offsets in an
affine clock. They do not supply a cumulative-pause theorem. The present
obstruction is different: it saturates a whole cut-shift interval even
though that interval has Theta(child area) choices.

## 6. What this leaves open

Every genuine P vector has horizontal leg at most h-1. A guard of length
h therefore separates P pairs whose endpoints lie in different children.
At one critical scale with Theta(h) labels per child, there are Theta(h)
cuts and the total guard cost is O(h^2). But the preceding theorem shows
why repeating the endpoint virtual pairs does not provide the required
occupied guard: the guard itself supplies a new forbidden endpoint.

The missing part of that alternative is internal validity of each
critical-scale tile and a guard using additional admissible rows. Pauses at
several cuts inside a child change the suffix/prefix pairing in (1).
The sign crossing can then land on a singleton slot rather than on two
genuine doubles. No impossibility theorem for simultaneous hierarchical
pauses is asserted here.

## Review status

The [sparse checker](check_pause_cut_obstruction.py) and its
[certificate](check_pause_cut_obstruction.json) pass1,364 small crossing
cases,21 sparse short-pause cases, and36 long-pause filler cases,
including228 common-corner colorings. The large cases verify the actual global Hilbert cells,
owner ranks, physical pools, clock displacement, and both rectangles.
The full written proof passed an independent review, including the
all-length endpoint-pair filling obstruction and the genuine owners.
A separate reader imported the checker without rewriting its outputs
and reran all21 short-pause and36 long-pause cases successfully.
