# A guarded third-row P move and its finite-palette limitation

15 November 2026. Changing a singleton's row within its existing parity
can cut an incoming P constraint without passing that constraint along
a parity implication path. There is a precise guarded one-source move.
There is also an occupied constant-sea configuration that defeats every
choice from any fixed finite same-parity row palette. Thus three rows
are useful locally, but are not a uniform P-choice theorem.

The obstruction below uses actual-good rows and long P pairs. It is
not claimed to occur in the sampled cap model.

## 1. One source cannot forbid three consecutive profile rows

Fix a nonzero horizontal displacement \(X\in4\mathbb Z\), an odd source
row \(a\), and three even candidate rows \(b-4,b,b+4\). At least one
of the three distances from \((X,a)\) to these candidates at column
zero is nonintegral.

Indeed, their signed vertical displacements are three consecutive terms
of an odd progression with step four. If they have both signs, one
has absolute value one, and \(X^2+1\) is not a square. Otherwise
reverse their order and signs if necessary, writing them as
\(Y,Y+4,Y+8>0\).

If all three lengths \(L_0,L_1,L_2\) were integers, they would be odd.
Strict monotonicity and
\[
 0<\sqrt{X^2+(Y+4)^2}-\sqrt{X^2+Y^2}<4
\]
force both successive length increments to equal two. But the second
difference of \(L_j^2\) would then be eight, while that of
\((Y+4j)^2\) is thirty-two. This contradicts
\(L_j^2-(Y+4j)^2=X^2\).

The conclusion also handles two sources at the same row and the same
absolute horizontal distance: they impose the same norm condition.
It does not bound the union of constraints from different norm fibers.

## 2. A concrete one-column move

Use the fine-grid geometry from
[the multi-anchor compatibility theorem](continuation_fine_multi_anchor_compatibility.md).
Its selected row-index values satisfy the global bound
\[
             |z(r)-z(s)|^2\le |r-s|/16+1             \tag{1}
\]
within either parity, as well as the stronger square bound except at
the old isolated unit seams.

Suppose an even singleton at fine rank \(r\) has row \(b\), and:

1. The three rows \(b-4,b,b+4\) are all actual-good and stay in the
   required profile pool.
2. Every rank \(s\) with \(0<|s-r|\le11\) is already occupied by
   an odd singleton. There are no even points in this guard.
3. All possible opposite-parity integral-distance partners of the three
   choices belong to one norm fiber \((|X|,a)\).

The first condition can be checked directly; it is not inferred from
the single-row good-family theorem. In particular, a buffered-good
interior row supplies it. The second condition concerns actual selected
points, not just availability of an odd option.

Choose a row among the three that avoids the fiber, using Section 1,
and replace the singleton by that row. Occupancy, width, and the complete
double-label list are unchanged.

For the changed even point and any other even point, \(q=|r-s|\ge12\).
Its index value changes by at most one. Thus (1) gives
\[
 |z_{\rm new}(r)-z(s)|^2
       \le 2|z(r)-z(s)|^2+2
       \le q/8+4\le q/2.                              \tag{2}
\]
All other same-parity pairs are unchanged. The move therefore introduces
no new unit seam, same-parity integral distance, same-parity right
triangle, or same-parity mixed support. It removes every P incident
to this singleton under condition 3 and changes no other P pair.

This is an actual P repair when the initial P failures are precisely
those incident pairs. It does not change the target's parity and hence
does not merely propagate a binary implication. Any new three-point,
four-point, or parked-six support must contain the new point; these
must still be excluded, for example by compiling all three row choices
before making the move.

If the guard was not already odd, one may instead use a common odd
cap row only when that filling has separately been proved compatible
with the outside same-parity geometry. Even then, the newly selected
odd points can create outgoing P constraints. That variant is not
asserted to be a local P repair.

## 3. A flat occupied background can defeat any fixed finite palette

Fix distinct integers \(e_1<\cdots<e_K\), independently of height.
For all sufficiently large \(h\), there are rows \(A,b\) such that
the following holds.

Fill a local constant-sea strip by row one at every column outside
\(4\mathbb Z\), and by the same odd row \(A\) at every arithmetic
column, except that column zero is to receive one even row from
\[
                         b+4e_1,\ldots,b+4e_K.        \tag{3}
\]
Every one of these choices creates an in-strip P diagonal with one
of the fixed odd background points. Both common corners are white
in the specified occupied background. If all required opposite-parity
row-pair owners are retained somewhere in the completed board, this
is an immutable rectangle-presentation collision.

