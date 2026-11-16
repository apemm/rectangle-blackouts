# Odd-relation deletion also has a superlinear total cost

12 November 2026. This continues
[the parity-sensitive Riesz criterion](continuation_arc_parity_riesz.md).
Independent review completed for the full written proof, including the
split-prime construction, actual diagonal cutoffs, and quantitative rate.

The criterion itself remains valid. Its proposed linear total deletion
bound fails:
\[
 \boxed{\displaystyle
 \frac1h\sum_T\beta_{\mathrm{odd}}(T,h)\longrightarrow\infty.}
 \tag{1}
\]
The elementary quantitative proof below gives
\[
 \boxed{\displaystyle
 \sum_T\beta_{\mathrm{odd}}(T,h)
 =\Omega\!\bigl(h\log\log\log\log h\bigr).}
 \tag{2}
\]
All iterated logarithms in (2) are evaluated at sufficiently large \(h\).
No useful small-height constant is asserted.

This obstructs deletion to the bounded even-relation condition. It does
not obstruct the Riesz partition-function ratio criterion, direct arc
coloring, or a linear monotone P-free partition.

## 1. Definitions and the two ingredients

Retain the positive, deduplicated, finite diagonal set
\[
 D_T(h)=\{|d|:\ d\ne0,\ |d|<n_T,\
      20d^2+4Td+T^2=L^2,\ 0<L<h\},
 \qquad k_T(h)=|D_T(h)|.
 \tag{3}
\]
For positive odd \(T\),
\[
 n_T=\lfloor h/2\rfloor-(T-1)/2
 \ge(h-T)/2.
 \tag{4}
\]
The cap \(m(k)\) is the least positive integer satisfying
\[
 2k\sqrt{m(k)}<2^{m(k)}.
 \tag{5}
\]
The deletion number \(\beta_{\mathrm{odd}}(T,h)\) is the minimum number
removed so that the retained set of \(k\) distances has no zero relation
with \(|c_d|\le m(k)\) and odd coefficient sum.

The proof uses two facts:

1. On the central range \(1\le T\le h/1000\), \(T\) odd,
   \(k_T(h)\) tends to infinity in density.
2. A fixed collection of short primitive right triangles creates
   \(\Omega(h\log B)\) reflection edges. Each edge is itself an
   odd-sum two-term relation with coefficients bounded by \(B\).

The first fact forces the cap of a cheaply retained set to grow. This is
why merely observing that the four-term reflection relations have even
sum does not settle the deletion question.

## 2. A bounded gap for every split prime

Let
\[
 \phi=\frac{1+\sqrt5}{2},\qquad
 u=\phi^2=\frac{3+\sqrt5}{2}.
\]
For every prime \(p\equiv1,4\pmod5\), there are integers \(d_p\ne0,L_p>0\)
such that
\[
 20d_p^2+4pd_p+p^2=L_p^2,\qquad
 |d_p|<2p,\qquad L_p<9p,\qquad p\nmid d_p.
 \tag{6}
\]
The last condition makes the reduced denominator of \(|d_p|/p\) exactly
\(p\).

Here is a self-contained construction.
The ring \(R=\mathbb Z[\phi]\) is norm Euclidean. Indeed,
\[
 N(a+b\phi)=a^2+ab-b^2.
 \tag{7}
\]
After rounding both coefficients of an element of \(\mathbb Q(\sqrt5)\),
the error has coefficients of absolute value at most \(1/2\). Its norm
has absolute value at most \(3/4<1\).
Division with smaller absolute norm follows, and every ideal of \(R\)
is principal.

For \(p\equiv1,4\pmod5\), the polynomial \(X^2-X-1\) has two distinct roots
modulo \(p\). One elementary way to see the residue condition is to take
a primitive fifth root \(\zeta\) in an algebraic closure of
\(\mathbb F_p\). The element \(\zeta+\zeta^{-1}\) satisfies
\(X^2+X-1=0\), and it is fixed by Frobenius exactly when
\(p\equiv1,-1\pmod5\).

Evaluation at one of the two roots gives an ideal \(P\) of index \(p\).
Write \(P=(\alpha)\). The determinant of multiplication by \(\alpha\)
is \(N(\alpha)\), so \(|N(\alpha)|=p\). At the other root modulo \(p\),
\(\alpha\) is nonzero: otherwise \(\alpha\in pR\), which would make its
norm divisible by \(p^2\).

