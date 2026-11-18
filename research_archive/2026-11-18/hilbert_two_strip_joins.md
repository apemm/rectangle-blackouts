# One-role obstructions disappear after joining all filled tiles

Use the quadtree blocks in [the separated-row construction](separated_row_tiles.md). They cover every odd-even label exactly once. There is a single filled board of width \(O(h^2)\) containing all those labels with the following guarantees.

1. No tilted black corner triple or nonvertical mixed quadruple has all its black points of the same row parity.
2. Every nonhorizontal same-parity chord between different columns has nonintegral length. In particular, no mixed quadruple with a horizontal black side or horizontal black diagonal occurs.
3. Each individual core still has all three obstruction exclusions of the separated-row theorem, including its test against a remote vertical owner. Cross-role obstructions need further work to obtain a valid blackout.

### Construction and row variation

Traverse the padded index square by the usual discrete Hilbert order. Each aligned dyadic square is a consecutive interval of ranks, and two index pairs at ranks \(r,t\) differ by \(O(\sqrt{|r-t|+1})\) in each coordinate. For the latter bound take the least power of four \(4^j\ge |r-t|+1\). The rank interval meets at most two squares of side \(2^j\) in the tiling at that level. If there are two they share an edge because consecutive points of the Hilbert path are neighbors. A coordinate difference is at most \(2^{j+1}\). These properties also follow from the [Hilbert recursion used in the tiling archive](../2026-11-14/hilbert_tiling_assembly.md).

Number the nonempty terminal squares in this order. Write \(b_i\) for their sides, and \(e_i\) for the number of discarded ranks between squares \(i,i+1\). Use an absolute constant \(K\), chosen sufficiently large below, and set
\[
 D_i=\left\lceil K(b_i^2+b_{i+1}^2+e_i)\right\rceil .
\]
Between consecutive cores first insert \(D_i\) columns containing the even representatives from core \(i\)'s modular rule and then \(D_i\) containing the odd representatives from core \(i+1\)'s rule. Extend each rule using the core's own horizontal origin; translations only change the affine intercept. For a unit square, repeat its sole row of the specified parity. Every guard column is a singleton. The sum of the \(D_i\) is \(O(h^2)\), since the squares have disjoint ranks and all discarded gaps together have at most \(N^2\) ranks.

A point's system is the tile giving its row, also in the adjacent guard where that row rule is extended. For each fixed role, different systems occur in tile order. Suppose a set of points of the same role meets systems from \(i\) to \(j\) with \(i<j\), and has horizontal span \(s\) and row diameter \(d\). Each intervening join contributes at least \(D_t\) to \(s\), since one of its two strips contains only the other role. The ranks from the start of tile \(i\) through the end of tile \(j\) occupy at most \(\sum_{t=i}^jb_t^2+\sum_{t=i}^{j-1}e_t\) positions. Each representative row is within \(O(b_t)\) of a row belonging to the physical tile, including in clipped boundary squares. The Hilbert bound and the conversion from row index to physical row give an absolute \(C\) such that
\[
 d^2\le C s/K. \tag{1}
\]
This applies even when the two extrema belong to the same tile. The separation pays for that tile's side square as well.

### Proof of the exclusions

Within one system the row representatives of a role are unique modulo the corresponding prime. The prime-line norm, dot-product, and mixed-support arguments of the separated-row theorem do not use a horizontal-span bound when all the points are in one role. They apply throughout the extended guard too. For a unit system all chords are horizontal.

For different systems (1) applied to a pair gives \(0<Y^2<2|X|+1\) on a nonhorizontal chord, once \(K>C\). Its squared norm lies strictly between consecutive squares. For a same-role tilted triple its two legs at the right angle satisfy \(|X_1 X_2|=|Y_1Y_2|\le d^2\), with both horizontal magnitudes positive. The black span is at most \(1+d^2\). For a same-role mixed support there is at most one point of that role per column. Its four black points, whose row spread is \(d\ge1\), therefore form a \(d\)-Lipschitz set. The two perpendicularities in [the linear locality proof](linear_collar_locality.md) give black span at most \(3d^2\): in that proof take \(D=d\), since it needs only the row differences of the black points and the difference of their pair midpoints. Thus a same-role obstruction using more than one system would have \(s\le3d^2\le 3Cs/K\). Taking \(K>3C\) excludes it. A one-row support cannot give either obstruction.

For a horizontal black side, equal squared norms give an integral length to the black diagonal. Integrality of the common corners gives even total row sum. Thus both endpoints of the diagonal have the same parity. They cannot form a nonhorizontal chord by the preceding result. Two horizontal vectors with equal norm have the same unoriented vector, which is excluded in a mixed support. The argument with a horizontal black diagonal is identical for a nonvertical black side. A vertical parity side cannot face a horizontal black diagonal since their vector coordinates differ modulo two. This proves the stated guarantees.

### What the two-role equations still allow

A mixed support can have two black points of each parity. In particular, suppose the side has odd endpoints and the diagonal has even endpoints (or conversely), and both chords span different systems of their role. By (1), their squared norms lie in the half-open square intervals starting at the squares of their horizontal magnitudes. Equality forces their horizontal magnitudes to agree. Orienting both to the right gives \(U=(u,v)\) and \(V=(u,-v)\), with \(v\ne0\). Write \(E-A=(t,c)\) for the displacement between their left endpoints. Then \(F-B=(t,c-2v)\), and perpendicularity becomes
\[
 ut=-v(c-v).
\]
Here \(v\) is even and \(c\) odd. This is a necessary equation for a remaining two-role obstruction.

Alternatively let both principal chords cross between roles, with positive horizontal components and the same role at their left endpoints. Then \(B_1=E-A\) and \(B_2=F-B\) are same-role chords. If both span systems, put \(t=\max_i|(B_i)_x|\), \(u=\min(U_x,V_x)>0\), and \(g=\max(|U_y|,|V_y|)\). The perpendicularities for \(B_1+B_2\) and \(B_1-B_2\), followed by \(|a+b|+|a-b|=2\max(|a|,|b|)\), give
\[
 t\le(g/u)\max_i|(B_i)_y|,\qquad u\sqrt{t}\le g\sqrt{C/K}.
\]
This estimate does not cover the opposite left-to-right role orientation. Cross-role rivals, tilted triples and two-plus-two mixed supports still have to be excluded on the full board.

Even two adjacent original blocks with identical slopes can fail without any guards. At height 508 take primes \(3,5\), both slopes 1, common even rows \(500,502,504,506,508\), first odd rows \(1,3,5\), and second odd rows \(7,9,11\). The old and new cores occupy columns 0–14 and 15–29 with their phases aligned. The black triple \((13,1),(16,7),(9,3)\) completes at \((12,9)\). The latter column contains row 502 and the owner of \(\{9,502\}\) is column 27, giving a second rectangle with the same visible corner. This illustrates the need to analyze seams.

