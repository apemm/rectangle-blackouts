# A near-affine placement without vertical rivals

Fix \(0<\delta<1\) and an integer \(K\ge1\). Every signed odd diagonal can be placed in separate bands so that all parity labels together use \(O_{\delta,K}(h^2)\) columns and have no in-strip vertical rivals. Within each translated band, the column of rank \(i\) differs from \(8Ki\) by at most \(8Kh^\delta\). The mean number of bands per signed diagonal is bounded. Every true column can be a multiple of \(8K\), so \(K=784\) gives the period-seven slot modulus \(6272\).

The proof uses only part of the gap \(t=|T|\) in the modular shear. The uncaptured part has bounded divisor moments. It increases the number of Pell orbits on some diagonals, and the mean palette stays bounded. [Full-gap modular shear](modular_shear_packing.md)

## A divisor of small size

For \(t\le h\), set aside every prime power \(p^e\Vert t\) with \(e\ge2\) or \(p\mid 2K\). Sort the remaining primes in increasing order. Take their longest initial segment whose product \(q\) does not exceed \(h^\delta\). The empty product is one. Write \(m=t/q\). For every fixed \(A>0\),
\[
 \sum_{t\le h}\tau(m)^A\ll_{\delta,K,A}h. \tag{1}
\]

To prove (1), first bound the number \(R(t)\) of single-exponent primes left after the initial segment, excluding those dividing \(2K\). If \(R(t)\ge k\ge1\), their smallest member is at most \(y=h^{1/k}\). Multiplying \(q\) by this prime would exceed \(h^\delta\). Hence
\[
 S_y(t)=\prod_{\substack{p\mid t\\p\le y}}p>h^\delta .
\]
If \(y<2\) the event is empty. For \(\theta=k\log(2k)/\log h\), expansion over squarefree divisors and the bound \(\lfloor h/d\rfloor/h\le1/d\) give
\[
 \frac1h\sum_{t\le h} S_y(t)^\theta
 \le \prod_{p\le y}\left(1+\frac{p^\theta-1}{p}\right)
 \le \exp(Ck).
\]
The convexity of the exponential gives \(p^\theta-1\le(2k-1)\log p/\log y\), and the Chebyshev estimate gives \(\sum_{p\le y}(\log p)/p\ll\log y\). Markov's inequality bounds the proportion with \(R(t)\ge k\) by \(\exp(Ck-\delta k\log(2k))\). Thus \(2^{A R(t)}\) has bounded mean for every fixed \(A\).

The set-aside part \(b(t)\) also has bounded \(\tau(b(t))^A\) mean for every fixed \(A\). The multiplicative function \(\tau(b(t))^A\) is nondecreasing in each exponent. Expand it as a divisor sum with nonnegative coefficients and bound the mean by its Euler product. At \(p\nmid2K\) the local term is \(1+O_A(p^{-2})\), since value one persists through exponent one. At the finitely many \(p\mid2K\), the local series converges because \(\sum_{e\ge0}(e+1)^A p^{-e}\) does. Now \(m=b(t)\) times the product of \(R(t)\) distinct primes coprime to \(b(t)\). Cauchy's inequality proves (1). It also bounds the average over odd \(t\), and using both signs changes the count by at most a factor of two.

## The residual distance equation

Rank \(i\) has rows \(1+2i\) and \(1+2i+T\) in the strip. For each \(p\mid q\), choose a nonzero residue \(r_p\) such that \(64K^2r_p^2+4\) is a nonsquare modulo \(p\). The character sum \(\sum_x(\frac{1+x^2}{p})=-1\) gives a choice, since \(p\nmid 2K\). Choose \(r\bmod q\) by the Chinese remainder theorem. Put
\[
 j_i=q\lfloor i/q\rfloor+[ri]_q,\qquad x_i=8Kj_i .
\]
For \(q=1\) use \(j_i=i\). This permutes slots in each interval of \(q\) ranks and gives \(|j_i-i|<q\).

