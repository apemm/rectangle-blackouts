# P propagation can disable every opposite-row cap option

15 November 2026. The movable two-corner cap menu is a geometric
extension, but its copied opposite-parity rows need not be usable in a
P-valid filling. A long forced barrier can propagate through both
constant side regions and force the entire cap to use its common row.

This is a local P obstruction to the menu. It is not an assertion that
every sampled cap, or any particular sampled cap in the current
construction, has the displayed row values.

## 1. A propagation criterion

Consider consecutive occupied lattice slots ell,...,u. At every slot
offer one common odd row A. On the left region ell,...,p also offer
an even row B_0. On the right region p+w+1,...,u offer an even row B_1.
The intervening w slots p+1,...,p+w have only A available.

Suppose the pair of row values (A,B_i), at lattice-slot separation q_i,
gives a genuine forbidden P pair for every pair of slots in this
interval at that separation. Both horizontal directions are included.
If

`w>=max(q_0,q_1)`,                                    (1)

then every P-valid singleton filling of this menu uses A at EVERY slot.

For the left region, the forced barrier contains a representative of
every residue modulo q_0. Starting from a forced odd point there and
stepping backwards by q_0, every preceding slot in the left region
must also be odd. Otherwise that even point and the already forced odd
point give a forbidden P pair. This covers the entire left region.
The same argument stepping forwards by q_1 covers the right region.

The conclusion is independent of p. Moving the barrier cannot make an
opposite-row option usable under (1). If the common role is even, the
same argument applies with the two roles reversed.

## 2. Exact in-strip P pairs in the constant row-one sea

Place core slots at columns 4r, and put row-one sea points at columns
not divisible by four. Let v be a positive integer and set

`t_0=12v^3+1`, `t_1=t_0+12v^2`,

`h=64t_0`, `A=36t_0+3`, `B_i=A+3t_i`.                (2)

The common row A is odd, 3 modulo four, and above h/2. Both B_i are
even, 2 modulo four. All three rows are in [1,h]. The t_i are odd.

An odd point at row A and an even point at row B_i separated by q_i=t_i
slots have displacement

`(4t_i,3t_i)`

and integral length 5t_i. Their vertical alternative corners lie at the
midpoint column and at rows

`A-t_i`, `A+4t_i`.                                   (3)

Both rows in (3) are strictly inside the strip. The lower row is above
one, and the upper row is at most A+4t_1<h. The midpoint column is
2 modulo four, so its only sea point is at row one. Thus both corners
in (3) are white, regardless of the singleton choices at core columns.

In a full balanced parity-label construction, the unordered row pair
in (3) has its axis owner elsewhere. The tilted rectangle and that axis
rectangle have the same two white corners. If a proposed final owner
were placed at that midpoint instead, the rectangle would be hidden.
In the stated sea model the midpoint is not a double column, so the
ordinary axis-owner alternative is the relevant one.

Therefore these are genuine P exclusions under the full-final-owner
condition, not merely formal integral norms. They apply equally when
the odd point is to the left or the right of the even point.

## 3. Compatibility with a long movable barrier

The opposite endpoint-row gap in (2) is

`g=B_1-B_0=36v^2`.                                   (4)

For any fixed Hölder constant C, the standard movable-barrier length

`w=ceil(g^2/(4C^2))-1`

eventually exceeds t_1, because it grows as a positive constant times
v^4 while t_1 grows as v^3. Choose the cap interval length large enough
that this barrier fits in its middle-half placement range and that
both side regions exist. Its required length is O_C(v^4), so the
horizontal interval remains subquadratic in h=Theta(v^3).

The three rows can all be declared good; the argument uses no bad-row
property. It tests the algebra of the menu after its good endpoints
have been supplied. Applying Section 1 forces every slot of this menu
to choose A, at every allowed barrier position.

## 4. Scope for the repair problem

The menu still contains the constant-A filling, so this is not an
intrinsic impossibility of filling that interval. It shows that adding
good opposite-parity options does not ensure that they can cut a forced
P path or erase a marked common-row point. The P implications can
propagate across the entire copied-row region.

The exact row triple in (2) has not been embedded as a selected random
cap of the current mechanical or multiscale scaffold. No statement
about every cap arrangement, every offset choice, or a complete-board
threshold follows from this local example.

An effective repair theorem must exploit more than the existence and
mobility of the two copied opposite endpoint rows. It may need other
row options, or a property of the actual cap endpoint pairs that excludes
the propagation criterion (1).

Independent review: the complete saved statement passed a separate
written review. The residue propagation, in-strip 3--4--5 witnesses,
white midpoint rows, final-owner condition, and barrier scaling were
checked. No sampled-cap embedding is asserted.
