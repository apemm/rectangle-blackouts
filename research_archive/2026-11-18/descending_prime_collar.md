# Joining a descending prime profile to a two-row background

Use row coordinates \(0,\ldots,h-1\). Fix an odd prime \(p\le h\) for which \(2\) is a quadratic nonresidue. For example \(p\equiv3,5\pmod8\) works. Put one black point in each integer column:
\[
 y(x)=
 \begin{cases}
 [-x]_p,&x\le0,\\
 x\bmod 2,&x\ge0.
 \end{cases}
\]
Here brackets mean the least nonnegative representative. The two definitions agree at zero.

**Theorem.** This joined singleton configuration is clean for the ordinary row-parity partition, including the tests against vertical row-pair owners at arbitrary columns. No guard columns are required. This statement treats the background. Inserting a prescribed double demands extra tests.

## The prime half and the crossing distances

For \(x\le0\) write the point as \((-kp-r,r)\) with \(k\ge0,\ 0\le r<p\). Its checkerboard color \(x+y\bmod2\) equals \(k\bmod2\). All points on the right have checkerboard color zero.

On the old half all points lie on \(x+y=0\bmod p\). A chord between different residues has nonsquare norm modulo \(p\), since it is a nonzero multiple of \((1,-1)\bmod p\). Two crossing chords at the same pivot cannot be perpendicular since \(2\ne0\bmod p\). A same-residue chord is horizontal. This excludes prime-half tilted triples and rival pairs. For mixed supports in this half, orient the black side \(U\) and black diagonal \(V\) to agree modulo \(p\), possible up to sign by equal squared lengths. If they cross residues, their common midpoint shift \(H/2\) satisfies \(H\cdot U=0\), and \(H\) also belongs to the same residue line, so \(H=0\bmod p\). The ends of the two segments then match in residue pairs. Both matched differences are horizontal, as a residue has one actual row. Hence \(H\) is horizontal. A nondegenerate mixed support has \(H\ne0\), so \(U\) would be vertical, impossible in this graph. A side divisible modulo \(p\) forces the diagonal divisible also, and then both are horizontal with the same length, which is degenerate.

A right-half point in row zero cannot be a rival. For a right-half point in row 1 and an old point in row \(r\) of opposite parity, \(r\) is even. The case \(r=0\) touches the boundary. For \(r\ge2\), containment of the alternative vertical diameter forces its length to be \(r+1\), since it is odd and strictly exceeds \(r-1\). Thus the horizontal gap \(X\) satisfies \(X^2=4r\). But the right-half point has positive odd column, so \(X\ge r+1>2\sqrt r\). Two points of opposite row parity on the right also differ by an odd horizontal distance, and their squared norm is \(2\bmod4\). Thus the joined configuration has no rival pair.

## The mixed supports

A graph with the property \(|\Delta y|\le|\Delta x|\) is a chain after the similarity \((x,y)\mapsto(x+y,x-y)\). The mixed-support part of the [chain lemma](../../papers/extremal/sections/sec5_threshold.tex) is invariant under similarities and excludes every nondegenerate mixed support in such a set.

Each checkerboard class of the joined configuration has this slope property. Old points of one period lie on a line of slope \(-1\). Old points of equal color in different periods are at horizontal distance at least \(p+1\), greater than the whole vertical span \(p-1\). Two right-half points satisfy the property, as does any chord crossing the seam since \(-x\ge r\) for an old point \((x,r)\), and a strictly positive right column is at least 1. More generally, a chord with \(|\Delta y|>|\Delta x|\) must cross one old reset. When oriented right it has vector \((u,p-u)\) with \(0<u<p/2\). Its Euclidean length is strictly less than \(p\), and it changes checkerboard color. Every chord between a right-half point and an opposite-color old point has horizontal length at least \(p\).

Let \(A,B\) form the black side of a mixed support, and let \(E,F\) form its black diagonal. Orient both chords left to right. Set \(U=B-A,\ V=F-E,\ H=E+F-A-B,\ J=U-V\). One has \(H\cdot U=0\) and \(J\cdot(U+V)=0\). Integrality of the common corners gives \(U\equiv V\bmod2\) in each coordinate. Hence the two black chords are either both monochromatic in checkerboard color or both bichromatic. When \(U,V\) both satisfy the slope property, their positive horizontal components give \(|H_x|\le|H_y|\) and \(|J_x|\le|J_y|\). Writing \(B_1=E-A,\ B_2=F-B\), the sum of these inequalities gives
\[
 \max_i|(B_i)_x|\le\max_i|(B_i)_y|.
\]
If both black chords are strictly shallow, the inequality is strict unless both matched differences vanish, which is degenerate.

We may assume the support uses a point on the right. Four points of the same color form a chain after rotation. If the black chords are individually monochromatic in different colors, at least one matched end-chord joins a right-half point to the opposite color, with horizontal extent at least \(p\). Both vertical extents are at most \(p-1\), contradicting the displayed inequality.

