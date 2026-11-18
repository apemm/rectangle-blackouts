# A prime congruence for an aligned period-seven diagonal

Fix a signed odd gap \(T\). Label \(i\) has rows \(1+2i\) and \(1+2i+T\) in the height-\(h\) strip. Use each index at most once. Within a single aligned period-seven profile, keep ordinary labels of one type \(i\bmod14\). I give a choice of columns for which the two possible obstruction families inside the band are the vertical rival P and the crossed mixed support R2s. Both are pair conditions. The proof allows an arbitrary lift of each column.

## The column congruence

Take a prime \(p>128h\) with \(p\equiv11\bmod120\). The prime number theorem in the fixed progression \(11\bmod120\) permits \(p=O(h)\), by taking a prime in \((128h,256h)\) for all sufficiently large \(h\). Enlarging the implied constant covers the finite exceptions. Quadratic reciprocity gives \((5/p)=1\), \((2/p)=-1\), and \((3/p)=1\). Fix either square root \(s\) of 20 modulo \(p\). Then
\[
 Q=s^2+4\equiv24\pmod p,\qquad (24/p)=-1 .
\]
Choose local coordinates for the profile so that its period-zero slots have column \(0\bmod7\). Put label \(i\) in any column \(x_i\) satisfying
\[
 x_i\equiv si\pmod p,\qquad x_i\equiv0\pmod{6272}.
\]
The second condition uses the original H7 spacing with \(\sigma=1\). A common translation of points and background is also allowed. There is one lift per interval of length \(6272p\). Distinct indices have distinct residues \(si\bmod p\). Thus one bounded set of consecutive lifts per label uses width \(O(h)\) for this diagonal and type.

Write \(t_0=1,\ t_1=1+T\) for the two role intercepts. A chord between distinct ranks has horizontal component \(sd\bmod p\), where \(d\) is the signed rank difference. A same-role chord has vertical component \(2d\). An opposite-role chord, oriented from role 0 to role 1, has vertical component \(2d+T\). Rank differences satisfy \(|d|<h\).

## True triangles and mixed supports

A tilted right angle has two nonvertical legs. If both legs from the vertex switch roles, their vertical components are odd, and their horizontal components are even. Their dot product is odd. If both preserve the role, their dot product is \(24dd'\bmod p\), nonzero for two nonzero rank differences. If one leg preserves the role, its dot product with a switching leg is \(d(24d'\pm2T)\bmod p\). The quantity in parentheses has absolute value below \(p\). It cannot vanish since \(T\) is odd. These possibilities exclude every tilted corner triple of true points.

Consider a true mixed support with nonvertical black side \(U\) and black diagonal \(V\). Its two chords have equal squared lengths and \(V\ne\pm U\). Equality modulo four forces the two chords to both preserve or both switch roles. For role-preserving chords their squared lengths reduce to \(24d^2,24d'^2\bmod p\). Orient them so \(d=d'\bmod p\). Since \(|d-d'|<2h<p\), they have the same rank difference over the integers. For role-switching chords orient both from role 0 to role 1. Subtracting squared lengths gives
\[
 (d-d')\big(24(d+d')+4T\big)=0\bmod p .
\]
The second factor has absolute value below \(p\). It is \(4\bmod8\), hence nonzero. Again \(d=d'\). This proof also allows \(d'=0\) when \(V\) is a vertical label.

In either case the vertical components agree over the integers. Equal lengths give equal absolute horizontal components. Their horizontal components agree modulo \(p\) with the same nonzero residue \(sd\), because \(U\) is nonvertical. They must therefore agree over the integers. This gives \(V=U\), contrary to a mixed support. Also, the squared length of every same-role chord between distinct ranks reduces to the nonsquare \(24d^2\bmod p\). Thus no such chord can have the same length as a horizontal chord of the sea.

## Parked triangles

The aligned profile has three sea rows, each determined by the column modulo seven. Every true row \(y\) and sea row \(v\) satisfy \(4\nmid y-v\). Consider a tilted parked triangle with a right angle at \(A=(x_i,t_r+2i)\), a same-role end \(C=(x_j,t_r+2j)\), and a sea point \(S=(x_i+\xi,v)\). Put \(d=j-i\ne0\). Its fourth point \(W\) has coordinates \((x_j+\xi,v+2d)\). The right angle gives
\[
 (x_j-x_i)\xi=-2d(v-t_r-2i),\qquad
 s\xi\equiv 2(t_r+2i-v)\pmod p .
\]

