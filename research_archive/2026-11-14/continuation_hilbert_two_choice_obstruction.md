# Two local choices do not repair the Hilbert placement

Date: 2026-11-14. Status: proved by the explicit five-label obstruction
below, with a separate exact finite check.

Consider the discrete Hilbert order and parity labels from
`continuation_hilbert_placement.md`. Let every rank independently choose
\[
x_r=32(2r+b_r),\qquad b_r\in\{0,1\}.                    \tag{1}
\]
Every such choice still excludes all same-parity nonhorizontal integral
distances. Nevertheless, no choice in (1) gives a valid full-label blackout
at height \(2048\), whatever filler sea is used.

The obstruction uses actual vertical completions inside the strip. It is
not an artifact of imposing the stronger condition \(L<h\) without the
boundary check.

## 1. Five labels

At height \(h=2048\), the label grid has side \(q=1024\). The following
five ranks have these Hilbert coordinates and rows:

| Name | Rank | Label \((i,j)\) | Odd row | Even row |
|---|---:|---:|---:|---:|
| \(A\) | 295029 | \((132,651)\) | 265 | 1304 |
| \(C\) | 295046 | \((139,649)\) | 279 | 1300 |
| \(D\) | 295047 | \((138,649)\) | 277 | 1300 |
| \(E\) | 295048 | \((138,650)\) | 277 | 1302 |
| \(H\) | 295065 | \((138,655)\) | 277 | 1312 |

Write their bits as \(b_A,b_C,b_D,b_E,b_H\). The following six bit
differences are forbidden by vertical rivals:

| Ranks | Forbidden later bit minus earlier bit | Horizontal gap | Vertical gap | Length | Completion rows |
|---|---:|---:|---:|---:|---:|
| \(A,C\) | 1 | 1120 | 1035 | 1525 | \(20,1545\) |
| \(A,D\) | -1 | 1120 | 1035 | 1525 | \(20,1545\) |
| \(C,D\) | 0 | 64 | 1023 | 1025 | \(276,1301\) |
| \(D,E\) | 0 | 64 | 1023 | 1025 | \(276,1301\) |
| \(D,H\) | -1 | 1120 | 1035 | 1525 | \(32,1557\) |
| \(E,H\) | 1 | 1120 | 1035 | 1525 | \(32,1557\) |

For the two short edges, use the even point of the earlier label and the
odd point of the later label. For the four long edges, use the odd point of
the earlier label and the even point of the later label.

The two identities are
\[
1120^2+1035^2=1525^2,\qquad
64^2+1023^2=1025^2.                                     \tag{2}
\]
For example, the rank gap from \(A\) to \(C\) is 17. If
\(b_C-b_A=1\), (1) gives the horizontal gap
\(32(2\cdot17+1)=1120\). The two rows are 265 and 1300, and their
vertical completion rows are
\((1565-1525)/2=20\) and \((1565+1525)/2=1545\).
Every other entry follows by the same calculation.

## 2. Each table entry is fatal

Each displayed completion consists of one even and one odd row inside
\([1,2048]\). The complete label set therefore contains the corresponding
row-pair label. It supplies an axis rectangle with the same presentation
as the tilted rectangle, unless that label were in the completion column.

That exception cannot occur here. In each long edge, the two bits differ,
so the midpoint column is congruent to 16 modulo 32. No label column in
(1) has this residue. In each short edge, the ranks are consecutive and
the bits agree. The midpoint lies strictly between their columns. The
ordering in (1) is strict, so no other label has that midpoint column.

More explicitly, the tilted rectangle has the two selected black label
points as one diagonal and the displayed vertical completion as the other.
The axis rectangle uses that vertical completion and the two black points
of its row-pair label. The symmetric difference is four black label points.
Thus the two rectangles have the same presentation regardless of any sea
points, or of the bit chosen for the row-pair label.

## 3. The six requirements are inconsistent

Avoiding the first two edges requires
\[
b_C\le b_A\le b_D.
\]
Avoiding the third requires \(b_C\ne b_D\). Hence
\(b_C=0\) and \(b_D=1\).

The fourth edge then forces \(b_E=0\). Avoiding the last two requires
\[
b_D\le b_H\le b_E,
\]
which reads \(1\le b_H\le0\). This is impossible.

The argument does not assume that any bits outside these five labels are
fixed. It excludes every assignment to the complete label set.

## 4. The obstruction recurs at larger powers of two

Under the Hilbert recursion, the third quadrant of the \(2q\)-square is an
unrotated copy of the \(q\)-square, translated by \((q,q)\), with a common
rank offset \(2q^2\). Thus all rank gaps in the table remain unchanged.
Every row, including each completion row, increases by \(2q\). The rows
remain inside the new strip of height \(4q\).

The five-label obstruction therefore embeds at every height
\(h=2048\cdot2^k\), \(k\ge0\). The fixed-stride, two-choice family (1)
cannot solve the quadratic construction for all heights.

## 5. Computation and scope

`hilbert_two_choice_rivals.py` reconstructs every opposite-parity pair that
can have integral length below \(h\), using integer factorizations of
\((X/2)^2\). By default, it also requires both vertical completion rows to
lie inside the strip. Each forbidden bit assignment becomes a 2-SAT
clause. The script solves the resulting implication graph and verifies
every recorded constraint for a satisfying assignment.

| Height | Labels | In-strip difference constraints | Clauses | Result |
|---:|---:|---:|---:|---|
| 512 | 65,536 | 4,726 | 4,726 | Satisfiable |
| 1,024 | 262,144 | 28,173 | 28,173 | Satisfiable |
| 2,048 | 1,048,576 | 163,060 | 184,999 | Unsatisfiable |

The results are in `hilbert_two_choice_rivals_in_strip.json`. The
satisfiable cases certify only avoidance of those rival pairs. They do not
certify complete blackouts.

An earlier run omitted the completion-row check. Its results are retained
in `hilbert_two_choice_rivals_check.json`. It also becomes unsatisfiable at
2048, but its first small core contains an out-of-strip completion. The
proof above uses the corrected, in-strip instance.

This obstruction is specific to two choices and stride 32. It does not
exclude three or more choices, different deterministic rank offsets, or
other space-filling orders. The Hilbert same-parity exclusion lemma remains
valid for all of them when the separation hypothesis is maintained.
