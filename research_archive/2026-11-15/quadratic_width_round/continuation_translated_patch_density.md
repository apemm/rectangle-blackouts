# Translated triangular patches can have logarithmic genuine P density

15 November 2026. The strip condition and triangular locality do not,
by themselves, force bounded P degree. For every fixed stride and
row-residue pair, some translated triangular patch has average
genuine P degree at least a constant times \(\log h\). Its P gaps
are proportional to \(h\), so a cutoff \(h^{1/2-o(1)}\) does
not remove them.

The translation is selected by averaging. This note does not show
that a selected translation occurs as a recursive patch in the new
full-size occupied scaffold. It also fixes the patch order before
selecting the translation. Permutations chosen separately for each
translation are outside the statement.

Independent review checked the primitive progression count, the
dyadic summation, the angular constants, the translation count, and
the genuine-corner and owner claims. The proof passed without
corrections.

## 1. The translated-patch theorem

Fix an even row step \(D\), an integer stride \(S\) divisible
by four, an odd base \(a_0\), and an even base \(b_0\). All
these parameters are independent of the height \(h\). Put
\(c_0=b_0-a_0\).

Choose \(n\) so that
\[
 N=|T_n|=n(n+1)/2\sim h/S.
\]
Fix any bijective order \((u_r,v_r)\), \(0\le r<N\), of
\(T_n=\{(u,v):u,v\ge0,\ u+v<n\}\). The triangular order
from the hole-free construction is one permitted choice. Put
\(I=\lfloor h/(4D)\rfloor\). For an integer translation \(T\),
label at slot \(r\) has row indices
\[
 i_r=I+u_r,\qquad j_r=I+T+u_r+v_r,
\tag{1}
\]
and physical black rows \(a_0+Di_r\), \(b_0+Dj_r\).
Its column is \(Sr\), up to a common translation.

For all sufficiently large \(h\), some integer
\[
 \frac{h}{4D}\le T\le\frac{h}{2D}
\tag{2}
\]
gives at least
\[
 c_{S,D}\,N\log h
\tag{3}
\]
distinct genuine P edges between patch labels. The constant is
positive and may also depend on the fixed bases. Every counted edge
has slot gap
\[
 \frac{h}{50S}<q<\frac{h}{14S}.
\tag{4}
\]
Both common corners stay inside the strip. Their owner is in the
same row-residue block and lies outside the patch. Thus these are
actual rectangle collisions whenever the owners are retained
elsewhere in the board.

Consequently the simple graph of these P edges has average degree
\(\Omega_{S,D}(\log h)\). Its degeneracy is also
\(\Omega_{S,D}(\log h)\), because a graph of degeneracy \(d\)
has at most \(dN\) edges.

## 2. Enough odd Pythagorean vectors in the strip

There are \(\Omega_{S,D}(h\log h)\) distinct integer triples
\((X,Y,L)\) with
\[
 X^2+Y^2=L^2,\qquad S\mid X,\qquad
 Y\equiv c_0\pmod D,
\tag{5}
\]
and
\[
 \frac h3\le Y\le\frac{5h}{12},\qquad
 \frac h{50}<X<\frac h{14},\qquad
 L<\frac{3h}{7},\qquad L-Y<\frac h{160}.
\tag{6}
\]
Moreover \(X/S\) is even, and \(Y,L\) are odd.

Here is an elementary count. Fix an even multiple \(M_0\) of
both \(S\) and \(D\). At a dyadic scale \(M\), take
\[
 m=M_0 a,\quad M\le a<2M,
\qquad
 \frac{M_0M}{16}\le n_0\le\frac{M_0M}{12},
\quad n_0\equiv1\pmod{2M_0},
\quad \gcd(a,n_0)=1.
\tag{7}
\]
There are \(\Omega_{M_0}(M^2)\) such pairs. To check this
density directly, use
\(1_{\gcd(a,n_0)=1}=\sum_{d\mid a,n_0}\mu(d)\).
Only \(d\) coprime to \(2M_0\) occur. The two interval counts
are \(M/d+O(1)\) and \(M/(96d)+O(1)\). Summing gives
\[
 \frac{M^2}{96}
 \prod_{p\nmid2M_0}(1-p^{-2})+O_{M_0}(M\log M).
\tag{8}
\]
The product is positive, since \(\sum_p p^{-2}<\infty\).

The integers \(m,n_0\) are coprime and have opposite parity.
They produce the primitive triple
\[
 X_0=2mn_0,\qquad Y_0=m^2-n_0^2,\qquad L_0=m^2+n_0^2.
\]
Their ratio obeys \(1/32\le n_0/m\le1/12\), and
\(Y_0\equiv-1\pmod D\). Multiply by positive integers \(d\)
in the progression
\[
 d\equiv-c_0\pmod D,
 \qquad \frac{h}{3Y_0}\le d\le\frac{5h}{12Y_0}.
\tag{9}
\]
Every such \(d\) is odd. At scales with
\(Y_0\le h/(100D)\), the number of choices is
\(\Omega_D(h/Y_0)=\Omega_{S,D}(h/M^2)\).
Therefore each sufficiently large dyadic scale
\(M\le c_{S,D}\sqrt h\) contributes
\(\Omega_{S,D}(h)\) triples. There are \(\Omega(\log h)\)
such scales.

