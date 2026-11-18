# Removing short vertical rivals from the filled Hilbert board

Fix \(1/2\le\beta<2/3\). At every sufficiently large height the [two-strip Hilbert board](hilbert_two_strip_joins.md) can be changed by replacing some columns by a singleton in row 1 so that

* every in-strip vertical rival with horizontal displacement at most \(h^\beta\) is excluded;
* all but \(O_\beta(h^{4/3+\beta}\log h)\) opposite-parity labels are retained, at their original positions;
* the width remains \(O(h^2)\).

This statement concerns vertical rivals. Replacing a singleton by row 1 can affect tilted triples and mixed supports. The short-range conclusion does not by itself restore the full set of one-role exclusions.

Put \(S=\lceil h^\beta\rceil\). Associate each original cell with the tile whose representatives supply its row. In the two-strip construction the systems occur in tile order: a core and its incoming and outgoing half-guards all use that core's rows. Each side \(b_i\) is \(O(h^{1/4})\) by the stopping rule. A representative lies within \(O(b_i)\) rows of a native label of the appropriate parity.

Consider the padded Hilbert traversal of rank cells. In each gap with positive discarded-rank count, the path leaves the rectangular set of actual index pairs through a boundary edge and later reenters. The path is simple and the rectangle has \(O(h)\) boundary edges. Thus there are \(O(h)\) such gaps. In the center of each corresponding guard, where the system changes, replace every column within distance \(S\) by a singleton in row 1. At most \(O(hS)\) labels are lost in this step. A column on only one side of a guard is treated by the same prescription if it falls within this distance.

Any two remaining original columns at displacement at most \(S\) have their systems connected by a run of terminal tiles with no positive discarded-rank gap. The ranks occupied by tiles strictly between their systems have total length at most \(S\): each such tile supplies at least \(b_i^2\) physical core columns. Indeed the modular core has \(p_iq_i>b_i^2\) columns, and a unit core has one. The two endpoint tiles together add \(O(h^{1/2})\) ranks. Hilbert locality now gives coordinate differences \(O(\sqrt S+h^{1/4})=O(\sqrt S)\) throughout these endpoint tiles. Partial clipping at the edge causes no change because the endpoint bound already pays for the full padded squares.

For each native index pair let its offset be the absolute difference of its physical odd and even rows. Consider original points of opposite parity in two columns at distance \(X\le S\), whose vertical difference in magnitude is \(g\). The offset of *every* native label in either source tile differs from \(g\) by \(O(\sqrt S)\). To see this, take the odd coordinate from one endpoint system and the even coordinate from the other. Both stay within the Hilbert locality bound of their chosen native coordinates, after multiplying index distances by two and allowing the representative extensions.

If \(X^2+g^2=L^2\) can yield an in-strip rival, \(g\) is odd and \(L<h\). An odd \(X\) is impossible modulo four. Thus \(X\) is even, \(L\) is odd, and
\[
 j=(L-g)/2\ge1,\qquad j(g+j)=(X/2)^2.
\]
Choose \(\sigma=2/3-\beta>0\). A gap \(g\ge h^{1-\sigma}\) satisfying this condition has \(j\le J=\lceil S^2/(4h^{1-\sigma})\rceil\). The two factors in the last equality have the same squarefree part. Write \(j=a u^2,\ g+j=a v^2\) with \(a\) squarefree. There are at most
\[
 \sum_{a\le J}\sqrt{J/a}\sqrt{(h+J)/a}
 \ \ll_\beta\ \sqrt{Jh}\log h
 \ \ll_\beta\ h^{\beta+\sigma/2}\log h
\]
possible large gaps. Here \(J=o(h)\).

Retire each tile containing a native offset at most \(h^{1-\sigma}+C\sqrt S\), or within \(C\sqrt S\) of any of the counted gaps, for an absolute \(C\) larger than the locality constant. Replace every column of a retired system, including its two adjoining half-guards, by singleton row 1. All labels in each such tile have native offsets within a further \(O(h^{1/4})=O(\sqrt S)\) of its triggering offset. Each integer offset occurs in \(O(h)\) native labels. The two losses are therefore
\[
 O_\beta(h^{2-\sigma}+h\sqrt S)
 \quad\hbox{and}\quad
 O_\beta\!\left(h^{1+3\beta/2+\sigma/2}\log h\right).
\]
Both exponents become \(4/3+\beta\) with the chosen \(\sigma\), and the seam losses fit in this bound.

A surviving original opposite-role chord of length in the lattice with \(0<X\le S\) would have triggered retirement at its first source tile. Every new point is on the strip boundary. An oblique chord from row 1 to row \(s\) has length \(L>s-1\), so the lower endpoint of its alternative centered vertical segment has row \((1+s-L)/2<1\). The same calculation applies for two points in row 1. These points cannot create an in-strip rival. This proves the assertion, including a comparison with any remotely placed opposite-parity owner.

At \(\beta=1/2\) this keeps all but \(O(h^{11/6}\log h)\) labels and removes vertical rivals out to distance \(\lceil\sqrt h\rceil\). The range can approach \(h^{2/3}\) through smaller fixed powers while retaining a power saving in the number of lost labels.

## Keeping all short-window exclusions on the same Hilbert construction

