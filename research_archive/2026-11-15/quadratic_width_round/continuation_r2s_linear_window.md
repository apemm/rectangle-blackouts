# A linear window for same-sea R2s collisions

15 November 2026. Under the spacing-four same-parity norm-gap
condition, every crossed R2s collision at the row-one sea has full
horizontal span at most \(h-1\). This includes both rectangles,
not only their four-point black symmetric difference. At any fixed
low sea row \(s\), the analogous bound is \(O_s(h)\). Reflection
gives the same conclusion for a sea within a fixed distance of
the top boundary.

The result is deterministic. It does not avoid the collisions, select
permutations, or supply safe collars at newly introduced cuts.

## 1. Positive row increments

Use
\[
 A=(0,n+s),\ B=(U,s),\
 C=(X,n+s+\delta),\ D=(X+V,s),\qquad n>0.
\]
For an R2s support,
\[
 TU=n\delta,\quad
 V^2=U^2-2n\delta-\delta^2,\quad
 2X=U+T-V,
\]
and the common corners are
\[
 P=(T/2,n+s+\delta/2),\qquad
 Q=(U+T/2,s+\delta/2).                              \tag{1}
\]
The two core rows have the same prescribed residue modulo four,
so \(\delta\in4\mathbb Z\setminus\{0\}\), and \(T\) is even.
Assume
\[
                         \delta^2\le2|X|.           \tag{2}
\]

Suppose first that \(\delta>0\). Reflect horizontally to make
\(U>0\), and hence \(T>0\). The norm equation implies
\[
                         0<T<X<U.
\]
The exact classification in
[the side-slope note](continuation_r2s_fixed_side_slope_permutations.md)
shows that \(U>n\) is impossible. Equivalently,
\[
                              T\ge\delta.            \tag{3}
\]
For a short direct summary, put \(a=X-T>0,b=U-X>0\). Then
\(4ab=T^2+\delta^2\). Assuming \(T\le\delta\), locality forces
\(b\le\delta/(\delta-2)\). The cases \(b=1\) and the possible
\(\delta=4,b=2\) both force \(T=\delta\); there is no case
\(T<\delta\).

Since \(X+V=T+b\), all four black support columns lie in \([0,U]\).
The common corner at \(Q\) is farther right. The full six-point span
is exactly \(U+T/2\), because \(P\) lies strictly between zero and
\(U\). Crucially,
\[
 n+\delta/2-U-T/2
     =(T-\delta)\left({U\over\delta}-{1\over2}\right)\ge0.        \tag{4}
\]
Here \(U>2T\ge2\delta\). The in-strip upper common row in (1)
therefore gives
\[
                   \operatorname{span}
                     =U+T/2\le n+\delta/2\le h-s.    \tag{5}
\]
This corrects the possible confusion between the black-support
span \(U\) and the full rectangle span \(U+T/2\).

At \(s=1\), the lower common row \(1+\delta/2\ge1\) excludes
negative \(\delta\). Thus (5) covers every crossed R2s support
at the row-one sea.

The isolated seam \((|X|,|\delta|)=(4,4)\), allowed by the fine
interpolation geometry, causes no missing positive-offset case.
After reflection, substitution of \(X=\delta=4\) gives
\[
              4(T-4)U+(T-8)^2+16=0.
\]
Positive even \(T\ge4\) makes the left side positive, while
\(T=2\) would require \(U=13/2\). Thus there is no integral support.

## 2. Negative increments at another fixed low sea

Suppose \(\delta=-d<0\), both core rows are strictly above \(s\),
and all corners are in the strip. The lower common row gives
\[
                     4\le d\le2(s-1),\qquad n>d.
\]
Reflect horizontally so \(U>0\). Now \(T<0\), and
\[
            V^2-U^2=d(2n-d)=:N>0,\qquad |T|=nd/U.
\]
The integer factorization
\[
                      (|V|-U)(|V|+U)=N
\]
gives \(U\le nd\) and \(|V|\le nd\); also \(|T|\le nd\).

Every column in (1), including \(X\) and \(X+V\), lies in
\[
 \left[-{|T|+|V|\over2},\,
        U+{|T|+|V|\over2}\right].
\]
Consequently
\[
 \operatorname{span}\le U+|T|+|V|
              \le3nd\le6(s-1)h.                    \tag{6}
\]
No norm-gap assumption was needed in this bounded negative-offset
case, so it includes any negative seam exception as well.

For a fixed list of low sea rows, (5)--(6) give one constant
\(C\) such that all of their crossed R2s collisions have full span
at most \(Ch\). Apply the vertical reflection
\(y\mapsto h+1-y\) for the corresponding upper-sea statement.

## 3. Scope

The conclusions apply to the crossed two-core/two-sea family with
both sea points on the same actual row. Other assignments of the
black corners, different sea rows, and other residual families need
their own classification. In the constant-sea assembly these are
separate established sieve questions.

The window can be used in later local interaction arguments.
It does not by itself justify deleting columns, filling a cut,
or applying an external relocation construction.

Independent written review: the complete note passed a separate
derivation, including the full-span identity, the positive seam
exclusion, and the factor bounds for negative increments.

