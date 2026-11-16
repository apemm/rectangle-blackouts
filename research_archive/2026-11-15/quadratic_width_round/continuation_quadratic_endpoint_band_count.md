# Quadratic endpoint gaps avoid most small-factor bands

15 November 2026. This note gives an arithmetic result for unrestricted
integer scales. It does not transfer that result to the dyadic scales of
the standard Hilbert construction.

Fix positive integers \(A_0,K\), integers \(B,C\), and fixed nonnegative
constants \(c_0,c_1\). Put
\[
 W(n)=A_0n^2+Bn+C.
\]
Assume
\[
 \frac{B^2}{4A_0}\notin\mathbb Z.                         \tag{1}
\]
For \(1\le a\le A\), consider all positive integers \(q\) such that
\[
 a\mid(Kq)^2,\qquad Y=(Kq)^2/a-a>0.
\]
Call an integer \(n\in[R,2R]\) exceptional if
\[
 |W(n)-Y|\le c_0\sqrt q+c_1                              \tag{2}
\]
for one such pair. If \(A=A(R)=o(R)\), then, for all sufficiently large
\(R\), the number of exceptional integers is at most
\[
 C_*\left(R^{1/2}A^{3/4}\log(2A)
                  +A^{3/2}\log(2A)\right).              \tag{3}
\]
The constant depends only on the fixed data. In particular, if
\(A\le R^{2/3}/\log^kR\) for fixed \(k>4/3\), all but \(o(R)\)
integer scales avoid the bands.

## 1. A one-sided count for a quadratic irrational rotation

For squarefree \(u\), and a fixed positive integer \(c\), put
\[
 \theta=\frac{\sqrt{A_0/u}}{c}.
\]
If \(\theta\) is irrational, then
\[
 \|j\theta\|\ge \frac{c_*}{\sqrt u\,j}\qquad(j\ge1),   \tag{4}
\]
with a positive constant uniform in \(u\). Indeed, for the nearest
integer \(p\), the nonzero integer
\(A_0j^2-c^2up^2\) has absolute value at least one. Factoring this
difference proves (4) when \(j\theta\ge1/2\). When
\(j\theta<1/2\), the nearest integer is zero and (4) follows directly.

Dirichlet's pigeonhole argument supplies coprime integers \(p,j\),
\(1\le j\le R\), with
\[
 |\theta-p/j|\le1/(jR).
\]
By (4), \(j\ge c_*R/\sqrt u\). In every block of \(j\)
successive integers, the orbit modulo one lies within \(1/R\) of
a translated uniform grid of mesh \(1/j\). Thus at most
\(2j\varepsilon+O(1)\) elements lie within distance
\(\varepsilon\) of an integer. Partitioning any interval of at most
\(R+1\) integers into these blocks, and enlarging its last partial
block, gives
\[
 \#\{n:\|n\theta+\beta\|\le\varepsilon\}
       \le C(R\varepsilon+\sqrt u),                     \tag{5}
\]
uniformly in \(\beta\). For \(\varepsilon\ge1/2\), the same
bound follows from the trivial count. This is an upper bound, not an
equidistribution assertion.

## 2. Divisibility determines the relevant rotation

Write \(a=uv^2\), where \(u\) is squarefree, and put
\[
 g=\gcd(uv,K),\qquad c=K/g.
\]
The divisibility condition is equivalent to
\(q=(uv/g)\ell\) for a positive integer \(\ell\). Consequently
\[
 Y=uc^2\ell^2-uv^2.                                      \tag{6}
\]
Throughout \(R\le n\le2R\), a solution of (2) has
\(\ell\asymp R/\sqrt u\) and \(q\asymp v\sqrt u R\).
These comparisons are uniform for \(a\le A=o(R)\). Dividing the
error in (2) by the derivative of the right side of (6), and expanding
the positive square root of \(W(n)+a\), yields
\[
 \left|\ell-\theta n-\beta\right|
 \le C\left(
       \frac{v^{1/2}}{u^{1/4}R^{1/2}}
       +\frac{a+1}{\sqrt u R}\right),                    \tag{7}
\]
where
\[
 \theta=\frac{\sqrt{A_0/u}}c,
 \qquad \beta=\frac{B}{2c\sqrt{A_0u}}.
\]
For clarity, the expansion error before division by \(c\sqrt u\)
is \(O((a+1)/R)\); all coefficients other than \(a,u,v\) are fixed.
There are only finitely many possible \(c\), since \(c\mid K\).

