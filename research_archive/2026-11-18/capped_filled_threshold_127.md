# A filled, extendible \(127\)-row board of width 498,166

Put \(M=498166\). Then
\[
 f(127,m)=m+4032,\qquad
 a_{127}(m)\ge 2^{m-M}\binom{m-M+3}{3}\qquad(m\ge M).
\]
The starting width is a certified upper bound for the threshold at this height. At \(m=M\), the board has 502,198 black cells and every one of the \(64\cdot63=4032\) opposite-parity row pairs occurs once. Encoding each column as two row bytes in increasing order, with second byte zero for a singleton, gives SHA-256 `b1576b8b526428ff89b175143efcd9804c4cb3fffa0daab46f8d8853a6105bfe`. The [assembler](assemble_capped_127.py) reconstructs these bytes and gives individual columns at larger widths.

## Four compact filled windows

The four palettes are those of the [preceding construction](compact_filled_threshold_127.md). Within each window keep its true labels in their original order, and cap the gap \(x_{j+1}-x_j\) between successive double columns. From left to right the caps are 1,024, 256, 256 and 512. Each label's new column is determined by the earlier window and its cap. Recompute the binary assignment to every remaining column, including 7,941 exterior singleton columns on either side.

| Window | Width including both halos | Double columns | Black-pair projections in the geometric scan | Singly visible tilted rectangles |
|---|---:|---:|---:|---:|
| [Rows 1 and 122](phase_127_capped_1_122_1024.json) | 328,475 | 2,478 | 83,240,533 | 22,357 |
| [Rows 1 and 124](phase_127_capped_1_124_256.json) | 110,003 | 903 | 30,034,559 | 8,020 |
| [Rows 1 and 126](phase_127_capped_1_126_256.json) | 63,551 | 474 | 17,470,121 | 3,899 |
| [Rows 2 and 127](phase_127_capped_2_127_512.json) | 34,655 | 177 | 5,929,185 | 1,639 |

Each filling passed the independent check of all 118,393 tilted rectangle templates, grouped into 107,180 displacements of the shared pair. Every possible opposite-parity owner in the grid is included. The optional sparse index discards a proposed placement only when its two black rows contain no black pair at the required signed horizontal displacement. The geometric tests themselves are independent of the constraints used to search for the binary words. [Certificate search](search_capped_127.py) · [Geometric verifier](check_filled_phase_bitsets.py)

## Joining the windows

The maximum horizontal span of one tilted rectangle is \(W=3970\). A nonvertical mixed support has black span at most \(G=4001\), including a tilted rectangle sharing a visible pair with an axis rectangle whose relevant side is nonvertical. The [mixed-support estimate](compact_filled_threshold_127.md) gives this bound, with an example attaining it. A remote vertical axis owner is handled by its local opposing pair, of displacement less than \(h=127\). Every tilted triple in one working window requires a double column. With only singleton columns present, two of its three black rows would have to coincide. Those two corners would be opposite, and reflection across their horizontal diagonal would put the fourth row outside the strip.

At the two exterior ends of the final board omit all 7,941 singleton columns. At each of its six interior window ends keep the \(G\) original singleton columns next to the end double and omit the other \(7941-G=3940\) columns. Add 405 copies of row 1 and then 599 copies of row 127 at the last join. The final width is
\[
 536684-2(7941)-6(3940)+405+599=498166.
\]

At the first join the second window begins with 4,001 consecutive cells in row 1. At the second join the second window ends with 2,298 consecutive cells in row 1. At either join the two high levels differ by two. The two-band estimate bounds the span of any singleton obstruction involving both high levels by \(5\cdot2\cdot126=1260\). At the last join the outgoing 226 original row-1 cells and incoming 32 original row-127 cells, with the inserted cells, give 631 consecutive positions in each respective boundary row. The parity-flip bound for \(\{1,126\}\) followed by \(\{2,127\}\) is \(5\cdot126=630\). Its constant boundary switch is a monotone chain. Therefore no tilted triple or nonvertical mixed support made entirely from singleton cells crosses any of the three joins. Across a same-anchor join a chord between opposite-parity singleton rows has an endpoint on boundary row 1. Across the last join the only interior rows are 126 and 2, both even. Thus an opposite-parity singleton chord there also has a boundary endpoint, excluding its in-strip vertical alternative. [Two-band estimates](two_band_profile_joins.md) · [Parity flip and endpoint geometry](compact_filled_threshold_127.md)

A mixed support across a join cannot use a double, since its black span is at most \(G\) and its first available double would already be farther than \(G\) from the other side. The same observation applies to a tilted triple, an all-black tilted rectangle, or an oblique chord opposed to a remote owner. Two tilted triples on different sides that share a completion would require two double columns at distance at most \(2W\). The shortest gap across any join exceeds \(2G>2W\). Every local configuration on just one side is part of the original certified phase, with its virtual owners. This also proves that the singletons at every changed join are compatible with the complete row-pair graph.

