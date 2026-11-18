# The normal order of the first vertical rival in a constant-row star

Consider the [quadratic-width construction on short windows](all_obstructions_short_windows.md). Every column of an odd star has a point in its center row \(o\). An even leaf in row \(e\) has signed gap \(e-o\), and its column lies more than \(2h\) from either end of the star. Write \(n=|e-o|\). A short rival can use any point of the constant row at horizontal distance \(X\) from this leaf. The minimum arithmetically possible \(X\) has a known normal order.

## Minimum Pythagorean leg for a given odd gap

For an odd integer \(n>1\), let
\[
 E(n)=\min_{d<d',\,d\mid n,\,d'\mid n}\log(d'/d).
\]
Then the least positive \(X\) for which \(X^2+n^2=L^2\) with \(L\) integral, and its corresponding hypotenuse, are
\[
 X_{\min}(n)=n\sinh E(n),\qquad L_{\min}(n)=n\cosh E(n).
\]
Indeed, write \((L+X)/n=v/u\) in lowest terms. Then \(L-X=nu/v\), so \(u,v\mid n\) and \(uv\mid n\). Conversely take divisors \(d<d'\), cancel their gcd, and obtain \(u<v\) coprime with \(uv\mid n\). The two integers
\[
 X=\frac{n}{uv}\frac{v^2-u^2}{2},\qquad
 L=\frac{n}{uv}\frac{v^2+u^2}{2}
\]
give the desired triangle. Since \(n,u,v\) are odd, \(4\mid X\) and \(L\) is odd. The displayed formulas follow by minimizing over ratios, since \(\sinh t\) increases for \(t>0\). The gap \(n=1\) has no nonzero horizontal leg.

For any particular row pair, the minimum leg is a true in-strip rival whenever the strip extends at least
\[
 j_{\min}(n)=\frac{L_{\min}(n)-n}{2}
\]
rows below the smaller row and above the larger one. Its proposed vertical endpoints have opposite parity and are integral. The column of the vertical lies halfway between the leaf and its selected sea point. All four rectangle corners are in the strip under this margin and the star-interior condition \(X_{\min}\le h\).

## The window exponent for these stars

Put \(\alpha=\log 3-1\). The divisor-spacing theorems of Erdős–Hall and Maier–Tenenbaum give
\[
 (\log n)^{-\alpha-\eta}\le E(n)\le(\log n)^{-\alpha+\eta}
\]
outside \(o(x)\) integers \(n\le x\), for each fixed \(\eta>0\). Restricting to odd integers preserves these exceptional-set estimates. The lower inequality follows from the theorem of Erdős and Hall using \(d\le n\); the upper inequality is implied by Theorem 1 of Maier and Tenenbaum. Both estimates are used only with fixed slack in the exponent. [Erdős and Hall, *The propinquity of divisors*](https://www.renyi.hu/~p_erdos/1979-26.pdf) and [Maier and Tenenbaum, *On the set of divisors of an integer*, Theorem 1](https://deepblue.lib.umich.edu/bitstream/handle/2027.42/46612/222_2005_Article_BF01388495.pdf)

**Almost all leaves can be retained below the transition.** For every fixed \(\epsilon>0\) put \(H=\lfloor h/(\log h)^{\alpha+\epsilon}\rfloor\). There is a filled \(O(h^2)\)-width core with \(q_h-o(h^2)\) labels and no black obstruction of span at most \(H\). To see this, first restrict to gaps \(n\ge h/(\log h)^{\epsilon/3}\), costing \(o(h)\) gap values. Outside \(o(h)\) additional exceptions, the lower bound with \(\eta=\epsilon/3\) gives
\[
 X_{\min}(n)\ge n E(n)
 \ge h(\log h)^{-\alpha-2\epsilon/3}>H .
\]
This handles all possible rival pairs in those windows, irrespective of the location of the owner of the corresponding vertical. The other deletions in the short-window proof use \(O(H)=o(h)\) signed gaps for the small-gap and nonvertical mixed tests. Each omitted signed gap costs \(O(h)\) labels.

**Almost all leaves must be removed above the transition for this construction.** For \(0<\epsilon<\alpha\), let \(H=\lfloor h/(\log h)^{\alpha-\epsilon}\rfloor\). Any subset of leaves in these same constant-row stars with every window of span \(H\) free from strip rivals has \(o(h^2)\) leaves. Indeed discard the \(O(h^{3/2})\) labels with \(n<\sqrt h\). Outside \(o(h)\) exceptional gaps, use the upper bound with \(\eta=\epsilon/3\). Uniformly for these \(n\) one has
\[
 X_{\min}(n)\ll h(\log h)^{-\alpha+\epsilon/3}=o(H),\qquad
 j_{\min}(n)\ll h(\log h)^{-2\alpha+2\epsilon/3}=o(h).
\]
For a concrete boundary margin set \(B=\lceil h(\log h)^{-\alpha+\epsilon/3}\rceil\). At most \(O(hB)=o(h^2)\) row pairs have an endpoint within \(B\) rows of a boundary. All other pairs have more room than \(j_{\min}\) requires. The center-row point at the required horizontal distance is available independently of the retained leaf set. Thus keeping any one of these remaining typical labels puts a true strip rival inside a window of span \(H\). This argument requires the full constant row of the star to remain present.

These bounds identify the transition up to \((\log h)^{o(1)}\) for retaining nearly all labels in this family under the local obstruction test. They give no lower bound on the full threshold \(m_h\) over other layouts. The positive assertion supplies a partial core; the \(o(h^2)\) estimate for its omitted labels alone gives no quadratic-cost relocation.

## Cost of deleting leaves or changing the constant sea

There is also a quantitative tradeoff for modifications to the star at fixed leaf positions. Write \(R=h/H\), with \(1\le R\le h^{1/3}\), and let \(D(R)=\max_{n\le C(2+R)^2}\tau(n)\) for a sufficiently large absolute \(C\). For every odd center \(h/4\le o\le h/2\), a star in which all span-\(H\) strip rivals have been removed requires
\[
 \#\{\text{removed original leaves}\}
 +\#\{\text{columns missing the original center-row point}\}
 \ \gg\ \frac{h}{R D(R)} .
\]
A leaf moved from its prescribed column counts as removed at that column. The estimate only uses original black cells, so adding replacement cells cannot repair the exhibited rivals while leaving both original endpoints present.

Choose the even integers \(m\) in \([16R,32R]\), put \(B_m=m^2-1\), \(A_m=4B_m+2m\), and take positive odd \(k\) for which \(h/8\le kB_m\le h/6\). For sufficiently large \(h\), uniformly on this range there are \(\gg h/R^2\) such \(k\) for every \(m\). Consider the even leaf \(e=o+kB_m\) and the original center-row point at column \(c+4o+kA_m\), where \(c\) is the star's intercept. Their displacement has horizontal length \(2km\le H\) and vertical length \(k(m^2-1)\), with hypotenuse \(k(m^2+1)\). The alternative vertical extends just \(k\) rows above and below the two original rows. The chosen ranges of \(o,e,k\) put both ends in the strip. The alternative column is integral, its endpoints have opposite parity, and both black points lie in the star.

Join the leaf vertex \(g=kB_m\) to the column vertex \(t=kA_m\). Every such edge requires a deletion at one endpoint. The ratio \((t-4g)/g=2m/(m^2-1)\) determines \(m\), hence the graph has \(\gg h/R\) distinct edges. Bound the second moment of the degrees on either side. In both cases the multipliers \(M_m=B_m\) or \(A_m\) are distinct positive integers comparable to \(R^2\). Write \(n_d=\#\{m:d\mid M_m\}\); distinctness in an interval of length \(O(R^2)\) gives \(n_d\ll R^2/d\) whenever \(n_d>0\). Thus
\[
 \sum_{m,l}\gcd(M_m,M_l)
 =\sum_d\varphi(d)n_d^2
 \ll R^2\sum_d n_d
 \ll R^3D(R).
\]
The number of common multiples of \(M_m,M_l\) in the vertex range is at most \(O(h\gcd(M_m,M_l)/(M_m M_l)+1)\). This yields \(O(hD(R)/R+R^2)\) for the sum of squared degrees, on each side. For \(R^3\le h\), Cauchy–Schwarz applied to the degrees in any vertex cover gives the claimed lower bound.

There are \(\gg h\) disjoint central stars. At \(H=\lfloor h/(\log h)^\beta\rfloor\) for fixed \(\beta>0\), the maximal divisor bound gives \(D(R)=(\log h)^{o(1)}\). The total cost is therefore at least \(h^2/(\log h)^{\beta+o(1)}\). With the original center rows intact, this is a lower bound for the number of omitted leaves in this construction. In particular, a budget of \(O(h^2/\log^2 h)\) omissions rules out every fixed \(\beta<2\). A modification cost of one per altered sea column allows more freedom than relocating every affected label.
