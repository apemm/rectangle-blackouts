# Choosing a stride for each diagonal in short windows

Write \(\gamma=\sqrt3-1\). For every fixed \(\varepsilon>0\), at every sufficiently large height there is a filled board of width \(O_\varepsilon(h^2)\) carrying each parity label once, such that every window of horizontal span
\[
 H=\lfloor h/(\log h)^{\gamma+\varepsilon}\rfloor
\]
distinguishes all the rectangles it contains. The construction checks local vertical rivals against the full set of parity owners. The previous [constant-row theorem](random_constant_row_windows.md) gives exponent \(1+\varepsilon\). The [single-stride lower estimate](short_diagonal_distance_mass.md) explains why counting all distances of a single stride cannot give this improvement.

## Slopes and assignment

Choose \(r\) fixed distinct odd multiples \(u_j\) of seven such that the squarefree kernels of \(\Delta_j=4u_j^2+1\) are pairwise coprime and exceed one. For instance start at seven and choose each next \(u\) divisible by seven and the product of all preceding \(\Delta_j\). The new \(\Delta\) is congruent to one modulo every preceding prime divisor and lies between consecutive squares. Write \(\chi_j\) for the quadratic character of the resulting squarefree kernel. These are independent characters on the reduced classes of a fixed common modulus: each nonempty product has a prime dividing its conductor that divides none of the other kernels. Consequently all sign vectors have proportion \(2^{-r}\) in these reduced classes. We discard the fixed primes dividing \(2\prod_j u_j\Delta_j\) throughout.

For a good prime \(p\) set \(I_j(p)=1_{\chi_j(p)=1}\), \(\overline I(p)=r^{-1}\sum I_j(p)\), and \(w_j(p)=3^{\overline I(p)-I_j(p)}\). Write \(\mathbb E\) for average over the sign vectors. For each nonzero signed diagonal \(T\), select \(j\) minimizing \(\sum_{p\mid T} I_j(p)\), resolving ties by a fixed rule. Then \(W_j(T)=\prod_{p\mid T}w_j(p)\ge1\). Products count each good prime only once, and \(W_j(1)=1\). Notice that \(w_j(p)\le1\) on primes splitting in the selected field.

For stride \(4u_j\) define \(D_{T,j}(H)\) by \(4u_jd\le H\), \(d>0\), and \((4u_jd)^2+(T\pm2d)^2=L_0^2\) for some \(0<L_0<h\). Put \(B_r=((1+3^{1/r})/2)^r-1\). For fixed \(b>0\), \(H=\lfloor h/(\log h)^b\rfloor\), the following estimate is the main point:
\[
 \sum_T |D_{T,j(T)}(H)| \ll_{r,b,u_1,\ldots,u_r}
     H(\log h)^{B_r}(\log\log h)^{O_r(1)}.                 \tag{1}
\]

## Counting short distances at the selected stride

Fix \(j\), write \(u=u_j\), \(w=w_j\), \(I=I_j\), and \(L=\log h\). The Euclidean parameters of a counted triangle are coprime integers \(m>n\ge1\) of opposite parity, with positive odd scale \(k\). Ignoring a bounded number of signs, they satisfy
\[
 X=2kmn\le H,\qquad k(m^2+n^2)<h,\qquad
 |uT|=|kF(m,n)|,\qquad F(m,n)=u(m^2-n^2)\pm mn .
\]
For example \(2d=X/(2u)=kmn/u\), which gives the displayed form. For a good prime \(p\mid F\) one has \(p\nmid n\), by primitivity, and \(m/n\) is a root of a quadratic with discriminant \(4u^2+1\). Thus \(I(p)=1\). Also \(F\ne0\) because the discriminant is nonsquare, and \(|F|\ll_u h\).

