# A quantitative exceptional set for the first Pythagorean leg

Let \(E(n)=\min_{d<d',\,d,d'\mid n}\log(d'/d)\), with \(E(1)=\infty\). Put \(\alpha=\log 3-1\). For each fixed \(\beta>\alpha\) there exists \(c_\beta>0\) such that
\[
 \#\{n\le x:E(n)\le(\log x)^{-\beta}\}
 \ll_\beta x(\log x)^{-c_\beta}. \tag{1}
\]
This is a quantitative version, with fixed exponent slack, of the lower divisor-spacing estimate used in [the constant-star window note](divisor_spacing_star_window.md). The proof uses the weighted divisor-pair method of Erdős and Hall. Here a finite partition of the sizes of the smaller divisor gives a power of \(\log x\) in the exceptional-set estimate. [Erdős and Hall](https://www.renyi.hu/~p_erdos/1979-26.pdf)

## Two multiplicative estimates

Use the modulus-one case of Shiu's theorem. In an interval \((U,U+V]\) with \(U^{1/3}\le V\le U\), a multiplicative \(0\le f\le1\) satisfies
\[
 \sum_{U<n\le U+V}f(n)
 \ll \frac V{\log(2U)}
       \exp\left(\sum_{p\le 2U}\frac{f(p)}p\right).
\]
Taking the full range up to \(K\) (or summing dyadic intervals) gives the analogous bound with \(K\) in the numerator and \(\log(2K)\) in the denominator. These applications satisfy the size and prime-power hypotheses since \(f\le1\). [P. Shiu, *A Brun–Titchmarsh theorem for multiplicative functions*, Theorem 1](https://doi.org/10.1515/CRLL.1980.313.161)

Write \(\Omega_Y(n)\) for prime factors counted with multiplicity, retaining just primes at most \(Y\). For \(z=1/3\), put \(f_Y(n)=z^{\Omega_Y(n)}\); it is completely multiplicative. Mertens' estimate for the prime harmonic sum and the preceding full-range bound give, uniformly for \(K,Y\ge2\),
\[
 \sum_{k\le K}f_Y(k)\ll K\{\log(2\min(K,Y))\}^{-2/3}.
 \tag{2}
\]
With a larger absolute constant this holds down to \(K=1\). On an interval as above whose upper endpoint is at most \(Y\), \(f_Y=z^{\Omega}\), and the interval mean is \(O((\log(2U))^{-2/3})\).

Fix \(1<A<2\) and let \(Q(A)=A\log A-A+1>0\). For \(2\le Y\le x\),
\[
 \#\{n\le x:\Omega_Y(n)>A\log\log Y\}\ll_A x(\log Y)^{-Q(A)}.
 \tag{3}
\]
Indeed \(A^{\Omega_Y}=1*g\), with \(g(p^j)=(A-1)A^{j-1}\) for \(p\le Y\), \(j\ge1\), and \(g(p^j)=0\) otherwise. Hence the mean is bounded by
\(\prod_{p\le Y}(1+(A-1)/(p-A))\ll_A(\log Y)^{A-1}\).
Markov's inequality gives (3). This proof of (3) handles repeated small prime factors.

## Counting close pairs

Let \(L=\log x\), \(\eta=2L^{-\beta}\). A pair achieving \(E(n)\le L^{-\beta}\) can be divided by its gcd to give coprime integers \(u<v\le(1+\eta)u\) with \(uv\mid n\). Thus \(n=kuv\) and \(u\le\sqrt x\). We may drop the coprimality restriction while upper-bounding these triples.

Choose \(0<\gamma_0<\min(\beta,1)\) fixed. For \(u\le 2\exp(L^{\gamma_0})\), the unweighted count is
\[
 \ll x\sum_{u\le2\exp(L^{\gamma_0})}\frac{\eta u}{u^2}
 \ll x L^{\gamma_0-\beta}.
\]
Here an interval \((u,u+\eta u]\), with integral \(u\), has at most \(\eta u\) integers. This avoids a short-interval estimate for small divisors.

For the larger divisors group \(u\) into dyadic boxes \([U,2U)\). First take \(U\le x^{1/4}\). Partition \([\gamma_0,1]\) into finitely many intervals \([s,t]\) of length at most \(\Delta\), and use each one for boxes with \(L^s\le\log U\le L^t\), assigning overlapping endpoints once. For this group set \(Y=\min(x,4\exp(L^t))\). This covers \(u\) and \(v\), and \(\log Y\asymp L^t\). Omit the integers exceptional in (3) for any one of these \(Y\)'s, and for \(Y=x\). Their combined number is \(O_{\beta,A,\Delta}(xL^{-\gamma_0Q(A)})\).

For each remaining integer \(n\), \(1\le(\log Y)^{A\log3}f_Y(n)\). We therefore count weighted triples, using \(f_Y(kuv)=f_Y(k)f_Y(u)f_Y(v)\). In a box \(U\), Shiu's estimate on \(v\) gives \(O(\eta U(\log U)^{-2/3})\) for each \(u\): the length \(\eta u\) is at least \(u^{1/2}\) for these \(U\) once \(x\) is large. Summing \(f_Y(u)\) gives \(O(U(\log U)^{-2/3})\). Finally use (2) for \(k\le x/U^2\). In this range \(x/U^2\ge x^{1/2}\), so the remaining logarithmic factor is \(O((\log Y)^{-2/3})\). The weighted total per box is at most
\[
 C x\eta (\log U)^{-4/3}(\log Y)^{-2/3}.
\]
Summing the dyadic \(U\)'s costs at most \(C L^{-s/3}\) in place of \((\log U)^{-4/3}\), by the tail of \(\sum j^{-4/3}\). After the typical-integer multiplier, the exponent of \(L\) in this group's bound, apart from the initial \(x\), is at most
\[
 -\beta+t(A\log3-2/3)-s/3
 \le -\beta+(A\log3-1)+\Delta/3.
\]

For the final boxes \(x^{1/4}<U\le\sqrt{x}\), take \(Y=x\). Both \(u,v\) contribute the same two powers giving \(L^{-4/3}\). The \(k\)-sum contributes the factor \((\log(2x/U^2))^{-2/3}\). Over dyadic \(U\) that last factor sums to \(O(L^{1/3})\), including the top box where \(x/U^2\) is bounded. The resulting bound is \(O(xL^{-\beta+A\log3-1})\).

Choose \(A>1\) sufficiently close to one and \(\Delta>0\) sufficiently small that \(A\log3-1+\Delta/3<\beta\). Every contribution then has a fixed negative exponent of \(L\). This proves (1).

## Application to a random sea row

For odd \(n>1\) the least positive horizontal leg is \(n\sinh E(n)\). Fix \(b>\alpha\) and let \(H\le h/(\log h)^b\). Choose \(0<\delta<b-\alpha\). There are \(O(h/(\log h)^\delta)\) possible positive gaps \(n<h/(\log h)^\delta\). For larger gaps, if a horizontal leg is at most \(H\), then
\[
 E(n)\le \operatorname{arsinh}(H/n)\le(\log h)^{-(b-\delta)}.
\]
Apply (1) with \(x=h\) and \(\beta=b-\delta\). Thus the number of possible odd vertical gaps is \(O_b(h/(\log h)^{c'_b})\) for some \(c'_b>0\). This bound includes legs whose competing vertical would fall outside the strip.

For a fixed leaf row and a sea chosen uniformly in any one residue class modulo a fixed integer, each unsigned gap has at most two preimages among \(\gg h\) sea choices. The probability of a short rival is consequently \(O_b((\log h)^{-c'_b})\). This applies, for example, to \(H=\lfloor h/(\log h\log\log h)\rfloor\) by using \(b=3/4\). A fixed number of independent trials then gives any prescribed negative power of \(\log h\). This argument controls the possible sea-to-leaf rivals. It provides no direct saving for the mean number of true-to-true forbidden distances on a fixed diagonal.
