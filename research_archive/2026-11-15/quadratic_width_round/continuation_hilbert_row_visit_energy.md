# Averaged Hilbert row visits and raw opposite-parity 6PT

15 November 2026. Long 6PT collisions whose two parked triangles use
opposite parities have expected count \(h^{3/2+o(1)}\), provided all
four core points retain their raw Hilbert coordinate formulas. This
count uses the two independent row offsets. It includes distinct sea
offsets and a fixed-size union over within-block permutations.

The proof does not cover cap-constant core points or two triangles of
the same parity. In particular, it does not count the complete 6PT
family in the cap construction.

## 1. Row visits in a rank progression

Let
\[
 H:\{0,\ldots,N^2-1\}\longrightarrow\{0,\ldots,N-1\}^2
\]
be a bijection satisfying
\[
 \|H(r)-H(t)\|_\infty\le C_0\sqrt{|r-t|}.
 \tag{1}
\]
The standard Hilbert order has this property with an absolute constant.
For either coordinate \(\alpha\in\{0,1\}\), put
\[
 R_{\alpha,y}=\{r:H(r)_\alpha=y\}.
\]
Each set has exactly \(N\) members.

**Lemma 1.** For every positive integer \(d\), residue \(a\), and
coordinate row \(y\),
\[
 |R_{\alpha,y}\cap(a+d\mathbb Z)|
 \le C_1\left(\frac{N}{\sqrt d}+1\right).
 \tag{2}
\]

For \(d>N^2\), the count is at most one. For \(d\le N^2\), the
case of bounded \(d\) follows from \(|R_{\alpha,y}|=N\). Otherwise,
around each counted rank take a rank interval of length
\(\lfloor d/3\rfloor\), centered as closely as integer endpoints
permit. These intervals are disjoint. Discard at most two intervals
that meet the ends of the full rank range. Every remaining interval
has at least \(d/4\) ranks.

By (1), the image of every such interval lies in the coordinate strip
\[
 |H(t)_\alpha-y|\le C_0\sqrt d.
\]
This strip contains at most \(N(2C_0\sqrt d+3)\) cells. Injectivity
therefore bounds the number of retained intervals by \(C_1N/\sqrt d\).
Adding the two discarded intervals proves (2).

The \(N/\sqrt d\) bound permits square-root resonances when
\(d\asymp N\). No claim of a uniform \(O(N/d)\) bound is needed.

## 2. Congruence energy averaged over the modulus

Write
\[
 A_{\alpha,y}(a;d)=|R_{\alpha,y}\cap(a+d\mathbb Z)|,
 \qquad
 E_\alpha(d)=\sum_y\sum_{a\bmod d}A_{\alpha,y}(a;d)^2.
\]
Let
\[
 \mathcal T_N=\max_{1\le n<N^2}\tau(n).
\]
For every fixed \(C_2\),
\[
 \sum_{1\le d\le C_2N}E_\alpha(d)
 \le C_3N^3(1+\mathcal T_N).
 \tag{3}
\]
Indeed, the diagonal pairs contribute
\(N^2\lfloor C_2N\rfloor\). Each ordered pair of distinct ranks
in the same coordinate row contributes at most
\(\tau(|r-t|)\le\mathcal T_N\). There are fewer than \(N^3\)
such pairs.

For later use, the elementary divisor estimate gives
\(\mathcal T_N=N^{o(1)}\). One proof fixes \(\varepsilon>0\).
For primes \(p\ge2^{1/\varepsilon}\),
\(e+1\le2^e\le p^{\varepsilon e}\). For each of the finitely
many smaller primes, \((e+1)p^{-\varepsilon e}\) is bounded.
Multiplication yields \(\tau(n)\le C_\varepsilon n^\varepsilon\).

For an integer row increment \(\ell\), define
\[
 K_\alpha(r,\ell;d)
 =\#\{p:H(p)_\alpha=H(r)_\alpha-\ell,
                  \ p\equiv r\pmod d\}.
\]
An absent coordinate row contributes zero. Cauchy--Schwarz gives
\[
 \begin{aligned}
 \sum_r K_\alpha(r,\ell;d)
 &=\sum_y\sum_{a\bmod d}
       A_{\alpha,y}(a;d)A_{\alpha,y-\ell}(a;d)\\
 &\le E_\alpha(d).
 \end{aligned}
 \tag{4}
\]
The same inequality holds if the two occurrences of the residue \(a\)
are translated by different fixed integers. This observation covers
the fixed rank displacements used in Section 5.

## 3. The divisibility imposed by one parked triangle

Use core columns \(Sr\), with fixed positive integers \(S,D\).
Raw physical rows of parity \(\alpha\) have the form
\[
 y_\alpha(r)=\rho_\alpha+D(H(r)_\alpha-U_\alpha),
 \tag{5}
\]
where \(U_0,U_1\) are independent and uniform in integer intervals
of lengths at least \(c h\). Assume \(c'N\le h\le C'N\).
Only points whose physical rows lie in \([1,h]\) are eligible.

