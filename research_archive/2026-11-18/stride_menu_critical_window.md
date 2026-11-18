# How many doubles fit before the stride-menu threshold?

Let \(q_h=\lfloor h^2/4\rfloor\), \(L=\log\log h\), and \(\mu=(\log 3)/2\). All logarithms are natural. The construction yields the following bound for the original geometric blackout problem. For every fixed real \(A\), uniformly at integer widths
\[
 m\ \ge\ h^2(\log h)^\mu\,\exp(-A\sqrt L),
 \qquad f(h,m)=m+q_h-o(h^2).
 \tag{1}
\]
The factor below the old bound \(h^2(\log h)^{\mu+\varepsilon}\) is obtained by choosing among several strides. The proof uses the deterministic obstruction estimates in the current stride-menu draft. It permits missing doubles.

There is also a lower bound at smaller widths. Fix \(0\le\alpha\le\mu\) and take \(m\ge h^2(\log h)^\alpha\). Then
\[
 f(h,m)-m\ \ge\ h^2(\log h)^{-J(\alpha)-o(1)},\qquad
 J(\alpha)=
 \begin{cases}
 1/3-\alpha,&0\le\alpha\le(\log3)/6,\\
 1/2-b+b\log(2b),\quad b=\alpha/\log3,&(\log3)/6\le\alpha\le\mu .
 \end{cases}
 \tag{2}
\]
At \(\alpha=0\) the [previous one-stride result](global_partial_size_bound.md) already gives an absolute constant in place of the subpower loss. Equation (2) is a constructive lower bound. An upper bound of the same order for the optimum is open.

## Keeping the first colors of each chain

Fix an admissible menu \(U\) of \(k\) strides. Write \(g_u(t)=\prod_{p^e\Vert t,\ p\text{ split in }K_u}(2e+1)\), with \(K_u=\mathbb Q(\sqrt{4u^2+1})\). The ideal count bounds the minimizing number of forbidden distances by
\[
 \kappa^U_T \le C_U(1+\log(3h/|T|))\min_{u\in U}g_u(|T|).
 \tag{3}
\]
A label goes to the stride minimizing the actual distance count. The inequality uses the other strides only to bound this minimum. [Ideal count](../../papers/extremal/drafts/upper_bound/part7_heavy.tex)

Let \(s\to\infty\) be an integer below \(B/4\), where \(B=\lceil(\log h)^{x_k}\rceil\) is the full menu budget. Take any diagonals with \(\kappa^U_T\le s/8\). Except for \(O_U(h^2/s)+o_U(h^2)\) labels, we can keep all their labels in a board of width at most \(C_U(s+1)h^2\). The error \(o_U(h^2)\) here can be taken as \(O_U(h^{11/6}\log h+h^{9/5+1/100}+h^{3/2}+h)\).

