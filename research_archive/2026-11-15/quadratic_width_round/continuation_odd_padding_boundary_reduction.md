# Odd padding localizes its P targets to the genuine boundary

15 November 2026. Choosing odd virtual options on padding ranks gives a
useful geometric reduction. Its P edges to genuine doubles can be erased
at subquadratic internal relocation cost. The reduction leaves explicit
singleton-to-singleton constraints and does not solve occupancy repair.

## 1. A boundary strip contains every genuine target

Embed the genuine coordinate rectangle of side lengths \(\Theta(h)\)
inside a padded Hilbert square of side \(N=\Theta(h)\). Call a rank
padding if its raw coordinate lies outside that genuine rectangle. Use
the existing good virtual options, and prefer odd on padding whenever
its odd option is good. This is a choice among existing rows, not insertion
of a new constant row.

An actual in-strip P event has hypotenuse at most \(h-1\), so its
horizontal separation is at most \(h-1\). At any fixed stride \(S\),
its rank separation is at most \((h-1)/S\). Raw Hilbert locality then
puts the two raw coordinate cells within \(C\sqrt h\) in each coordinate.

If one endpoint is a padding rank and the other is genuine, the genuine
cell is therefore in a boundary strip of width \(C\sqrt h\) around
the genuine rectangle. This strip has at most \(O(h^{3/2})\) cells.
The argument is unaffected by changes of a padding row to an existing cap
option: it uses raw rank geometry and the actual in-strip condition only.
Fixed-size object permutations add only a fixed error to the rank bound.

Erase the even point of every surviving genuine double in this strip,
retain its odd point, and relocate its complete pair. This removes all P
events from odd padding to those double targets. It requires at most
\(O(h^{3/2})\) conversions, hence \(h^{3/2+o(1)}\) internal width
under the cited subpolynomial relocation factor. Every converted slot
remains occupied.

## 2. Forced even padding and the repeated-row family

Under odd preference, padding is forced to remain even only where its
virtual odd value is bad. The total virtual palette bound gives at most
\(Nb_0=O(hb_0)\) such ranks, where \(b_0\) is the number of bad
odd rows. In particular this is \(h^{11/6+o(1)}\) under the current
R2s bad-row estimate.

For the repeated even-row one-label/two-sea family, each such even point
has degree \(h^{o(1)}\), by
[`continuation_repeated_even_row_six.md`](continuation_repeated_even_row_six.md).
Converting every adjacent surviving genuine double to its odd stub
therefore costs at most \(h^{11/6+o(1)}\) labels. This removes the
forced-padding-to-double part of that family.

These two operations are erasures of existing even points. They preserve
the geometric bounds and cannot add a support inside the old black set.
They can change which remaining points are treated as exceptional odd
sources in later counting arguments, which must be tracked explicitly.

## 3. The remaining qualifications

The boundary operation cannot erase an even-only target left by an earlier
odd-point cleanup without emptying that slot. P events from odd padding
to such even singletons therefore remain. Restoring their odd point and
swapping parity would be a new insertion, outside the erasure argument.

Likewise, an edge of the repeated-row family between two forced even
singletons remains. The small number of these stubs and their small
individual degree do not make that occupancy constraint satisfiable.
The finite-menu obstruction in the linked note applies to a direct
bounded-gap remedy.

For a converted genuine double that previously passed uniform own-gap
and half-factor filters, its original even mate can still be retained as
a counterfactual coordinate. The prior same-parity bounds against every
surviving even point remain valid after its erasure. Thus the old
long-gap conclusion for its retained odd point can continue to hold.
This does not apply automatically to a genuine label whose odd point
had already been removed, nor to arbitrary padding or cap sources.

The geometry localizes targets of actual P only. It does not cover the
larger out-of-strip norm graph, and it does not remove the remaining
multi-label mixed and six-cell families. The conclusion is a padding
orientation reduction with two explicit residual singleton problems,
not a completed quadratic construction.

## Review status

The full written reduction was independently reviewed on 15 November 2026.
The review checked raw-rank boundary localization, the forced-even count,
and the two conversions. The already-singleton exceptions remain part of
the statement. No correction was needed.
