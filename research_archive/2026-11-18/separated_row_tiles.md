# Filled blocks for separated odd and even row intervals

Let \(I\) consist of \(p\) consecutive odd rows and \(J\) of \(q\) consecutive even rows in the strip, for distinct odd primes \(p,q\). Either interval may be the higher one. Put \(P=pq,\ S=P-1,\ d=2\max(p-1,q-1)\), and \(g=\min_{a\in I,b\in J}|a-b|\). Assume the intervals have disjoint convex hulls and
\[
 g>\max(2S^2,\ S+d).
\]
There is a filled block of \(P\) columns containing every pair in \(I\times J\) once. Every column is a double. The block has no tilted black corner triple, mixed quadruple with nonvertical side, or in-strip parity rival. Arbitrary deletions of a single endpoint in any subset of columns preserve these exclusions. This gives filled blocks for arbitrary subsets of the prescribed labels.

Choose units \(u\bmod p,v\bmod q\) such that \(1+u^2,1+v^2\) are quadratic nonresidues in their respective fields. Such a unit exists at every odd prime \(\ell\). There are \(\ell-1\) pairs satisfying \(z^2-t^2=1\), by factoring its left side, so the sum over \(t\) of the quadratic character of \(1+t^2\) is \(-1\). The value at \(t=0\) is 1. In column \(x=0,\ldots,P-1\), use the two rows uniquely specified by
\[
 x\equiv u a\pmod p,\quad a\in I,\qquad x\equiv v b\pmod q,\quad b\in J.
\]
Each interval gives one representative per residue, since its row step is 2. The Chinese remainder theorem proves the label count.

Inside either row interval write \(\ell,w\) for its prime and slope. A nonhorizontal chord \((X,Y)\) has \(Y\not\equiv0\bmod\ell\) and \(X\equiv wY\bmod\ell\). Its length is nonintegral, since its squared norm is a nonresidue. Two tilted chords from that interval cannot be perpendicular, since their dot product reduces to \((1+w^2)Y_1Y_2\ne0\bmod\ell\). If a tilted triple uses both intervals, one leg has vertical magnitude at least \(g\) and the other at least 1. The product exceeds \(S^2\), the maximum horizontal product.

For a mixed pair write \(U=B-A,\ V=F-E,\ H=E+F-A-B\), with \(U\) the nonvertical black side and \(V\) the black diagonal. The equations are \(|U|=|V|,\ U\cdot H=0,\ H\ne0,\ V\ne\pm U\). Each horizontal length is at most \(S\) and \(|H_x|\le2S\).

* If both chords are in one row interval, a horizontal side forces a horizontal diagonal by the nonintegral length test. Otherwise reduce the norm equation modulo \(\ell\) and interchange \(E,F\) so that \(V_y\equiv U_y\). The perpendicularity gives \(H_y\equiv0\bmod\ell\). As 2 is invertible, \(E_y\equiv A_y,\ F_y\equiv B_y\bmod\ell\). Uniqueness of the row representatives upgrades both congruences to equalities. Thus \(H_y=0\), and \(U_x\ne0\) forces \(H=0\).
* If each chord lies in its own interval, \(|H_y|\ge2g\). A nonhorizontal side would give \(|U_yH_y|>2S^2\ge|U_xH_x|\). A horizontal side again forces a horizontal diagonal, which gives \(V=\pm U\).
* A chord crossing between the intervals has length at least \(g>S+d\), and a within-interval chord has length at most \(S+d\). They cannot have equal length.
* If both chords cross, then \(|U_y|\ge g>2S^2\). Perpendicularity alone forces \(H_y=0\) and then \(H_x=0\).

Finally a nonvertical chord between opposite-parity rows must cross between the intervals. Its squared length lies strictly between \(Y^2\) and \((|Y|+1)^2\), since \(0<X^2\le S^2<2|Y|+1\). It cannot be the diagonal opposed to a vertical owner, even if the owner is placed arbitrarily far away. Together with the distinct parity labels these facts give validity by the paper's [reduction lemma](../../papers/extremal/sections/sec5_threshold.tex).

## Covering every label at quadratic total width

Index the odd and even rows independently starting at 0, and pad their Cartesian product to an \(N\)-by-\(N\) square with \(N\) a power of two less than \(2h\). Subdivide aligned dyadic squares into quadrants. Discard squares with no actual labels. For side \(b=1\), put the one desired double in a one-column block. For \(b\ge2\), stop on a nonempty square if its minimum gap between physical odd and even rows exceeds \(1024b^4\). Otherwise subdivide.

For a stopped square take primes \(b<p<2b<q<4b\), by Bertrand's postulate. Extend the odd row list to \(p\) consecutive odd rows of the strip and the even list to \(q\) consecutive even rows. The gap assumption ensures that the strip has room to do this, including at its boundary. The new gap is at least \(1024b^4-12b\), since the extended intervals add at most \(2(p-1)+2(q-1)\) in the direction of the other interval. Their span parameters satisfy \(S<8b^2,\ d<8b\). Thus the filled-block theorem applies. At columns belonging to labels outside the stopped square delete one endpoint. The block now has precisely the desired doubles. Its width is at most \(8b^2\), including every singleton. The stopped squares are disjoint, so their total filled width is at most \(8N^2=O(h^2)\).

There are \(O(h^{3/2})\) nonempty blocks. For any stopped or unit square of side \(b\) its parent failed the stopping rule and contains an actual pair at gap at most \(1024(2b)^4\). All cells in the parent, including padded cells, are within index distance \(O(b^4)\) of the diagonal. At side \(b\) this allows at most \(O(N\min(N,b^4)/b^2)\) squares, by counting their disjoint cells. Summing over dyadic \(b\le N^{1/4}\) gives \(O(N^{3/2})\) by summing \(Nb^2\). Summing \(O(N^2/b^2)\) above that scale gives the same bound. A root with no parent, if present, contributes at most one block.

In particular the construction uses no external choice of singleton rows *inside* the blocks. What remains is to place the blocks and fill the joins so that no obstruction uses points from more than one block. A width estimate on the disjoint intervals by itself gives no threshold bound. A sufficient condition would be a global arrangement with \(O(h^2)\) total additional columns and no cross-block obstruction. Even for the far-from-diagonal squares, this permits an average joining cost of order \(\sqrt h\) when there are order \(h^{3/2}\) blocks. The paper's general quadratic locality radius per join exceeds this budget.

