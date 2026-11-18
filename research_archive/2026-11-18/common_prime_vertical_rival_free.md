# A common prime modulus on a quadratic placement without vertical rivals

Fix \(0<\delta<1/2\) and a horizontal stride \(S=8K\) with \(K\) fixed. At all sufficiently large heights, one can place every parity double in \(O_{\delta,K}(h^2)\) columns, exclude all true vertical rivals, and enforce a single congruence
\[
 x_i\equiv Si\pmod p,\qquad h^{1-\delta}\le p\le 2h^{1-\delta},
\]
throughout all the diagonal bands. Here \(i\) is the index of the odd row \(2i+1\). One can also fill every remaining column at a boundary row while preserving vertical-rival exclusion. The useful change from the [near-affine construction](near_affine_p_free_shear.md) is the freedom to multiply its bounded modular shift by a large prime. This makes perpendicularities between labels constrain actual rank differences.

Inside one band of signed odd offset \(T\), a **role-preserving** chord joins two odd rows or two even rows. Its row difference is \(2d\) for signed rank difference \(d\). A **role-switching** chord oriented from odd to even has row difference \(2d+T\). The following reductions concern all-true tilted triangles and mixed supports within a band.

- Every triangle with two role-preserving legs has all three ranks equal modulo \(p\).
- After a bounded refinement, for \(p\nmid T\) every remaining tilted triangle has a role-preserving leg with both coordinates divisible by \(p\). The two coordinates after division are \(O_K(h^\delta)\).
- In every genuine mixed support whose side and diagonal both preserve roles, both principal chords have both coordinates divisible by \(p\). When both switch roles and \(p\nmid T\), one may orient them so that their difference is a nonzero vector divisible by \(p\), with coordinates \(O_K(h^\delta)\) after division.

This gives the prime reduction and vertical-rival exclusion in the same placement. Same-fiber cases, supports involving the singleton sea, and inter-band comparisons still require separate arguments.

## Choosing columns

Choose any prime \(p\) in the indicated interval. Let \(t=|T|\), and take the squarefree divisor \(q\le h^\delta\) from the residual-divisor estimate in the [near-affine proof](near_affine_p_free_shear.md). Thus the primes of \(q\) are coprime to \(2Kp\), and every fixed moment of \(\tau(t/q)\) is bounded on average. For every prime \(\ell\mid q\) choose a nonzero \(\sigma_\ell\bmod\ell\) for which \(\sigma_\ell^2+4\) is a nonsquare and \(S\sigma_\ell+4\ne0\bmod\ell\). Such a nonsquare exists by the elementary quadratic character sum, and the two signs cannot both violate the second condition. Choose \(r\bmod q\) with \(S(1+pr)\equiv\sigma_\ell\bmod\ell\) for every such \(\ell\). Set
\[
 F_i=[ri]_q,\qquad x_i=S(i+pF_i).
\]
Take \(F_i=0\) for \(q=1\). The range of \(x_i\) has length \(O_K(h+p q)=O_K(h)\).

These are distinct columns. If two coincide, write \(d=i-j=pD\) and \(a=F_i-F_j=-D\). Since \(a\equiv rpD\bmod q\), the unit \(1+pr\bmod q\) forces \(q\mid D\), hence \(F_i=F_j\) and \(D=0\).

If a chord from odd to even at distinct ranks has integral length, then \(q\mid d\). Indeed, at any prime of \(q\) not dividing \(d\) its squared length is \((\sigma_\ell^2+4)d^2\bmod\ell\), a nonzero nonsquare. For \(d=qn\) the shift cancels, so the actual horizontal component is \(S qn\). After dividing by \(q\), the square test is precisely \((Sn)^2+(2n\pm t/q)^2=z^2\). Use the Pell-orbit and dyadic-distance coloring of the near-affine proof on these quotient differences. The mean number of colors is bounded by its residual-divisor estimate. Each color gets its own translated band, separated from other bands by more than \(h\) columns. Translations by multiples of \(Sp\) cost only \(O_K(h)\) per band and preserve the common congruence. This proves the claimed width and exclusion. A boundary-row singleton cannot be the endpoint of an in-strip oblique rival to a vertical parity pair: the vertical alternative would extend past the boundary. The other geometric restrictions on such fillers remain open.

