# The board payoff of a polynomial chromatic saving

14 November 2026. The optimization below is proved. Every improved board
bound in this note is conditional on a new chromatic estimate.
The stride-menu version also needs a degree-cap transfer that the current
menu audit does not supply.

Let \(\Lambda=\log h\). Suppose, for some fixed \(0<\delta\le1\), that
the relevant primary distance graphs admit
\[
 \chi(G_T[\tau])\le C(1+\kappa_T)^\delta
 \tag{1}
\]
uniformly in \(h,T,\tau\). A bound for the full graph \(G_T\) implies (1).
No such power saving with \(\delta<1\) is established here.

The two assembly routes have different costs. Independent random
refinement alone loses much of the gain. The degree-cap method avoids
that loss.

## 1. The degree-cap input and its scope

The companion
[assembly note](continuation_chi_assembly_requirements.md)
proves the elementary refinement statement:
if \(G\) has a proper \(c\)-coloring and the auxiliary graph has
back-degree at most \(d\), their union is colorable with \(c(d+1)\)
colors.

The corrected stride-four degree-cap theorem supplies
\[
 d=9(D-1)+6,\qquad D=\lceil\Lambda^\eta\rceil,
 \tag{2}
\]
outside a coordinate-defined exceptional set. All labels, including that
set, must retain a primary color. The auxiliary graph uses only
nonexceptional endpoints. The exceptional set has the stated weighted
relocation cost \(h^2(\log\log h)^{O_\eta(1)}\).

Consequently a primary class cap \(A\) becomes
\(O(A\Lambda^\eta)\), without needing a degree bound for the primary
graph or a pair-correlation law for its coloring.

This uses the corrected statement in
\( \texttt{audit\_degree\_capped\_colouring.md}\), including its board
hypotheses. That audit treats stride four. The stride-menu audit
explicitly does not use the degree-cap theorem at other strides.
Thus a menu application below additionally assumes:

- the analogue of (1) for every chosen stride;
- a valid degree-cap and relocation transfer for those stride boards.

The exponent \(1.3108172+\varepsilon\) already obtained by the audited
menu construction does not require these new assumptions.

## 2. Optimization with a general moment exponent

Suppose the primary distance counts satisfy, for every fixed \(a>0\),
\[
 \sum_T(1+\kappa_T)^a
 \ll_a h\Lambda^{b(a)}.
 \tag{3}
\]
Threshold the primary chromatic bound at \(A=\Lambda^x\).
By (1), a diagonal that fails this threshold has
\(\kappa_T\gg A^{1/\delta}\). The moment estimate and the existing heavy
diagonal relocation price give a contribution
\[
 h^2\Lambda^{b(a)+2}A^{-a/\delta}.
 \tag{4}
\]
The light contribution after degree-cap refinement is
\[
 h^2 A\Lambda^\eta.
 \tag{5}
\]
The remaining degree-cap cost has only powers of \(\log\log h\).
Letting the arbitrarily small fixed \(\eta\) be absorbed into the final
exponent loss, balancing (4) and (5) gives
\[
 E_{\rm DC}(\delta)
 =\inf_{a>0}\frac{b(a)+2}{1+a/\delta}.
 \tag{6}
\]
The resulting conditional statement has exponent
\(E_{\rm DC}(\delta)+\varepsilon\), for every fixed \(\varepsilon>0\).

## 3. A saving at stride four alone

For stride four,
\[
 b_1(a)=\frac{3^a-1}{2}.
 \]
Therefore the conditional exponent using only this stride is
\[
 E_{1,\rm DC}(\delta)
 =\inf_{a>0}\frac{\delta(3+3^a)}{2(\delta+a)}.
 \tag{7}
\]
Put \(\lambda=\log3\), and let \(W\) denote the positive real inverse of
\(z\mapsto ze^z\). Differentiating (7) gives
\[
 z=W(3e^{\lambda\delta-1}),\qquad
 a_*=\frac{1+z}{\lambda}-\delta,\qquad
 E_{1,\rm DC}(\delta)=\frac{3\lambda\delta}{2z}.
 \tag{8}
\]
For \(0<\delta\le1\), \(a_*>0\), so this is the interior minimum.

| Assumed power \(\delta\) | Conditional exponent | Optimizing moment \(a_*\) |
| ---: | ---: | ---: |
| \(1\) | \(1.496742913\) | \(0.912415343\) |
| \(0.9\) | \(1.420408175\) | \(0.960670253\) |
| \(0.75\) | \(1.285210110\) | \(1.035582481\) |
| \(0.5\) | \(0.990421407\) | \(1.167492649\) |

