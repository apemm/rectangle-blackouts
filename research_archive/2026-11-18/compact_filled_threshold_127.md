# Four filled windows at height 127

The 27 groups in [the first complete certificate](filled_threshold_127.md) can be packed into four windows. Each window has one two-row singleton palette. Its binary word was recomputed after the constituent double groups were moved closer together. The four window widths are
\[
 553319,\quad 198923,\quad 121247,\quad 74323.
\]
They contain 2,478, 903, 474 and 177 doubles, respectively. Their palettes in order are \(\{1,122\},\{1,124\},\{1,126\},\{2,127\}\). The first window uses 1,024 as its minimum gap between consecutive double groups. The other three use 256. All 4,032 opposite-parity labels occur once. No additional columns are used between windows.

[First window](phase_127_merged_1_122.json) · [Second window](phase_127_merged_1_124.json) · [Third window](phase_127_merged_1_126.json) · [Fourth window](phase_127_merged_2_127.json)

The original geometric verifier reads these assignments as bitsets and checks tilted rectangles and distant axis owners by the method described in the preceding note. It also checks the full set of rectangle templates on the 15,880-column interval centered at each of the three new joins and at the right tail. These interval checks suffice at a cut because a tilted rectangle has horizontal span at most 3,970, an intersecting pair has span at most 7,940, and distant axis owners are included separately. The complete four-window word starts at width 947,812. Sixteen same-palette cuts, justified below, shorten it by 205,188 columns. Remove the 7,941 singleton columns before the first double and the 7,941 after the last. Each remaining end column is a double. At the resulting width \(M=726742\), the board has 730,774 black cells. Widen it at the first join with additional row-1 columns. The join argument below proves
\[
 f(127,m)=m+4032\qquad(m\ge M).
\]
Encode each column by two bytes in increasing row order, with the second byte zero for singleton columns. The SHA-256 digest of the board at width \(M\) is `33942fef1691ba1ef46668a4573934827a7a2c78362558c53304d156dbd32761`. The digest after the sixteen cuts and before trimming is `14d38e34da36915904c390001aa27db15b0848a26d7ed6b7980f7e3f6e5fba29`. The original four windows concatenate to `ca0393c5dde84d04892a8889db9ed111fe9d6f4abff3d2b8988531190834834b`.
[Assembly and independent verification](assemble_compact_127.py) · [Search](search_compact_127.py)

## Why the joins work

For the first two joins the two high rows are consecutive even rows, with common low row 1. The linear two-band locality estimate bounds a singleton obstruction crossing a seam by \(5\cdot2\cdot126=1260\) columns. Before each seam there are respectively 3,972 and 6,324 consecutive row-1 columns. Therefore any local witness reaching the next profile meets only a valid two-row background. The original filled halos keep every double more than 7,940 columns from an exterior edge. [Two-band estimate](two_band_profile_joins.md)

The last join changes parity in both bands. Its left columns use only \(\{1,126\}\), its right columns only \(\{2,127\}\). A tilted triple has a leg within one of the two bands, unless the other two corners are both in the band opposite its pivot. The latter case completes outside the strip. The within-band row difference is at most one, so the triple has horizontal span at most \(2\cdot126\).

For a mixed support write \(U\) for its black side, \(V\) for its black diagonal and \(H\) for twice the displacement between their centers. The cases with both pairs within bands, or both running between bands, have span at most \(5\cdot126\) by the usual two-band calculation. If \(U\) runs between bands and \(V\) stays within a band, the common corners have rows separated by at least 124 and centered in a band of diameter one. They leave the strip. If \(U\) stays within a band and \(V\) crosses, a nonhorizontal \(U\) has \(|U_y|=1\). Since \(U\cdot H=0\) and \(H\ne0\), one has \(H_x\ne0\) and \(|U_x|\le2\cdot126\). Also \(|H_x|\le2\cdot126\), and \(|V_x|\le|U|\le2\cdot126+1\), giving span less than \(5\cdot126\). If \(U\) is horizontal, integrality of the common corners requires the two ends of \(V\) to have the same parity. A cross-band pair with this property must go between the phases. A horizontal \(U\) of length \(|V|>|V_x|\), centered at the same horizontal coordinate as \(V\), projects beyond both ends of \(V\). That would put the same black row in both phases, whose row sets are disjoint.

The preceding argument gives the same linear phase-flip bound when the levels are \(\{1,h-1\}\) then \(\{2,h\}\), for odd \(h\) sufficiently large that the two bands are separated. Vertical rivals are local on the oblique segment, and its virtual owner can be arbitrarily far away. A switch from constant 1 to constant \(h\) has no such rival or mixed support. Its black points are coordinatewise ordered. In the certificate there are already 4,166 row-1 columns before the switch and 3,972 row-127 columns after it. These exceed the \(5\cdot126\) locality radius. The independent seam checks are separate from this analytical argument.

## Removing long singleton intervals