## Role-preserving perpendicular legs

Write \(Q=S^2+4\). For a rank step \(d\) let \(a\) be the corresponding signed change in \(F_i\). Then \(|a|<q\), \(a\equiv rd\bmod q\), and a role-preserving leg has displacement \((S(d+pa),2d)\). Suppose two such tilted legs of steps \(d,d'\) are perpendicular. Modulo \(p\) their dot product gives \(Qdd'=0\). For large \(h\), \(p\nmid Q\). If \(p\nmid d'\), write \(d=pD\), divide the dot product by \(p\), and reduce again:
\[
 (QD+S^2a)d'=0\bmod p .
\]
The first factor has magnitude \(O_K(h^\delta)<p\). Thus \(QD+S^2a=0\) as an integer. Modulo \(\ell\mid q\) this says \((4+S\sigma_\ell)D=0\), so \(q\mid D\). Since \(q\mid d\), we have \(a=0\), forcing \(D=0\). This would be a zero leg. Both nonzero rank steps are therefore divisible by \(p\). Their coordinates are divisible by \(p\) as well.

Two role-switching legs from one pivot cannot be perpendicular because both vertical factors are odd and both horizontal factors are even. For one preserving leg and one switching leg the dot product modulo \(p\) is \(d(Qd'\pm 2T)\). When \(p\nmid T\), a bounded rank palette rules out \(d'\equiv\pm2T/Q\bmod p\). In detail put \(c=2T/Q\bmod p\), multiply residues by a unit sending \(c\) to \(\lfloor p/3\rfloor\), and split the resulting representatives into 24 consecutive intervals of nearly equal lengths. A difference of ranks in one interval cannot equal \(\pm c\) after undoing the dilation. Also a sum of two such differences cannot equal \(\pm2c\), a fact used below. Thus the preserving leg has rank difference divisible by \(p\). Each band has horizontal and vertical diameter \(O_K(h)\), so dividing this leg by \(p\) gives the stated bound. The diagonals with \(p\mid T\) contain \(O(h^2/p)=O(h^{1+\delta})\) labels altogether.

## Mixed comparisons

A genuine nonvertical mixed comparison requires equal-length vectors \(U,V\) with \(V\ne\pm U\). Modulo four, their squared lengths force both chords to preserve roles or both to switch. In the first case norm equality modulo \(p\) gives \(d'\equiv\pm d\bmod p\). Orient the chords so that \(d'-d=pD\). Let \(a\) be the difference between the two signed \(F\)-increments. Then \(a\equiv rpD\bmod q\), \(|a|<2q\), and
\[
 V-U=p\bigl(S(D+a),2D\bigr).
\]
If \(p\nmid d+d'\), take the dot product of \((V-U)/p\) and \(V+U\), which is zero, and reduce modulo \(p\). As above \(QD+S^2a=0\) over the integers and \(q\mid D\). The equal rank differences modulo \(q\) mean their two signed \(F\)-increments are congruent modulo \(q\). Hence \(a\in\{0,q,-q\}\). Writing \(D=qD_1\), the relation \(QD_1=-S^2a/q\) forces \(D_1=a=0\), since \(S^2<Q\). This would give \(V=U\). Thus \(d+d'\equiv d'-d\equiv0\bmod p\), so both chords have both components divisible by \(p\).

If both chords switch, orient them from odd to even. Norm equality now becomes \((d'-d)(Q(d+d')+4T)=0\bmod p\). For \(p\nmid T\) the 24-color refinement excludes the second factor. The formula for \((V-U)/p\) applies again, and its coordinates are \(O_K(h^\delta)\). In this case perpendicularity gives the residual equation
\[
 (QD+S^2a)d+2TD=0\bmod p .
\]
A switching leg perpendicular to a \(p\)-divisible preserving leg gives the same equation up to the orientation of \(T\). A uniform solution of these residual conditions and the single-fiber conditions would advance this construction. The prime in this placement and its horizontal coefficient differ from those used in the [crossed mixed support estimate](auxiliary_prime_h7_diagonal.md); that estimate cannot be transferred without an additional argument.

