# A dyadic matching reduces each block to vertical rivals

Let \(N\) be the least power of two at least \(\lceil h/2\rceil\). Index odd rows by \(o_i=2i+1\) and even rows by \(e_j=2j+2\), keeping only rows in the strip. A dyadic isometry on \([0,N-1]\) is a permutation preserving \(v_2(i-j)\) for every \(i\ne j\).

Fix dyadic isometries \(\pi,\sigma\). In one block place the pair \(\{o_i,e_{\pi(i)}\}\) at
\[
 x_i=A c_i+8\sigma(i),
\]
whenever both rows exist. Here \(A\) is a power of two exceeding \(32h\), and \(0\le c_i<C\) are arbitrary band numbers. Every true row and every column occurs in at most one pair, though a column carries both of its row points. The width of this block is at most \(AC+8N\).

Every tilted true chord with displacement \((X,Y)\) satisfies
\[
 v_2(X)\ge v_2(Y)+2.
\]
For equal-role endpoints indexed by \(i,j\) one has \(v_2(X)=3+v_2(i-j)\) and \(v_2(Y)=1+v_2(i-j)\). The \(A\)-summand cannot change the first valuation since \(4N<A\). For opposite roles \(Y\) is odd and \(8\mid X\). A vertical pair itself has \(v_2(X)=\infty\) and \(Y\) odd. No horizontal chord connects distinct true points.

These inequalities exclude a tilted true triangle because the horizontal product has strictly larger valuation than the vertical product at a right angle. They also exclude every true mixed four-point support whose black side is nonvertical. To see this, let \(U=B-A_0\) be the black side, \(V=F-E\) the black diagonal, \(H=E+F-A_0-B\), and \(J=U-V\). Then
\[
 H\cdot U=0,\qquad J\cdot(U+V)=0,\qquad |U|=|V|,\qquad H\ne0.
\]
The absence of horizontal chords and the valuation inequality give \(v_2(U_y)=v_2(V_y)=q\). Reverse \(V\) if necessary so \(v_2(U_y+V_y)=q+1\). Perpendicularity now gives \(v_2(H_y)\ge v_2(H_x)+2\) and \(v_2(J_y)\ge v_2(J_x)+1\). The first relation has finite valuations since \(U_x,U_y\ne0\) and \(H\ne0\). The second allows zero components with the usual convention.

Put \(j=\min(v_2(H_x),v_2(J_x))\). One of \(H_x\pm J_x\) has valuation at most \(j+1\), while the vertical sums and differences are both divisible by \(2^{j+1}\). The corresponding vector among \((H+J)/2=E-A_0\) and \((H-J)/2=F-B\) has horizontal valuation at most \(j\) and vertical valuation at least \(j\). This is a true chord with nonzero horizontal component. Its vertical component is nonzero because distinct true points cannot share a row. This contradicts the valuation inequality.

If the black side is vertical, its owning double can be remote. This is the ordinary vertical-rival test. The local black diagonal would have opposite row parities and integral length at most \(h-1\). Define a simple graph on retained indices by joining distinct \(i,j\) if either of
\[
 64(\sigma(i)-\sigma(j))^2+(2i-2\pi(j)-1)^2,\qquad
 64(\sigma(i)-\sigma(j))^2+(2j-2\pi(i)-1)^2
\]
is a square at most \((h-1)^2\). Taking \(c_i\) from any proper coloring excludes these rivals. Within a band the displayed lengths are the actual lengths. Across different bands the horizontal separation is greater than \(A-8N>h\). A vertical diagonal within a single double has no distinct vertical alternative with the same midpoint and length.

There are no fully black axis rectangles since the row pairs are distinct and no row repeats. The double graph is a matching, so its axis presentations distinguish axis rectangles. Hence the black label points alone give a valid sparse block relative to the complete ordinary parity-pair graph. This includes the case of a black diagonal with some additional surrounding black cells, since the local square test is stronger than necessary.

Take \(\pi_t(i)=i\mathbin{\mathrm{XOR}}t\) for \(0\le t<N\). Changing the same binary digits of both indices preserves the least bit at which they differ. Thus every \(\pi_t\) is a dyadic isometry. Each pair of row indices occurs in the unique matching \(t=i\mathbin{\mathrm{XOR}}j\). The column isometry \(\sigma_t\) can be chosen separately in every matching. If its vertical-rival graph admits \(C_t\) colors, the sum of the physical block widths is \(O(h^2+h\sum_t C_t)\). In particular a bounded mean palette gives \(O(h^2)\) total length of the separate sparse blocks.

The last estimate does not control interactions between different blocks or fill their other columns. A uniform bound on the mean palette is also open. These remain additional steps toward a quadratic-width equality board.
