# A common cubic row family cannot replicate an R2s path

15 November 2026. The R2s row-pair graph has small triangles and
increasing paths in exact computations. There is nevertheless a
structural obstruction to one natural way of reproducing them at
arbitrarily large heights: fixed row offsets from a common cubic,
with polynomial witnesses, cannot contain an increasing path of
length two. All edges in such a family cross one common threshold
in the offsets.

This is not a bounded-coloring theorem for the full row-pair graph.
It concerns a specific algebraic family, and it does not assert
that all actual supports admit this form.

## 1. Polynomial-witness model

Let \(N(t)\in\mathbb R[t]\) be nonconstant, with positive leading
coefficient and \(1\le\deg N\le3\), and let \(c_1,\ldots,c_m\) be distinct real
constants. The row-distance polynomials are
\[
                         n_i(t)=N(t)+c_i.
\]
Consider an edge \(i\to j\), with the fixed positive increment
\(\delta=c_j-c_i>0\). Require polynomials \(U,T,V\) satisfying
\[
 UT=n_i\delta,\qquad
 V^2=U^2-2n_i\delta-\delta^2,                         \tag{1}
\]
and eventually \(U,T>0\). These are necessary equations for a
positive-offset row-one R2s support after choosing its horizontal
orientation. If a proposed integral family satisfies them on an
unbounded sequence of parameter values, they hold as polynomial
identities.

The theorem below does not need the column residues or norm-gap
inequality. It therefore applies to every such polynomial family
that passes those additional tests.

## 2. A nonconstant family must have degree three

The norm equation gives \(U>2T\) for sufficiently large positive
\(t\). Thus \(\deg U\ge\deg T\). Since \(UT=n_i\delta\),
\[
                         2\deg T\le\deg N\le3.
\]
If \(T\) were constant, the identity
\[
                (U-T-V)(U-T+V)=T^2+\delta^2           \tag{2}
\]
would force both factors to be constant polynomials, hence \(U\)
and \(n_i\) constant. Therefore \(T\) has degree one.

The quadratic \(T^2+\delta^2\) has no real root and is irreducible
over \(\mathbb R[t]\). Equation (2) consequently has one constant
factor. Both factors are eventually positive because
\(|V|<U-T\); write that constant as \(2a\), with \(a>0\).
Then
\[
 U={ (T+2a)^2+\delta^2\over4a},\qquad
 n_i={T\{(T+2a)^2+\delta^2\}\over4a\delta}.            \tag{3}
\]
In particular \(N\) has degree three. There is no nonconstant
degree-one or degree-two family in this model.

## 3. One threshold separates all sources from all targets

Make a common affine change of parameter so that
\[
                         N(z)=Az^3+Bz+C,\qquad A>0.
\]
Comparing the quadratic coefficients in (3) shows that
\[
                         T=rz-4a/3,\qquad r>0.
\]
Expanding (3) gives
\[
 \begin{split}
 A&={r^3\over4a\delta},\\
 B&={r(\delta^2-4a^2/3)\over4a\delta},\\
 C+c_i&=-{\delta\over3}-{4a^2\over27\delta}.
 \end{split}                                                   \tag{4}
\]
Put
\[
 x={a\over r}>0,\qquad w={\delta\over r}>0,\qquad C_0={B\over A}.
\]
Then
\[
 w^2=C_0+4x^2/3,\qquad r=4Axw.
\]
The two constant terms for the edge are therefore
\[
 \begin{split}
 C+c_i&=f(x):=-{4A\over27}x(9C_0+16x^2),\\
 C+c_j&=g(x):={4A\over27}x(18C_0+20x^2).
 \end{split}                                                   \tag{5}
\]
Their difference is \(\delta>0\), as required.

If \(C_0\ge0\), then \(x>0\), \(f(x)<0<g(x)\).
If \(C_0<0\), put \(x_0=\sqrt{-3C_0/4}\).
The condition \(w>0\) gives \(x>x_0\). On this interval \(f\)
is strictly decreasing and \(g\) strictly increasing. Their common
endpoint value is
\[
             f(x_0)=g(x_0)={4AC_0\over9}
                                      \sqrt{-3C_0/4}.
\]
Thus, in both cases, there is a number depending only on the common
cubic,
\[
 \theta=
 \begin{cases}
 -C,&C_0\ge0,\\
 \displaystyle {4AC_0\over9}\sqrt{-3C_0/4}-C,&C_0<0,
 \end{cases}
\]
such that every edge satisfies
\[
                              c_i<\theta<c_j.        \tag{6}
\]

**Conclusion.** The entire polynomial-witness graph is bipartite,
with all edges directed from the lower part to the upper part.
No vertex can be both the target and the source of an edge.
In particular there is no directed path of length two, and no
triangle or other odd cycle.

The conclusion permits different witness polynomials and different
fixed increments on different edges. The common nonconstant cubic
and fixed vertex offsets are essential.

## 4. What remains open

The full R2s row graph allows increments and witness parameters
that depend on height without belonging to one polynomial family.
Its bounded chromatic number is not settled by (6). The observed
small triangles and longer increasing paths therefore do not
contradict this theorem: they are isolated finite configurations,
not a proven common-cubic replication.

Similarly, a partition-regularity theorem for unrestricted
homogeneous forms would not automatically give an obstruction
inside the strong-locality graph. The required integral scale and
norm-gap inequalities must survive the extraction.

Independent written review: two separate readers checked the complete
saved proof, including the nonconstant hypothesis, degree split,
positive factor, depressed coefficients, derivative signs, and exact
scope of the common threshold.