These triples are distinct. Their primitive triple is recovered by
dividing by the common gcd, and then
\(m^2=(L_0+Y_0)/2\), \(n_0^2=(L_0-Y_0)/2\).
The disjoint dyadic ranges of \(a\) prevent double counting
between scales.

The angle bounds in (7) give
\[
 \frac{64}{1023}\le\frac X Y\le\frac{24}{143},
 \qquad \frac L Y\le\frac{145}{143},
 \qquad \frac{L-Y}{Y}\le\frac2{143}.
\]
Together with the range of \(Y\), these prove (6).
Finally, \(S\mid m\) gives even \(X/S\), and
\(d n_0^2\equiv-c_0\pmod D\).

## 3. Averaging over translations

Fix one triple from (5)--(6), and put \(q=X/S\). For every
\(0\le r<N-q\), there is a unique integer translation
\[
 T=\frac{Y-c_0}{D}
   -(u_{r+q}+v_{r+q}-u_r)
\tag{10}
\]
for which the odd point at slot \(r\) and even point at slot
\(r+q\) have vertical difference \(Y\).
The correction in parentheses is \(O(n)=O_{S}(\sqrt h)\).
Thus (6) puts (10) inside the range (2), for all sufficiently
large \(h\).

Since \(q<h/(14S)\) and \(N\sim h/S\), each triple gives
at least \(N/2\) edges, counted across the translations. A fixed
translation and rank pair determines its vector \((X,Y)\), so
different triples cannot count the same edge twice. Section 2 gives
\[
 \sum_T E_T\ge c_{S,D}N h\log h.
\]
There are \(O_D(h)\) translations in (2). One therefore
satisfies (3).

The logarithmic order is also an upper bound for the translation
average of all genuine P edges. There are \(O(h\log h)\)
positive integer Pythagorean triples with hypotenuse at most \(h\).
Indeed every such triple is a positive multiple of a primitive
triple, and the usual coprime-factor parametrization gives
\[
 \#\{(X,Y,L):L\le h\}
 \le C\sum_{m\le\sqrt h}\sum_{1\le n_0<m}
       \frac{h}{m^2+n_0^2}
 \le C h\sum_{m\le\sqrt h}\frac1m
 =O(h\log h).
\]
Dropping parity and stride restrictions only increases this bound.
For either opposite-parity role, one triple and one rank pair give
at most one translation. Thus a triple contributes at most \(2N\)
edges across the entire translation family. Since (2) has
\(\Theta_D(h)\) translations, the average genuine edge count is
\[
 \frac1{\#\{T\}}\sum_T E_T=\Theta_{S,D}(N\log h).
\tag{12}
\]
This is a statement about the translation average, not a uniform
upper bound for each translation.

## 4. The counted edges are genuine

Write the odd and even endpoint rows as \(A\) and \(B=A+Y\).
The common vertical diagonal has rows
\[
 A-w,\qquad B+w,
\quad w=(L-Y)/2=d n_0^2.
\tag{11}
\]
Its column is the midpoint of slots \(r,r+q\). Because \(q\)
is even, that midpoint is another occupied slot inside the patch.

Uniformly over translations (2), the patch odd rows are
\(h/4+O_{S,D}(\sqrt h)\), while its even rows lie between
\(h/2+O_{S,D}(\sqrt h)\) and
\(3h/4+O_{S,D}(\sqrt h)\). Equations (6) and (11) place
both common rows strictly inside the strip. The lower common row
cannot be an even row of any patch label, and the upper common row
cannot be an odd row of any patch label. The midpoint corners are
therefore white in the label-only patch.

Since \(w\) is odd, the lower common row is even and the upper
one is odd. Also
\[
 A-w\equiv a_0+c_0=b_0\pmod D,
\qquad
 B+w\equiv b_0-c_0=a_0\pmod D.
\]
Their row-pair owner is a valid label in the same residue block.
Its odd row is above the entire patch odd-row range, and its even
row is below the entire patch even-row range, so it lies outside
the patch. Retaining that owner at any other column produces the
axis rectangle with the same presentation as the tilted rectangle.
Additional black fillers cannot distinguish their presentations.

## 5. The embedding question is still essential

This result rules out a uniform bound derived only from the local
triangular ordering, the strip condition, and a sublinear short-P
cutoff. It applies to every fixed order of the patch, so it also
applies to its triangular recursive order.

It does not prove unbounded degree for the particular full-size
scaffold. Recursive child locations restrict the available
translations and orientations, while the averaging argument uses
all translations in (2). Showing that a dense translation embeds
at a comparable ambient height is a separate problem. The result
also does not exclude adaptive block permutations or sparse
relocation as a way to resolve the remaining P edges.