Set \(\beta=\phi\alpha^2\), so \(N(\beta)=-p^2\). Its value at the other
root is still nonzero, and hence
\[
 \beta\notin pR.
 \tag{8}
\]
Choose a global sign so the first real embedding \(z\) of \(\beta\) is
positive. Multiplying by an integral power of the positive norm-one unit
\(u\), arrange \(1\le z/p<u\).

Modulo two, \(R/2R\) is the field with four elements, and \(u\) generates
its multiplicative group. Since \(N(\beta)\) is odd, multiplying by one
of \(1,u,u^2\) makes the \(\phi\)-coefficient odd. After this adjustment,
write
\[
 \beta=(Y+L\sqrt5)/2,\qquad
 Y,L\ \text{odd},\qquad
 1\le z/p<u^3.
 \tag{9}
\]
The norm equation and the two real embeddings give
\[
 Y^2-5L^2=-4p^2,\qquad
 Y=z-p^2/z,\qquad L=(z+p^2/z)/\sqrt5.
 \tag{10}
\]
Since \(u^3=9+4\sqrt5\) and \(u^3+u^{-3}=18\),
\[
 |Y|<18p,\qquad |L|<9p.
 \tag{11}
\]
Modulo five, (10) gives \(Y\equiv p\) or \(-p\).
Choose the global sign to obtain \(Y\equiv p\pmod5\). Both are odd, so
\(Y\equiv p\pmod{10}\). Put
\[
 d_p=(Y-p)/10,\qquad L_p=|L|.
 \tag{12}
\]
Equations (10)--(12) give the norm identity and bounds in (6).
If \(p\mid d_p\), then \(p\mid Y\), and (10) forces \(p\mid L\).
Because \(p\) is odd, this would put \(\beta\) in \(pR\), contradicting
(8). Thus \(p\nmid d_p\), completing the proof.

## 3. Many distinct actual gaps on most central diagonals

Suppose \(T\) is odd, \(0<T\le h/1000\), and \(p\equiv1,4\pmod5\) divides
\(T\). Scale (6) by \(T/p\):
\[
 d=(T/p)d_p,\qquad L=(T/p)L_p.
 \tag{13}
\]
Then
\[
 L<9T<h,\qquad |d|<2T<n_T.
 \tag{14}
\]
Thus \(|d|\in D_T(h)\). Distinct primes give distinct gaps: the rational
number \(|d|/T=|d_p|/p\) has reduced denominator \(p\).
Consequently
\[
 k_T(h)\ge\omega_{\mathrm{split}}(T),
 \tag{15}
\]
where \(\omega_{\mathrm{split}}\) counts distinct prime divisors
congruent to \(1\) or \(4\) modulo five.

For completeness, the required density statement can be proved without
a prime number theorem. Define the real character
\[
 \chi(n)=
 \begin{cases}
  0,&5\mid n,\\
  1,&n\equiv1,4\pmod5,\\
 -1,&n\equiv2,3\pmod5.
 \end{cases}
\]
The series \(L(1,\chi)\) converges and is positive. Its consecutive
five-term blocks are
\[
 \frac1{5j+1}-\frac1{5j+2}-\frac1{5j+3}+\frac1{5j+4}>0.
 \tag{16}
\]
Bounded partial sums of \(\chi\) give continuity of \(L(s,\chi)\) at
\(s=1\) from the right. The absolutely convergent Euler products for
\(s>1\) imply
\[
 \log\zeta(s)+\log L(s,\chi)
 =2\sum_{p\equiv1,4\ (5)}p^{-s}+O(1),
 \tag{17}
\]
with an error bounded as \(s\downarrow1\). Since \(\zeta(s)\to\infty\)
and \(L(s,\chi)\to L(1,\chi)>0\), it follows that
\[
 \sum_{p\equiv1,4\ (5)}\frac1p=\infty.
 \tag{18}
\]

Let \(T\) be uniform among positive odd integers at most \(X\).
For a fixed finite collection \(\mathcal P\) of these primes, set
\[
 W(T)=\sum_{p\in\mathcal P}\mathbf1_{p\mid T},
 \qquad \mu=\sum_{p\in\mathcal P}\frac1p.
 \]
Elementary divisibility counts give
\[
 \mathbb EW=\mu+o(1),\qquad
 \operatorname{Var}W\le\mu+o(1)
 \quad(X\to\infty).
 \tag{19}
\]
For any fixed \(K\), first take \(\mathcal P\) with \(\mu\) arbitrarily
large and then let \(X\to\infty\). Chebyshev's inequality gives
\[
 \mathbb P\{\omega_{\mathrm{split}}(T)<K\}\longrightarrow0.
 \tag{20}
\]
With \(X=h/1000\), (15) proves the density assertion used below.

