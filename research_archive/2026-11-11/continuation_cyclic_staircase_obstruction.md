# A regular cyclic staircase defeats the three-corner route

Research note, 11 November 2026. This is a continuation of
[saturated_diagonal_forest.md](saturated_diagonal_forest.md).
It does not settle the saturated complete-balanced case.

For every \(h\ge4\), there is an axis-valid \(h\times h\) all-double board that uses every row exactly twice and has no tilted rectangle with three or more black corners. All its primitive perpendicular line-incidence graphs are therefore forests.

The board is invalid for a different reason: one explicit mixed \(45^\circ\)/axis collision works at every height. Thus regular row degrees and the diagonal forest identities alone cannot force a tilted three-corner obstruction.

## 1. The family

Take
\[
 S_h=\{(i,i):1\le i\le h\}
 \ \cup\ \{(i,i+1):1\le i<h\}
 \ \cup\ \{(h,1)\}.                                      \tag{1}
\]
Its columns are
\[
 12,\ 23,\ 34,\ \ldots,\ (h-1)h,\ h1.
\]
Every row and column has degree two. Its row-pair graph is \(C_h\), so it is axis-valid for \(h\ge4\). For even \(h\), all its labels have opposite physical parity.

Write
\[
 D_0=\{(i,i)\},\qquad D_1=\{(i,i+1)\},\qquad C=(h,1),
\]
with the ranges in (1).

## 2. No tilted rectangle has three black corners

It suffices to examine right angles among three points of \(S_h\).

First consider three points in \(D_0\cup D_1\). Two lie on one of the two parallel diagonal lines.

A right angle cannot be at either of those two points: the perpendicular projection from the other diagonal has half-integral coordinate along the first. Equivalently, the coordinate sums of points on \(D_0\) and \(D_1\) have opposite parity.

If the right angle is at the point on the other line, its perpendicularity equation has one of the forms
\[
 (u,u-1)\cdot(v,v-1)=0,\qquad
 (u,u+1)\cdot(v,v+1)=0.
\]
These are respectively
\[
 (2u-1)(2v-1)=-1,\qquad (2u+1)(2v+1)=-1.
\]
The only integral possibilities give one horizontal and one vertical leg. Hence the rectangle is axis-aligned.

Now consider a triple containing \(C\).

If its other two points lie on one diagonal line, a tilted right angle at a point \(P\) on that line would have its other same-line point \(P+(t,t)\), \(t\ne0\). Its fourth corner would be
\[
 C+(t,t)=(h+t,1+t).
\]
For \(t>0\) this is beyond the right boundary; for \(t<0\) it is below the board.

A right angle at \(C\) is also harmless. All other points lie northwest of \(C\). Their two displacement vectors have nonpositive first coordinates and nonnegative second coordinates. Their dot product can vanish only when one is horizontal and the other vertical.

It remains to take \(P=(i,i)\in D_0\) and \(Q=(j,j+1)\in D_1\), and put \(d=j-i\).

If the right angle is at \(P\), its fourth corner is
\[
 Q+C-P=(h+d,d+2).
\]
For this point to lie in the board, one must have \(d\in\{-1,0\}\). In either case \(PQ\) is horizontal or vertical, so a perpendicular rectangle is axis-aligned.

If the right angle is at \(Q\), its fourth corner is
\[
 P+C-Q=(h-d,1-d).
\]
Containment requires \(d=0\). Then \(PQ\) is vertical, but \(QC\) is not horizontal, so this is not a right angle.

These cases exhaust all triples. Every tilted rectangle has at most two black corners. In particular the family has no hidden tilted rectangle, and all slope-incidence forest conclusions apply.

## 3. A uniform mixed collision

Put
\[
 s=\lceil h/2\rceil,\qquad d=\lfloor h/2\rfloor,\qquad
 \epsilon=d+1-s\in\{0,1\},\qquad a=\lfloor s/2\rfloor.
\]
Here \(\epsilon=1\) for even \(h\) and \(0\) for odd \(h\).

The axis rectangle
\[
 R=\{(s,1),(h,1),(s,d+1),(h,d+1)\}
\]
has black corners
\[
 C=(h,1),\qquad P=(s,d+1)=(s,s+\epsilon).
\]
Its white corners are
\[
 W=(s,1),\qquad Z=(h,d+1).                       \tag{2}
\]

The same two points are a side of the tilted rectangle
\[
 T=\{W,Z,Q_1,Q_2\},
\]
where
\[
 Q_1=(s-a,1+a),\qquad Q_2=(h-a,d+1+a).           \tag{3}
\]
Indeed,
\[
 Z-W=(d,d),\qquad Q_1-W=(-a,a),
\]
so the sides are nonzero and perpendicular.

Both \(Q_1,Q_2\) lie on the same occupied diagonal:
\[
 Q_{j,y}-Q_{j,x}=1+2a-s
 =
 \begin{cases}
 0,&s\text{ odd},\\
 1,&s\text{ even}.
 \end{cases}
\]
They therefore belong to \(D_0\) or \(D_1\).

All coordinates fit. Since \(s\ge2\), one has
\[
 1\le a\le s-1,\qquad d+1+a\le d+s=h.
\]
Also \(Q_{2,x}=h-a<h\), so a point on \(D_1\) never uses its excluded column \(h\). The points \(W,Z\) are white: \(2\le s<h\) and \(2\le d+1<h\).

Consequently
\[
 R\setminus S_h=T\setminus S_h=\{W,Z\}.           \tag{4}
\]
This gives an immutable four-black-cell collision at every \(h\ge4\).

## 4. Scope for the saturated problem

The family has the following properties simultaneously:

- exactly two black points in every column;
- exactly two in every row;
- distinct double labels;
- an axis-valid row-pair graph, bipartite at every even height;
- no three-black tilted rectangle;
- zero cycle rank for every primitive perpendicular slope pair.

It still fails full validity through (4). Thus a proof of a general minimum-row-degree obstruction cannot rely only on forcing a tilted three-black rectangle or a positive slope cycle rank from these properties.

The saturated \(h\times q_h\) board has an additional, much stronger requirement: all labels of \(K_{\lfloor h/2\rfloor,\lceil h/2\rceil}\) must occur. Our family satisfies that requirement only at \(h=4\). It does not disprove that saturation forces a three-black tilted rectangle or a mixed collision.

The useful reduction is that a forest argument must use complete row-pair coverage in an essential way, or it must detect the mixed collisions omitted by the forest invariant.

The [exact checker](check_cyclic_staircase_obstruction.py) verifies (4) for every height from 4 through 1024 and exhaustively tests all black triples through height 10. Its [output](check_cyclic_staircase_obstruction.json) records the explicit small certificates. The all-height statements follow from Sections 2 and 3, not from these checks.