Moreover, \(A\) and every row in (3) may be required to avoid any
given actual forbidden row sets of cardinality \(o(h)\), in their
respective fixed profile residues. All the constructed horizontal
legs and smaller half-factors are \(\Theta_K(h)\).

### Construction

Choose distinct odd primes
\[
                  p_1<\cdots<p_K,\qquad p_j\equiv3\pmod4.
\]
Let \(P=\prod_jp_j\), and choose a sufficiently small constant
\(c>0\), depending only on this finite prime list and the offsets.
First choose an actual-good row
\[
       .70h\le A\le .71h,\qquad A\equiv3\pmod4.
\]
There are \(\Theta(h)\) possible rows and only \(o(h)\) exclusions.

Choose \(Y\in[ch,2ch]\) in the fixed progression
\[
          Y\equiv3\pmod4,\qquad
          Y\equiv-4e_j\pmod{p_j}\quad(1\le j\le K).    \tag{4}
\]
Put \(b=A+Y\). The progression has a fixed modulus \(4P\), so it
has \(\Theta_K(h)\) candidates. Requiring each \(b+4e_j\) to
be actual-good removes only \(K\,o(h)\) candidates. Hence \(Y\)
can satisfy all these requirements.

Write
\[
 Y_j=Y+4e_j=p_jg_j,\qquad
 X_j=\frac{p_j^2-1}{2}g_j,\qquad
 L_j=\frac{p_j^2+1}{2}g_j.                             \tag{5}
\]
For large \(h\), every \(g_j\) is positive and odd. These are
integer Pythagorean triples, and \(X_j\in4\mathbb Z\).
The fixed odd point
\[
                        (-X_j,A)
\]
and the choice \((0,b+4e_j)\) have precisely this norm.
The \(X_j\)'s are distinct: their coefficients
\((p_j^2-1)/(2p_j)\) strictly increase with \(j\), as do \(Y_j\).

Its smaller half-factor is
\[
            t_j=(L_j-Y_j)/2=\frac{(p_j-1)^2}{4}g_j.    \tag{6}
\]
Since \(Y_j\equiv3\pmod4\), \(p_j\equiv3\pmod4\), and
\(g_j\equiv1\pmod4\), one has \(t_j\equiv1\pmod4\).
The common vertical pair is at column \(-X_j/2\), in rows
\[
                       A-t_j,\qquad A+Y_j+t_j.        \tag{7}
\]
For \(c\) small enough, uniformly over this fixed finite list,
\[
 X_j<h/10,\qquad t_j<h/20,\qquad 0<Y_j<h/20.
\]
Thus both rows in (7) lie in the strip; their odd member is above
\(h/2\), and the even member has the required residue two modulo four.
Both are distinct from \(A\).

The midpoint column is even. If it is \(2\pmod4\), its sole black
point is sea row one, so both cells in (7) are white. If it is
\(0\pmod4\), it is a nonzero arithmetic column carrying only row
\(A\), so both cells are again white. The target choice is at column
zero and cannot alter these cells.

Take the local interval long enough to contain all source and midpoint
columns. A common translation by a multiple of four can make them
positive. Every column of this interval is occupied. The background
odd row is constant, and there is only one selected even point, so
the partial same-parity square-root geometry is automatic. The usual
full-family axis owner for the row pair (7) may lie elsewhere in the
board; it need not belong to this local strip.

The constants in (5)--(6) are positive and fixed, while \(Y\asymp_K h\).
Thus each specified leg and half-factor is \(\Theta_K(h)\). The
obstruction is not removed by its own short-gap or small-factor size.
No survival under every other deletion rule is claimed.

## 4. Consequence for a third-row strategy

Section 2 is a useful local move when its guard and single-fiber
conditions are known. Section 3 shows why adding any fixed finite
number of same-parity row alternatives cannot by itself give a
uniform repair theorem, even in an occupied flat background with
actual-good rows.

This does not exclude a growing palette, changing the surrounding
points, choosing a different parity, or a coupled block permutation.
It also does not embed the obstruction into a sampled multi-anchor cap.
To use third-row changes globally, one still needs a structural bound
on the distinct incoming norm fibers or a coupled geometric move.
Those are additional requirements, not consequences of short-cycle
deletion or of the good-row gap theorem.

Independent written review: the complete note passed a separate check
of the mixed-sign norm argument, guarded geometry, fixed-prime CRT
construction, actual-good row exclusions, and common white cells.
The distinction between an already selected guard and a separately
validated cap filling was checked explicitly.
