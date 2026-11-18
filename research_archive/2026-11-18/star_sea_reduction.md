# The aligned period-seven sea on dyadically ordered stars

In an aligned profile of [design H7](../2026-11-14/hilbert_sea_design_h7.md), take the [star placement](star_placement.md) for the labels of that profile and multiply its columns by 49. Keep full star indices when some labels are absent. The resulting columns meet the mod-7 and mod-4 placement conditions of the local sieve. Fill other columns with the profile's ordinary sea. The grid has a fixed number of these profiles. Here are the geometric conclusions inside one profile, conditional only on its stated row, parity, and margin conditions. The width estimate of the star placement is multiplied by 49.

Write \((X,\delta)\) for a chord between points of the same role. For an odd-role chord (two centers), either \(\delta=0\) or \(|X|>16h|\delta|\). For an even-role chord with \(\delta\ne0\),
\[
 v_2(X)=v_2(\delta)+2 .
\]
When its row is repeated, \(A\mid X\), where the star spacing \(A\) is a power of two greater than \(32h\). Multiplication by 49 preserves these inequalities. Every label point \(y\) and sea row \(s\) satisfy \(v_2(s-y)\le1\), with \(s\ne y\).

## No parked triangles from the labels

A parked triangle of type PT has an angle at a true point with one leg \((X,\delta)\) to a true point of the same role and one leg \((\xi,m)\) to a sea point, where \(m=s-y\). A tilted angle would require \(X\xi=-\delta m\), with both horizontal components nonzero. If the true points are odd, the spacing makes the left side larger in absolute value than the right. For even points the left side has valuation at least \(v_2(\delta)+2\), while the right side has valuation at most \(v_2(\delta)+1\). The case \(\delta=0\) gives only axial angles. Thus there are no PTs. In particular both FW (a PT ending in a double column) and 6PT (two PTs sharing a white corner) disappear at every height covered by the profile assumptions.

All three-true tilted corners also disappear by the star proof. The row and column congruences needed for the mod-7 sieve and the mod-4 exclusions of other triangle patterns survive the factor 49. Thus the one-label theorem and the sieve from H7 exclude every tilted triangle in the profile, including those involving singleton points. This statement concerns cores with the profile's ordinary labels and background.

## A 2-adic exclusion for all-even mixed supports

Suppose four distinct true points of the even role formed a mixed support. Let \(U=B-A,V=D-C,H=C+D-A-B,J=U-V\). The equations are \(H\cdot U=J\cdot(U+V)=0\) and \(|U|^2=|V|^2\), with \(H\ne0\). The even role has at most one point per physical column. If \(U_y=0\), the horizontal chord \(U\) is divisible by \(A\). Any nonhorizontal even-role chord with row difference \(\delta\) has squared norm of valuation \(2v_2(\delta)<2v_2(A)\). Thus \(V_y=0\) as well, giving the excluded case \(V=\pm U\). Exchange the norm argument if \(V_y=0\).

Otherwise \(v_2(U_y)=v_2(V_y)=q\) by equality of norms. Reverse \(V\), interchanging \(C,D\), so \(v_2(U_y+V_y)=q+1\). Since both horizontal components are divisible by \(2^{q+2}\), perpendicularity gives
\[
 v_2(H_y)\ge v_2(H_x)+2,\qquad
 v_2(J_y)\ge v_2(J_x)+1 ,
\]
with \(v_2(0)=\infty\). Here \(H_x,H_y\ne0\), since \(U_x,U_y\ne0\) and \(H\ne0\). Put \(j=\min(v_2(H_x),v_2(J_x))\). At least one of \(H_x+J_x,H_x-J_x\) has valuation at most \(j+1\), since their half-sum and half-difference are \(H_x,J_x\). Both corresponding vertical sums are divisible by \(2^{j+1}\). The vectors \((H+J)/2=C-A\) and \((H-J)/2=D-B\) are even-role chords. One of them has horizontal valuation at most \(j\) and vertical valuation at least \(j\). If its vertical component is nonzero this contradicts the chord condition. If it is zero it contradicts \(A\mid X\), because \(j\le v_2(H_y)-2< v_2(A)\) and \(|H_y|\le2(h-1)\). This proves the exclusion for every dyadic permutation. The odd-role points are a chain in the ordinary coordinate order and have no mixed support by the paper's chain lemma.