The function in (7) is strictly increasing in \(\delta\). For fixed
\(a>0\), the factor \(\delta/(\delta+a)\) increases strictly, and the
displayed minimizer remains finite and positive.
Comparison with the current menu limit
\(1.310817196592256\) gives the numerical threshold
\[
 \delta<0.776216335\ldots.
 \tag{9}
\]
Thus a power saving only for the original stride-four graph would need
to pass (9) to beat the current menu exponent by this assembly route.
A square-root chromatic bound would be more than sufficient.
These are implications of the unproved estimate (1), not new board bounds.

## 4. The conditional stride-menu limit

For a menu of \(m\) independent quadratic fields, the existing moment
exponent is
\[
 b_m(a)=\left(\frac{1+3^{a/m}}2\right)^m-1.
 \tag{10}
\]
If the additional menu hypotheses in Section 1 hold, (6) applies with
this \(b_m\). Taking larger fixed menus approaches
\[
 b_\infty(a)=3^{a/2}-1,
 \]
and therefore
\[
 E_{\infty,\rm DC}(\delta)
 =\inf_{a>0}\frac{\delta(1+3^{a/2})}{\delta+a}.
 \tag{11}
\]
With \(\lambda=\tfrac12\log3\), the exact minimizer is
\[
 z=W(e^{\lambda\delta-1}),\qquad
 a_*=\frac{1+z}{\lambda}-\delta,\qquad
 E_{\infty,\rm DC}(\delta)=\frac{\lambda\delta}{z}.
 \tag{12}
\]
The limit is interpreted with an arbitrarily small exponent loss:
first choose a sufficiently large finite menu, then let \(h\) grow.

| Assumed power \(\delta\) | Conditional menu-limit exponent |
| ---: | ---: |
| \(1\) | \(1.310817197\) |
| \(0.9\) | \(1.226568459\) |
| \(0.75\) | \(1.084499751\) |
| \(0.5\) | \(0.799738186\) |

Every fixed \(\delta<1\) improves the limiting exponent if both the
chromatic saving and the menu degree-cap transfer are proved.

## 5. What independent random refinement would give instead

Without degree capping, start from \(A\) primary colors and assign each
label an independent secondary color among \(K\) choices. The product
coloring uses \(AK\) colors and gives pair-collision probability at most
\(1/K\).

Write \(A=\Lambda^x\), \(K=\Lambda^y\). The three exponent terms are
\[
 x+y,\qquad 2-y,\qquad b(a)+2-xa/\delta.
 \tag{13}
\]
At the interior optimum, \(x=2E-2\), \(y=2-E\), giving
\[
 E_{\rm iid}(\delta)
 =1+\inf_{a>0}\frac{b(a)+1}{1+2a/\delta}.
 \tag{14}
\]
For the menu-limit moment, this simplifies to
\[
 E_{\infty,\rm iid}(\delta)
 =1+\frac{\delta\log3}{4}
          \exp\left(1-\frac{\delta\log3}{4}\right).
 \tag{15}
\]
For example,
\[
 E_{\infty,\rm iid}(1/2)=1.325393438\ldots,
 \]
which is worse than the current menu limit. This route would need
\(\delta<0.474234243\ldots\) to improve that limit.
Equation (15) is not a limitation on the degree-cap route or on other
coloring laws.

## 6. Why chromatic number alone does not give decorrelation

There is a quantitative obstruction to a universal replacement of
independent refinement by a \(1/B\) pair-collision bound.
Let \(G\) be the complete \(A\)-partite graph with \(N\) vertices in each
part. In any proper coloring with at most \(B\) colors, let \(b_i\) be the
number of colors used in part \(i\). Different parts use disjoint colors,
so \(\sum_i b_i\le B\).

Averaging over distinct ordered pairs in one part, and then over the
parts, the collision probability is at least
\[
 \frac{N\left(A^{-1}\sum_i b_i^{-1}\right)-1}{N-1}
 \ge \frac{NA/B-1}{N-1}.
 \tag{16}
\]
The first inequality is Cauchy--Schwarz applied to color-class sizes; the
second is the harmonic-mean inequality.
The same bound holds under every probability law on proper \(B\)-colorings.
As \(N\to\infty\), it approaches \(A/B\).

This example is also a finite integer distance graph: take vertices
\(0,\ldots,AN-1\), with all positive differences below \(AN\) that are
not divisible by \(A\). Its parts are the residue classes modulo \(A\).
Thus generic integer-distance structure does not remove the obstruction.

This does not prove that the Pell distance graphs require such a loss.
Their auxiliary pairs and their arithmetic structure could admit a
better law. The degree-cap route already avoids asking for one, under
its stated hypotheses.