Write \(W=3970\) for the maximum horizontal span of a tilted rectangle in this strip, and \(G=W+\lceil(h-1)/2\rceil=4033\). The four working palettes each include a boundary row, and their two rows are separated by more than \((h-1)/2\). An arbitrary word in one such palette is valid, including the test for an opposite-parity axis owner in any column. In particular a tilted rectangle cannot have three black corners in such a word: two of those three would be at the same height, hence opposite rather than adjacent tilted corners. The fourth row would lie outside the strip by reflection across their horizontal diagonal. A tilted triple in a certified window therefore includes a double column.

In a same-palette gap between double columns with horizontal difference \(d>2G+1\), keep the nearest \(G\) singleton columns on each side and delete the \(d-1-2G\) middle columns. This is safe. First consider two rectangles with a shared pair of visible positions. If the pair is a diagonal in both rectangles, both pairs of remaining corners have the same midpoint. Their total horizontal span is at most the larger of their own horizontal widths, hence at most \(W\) when a tilted rectangle is involved. An axis diagonal in this case has the same horizontal projection as the common diagonal. If the common pair is a side of two tilted rectangles, the four remaining corners form a black rectangle, with span at most \(W\). Two axis rectangles are handled by the simple bipartite graph of double labels.

For a side-diagonal rival let \(u\) be the horizontal magnitude of the common pair, \(z\) the horizontal distance from its midpoint to the parallel black side, and \(v\) the horizontal magnitude of the other black diagonal. The black points have span at most
\[
 \max\{u,v,z+(u+v)/2\}.
\]
The side rectangle gives \(z+u\le W\) when it is tilted. For a horizontal axis side \(z=0\), and \(u\le W\) from the tilted diagonal rectangle. A vertical axis side is the distant-owner test treated separately. Also \(v\le W\): the diagonal rectangle is tilted or its axis diagonal has horizontal magnitude \(u\). The equal norms of the common pair and other diagonal give \(v\le u+h-1\). Thus the black span is at most \(G\). Any such support crossing a new cut lies entirely in its pure singleton palette. A cut cannot introduce a remote vertical-axis rival either: the relevant oblique black chord has horizontal length less than \(h\), and a pure word in each working palette excludes such a rival. Axis-only coincidences remain excluded by the original distinct labels.

The mixed-support estimate itself admits a sharper bound. Write \(H=h-1\) and \(W=1+\lfloor H^2/4\rfloor\). For a tilted side rectangle, let \(a,b\) be the positive vertical magnitudes of its side and perpendicular translation, so \(uz=ab\) and \(a+b\le H\). Since \(u,z\) are positive integers, \(u+z\le1+ab\). The integer \(v\le\sqrt{u^2+a^2}<u+a\) gives
\[
 z+(u+v)/2\le 1+ab+(a-1)/2
 \le W+\frac{\lceil H/2\rceil-1}{2}.
\]
For the last bound, maximize at \(a=\lceil H/2\rceil,\ b=H-a\), comparing the two central integers. Taking the integer part gives \(4001\) at height 127. This numerical constant is attained. Use common corners \((0,1),(1,64)\), their translates by \((-3969,63)\) as the black side, and use \((-31,32),(32,33)\) as the other black diagonal. The last pair and the common pair share their midpoint and squared length. The black span is \(32-(-3969)=4001\). The certificate keeps the original, slightly larger guard \(G=4033\).

A tilted rectangle with one or zero visible corners near a cut must contain a double column. Its entire span is at most \(W\), so any such rectangle lies on its double's original side of every cut. Two tilted triples from opposite sides cannot acquire a common white corner, since their double columns are separated by at least \(2G+1>2W\). A singly visible tilted rectangle remains safe against an axis owner by the original virtual-owner test at its visible corner. Presentations of size three or four determine their rectangle directly. These cases cover all collisions. The same argument works for one cut at a time, since every remaining cut lies between a distinct pair of consecutive doubles.

The four windows admit respectively 8, 4, 2 and 2 cuts. The deleted widths are 120,512, 45,396, 23,034 and 16,246. The original palette changes keep their full halos. The reconstruction script's optional `--shortcuts` mode separately enumerates all geometric rectangle shapes around each cut, using the full radius \(2W\) on either side and a virtual owner for every opposite-parity label.

## Multiplicity at these widths

For \(t=m-M\), divide the extra columns between two sites, immediately before windows two and three. At each site use an arbitrary word in the incoming palette. The preceding row-1 run separates the old high level from the new one. The supports of the new words which approach a double meet only the original certified background, since each join lies more than 7,940 columns from any double. The lengths of the inserted words can be recovered from the gaps between labeled doubles. Thus
\[
 a_{127}(m)\ge (t+1)2^t\qquad(m\ge M).
\]

For a stronger bound at large widths put \(s=m-742624\ge0\) and keep the full outer halos. Add two further independent words, one before the first window in its palette and one after the last window in its palette. The double positions recover all four lengths, so the bound becomes \(2^s\binom{s+3}{3}\). A fifth site lies immediately before window four. Require its first \(\min(n,631)\) letters to be 127 when its length is \(n\). Its remaining letters are arbitrary in \(\{2,127\}\), and the existing prefix supplies the rest of the constant guard for a shorter insertion. This gives \(2^{s-631}\binom{s+4}{4}\). The first certificate gives a higher polynomial power at its larger starting width. The uniform quadratic threshold remains open.