The assembler has a second check at each join. It examines the full \(2W\) neighborhood on either side with actual true columns present, and also checks the finite right endpoint with its original exterior halo and the constant outer extension.

## Larger widths and multiplicity

Let \(t=m-M\). There are four independent binary insertion sites. At the first phase join use the outgoing palette \(\{1,122\}\). The 4,001 incoming row-1 cells remain. At the second join use the incoming palette \(\{1,126\}\), keeping the preceding 2,298 row-1 cells. At the last join allow an arbitrary outgoing word in \(\{1,126\}\) immediately before the 405 added row-1 cells and an arbitrary incoming word in \(\{2,127\}\) immediately after the 599 added row-127 cells.

For the last two sites we need a pure-background span bound below 405. It suffices to use 378. In either band \(\{1,2\}\) or \(\{126,127\}\) a nonhorizontal vertical displacement has magnitude one. A tilted triple with a within-band leg therefore satisfies \(|X_1X_2|\le126\), so its whole rectangle spans at most \(|X_1|+|X_2|\le127\) columns in horizontal displacement. If both legs cross bands the completion leaves the strip. For a mixed support with both chords crossing bands, the vertical magnitudes lie in \(\{124,125,126\}\). If they differ, the nonnegative squares of the horizontal magnitudes differ by at most 500. Since \(n^2-(n-1)^2=2n-1\), each magnitude is at most 250. If the vertical magnitudes agree, the horizontal magnitudes agree, and perpendicularity gives \(|U_x|\le252\) because the two row sums differ by at most two. In both cases \(|H_x|\le252\). A within-band nonhorizontal side has \(|U_y|=1\), so \(|U_x|,|H_x|\le252\) by perpendicularity and \(|V_x|\le |U_x|\) by integrality and equal lengths. A horizontal side with a diagonal inside a band cannot oppose a nonhorizontal chord of vertical size one, since \(v^2+1=u^2\) has no positive \(u,v\). The other pairings are excluded by the disjoint-phase and midpoint arguments in [the join proof](compact_filled_threshold_127.md). The two centers differ horizontally by at most 126 and each endpoint is at most 126 from its center. This gives span 378. Joined tilted triples with a common completion have span at most 254. The 405 and 599 constant cells separate all these obstructions from the middle switch.

Any new non-pure support would have to meet a double, too far from an insertion site by the sharp \(G\) bound and the two-triple argument. The distances between the known labeled doubles across the first two joins recover their insertion lengths. At the last join the outgoing and incoming alphabets are disjoint; the unique change of alphabet recovers both lengths there. Thus the \(\binom{t+3}{3}\) weak compositions and \(2^t\) row words give distinct boards, all optimal by the row bound.

### An insertion alphabet with exponential rate greater than two

Use the singleton alphabet \(\{1,122,124\}\). Forbid two different high rows at any horizontal distance in
\[
 D=\{1,2,4,11,22,121,242\}.
\]
Every such word is valid with all remote parity owners. A tilted triple involving both high levels and row 1 can have an in-strip completion only if its pivot is row 122. Its two horizontal legs then have product \(2\cdot121\). If all three points are high, the nonhorizontal legs force the off-level pivot and their product in absolute value is four. The high-high distance in either case belongs to \(D\). A triple using only row 1 and a single high level completes outside the strip or has an axial leg.

For a mixed support the parity of the row sum leaves zero, two or four high points. With zero or four, a horizontal chord cannot oppose a nonhorizontal chord with vertical magnitude two, as \(v^2+4=u^2\) has no positive integral solution. Two chords crossing the two high levels have the same midpoint row, preventing a genuine perpendicular midpoint displacement; two horizontal chords are parallel. The same horizontal-norm check handles the two-high case in which each principal chord stays on its own side of the lower/upper division. Otherwise orient both principal chords from low to high. If their high levels differ, their vertical magnitudes are 121 and 123. The norm equation then gives horizontal squares differing by \(123^2-121^2=488\). Factoring 488 gives only \((123,121)\) and \((63,59)\) in decreasing order of horizontal magnitudes. If the side has vertical magnitude 121, its horizontal magnitude would have to be 123 or 63 and divide \(2\cdot121\) by the perpendicularity equation. Neither does. For a side of vertical magnitude 123, the required horizontal magnitude 121 or 59 does not divide \(2\cdot123\). Equal high levels again put the two centers at the same row. Opposite-parity chords incident to the boundary row have no in-strip vertical alternative.

