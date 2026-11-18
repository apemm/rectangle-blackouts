# Pair interactions among insertions in an affine sea

Use the notation of the [affine sea note](affine_sea_double_obstruction.md). The ordinary even representatives form a fixed interval \(J\) of \(p\) consecutive even rows, and the even sea has \(b(x)\equiv vx+c\bmod p\), with \(1+v^2\) a quadratic nonresidue. All prospective extra points are odd and have prescribed row and column residue.

**Crossed mixed supports.** For two prescribed insertions at distinct points modulo \(p\), at most \(h^{o(1)}\) signed differences between their actual columns can produce a nondegenerate mixed support whose two principal chords each run from an insertion to an even point. The bound is uniform in the labels, prime and slope. It permits the even points at arbitrary columns of the infinite sea.

Translate the first insertion to \(A=(0,a)\) and write the second as \(A'=(t,a+s)\). Both the residue of \(t\) and the integer \(s\) are prescribed. Write \(B=(u,a+V)\) and \(C-B=(d,\zeta)\) for the even endpoints of the side and diagonal respectively. Then
\[
 V\equiv vu+e,\qquad \zeta\equiv vd\pmod p,\qquad e=b(0)-a.
\]
Orient the side from \(A\) to \(B\) and the diagonal from \(A'\) to \(C\). The difference between doubled midpoints is \((t+d,s+\zeta)\). Orthogonality to the side and equality of squared lengths give
\[
 u(t+d)+V(s+\zeta)=0,\qquad
 4(ut+Vs)=(d-t)^2+(\zeta-s)^2.
\]
Both identities hold over the integers. For the second, expand equality of norms and subtract twice the first equation.

Set \(T=t+vs\) and \(K=1+v^2\) in \(\mathbb F_p\). If \(T\ne0\), the second identity expresses \(u\) as a quadratic polynomial in \(d\), with leading coefficient \(K/(4T)\). The first identity is \(u(T+Kd)+e(s+vd)=0\). Substitution gives a cubic with nonzero leading coefficient \(K^2/(4T)\), hence at most three choices for \(d\bmod p\), and each fixes \(u\bmod p\). If \(T=0\), the second identity is a quadratic in \(d\) with leading coefficient \(K\), hence has at most two roots. A root \(d=0\) would imply \(es=0\) by the first identity and \(4es=t^2+s^2=Ks^2\) by the second. This gives \(t=s=0\bmod p\), contrary to distinct residue points. Thus \(d\ne0\), and the first identity fixes \(u\) once again. Each candidate gives the two actual even rows, because \(J\) contains one row per residue.

For fixed even rows let \(W=V+\zeta-s\) be the signed vertical component of the diagonal and \(w=u+d-t\) its horizontal component. The relation
\[
 (u-w)(u+w)=W^2-V^2
\]
gives at most \(h^{o(1)}\) signed pairs \(u,w\) when its right side is nonzero. Here and below the elementary divisor bound is applied only to integers of magnitude \(O(h^2)\). Since the side is nonvertical, \(u\ne0\), and \(u(2t+w-u)=-V(s+\zeta)\) fixes the actual \(t\).

If \(W=V\), then \(\zeta=s\). Equal oriented vectors are degenerate, so \(w=-u\), and the midpoint equation gives \(u(t-u)=-Vs\). When \(s\ne0\) this again gives \(h^{o(1)}\) possible \(t\), since \(V\) is odd and nonzero. If \(s=0\), then \(t=u\) would make the midpoint difference zero. If \(W=-V\), then \(\zeta=s-2V\). Opposite oriented vectors are degenerate, so \(w=u\) and \(ut=-V(s-V)\). When its right side is nonzero the divisor bound applies. Otherwise \(t=0\), which is at most one actual column difference (and is disallowed for two distinct double columns). Exchanging the two insertions between side and diagonal changes the bound by at most a factor of two.

## Simultaneous boundary insertions

If the chosen safe insertions all lie in boundary row 1 and \(J\) is strictly above \((h+1)/2\), this is the only additional positional constraint created by combining them. An integral nonvertical chord from the boundary has no in-strip vertical alternative. A triangle with two points in row 1 and one in \(J\) either requires an axial leg or has its fourth row \(2-b<1\). A mixed support with one or three odd points cannot have even total row sum. A mixed support with its odd points on one principal chord would have a horizontal chord paired to an integral chord in the even sea, so both must be horizontal and the support is degenerate. A support with only odd points lies on the boundary line.

For \(p\asymp h\), take \(r\gg_\epsilon p^{1-\epsilon}\) individually safe labels from the affine sea note, with \(r\le p^{1-\epsilon}\) by discarding surplus labels. Their prescribed column residues are distinct. Suppose \(j\) labels have been placed. At most \(jh^{o(1)}\) actual columns for the next label are forbidden by the crossed-support estimate; two columns cannot coincide anyway, by their different residues. In its prescribed residue class the interval of width \(O(prh^{o(1)})\) offers strictly more candidates than that. Greedy placement yields a filled board in that width carrying all \(r\) distinct boundary labels together. Its extension by the same affine sea on both sides has no obstruction, including tests with remote parity owners. For \(p\asymp h\) this gives \(h^{1-\epsilon}\) labels at width \(h^{2-\epsilon+o(1)}\).

## Tilted triples with two arbitrary insertions

Assume now that the inserted points have distinct residues as points of \(\mathbb F_p^2\), and that each is off the even sea line modulo \(p\), so \(e\ne0\) for either choice of first insertion. A nonaxial right angle at the first insertion has equation \(ut+Vs=0\). Modulo \(p\), \(Tu+es=0\). If \(T=0\), then \(s=0\) and hence \(t=0\bmod p\), impossible. Otherwise \(u\bmod p\) determines the actual sea row. If \(s=0\) this angle would be axial; otherwise \(ut=-Vs\) leaves at most \(h^{o(1)}\) actual \(t\). A pivot at the other insertion is identical. At the sea pivot the equation is \(u(u-t)+V(V-s)=0\). This is quadratic in \(u\bmod p\) with leading coefficient \(K\), hence fixes at most two actual sea rows. Over the integers both \(V\) and \(V-s\) are odd and nonzero, and \(u(u-t)=-V(V-s)\) gives the same divisor bound. Thus all such tilted triples impose at most \(h^{o(1)}\) forbidden pair differences.

## Mixed supports whose principal chords each stay within a role

Assume also \(v^2\ne1\bmod p\). For two insertions at distinct residue points, at most \(h^{o(1)}\) signed column differences can give such a support. Keep the coordinates \(A,A',B,C,t,s,u,V,d,\zeta,e\) from above, now using the chords \(AA'\) and \(BC\) as the two principals. Their common squared length fixes at most two residues for \(d\), since
\[
 (1+v^2)d^2=t^2+s^2\bmod p .
\]
Each yields at most two actual \(\zeta\), since \(J\) contains \(p\) consecutive parity rows and the index difference is between \(-(p-1)\) and \(p-1\). If \(\zeta^2-s^2\ne0\), factoring \((t-d)(t+d)=\zeta^2-s^2\) proves the bound. Otherwise both chords are horizontal and degenerate when \(s=0\). For \(s\ne0\), reversing the sea chord as needed, the only nonparallel possibility has \(d=t,\ \zeta=-s\). Write \(B\) for its first endpoint in this orientation. Then the doubled midpoint shift is \((2u,2V-2s)\). Taking its dot product with either \((t,s)\) or \((t,-s)\), according to which is the side, gives
\[
 tu=\pm s(V-s).
\]
Modulo \(p\), \(s\equiv-vt\). Here \(t\ne0\bmod p\) because the insertion residue points are distinct. Substituting \(V\equiv vu+e\) gives a coefficient of \(u\) equal to \(t(1+v^2)\) or \(t(1-v^2)\), both nonzero. Thus the actual even row \(a+V\) is fixed. Since \(V-s\) is odd and nonzero, the divisor bound applies to this last equation as well.

## Combining individually safe interior insertions

Suppose \(N\) distinct labels can each individually be inserted without creating any in-strip corner triple, mixed support or vertical rival in the same infinite even affine sea. Assume all insertion residue points are distinct, each is off the sea line modulo \(p\), \(1+v^2\) is a quadratic nonresidue, and \(v^2\ne1\). Write \(D\) for the diameter of the inserted odd rows. All \(N\) labels can be inserted together in an interval of width
\[
 O\bigl(N(D+p h^{o(1)})\bigr)
\]
with clean continuation by the unchanged sea in both directions.

Indeed, per earlier label the new column cannot use \(h^{o(1)}\) actual signed differences coming from a tilted triple on two insertions or either type of two-insertion mixed support, by the preceding results. Require also that the new column be more than \(D\) from each earlier one, at a cost of \(O(1+D/p)\) candidates in its prescribed residue class. Greedy placement is then possible in the stated interval, by counting candidate columns in that class. All chords between insertions have strictly smaller vertical than horizontal magnitude. Thus two tilted legs cannot be perpendicular, and the inserted points become a chain after a 45-degree similarity, ruling out mixed supports entirely within this set. Four-point mixed supports with an odd number of insertions have odd total row sum. The individual and pair exclusions deal with all remaining cases, including all rival pairs against arbitrary parity owners.
