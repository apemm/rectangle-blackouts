# Four-column spacing removes horizontal sea comparisons from matching bands

Use the [dyadic matchings](dyadic_matching_blocks.md), with true columns \(x_i=A c_i+4\sigma(i)\), \(A\) a power of two divisible by \(4N\) and exceeding \(32h\). One may multiply all these physical columns by a fixed odd integer \(p>0\). Each true row occurs at most once in the matching. A true chord with displacement \((X,Y)\) connecting different even rows or different odd rows satisfies
\[
 v_2(X)=v_2(Y)+1 .
\]
In fact \(Y=2(i-j)\) up to the isometry of the even row indices, while \(v_2(X)=2+v_2(i-j)\). A true chord connecting opposite roles has odd \(Y\), with \(4\mid X\). In particular every nonvertical chord satisfies \(v_2(X)>v_2(Y)\).

## True triangles and mixed supports

The strict inequality excludes perpendicular tilted chords, as the horizontal and vertical products have different valuations. Let \(U=B-A_0\) be a nonvertical black side, \(V=D-C\) the black diagonal of a purported mixed support, \(H=C+D-A_0-B\) and \(J=U-V\). The mixed equations give \(|U|=|V|\), \(H\cdot U=0\), \(J\cdot(U+V)=0\), \(H\ne0\). Write \(q=v_2(U_y)=v_2(V_y)\), as follows from the equality of norms. Reverse \(V\) so \(v_2(U_y+V_y)=q+1\). If \(q=0\), both horizontal components are divisible by four. If \(q\ge1\), both have valuation \(q+1\) because these are same-role chords. In both cases \(v_2(U_x+V_x)\ge q+2\). Perpendicularity gives
\[
 v_2(H_y)\ge v_2(H_x)+1,\qquad v_2(J_y)\ge v_2(J_x)+1 .
\]
Here \(H_x,H_y\ne0\). If a component of \(J\) vanishes, the second inequality is still valid with infinite valuations, from its equation with \(U+V\). Put \(j=\min(v_2(H_x),v_2(J_x))\). At least one of \(H_x\pm J_x\) has valuation at most \(j+1\), and both \(H_y\pm J_y\) are divisible by \(2^{j+1}\). The corresponding chord \((H+J)/2=C-A_0\) or \((H-J)/2=D-B\) has a nonzero horizontal component and violates the strict inequality. This excludes every all-true mixed support with nonvertical black side. The remaining all-true test is the opposite-role P graph, now with squared horizontal term \(16p^2(\sigma(i)-\sigma(j))^2\) within each band.

For a same-role chord, normalize its squared length by \(2^{2v_2(Y)}\). Its residue is \(1+4=5\bmod 8\), so its length is irrational. Consequently no such black chord and no horizontal sea chord can have equal lengths, in either order. This step also works across colors \(c_i\) within the same matching.

## Parked triangles in the aligned sea

Use the aligned profiles of [design H7](../2026-11-14/hilbert_sea_design_h7.md) and keep their stated row and margin assumptions. In particular the sea rows lie outside the range of true rows, and any label row \(y\) and sea row \(s\) have \(v_2(s-y)\le1\). Choosing \(49\mid p\) preserves the column congruences. Profile restrictions on row indices retain the original ranks of present labels.

A parked triangle has initial true point \(A=(x_A,y)\), another true point \(C=A+(X,\delta)\) of the same role, and a sea point \(S=A+(\xi,s-y)\), with \(X\xi=-(s-y)\delta\). Its fourth point is \(W=(x_C+\xi,s+\delta)\). Here \(v_2(X)=v_2(\delta)+1\). Thus \(v_2(s-y)=1\), \(\xi\) is odd, and \(W\) is in an odd column. It cannot be a true column, excluding FW. Its sea row, when it lies in the strip, is the same \(s\) as at \(S\) by period seven and \(7\mid X\).

