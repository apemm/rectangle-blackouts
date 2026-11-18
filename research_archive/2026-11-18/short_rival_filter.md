# Excluding all short vertical rivals from a filled two-track core

Fix \(0<\epsilon<2/3\). There is a fully filled board of width \(O(h^2)\) containing each ordinary parity label once except for
\[
 O_\epsilon\bigl(h^{2-3\epsilon/2+o(1)}\bigr)
\]
omitted labels. In this board no opposite-parity nonvertical chord of horizontal extent at most \(h^{2/3-\epsilon}\) has integral length. No tilted triple or nonvertical mixed quadruple has all black points in one parity, at any horizontal extent. No mixed support has a horizontal black side or diagonal. The singleton rule is part of this construction. These statements leave long opposite-parity rivals and two-role tilted or mixed obstructions.

### A trace for each parity

Pad the grid of odd and even row indices to a dyadic square \([0,N)^2\), where \(N\) is the least power of two at least \(\lceil h/2\rceil\). Traverse the square in Hilbert order. At padded cells clip each coordinate to its largest actual index. At rank \(r\) the resulting row pair is \((a_r,b_r)\), with \(a_r\) odd and \(b_r\) even. Every actual label has one designated occurrence at its original cell. Clipping is nonexpansive and each step changes at most one physical row by 2. Give each rank \(K\) consecutive columns for an absolute integer \(K\). Its two possible black rows, throughout those columns, are \(a_r,b_r\).

First consider either row trace with its point present at *every* column. A set of points from one or two consecutive ranks lies on a chain, possibly after a row reflection, and has no tilted triple or mixed quadruple. A nonhorizontal chord in this set has vertical magnitude 2. Its length cannot be integral for \(X\ne0\), since \((L-X)(L+X)=4\) has no positive factors of equal parity giving \(X>0\).

A set meeting ranks \(r,s\) with \(s-r=n\ge2\) has horizontal span at least \(K(n-1)\). Its row diameter squared is at most \(C(n+1)\) by Hilbert locality, with an absolute \(C\), including points at all intermediate ranks. Take \(K>9C\). The one-parity obstruction span bound \(3d^2\) and the inequality between consecutive squares from the [two-strip proof](hilbert_two_strip_joins.md) now exclude all same-parity tilted triples and nonvertical mixed supports, and all nonhorizontal same-parity chords of integral length. These statements persist under arbitrary point deletions from either trace. Also a mixed support with a horizontal principal chord would require an equal-length same-parity chord and is excluded as in the two-strip proof.

### Which gaps to omit

Set \(H=\lfloor h^{2/3-\epsilon}\rfloor\) and
\[
 {\cal Y}(H)=\{1\le y<h:\exists\,1\le x\le H,\quad x^2+y^2=L^2,\ L\in\mathbb Z\}.
\]
For any \(x\), factoring \((L-y)(L+y)=x^2\) gives at most \(\tau(x^2)\) possible values of \(y\). Thus \(|{\cal Y}(H)|\le Hh^{o(1)}\), by the elementary divisor bound used in the [threshold draft](../../papers/extremal/drafts/upper_bound/part8_assembly.tex). The Hilbert locality estimate implies that whenever two physical columns are within \(H\) of one another, their odd trace rows differ by at most \(C_1\sqrt{H+1}\), for an absolute \(C_1\). Declare an absolute label gap \(g\) exceptional if it is within \(C_1\sqrt{H+1}\) of \({\cal Y}(H)\). There are \(O(H^{3/2}h^{o(1)})\) such gap values. Each gap occurs in at most \(h\) labels, proving the announced exceptional count.

Fill *every* column with its odd trace row. Add the even row at one designated column of each nonexceptional label, and nowhere else. This fills the board and retains every desired double once, including at the padded boundary. Suppose an even point of a retained double formed an integral chord of horizontal extent \(1\le |X|\le H\) with an odd point. Their absolute row difference belongs to \({\cal Y}(H)\). It differs from the gap of that double by at most the difference of the odd trace rows at the two locations, at most \(C_1\sqrt{H+1}\). This contradicts the choice of that double. More generally the same proof allows even singletons at nonexceptional ranks if desired.

The [positional block estimate](../../papers/extremal/drafts/upper_bound/part8_assembly.tex) budgets \(O(h^2)\) columns to an arbitrary set of \(O(h^{2-\delta})\) exceptional labels for fixed \(\delta>0\). Thus the number omitted here fits that budget. The entire main core still needs its long-rival, mixed, and triangle tests before that assembly can give a threshold result.

### Where a different ordering helps the radius

For the vertical-rival conclusion alone, traverse the labels one odd star at a time in increasing odd-row order. Give each star \(\lfloor h/2\rfloor\) columns, one per even leaf. Fill the columns by the odd trace and insert the desired even rows. An interval of integer length \(H\le h\) now meets only a bounded number of consecutive stars, so its odd rows differ by \(O(1)\). The same proof deletes only \(O(hHh^{o(1)})\) labels. It excludes all rivals out to \(H=h^{1-\epsilon}\) at a subquadratic deletion cost. The slow trace estimate in this ordering controls the odd rows. The two-track Hilbert proof of all single-parity exclusions does not extend to an arbitrary order of the even leaves.