The spacing condition is a convenient sufficient test. A more precise count gives a larger insertion rate. Start with a binary word of length \(j\) in rows 1 and 122, writing 1 for a high bit and 0 for a low bit in the calculation below. A high center at position \(x\) is eligible to become 124 if it is at least 242 positions from the exterior and its translated binary neighborhood has the following properties:

* for every signed divisor \(d\) of 242, a high bit at \(-d\) implies a high bit at \(242/d-d\);
* neither of the pairs \((-1,4),(-2,2),(-4,1)\) is simultaneously high.

The first condition excludes a triangle with its pivot at a 122 point, one neighbor at the new 124 point and the other in row 1. Their two horizontal legs would have product 242. The possible case with two neighbors in row 122 and pivot at the new 124 point has product \(-4\), giving the second condition. If two changed points in row 124 form a triangle with a row-122 point, they must be separated by 4 or 5. Triangles with one changed point cannot be created by subsequently changing other high bits: another changed bit ceases to be a 122 point and does not become a row-1 point. The mixed-collision argument above excludes mixed supports for the whole alphabet without any spacing rule.

There are 18 noncentral offsets in the eligibility test. With the center fixed high, exactly 6,720 of their \(2^{18}\) assignments are admissible. The count factors into disjoint groups. Each of the two groups involving one sign of rows \(\pm1,\pm4,\pm241,\pm242\) has eight assignments. The six positions at \(\pm2,\pm119,\pm121\) contribute 21, and the four positions at \(\pm11,\pm22\) contribute five. For example, the last group requires the bits at \(\pm11\) to agree, with the \(\pm22\) bits forced low only if that common bit is low. The unconditional one-site probability is \(p=6720/2^{19}=105/8192\).

Two translated eligibility tests overlap in just three variables at spacing four and two variables at spacing five. In the table the subset index uses the given offsets as bits in increasing order from least to most significant. Conditional on these bits the remaining variables for the two tests are disjoint.

| Spacing | Shared offsets | Counts of eligible assignments in the left test | Counts in the right test |
|---:|---|---|---|
| 4 | \(0,2,4\) | \(0,3000,0,1200,0,1800,0,720\) | \(0,0,0,0,3000,1800,1200,720\) |
| 5 | \(1,4\) | \(3150,1050,1890,630\) | \(3150,1890,1050,630\) |

Taking the dot product in each row and dividing by the number of binary assignments on both stencils gives \(p_4=3758400/2^{35}\) and \(p_5=14288400/2^{36}\). In particular \(p-p_4-p_5>1/80\). [Integer check of the neighborhoods](check_127_ternary_neighborhoods.py)

Join eligible centers at distances four or five. By deleting at most one endpoint per edge we get an independent set of size at least the number of eligible centers minus the number of edges. Its expected size in a uniform binary word is at least \((j-484)_+(p-p_4-p_5)\). Fix such a set by any deterministic rule. Recolor any subset to row 124. Every resulting word satisfies the geometric exclusions proved above. The original binary word can be recovered by identifying the high sites, so convexity of \(2^x\) gives at least \(2^{j+(j-484)_+/80}\) different insertions. At the first join the exterior row-122 cells lie outside the test stencil, and the 4,001 incoming row-1 cells separate the word from the incoming row 124. Consequently
\[
 \liminf_{m\to\infty} a_{127}(m)^{1/m}\ge 2^{81/80}>2.0174.
\]
Keeping the other three binary insertion sites and summing over the first length gives the finite bound
\[
 a_{127}(M+t)\ \ge\ 
 2^t\sum_{j=0}^t\binom{t-j+2}{2}\,2^{(j-484)_+/80}.
\]

To reproduce the certificate, run the following commands from the repository root. The first reconstructs the board and scans the phase joins and tail. The second also scans all four complete windows.

~~~text
python -B research_archive/2026-11-18/assemble_capped_127.py --seams
python -B research_archive/2026-11-18/assemble_capped_127.py --audit --sparse-index
~~~

## A second check of the board

[A separate program](check_127_three_black.py) reads only the board bytes. It finds 4,032 doubles with distinct row pairs, a bipartite pair graph with parts of 63 and 64 rows, and no tilted rectangle with 4 black corners. There are 35,877 tilted rectangles with 3 black corners. They show 35,877 different white corners, and none of these is also the single white corner of an axis-aligned rectangle. This rules out every collision in which some rectangle has at most 1 white corner. It does not test a collision between 2 rectangles that share 2 white corners, where the shared pair is a side of one and a diagonal of the other. The main verifier covers that case. [The test](test_check_127_three_black.py) compares the enumeration with a direct one on 300 small boards.

~~~text
python -B research_archive/2026-11-18/check_127_three_black.py
~~~
