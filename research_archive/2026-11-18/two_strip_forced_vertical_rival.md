# A vertical rival forced by the two-strip guards

Consider the filled Hilbert board in [the two-strip construction](hilbert_two_strip_joins.md). The singleton rule at its joins produces a vertical rival at every sufficiently large height. The same obstruction survives if each of the first guard's columns can choose either representative from the preceding core.

## A restriction near any double

Suppose a column \(c\) contains the opposite-parity rows \(r<s\), with \(g=s-r\). Take an even integer \(X>0\) with \(X^2+g^2=L^2\), and set \(j=(L-g)/2\). Assume \(r-j\ge1\), \(s+j\le h\), and that all opposite-parity pairs have owners. A black point in either row \(r\) or \(s\) at column \(c+X\) precludes validity. The conclusion also holds at \(c-X\) when that column is in the board.

Indeed one of the two points of the double and the proposed point form an oblique diagonal of length \(L\). Its midpoint lies on the column \(c+X/2\). The vertical segment centered there has the opposite-parity rows \(r-j,s+j\). If their owner lies in a different column, pairing the vertical segment with the owner's side or the oblique diagonal gives two distinct rectangles with identical presentations. If the owner is at the midpoint column, the oblique and vertical segments are both fully black diagonals. Reflect the oblique diagonal by swapping its two endpoint columns. This third diameter is distinct and in the strip. Pairing it with each of the two black diagonals again gives the collision.

## Unit tiles

The aligned index square \(\{6,7\}\times\{8,9\}\) uses odd rows \(13,15\) and even rows \(18,20\). It and all its ancestors fail the stopping criterion, since they contain a row pair at gap at most seven. Thus these four labels are four consecutive unit cores. Their vertical gaps belong to \(\{3,5,7\}\). For each of them take \(X=(g^2-1)/2\), \(L=(g^2+1)/2\). Then \(X\le24\), and \(j=(g-1)^2/4\le9\). The vertical alternative is in the strip when \(h\ge29\).

At each internal join the first \(D=2K\) columns are prescribed the preceding core's even row. For \(K\ge12\), the column at distance \(X\) from that core lies in this strip. The preceding restriction excludes both the odd and even rows of the core there. Thus neither the prescribed choice nor an arbitrary choice between those two rows can work throughout the first strip.

## Arbitrarily large tiles

The obstruction also occurs at a side \(b\) growing like \(h^{1/4}\). For the prime pair \(b<p<2b<q<4b\), put \(P=pq<8b^2\). Choose a multiple \(t\) of \(2P\) with \(40b^2\le t<56b^2\). Set \(g=t^2-1\), \(X=2t\), \(L=t^2+1\), so \(j=1\).

Choose an aligned \(b\)-square containing a pair at gap \(g\), with both representative rows in the interior. This can be done when \(h\ge 4000b^4+20b\). For example take the odd index \(i=2b\), let the even index be \(i+(g-1)/2\), and take the aligned square containing that cell. It and its parent are inside the padded index square. All row gaps in the \(b\)-square differ from \(g\) by at most \(4b\). Its minimum therefore exceeds \(1024b^4\), whereas its parent contains the pair at gap \(g<16384b^4\) and must be subdivided. Every ancestor fails for the same reason. The square is a terminal core. Taking a dyadic \(b\) within a fixed factor of \((h/5000)^{1/4}\) gives such a tile for all sufficiently large \(h\). This statement uses a prime pair fixed at the scale \(b\), as in the usual choice of Bertrand primes. If a construction chooses primes separately for every tile after inspecting its rows, the unit-tile obstruction still applies.

Let \(c\) be the true column assigned the pair at gap \(g\). Since \(P\mid X\), at \(c+X\) both of the source system's row representatives repeat those at \(c\). Also \(P<X<112b^2\). If the outgoing guard exists and \(K\ge112\), this location lies in the first strip of its join. At an end core one can use the incoming strip and \(c-X\) instead. The restriction near a double gives the collision regardless of the two modular slopes, horizontal translation, or the choice of either repeated representative.

For any one fixed constant \(J\), the set of gaps \(g\le h\) for which \(j(g+j)\) is a square for some \(1\le j\le J\) has size \(O_J(\sqrt h)\). Consequently one may discard all original tiles whose intervals can attain one of these gaps and still discard only \(O_J(h^{7/4})\) labels: their sides are \(O(h^{1/4})\), so the label's own offset differs from such a gap by \(O(h^{1/4})\). This counts the labels affected by short-overhang in-core failures. New guard assignments after removal, and P chords between distant systems, require further arguments. The forced collisions above apply to the stated filled board; they give no lower bound for \(m_h\).