Here are the geometric inputs. Remove the fixed boundary labels (R-a) through (R-c). For each diagonal and type, the three bounded-shape mixed families and the short-distance graph together have \(O_U(h)\) edges. Indeed, each shape has \(O_U(h/q+1)\) or \(O_U(h/|U'|+1)\) designated ends determining the other ends, with the reciprocals summable. On the bounded-shape ranges the \(+1\) is absorbed. Remove vertices of degree above \(s/4\) in this union. This costs \(O_U(h/s)\) per type and diagonal. The surviving graph after adding the forbidden distances has maximum degree at most \(s/2\). Color it with the first \(s\) colors. On the rest of the same diagonal and type use only the last \(B-s\) colors, respecting forbidden distances. On every other light diagonal choose any proper coloring. The prime minimization deals with cross-class exceptions uniformly in these class choices. No selected edge has a bounded-shape in-class conflict, and the large-shape and cross-class exceptional labels cost the power-saving error above. Keep the surviving selected labels and restore the prescribed background at other candidate slots. The obstruction table permits this subset operation. [In-class estimates](../../papers/extremal/drafts/upper_bound/part5_classes.tex), [obstruction table](../../papers/extremal/drafts/upper_bound/part6_table.tex), and [assembly estimates](../../papers/extremal/drafts/upper_bound/part8_assembly.tex)

Within each type and stride all retained labels occur in the first \(s\) color periods. Shorten the remaining pure profile by multiples of 16 columns, leaving more than \(2W_h+1\) old profile columns on both sides of any deletion, where \(W_h=1+\lfloor(h-1)^2/4\rfloor\). All local tests at each new seam agree with old ones. Tests using a remote owner use the full parity graph. The chains have row-1 exteriors and disjoint label sets. The assembly lemma joins them with \(2W_h+1\) columns of row 1 between consecutive windows. There are \(512k\) regions, with \(k\) fixed as \(h\to\infty\). This gives the width above and an infinite row-1 exterior for every larger width. [One-stride shortening argument](global_near_equality.md) and [block gluing lemma](../../papers/extremal/drafts/upper_bound/part2_validity.tex)

## Distribution across a fixed menu

Choose \(t\) uniformly among the odd integers in \([c h,d h]\), for any fixed \(0\le c<d\le1\). Let \(\omega_u(t)\) count its distinct split prime divisors. As \(h\) tends to infinity, the vector
\[
 \left(\frac{\omega_u(t)-L/2}{\sqrt{L/2}}\right)_{u\in U}
 \quad\Longrightarrow\quad
 \left(\frac{Z_0+Z_u}{\sqrt2}\right)_{u\in U},
 \tag{4}
\]
where the \(k+1\) variables \(Z\) are independent standard normals. For the split condition of one field the prime density is \(1/2\). For two distinct fields the density of a common split is \(1/4\), since the two quadratic characters and their product are nonprincipal. Mertens' theorem on the reduced residue classes of the fixed common modulus gives these same coefficients for the reciprocal-prime sums, with bounded error. Excluding the finitely many ramified primes and 2 costs a bounded amount. [Williams, Mertens' theorem for arithmetic progressions](https://people.math.carleton.ca/~williams/papers/pdf/057.pdf)

For detail, truncate at \(y=h^{1/L}\). For any fixed moment order \(r\), expanding the moments of a linear combination of the truncated counts gives the moments of independent Bernoulli divisibility variables of means \(1/p\), up to \(O_{r,U,c,d}((1+L)^r y^r/h)=o(1)\). This follows by counting odd multiples of the squarefree product of the distinct primes in each monomial. Centering by the independent means introduces at most the displayed power of \(1+L\). In the independent model the variance is the sum of the squared weights times \(p^{-1}(1-p^{-1})\). After division by \(L/2\) it has diagonal entries 1 and off-diagonal entries \(1/2\). All fixed cumulants of order at least three before normalization are \(O_{r,U}(L)\), since the weights are bounded and the cumulant of a Bernoulli variable is \(O_r(1/p)\). The normalized moments therefore converge to the normal moments. The omitted primes have expected number \(O_{c,d}(\log L+1)=o(\sqrt L)\), and truncation changes the centering by \(O(\log L)\). This proves (4) by taking linear combinations. The method is the moment proof of the Erdős–Kac theorem. [Granville and Soundararajan](https://arxiv.org/abs/math/0606039)

Also \(\log g_u(t)=(\log3)\omega_u(t)+O_{\mathbb P}(1)\) jointly for fixed \(U\). The nonnegative difference is at most \((\log3)\sum_{p^j\mid t,\ j\ge2}1\), whose mean is bounded by summing \(p^{-j}\) (or counting positive multiples up to \(h\)). Each signed diagonal of offset \(T\) has \((h-|T|)/2+O(1)\) labels. Thus (4) also describes \(|T|\) for a uniformly chosen label, by partitioning \(|T|/h\) into fixed intervals followed by Riemann sums. Offsets below \(h/\log h\) have \(o(h^2)\) labels. On all remaining offsets, the logarithm of the prefactor in (3) is \(O_U(\log(2+L))=o(\sqrt L)\).

Choose \(s=\lfloor m_*/(2 C_U h^2)\rfloor\) with \(m_*=h^2\exp(\mu L-A\sqrt L)\), increasing \(C_U\) if needed. For any fixed menu this tends to infinity and is \(o(B)\), since \(x_k>1>\mu\). By (3) and (4), the limiting lower bound for the fraction of all labels that fit is
\[
 1-\Pr\!\left(\min_{u\in U}(Z_0+Z_u)/\sqrt2
                         > -\sqrt2 A/\log3\right).
 \tag{5}
\]
The continuous limiting distribution absorbs constant factors in the width budget. At \(A=0\), the failure probability equals \(1/(k+1)\), since it is the probability that \(-Z_0\) is smallest among \(k+1\) independent standard normals. For any fixed \(A\), conditional on \(Z_0\) the failure probability is a \(k\)th power of a number strictly below 1. It tends to zero by dominated convergence. Menus exist at every fixed size. Choose \(k\) first for a prescribed error and then take \(h\) large. This proves (1). A diagonal choice of successively larger integer \(A\) also gives (1) for some sufficiently slowly growing \(A(h)\to\infty\). The argument supplies no prescribed speed for \(A(h)\).

## The bound between quadratic width and the Gaussian range

Use stride four alone, and positive odd \(T\in[h/4,h/2]\). Here each compatible type contains \(\gg h\) eligible indices and the factor \(1+\log(3h/T)\) is bounded. Provided \(C g_1(T)\le B/8\), the first \(s\) periods with \(1\le s=o(B)\) can keep
\[
 \gg h\min(1,s/g_1(T))
 \tag{6}
\]
indices of that type, before the global power-saving exceptions. To see this, discard vertices whose bounded-shape mixed degree exceeds a sufficiently large constant. The edge estimate above leaves at least half the indices. On these vertices the mixed and forbidden-distance graphs together have a proper coloring in \(O(g_1(T))\) colors. Take the \(s\) largest classes, or all if there are fewer, and use fresh late colors for all other vertices as above. Global power-saving deletions are negligible compared with \(h^2/(\log h)^C\) for fixed \(C\).

For \(0<b\le1/2\) put \(I(b)=1/2-b+b\log(2b)\). At least \(h(\log h)^{-I(b)-o(1)}\) eligible offsets satisfy \(g_1(T)\le(\log h)^{b\log3+o(1)}\). Here is a lower bound sufficient for this assertion. Put \(z=2b\) and consider odd squarefree \(d\) with primes at most \(h^\eta\), weighted by \(z^{\omega_1(d)}/d\). The total weight is comparable to \((\log h)^{(1+z)/2}\) by the Euler product and the two splitting densities. Under the normalized weights the primes occur independently. The split count has mean \(bL+O(1)\) and variance \(O(L)\), and \(\mathbb E\log d=O(\eta\log h)\). Choose fixed \(\eta<1/4\) small enough that at least three quarters of the weight has \(d\le h^{1/4}\). By Chebyshev, a positive fraction of the total weight also satisfies \(|\omega_1(d)-bL|\le L^{2/3}\) simultaneously. For these \(d\), removal of the weight \(z^{\omega_1(d)}\) multiplies the sum by \(\exp(-bL\log z+o(L))\). Each \(d\) extends in \(\gg h/(d\log h)\) ways to \(T=d\ell\in[h/4,h/2]\) with \(\ell\) prime, by the prime number theorem. Its largest prime \(\ell\) exceeds \(h^{1/2}\) and determines \(d\) uniquely. The resulting offsets are squarefree and \(g_1(T)\le3^{\omega_1(d)+1}\). This gives the count.

Take \(s\) comparable to \((\log h)^\alpha\) with a small fixed coefficient for \(\alpha>0\). For \(\alpha=0\) use the existing width-\(O(h^2)\) board and its interval averaging argument. Equations (3) and (6) and the offset count give a gain in the exponent of the logarithm equal to
\[
 -I(b)+\min(0,\alpha-b\log3).
\]
Taking \(b=\max(1/6,\alpha/\log3)\) proves (2). All these claims concern globally valid, filled boards. Equality at width \(O(h^2)\) still requires a way to include every missing label.