## 4. Short primitive triangles give small odd relations

Take a primitive positive right triangle
\[
 (4a)^2+b^2=H^2,\qquad H,b\ \text{odd},
 \tag{21}
\]
from Euclid parameters
\[
 a=uv/2,\quad b=u^2-v^2,\quad H=u^2+v^2,\quad
 \gcd(u,v)=1,\quad u+v\ \text{odd},\quad u\ge2v.
 \tag{22}
\]
Define
\[
 T_0=5(b-2a),\qquad d_0=5a,\qquad e_0=3a+b.
 \tag{23}
\]
Then
\[
 0<H\le T_0,\qquad
 20d_0^2+4T_0d_0+T_0^2=(5H)^2,
 \tag{24}
\]
and the reflected signed gap is \(-e_0\). In particular,
\[
 e_0-d_0=T_0/5>0.
 \tag{25}
\]
The inequality \(H\le T_0\) follows from
\[
 T_0-H=(u-2v)(4u+3v)\ge0.
 \]

The two positive distances have opposite parity, because their difference
in (25) is odd. Also
\[
 \gcd(d_0,e_0)\mid5,\qquad
 \max(d_0,e_0)\le2H.
 \tag{26}
\]
For the gcd assertion, use \(\gcd(a,b)=1\), which follows from the
primitive triangle. Put \(g_0=\gcd(d_0,e_0)\). The relation
\[
 (e_0/g_0)d_0-(d_0/g_0)e_0=0
 \tag{27}
\]
has odd coefficient sum and coefficients of magnitude at most \(2H\).
Odd scaling preserves these reduced coefficients.

Fix \(B\), and keep the finite primitive family (22) with \(H\le B/2\).
For every positive odd scale \(q\) with \(T=qT_0\le X=h/1000\), (24)
produces the actual edge
\[
 \{qd_0,qe_0\}\subseteq D_T(h).
 \tag{28}
\]
Indeed, its hypotenuse is \(5qH\le5T<h\), and both distances are at most
\(2qH\le2T<n_T\). Every edge has an odd relation at coefficient cap \(B\).

Let \(E_T(B)\) be the number of distinct edges (28).
There are no multiplicities hidden in this count. The orientation
\(d<e\) is recovered from (25). From the edge one recovers the scaled
triangle using \(a'=d/5\), \(b'=e-3d/5\). Its gcd recovers \(q\), and
then the primitive triangle.

For fixed \(T\), all edges have the same difference \(T/5\). Their graph
is a union of paths, with maximum degree two. Moreover
\[
 E_T(B)\le C_B,\qquad C_B=O(B),
 \tag{29}
\]
since there are \(O(B)\) primitive parameter pairs with \(u^2+v^2\le B/2\).
Each primitive pair contributes at most one scale to a prescribed \(T\).

## 5. The total number of these edges

Uniformly for large \(B\),
\[
 \sum_{\substack{\text{primitive family }(22)\\H\le B/2}}
 \frac1{T_0}\ge c\log B.
 \tag{30}
\]
To prove this, take dyadic \(R\) and restrict
\[
 2R\le u<3R,\qquad R/2\le v<R.
 \tag{31}
\]
For large \(R\), at least \(cR^2\) pairs are coprime and have opposite
parity. There are \(R^2/4\) opposite-parity pairs before imposing
coprimality. A common divisor must be odd. Summing the elementary bound
\[
 \frac{R^2}{4q^2}+O(R/q+1)
 \]
over odd \(q\ge3\), and using \(\sum_{q\ge3}q^{-2}<1/2\), leaves
at least \(R^2/16\) pairs for all sufficiently large \(R\).

In this box, \(H\le10R^2\) and \(T_0\le45R^2\).
Each dyadic \(R\le\sqrt{B/20}\) contributes an absolute positive constant
to (30). The boxes have disjoint \(u\)-ranges. There are
\(\Omega(\log B)\) eligible scales.

For each primitive triangle, the number of positive odd scales
\(q\le X/T_0\) is \(X/(2T_0)+O(1)\). Therefore
\[
 \sum_{\substack{1\le T\le X\\T\ {\rm odd}}}E_T(B)
 \ge cX\log B-O(B)
 \ge c' h\log B-O(B).
 \tag{32}
\]
The constants are absolute. The cutoff \(X=h/1000\) is fixed throughout.

## 6. Why reducing the retained cap cannot avoid the cost

Let \(K_B=2^B\). If a retained set has cardinality \(k\ge K_B\), then
\(m(k)>B\): no integer \(m\le B\) can satisfy (5).

