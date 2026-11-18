# Exact factorization on a union of prime residue classes

Let \(H,M\ge4\). For any prime \(p>200HM\) there is a unit \(\lambda\bmod p\) with the following property. On a \(pH\)-by-\(pM\) grid restrict every black cell to \(y\equiv\lambda x\bmod p\), in coordinates starting at zero. A coloring supported there is a valid blackout if and only if its \(p\) induced \(H\)-by-\(M\) blackouts are all valid. In particular its size enumerator is
\[
 Z^{\rm restricted}_{pH,pM}(t)=Z_{H,M}(t)^p .
\]
The largest size subject to that congruence is \(p f(H,M)\), attained in \(a_H(M)^p\) ways. On the unrestricted larger grid this gives a lower bound on \(f(pH,pM)\) and a count at the specified size. A still larger size need not have that multiplicity.

This extends [window amplification](window_amplification.md) from the test for tilted triples to **all pairs of actual rectangle presentations**. It uses the midpoint argument from the [one-gap modular construction](modular_gap_blocks.md).

### Selecting the residue slope

Require \(1+\lambda^2\) to be a quadratic nonresidue and
\[
 r+\lambda s\ne0\bmod p
 \quad\text{whenever }(r,s)\ne(0,0),\quad
 |r|\le2M,\quad |s|\le2H.
 \tag{1}
\]
The rectangle contains at most \((4M+1)(4H+1)-1<25HM\) nonzero vectors. Each with \(s\ne0\) forbids at most one slope, and a vector with \(s=0\) forbids none. At least \((p-3)/2\) nonzero slopes have nonsquare \(1+\lambda^2\): use \(\sum_x(\frac{1+x^2}{p})=-1\), obtained by counting \((z-x)(z+x)=1\). Thus a slope exists at the stated size. Put \(v=(1,\lambda)\); in particular \(v\cdot v\ne0\bmod p\).

For each \(0\le j<p\), the residue class \(x\equiv j\) uses the physical points
\[
 (x,y)=(j+pX,[\lambda j]_p+pY).
\]
The full coordinate ranges for \(X,Y\) are precisely those of the base rectangle. A vector between black points reduces to a multiple of \(v\), nonzero when the points belong to different classes. Call a vector crossing if its residue is a nonzero multiple of \(v\).

### Where a collision could occur

Any triple of black corners of a rectangle belongs to one class. Indeed the two perpendicular legs from its black right-angle vertex cannot both be crossing, by \(v\cdot v\ne0\). If one is divisible by \(p\), dividing it by \(p\) gives a nonzero bounded integer vector \((r,s)\). It cannot be perpendicular to a crossing leg by (1). Both legs are therefore divisible by \(p\), and the fourth corner also lies in the class. This reasoning includes axis rectangles. In particular every hidden rectangle descends to a hidden rectangle in a base grid. A valid grid in dimensions at least four has no such rectangle by the [hidden-rectangle lemma](windows.md).

Suppose two different rectangles have the same presentation. An empty presentation would require a hidden rectangle, which was just excluded. Three visible corners determine a rectangle, so consider presentations with one or two corners. With one visible corner each rectangle descends as just shown, and its visible cell determines the common residue class. With two visible corners, if the shared segment is a side in both rectangles the other two sides are parallel equal translates normal to the segment; their four endpoints are a black rectangle. If the shared segment is a diagonal in both, their two other diagonals have the same midpoint and length, and form a black rectangle. The preceding paragraph excludes both possibilities.

In the mixed case let \(A,B\) be the black side endpoints and \(C,D\) the black diagonal endpoints. Write
\[
 u=B-A,\qquad v'=D-C,\qquad 2n=C+D-A-B .
\]
The shared corners are \(A+n,B+n\), where \(n\ne0\) is an integer vector, \(u\cdot n=0\), and \(|u|=|v'|\). The residues of all three vectors are on the line spanned by \(v\), as \(p\) is odd. If \(u\equiv0\) and \(n\) crosses, divide \(u\) by \(p\) and apply (1) to the crossing vector \(n\). If \(u\) crosses, then \(n\equiv0\) by perpendicularity. Norm equality gives \(v'\equiv\pm u\); interchange \(C,D\) to get the plus sign. The midpoint relation now gives \(C\equiv A,D\equiv B\) in both coordinates. Thus \(2n/p=(C-A)/p+(D-B)/p\) is a nonzero integer vector satisfying the doubled coordinate bounds of (1), and it cannot be perpendicular to the crossing \(u\). The remaining case has \(u,n\equiv0\). Norm equality then gives \(v'\equiv0\); the midpoint relation puts all four black points and both shared corners in one class. The mixed collision would already occur in the base rectangle of that class. This reasoning also covers a mixed side that is vertical.

Conversely any pair of colliding base rectangles lifts by the displayed similarity and still collides, since their corners are all in the same class and other classes do not change them. The choices in distinct classes are independent, proving the enumerator identity.

### A clean module for the labels whose row difference is divisible by a large prime

One can also use \(h\) physical rows not divisible by \(p\). The \(p\) classes then have base heights \(\lfloor h/p\rfloor\) or \(\lceil h/p\rceil\); using those actual heights preserves both coordinate boundaries. Set \(H=\lceil h/p\rceil\) for condition (1), and use a common base width \(M\). When the smaller base height is at least four, choose in each class a complete parity board at that height from the [threshold construction](../../papers/extremal/drafts/upper_bound/part1_theorem.tex), at width \(M\) sufficient for both heights. The finite strip module of width \(pM\) uses precisely every opposite-parity pair of rows congruent modulo \(p\), once. The prime is odd, so opposite parity in a physical class is equivalent to opposite parity after dividing row differences by \(p\). The construction controls the filled singleton columns along with the doubles.

For clarity the stronger virtual-owner tests pass when the base configurations are clean relative to their full parity graph. An integral chord between distinct classes would have squared norm a nonsquare modulo \(p\). A same-class chord of opposite parity with odd integral length has length divisible by \(p\); its vertical alternative descends to the same class since \(p\) is odd. A tilted triangle with white completion and every black point in its completion column also lie in that completion's residue class. Thus any axis owner required by that comparison has two congruent rows and is already included among the base owner's tests. Two triangles sharing their white corner descend to the same class as well.

For fixed \(\eta>0\), when \(p\ge h^{3/4+\eta}\), \(p\le h/4\), the size condition \(p>200HM\) holds for large \(h\) with \(M=O_\delta(H^2(\log(2H))^{1.3108172+\delta})\), for each fixed \(\delta>0\), by the existing full-board bound. Thus this congruence family has a globally valid module at width
\[
 O_\delta\!\left(\frac{h^2}{p}(\log(2h/p))^{1.3108172+\delta}\right).
\]
It is one complete finite module. Joining modules based on different primes while retaining global validity remains a separate problem.
