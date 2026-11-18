# Row stability below equality

18 November 2026. Write \(q_H=\lfloor H^2/4\rfloor\). For a blackout \(S\) on \(h\) rows, let \(t\) be the number of occupied columns. Put \(e=|S|-t\) and \(D=q_h-e\). If there are \(z\) empty columns, the deficit from the row bound is
\[
m+q_h-|S|=D+z.
\]
For \(h,m\ge3\), validity for axis-aligned rectangles means that the row-column incidence graph contains neither a four-cycle nor a six-cycle. In particular \(e\le q_h\) by the [row-tree bound](../../papers/extremal/sections/sec3_rowbound.tex). All row deletions below keep the original column incidences. The argument uses no compression of geometric coordinates.

## 1. Removing exceptional rows

**Theorem 1.** Suppose \(D=o(h^2)\). There is a set \(X\) of \(O(D/h)\) rows such that every column contains at most two rows outside \(X\). The pairs in these remaining columns form a bipartite graph. For instance, \(|X|\le40D/h\) when \(h\ge40\) and \(D\le h^2/100\).

To start, take a column \(B\) of size \(k\ge3\) among the current \(H\) rows. Each other column meets \(B\) at most once, by the four-cycle condition. A column that meets \(B\) and has at least one outside row loses one unit of excess when \(B\) is removed. An outside row cannot belong to two such columns. If they meet the same row of \(B\), they give a four-cycle. If they meet different rows, the two columns and \(B\) give a six-cycle. There are at most \(H-k\) such columns. Removing \(B\) therefore lowers \(e\) by at most \(k-1+H-k=H-1\).

The corresponding drop in \(D\) is at least \(q_H-q_{H-k}-H+1\). For \(H\ge6\) this is at least \(kH/12\). To check this, use \(q_H-q_{H-k}\ge k(2H-k)/4-1/4\). After subtracting \(H-1+kH/12\), the lower bound is concave in \(k\). At \(k=3\) it equals \(H/4-3/2\). At \(k=H\) it equals \(H^2/6-H+3/4\). Both are nonnegative.

Once all columns have size at most two, the row graph \(G\) with the double columns as edges is triangle-free. If \(G\) is nonbipartite, take a shortest odd cycle of length \(g\ge5\). It has no chord. An outside vertex has at most two neighbors on the cycle. Otherwise its consecutive neighbors give at least three gaps, each of length at least two. Some gap is odd and is at most \(g-4\). That arc and the outside vertex give a shorter odd cycle. The sum of the degrees on the shortest odd cycle is at most \(2H\), so one row has degree at most \(2H/5\). Removing it saves at least \(\lfloor H/2\rfloor-2H/5\ge H/20\) units of deficit when \(H\ge20\).

Perform one of these operations whenever possible. As long as \(H\ge h/2\), each removed row accounts for at least \(h/40\) of the initial deficit, including the last batch if it would cross \(h/2\). With \(D\le h^2/100\), crossing \(h/2\) would require more than the initial deficit. The residual deficit stays nonnegative by the row-tree bound. This proves Theorem 1.

## 2. A cut for all pairs in a column

Call two rows neighbors if they occur together in any original column. This includes every pair in a column of size three or more.

**Theorem 2.** Under the hypotheses of Theorem 1, there is a coloring of the rows with two colors for which \(O(D^{3/2}/h)\) neighboring pairs are monochromatic.

Take the bipartition \(A,B\) of the rows outside \(X\) given by Theorem 1. If \(H=h-|X|\), its row graph has \(q_H-D'\) edges with \(D'\le D\). It therefore misses at most \(D\) pairs of \(A\times B\), since \(|A||B|\le q_H\).

Fix \(x\in X\), and write \(a,b\) for its neighbor counts in \(A,B\). Consider a neighbor \(u\) in \(A\) and a neighbor \(v\) in \(B\). If their columns with \(x\) are distinct, then \(uv\) is absent. A third owner for \(uv\) would give a six-cycle, and either of the first two owners would repeat a pair. If they have the same column with \(x\), that column contains only those two core rows. These exceptions form a matching, because each pair with \(x\) has a unique owner. Hence \(ab-\min(a,b)\le D\), which gives \(\min(a,b)\le1+\sqrt D\).

Give \(x\) the color opposite to its larger core neighborhood. Do this for every \(x\in X\). The number of monochromatic neighboring pairs is at most
\[
 |X|(1+\sqrt D)+\binom{|X|}{2}=O(D^{3/2}/h).
\]
For \(D=0\), the row set \(X\) is empty.

