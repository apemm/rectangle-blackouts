# A linear join with a macroscopic change of anchor

The upper anchor in a two-level singleton profile can rise by a fixed fraction of the strip height in a join of linear width. The right tail continues to use the low row. Its high columns have a different residue modulo four. This choice permits some tilted triples and determines each triple from its missing corner.

Fix a prime \(a\equiv3\bmod4\), a prime \(p>4(a+1)\), and an odd row \(L<p\). Set
\[
 B=L+ap,\qquad T=L+(a+2)p .
\]
Require \(T\le h\), \(2B-L>h\), and \(2L-B<1\). On the left use rows \(L,B\), with \(B\) allowed only at columns \(0\bmod4\). On the right use rows \(L,T\), with \(T\) allowed only at columns \(2\bmod4\). Every high column on the right must lie more than \(3ap\) columns to the right of every high column on the left. Fill every other column by \(L\). Either side can extend indefinitely. Each high point is optional.

Assume that neither distance between \(L\) and one of the high rows can produce a vertical alternative with both endpoints in the strip and with opposite row parities. It suffices that there are no positive integers \(X,Z\) with \(X^2+(U-L)^2=Z^2\) and \(Z\le\min(U+L-2,2h-U-L)\), for \(U=B,T\). At \(L=1\) the condition holds without restrictions.

The resulting board distinguishes all rectangles and is clean with respect to remote ordinary-parity owners. The separation is at most \(3ap+O(1)\) additional columns when the two pieces are placed consecutively.

## Tilted triangles

Three high points form an increasing chain in the ordinary coordinates, since all \(B\) points precede all \(T\) points. They cannot make a tilted triangle. With two low points and one high, a tilted right angle can only be at the high point, and its completion lies below the strip. With two high points and a low pivot the completion exceeds \(h\). If both high points use the same row, all in-strip tilted triples have now been excluded. If the high rows are different and the pivot is \(T\), the completion row is \(B+L-T=L-2p<1\).

This leaves a right angle at the point of row \(B\). Let \(X\) be the horizontal distance to the point of row \(T\). Let \(s\) be the signed horizontal displacement from the pivot to the low point. Then
\[
 sX=(B-L)(T-B)=2ap^2 .
\]
Since \(X>3ap\), one has \(s>0\) and \(p\nmid s\). Since \(X\equiv2\bmod4\), \(s\) is odd. Therefore \(s\) is either 1 or \(a\). The completion \(W\) has row \(L+2p\) and column \(x_T+s\), which is odd. The black point in its column is at \(L\), also odd. Thus the completion is white and has no parity-axis owner.

The two possible values of \(s\) differ modulo four. Since \(x_T\equiv2\bmod4\), the column of \(W\) determines \(s\). It then determines \(x_T=W_x-s\), \(X=2ap^2/s\), the pivot, and the low point. This proves uniqueness. It also excludes every fully black tilted rectangle.

## Two-white presentations

In a mixed support the sum of the four black rows is even, by integrality of the common corners. Both high rows are even and \(L\) is odd. Hence there are zero, two, or four high points. With zero high points the black support is collinear. With four it lies in the increasing chain above. Such a chain has no mixed support, by the pair-order proof in [the collar note](../2026-11-15/quadratic_width_round/continuation_lipschitz_collar_graphs.md), applied in the ordinary coordinates.

Suppose there are two high points. If their rows agree, the support uses only two levels of opposite parity. A horizontal pair against a crossed pair would give a half-integral row in at least one common corner. Two crossed pairs of equal length have equal absolute horizontal components. Their midpoint heights agree, so perpendicularity either identifies their midpoints or the two vectors are parallel. Neither gives a mixed support. Two horizontal pairs are parallel as well.

Suppose the two high rows are \(B,T\). If the high points make one black pair, the low points make a horizontal pair. Equal lengths would give an integral norm to \((X,2p)\). Both \(X/2\) and \(p\) are odd, so \((X/2)^2+p^2\equiv2\bmod4\). This is impossible.

Otherwise the black side and black diagonal each join a low point to a high one. Orient both upwards. If the side ends at \(T\) and the diagonal at \(B\), the lower common row is \((B+L-(T-L))/2=L-p<1\). If the side ends at \(B\), write its horizontal component as \(u\) and the diagonal's as \(v\). Both are nonzero. Put \(H\) equal to the sum of the diagonal endpoints minus the sum of the side endpoints. Equal norms and perpendicularity give
\[
 u^2-v^2=4(a+1)p^2,\qquad uH_x=-2ap^2 .
\]
If \(p\nmid u\), then \(|u|\le2a\), contradicting the first equation. If \(p^2\mid u\), let \(r=|u|-|v|>0\). From \(r(|u|+|v|)=4(a+1)p^2\) we get \(r\le4(a+1)<p\). Reducing \(r(2|u|-r)\) modulo \(p^2\) gives \(p\mid r\), another contradiction. Thus \(p\) divides \(u\) just once. The second equation yields \(|u|\le2ap\) and \(|H_x|\le2ap\). Also \(|v|<|u|\). The distance between the high points is
\[
 \tfrac12|H_x+v-u|\le3ap ,
\]
contrary to the separation.

