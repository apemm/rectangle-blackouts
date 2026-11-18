# A clamped descending block with many prime-gap doubles

Use rows \(0,\ldots,H\). Let \(p\ge5\) be prime, with \(2\) a quadratic nonresidue modulo \(p\). Write \(H=p+R\), where \(R\) is even and \(0<R<p/2\). Start with one point per column on the clamped line \(y=\min(H,\max(0,-x))\). Write \(D_t=(-t,t)\), \(0\le t\le H\). At any chosen odd index \(r\) with \(0<r<R\) add \(U_r=(-r,p+r)\). Thus one block admits as many as \(R/2\) prospective doubles.

**Proposition.** The construction excludes all in-strip rivals to vertical owners. Every in-strip nonaxial rectangle with three black corners has a unique parked white completion for the ordinary row-parity partition. Mixed supports entirely in the core are impossible. A mixed support meeting a constant tail remains possible, even with only one chosen double.

## Vertical owners

A chord with a point on the bottom or top boundary has no longer vertical diameter with both ends in the strip at its midpoint height. For core points, \(x+y=0\bmod p\). The squared length of a chord in different residue classes is a nonzero multiple of \(2\) by a square modulo \(p\), hence a nonsquare. In the same residue class both coordinate differences are divisible by \(p\). A nonaxial chord of length at most \(H<3p/2\) then has both coordinate magnitudes \(p\), giving nonintegral length \(p\sqrt2\). A horizontal chord has both endpoints in one row and cannot be a rival to an opposite-parity owner.

## Tilted triples

The background is antitone, so any nonaxial chord has negative slope. This immediately treats three background points. For three core points use the similar coordinates \(u=x+y,\ v=y-x\). The two lines occupied by the core are
\[
 D_t=(0,2t),\qquad U_r=(p,p+2r).
\]
A leg joining like points is vertical in these coordinates, whereas a chord between the two lines has odd \(v\)-difference. The remaining possibility is that the two endpoints of the hypotenuse belong to the same line. If both endpoints are uppers, their diameter is at most \(2R<p\), too small to reach the other line. If they are \(D_t,D_s\), the right-angle equation at \(U_r\) is
\[
 (2t-p-2r)(2s-p-2r)=-p^2.
\]
Each factor has magnitude less than \(p^2\), since \(H<3p/2\) and \(p\ge5\). Thus the factors are \(p,-p\), giving the axial legs to \(D_r,D_{p+r}\) in the original coordinates.

Two uppers and a tail point form an antitone set. One upper and two tail points likewise form an antitone set, since both halves of the background tails lie weakly beyond every upper in horizontal and vertical order. It remains to take \(D_t,U_r\) and one tail point. Put \(s=t-r\).

For a bottom point \((z,0)\), \(z\ge0\), a pivot at the bottom with two tilted legs is impossible because both endpoints lie up and to the left. A pivot at \(U_r\) would require \(s(z+r)=(p-s)(p+r)\) and the fourth row \(s-p\ge0\), incompatible. At \(D_t\) the equation is \(s(z+t)=(p-s)t\). Hence \(0<s<p/2\) and
\[
 z=(r+s)(p/s-2),\qquad W=(z+s,p-s).
\]
Integrality gives \(s\mid r\), because \(s<p\) and \(p\) is prime. Since \(r\) is odd, so is \(s\). Thus \(W\) is a white cell of even row at a positive-column singleton in row zero.

For a top point \((-H-z,H)\), \(z\ge0\), the pivot cannot lie at the top, by the same coordinate ordering. A pivot at \(D_t\) would require \(s z=(H-t)(p-2s)\), with \(0<s\le p/2\) in a tilted triple, and the fourth row \(H+p-s\) would exceed \(H\). At \(U_r\) one obtains
\[
 z=p(R-r)/s-(p+2(R-r)),\qquad W=(-H-z-s,R+s).
\]
Here \(s>0\), \(s<p/2\) and \(s\mid R-r\) by the same integrality argument. The odd \(s\) gives an odd completion row at a top-tail singleton in the odd row \(H\).

The two types of completions belong to opposite tails. In either tail the row of \(W\) determines \(s\), then its column determines \(z\) and \(r\), since \(p/s-2>0\). Thus each completion has only one tilted presentation.

## Mixed supports

The background lies on a 1-Lipschitz graph, hence is a chain after a 45-degree similarity. The mixed-support assertion of the chain lemma applies. For a four-point support entirely in the core, equal chord lengths imply an even total number of uppers by checkerboard parity. Orient the two principal chords as needed. If each lies within one line, equal lengths force them parallel and equal up to sign, which is degenerate. Otherwise both go from \(u=0\) to \(u=p\). The shift between their doubled midpoints has zero \(u\)-component and is perpendicular to the side chord. That chord has odd \(v\)-component, so the midpoint shift is zero, again degenerate.

For an actual counterexample involving a tail take \(p=37,\ R=16,\ H=53\) and choose only \(r=9\). The black side joins \((-58,53),(-9,46)\) and the black diagonal joins \((-53,53),(-18,18)\). Their squared lengths are both \(2450\). The doubled midpoint difference is \((-4,-28)\), perpendicular to the side \((49,-7)\). The common white cells are \((-60,39),(-11,32)\). This prevents using the full set of prospective labels without additional exclusions.
