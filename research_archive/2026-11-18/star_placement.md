# A star placement with no tilted corner triples

Use one star for each odd row \(o=2i+1\). Its leaves are the even rows \(e_n=2n+2\), \(0\le n<\lfloor h/2\rfloor\). Let \(P\) be the least power of two at least \(\lfloor h/2\rfloor\), and let \(\pi\) be a permutation of \([0,P-1]\) preserving \(v_2(n-n')\) for unequal inputs. Color the leaves in star \(i\) by \(c_{i,n}\in[0,C_i-1]\). Put
\[
 A=2^{\lfloor\log_2(32h)\rfloor+1},\quad
 L_i=\sum_{j<i}(C_j+1),\quad
 x_{i,n}=A(L_i+c_{i,n})+8\pi(n).
\]
In this column put the odd center and the even leaf. The distinct columns lie in \(8\mathbb Z\). The total width is at most \(A\sum_i(C_i+1)+8P\).

**Proposition.** The black label points contain no tilted right angle, for any choices of colors.

For an even-to-even tilted chord take differences \(X,Y\) in coordinates. If \(n=n'\), the chord is horizontal. Otherwise
\[
 v_2(X)=3+v_2(n-n'),\qquad v_2(Y)=1+v_2(n-n').
\]
The large \(A\)-summand cannot change the first valuation since \(2^{3+v_2(n-n')}\le4P<A\). For a mixed-parity tilted chord \(Y\) is odd and \(8\mid X\). Thus every tilted chord meeting an even point satisfies \(v_2(X)>v_2(Y)\). If two such chords were perpendicular, their horizontal and vertical products would have different valuations.

It remains to consider an odd pivot with an odd leg endpoint. A tilted odd-to-odd chord connects distinct stars, at star distance \(d\ge1\), with \(|Y|=2d\). The band indices \(L_i+c_{i,n}\) in these stars differ by at least \(2d\), and the residual term has absolute difference less than \(8P\le8h\). Hence \(|X|>32hd\). Every other tilted chord has \(|Y'/X'|\le(h-1)/8\). The product of these absolute slopes is less than one. Two mixed chords at an odd pivot were already excluded by their valuations. This proves the assertion for the infinite ambient strip.

**Vertical rivals.** Endpoints at an in-strip vertical-rival distance have opposite parity and distance at most \(h-1\). Chords between different bands have horizontal length \(A-8P>h\) or greater. Inside a band define an edge on distinct leaf indices \(n,n'\) whenever
\[
 64(\pi(n)-\pi(n'))^2+(2n+2-o)^2
\]
or the expression with \(n'\) in the vertical term is a square at most \((h-1)^2\). A proper coloring of this graph for each star excludes every such rival between distinct labels. The vertical pair of a double cannot itself serve as the distinct diagonal in a mixed presentation with the same vertical common pair.

The [coloring program](star_palette.py) lists primitive Pythagorean triples and their odd multiples, adds both possible horizontal signs and checks each color against every generated edge. Both the modular odd-multiplier permutation and the binary tree permutation used at most five colors at heights 383, 1025, 2049, 4097 and 8193. At height 8193 the tree computation included 22,756,145 directed norm events, with 2,141 stars using four colors and the remaining 1,956 stars using five. These are finite computed colorings. Bounding \(\sum_i C_i=O(h)\), or even finding another permutation with that property, remains open. Horizontal stars also leave mixed supports and the problem of filling the other columns.

For example the linear permutation allows a mixed collision inside a single star. At height 996 take center row 129 and use \(t=e-129\). In coordinates translated horizontally and vertically the two endpoints at parameter \(t\) are \(O(t)=(4t,0)\) and \(E(t)=(4t,t)\). Put the four indicated leaves in the same band. Take the side \(O(867),E(833)\) and the diagonal \(E(577),O(731)\). The common corners are \((2684,-128),(2548,705)\); adding 129 to their rows gives 1 and 834. The side and diagonal vectors are \((-136,833)\) and \((616,-577)\) with equal squared norm 712385. The perpendicular shift from the side is \((-784,-128)\), since their dot product is zero. This remains a pair of rectangles with the same presentation after any further black cells are added.