Consider a central diagonal with
\[
 k_T(h)\ge K_B+C_B.
 \tag{33}
\]
If fewer than \(K_B\) distances are retained, the deletion cost is at
least \(C_B\). If at least \(K_B\) are retained, (27) forbids retaining
both endpoints of any edge counted by \(E_T(B)\).
Since deleting one vertex destroys at most two edges,
\[
 \beta_{\mathrm{odd}}(T,h)\ge E_T(B)/2
 \tag{34}
\]
in both cases.

For fixed \(B\), (20) and (15) show that (33) fails on only \(o_B(h)\)
central diagonals. The lost edge count is \(o_B(h)\), by (29).
Summing (34) and using (32) gives
\[
 \liminf_{h\to\infty}\frac1h\sum_T\beta_{\mathrm{odd}}(T,h)
 \ge c\log B.
 \tag{35}
\]
Now let the fixed \(B\) tend to infinity. This proves (1).
No assumption about the size of the total deletion cost was used.

## 7. An elementary quantitative rate

The same proof gives (2). Write \(X=h/1000\), \(Y=X^{1/4}\), and
\[
 \mu(Y)=\sum_{\substack{p\le Y\\p\equiv1,4\ (5)}}\frac1p.
 \]
Then
\[
 \mu(Y)=\frac12\log\log Y+O(1).
 \tag{36}
\]
Only Chebyshev's elementary upper bound for primes is needed here.
For clarity, it follows from
\(\prod_{n<p\le2n}p\le\binom{2n}{n}\le4^n\):
dyadic summation gives \(\sum_{p\le x}\log p=O(x)\), and then
\(\pi(x)=O(x/\log x)\).

Take \(s=1+1/\log Y\) in (17). The integral comparison for \(\zeta(s)\)
and continuity of \(L(s,\chi)\) give
\[
 \sum_{p\equiv1,4\ (5)}p^{-s}
 =\tfrac12\log\log Y+O(1).
 \]
Chebyshev's bound supplies both uniform errors
\[
 \sum_{p>Y}p^{-s}=O(1),\qquad
 \sum_{p\le Y}(p^{-1}-p^{-s})
 \le(s-1)\sum_{p\le Y}\frac{\log p}{p}=O(1).
 \tag{37}
\]
For the first estimate, partial summation reduces the tail to
\(\int_{\log Y}^{\infty}e^{-u/\log Y}\,du/u=O(1)\).
This proves (36).

Let \(W(T)\) count only these split primes at most \(Y\), with \(T\)
uniform among positive odd integers at most \(X\).
The divisibility counts now give, uniformly,
\[
 \mathbb EW=\mu+O(Y/X),\qquad
 \operatorname{Var}W\le\mu+O(Y^2/X).
 \tag{38}
\]
The error \(Y^2/X=X^{-1/2}\) tends to zero. Thus
\[
 \#\{T\le X:\ T\text{ odd},\ k_T(h)<\mu/2\}
 =O(X/\mu).
 \tag{39}
\]

Choose
\[
 B=\left\lfloor\frac{\log\mu}{8\log2}\right\rfloor.
 \tag{40}
\]
Then \(2^B\le\mu^{1/8}\), \(C_B=O(B)\), and
\(K_B+C_B<\mu/2\) for large \(h\).
The exceptional contribution to the edge sum is at most
\[
 O(BX/\mu)=o(X\log B).
 \tag{41}
\]
Equations (32), (34), and (39)--(41) therefore give
\[
 \sum_T\beta_{\mathrm{odd}}(T,h)\ge c h\log B.
 \tag{42}
\]
Since \(\mu\asymp\log\log h\), the final factor is
\(\log B=\log\log\log\log h+O(1)\), proving (2).

## 8. What remains possible

The original dissociated-deletion cost is \(\Theta(h\log h)\).
The weaker odd-relation cost is now bounded by
\[
 \Omega\!\bigl(h\log\log\log\log h\bigr)
 \le\sum_T\beta_{\mathrm{odd}}(T,h)
 \le O(h\log h).
 \tag{43}
\]
The lower bound does not determine its true order.

The arc problem remains open. Odd relations make some constant terms
negative, but they do not by themselves force the partition-function
ratios to be large or prevent a good angle.
The exact sufficient condition
\[
 2|D|\sqrt m\,\sin^{2m}(\pi\delta)
 \max_{d\in D}\frac{Z_{D\setminus\{d\}}}{Z_D}<1
 \]
still tolerates every relation pattern. Controlling this ratio, or
constructing angles by a different argument, remains a distinct target.
