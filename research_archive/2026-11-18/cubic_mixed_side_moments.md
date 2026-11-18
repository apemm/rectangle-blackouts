# Bounded moments for crossed mixed supports on affine diagonals

In a fixed row role of an affine diagonal band, true columns differ by \(\kappa\Delta\) when the true rows differ by \(\Delta\), with a fixed nonzero integer slope \(\kappa\). Take a sea row \(s\). The mixed supports with one true and one sea point in each of their side and diagonal give the same equations as [the constant-star calculation](cubic_star_mixed_graph.md), with \(4\) replaced by \(\kappa\). If the side starts at a sea point and ends at a true row of signed gap \(g=y-s\ne0\), then for \((a,b)=1,b>0,k\ne0\),
\[
 u=bk,\qquad g=k(a-2\kappa b),\qquad
 \Delta(a^2+b^2)=4kb^2(\kappa b-a).
\]
Here \(u\) is the horizontal component of the black side, \(\Delta\) the difference of the two true rows, and the diagonal's signed horizontal component is \(v=u+(a/b)\Delta\). This derivation uses no strip truncation. It overcounts when the sea columns or the common corners are unavailable.

For a nonzero side gap define its *side degree* to be the number of possible ordered mixed supports for that given true endpoint in the band. For every fixed integer \(r\ge1\),
\[
 \sum_{0<|g|\le h} \operatorname{deg}_{\rm side}(g)^r\ll_{\kappa,r}h .
 \tag{1}
\]
The constants are uniform in the sea level, the retained true rows, and the length of the band.

To prove this put \(d=\gcd(a^2+b^2,4b^2(\kappa b-a))\). Since \((a,b)=1\), one has \(d\le4(1+\kappa^2)\). The base side modulus is
\[
 A(a,b)=|a-2\kappa b|(a^2+b^2)/d .
\]
Every admissible pair \(a,b\) forces \(A(a,b)\mid g\); then \(k\) is fixed, as are all four endpoints for the given side true point. Exclude \(a=2\kappa b\), which would give \(g=0\). Count moduli with their multiplicities.

First, \(\#\{(a,b):A(a,b)\le U\}\ll_\kappa U^{2/3}\). If \(b\le U^{1/3}\), then \(|a|\ll_\kappa U^{1/3}\), since for \(|a|>4|\kappa|b\) the numerator is at least \(|a|^3/2\). If \(b>U^{1/3}\), \(|a-2\kappa b|\ll_\kappa U/b^2\); this nonzero integer has \(O_\kappa(U/b^2)\) possible values. Summing over \(b\) gives the same bound. Moreover any fixed \(A\asymp U\) occurs \(U^{o(1)}\) times. For each of the bounded choices of \(d\), the nonzero signed \(a-2\kappa b\) divides \(dA\). Once it is fixed, \(a^2+b^2\) is fixed and the equation in \(b\) is quadratic.

Let \(F_U(g)\) count the divisibility indicators with \(U\le A<2U\). The average of \(F_U(g)^r\) over \(1\le g\le h\) is at most the sum of \(1/L\) over ordered \(r\)-tuples of moduli, \(L\) denoting their least common multiple. Fix the first modulus with multiplicity. Then \(L\le(2U)^r\) and \(A_1\mid L\). For each \(L\), all the other entries are divisors of \(L\); including multiplicities there are at most \(U^{o_r(1)}\) choices for their tuple by the maximal divisor bound. Sum \(1/L\) over the multiples of \(A_1\) in this range to obtain \(O_r(\log(2U)/U)\). The preceding count of first moduli gives
\[
 \frac1h\sum_{g\le h}F_U(g)^r\ll_{\kappa,r}U^{-1/3+o_r(1)}.
\]
The \(L^r\) triangle inequality and summation over dyadic \(U\) prove (1). A finite set of roles and sea rows obeys the same estimate by another triangle inequality. For every \(\epsilon>0\), \(B>0\), remove the labels whose total side degree exceeds \((\log h)^\epsilon\). Taking \(r>B/\epsilon\) gives \(O_{\epsilon,B}(h/(\log h)^B)\) removed labels on each diagonal. Orient each remaining support from its side label. Every induced subgraph then has average degree at most \(2(\log h)^\epsilon\) up to a fixed factor, so greedy coloring uses \(O((\log h)^\epsilon)\) colors.

For a short support \(|u|\le H\) with \(G\le|g|\le2G,\ G\ge C_\kappa H\), the parameter equations give \(|a|\gg_\kappa bG/H\) and \(|a-2\kappa b|\asymp_\kappa|a|\). Hence the number of such side rows is
\[
 O_\kappa\left(\sum_{b\ge1}\sum_{|a|\gg bG/H}G/|a|^3\right)
 =O_\kappa(H^2/G).
\]
With \(k=\ell(a^2+b^2)/d\) the same calculation gives \(|g|\asymp_\kappa|\ell|\,|a|^3\) and \(|\Delta|\asymp_\kappa|\ell|b^2|a|\), and in particular \(|g|^{1/3}\ll_\kappa|\Delta|\ll_\kappa H^2/|g|\).

For example, take \(H=h/(\log h)^\beta\), \(\beta>1\), and \(Y=h/(\log h)^\delta\) with \(0<\delta<\min(\beta,2\beta-2)\). On a fixed parallel diagonal the labels having either endpoint within \(Y\) of any fixed sea row occupy a bounded number of intervals, of total physical span \(O_\kappa(Y)\). After the high-degree omissions above, copies colored with \(\epsilon=\delta/2\), including width-\(H\) guards, cost \(O_\kappa((Y+H)(\log h)^{\delta/2})=O_\kappa(h)\). For all other labels the short-support count summed over dyadic \(G\ge Y\) removes at most \(O_\kappa(H^2/Y)=O(h/(\log h)^{2\beta-\delta})\) side rows. This bounds the physical cost per existing true-rival color for the crossed mixed family. Other families, omitted-label relocation, and transitions still require separate board arguments.
