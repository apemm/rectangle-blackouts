# Two colors for an expanding R2s parameter family

15 November 2026. Fix upper bounds on the positive row increment
\(\delta\) and the smaller factor \(\min(a,b)\) in the exact R2s
parametrization. Beyond a finite row threshold, the corresponding
row-pair graph has no increasing path of length two. It is therefore
bipartite.

The threshold is not quantified. A diagonal choice nevertheless lets
both parameter bounds tend to infinity while retaining two colors
on every fixed bulk interval \([\eta h,h]\). This does not color the
complementary parameter family or prove the quadratic-width theorem.

## 1. Exact parameters and the statement

For a positive-offset crossed R2s support above a constant sea, write
\(n\) for the lower core row's distance from the sea. The exact
parameters satisfy
\[
 \begin{gathered}
 \delta>0,\qquad T>0,\qquad a,b>0,\\
 4ab=T^2+\delta^2,\qquad U=T+a+b,\qquad
 n={T(T+a+b)\over\delta}.                         \tag{1}
 \end{gathered}
\]
For an integral support these parameters are integers. In the
usual orientation, \(a=X-T\) and \(b=U-X\). Interchanging \(a,b\)
does not change \(U,n,T,\delta\).

For positive integers \(A,D\), retain every row edge
\(n\to n+\delta\) that has at least one witness with
\[
                  \delta\le D,\qquad \min(a,b)\le A. \tag{2}
\]
The row graph may impose the actual column residues, strip tests,
and strong locality. The theorem also holds after dropping all
those additional tests.

**Theorem.** For every \(A,D\), there is a finite \(N(A,D)\) such
that the graph induced on \(n>N(A,D)\) has no directed path of
length two. In particular it admits a proper two-coloring.

The bound concerns an entire parameter union, not one fixed slope
or one factor at a time.

## 2. The curve for two consecutive edges

Choose the smaller of \(a,b\), and call it \(a\). Equation (1) gives
\[
 U={ (T+2a)^2+\delta^2\over4a},\qquad
 n=F_{a,\delta}(T):=
       {T\{(T+2a)^2+\delta^2\}\over4a\delta}.       \tag{3}
\]
Thus a path with successive witness pairs
\((a_1,\delta_1),(a_2,\delta_2)\) gives a positive integral point
\((T,W)\) on
\[
 F_{a_1,\delta_1}(T)+\delta_1
                  =F_{a_2,\delta_2}(W).          \tag{4}
\]

For each fixed pair of parameter pairs, this affine cubic is
absolutely irreducible. Here is the argument.

A complex-reducible real cubic has a real affine line component.
Indeed, it has a complex linear factor. If that factor is not
defined over the reals, its conjugate is another factor, leaving a
real linear factor. A vertical or horizontal line cannot divide
(4), because both univariate cubic leading coefficients are nonzero.
Every remaining real line has the form
\[
                            W=\alpha T+\beta.
\]
Its leading coefficients force \(\alpha>0\).

Such a line would supply polynomial witnesses for the common
nonconstant cubic \(N(T)=F_{a_1,\delta_1}(T)\), with three fixed
row offsets
\[
                            0,\quad \delta_1,\quad
                            \delta_1+\delta_2.
\]
For each edge, take \(U\) from (3) and
\(V=U-T-2a\), using \(W\) in place of \(T\) on the second edge.
These satisfy the exact norm equations and have \(U,T>0\)
eventually. They would therefore give the polynomial two-edge path
excluded by
[the common-cubic threshold theorem](continuation_r2s_cubic_row_family.md).
This contradiction excludes every real line component, proving
absolute irreducibility.

This use of the earlier theorem needs neither integral values of
the affine-line coefficients nor the locality inequality. Its
eventual-positive real-polynomial formulation is essential here.

## 3. Three points at infinity give finiteness

Write the positive cubic leading coefficients in (4) as
\[
                       c_i={1\over4a_i\delta_i}.
\]
The projective closure meets the line at infinity in
\[
                         c_1T^3-c_2W^3=0.        \tag{5}
\]
There are exactly three distinct geometric points. At each,
both \(T,W\) are nonzero, and the partial derivative with respect
to \(T\) is \(3c_1T^2\ne0\). Each point is therefore nonsingular.
They remain three distinct points after normalization, and an
affine coordinate has a pole at each.