Suppose two distinct parked triangles produce the same \(W\). The profile fixes their common sea row \(s\) from the residue of \(W_x\). Hence they have the same \(\delta=W_y-s\). Their initial rows \(y,y'\) have the parity of \(s\) and belong to the same true role. If the two rows agreed, the initial points, ending points, and the sea points would all agree. Thus \(c=v_2(y-y')\) is finite. Put \(q=v_2(\delta)\). The differences of the ending true rows and of the initial true rows are both \(y-y'\). Write \(X,X'\) for the two true displacements and \(\xi,\xi'\) for the two offsets from the initial true points to the sea. The equality of white columns gives
\[
 v_2(\xi-\xi')=v_2(x_C-x_{C'})=c+1,\qquad
 v_2(X)=v_2(X')=q+1 .
\]
With \(m=s-y,m'=s-y'\), the relation \(\xi-\xi'=-\delta(mX'-m'X)/(XX')\) gives
\[
 v_2(mX'-m'X)=c+q+3.
\]
In \(mX'-m'X=(m-m')X'+m'(X'-X)\), the first summand has valuation \(c+q+1\). The second must have that same valuation to cancel it, and \(v_2(m')=1\). Thus
\[
 v_2(X-X')=c+q. \tag{1}
\]
On an ordinary unwrapped affine diagonal of a single nonzero slope, equal row displacements would give \(X=X'\), so two parked triangles cannot meet at \(W\).

## Polynomial column maps in a single band

For an additive matching \(\pi_t(i)=[i+t]_N\), take \(\sigma(i)=[F(i)]_N\), where \(F(i)=a i+2P(i)\), \(a\) odd and \(P\in\mathbb Z[x]\). On the odd true role the physical column is \(4pF(i)\) modulo \(4pN\); on the even role it is \(4pF(i-t)\) modulo \(4pN\), using the row index of that role. These formulas also hold after adding integer multiples of \(4pN\) to columns. For a fixed row displacement \(\delta=2d\), the second difference
\[
 F(i+d)-F(i)-F(i'+d)+F(i')
\]
is divisible by \(2d(i-i')\), by expanding each monomial. Since \(v_2(i-i')=c-1\), this proves
\[
 v_2(X-X')\ge \min(\log_2N+2,\ c+q+1).
\]
Comparing with (1) gives \(2^{c+q}\ge4N\). Also \(p\mid X-X'\), so \(|X-X'|\ge4pN\).

Take just one band whose true columns fit in an interval of span strictly less than \(4pN\), as happens for \(x_i=x_0+4p\sigma(i)\). Then \(|X|,|X'|<4pN\); a putative collision forces \(X\) and \(X'\) to have opposite signs. When \(-m\delta>0\) (with \(m,m'\) of the same sign by the profile margins), each of \(\xi,\xi'\) has the same sign as its own true displacement. If \(X>0>X'\), the common white column lies between \(x_C\) and \(x_{C'}\), and
\[
 X-X'=(x_{A'}-x_A)-(x_{C'}-x_C)\le |x_{A'}-x_A|<4pN.
\]
The other ordering gives the same contradiction.

For the other sign and \(W\) in the strip one has \(|\delta|\le C\), where a lower sea row \(s\) is at distance at most \(C\) from row 1 and an upper sea row is at distance at most \(C\) from row \(h\). Indeed \(\delta\) moves from \(s\) toward that nearer boundary. The true horizontal displacements are multiples of \(p2^{q+1}\), and the distance between ending columns is at least \(p2^{c+1}\). Using \(|m|,|m'|\le h-1\),
\[
 p2^{c+1}\le|\xi|+|\xi'|\le\frac{h|\delta|}{p2^q}.
\]
It follows that \(2p^2\,2^{c+q}\le h|\delta|\). Since \(h\le2N\), this requires \(|\delta|\ge4p^2\). Choose an odd multiple of 49 with \(4p^2>C\). This excludes every pair of distinct parked triangles sharing a white corner in this single band. For the quoted H7 bounds \(C=24000\), \(p=147\) suffices.

The resulting local tests inside one smooth band are opposite-role vertical rivals and the two-true, two-sea crossed mixed family R2s, subject to the profile and single-label hypotheses. This statement does not combine different bands or matchings. In particular the finite stride-eight coloring certificates do not apply directly to the stride-four P graph.