The tilted-triangle argument excluded hidden tilted rectangles. There is no hidden axis rectangle in a singleton graph. Two-white collisions with the common pair a side of both rectangles, or a diagonal of both, would require a hidden rectangle. Presentations with at least three visible corners determine the rectangle. The only possible vertical parity rival would have a diagonal joining \(L\) to \(B\) or \(T\), since equal-parity black rows cannot induce a vertical alternative of odd length. The stated vertical-distance assumption excludes it. This finishes the proof.

## Parameters and a finite check

For example, take \(L=1\), \(a=11\), and any prime \(p\) with \(0.072h<p<0.075h\). All hypotheses hold for sufficiently large \(h\), and the prime number theorem supplies such a prime at every sufficiently large height. The two high anchors differ by \(2p\). Both the difference and the guard length are proportional to \(h\).

I checked an instance with \(L=1,a=3,p=17,h=90\), so that \(B=52,T=86\). The grid had 1,801 columns numbered 0 through 1,800. Rows 52 and 86 occupied all allowed columns through 16 and from 170 onward, respectively. All other columns used row 1. Enumerating primitive perpendicular directions from every black pivot found ten tilted triples in the strip. All ten completed uniquely at white points in row 35, five with \(s=1\) and five with \(s=3\). Grouping black segments by squared length and checking the midpoint perpendicularity found no mixed support. The checks also found no vertical parity rival.

This construction gives a join for these two profiles. Carrying the other row pairs and gluing cores whose cells extend outside the profiles remain separate requirements for the quadratic threshold.

## Several macroscopic levels and actual star labels

Fix any finite list \(0<a_1<\cdots<a_k\) of odd integers, with \(k\ge2\). For a sufficiently large odd prime \(p\), put \(b_i=L+a_i p\). Require \(L\) odd, \(L<p\), \(b_k\le h\), \(2b_1-L>h\), \(2L-b_1<1\), and the same vertical-distance assumption for each \(\{L,b_i\}\). Take the high levels in increasing horizontal order, one zone per level.

The following constants depend only on the list. Put
\[
 K=\max_{i,j}a_i|a_j-a_i|,\qquad J=\max_{i,j}|a_j^2-a_i^2|.
\]
Assume \(p>\max(2K,2J)\). Choose a power of two \(b>\max a_i\), then choose a larger power of two \(M\). In \(\mathbb Z/M\mathbb Z\) choose residues \(r_i\) with pairwise circular distances greater than \(2K\) and
\[
 r_i\equiv(a_i-a_1)p\pmod b.
\]
Such an \(M\) can be fixed independently of \(p\). For example, give each \(r_i\) a separate interval of length \(b\) with gaps exceeding \(2K\), including the wraparound gap. All residues \(r_i\) are even. In zone \(i\), allow high points only at \(x\equiv r_i\bmod M\). Use row \(L\) elsewhere, and put at least \(3Kp+1\) columns between the high supports of successive zones.

The resulting word is clean. One may also put \(L\) below one selected high point of each zone. Thus this word can own every row pair \(\{L,b_i\}\) once, while all other high points in the zone are singletons. The total joining width between the zones is \(O_{\{a_i\}}(h)\).

For distinct high types \(i,j\), write \(X=x_j-x_i\). The residues give
\[
 v_2(X)=v_2((a_j-a_i)p).
\]
The valuation is smaller than \(v_2(b)\), so the equality follows from the congruence modulo \(b\). After dividing both components by this common power of two, the high-high vector has two odd components. Its norm cannot be integral.

For an in-strip tilted triple, the preceding proof again leaves a lower high pivot \(i\), a higher endpoint \(j\), and the low endpoint at displacement \(s\) from the pivot. Here
\[
 sX=a_i(a_j-a_i)p^2,\qquad X>3Kp.
\]
It follows that \(s>0\) and \(p\nmid s\), so \(s\le K\). The displayed valuation equality shows that \(s\) is odd. The missing corner has odd column \(x_j+s\) and odd row \(L+(a_j-a_i)p\). Its column contains only \(L\). Its residue modulo \(M\) identifies \(j\) and \(s\), because the radius-\(K\) intervals about the \(r_j\) are disjoint and \(2K<M\). Its row then identifies \(i\). The right angle equation recovers both high points and the low point.

In a crossed mixed support with side rising to \(b_i\) and diagonal rising to \(b_j\), \(i>j\) again puts the lower common row below the strip, since \(a_i-a_j\ge2\) and \(L<p\). Suppose \(i<j\). In the notation above,
\[
 u H_x=-a_i(a_j-a_i)p^2,\qquad
 u^2-v^2=(a_j^2-a_i^2)p^2.
\]
In particular \(u\ne0\), even if some high columns are doubled. If \(p\nmid u\), the first equation gives \(|u|\le K\), contradicted by the second. If \(p^2\mid u\), the positive difference \(r=|u|-|v|\) satisfies \(r\le J<p\), while reduction modulo \(p^2\) forces \(p\mid r\). Thus \(p\) divides \(u\) just once. Now \(|u|,|H_x|\le Kp\), and \(|v|<|u|\). The high separation is at most \(3Kp/2\), contradicting the chosen gap. The other mixed pairings are excluded by the high-high norm test, the two-level parity argument, or the increasing high chain.

Adding the selected low cells at even high columns does not change the tilted-triple proof or the parking at odd columns. A fully black axis rectangle would require two doubles with the same row pair. The chosen double graph is a star, hence bipartite with distinct pairs. This gives axis-axis uniqueness. A vertical black pair has no distinct vertical alternative in its own column, and all other opposite-parity vertical rivals are covered by the stated distance assumption.
