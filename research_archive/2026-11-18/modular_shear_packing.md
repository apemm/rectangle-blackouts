# A bounded palette for true vertical rivals after a modular shear

On a fixed signed odd offset \(T\), a label at index \(i\) has rows \(2i+1\) and \(2i+1+T\), both in \([1,h]\). Write \(t=|T|\). There is a placement of this entire diagonal in \(O(h)\) columns whose true labels have no in-strip vertical rivals, with an absolute implied constant. This construction changes the horizontal order of the diagonal.

For every odd prime \(p\mid t\) choose \(r_p\ne0\bmod p\) with \(64r_p^2+4\) a quadratic nonresidue. The identity \(\sum_{x\bmod p}(\frac{1+x^2}{p})=-1\) gives such a residue, since \(x=0\) contributes \(+1\) and \(x=4r_p\) is an invertible change of variables. One proof counts \((v-x)(v+x)=1\), which has \(p-1\) solutions, to evaluate the sum. By the Chinese remainder theorem take \(r\) coprime to \(t\) with these residues. For \(0\le i\le(h-1)/2\) put
\[
 j_i=t\lfloor i/t\rfloor+[ri]_t,\qquad x_i=8j_i ,
\]
where \([a]_t\in[0,t-1]\). For \(t=1\) take \(j_i=i\). These indices are distinct and \(0\le j_i\le h/2+t\) since the map permutes each period of length \(t\).

