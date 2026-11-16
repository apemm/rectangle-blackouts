# A global Pell crossing forces P in a continuous full-square order

15 November 2026. A nearest-neighbor order of a complete affine label
square cannot avoid every long P constraint while retaining uniform
square-root locality and constant column stride. Two neighboring Pell
norm heights cannot both be skipped by the sliding cross-row difference.

This does not require adjacent-corner endpoints or a specified quadrant
orientation. It does require every visited label in the protected square
to remain a double. Point erasures, optional singleton parities, and
nonconstant column clocks can break the argument.

## 1. Two close norm heights

Fix a column stride S divisible by four and a locality constant C.
Choose infinitely many positive Pell solutions

    Z^2-3w^2=1,    Z=1 modulo four,    S divides w.        (1)

Such a sequence exists elementarily. The matrix
[[2,3],[1,2]] is invertible modulo 4S and therefore has finite order
there. A suitable positive power of 2+sqrt(3), and every further
multiple of that power, gives (Z,w)=(1,0) modulo 4S.

Put X=3w and q=X/S. Then

    X^2+(Z-2)^2=(2Z-1)^2,
    X^2+(Z+2)^2=(2Z+1)^2.                               (2)

The two positive heights differ by four. Their smaller half-factors
are respectively (Z+1)/2 and (Z-1)/2.

Let n be the largest power of two at most Z, and let h=16Z.
For large solutions of (1), n is comparable to Z, q is comparable
to Z with an S-dependent constant, and n/sqrt(q) tends to infinity.

## 2. A complete affine profile

Consider the n-by-n labels (i,j), 0<=i,j<n, with rows

    a_i=A+4i,    b_j=B+4j,
    A=8Z+3,     B=7Z+1.                                 (3)

All odd rows are 3 modulo four and lie above h/2. All even rows
are 0 modulo four. Every row lies strictly in [1,h].

Let (i_r,j_r), 0<=r<n^2, be ANY bijective traversal of this square
such that consecutive cells are lattice neighbors and

    max(|i_r-i_s|,|j_r-j_s|) <= C sqrt(|r-s|).             (4)

Place each complete label at column Sr, allowing an overall
horizontal translation. In particular both its row points are black.

Standard continuous hierarchical Hilbert traversals satisfy (4)
with C=4, uniformly over their compatible recursive orientations.
If S>8C^2, then every nonhorizontal same-parity black pair has
nonintegral Euclidean distance. For the strict Hilbert estimate
C=4, S=128 also suffices. Thus the obstruction is compatible with
the usual same-parity exclusion.

## 3. The sliding difference has a forced crossing

For 0<=r<n^2-q, define the integer

    g(r)=j_(r+q)-i_r.                                    (5)

Nearest-neighbor traversal gives

    |g(r+1)-g(r)|<=2.                                    (6)

There is a rank r_- with g(r_-)<0 and a rank r_+ with
g(r_+)>=2. To see this, take the bottom-right and top-left quarter
boxes

    B_-: i>=3n/4, j<n/4,
    B_+: i<n/4, j>=3n/4.

Each contains n^2/16>q labels for sufficiently large Z. Hence each
contains a label whose rank is before the final q positions.
For its rank r, locality gives |j_(r+q)-j_r|<=C sqrt(q).
Consequently

    g(r) <= -n/2-1+C sqrt(q) <0  on B_-,
    g(r) >=  n/2+1-C sqrt(q) >=2 on B_+.

Traverse the rank interval between r_- and r_+. An integer sequence
with steps of magnitude at most two cannot pass from values at most
-1 to values at least two without hitting zero or one. Thus some r
satisfies

    g(r)=0 or 1.                                         (7)

The directed cross-row difference at that pair is

    b_(j_(r+q))-a_(i_r)
       = -Z-2+4g(r).

It is -(Z+2) in the first case and -(Z-2) in the second. The
horizontal distance is exactly X=Sq, so (2) gives an integral norm.

The endpoint values in (3) are not tuned to a particular orientation
or to the traversal's first and last corners. The argument uses the
full-square coverage and the sliding bounded-step crossing.

## 4. The constraint is an actual in-strip collision

Write a=a_(i_r), b=b_(j_(r+q)), and let L=2Z+1 or 2Z-1
as appropriate. The alternative vertical pair is at the midpoint
column and at rows

    (a+b-L)/2,    (a+b+L)/2.                              (8)

The rows are integers because a+b and L are odd. Their difference
L is odd, so they have opposite parity.

The black-row ranges in (3) give

    8Z+3 <= a <=12Z-1,
    7Z+1 <= b <=11Z-3.

It follows that both rows in (8) lie strictly between 1 and h=16Z.
The midpoint column is integral, since X is divisible by four.

Under the full-final-parity-owner condition, the row pair (8) has
its axis owner. If that owner is at the midpoint, the tilted rectangle
is hidden. Otherwise the tilted rectangle and the owner's axis
rectangle have black symmetric difference and equal presentations,
regardless of the common corners' colors. The owner may belong to
another profile; membership in this particular upper-odd square is
not required and is not asserted.

The horizontal span, norm, and both half-factors in (2) are Theta(h).
The own-row gaps of the two endpoint labels are also large. Indeed
(4) changes the even or odd row by only O(sqrt(q)) between these
two ranks, so each own gap is

    -Z+O_C(sqrt(q)).

Its magnitude is at least Z/2 for large solutions. The event therefore
survives tests based only on its own near-linear span, half-factor,
and own-row gap. Deletion for a different small-factor event remains
outside this conclusion.

## 5. Scope for column-clock choices

The protected square occupies width S(n^2-1)=O_S(h^2).
It can also be embedded as a genuine aligned square in a padded
profile by translating the two raw coordinate offsets. No particular
recursive orientation is used in the proof.

This proves a structural obstruction for a constant-stride, full-double
continuous order. It does not say that a cap-filled or interpolated
scaffold has an actual P pair: there the two virtual points found
in (7) may not both be selected black points. A permutation that
breaks the unit-step condition can also skip both norm heights.

For a nonconstant column clock, the horizontal distance between r and
r+q varies with r. Equations (2) then no longer describe one fixed
forbidden pair of heights. This is a genuine additional freedom,
rather than a case covered by the crossing proof.

The theorem gives no general lower bound on quadratic-width
constructions and no assertion that the complete filtered scaffold
must contain the displayed square of retained doubles.

## 6. Sparse exact verification

The companion checker constructs Pell solutions with the required
congruences. It uses forward and inverse Hilbert maps only at queried
ranks, locates a crossing by bisection of opposite-sign values of (5),
and checks the exact norm, own gaps, in-strip alternatives, both
rectangle presentations, and every coloring of the common pair.

The saved run contains four exact cases at S=128 and S=256.
It performs 2168 gap evaluations during the sparse bisections, rather
than enumerating the very large boards.

Files:
[checker](check_global_pell_crossing_obstruction.py) and
[certificate](check_global_pell_crossing_obstruction.json).

Independent written review passed on 15 November 2026. A separate
import-based rerun, without rewriting the certificate, passed all four
cases and 2168 gap evaluations.