Fix \(1/4<\alpha<1/2\) and \(1/2\le\beta<2/3\). Put \(T=\lceil h^\alpha\rceil,\ S=\lceil h^\beta\rceil\). A variant of the preceding repair gives a fully filled Hilbert board of width \(O(h^2)\) with all but \(O(h^{2-\delta})\) labels for some \(\delta(\alpha,\beta)>0\). It has no tilted black triple or nonvertical mixed support of black span at most \(T\), and no in-strip vertical rival with oblique horizontal displacement at most \(S\). This construction retains the original representatives and their physical spacings on every surviving tile. There is a stronger short-window bound on a different, [star-shaped board](all_obstructions_short_windows.md).

Let \(F\) consist of three odd rows near \(1,h/2,h\), pairwise at least \(h/3\) apart for large \(h\). To any tile assign a row in \(F\) whose distance from both of its native central rows is at least \(h/10\). Each central row rules out at most one candidate. The possible gap set
\[
 {\cal Y}(S)=\{g\le h:\ g^2+X^2=L^2,\quad 1\le X\le S,\; L\in\mathbb Z\}
\]
has size \(S h^{o(1)}\): for each \(X\) count divisors by \((L-g)(L+g)=X^2\). The maximum number of divisors of an integer of size at most \(h^2\) is \(h^{o(1)}\), as in the [short-rival filter](short_rival_filter.md).

Cut the sequence into runs at positive discarded-rank gaps. At each cut insert two extra half-guards of \(S+1\) singleton columns, using the assigned row of the respective endpoint tile. This costs \(O(hS)\) columns. The original half-guards are retained. Within each run any two source tiles appearing in physical positions at distance at most \(U\le S\) have native coordinates and their representatives within \(O(\sqrt U+h^{1/4})\) rows of one another in each role. This follows by counting the intervening tile ranks as above. Include a new half-guard at its adjacent endpoint when applying this estimate. In particular a span-\(S\) set can contain surviving original points from at most one run. If it contains such points, any extra half-guard it sees belongs to that same run.

Retire a tile if one of the following holds for a native label or a representative.

1. A native gap is at most \(20T^2+C\sqrt S\).
2. A native gap lies within \(C\sqrt S\) of \({\cal Y}(S)\).
3. Its extended even representative interval contains a row at distance in \({\cal Y}(S)\) from a member of \(F\).

Here \(C\) exceeds the locality constant. Replace the entire system of each retired tile by its assigned constant row from \(F\). Accounting for the native tile diameter \(O(h^{1/4})\), the respective numbers of lost labels are
\[
 O(h T^2+h\sqrt S),\qquad
 h^{1+3\beta/2+o(1)},\qquad
 h^{5/4+\beta+o(1)}.
\]
In the last estimate each of the \(O(S h^{o(1)})\) dangerous even rows costs at most \(O(h^{1/4})\) nearby native even-row values and hence \(O(h^{5/4})\) native labels. Each of the three estimates has a fixed power saving from \(h^2\).

Consider a span-\(T\) window. Its surviving original odd rows form one band of diameter \(d=O(\sqrt T+h^{1/4})\), and the original even rows form another. If both occur, their mutual separation is greater than \(10T^2\), by the first retirement rule and locality. Every replacement or added row present is at least \(h/10-O(\sqrt T+h^{1/4})\) from either original band: compare their original tiles in the same run. Treat each distinct level from \(F\) as a separate, constant band. All these bands are thus mutually separated by more than \(4T^2\) for large \(h\).

A tilted triple using two or more bands has one vertical leg of magnitude greater than \(4T^2\) and another nonzero vertical leg. Its horizontal product is at most \(T^2\). A triple inside one original band is excluded by the one-role Hilbert theorem. Adding cut guards does not change relative positions within runs. A constant band has no such triple.

For a mixed witness write \(U,V,H=E+F-A-B\) for its usual side, diagonal and doubled midpoint displacement, where \(U\) is nonvertical. A side crossing bands is impossible since \(|U_y|>4T^2\) and \(|U_xH_x|\le2T^2\). Perpendicularity forces \(H_y=0\), then \(H_x=0\). If the side lies within a band then its norm is at most \(T+d\), so the equal diagonal cannot cross bands. If side and diagonal lie in different bands then \(|H_y|>4T^2\). Perpendicularity forces \(U_y=0\), and the equal-integer-length diagonal is horizontal as well, because every nonhorizontal chord within either original band has nonintegral length. Thus \(V=\pm U\), which is excluded. In the last case all endpoints belong to one band, so the original one-role result or constancy applies.

For the vertical rival up to displacement \(S\), a chord between surviving roles would force retirement by rule 2. A chord from a replacement or added point to an original even row would force retirement by rule 3. Endpoints both in the odd role, including the assigned levels from \(F\), cannot give an integral vertical diameter with opposite-parity endpoint rows. Indeed that vertical diameter has odd squared length modulo four. More directly, its midpoint is a half-integer row, while an odd-odd chord has integer midpoint row. These cases exhaust the possibilities.

The repair proves these two window bounds on the same filled board. Long mixed supports, long tilted triples, and vertical rivals beyond \(S\) remain to be controlled.