If \(\theta\) is irrational, (5) and (7) bound the number of
exceptional scales for this \(a\) by
\[
 C\left(R^{1/2}v^{1/2}u^{-1/4}
                  +(a+1)u^{-1/2}+\sqrt u\right).         \tag{8}
\]

## 3. Rational slopes do not resonate

Write \(A_0=s w^2\) with \(s\) squarefree. A rational
\(\theta\) requires \(u=s\). In lowest terms it is
\(P/Q=w/c\), with \(P=w/\gcd(w,c)\). If
\(n\theta+\beta\) were an integer, then \(Q\beta\) would be
an integer. But
\[
 Q\beta=\frac{PB}{2A_0}
       =\frac{B}{2s w\gcd(w,c)}.
\]
Its integrality would imply \(B^2/(4A_0)\in\mathbb Z\), contrary
to (1). Hence these affine rational orbits stay a fixed positive
distance from the integers. The distance can be chosen uniformly over
the finitely many \(c\mid K\).

The right side of (7) tends to zero uniformly for the rational cases:
\(u=s\) is fixed, \(v\le\sqrt A\), and \(A=o(R)\).
Therefore no rational case is exceptional for sufficiently large \(R\).

## 4. Summing the irrational cases

Dropping the squarefree restriction only enlarges each sum. The three
terms in (8) satisfy
\[
 \begin{aligned}
 \sum_{uv^2\le A}v^{1/2}u^{-1/4}
     &\le C A^{3/4}\log(2A),\\
 \sum_{uv^2\le A}(uv^2+1)u^{-1/2}
     &\le C A^{3/2}\log(2A),\\
 \sum_{uv^2\le A}\sqrt u
     &\le C A^{3/2}.
 \end{aligned}
\]
For example, the first sum is at most
\(C A^{3/4}\sum_{v\le\sqrt A}v^{-1}\). The second uses
\(\sum_{u\le A/v^2}\sqrt u\le C(A/v^2)^{3/2}\), and the
third sums \(v^{-3}\). These bounds prove (3).

## 5. Application and limit for the long two-cycle

The endpoints in
[`continuation_long_private_two_cycle.md`](continuation_long_private_two_cycle.md)
have exact own-row gaps
\[
 W_\pm(L)=308Y_0L^2\pm14DL+(Y_0\pm D),
 \qquad Y_0=(SM)^2-1.
\]
Their nonresonance quantity is
\[
 \frac{(14D)^2}{4\cdot308Y_0}
       =\frac{7D^2}{44Y_0},
\]
which lies strictly between zero and one for the stated full-grid and
H7 parameters. Applying (3) to both endpoints shows that almost every
unrestricted integer \(L\in[R,2R]\) avoids the small-factor bands at
the scale \(A\le R^{2/3}/\log^4R\).

The existing exact Hilbert embedding requires \(L\) to be a power of
two. An estimate for all integer scales gives no conclusion about that
sparse subsequence. A different order admitting unrestricted scales,
or an additional argument on the dyadic subsequence, is still needed.
No endpoint-survival theorem for the actual Hilbert family is asserted.

Independent review checked the norm lower bound, reduced Dirichlet
denominator, rational-grid count, divisibility substitution, expansion
error, rational nonresonance, and the three sums. The complete written
argument passed that review on 15 November 2026.
