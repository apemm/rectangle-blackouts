# Independent reflected phases for the two Hilbert traces

Use the ordinary parity partition and write \(n_o=\lceil h/2\rceil\), \(n_e=\lfloor h/2\rfloor\). For \(1\le H\le h\), there is a filled board of width \(O(h^2)\) carrying all labels except for
\[
 O\!\left(hH(1+\log H)\min\{1+\log H,1+\log(h/H)\}\right).
\]
Every opposite-parity nonvertical chord of horizontal extent at most \(H\) has nonintegral length. At every extent, a single row parity contains no tilted triple, nonvertical mixed support, or nonhorizontal integral chord. These conclusions exclude mixed supports having a horizontal principal chord. They leave longer opposite-parity chords and mixed-parity tilted and mixed supports.

In particular \(H=\lfloor h^{1-\epsilon}\rfloor\) for any fixed \(0<\epsilon<1\) costs \(O_\epsilon(h^{2-\epsilon}\log^2 h)\) omitted labels. Their number fits the positional block's quadratic width budget. The assertion here concerns the main core and the size of the exceptional set. Applying the positional block also requires a clean join.

## Two independent translations

For \(n\ge1\) define a periodic function \(w_n\) on the integers, of period \(2n\), by a single period of values
\[
 0,1,\ldots,n-1,n-1,\ldots,1,0 .
\]
The function is 1-Lipschitz on the integer line. A uniform random translate gives a uniform value among the \(n\) indices at every fixed input. Choose \(N\) dyadic with \(2\max(n_o,n_e)\le N<4\max(n_o,n_e)\). At rank \(r\) in the Hilbert order on \([0,N)^2\), write its coordinates as \(i_r,j_r\). Take independent uniform phases \(s_o\bmod 2n_o,\ s_e\bmod 2n_e\). The prospective rows are
\[
 a_r=1+2w_{n_o}(i_r+s_o),\qquad b_r=2+2w_{n_e}(j_r+s_e).
\]
Each coordinate range of the full square contains a complete period. Thus every actual odd-even label occurs at least once for every phase choice. Give every rank \(K\) columns, for the same absolute stretching constant as in [the short-rival filter](short_rival_filter.md). Put the odd row throughout and test the even row only in the first column of each rank.

The two reflected coordinate functions preserve the Hilbert diameter estimate, and neighboring ranks still change each physical row by zero or two. The one-parity proof of the short-rival filter applies to both traces, even before removing points. Zero vertical difference makes an axial chord. In a nondegenerate mixed support a horizontal principal chord forces the other chord to be in a single row parity by integrality of the common corners. That other chord cannot be nonhorizontal of the same length. A vertical same-parity chord is unavailable because each column has at most one point of that parity.

## Counting horizontal offsets

For a fixed candidate column \(z\) and an odd trace column \(z+X\), the even row at \(z\) and the odd row at \(z+X\) are independent and individually uniform over their row parities. The assertion holds when both columns come from the same rank. For each fixed \(y>0\), at most two odd rows can be at distance \(y\) from a given even row. Thus the probability of any specified absolute difference is at most \(2/n_o\).

Write \(T(H,h)\) for the number of positive pairs \((x,y)\) with \(x\le H,\ y<h\) odd in its second coordinate, and \(x^2+y^2=L^2\) for some integer \(L\). There are \(N^2=O(h^2)\) candidate columns. Summing the probability over candidates, both signs of \(X\), and all the pairs counted by \(T\), the expected number of witnesses is \(O(hT(H,h))\). Choose phases achieving at most this many. For each actual label keep one occurrence whose even point has no witness, if available. Every omitted label has at least one witness, and distinct labels use disjoint candidate ranks. Keeping the odd trace everywhere and only the selected even points gives the claims.

Factoring \((L-y)(L+y)=x^2\) gives \(T(H,h)\le\sum_{x\le H}\tau(x^2)\). At a prime power, \(2k+1\le(k+1)(k+2)/2\), so \(\tau(x^2)\le d_3(x)\). Summing ordered factorizations proves \(T(H,h)\le H(1+\log H)^2\).

A second elementary estimate is sharper near \(H=h\). Since \(y\) is odd, \(x\) is even, and every such triangle has the parametrization \(x=2duv,\ y=d(u^2-v^2)\), \(u>v\ge1\). Here one can drop the coprimality and parity restrictions for an upper bound. For each \(d\le H\) put \(A=H/d\). Since \(u^2+v^2=L/d\le2h/d\), we have \(u\le\sqrt{2h/d}\), and \(v\le\min(u,A/u)\). The sum over \(u\le\sqrt A\) is \(O(A)\), and over \(\sqrt A<u\le\sqrt{2h/d}\) is \(O(A(1+\log(h/H)))\). Summing over \(d\) gives \(T(H,h)=O(H(1+\log H)(1+\log(h/H)))\).

## Excluding tilted and mixed supports in every short interval

Let \(1\le L\le h\), independently of the rival radius \(H\). The same filled core can additionally exclude all tilted triples and nonvertical mixed supports of horizontal span at most \(L\) by omitting at most \(O(hL^2)\) more labels. Thus one can take \(H=h^{1-\epsilon}\) and \(L=h^{1/2-\epsilon}\) simultaneously, for \(0<\epsilon<1/2\), and omit a power-saving fraction of the labels.

Choose an absolute constant \(C\) large enough that either physical trace has row diameter at most \(C\sqrt{L+1}\) throughout any interval of \(L+1\) columns. The Hilbert estimate, the stretching, and the Lipschitz folding give this for every choice of phases. Omit all labels of absolute gap at most
\[
 2L^2+2C\sqrt{L+1}.
\]
For each positive gap there are at most \(h\) labels, giving the asserted cost. If a candidate obstruction in an interval contains an even point, that point is at a retained double. Hence throughout the interval the odd rows and the even rows lie in disjoint bands with a common separation greater than \(2L^2\).

At a cross-role tilted triple at least one leg joins the two bands, and the other tilted leg has nonzero integer vertical magnitude. Their vertical product thus exceeds \(L^2\), while the horizontal product has magnitude at most \(L^2\). A single-role triangle is already excluded.

For a mixed support use \(U\) for the nonvertical side chord, \(V\) for its black diagonal, and \(M\) for the difference of doubled midpoints. Both chords lie within single parities, or both join the two parities, by the even total of the four black rows. In a two-role case of the former type, \(|M_y|>4L^2\). A nonhorizontal side has \(|U_yM_y|>2L^2\), contradicting \(|U_xM_x|\le2L^2\). Horizontal principal chords have already been excluded. In the latter type \(|U_y|>2L^2\). Thus \(U\cdot M=0\) forces \(M_y=0\) and then \(M_x=0\), impossible for a nondegenerate support. The single-role and vertical-owner cases are covered by the earlier exclusions, with radius at least \(L\) for the last case.