Take dyadic boxes \(m\in[M,2M)\), \(n\in[N,2N)\) with \(N\le M\). We may enlarge the range of \(k\) to \(k\le K=\min(h/M^2,H/(MN))\), dropping empty boxes. For a primitive pair, the indicator that the computed diagonal is assigned to \(j\), with the original divisibility conditions, is at most
\[
 W_j(F)\, f_F(k),\qquad
 f_F(k)=\prod_{\substack{p\mid k\\p\nmid F}} w(p).
\]
Set the weights of discarded primes to one. The identity with \(W_j(T)\) holds on tuples with integral \(T\). All summands on the enlarged range are nonnegative. The function \(f_F\) is multiplicative, with prime-power values at most three. The [elementary mean-value bound in the stride draft](../../papers/extremal/drafts/upper_bound/part7_heavy.tex) gives, uniformly in \(K\ge1\),
\[
 \sum_{k\le K}f_F(k)
 \ll K(\log(2h))^{A}(\log\log(3h))^{O(1)},\qquad A=\mathbb E w-1\ge0.             \tag{2}
\]
Indeed \(\sum_{p\le K}(w(p)-1)/p=A\log\log(3K)+O(1)\) by the reciprocal-prime estimate in fixed residue classes. Resetting \(w(p)\) to one at primes dividing \(F\) changes this by \(O(\log\log\log(30h))\), since the sum of reciprocals of prime divisors of any \(n\ll_u h\) has this bound. To see the latter, sum all primes up to \(\log(3h)\), and use \(\omega(n)\le\log n/\log2\) for the remaining primes. The inequality \(A\ge0\) follows from \(\mathbb E\log w=0\). [Williams, *Mertens' theorem for arithmetic progressions*](https://people.math.carleton.ca/~williams/papers/pdf/057.pdf)

It remains to bound the average of \(W_j(F)\) in one box. Put \(C=2\mathbb E[I(w-1)]\), so \(-1<C\le0\). We claim that for \(N\ge\sqrt M\) this average over primitive pairs, normalized by \(MN\), is
\[
 \ll (\log(2M))^{C}(\log\log(3h))^{O_r(1)}.                 \tag{3}
\]
For \(\log N\le(\log L)^3\), use \(W_j(F)\le1\) on primitive pairs, which implies (3) at a cost polynomial in \(\log L\). Otherwise set \(z=\exp(\log N/(\log L)^2)\). Drop all factors of \(W_j(F)\) except the split primes \(p\le z\). As each dropped factor is at most one, it suffices to average the remaining product over *all* pairs. A split good prime has two distinct slopes modulo \(p\); their lines meet at the origin. Its root density in the full residue square is \(\alpha_p=(2p-1)/p^2\).

Here are details of the uniform product bound. Put \(b_p=1-w(p)\) on these split primes and \(b_p=0\) otherwise, so \(0\le b_p<1\). Truncate the expansion of \(\prod(1-b_p1_{p\mid F})\) after the even degree \(2\lceil D\log L\rceil\), with \(D\) a sufficiently large fixed constant. This gives a pointwise upper bound by the Bonferroni inequalities, or by independently retaining each marked prime with probability \(b_p\) and bounding the probability of no retained marks. For any squarefree product \(d\) in these terms, \(d\le z^{2\lceil D\log L\rceil}=N^{o(1)}\). By counting each residue class in the two coordinate intervals and applying the Chinese remainder theorem, the fraction of pairs satisfying \(d\mid F\) is
\[
 \left(\prod_{p\mid d}\alpha_p\right)(1+O(d/N+d/M+d^2/(MN))).
\]
All absolute main terms sum to at most \(\exp(\sum b_p\alpha_p)\le L^{O(1)}\), so the total error is \(N^{-1+o(1)}L^{O(1)}\). The omitted tail of the model product has absolute value at most \(\sum_{\ell>2\lceil D\log L\rceil}(\sum b_p\alpha_p)^\ell/\ell!\). Taking \(D\) large makes this \(O(L^{-3})\). The model product is \(O((\log z)^C)\), by the same fixed-modulus prime sum and \(\alpha_p=2/p+O(p^{-2})\). Since \(\log z=\log N/(\log L)^2\) and \(N\ge\sqrt M\), this gives (3). All moduli and implicit constants here may depend on the finite menu.

To sum the boxes, their bare volume \(MN K\) is at most \(\min(hN/M,H)\). For each dyadic \(M\) its sum over dyadic \(N\le M\) is \(O(H(1+\log(2h/H)))\), by summing the geometric small-\(N\) range and counting the rest. For \(N\ge\sqrt M\), (2) and (3) thus give a total at most
\[
 H L^{A}(\log L)^{O_r(1)}\sum_{M\ {\rm dyadic},\ M\le\sqrt h}(\log(2M))^C
 \ll H L^{1+A+C}(\log L)^{O_r(1)} .
\]
For \(N<\sqrt M\) it is enough to count the original triangles without selection or weights. The boxes \(M\le (2h/H)^2\) contribute \(O(H(1+\log(2h/H))^2)\). For larger \(M\), summing \(hN/M\) first over \(N<\sqrt M\) and then over dyadic \(M>(2h/H)^2\) gives \(O(H)\). Finally,
\[
 1+A+C=\mathbb E[(1+2I)w]-1=\mathbb E[3^{\overline I}]-1=B_r,
\]
since \(1+2I=3^I\). This proves (1), with a fixed number of signs and strides.

## Incorporating the sea and the missing labels

As \(r\to\infty\), \(B_r\to\sqrt3-1\). Take \(r\) so large that \(B_r<b=\sqrt3-1+\varepsilon\). Then (1) is \(O(h)\). On each diagonal use \(x_i=4u_{j(T)}i+x_0\), with the same index classes modulo 14 and the same random constant odd sea as in the [one-stride proof](random_constant_row_windows.md). The physical same-role slope is now \(\kappa=2u_j\), an even integer of valuation one divisible by seven. Thus the all-true valuation tests, the modulo-seven norm test, and the true-pivot exclusions are unchanged. The crossed-support count is \(O_\kappa(H)\), with a uniform constant over this fixed menu. The total number of bands in each trial is \(O(h)\) by (1), and the width including guards is \(O(h^2)\).

By the [quantitative divisor-spacing bound](quantitative_divisor_window.md), for every fixed even true row \(y\), a uniform candidate \(s\) in its prescribed class modulo 28 has probability \(O((\log h)^{-c_b})\) of allowing any sea chord with \(0<X\le H\) and integral length. Its hypothesis \(b>\log3-1\) holds. The small-gap and crossed-support exclusions cost \(O(H/h)\) each. A fixed number of independent trials makes the marginal miss probability at most \((\log h)^{-4}\), with independence across diagonals. Theorem D, the shortened class guards, the WP block and the constant-row joins now apply as in the one-stride proof. This proves the window theorem for all labels.

Within the main collection of bands, one may also order the bands by nondecreasing sea row and give each a length-\(h+1\) guard at both ends at the same total order of width. All the main singleton sea points then form a coordinatewise chain, and a pair of true points in different bands is too far apart to be an in-strip vertical rival. The theorem still controls all families together only up to span \(H\). The universal upper bound for the span of a pair of intersecting tilted rectangles remains of order \(h^2\).