If the black chords are bichromatic, the chord touching the right half has length at least \(p\), so both do. The preceding steep-chord classification shows both are shallow. They are strictly shallow, because a chord of slope \(+1\) or \(-1\) preserves checkerboard color. The two matched end-chords preserve color if \(A,E\) have the same color. The strict inequality above then contradicts their slope property. If \(A,E\) have different colors, the matched end-chord touching the right half has extent at least \(p\), again contradicting the inequality. This proves mixed-support exclusion.

## The tilted triples and their completions

The final old period \((-r,r)\), \(0\le r<p\), together with the right half is 1-Lipschitz. Its tilted right angles therefore use slopes \(+1\) and \(-1\). The only increasing unit-slope segments are between adjacent points on the right. A decreasing unit-slope segment reaching an old point in the final period lies on \(x+y=0\), so its right-half endpoint must be \((0,0)\). The cross triples in this last period have corners \((0,0),(1,1),(-r,r)\) for \(1\le r<p\). They complete at \((1-r,1+r)\).

Here is the exclusion of earlier periods. A chord from the right half to any old point is shallow, with equality only possible for a point in the final period. If two endpoints of a right angle are on the right and its pivot is old, the two endpoint rows 0 and 1 cannot lie strictly on opposite sides of the pivot row. If the pivot is on the right and one endpoint on each side, the two chords are shallow and equality of both slopes is required, already treated.

Now take two old points \(A=(x,r)\), \(B=(x+s,r+d)\) with \(s>0\), and a right-half point \(Z=(z,t)\), \(z>0,\ t\in\{0,1\}\). If \(Z\) is the pivot, the old rows must straddle its row. This forces \(t=1\) and one old row zero. The other old row \(r'>1\) then has horizontal distance at least \(z+r'>r'-1\) from \(Z\). The horizontal product is greater than the vertical product \(r'-1\).

For a pivot at \(A\), perpendicularity gives \(s(z-x)=d(r-t)\), and the fourth row is \(t+d\). When \(d<0\), positivity of \(z-x\) forces \(r=0,t=1\), which is incompatible with \(r+d\ge0\). When \(d>0\), the chord crosses a reset, so \(s>r\), \(x=-kp-r\) with \(k\ge1\), and \(d<p\). Consequently \(z-x=d(r-t)/s<p\), too small to reach the right half. At a pivot at \(B\), the analogous equation is \(s(z-x-s)=d(r+d-t)\) and the fourth row is \(t-d\). For \(d>0\), an in-strip fourth row forces \(t=d=1\), and the horizontal gap \(r/s<1\) is impossible. For \(d<0\), a positive right gap forces \(r+d=0,t=1\). Every descending old chord has \(|d|\le s\), so the gap is at most one. This requires \(B=(0,0)\), yielding the already listed final-period triples. Zero \(d\) gives no tilted leg.

The all-right triples with in-strip completions are the unit diamonds at even-column row-zero pivots, with both adjacent row-one points present. Their white corners are in row 2. The cross completions \((1-r,1+r)\) lie at distinct columns \(\le0\), with the same parity as the unique black row there and a different row. The unit diamonds wholly on the right have positive even pivot column. Thus every in-strip completion is parked and unique.

## A double in the preceding periodic background

The clean background does not allow arbitrary substitutions. Add \((x,r+p)\) above a regular point \((x,r)\) with \(1\le r<p\). If the same residue appeared one period earlier and \((x-p+1,r-1)\) is regular, the three black points \((x-p,r),(x-p+1,r-1),(x,r+p)\) form a tilted rectangle. Its fourth corner \((x+1,r+p-1)\) has opposite parity to the regular row \(r-1\) in that column. On an equality board this produces a collision. A profile for gap-\(p\) doubles has to handle these points separately.

## A difference between the two tails

A constant bottom tail fails for every odd \(p\ge7\). In zero-based rows the last reset supplies \(A=(-p,0)\) and \(C=(-p+1,p-1)\). Put \(L=1+(p-1)^2/4\) and \(z=L-p>0\). If \(B=(z,0)\) and \(D=(z-1,0)\) are black, \(AB\) is horizontal of length \(L\) while \(CD\) has vector \((L-2,-(p-1))\) of the same length. Their doubled midpoint coordinates agree horizontally. The common corners are \((-p,(p-1)/2)\) and \((z,(p-1)/2)\). This mixed presentation is possible a quadratic distance from the reset.

## The final period also reserves every interior column

Fix a final-period column \((-r,r)\) with \(0\le r\le p-2\). The existing triple \((0,0),(1,1),(-r-1,r+1)\) completes at \(W=(-r,r+2)\). Whenever a gap-\(p\) double fits, \(r+p\le h-1\), the completion lies in the strip. The new double contains both parities. This gives a vertical owner for the row of \(W\), so the two presentations collide. The last residue \(r=p-1\) is outside this argument.
