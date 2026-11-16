# Three-cycles in a fixed P direction palette

15 November 2026. Independent mechanical stretches give an expected
\(h^{31/16+o(1)}\) bound for all genuine central three-cycles from any
fixed finite palette of Pythagorean directions. This includes collinear
coefficient triples. The palette must be independent of height for this
bound. Separate corollaries in Sections 6--7 cover all P directions
outside a band of determinants near \(\sqrt h\). Cap-constant vertices
and arbitrary fold branches remain outside these statements.

## 1. Precise model and statement

Use the sampling and uniform affine approximation in
[the joint-P note](continuation_mechanical_p_joint_constraints.md).
For a fixed class pair, a genuine central object at raw Hilbert cell
\((i_r,j_r)\) has physical rows
\[
 a_r=\rho_0+D\alpha_0(i_r-U_0)+O(1),\qquad
 b_r=\rho_1+D\alpha_1(j_r-U_1)+O(1),                  \tag{1}
\]
with independent stretch variables of bounded density on a fixed compact
interval and independent uniform integer offsets on intervals of length
\(\Theta(h)\). The errors may depend on every parameter but are
uniformly bounded. Physical columns are a fixed constant multiple of the
raw ranks, with bounded perturbations and bounded multiplicity allowed.
Raw-coordinate provenance must remain within a fixed rank distance.
All relevant same-parity row functions obey a uniform square-root
locality bound.

Fix a finite set \(\mathcal M\) of nonzero signed rational slopes,
independent of \(h\). An oriented edge \(r\to s\) in this note has
\[
 b_s-a_r=\mu(x_s-x_r),\qquad \mu\in\mathcal M,        \tag{2}
\]
and is an actual in-strip P edge. In particular its horizontal span is
less than \(h\). Count three-cycles of distinct genuine objects
\(r_0\to r_1\to r_2\to r_0\).

If bounded copies with the same raw cell occur, assume the own-gap cutoff
\(|b_r-a_r|/\sqrt h\to\infty\) uniformly for the retained objects.
Such copies cannot be consecutive in an actual P cycle: their horizontal
gap is bounded, whereas a nonzero integral norm requires
\(X^2\ge2|Y|+1\). Otherwise the three objects have distinct raw cells
without this additional assumption.

The expected number of the stated cycles is
\[
                         h^{31/16+o(1)}.             \tag{3}
\]
Consequently their genuine endpoints have the same expected upper bound.
The result is uniform in the independent good anchors of
[the anchor-pool note](continuation_random_top_anchor_pools.md), since
inserting fixed sampled anchors changes (1) by a uniformly bounded error.

## 2. Joint probability and a short third-rank interval

The three coefficient points of the edge requirements are
\[
 (i_0,j_1),\quad(i_1,j_2),\quad(i_2,j_0).
\]
Let \(R\) be their largest sup-norm difference and \(\Delta\) their
signed difference determinant. The joint-P estimate gives
\[
 \Pr(\text{three edges})
 \le {C\over h}\min\{1,1/\max(1,R),1/|\Delta|\},     \tag{4}
\]
omitting the final term when \(\Delta=0\). This uses the shared
parameters jointly, rather than multiplying edge probabilities.

There are \(O(h^2)\) choices for \(r_0\), and \(O(h)\) for \(r_1\).
For fixed first two objects and the first two assigned slopes, locality
forces
\[
 |(b_2-a_1)-(b_1-a_0)|
   \le |b_2-b_1|+|a_1-a_0|=O(\sqrt h).
\]
Therefore
\[
 \mu_2(x_2-x_1)=\mu_1(x_1-x_0)+O(\sqrt h).           \tag{5}
\]
The possible third ranks lie in a deterministic interval of length
\(O(\sqrt h)\). Its center depends on the first two columns and
assigned slopes, but not on the sampled parameters. Bounded column and
provenance perturbations only enlarge the interval by a constant.
Its raw cells lie in a box of side
\[
                            L=O(h^{1/4})             \tag{6}
\]
by Hilbert locality. There are at most \(O(\sqrt h)\) such cells.
All three raw cells are within \(O(\sqrt h)\) of one another.

Translate the first cell to \((0,0)\), and write the other two as
\((u,v)\) and \((w,z)\). Then, up to an irrelevant overall sign,
\[
 \Delta=w(v-z)-uv,\qquad R\ge\max(|u|,|v|).           \tag{7}
\]
The second cell is distinct, so the latter maximum is nonzero. Grid
packing gives
\[
 \sum_{r_1}{1\over\max(|u|,|v|)}=O(\sqrt h).         \tag{8}
\]
The bounded-multiplicity variants have the same bound.