If \(W_x=x_k\) for an occupied column, this becomes \(20(k-j)\equiv2(t_r+2i-v)\bmod p\). Both sides differ by less than \(p\) in absolute value, hence \(10(k-j)=t_r+2i-v\) over the integers. The ranks \(k,j\) are congruent modulo 14, so the left side is divisible by four. This contradicts alignment. Thus the parked triangle cannot end in a double column (FW).

Suppose two parked triangles give the same \(W\). The sea point \(S\) has column \(W_x\bmod7\), because \(x_j-x_i\) is a multiple of seven. Both triangles therefore have the same sea row \(v\) and the same \(d=(W_y-v)/2\). Their common fourth column satisfies
\[
 sW_x\equiv 24i+20d+2t_r-2v\pmod p .
\]
If their initial indices and roles are \(i,r\) and \(i',r'\), then \(24(i-i')+2(t_r-t_{r'})=0\bmod p\). Its absolute value is below \(p\), so it vanishes over the integers. Distinct roles would give \(24(i-i')=\pm2T\), impossible for odd \(T\). Equal roles force \(i=i'\), and \(d,W\) then determine \(C,S\) as well. Each such \(W\) has at most one parked triangle, including triangles with a shared black corner. This excludes 6PT.

## What the profile reduction uses

Take the infinite ordinary H7 sea and replace selected period-zero singleton columns by their indicated labels. Assume the H7 bulk, profile, and zero-label and one-label hypotheses for those substitutions. The mod-seven sieve S1 and mod-four exclusions S2 use only the row types, the alignment, and the column residues. They apply to these lifts. They leave the following tests. [Design H7, Lemmas S1, S2, S4 and the completeness proof](../2026-11-14/hilbert_sea_design_h7.md)

- A true-side vertical comparison against an oblique diagonal requires P. The owner can be anywhere in the full parity graph. The zero-label and one-label hypotheses cover any rival with at most one local label.
- An all-true tilted triple or nonvertical mixed support was excluded above. A same-role true chord cannot match a horizontal sea chord in either orientation.
- A remaining mixed support containing sea points must have one true point and one sea point in each principal chord. Its true points preserve the role and its sea points occupy the same sea row. This is R2s. S1 and S2 exclude the other two-sea patterns and every one-sea mixed pattern.
- A remaining tilted triangle with sea points must be a parked triangle of the form just proved. Its fourth point, when in the strip, is white in a singleton column with the required parity by S4. It cannot belong to another parked triangle. This also rules out a fully black tilted rectangle and competing single-white presentations from these triangles.

Each band uses its own signed diagonal and profile. The proof leaves the P and R2s tests on that band, the exceptional labels, and interactions between distinct bands and their collars. The width accounting \(O(h)\) for a band does not pay for an \(O(h^2)\) separator at every diagonal. A bounded number of lifts per label that resolves the two pair tests, together with a global joining argument, is still needed.

## A restriction on the remaining true displacement

Take any two same-role labels in the band. Write \((X,\delta)\) for their displacement. Then \(X^2\equiv5\delta^2\bmod p\). The integer \(X^2-5\delta^2\) is nonzero since \(\delta=2d\ne0\) and 5 is a nonsquare integer. Consequently
\[
 |X^2-5\delta^2|\ \ge\ p .
\]
In particular every R2s pair requires \(\max(|X|,\sqrt5|\delta|)\ge\sqrt p\). This restricts small displacements and allows larger ones.

## Excluding finitely many shapes of both pair families

Fix \(B\ge1\). In R2s write the true points as \((0,y),(X,y+\delta)\) and the sea points as \((u,v_0),(X+v,v_0)\). Put \(m=v_0-y\). The horizontal side offset \(u\) is nonzero. The integer \(\delta\ne0\), since same-role true rows are distinct. The bulk profile puts the sea row outside the interval of the two true rows, so \(\delta\ne2m\). The factorization \((u-v)(u+v)=\delta(\delta-2m)\) then gives \(u-v\ne0\). Define the reduced shape by
\[
 u-v=aL,\qquad \delta=bL,\qquad (a,b)=1,\ b>0 .
\]
The norm and midpoint equations, written as in H7 Lemma S5, give
\[
 2au+2bm=(a^2+b^2)L,\qquad
 4u(aL-X)=(a^2+b^2)L^2. \tag{1}
\]
Suppose \(|a|,b\le B\), and put \(D=a^2+b^2\). Write \(u=g r,\ L=g n\), where \(g>0,\ (r,n)=1\). The second equation in (1) implies \(r\mid Dg\), hence \(|r|\le Dg\). Since \(\delta\ne0\) and \(|\delta|<p\), both \(g\) and \(n\) are units modulo \(p\). Provided \(p>2B^2\), the integer \(D\) is also a unit. Substituting \(X\equiv(s/2)\delta\bmod p\) in (1) and cancelling \(n\) gives
\[
 4ar-D n\equiv 4(s/2)br\pmod p.
\]
Thus \(p\) divides the nonzero integer
\[
 J=(4ar-Dn)^2-5(4br)^2.
\]
Nonvanishing follows from \(br\ne0\) and the irrationality of \(\sqrt5\).

Let \(W\) bound the physical span of the true points. The sea points may be outside this interval. The first equation in (1) gives \(|u|\le2B^2 h\) since \(|L|\le h/b,\ |m|<h,\ |a|\ge1\). Hence \(r^2\le D|u|\le4B^4 h\). The second equation gives \(n^2\le4|aL-X|\le4(Bh+W)\), using \(|r|\le Dg\). Therefore
\[
 |J|\le (32a^2+80b^2)r^2+2D^2 n^2
 \le 500 B^6(h+W).
\]
Take \(p>2000 B^6h\) in the same progression, with \(p=O_B(h)\). Divide a single lift period of \(6272p\) columns into consecutive intervals of width at most \(h\). Keep the labels of each interval in a separate copy of its ordinary profile, preserving the relative positions and the congruences up to a common translation. There are \(O_B(1)\) intervals. In each copy \(W\le h\), which contradicts \(0<|J|<p\). Hence every R2s of reduced shape \(|a|,b\le B\) is absent. This exclusion also covers comparisons whose two sea points are arbitrarily far from the true interval.

A primitive Pythagorean shape has positive legs \((A,E)\) and hypotenuse \(C\), with \(A\) used horizontally. Fix a shape with \(\max(A,E)\le B\), and fix signs for the horizontal and vertical legs. For a genuine P competitor the cross chord has \(X=\pm kA,\ 2d+T=\pm kE,\ 0<kC<h\). The congruence \(X\equiv sd\bmod p\) becomes
\[
 (\pm 2A\mp sE)k\equiv -sT\pmod p
\]
with corresponding choices of signs. The coefficient is nonzero, since its vanishing would give \(A^2-5E^2=0\bmod p\), while this nonzero integer has absolute value below \(p\). Each choice of signs and shape allows at most one \(k\), hence at most one \(d\), since \(0<k<h<p\). Cases with \(d=0\) concern a single label. The union of \(O_B(1)\) nonzero forbidden differences can be colored on the ranks with \(O_B(1)\) colors by the degree bound. Splitting each interval copy once more by this coloring excludes all its P competitors of these shapes. This can restore sea points in vacated slots. The R2s argument allowed all candidate sea coordinates in the first place. The other exclusions above apply to every subset under the one-label substitution and profile hypotheses.

For fixed \(B\), the resulting list contains \(O_B(h)\) separate band copies of width \(O_B(h)\) for all ordinary signed diagonals and types. Shapes outside these cutoffs and comparisons involving more than one band still require control.


## A prime that leaves few R2s pairs at every shape

For every \(\varepsilon>0\), some prime \(128h<p<256h\), \(p\equiv11\bmod120\), leaves \(O_\varepsilon(h^{5/7+\varepsilon})\) possible R2s tuples with \(|X|\le h\), simultaneously for every signed diagonal and sea row. Here and below \(h\) is sufficiently large. This gives a power-saving bound for the number of ordinary labels to remove from all the individual bands to eliminate R2s, including shapes of unbounded size.

Put \(z=u-v\). The two mixed equations give
\[
 u(2X-z)=-m\delta,\qquad z(2u-z)=\delta(\delta-2m),
 \qquad 4u(z-X)=z^2+\delta^2 .
\]
As before \(X,z,\delta,m,2X-z\) are all nonzero. In particular, \(z=0\) would imply \(\delta=2m\), and \(2X=z\) would imply \(m\delta=0\). Since \(z^2+\delta^2>0\), also \(X\ne z\). Eliminating \(u\) gives the homogeneous cubic equation
\[
 F(X,z,\delta,m)=(z^2+\delta^2)(2X-z)-4m\delta(X-z)=0 .
\]
Its four coordinates have magnitude \(O(h)\). To check the only additional bound, suppose \(|z|>8h\). Since \(|X|\le h\), the first equation gives \(|u|\le h^2/(|z|-2h)<h/6\). Now \(|z(2u-z)|>3h^2\), contradicting the second equation. No bound on the horizontal reach of the sea points is needed.

The cubic surface \(F=0\) in projective three-space is geometrically integral. Viewed as a polynomial in \(m\), it is linear and its coefficients are relatively prime even over \(\overline{\mathbb Q}\). Neither \(\delta\) nor \(X-z\) divides \((z^2+\delta^2)(2X-z)\). I record the lines on the surface since the point count removes them.

Project from \(O=[0:0:0:1]\) to \([X:z:\delta]\). A line on the surface through \(O\) projects to a common zero of \(\delta(X-z)\) and \(N=(z^2+\delta^2)(2X-z)\). There are only five such points over the algebraic closure. On \(\delta=0\) the points are \([1:0:0]\) and \([1:2:0]\). On \(X=z\) they are \([0:0:1]\), \([\sqrt{-1}:\sqrt{-1}:1]\), and \([-\sqrt{-1}:-\sqrt{-1}:1]\). Any rational point of a line through \(O\), other than \(O\), therefore has either \(\delta=0\) or \(X=z=0\).

A line on the surface avoiding \(O\) projects isomorphically to a line. The projected line cannot be \(\delta=0\) or \(X=z\), since \(N\) does not vanish identically on either. At its intersection with each of those two lines, \(N\) must vanish. Thus the projected line joins two of the five base points, one on each component. These intersections are distinct since the components meet at \([1:1:0]\), where \(N\ne0\). There are at most six possible projected lines. Each has at most one lift avoiding \(O\), since \(F\) determines \(m\) away from the base locus. A rational projected line must pass through \([0:0:1]\) and one of the two rational base points on \(\delta=0\). It therefore satisfies \(z=0\) or \(2X=z\). A genuine R2s lies on neither. Each of the finitely many nonrational lines contains at most one rational projective point because two distinct rational points determine a rational line.

Salberger's cubic surface bound gives \(O_\eta(h^{12/7+\eta})\) rational points off the lines with projective height \(O(h)\), for every \(\eta>0\). It applies to this geometrically integral surface, including singular surfaces. The nonrational lines add \(O(1)\) rational projective points. The same power bounds the number of integer tuples of height \(O(h)\) that pass the R2s nonvanishing tests. Sum the projective estimate with height \(O(h/j)\) over the positive common divisors \(j\) and allow both signs. The series converges since \(12/7>1\). [Per Salberger, *Uniform bounds for rational points on cubic hypersurfaces*](https://research.chalmers.se/en/publication/236437)

For a possible R2s tuple the nonzero integer \(X^2-5\delta^2\) has magnitude at most \(6h^2\). It has at most one prime divisor exceeding \(128h\). The prime number theorem in the fixed progression supplies \(\gg h/\log h\) candidate primes in \((128h,256h)\). By averaging over them, one prime divides the integer for at most \(O_\varepsilon(h^{5/7+\varepsilon})\) tuples. The same prime works for every diagonal, every ordinary profile, and either choice of the root \(s\).

Split each original lift period into intervals of width at most \(h\), as above. There are a bounded number of such intervals, since \(p<256h\). Within each diagonal and type, fix the sea row and true role. The coordinate \(m\) fixes the first true row and hence its rank, and \(\delta\) fixes the second rank. Each tuple therefore gives at most one ordered rank pair. There are only three sea rows and two roles. Across \(O(h)\) signed diagonals and their bounded number of types, deleting their candidate endpoints sets aside \(O_\varepsilon(h^{12/7+\varepsilon})\) labels. The argument allowed all sea positions, including newly vacant slots. It also applies to arbitrary further splitting or to arbitrary lifts inside intervals of true span at most \(h\).

The width of the separate interval copies is \(O(h^2)\). For \(\varepsilon<2/7\) the exception count is within the power-saving regime of the archive's WP relocation bound, provided a joined main layout with compatible ends is available. True vertical rivals P on the retained labels and comparisons across distinct bands remain open. [WP assembly](../../papers/extremal/drafts/upper_bound/part8_assembly.tex)