This estimates the optimum in the geometric problem. Let \(f_{\rm bp}(h,m)\) be the largest valid blackout for which some coloring of the rows with two colors puts at most one point of each color in every column. Write \(\delta=m+q_h-f(h,m)\) and \(\delta_{\rm bp}=m+q_h-f_{\rm bp}(h,m)\). Then
\[
 0\le\delta_{\rm bp}-\delta\ll\delta^{3/2}/h
 \qquad\bigl(\delta=o(h^2)\bigr).
\]
In a valid optimum \(D\le\delta\). Apply Theorem 2, then retain one row of each occupied color in each column. The number erased is at most the number of monochromatic pairs, as each pair occurs only once. Revealing cells preserves distinct rectangle presentations. In particular, if \(m=q_h-d\) with \(0\le d=o(h^2)\), then \(f(h,m)\le2m+O(d^{3/2}/h)\). This follows at once if \(f\le2m\). For \(f>2m\), use \(\delta<d\) and \(f_{\rm bp}\le2m\).

The order of the monochromatic-pair bound is sharp for axis validity. Take the graph obtained from a five-cycle by replacing its consecutive vertices by independent sets of sizes \(N,N,s,t,s\) and each edge by a complete bipartite graph. Use its edges as double columns. The graph is simple and triangle-free, so its incidences have girth at least eight. It has \(h=2N+2s+t\) and \(e=N^2+2Ns+2st\). Hence
\[
 D=s^2+Nt-st+\lfloor t^2/4\rfloor.
\]
In a maximum cut one can give each class a single color, as all its vertices have identical neighborhoods and no internal edges. Recolor the classes successively without decreasing the cut. Some adjacent pair of classes on the odd cycle is monochromatic. For \(1\le t=o(N)\) and \(s=\lfloor\sqrt{Nt}\rfloor\), the smallest such complete pair has \(st\asymp D^{3/2}/h\) edges. The assertion of sharpness concerns row pairs with prescribed axis-valid incidences.

## 3. Triples sharing a row

**Lemma 3.** Put \(n=\lfloor h/2\rfloor\), and assume \(h\ge12\) and \(D<h-4\). Every column of size at least three is a triple. If there are \(T\ge1\) triples, they share a row \(x\). If \(a\) ordinary doubles contain \(x\), then
\[
 D\ \ge\ n-1+(T-1)^2+(T-1)a .
\]

A column of size at least four implies \(D\ge q_h-q_{h-4}-h+1=h-3\) by the removal bound. Two disjoint triples imply \(D\ge q_h-q_{h-6}-(h-1)-(h-4)=h-4\) by removing them successively. Thus the triples meet pairwise. For \(T\ge2\), choose their first two and let their intersection be \(x\). Any further triple missing \(x\) meets both at different rows, giving a six-cycle. For \(T=1\), choose any row of the triple.

Write the triples as \(\{x,u_i,v_i\}\). All \(2T\) endpoints are distinct. No double joins different endpoint pairs, since it would close a six-cycle through \(x\). Of the \(g=h-1-2T\) other rows, each row is joined to at most one endpoint of any given pair by a double. Two such doubles would form a six-cycle with its triple. Each row joined to \(x\) by a double has no double to any endpoint, for the same reason. Doubles among the \(g\) rows form a triangle-free graph. Consequently
\[
 e\le 2T+a+(g-a)T+q_g
   = q_{h-1}+2T-T^2-(T-1)a .
\]
Here \(q_{h-1}-q_g=T(h-1)-T^2\) for both parities of \(h\), and \(q_h-q_{h-1}=n\).

## 4. The first staircase

**Theorem 4.** Let \(h\ge12\), \(w=q_h-n\), and \(m=w-\ell\) for a nonnegative integer \(\ell\). Put
\[
 k=\left\lfloor\frac{\sqrt{4\ell+1}-1}{2}\right\rfloor,\qquad G=k+1.
\]
Whenever \(\ell-G\le\lceil h/2\rceil-4\),
\[
 f_{\rm ax}(h,m)=2m+G,\qquad f(h,m)\le 2m+G .
\]
The range includes \(0\le\ell\le\lceil h/2\rceil-4\). The earlier bound used \(h-3\ge12(\ell+1)\). [Earlier staircase and construction](../2026-11-09/full_problem_push/axis_borderline_single_triple.md)

Suppose an axis-valid board has at least \(2m+G+1\) cells. As \(t\le m\), its \(D\) is at most \(n+\ell-G-1\le h-5\). By Lemma 3 only triples can exceed two cells, so \(T\ge G+1\). Thus \(n-1+G^2\le D\le n+\ell-G-1\). This implies \(\ell\ge G(G+1)\), contrary to the definition of \(k\).

For attainment, start with the triple \(\{x,b_1,b_2\}\). Split the other \(h-3\) rows into balanced parts \(A,C\). Select \(k\) distinct rows \(u_i\) of \(A\) and \(k\) distinct rows \(v_i\) of \(C\). Add the triples \(\{x,u_i,v_i\}\), attach the remaining rows of \(A\) to \(b_1\) by doubles, and attach the remaining rows of \(C\) to \(b_2\). Include every double in \(A\times C\) except the product of the two selected sets.