An opposite-role chord between distinct ranks has displacement \((8K(j_i-j_j),2d\pm T)\), where \(d=i-j\ne0\). If \(p\mid q\) and \(p\nmid d\), its squared length is the nonsquare \((64K^2r^2+4)d^2\bmod p\). Since \(q\) is squarefree, an integral length requires \(q\mid d\). Write \(|d|=q\ell\). The rank residues agree, so the slot difference equals \(d\). Its length divided by \(q\) is an integer, because its square is an integer and it is rational. With \(D=16K^2+1\), a surviving distance satisfies
\[
 z^2=4D\ell^2\pm4m\ell+m^2,\qquad
 (2D\ell\pm m)^2-Dz^2=-(4Km)^2 . \tag{2}
\]
For equal-role chords in one band the same reduction applies. When \(q\mid d\) their length is \(2|d|\sqrt D\), irrational since \(D\) lies strictly between \((4K)^2\) and \((4K+1)^2\). Thus every distinct-rank same-role chord in that band has irrational length.

## Distances in one dyadic interval

There are \(O_K(\tau(m)^{C})\) solutions \(\ell\) of (2) in each interval \([L,2L]\), with an absolute exponent \(C\). Write \(x=2D\ell\pm m,\ y=z>0\). For \(g=(x,y)>0\), one has \(g\mid4Km\). The primitive coordinates \(x'=x/g,y'=y/g\) have norm \(-n\), where \(n=(4Km/g)^2\). Then \((y',n)=1\) and \(x'/y'\bmod n\) is a square root of \(D\bmod n\). Interpret the root modulo one as a single class.

There are \(O_D(2^{\omega(n)})\) such roots. Each odd prime outside \(2D\) gives at most two roots at every exponent by lifting a simple root. For each fixed prime dividing \(2D\), the number is bounded independently of the exponent. Up to exponent \(v_p(D)\) this is a finite check. Beyond it a solution forces \(v_p(D)\) even, and division by that power of \(p\) reduces to a unit square root, with at most four unit roots and a bounded number of lifts.

Fix \(g\) and a root. Any two positive numbers \(\alpha=x'+y'\sqrt D\) from that root differ by a multiplicative unit of norm one in \(\mathbb Z[\sqrt D]\). To check this, divide the first by the second using its conjugate. The two numerator coefficients \(x'_1x'_2-Dy'_1y'_2\) and \(y'_1x'_2-x'_1y'_2\) are both divisible by \(n\), by the common residue. The quotient has integer coefficients and norm one. A positive norm-one unit greater than one is at least \(1+c_D\) for some \(c_D>0\). This follows since for such a unit \(\eta=a+b\sqrt D\), \(b=(\eta-\eta^{-1})/(2\sqrt D)\) is a positive integer.

On \(L\le\ell\le2L\),
\[
 g\alpha=x+\sqrt{x^2+(4Km)^2}\asymp_K L+m.
\]
For example, when \(L\ge m\), \(x\) is positive and comparable to \(L\). When \(L<m\), \(x/m\) ranges in a fixed compact interval and \(x/m+\sqrt{(x/m)^2+(4K)^2}\) stays positive. Thus a fixed root contributes \(O_K(1)\) solutions for each sign. Summing over \(g\mid4Km\) and the roots proves the stated dyadic bound, since \(\tau(4Km)\ll_K\tau(m)\) and \(2^{\omega(m)}\le\tau(m)\).

## Coloring distances with bounded dyadic counts

Suppose a set of positive integer distances has at most \(R\ge1\) members in each dyadic interval. It has a proper coloring on the integer line with \(O(R^2\log^2(2R))\) colors. I include the construction to keep the dependence on the number of Pell orbits explicit.

Take \(B\) a power of two with \((100R)^4\le B<2(100R)^4\), and \(J=R\log_2 B\). Each shell \([B^n,B^{n+1})\), \(n\ge0\), has at most \(J\) distances. Set \(\gamma=1/(100J)\). Treat even and odd indexed shells separately. For either family I construct a \(\theta\in[0,1]\) satisfying \(\|d\theta\|\ge\gamma\) for all its distances.

Start with \([0,1]\). Before a shell of lower endpoint \(A=B^n\), the interval from the preceding treated shell has length \(\gamma/(2(A/B))\), or the initial interval has length one. Thus for every current \(d\), its length times \(d\) is at least one. Indeed, in a later shell the product is at least \(\gamma B/2>1\). In any interval \(I\) with \(|I|d\ge1\), the proportion where \(\|d\theta\|<2\gamma\) is at most \(12\gamma\), by covering the rescaled interval by at most \(d|I|+2\) unit periods. All current distances together exclude at most \(12J\gamma<1/4\). Retain a point in the middle half of \(I\) outside that union. The centered subinterval of length \(\gamma/(2AB)\) remains inside \(I\) and has \(\|d\theta\|\ge\gamma\) for every current \(d<AB\). Nested compact intervals give the required \(\theta\). Taking equal arcs of length at most \(\gamma\) colors this family with \(O(J)\) colors by the arc containing \(\{\theta k\}\). The pair of colors from the two families excludes every distance.

Apply the coloring to the distances \(\ell\) in (2), and give rank \(i\) the color of \(\lfloor i/q\rfloor\). Any candidate \(q\ell\) has quotient ranks differing by \(\ell\). Thus each diagonal needs at most \(O_K(\tau(m)^{C'})\) colors for some fixed \(C'\). By (1) there are \(O_{\delta,K}(h)\) bands in total. Use a translated copy of the original local slot interval for each color and diagonal. Keep more than \(h\) columns between successive occupied intervals. Each interval, including its guard, uses \(O_K(h)\) columns since \(q\le h\). Any in-strip vertical rival has length less than \(h\) and cannot cross such a guard. Placing singleton points in boundary row 1 elsewhere preserves this particular exclusion, since a nonvertical diagonal with a vertical rival cannot meet the boundary row. The proof controls vertical rivals for the filled board.

## A true angle requires a short same-role leg

The near-affine placement also allows a bounded refinement in each band. On every diagonal with \(t\ge160K^2q\), each tilted right angle among true points within a refined band has a same-role leg whose rank difference is \(O_K(h^\delta)\).

Let \(E=q\). If both legs from the pivot cross roles, their dot product is odd. If both preserve the role and their rank lengths exceed \(8E\), their slopes have the same positive sign, since \(|(j_i-j_j)-(i-j)|<2E\). They cannot be perpendicular.

For a same-role leg with signed rank difference \(d\) and a cross leg with signed rank difference \(d'\), write the slot differences as \(d+a,d'+b\), with \(|a|,|b|<2E\). Orthogonality would imply
\[
 d'=\frac{\mp T-32K^2(1+a/d)b}{2+32K^2(1+a/d)} .
\]
When \(|d|\ge8E\) and \(t\ge160K^2 E\), the error in the numerator is at most \(80K^2E\). The denominator is between \(2+24K^2\) and \(2+40K^2\). Hence \(c_Kt\le |d'|\le C_Kt\) for positive constants depending only on \(K\). To exclude the entire interval, color \(i\) by \(\lfloor i/(c_K t/2)\rfloor\bmod M_K\), taking \(M_K>2C_K/c_K+3\). Ranks in the same interval differ by less than \(c_Kt\). Ranks in distinct intervals of the same color differ by more than \(C_Kt\). This multiplies the number of bands by a bounded factor.

If \(t<160K^2E\), the formula only gives \(|d'|=O_K(E)\) when \(|d|\ge8E\). To obtain the stated same-role conclusion uniformly, set aside all labels on \(t<160K^2h^\delta\) diagonals when using the angle refinement. These account for \(O_K(h^{1+\delta})\) labels. The vertical-rival theorem includes these diagonals without this removal. Equivalently, the short-leg conclusion applies directly to all diagonals with \(t\ge160K^2E\), and to the remaining ones only after a separate treatment.

The angle refinement does not address mixed four-point supports, filler collisions, or interactions between different bands. A proof of quadratic width for valid equality boards still needs those steps and the remaining short-leg cases.