For a cross chord between two labels, put \(d=i-i'\ne0\). Its horizontal difference is \(X=8(j_i-j_{i'})\) and its vertical difference is \(Y=2d\pm T\). Suppose \(p^\nu\Vert t\) and \(w=v_p(d)<\nu\). Reducing after division by \(p^{2w}\) gives
\[
 (X^2+Y^2)/p^{2w}\equiv(64r^2+4)(d/p^w)^2\pmod p.
\]
The residue is a nonzero nonsquare, so the norm cannot be integral. This argument at every prime gives \(t\mid d\) for any surviving integral-norm cross chord. If \(d=\ell t\), the two indices have the same residue and \(j_i-j_{i'}=\ell t\). The remaining positive blocked distances in the quotient are therefore contained in the single set
\[
 {\cal D}=\bigl\{\ell\ge1:64\ell^2+(2\ell+1)^2
 \ \text{or}\ 64\ell^2+(2\ell-1)^2 \text{ is a square}\bigr\}.
\]
This set does not depend on the height or the offset. We have allowed all integral hypotenuses here, regardless of strip boundaries.

## Three colors for the quotient

For each \(\ell\in\mathcal D\) there is an odd positive \(z\) and a sign such that
\[
 (34\ell\pm1)^2=17z^2-16 .
\]
With \(x=34\ell\pm1\ge33\),
\[
 \left|\sqrt{17}\,\ell-z/2\right|
 \le\frac{\sqrt{17}}{34}
       +\frac{16\sqrt{17}}{34(x+\sqrt{17}z)}
 \le\frac{\sqrt{17}}{34}\left(1+\frac{16}{66}\right)<\frac16 .
\]
Since \(z/2\) is a half-integer, \(\|\sqrt{17}\,\ell\|>1/3\). The coloring \(c(q)=\lfloor3\{\sqrt{17}\,q\}\rfloor\) of the integers excludes every difference in \(\mathcal D\): two points in the same third of the circle have circular distance strictly below \(1/3\). This palette is optimal for the unrestricted quotient distance graph. The distances \(3,5,200\) belong to \(\mathcal D\), with respective hypotenuses \(25,41,1649\) for a choice of sign in each case. The path from zero using 65 steps of \(+3\) and one step of \(+5\) ends at 200; the edge of length 200 closes an odd cycle on 67 distinct vertices.

Color label \(i\) by \(c(\lfloor i/t\rfloor)\). Place each of the three colors in a copy of its \(8j_i\) coordinate interval, with copies at horizontal distance greater than \(h\). Two labels in different copies cannot form an in-strip rival. In the same copy a candidate must have \(d=\ell t\), so the quotient colors already exclude it. Each diagonal uses \(O(h)\) columns including the separations. Taking all diagonals in separate intervals with the same separation packs all parity edges in \(O(h^2)\) columns free of true-to-true vertical rivals.

## True mixed supports in one prime period

There is a separate geometric consequence when an odd prime \(p\mid t\) and all indices used in one band are distinct modulo \(p\). Every true point of this band reduces modulo \(p\) to one point of an affine line parameterized by \(i\bmod p\). The direction has nonzero squared norm \(64r^2+4\bmod p\), up to the harmless choice of using \(i\) as parameter. Thus a tilted true right angle at ranks \(i,j,k\) with both other ranks distinct from the pivot is impossible modulo \(p\). If one of the two legs has both endpoints in one rank, it is vertical and cannot be a tilted leg.

For a true mixed support with nonvertical black side and with all indices in the band distinct modulo \(p\), write \(U,V\) for the black side and diagonal and \(H\) for the difference between the sums of their endpoints. The horizontal span of \(U\) is nonzero, so its endpoint ranks are different. The relation \(H\cdot U=0\bmod p\) forces the sums of the rank pairs to agree modulo \(p\), since every vector is parallel to the same line direction modulo \(p\). Equality of the squared norms forces the rank differences to agree up to sign. As \(p\) is odd, the unordered rank pairs coincide, hence both principal chords use the same two label columns. Their true points consist of the two offset pairs at these columns. If both chords are same-role they have the same unoriented displacement. If both are cross-role their vertical differences have magnitudes \(|2d+T|\), \(|2d-T|\), which are unequal since \(dT\ne0\). These exhaust the four distinct points distributed over two columns. This proves the mixed exclusion in such a band. The hypothesis holds for any interval of \(p\) consecutive indices, with arbitrary omissions.

For general composite offsets or bands longer than an available prime divisor these last exclusions do not follow. In particular the complete \(O(h^2)\) sum is a construction for the true vertical-rival condition. Its tilted and nonvertical mixed supports, singleton choices, and inter-band interactions for the other obstruction families are open.

## A filled board with no vertical rivals

Place a singleton in row \(1\) in every unused column, including all guards. More generally either boundary row may be used independently in those columns. An in-strip rival pair cannot contain a point in row \(1\) or row \(h\): if its two rows are \(a<b\), the vertical alternative extends to \(a-j,b+j\) for an integer \(j\ge1\). Thus adding these singletons preserves the full vertical-rival exclusion. The resulting board has all \(q_h\) distinct parity doubles, exactly one black cell in every other column, and no vertical rival, irrespective of its span. The three copies per diagonal have individual width at most \(12h+1\), there are at most \(h\) signed odd offsets, and guards of \(h\) singleton columns suffice. In particular width at most \(40h^2\) suffices, for \(h\ge3\), for these conditions alone.


## A large prime divisor isolates geometric supports by residue

Fix a band whose true points have horizontal span \(W\) and vertical span at most \(h\). Suppose an odd prime \(p\mid t\) satisfies \(p^3>CWh\) for a sufficiently large absolute \(C\). We can choose \(r_p\) so that every tilted true corner triple and every true mixed support with nonvertical side has all its rank indices in a single residue class modulo \(p\).

In the plane modulo \(p\), all differences between true points lie on \(X=4r_pY\). Their horizontal-coordinate representatives need only have the prescribed residue modulo \(p\). For each primitive integer direction \((a,b)\) with \(ab\ne0,\ |a|\le2W/p,\ |b|\le2h/p\), forbid the choices of \(r_p\) for which this direction or its perpendicular lies on the modular line. There are at most two such choices per pair: a primitive vector cannot vanish modulo \(p\). There are \(O(Wh/p^2)\) pairs. The original nonresidue condition leaves \((p+1-\#\{x:x^2=-1\bmod p\})/2\) elements. The remaining set is nonempty by the hypothesis.

Let \(U=m(a,b)\) and \(V=n(-b,a)\) be two nonzero tilted perpendicular vectors on this modular line, both in the box \([-2W,2W]\times[-2h,2h]\), with \((a,b)=1\). Since the line is nonisotropic, at least one of \(U,V\) is zero modulo \(p\); its multiplier is divisible by \(p\). Its corresponding primitive direction meets the size bounds above. The other direction cannot lie on the modular line, by the extra deletions, so the other multiplier is divisible by \(p\) as well. For a corner triple apply this result to its two legs. For a mixed support apply it to its nonvertical true side \(U\) and its nonzero perpendicular \(H=C+D-A-B\). The side is tilted since no two distinct labels repeat a row on this diagonal. Thus \(U=H=0\bmod p\). The equal squared norm of the diagonal on the nonisotropic line forces its difference to vanish modulo \(p\) as well. The endpoint sums then put all four in one residue class; \(2\) is invertible modulo \(p\).

Inside each resulting fiber write \(i=a+p i'\) and \(x=x_0+8[r_p a]_p+8p F_a(i')\). The argument between fibers allows an arbitrary choice of every integer-valued \(F_a\) respecting the common physical span. Translating and rescaling a fiber by \(p\) gives even and odd row sequences differing by \(T/p\) in a strip of height \(O(1+h/p)\). This is a reduction for large prime divisors. It does not apply uniformly to all offsets.

## Locality inside a single shear band

For the unmodified modular lift \(j_i=t\lfloor i/t\rfloor+[ri]_t\), choose the residues so that \(\gcd(16r+1,t)=1\). The two signs of every admissible nonzero \(r_p\) have the same nonsquare property. At least one sign avoids \(16r_p+1=0\bmod p\). Constant horizontal translations and passing to one color band do not affect the following bound.

In displacement coordinates put \(\ell(X,Y)=4X+Y,\ z(X,Y)=X-4Y\). The range of \(z\) on all true points is at most \(B=20t\), since \(j_i-i\) has range \(<2t\), and switching roles adds \(4t\) to the possible spread. For a chord or for \(H=C+D-A-B\), one has \(X=4rY\bmod t\) and \(8\mid X\). If \(\ell=0\), the choice of \(r\) implies \(t\mid Y\). Also \(32\mid Y\) since \(Y=-4X\). With \(t\) odd, a nonzero such vector would have \(|z|=17|Y|/4\ge136t\), impossible for a chord (\(|z|\le B\)) or \(H\) (\(|z|\le2B\)). Thus \(\ell\) is a nonzero integer on every nonzero vector of these types.

For perpendicular vectors \(U,V\) one has \(\ell(U)\ell(V)=-z(U)z(V)\). For a true corner triple the integral nonvanishing bounds both \(\ell\)'s by \(B^2\). In a true mixed support apply the same identity to the nonzero vectors \(U,H\), bounding both by \(2B^2\). The actual diagonal has the same length as \(U\), and its midpoint differs from that of the side by \(H/2\). Since \(X=(4\ell+z)/17,\ Y=(\ell-4z)/17\), all four points have horizontal span \(O(t^2)\). The bound applies within one band for every height.
