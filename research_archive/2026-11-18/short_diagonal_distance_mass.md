# The aggregate cost of short forbidden distances on affine diagonals

Fix the stride \(x_i=28i\) and true rows \(2i+1,\ 2i+1+T\) of the [random constant-row construction](random_constant_row_windows.md). Define \(D_T(H)\) as there. Uniformly for \(h^{7/8}\le H\le h\),
\[
 \sum_{|T|<h,\ T\ {\rm odd}} |D_T(H)\cap14\mathbb Z|
 \asymp H\log h\,(1+\log(h/H)).
\]
For the lower bound one can count only distances realized by pairs in the same residue class of indices modulo 14, with the alternative vertical endpoints inside the strip. Each distance counted by the proof occurs at \(\gg h\) pairs of indices on its own diagonal. This estimates the number of distances before coloring. It gives no lower bound of this order on the chromatic number.

The upper bound is the even-leg triangle count from the linked proof. For the lower bound choose a dyadic \(M\) with \(h^{1/4}\le M\le h^{1/3}/2\). Independently choose a dyadic ratio \(\lambda=2^{-j}\) with \(j\ge2\), \(\lambda\ge H/(8h)\). The number of such ratios is comparable to \(1+\log(h/H)\). Put \(N=\lambda M\), so \(N\gg h^{1/8}\). Use primitive Euclidean parameters
\[
 M\le m<2M,\quad N\le n<2N,\quad
 196\mid m,\quad n\equiv1\bmod392,\quad (m,n)=1.
\]
There are \(\gg MN\) choices uniformly in these boxes. For completeness, write \(m=196r\) and use Möbius inversion on \((r,n)\). Only divisors coprime to 392 matter. The main term is \(MN/(196\cdot392)\) times the product \(\prod_{\ell\nmid392}(1-\ell^{-2})\) over primes. Truncating the divisor sum at \(2N\) changes that main term by \(O(M)\). For each divisor the two progression counts have errors \(O(1)\). Their accumulated error is \(O((M+N)\log(2M))=o(MN)\). These estimates hold for the fixed progression moduli and the stated range of \(N\).

For each such pair choose an odd \(k\) in \([H/(8192MN),H/(4096MN)]\). There are \(\gg H/(MN)\) choices as \(M N\le h^{2/3}\). Put
\[
 X=2kmn,\qquad Y=k(m^2-n^2),\qquad L=k(m^2+n^2).
\]
Here \(X<H\), \(Y,L\) are odd, and \(392\mid X\). Moreover \(L\le5H/(4096\lambda)<h/80\), using \(n<m\) and the chosen ranges (the estimate \(m^2+n^2\le5M^2\) follows from \(2N\le M/2\)). Every box gives \(\gg H\) triples. The intervals for dyadic \(m\) and for \(n\) at fixed \(M\) are disjoint. Uniqueness of the primitive parametrization with specified even leg ensures that different triples of parameters give different pairs \((X,Y)\).

Map \((X,Y)\) to \(d=X/28\), \(T=Y-2d\). This is injective, \(14\mid d\), and \(28^2d^2+(T+2d)^2=L^2\). In particular \(T\) is odd with \(|T|<h/8\). Take an odd true row \(2i+1\) in \([h/3,h/2]\), and use the even point of index \(i+d\) in the same diagonal. Their row difference is \(T+2d=Y\). All four rows of the two labels fit in the strip. The indices agree modulo 14, their horizontal distance is \(X\), and the vertical alternative is centered at their midpoint with length \(L<h/80\). Its column and endpoint rows are integral by the parities of \(X,Y,L\). Both alternative rows lie strictly inside the strip and have opposite parity. There are \(\gg h\) admissible choices of \(i\).

Summing over the two dyadic parameters proves the assertion. In particular, charging a separate length-\(h\) band to each distance costs more than quadratic width if \(H\log h(1+\log(h/H))/h\) tends to infinity. A stronger coloring or a different placement could still handle those distances in quadratic width.