Two true even points used as the black side against a diagonal of two true odd points are also impossible for a nonhorizontal side. Profile alignment makes \(H_y\) twice an odd integer, contradicting the first valuation inequality. A horizontal side of that role cannot face a nonhorizontal odd-role diagonal, whose length lies strictly between consecutive integers by the spacing bound. A horizontal odd-role diagonal would have the same unoriented vector as the side. Also, any nonhorizontal odd-role black side in a mixed support would satisfy \(|H_x|=|\delta H_y/X|<1\). This gives \(H_x=H_y=0\), which is degenerate.

## Mixed supports with two true points and two sea points

For the H7 case R2s put the same-role true points at \((0,y),(X,y+\delta)\), and the sea points at \((u,s),(X+v,s)\). Write \(m=s-y\), \(P=u-v\) and \(t=2X-P\). The equations are
\[
 ut=-m\delta,\qquad P(u+v)=\delta(\delta-2m),\qquad
 4u(P-X)=P^2+\delta^2.
\]
The last follows by substituting the first into the second. The points of each black pair occupy different physical columns so \(u\ne0\). The sea level lies outside the interval of the two true rows by the profile margins. Hence \(\delta=2m\) is impossible. For \(\delta\ne0\),
\[
 |t|\le h|\delta|,\qquad |P|\le3h|\delta|,\qquad |X|\le2h|\delta|.
\]
For \(\delta=0\) the midpoint condition gives zero perpendicular shift since \(u\ne0\). These observations exclude every odd-role R2s.

For an even-role R2s, let \(\ell=v_2(m)\le1,\ q=v_2(\delta)\). If \(q\ge\ell+3\), the necessary conditions are
\[
 2v_2(P)=q+\ell+2,\qquad 2v_2(u)=q+\ell-2.
\]
Indeed \(v_2(2X)\ge q+3>q+\ell\), so the first equation for \(ut\) forces \(v_2(t)=v_2(P)\le q+\ell\). Also \(v_2(P-X)=v_2(P)\). The left side of the third equation has valuation \(q+\ell+2<2q\). Its right side therefore forces \(v_2(P)<q\) and has valuation \(2v_2(P)\). In particular \(q\equiv\ell\bmod2\).

One extra case must be retained when transferring the H7 argument from Hilbert geometry. A same-role true chord and a horizontal sea pair could have equal length. For a nonhorizontal odd-role chord the spacing gives \(0<\delta^2<2|X|+1\), ruling out integral length. For an even-role chord used as the **side**, its row difference is divisible by four and \(H_y=2(s-y)-\delta\). When the two even rows agree modulo eight, \(v_2(H_y)\le2\). Perpendicularity requires \(v_2(H_x)=v_2(H_y)-2\le0\). But both sea endpoints have the same column parity since their horizontal distance has valuation \(v_2(\delta)\ge3\). The two true columns are even, so \(H_x\) is even, a contradiction. Enforce even-row alignment modulo eight by further splitting each profile into two copies if using this exclusion. For the **diagonal** role a nonhorizontal even chord of integral length remains a possible obstruction. Its endpoints have equal rows modulo seven, both columns are multiples of seven, and hence its length is divisible by seven. The prospective horizontal black side has both columns zero modulo seven, where the profile uses \(F\) whenever the column holds an ordinary singleton.

The period-seven sieve and the argument above reduce the open cases to vertical-rival pairs between labels, mixed supports with both true roles, even-role R2s, and the horizontal-sea-side comparison just described. These conditions include four-point tests. The color certificates in the star placement use the columns before the factor 49. Multiplying only the horizontal coordinate changes square norms, so those certificates give no vertical-rival guarantee for this filled placement. The ordinary-row and one-label hypotheses of H7 are also needed when applying its sieve.