In a parked triangle, let \(r\) be the rank of the core point next to
the completion and \(p\) the other core rank. Let \(\xi\ne0\)
be the sea offset, \(s\) its sea row, and \(\delta\ne0\) the
same-parity row increment. The equations are
\[
 \delta=y_\alpha(r)-y_\alpha(p)=D\ell,
 \qquad
 S(r-p)\xi=-\delta(s-y_\alpha(p)).
 \tag{6}
\]
Consequently
\[
 d_\ell:=\frac{|D\ell|}{\gcd(|D\ell|,|S\xi|)}
 \quad\hbox{divides }r-p.
 \tag{7}
\]
For fixed nonzero \(\xi\), a positive value of \(d_\ell\) has at
most \(2\tau(|S\xi|)\) preimages among the signed integers \(\ell\).
To see this, write \(|D\ell|=d_\ell g\), where
\(g=\gcd(|D\ell|,|S\xi|)\) divides \(|S\xi|\). Some such
choices do not give an integral \(\ell\), which only reduces the count.

Let \(K_{\alpha,\xi}(r,\ell)\) count the ranks satisfying the
coordinate and congruence requirements in (6)--(7), without imposing
the remaining geometric or sea-color conditions. Since actual row
increments obey \(|D\ell|<h\), (3)--(4) imply
\[
 \sum_{r,\ 0<|D\ell|<h}K_{\alpha,\xi}(r,\ell)
 \le C\tau(|S\xi|)h^3(1+\mathcal T_N).
 \tag{8}
\]

For each listed pair \((r,p)\), the second equation in (6) fixes
at most one value of \(U_\alpha\). This follows because its right
side is affine in \(U_\alpha\), with nonzero coefficient
\(-\delta D\). Therefore the probability that this parked triangle
occurs is at most \(C/h\). This statement is unconditional in the
random offsets. Conditioning on the chosen cap configuration is not
part of the argument.

## 4. Long opposite-parity pairs

Take two parked triangles with a common completion, a common sea row,
and a common nonzero increment \(\delta\). Suppose one uses parity
zero and the other parity one, and all four core rows have the raw
form (5). Their sea offsets are \(\xi_0,\xi_1\), and their
completion-end ranks satisfy
\[
 r_1=r_0+(\xi_0-\xi_1)/S.
 \tag{9}
\]
If the shift in (9) is not an integer, there is no such pair.

Use the long-support reduction in
[the local-anchor note](continuation_long_support_local_anchors.md).
For core span greater than \(h^2/K\), with \(1\le K\le c_0h\)
for a sufficiently small fixed \(c_0\), it gives
\[
 |\xi_0|,|\xi_1|\le C K,
 \qquad |\delta|\ge c h/K.
 \tag{10}
\]
Hence each modulus in (7) is at least \(c h/K^2\). Lemma 1 gives
\[
 K_{\alpha,\xi_\alpha}(r,\ell)
 \le C(\sqrt h\,K+1).
 \tag{11}
\]
For each fixed pair of offsets, (8) and (11) now show that the number
of candidate quadruples \((r_0,\ell,p_0,p_1)\) is at most
\[
 C\tau(|S\xi_0|)(1+\mathcal T_N)K h^{7/2}.
 \tag{12}
\]
The arbitrary fixed shift in (9) does not affect this estimate:
bound the second partner count uniformly by (11), then sum the first
using (8).

Each candidate fixes at most one pair \((U_0,U_1)\), by the final
paragraph of Section 3. Independence gives probability at most
\(C/h^2\). There are \(O(K^2)\) offset pairs and only a fixed
number of possible sea rows in the H7 construction. Thus, with
\(\mathcal T_{CKS}=\max_{n\le CKS}\tau(n)\), the expected
number of long opposite-parity raw 6PT witnesses is at most
\[
 C K^3 h^{3/2}(1+\mathcal T_N)\mathcal T_{CKS}.
 \tag{13}
\]
For every fixed power \(K=(\log(2h))^A\), this is
\[
 h^{3/2+o(1)}.
 \tag{14}
\]
Witness multiplicity only enlarges the bound. Degenerate pairs,
wrong sea types, points outside the physical strip, and collisions
with extra black corners can all be discarded.

## 5. Fixed-size permutation unions and scope

Suppose objects can be permuted within fixed blocks of \(k\) ranks.
The object at a physical rank \(r\) then has original rank
\(r+e\), where \(|e|\le k-1\). Enumerate the displacements of
the four core points. There are at most \((2k-1)^4\) patterns.
For each pattern, the coordinate-row sets in (4) have fixed residue
translations. The Cauchy--Schwarz bound there and the progression
bound (2) are unchanged. Geometry still fixes the two independent
offsets. Therefore (13)--(14) hold for the union of all candidate
within-block permutations, with a constant depending on \(k\).

The estimate can be included in a joint Markov selection with the
existing cap-area, stub-incidence, and small-factor objectives.
It does not justify conditioning on those objectives first. If
relocating every implicated genuine label is separately permitted at
cost \(T(h)^2\) per label, where \(T(h)=h^{o(1)}\), the counted
family has an \(h^{3/2+o(1)}=o(h^2)\) internal relocation budget.
This accounting statement does not choose a safe erasure or resolve
constraints involving stubs.

Two remaining cases need different arguments. A cap-constant point
can occupy many ranks with one coordinate value, so the row-visit
energy proof does not apply to that value. For two triangles of the
same parity, both equations depend on one offset. Even with raw
coordinates, the \(h^{-2}\) probability in Section 4 is unavailable.
The distinct-offset same-parity example in the local-anchor note
shows why this case cannot be omitted.

Independent review: the complete written proof passed a separate audit.
The review checked the row-strip packing, divisor-energy sum, modulus
preimage count, fixed-displacement union, and the two independent
offset constraints. The cap-constant and same-parity exclusions remain
part of the theorem's scope.