## 3. Small determinants

Put \(A=h^{7/16}\). For \(|\Delta|\le A\), fix its integer value
\(d\). Equation (7) becomes
\[
                       w(v-z)=uv+d.                 \tag{9}
\]
If the right side is nonzero, signed divisor enumeration gives
\(h^{o(1)}\) possibilities for \((w,z)\). All integers being factored
are \(O(h)\); the bound is uniform. Summing over \(d\) gives
\(A h^{o(1)}\) third-cell possibilities for each second cell.
Using the \(1/(hR)\) term in (4), followed by (8), bounds their expected
number by
\[
 h^2\,{A h^{o(1)}\over h}\,O(\sqrt h)
                         =h^{31/16+o(1)}.            \tag{10}
\]

When \(uv+d=0\), there is only one such \(d\) for each second cell,
and (9) is the union of the two lines \(w=0\) and \(z=v\).
Their intersection with the short third-cell box (6) has \(O(L)\)
integer points. The same weighted sum bounds this degenerate part by
\[
                 O(h^2\,L\sqrt h/h)=O(h^{7/4}).      \tag{11}
\]
Thus the zero-product case, including the relevant collinear triples,
does not require a nonzero determinant.

## 4. Large and intermediate determinants

Put \(B=h^{9/16}\). There are at most \(O(h^{7/2})\) candidate triples
by (5). For \(|\Delta|\ge B\), (4) bounds the expected count by
\[
                      O(h^{7/2}/(hB))=O(h^{31/16}).  \tag{12}
\]

It remains to consider \(A<|\Delta|<B\). Every such triple has
probability at most \(C/(hA)\). Set \(G=h^{7/16}\).

First suppose \(|w|\ge G\). For each fixed \(w\) in the short box,
the determinant band permits an interval of \(z\) of length
\(O(B/|w|)\), and hence \(O(1+B/G)\) integers. There are \(O(L)\)
choices of \(w\). The same estimate, reversing the roles of the two
coordinates, applies where \(|v-z|\ge G\). Their union has at most
\[
                 O(L(1+B/G))=O(h^{3/8})             \tag{13}
\]
third-cell possibilities per fixed first and second cell. Its expected
contribution is
\[
                O(h^2 h h^{3/8}/(hA))=O(h^{31/16}). \tag{14}
\]

In the remaining region both \(|w|<G\) and \(|v-z|<G\). Equation (7)
then implies
\[
                         |uv|\le G^2+B=O(h^{7/8}).  \tag{15}
\]
Inside a square of side \(O(\sqrt h)\), the number of integer pairs
with \(|uv|\le T\) is \(O(T\log(2h)+\sqrt h)\): sum
\(\min(O(\sqrt h),T/|u|)\) over nonzero \(u\), and count the axes
separately. Thus (15) leaves only \(O(h^{7/8}\log h)\) second cells
per first cell. Use the unrestricted \(O(\sqrt h)\) candidate ranks
for the third cell from (5). The expected count is at most
\[
 O(h^2 h^{7/8}\log h\,h^{1/2}/(hA))
                          =O(h^{31/16}\log h).       \tag{16}
\]
Equations (10)--(16) prove (3).

## 5. What this removes

This closes the small-determinant gap in the fixed-palette, genuine
central three-cycle estimate. It gives a subquadratic set of genuine
endpoints that may be charged to the existing relocation budget.
It does not establish a Hall condition, remove singleton cycles after
those doubles are relocated, or control a palette whose size or slopes
vary with \(h\). The short third-rank interval has constants depending
on the fixed nonzero slopes. Constant anchors and arbitrary cap or fold
forms require their own joint estimates and cannot be included merely by
calling them a finite union.

## 6. All directions when the determinant is large

For any fixed \(\varepsilon>0\), the expected number of genuine central
three-cycles, with arbitrary Pythagorean directions, satisfying
\[
                    |\Delta|\ge h^{1/2+\varepsilon}  \tag{17}
\]
is \(h^{2-\varepsilon+o(1)}\). The finite-palette restriction is not
needed for this corollary.

