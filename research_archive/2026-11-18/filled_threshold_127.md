# A filled optimal board at height 127

Let \(M=1{,}507{,}048\). The certificates below give
\[
 f(127,m)=m+4032,\qquad
 a_{127}(m)\ \ge\ 2^{m-M}\binom{m-M+27}{27}
 \qquad(m\ge M).
\]
Here \(4032=64\cdot63\). The size follows from the rectangle-blackout upper bound \(f(h,m)\le m+\lfloor h^2/4\rfloor\) and a board with one black cell in each column and one extra black cell for each opposite-parity row pair. \(M\) is an upper bound for the first width at which equality persists.

## The 27 windows

Start with the translated 127-row double assignment in [the coordinate certificate](fiber_search_127_96_186.json). The labels have 23 occupied congruence groups. Nineteen groups use one window each. In the remaining four groups, divide the labels by their parity of rank in increasing column order. Each of these eight smaller groups uses one window. The windows keep the original column differences of their own doubles.

Each window uses one singleton in every other column, from one of the palettes \(\{1,122\}\), \(\{1,124\}\), \(\{1,126\}\), \(\{2,127\}\). The palettes and the individual choices are part of the certificate. The 19 full-group windows and the eight split-group windows are stored separately. [Full groups](phase_127_filled_windows.json) · [Split groups](phase_127_remaining_windows.json)

For height \(h\), put \(W=1+\lfloor(h-1)^2/4\rfloor\). Every tilted rectangle has horizontal span at most \(W\). Its two nonzero horizontal leg magnitudes \(u,v\) satisfy \(uv\le(h-1)^2/4\), since perpendicularity identifies their product with that of the two vertical leg magnitudes, whose sum is at most \(h-1\). Then \(u+v\le uv+1\). At height 127 take \(B=2W+1=7941\). In each window there are at least \(B\) filled columns before the first double and after the last double.

## What the independent verifier checks

The geometric verifier reads the double coordinates and each binary word directly. Its input includes the labels that occur in other windows through the final opposite-parity graph. The search used geometric clauses and a Boolean solver. The verifier instead enumerates the tilted rectangles by their primitive side directions. [Geometric verifier](check_filled_phase_bitsets.py) · [Search](search_127_filled_phases.py)

The bottom corner of a tilted rectangle is unique. Its two upward sides are \(k(a,b)\) and \(j(-b,a)\), for positive integers \(a,b,j,k\) with \(\gcd(a,b)=1\) and \(kb+ja\le126\). These conditions give 118,393 shapes. For each shape, the checker takes each of its six corner pairs \(P,Q\) as candidate common corners. At fixed row and displacement \(Q-P\), a bit represents a horizontal translation at which the other two corners of that rectangle are both black. Intersecting with the bitset from previous completions detects two rectangles with the same presentation, irrespective of the colors of \(P,Q\).

An axis rectangle completing a nonhorizontal, nonvertical pair uses the two swapped coordinates. For a horizontal pair, its opposite side must be a black pair of the same columns in another row. For a vertical pair of opposite-parity rows there is always an axis completion at its unique owner column, except when that owner coincides with the shared column. The owner can be arbitrarily far outside the window. Same-parity rows have no owner.

For shared singletons the checker uses the black corner diagonally opposite the white corner to count every tilted triple once. It rejects a repeated white corner and any coincidence with a virtual axis singleton. A white cell has such an axis alternative precisely when its own column contains a black row of opposite parity, since that pair has an owner. The checker also rejects fully hidden tilted rectangles. Axis-only collisions are excluded because the final row-pair graph is simple and bipartite. Two rectangles cannot share three corners without being equal. These tests cover the cases of two, one and zero visible corners, including two disjoint hidden rectangles. All 27 windows passed.

## Joining the windows

Each palette \(\{L,H\}\) contains a boundary row called its anchor. The two levels have opposite parity, \(2L-H<1\) and \(2H-L>127\). An arbitrary singleton word in these two levels is valid relative to the final parity graph. Three black corners on two levels would either use a vertical side or reflect one level past the other, which puts the fourth row outside the strip. In a mixed side/diagonal collision with a \(3+1\) split of black rows, the row sum is odd. With a \(2+2\) split either the segments are horizontal and parallel, or each joins the two levels. In the latter case their centers have the same row, and perpendicularity to a nonvertical side forces the centers to coincide. A diagonal joining the two levels cannot have an in-strip vertical alternative, since one of the levels is a strip boundary. A same-level diagonal has the wrong row-sum parity for a vertical owner.

Put the 25 windows with anchor 1 first, followed by the two windows with anchor 127. Between consecutive windows with the same anchor put \(B\) constant columns of that row. At the single change of anchor put \(B\) columns of row 1 and then \(B\) columns of row 127. A pure \(1\)-to-\(127\) switch has its black points ordered monotonically in both coordinates. Such a step has no tilted black triple. It has no mixed support either. Orient each of the proposed side and diagonal segments in increasing coordinate order. Nested endpoint intervals have different lengths. Otherwise their ordered endpoints give coordinatewise comparable midpoints, whose difference cannot be perpendicular to a nonhorizontal, nonvertical segment. For a horizontal side the two centers would need the same column, which is impossible for two distinct ordered intervals with comparable endpoints in this one-point-per-column step. A cross-boundary diagonal has no in-strip vertical alternative.

Every collision involving intersecting tilted rectangles has horizontal span at most \(2W\). If an axis rectangle competes with a tilted rectangle, a shared oblique or horizontal pair keeps all relevant columns in the tilted span. A shared vertical pair may have a distant axis owner, which the verifier included. The same holds for a singleton axis competitor. The \(B\)-column halos prevent any local witness containing a double from crossing the end of its window. A witness confined to singleton columns at a join sees either a single palette or the isolated monotone switch. This proves validity after joining. It also proves validity for any continuation in the final palette, including a constant row-127 tail.

The windows occupy 1,292,641 columns. The separators add \(27\cdot7941=214{,}407\). The resulting 1,507,048 columns contain 1,511,080 black cells. The SHA-256 digest of the board, encoding each column by its sorted positive rows followed by zero if it is a singleton, is
\[
\texttt{1fda532117c3534cb1fe5b6b1db07f9162f9862fd0f80e28b0a88e4d9dc4ddb0}.
\]
[Assembly and replay](assemble_127_filled_board.py)

Run the assembly checker with \(\texttt{--audit}\) to repeat all 27 geometric checks. Its \(\texttt{--column}\) option returns the black rows at a one-based column index, including columns in the constant continuation.

## Counting the continuations

Before the first window insert a word in its palette. Immediately after each of the 27 windows, before its separator if present, insert a word in that window's palette. All choices are valid by the same collar argument. For \(t=m-M\) one can distribute \(t\) columns among the 28 positions in \(\binom{t+27}{27}\) ways. Each distribution admits \(2^t\) binary words. The position of the first double recovers the initial length, and each separation between successive windows recovers the next inserted length. The total width then recovers the last length. Thus words from different distributions give different labeled boards.

This certificate establishes one height. A proof of \(m_h=O(h^2)\) still needs uniform constructions of the double placements, singleton words and collars, with a width estimate uniform in \(h\).

