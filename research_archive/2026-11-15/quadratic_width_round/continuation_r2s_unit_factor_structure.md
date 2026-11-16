# The unit-factor R2s graph: exact coordinates and descent limits

15 November 2026. The entire family with \(b=U-X=1\) has a short
two-parameter description. It contains directed paths of length two
and vertices with two incoming edges, including in the compatible
odd-row profile. Neither property can therefore establish
acyclicity. Whether this whole family is bipartite remains open.

## 1. Exact parametrization

Use sea row one, core columns \(4\mathbb Z\), positive row increment
\(\delta\in4\mathbb Z\), and the strong locality inequality
\(\delta^2\le2X\). The exact equations are
\[
 4ab=T^2+\delta^2,\quad U=T+a+b,\quad X=T+a,
 \quad n={TU\over\delta}.
\]
If \(a=1\), then \(X=T+1\) is odd, contradicting
\(X\in4\mathbb Z\). Thus the admissible family
\(\min(a,b)=1\) has \(b=1\).

Write \(\delta=4d\) and \(T=2k\). The congruence
\[
 X=k^2+2k+4d^2\equiv0\pmod4
\]
forces \(k\) even. Hence \(T=4m\), and
\[
 \begin{split}
 a&=4(m^2+d^2),\\
 X&=4(m^2+d^2+m),\\
 U&=(2m+1)^2+4d^2=X+1,\\
 V&=T-U+2,\qquad X+V=4m+1,\\
 n&={m\{(2m+1)^2+4d^2\}\over d}.
 \end{split}                                                   \tag{1}
\]
Both sea columns are \(1\bmod4\). The locality condition is
\(d^2\le m(m+1)\), which for positive integers is equivalent to
\[
                              1\le d\le m.          \tag{2}
\]
The remaining integrality condition is
\[
                        d\mid m(2m+1)^2.            \tag{3}
\]
Subject to the strip bound, (1)--(3) give the complete unit-factor
family in this profile.

For fixed \(m\), both endpoint functions are strictly decreasing
in the real variable \(d\in[1,m]\):
\[
 n(d)={m(2m+1)^2\over d}+4md,\qquad
 n(d)+4d={m(2m+1)^2\over d}+4(m+1)d.                 \tag{4}
\]
The second derivative with respect to \(d\) is not needed:
the first derivatives are negative, including at \(d=m\).
Thus a fixed \(m\) has at most one outgoing representation at a
specified source, and at most one incoming representation at a
specified target. This does not give uniqueness after \(m\) varies.

## 2. A compatible directed path and a repeated target

The following exact supports have \(b=1\). Their columns and rows
satisfy every congruence in (1), and \(\delta^2\le2X\).

| Source \(n\) | Target \(n+\delta\) | \(m,d\) | \(X,U,T,V\) |
|---:|---:|---:|---|
| 11830 | 11834 | \(14,1\) | \(844,845,56,-787\) |
| 11834 | 11902 | \(34,17\) | \(5916,5917,136,-5779\) |
| 72150 | 72234 | \(70,21\) | \(21644,21645,280,-21363\) |
| 71910 | 72234 | \(94,81\) | \(61964,61965,376,-61587\) |

Every displayed \(n\) is \(2\bmod4\), so every inserted row
\(n+1\) is \(3\bmod4\). These are not artifacts of an unused row
residue. The first two edges form an increasing path of length two.
The final two edges give one vertex with two distinct incoming
neighbors.

For each row of the table, the black support is
\[
 (0,n+1),\quad (U,1),\quad (X,n+1+4d),\quad (4m+1,1).
\]
Its common white cells are
\[
                 (2m,n+1+2d),\qquad(U+2m,1+2d).
\]
Here \(m\) is even and \(d\) odd. The first white cell has column
in \(4\mathbb Z\) and row \(1\bmod4\), so an odd-\(3\bmod4\),
even-\(2\bmod4\) core cannot blacken it. The second is a sea column
above row one. Thus the displayed supports remain genuine
two-white collisions whenever their two required odd core points
are present in that standard profile. The row graph records these
potential constraints; it does not require that all four listed
supports appear in one proposed core ordering.

The short exact checker
[check_r2s_unit_factor_examples.py](check_r2s_unit_factor_examples.py)
verifies the equations, residues, locality, and white-cell tests.

## 3. Why the direct integer Vieta move leaves the graph

At fixed \(n,T\), the row increment satisfies
\[
          T\delta^2-4n\delta+T(T+2)^2=0.             \tag{5}
\]
The conjugate root is
\[
          \delta^*={(T+2)^2\over\delta}
                   ={(2m+1)^2\over d}.             \tag{6}
\]
The original integrality condition (3) does not imply that
\(\delta^*\) is integral. For example, \(m=2w,d=2\) is admissible
for every \(w\ge1\), while
\(\delta^*=(4w+1)^2/2\) is not integral.

Even when \(\delta^*\) is integral, it is odd. It therefore leaves
the required class \(\delta\in4\mathbb Z\). Also (2) gives
\[
                    \delta<T+2<\delta^*.
\]
So the Vieta swap leaves both the integral residue condition
and, independently, the strong-locality branch whenever those
conditions can be compared.

One can normalize (3) further. If \(m=gr,d=gs\), with
\(\gcd(r,s)=1\), then
\[
                         s\mid(2gr+1)^2,
\]
so \(s\) is odd. This identifies the rational denominator that a
different descent would need to track. It is not yet a descent
or a coloring rule.

The finite checks motivating this branch do not establish a
forest theorem. The exact path and repeated target only eliminate
two proposed shortcuts to such a theorem.

There is nevertheless a uniform counting statement. Equation (4)
gives \(n(m,d)\ge n(m,m)=8m^2+4m+1\), so \(n\le h\)
forces \(m\le\sqrt{h/8}\). For each \(m\), (3) permits at most
\(\tau(m(2m+1)^2)\) increments. The entire unit-factor graph
therefore has \(h^{1/2+o(1)}\) edges through height \(h\).
The growing-factor version is proved in
[the small-factor count](continuation_r2s_small_factor_sparsity.md).

The complete saved proof and all four exact support certificates passed
independent written and integer-checker review.