No row pair repeats. The double graph is bipartite. A six-cycle using one triple would require a row joined by doubles to two of its members. The attachments to \(b_1,b_2\) are disjoint and \(x\) has no doubles. For a selected pair \(u_i,v_i\), neighbors by doubles lie in opposite parts and include neither \(b_1\) nor \(b_2\). A six-cycle using two triples would need a double between endpoints of different pairs. These would be a deleted cross-edge or an absent attachment to a selected row. Three triples meet only at \(x\). This verifies axis validity.

Since \(1+h-3+q_{h-3}=w\), there are \(w-k(k+1)\) columns, of which \(G\) are triples. Delete \(\ell-k(k+1)\le2k+1\) ordinary doubles. The range of the theorem gives \(k^2\le\lceil h/2\rceil-3\le|A|\), taking \(|A|\le|C|\). For \(h\ge12\) both parts have at least four rows, and \(|A||C|-k^2\ge|A|(|C|-1)\ge2k+1\). Thus all choices and deletions are possible. The remaining width is \(m\), with \(2m+G\) cells.


## 5. The order of the axis-only gain on intermediate widths

**Theorem 5.** Fix \(A>0\). Uniformly for integers \(h\le d\le h(\log h)^A\) and \(m=q_h-d\),
\[
 f_{\rm ax}(h,m)=2m+\Theta_A(d^{3/2}/h)\qquad(h\to\infty).
\]
The lower construction in this theorem uses axis validity. For the geometric problem, Theorem 2 gives the upper bound throughout the same range.

The upper bound for \(f_{\rm ax}\) follows by applying Theorem 2 to an axis optimum and erasing its monochromatic pairs as in Section 2. If its size exceeds \(2m\), then \(D<d=o(h^2)\).

For the lower bound put \(t=\max(1,\lfloor d/(2h)\rfloor)\) and \(s=\lfloor\sqrt d/2\rfloor\). Set aside \(t\) anchor rows. Split the other \(h-t\) rows into two balanced parts \(P,Q\). In each part choose a set of \(s\) rows, denoted by \(P_0,Q_0\). Here \(t\ll(\log h)^A\) and \(s=o(h)\). Use every ordinary double from \(P\times Q\) outside \(P_0\times Q_0\).

Inside \(P_0\times Q_0\) I need \(t\) edge-disjoint induced matchings, each of size \(\gg_A s\), in a bipartite graph. A matching is induced if the graph has no other edge between its endpoint sets. Choose a fixed integer \(j>A\) and put \(b=\lfloor(\log_2 s)/2\rfloor\) and \(r=\lfloor(b-j)/2\rfloor\). On one side take all \(r\)-subsets of \([b]\), and on the other all \((r+j)\)-subsets. Join \(U\) to \(V\) when \(U\subset V\), and give this edge the color \(J=V\setminus U\). Each color is an induced matching. Its left endpoints avoid \(J\), and its right endpoints contain \(J\). If two such endpoints are joined, the difference of their sizes forces \(V\setminus U=J\).

There are \(\binom bj\gg_A(\log h)^j\) colors, so select any \(t\). Each selected color has \(\binom{b-j}r\) edges. If \(M\) is the larger of the two layer sizes, this is \(\gg_A M\). The ratios to the two layer sizes tend to \(2^{-j}\) by the binomial product formula. Take \(\lfloor s/M\rfloor\) disjoint copies on the two selected parts, using the same colors in each. Since \(M\le2^b\le\sqrt{s}\), every color now has \(\gg_A s\) edges. Its matching is still induced in the union of the selected edges.

For each edge \(uv\) of color \(i\) make the triple \(\{x_i,u,v\}\), where \(x_i\) is the corresponding anchor. Edges of one color form a matching, and every data pair \(uv\) has one color. No row pair therefore occurs in two triples. The ordinary doubles avoid the box, so no pair repeats anywhere.

It remains to exclude six-cycles. Three doubles would give a triangle in a bipartite graph. One triple and two doubles would give a two-edge path between \(u\in P\) and \(v\in Q\), as no double meets an anchor. For two triples and one double, two triples sharing an anchor have their other endpoints in the box, where there is no double. If the triples share a data row, their two other data endpoints lie in the same part, and the remaining endpoints are anchors. For three triples, three different colors would require a triangle among data edges. Three of one color meet only at the anchor. If two have color \(i\) and the third a different color, its edge would join endpoints of different edges of the induced matching of color \(i\). These exhaust the possible incidence six-cycles.

The number \(T\) of triples satisfies \(T\asymp_A ts\asymp_A d^{3/2}/h\). Before deleting any columns, the construction has \(q_{h-t}-s^2\) doubles, which by itself is at least \(m\) for large \(h\). In fact \(q_h-q_{h-t}\le ht/2+1\le d/2+1\) and \(s^2\le d/4\). Also \(T\le ts=o(h^2)\), whereas \(m\sim h^2/4\). Thus ordinary doubles can be removed until the width is \(m\), keeping all \(T\) triples. There are then \(2m+T\) cells.