Siegel's theorem now gives finitely many integral points on (4).
For the precise version used here, see the introduction and
Theorem 1.1 of
[Alvanos, Bilu, and Poulakis, *Characterizing algebraic curves with infinitely many integral points*](https://arxiv.org/html/0907.2097v1).
Their formulation defines infinity points as places of the function
field where an affine coordinate has a pole. It applies to an
irreducible affine curve without assuming the given plane model
is smooth. Thus possible finite singularities cause no additional
hypothesis in this application.

There are finitely many choices
\(1\le a_i\le A,\ 1\le\delta_i\le D\). The union of their positive
integral solutions is finite. Consequently only finitely many
vertices occur in paths of length two satisfying (2). Take
\(N(A,D)\) larger than all of them.

To obtain the coloring on the remaining graph, color every vertex
with a positive outgoing degree red, and every other vertex blue.
The target of a red vertex cannot have an outgoing edge, because
that would form a path of length two. Every edge therefore joins
a red vertex to a blue vertex.

The proof gives finiteness rather than a usable numerical threshold.
No effective height estimate is asserted.

## 4. Growing parameter bounds with a fixed two-color palette

Choose nondecreasing finite thresholds \(N_j\) for \(A=D=j\),
enlarging them so that \(N_j\ge j\). Define
\[
 J(h)=\max\bigl(\{j:N_j<\sqrt h\}\cup\{0\}\bigr).
                                                               \tag{6}
\]
Then \(J(h)\to\infty\). On rows \(n\ge\sqrt h\), the entire union
\[
                  \delta\le J(h),\qquad
                  \min(a,b)\le J(h)                 \tag{7}
\]
has a proper two-coloring. In particular, for every fixed
\(\eta>0\), this holds throughout \([\eta h,h]\) once \(h\) is
large enough.

The two cutoffs can instead grow at different sufficiently slow
rates. They can also be decreased to lie below any prescribed
divergent comparison function. The argument supplies no explicit
growth rate.

For fixed \(D\), a finite coloring already follows from coloring
integers by their residue modulo \(D+1\). The new feature is a
two-color palette independent of both expanding cutoffs, after
discarding a sublinear initial row interval.

## 5. An effective bound within one rational cube class

There is an elementary quantitative version when the products
\(a\delta\) belong to one rational cube class. Assume
\(1\le a_i,\delta_i\le B\), where \(B\ge1\), and write
\[
 a_1\delta_1=cq^3,\qquad a_2\delta_2=cp^3,
 \qquad \gcd(p,q)=1.
\]
The numbers \(p,q,c\) are positive integers. Define
\[
 \begin{split}
 X&=3T+4a_1,\qquad Y=3W+4a_2,\\
 B_i&=3(3\delta_i^2-4a_i^2),\\
 C_i&=-4a_i(4a_i^2+9\delta_i^2).
 \end{split}
\]
Then
\[
 F_{a_i,\delta_i}(T)
       ={X^3+B_iX+C_i\over108a_i\delta_i}
\]
with \(Y,W\) on the second side. Setting \(Z=pX\), \(Z'=qY\),
equation (4) becomes
\[
               Z^3-Z'^3+PZ-QZ'+R=0,                 \tag{8}
\]
where
\[
 \begin{split}
 P&=p^2B_1,\qquad Q=q^2B_2,\\
 R&=p^3C_1-q^3C_2+108cp^3q^3\delta_1.
 \end{split}
\]
All coefficients are integers, and
\[
 |P|,|Q|\le21B^4=:K,\qquad |R|\le212B^5=:L.          \tag{9}
\]
Indeed, \(p^3,q^3\le B^2\), \(|B_i|\le21B^2\),
\(|C_i|\le52B^3\), and
\(cp^3q^3\delta_1\le B^5\).

If \(Z\ne Z'\), their positive integral values give
\[
 {3\over4}(Z+Z')^2
 \le |Z^3-Z'^3|
 \le K(Z+Z')+L.
\]
Consequently \(Z+Z'\le8K+\sqrt{8L}\). If \(Z=Z'\),
equation (8) reduces to
\[
                         (P-Q)Z+R=0.
\]
The coefficients \(P-Q,R\) cannot both vanish: otherwise
\(p(3T+4a_1)=q(3W+4a_2)\) would be a line component
of (4), already excluded in Section 2. Thus either there is no
solution or \(Z\le L\). Together,
\[
                         Z+Z'\le424B^5.
\]
It follows that \(T,W<142B^5\), and
\[
 F_{a_1,\delta_1}(T)
 \le {142\{144^2+1\}\over4}B^{15}
 <10^6B^{15}.                                      \tag{10}
\]

**Effective consequence.** Fix any rational cube class. On rows
\(n>10^6B^{15}\), the union of all witnesses in that class with
\(a,\delta\le B\) has no path of length two and is bipartite.
The threshold is uniform over the cube class. For every fixed
\(0<\varepsilon<1/15\), one can therefore take
\(B=h^{1/15-\varepsilon}\) on any fixed bulk interval.

If all witness products \(a\delta\) are exactly equal, then
\(p=q=1\). In this case (9) improves to
\(K=21B^2,L=212B^3\), and the same proof gives
\[
                         n<10^6B^9                 \tag{11}
\]
for every path of length two. The corresponding growing cutoff is
\(B=h^{1/9-\varepsilon}\), for fixed \(0<\varepsilon<1/9\).

These quantitative conclusions apply to one parameter class at a
time. The union of arbitrarily many cube classes is covered by
the nonquantitative theorem, not by (10) with a common threshold.

## 6. Exact construction transfer and remaining scope

Apply the two-coloring separately to the two parity row pools.
The
[row-color product filling construction](continuation_r2s_row_coloring_reduction.md)
then uses at most four color-product runs for the bulk labels.
It keeps the original Hilbert anchors, slows them by a fixed
constant, and fills between retained anchors. It needs no
bounded-gap hypothesis on the color classes. All bulk labels
remain represented, and every R2s support from the parameter
family (7) is excluded within its run.

This is an R2s reduction, not a completed blackout construction.
The omitted low-row labels, edges with larger \(\delta\) or
larger \(\min(a,b)\), singleton P constraints, the other collision
families, and interfaces between runs still need treatment.
The growing cutoff must not be treated as a quantified power of
\(h\).

The complete saved proof passed independent written review, including
the real-line reduction, all three infinity places, the finite parameter
union, both effective exponents, and the construction scope. The
integral-point source was independently checked directly in its primary
version.

