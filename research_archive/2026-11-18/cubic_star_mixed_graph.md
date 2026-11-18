# Crossed mixed supports on a constant-row star

In the [filled star construction](all_obstructions_short_windows.md), every column carries an odd point in row \(o\) and a retained even leaf \(e=o+g\) is at \(x=c+4e\). Join two distinct nonzero signed odd gaps if the two corresponding leaves together with two odd points form a crossed nonvertical mixed support. This note counts the possible edges in the full star, shows that their graph has unbounded degeneracy, and gives a realized odd cycle.

## The number of crossed supports

For a side directed from odd to even write \((u,g)\); write \((v,g+\Delta)\) for the similarly directed diagonal. Then \(\Delta\ne0\), and the mixed equations are
\[
 u(8\Delta+u-v)=-g\Delta,\qquad u^2-v^2=\Delta(2g+\Delta).
\]
Write \((v-u)/\Delta=a/b\), \((a,b)=1,\ b>0\). The short-window proof gives
\[
 u=bk,\quad g=k(a-8b),\quad
 \Delta(a^2+b^2)=4kb^2(4b-a).
\]
Put \(d_{a,b}=\gcd(a^2+b^2,4b^2(4b-a))\). Since \(\gcd(a^2+b^2,b)=1\), any common factor with \(4b-a\) divides 17. Thus \(d_{a,b}\le68\), and \(k\) must be a multiple of \(K_{a,b}=(a^2+b^2)/d_{a,b}\).

If \(1\le |g|\le h\), then \(a\ne8b\), and there are at most \(136h/(|a-8b|(a^2+b^2))\) allowed nonzero \(k\)'s. No restriction on \(u\) or \(v\) enters here. The series
\[
 \sum_{b\ge1}\ \sum_{a\ne8b}\frac1{|a-8b|(a^2+b^2)}
\]
converges. Indeed, set \(j=a-8b\). For \(0<|j|\le16b\), sum first over \(j\) using \(a^2+b^2\ge b^2\) to get \(O(\log(2b)/b^2)\). For \(|j|>16b\) one has \(|a|\ge|j|/2\), giving \(O(1/b^2)\). The subseries with \(b>R\) is \(O(\log(2R)/R)\). The same bound holds for \(b\le R,\ |a-8b|>16R\) by the latter estimate and direct summation. Therefore the whole star has \(O(h)\) possible ordered crossed mixed supports. For a fixed \(g,k,a,b\) the two even points and the horizontal offsets \(u,v\) determine the four black points.

## Rational ratios and their realization in a strip

When the two gaps are positive, their directed ratio is
\[
 \frac{g+\Delta}{g}
 =\frac{a^3-8a^2b-3ab^2+8b^3}{(a-8b)(a^2+b^2)}.
\]
Since \(g\) is odd, both \(a\) and \(k\) are odd. Conversely, take \(a\) odd and positive \(b\) coprime to it, with \(a\ne4b,8b\), and take a ratio with two positive gaps. Here \(K_{a,b}\) is odd: for \(b\) even the numerator \(a^2+b^2\) is odd; for \(b\) odd its valuation is 1 and that factor is removed by \(d_{a,b}\). Choose \(k=\pm K_{a,b}\) to make \(g>0\). The resulting \(\Delta\) is a nonzero even integer divisible by \(b\), so \(g'=g+\Delta\) is odd and \(v=bk+(a/b)\Delta\) is integral. In fact \(v-u\) is even: \(4kb(4b-a)/(a^2+b^2)=\Delta/b\) is even. These two odd base gaps and every simultaneous odd multiple satisfy the equations. An abstract edge on rational gaps by itself does not give the integer placements or the strip margins.

For clarity, a finite rational pattern made from these ratios on positive rationals of 2-adic valuation zero can be realized. Scale all vertices by an odd integer so that each edge is an integral odd multiple of its ordered base pair, reversing an unordered edge when needed. There are only finitely many odd denominators and base numerators to clear. Take a sufficiently large even \(h\), put an odd \(o\) near \(h/2\), and place all the leaves in the standard \(16h\)-column star. In local coordinates write
\[
 B=(4h+4(o+g),o+g),\quad D=(4h+4(o+g'),o+g'),\quad
 A=(B_x-u,o),\quad C=(D_x-v,o).
\]
The potentially shared corners are \(A+n,B+n\), with \(n=(C+D-A-B)/2\). This is an integer vector by the parity checks above. One has \(n\cdot(B-A)=0\) and \(|D-C|=|B-A|\), so these are a side rectangle and a diagonal rectangle with the same two shared corners. The vectors \(n\) and \(\Delta\) are nonzero. The diagonal cannot agree up to sign with the side since their positive vertical components are distinct. The odd points \(A,C\) differ because \(C_x-A_x=(4-a/b)\Delta\ne0\). All six coordinates are in the star for sufficiently large \(h\): the fixed offsets are independent of \(h\), while \(o\) and \(4h+4o\) lie in its interior. This proves the realization for every edge of the finite pattern simultaneously.

## High minimum degree and a 9-cycle

For \(b=1\), choose \(a>8\) odd with \(a\equiv8\bmod p\), where \(p>17\) is a prime that divides none of the preceding ratio numerators or denominators. The numerator of the ratio is \(-16\bmod p\), and its denominator is zero modulo \(p\). The resulting positive ratios, one for each new prime, are multiplicatively independent: projecting a relation onto its newest prime forces the exponent of the latest generator to vanish, and then one argues backwards. For any \(d\) such generators \(r_1,\ldots,r_d\), the \(2^d\) distinct products \(\prod_j r_j^{\epsilon_j}\), \(\epsilon_j\in\{0,1\}\), contain a \(d\)-dimensional cube. Clearing denominators and choosing the strip as above gives minimum degree at least \(d\) on a set of retained gaps. Thus the degeneracy is unbounded even with true in-strip geometry. The cube gives no lower bound exceeding two for the chromatic number.

The crossed graph also has this odd cycle on positive gaps:
\[
 2035,\ 1517,\ 1147,\ 2597,\ 371,\ 53,\ 3445,\ 2635,\ 2125,\ 2035 .
\]
It already occurs at \(h=8192,o=4095,c=4h\). In the table \(g\) is the side gap, \(g'\) the diagonal gap. The order of the two may differ from the cycle traversal. Substituting the listed horizontal offsets in the formulas for \(A,B,C,D\) independently checks all nine supports.

| \(g\) | \(g'\) | \(a\) | \(b\) | \(k\) | \(u\) | \(v\) |
|---:|---:|---:|---:|---:|---:|---:|
|2035|1517|−3|1|−185|−185|1369|
|1517|1147|9|1|1517|1517|−1813|
|2597|1147|−9|5|−53|−265|2345|
|2597|371|1|1|−371|−371|−2597|
|371|53|1|1|−53|−53|−371|
|3445|53|33|4|3445|13780|−14204|
|3445|2635|19|9|−65|−585|−2295|
|2125|2635|7|1|−2125|−2125|1445|
|2125|2035|13|1|425|425|−745|

For each row the six points are distinct. Direct substitution puts their columns between 49,148 and 63,564 and their rows between 2,399 and 7,540. Thus two colors do not suffice even for this one family. Whether a bounded palette of at least three colors suffices for all heights remains open.