Choose \(r_0\) and \(r_1\) in \(O(h^2)\) and \(O(h)\) ways.
The first horizontal gap \(X_1\) is then fixed. Factorization of
\(X_1^2=L_1^2-Y_1^2\) leaves only \(h^{o(1)}\) signed integral
P heights \(Y_1\) in the strip. Every actual second edge satisfies
\[
                       |Y_2-Y_1|=O(\sqrt h)           \tag{18}
\]
by the same-parity locality calculation preceding (5). This inequality
holds with the signed heights; there is no need to assume they have the
same sign. Thus only \(O(\sqrt h)\) integer values of \(Y_2\) remain.
They are nonzero and odd in the parity-pair construction. For each,
\[
                       (L_2-X_2)(L_2+X_2)=Y_2^2
\]
gives only \(h^{o(1)}\) possibilities for the signed horizontal gap
\(X_2\), and hence for the third column and object. The closing
horizontal gap is now fixed; it has only \(h^{o(1)}\) possible signed
heights \(Y_3\). These factor bounds may count extraneous
out-of-strip choices, which only enlarges the candidate set.

Consequently there are \(h^{7/2+o(1)}\) rank-and-height candidates.
For each, the joint estimate (4) applies to its three specified heights,
uniformly in the direction choices. Equation (17) supplies probability
\(O(h^{-3/2-\varepsilon})\), proving the corollary.

The candidate third ranks in this proof need not form a short interval.
They are a dispersed set arising from many different factorizations of
the nearby heights in (18). Hence the side-\(O(h^{1/4})\) third-cell box
used in Sections 3--4 is not available. The corollary does not extend
the \(h^{31/16+o(1)}\) full-determinant bound to all directions.

## 7. All directions when the determinant is small

For \(1\le A\le h\), with arbitrary Pythagorean directions, the
expected number of genuine central three-cycles satisfying
\(|\Delta|\le A\) is at most
\[
            h^{3/2+o(1)}(A+\sqrt A+\log(2h)).         \tag{19}
\]
In particular, for each fixed \(0<\varepsilon<1/2\), the range
\(|\Delta|\le h^{1/2-\varepsilon}\) contributes only
\(h^{2-\varepsilon+o(1)}\). Exact collinearity contributes
\(h^{3/2+o(1)}\).

All three raw cells lie in a box of side \(N=O(\sqrt h)\), because
the first two actual edges each have horizontal span less than \(h\).
For each fixed rank triple, the three fixed horizontal gaps have only
\(h^{o(1)}\) possible triples of signed norm heights. Thus their
joint probability is at most
\[
                    {h^{o(1)}\over h\max(1,R)}.      \tag{20}
\]
This enumeration is done separately for each rank triple; it does not
assume independent heights.

For the nonzero right sides in (9), exactly the argument of (10) now
gives \(h^{3/2+o(1)}A\), without needing the short third-rank interval.
For the zero right side, there is again just one possible determinant
\(d=-uv\), and it can be counted only if \(|uv|\le A\).
The two third-cell lines now have \(O(N)\), rather than \(O(L)\),
possible grid points. The necessary improvement comes from the weighted
second-cell count
\[
 \sum_{\substack{0<\max(|u|,|v|)\le N\\ |uv|\le A}}
       {1\over\max(|u|,|v|)}
          =O(\sqrt A+\log(2N)).                    \tag{21}
\]
To prove (21), split into dyadic annuli
\(R<\max(|u|,|v|)\le2R\). Their number of points is
\(O(\min(R^2,A+R))\): for example, if \(|u|\asymp R\),
then \(|v|\le A/|u|\), including the zero value of \(v\).
After division by \(R\), the annuli below \(\sqrt A\) sum to
\(O(\sqrt A)\). The higher annuli contribute
\(O(A/R+1)\) each, summing to \(O(\sqrt A+\log(2N))\).

Multiplying (21) by \(O(h^2)\) first cells, \(O(\sqrt h)\)
third cells on the two lines, and the \(h^{-1+o(1)}\) factor in (20)
gives the remaining terms of (19). For exact \(\Delta=0\), the
nonzero-factor contribution has just one determinant value, and (21)
with the restriction \(uv=0\) is \(O(\log(2N))\), giving the stated
collinear bound.

Combining Sections 6 and 7 shows that, for all actual directions, only
\[
           h^{1/2-\varepsilon}<|\Delta|<h^{1/2+\varepsilon}
\]
remains outside these power-saving estimates. This is a reduction of the
three-cycle incidence problem, not a bound on that critical band or on
longer directed cycles.

## Review status

The preceding joint probability lemma and short-interval step were
independently reviewed earlier. A second reader then checked the full
determinant summation in Sections 3--4, including both product-zero lines
and both intermediate-gradient cases. The all-direction corollary in
Section 6 was independently derived in parallel and its saved proof
passed that reader's review. The Section 7 weighted annular argument,
divisor count, and exact-collinearity specialization also passed a
separate written check. The critical-band and branch restrictions remain
part of the conclusions.
