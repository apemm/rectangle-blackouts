# Vertical rivals in the canonical prime shuffle

The prime that makes crossed mixed supports rare in the [auxiliary-prime construction](auxiliary_prime_h7_diagonal.md) cannot make its vertical rivals rare. Let \(M=6272\), \(128h<p<256h\), and \(s^2=20\bmod p\). In the first lift period give rank \(i\) the column \(x_i=M[s i/M]_p\), where brackets denote the representative in \([0,p)\). Its two rows on diagonal \(T\) are \(2i+1\) and \(2i+1+T\). Split each diagonal by any rank palette of fixed period \(K\), possibly depending on \(T\), keeping relative positions within a color. Take \(K\) divisible by 14, replacing it by its least common multiple with 14 if necessary. All constants below may depend on \(K\).

Already in the first width-\(h\) slice of each lift period, and using ranks of one residue modulo \(K\), the following statements hold for all sufficiently large \(h\), uniformly in \(p,s\).

1. Across the diagonal conflict graphs there is a matching of size \(\gg_K h^2\) consisting of in-strip vertical-rival edges. Thus relocating \(o(h^2)\) labels cannot resolve P in this version of the construction.
2. The sum of the numbers of distinct positive forbidden rank differences over the signed diagonals is \(\gg_K h\log h\). The union of the conflict graphs contains \(\gg_K h^2\log h\) edges. In particular the mean degree on the whole collection is unbounded.

Here the row-pair owner for the alternative vertical diagonal may be anywhere in the eventual board, as in the P test against the complete parity graph. These statements allow deletion of a power-saving number of exceptional labels in the matching conclusion. They do not bound the chromatic number for arbitrary rank-dependent palettes or forbid changing the placement.

## Two elementary distribution estimates

The parameters \(M,K\) are fixed. Consider a positive integer \(X_0=O(h^{1/4})\), and odd \(k\) in an interval of length \(\gg h^{3/4}\). The residues
\[
 \frac1p\left[\frac{X_0k}{Ks}\right]_p
\]
are uniformly distributed in the unit interval, with discrepancy \(o_K(1)\) uniform in \(p,s,X_0\) and in the starting point. To check this, fix a nonzero Fourier frequency \(l\) and let \(r\) be the least absolute representative of \(2lX_0/(Ks)\bmod p\). Then \(20K^2r^2-4l^2X_0^2\) is a nonzero multiple of \(p\). It cannot be zero over the integers since 5 is not a square. Since \(l\) is fixed and \(X_0^2=o(p)\), this implies \(|r|\gg_K\sqrt p\) for large \(h\). The geometric sum over consecutive odd \(k\) at frequency \(l\) therefore has magnitude \(O_K(\sqrt p)\). Divide by the number of terms and approximate interval indicators from above and below by trigonometric polynomials. Uniformity over translated intervals follows by translating the approximants or by partitioning the unit interval into a fixed fine mesh.

For \(i\equiv0\bmod K\) in \([h/5,h/4]\), the values \(x_i/(Mp)\) are uniformly distributed by the same argument. If \(r\) represents \(lKs/M\), then \(M^2r^2-20l^2K^2\) is a nonzero multiple of \(p\). The progression here has length \(\gg_K h\). In particular \(\gg_K h\) starting ranks have \(h/4\le x_i\le h/2\), uniformly in the prime. Although this is a small subinterval of the period, its relative length is at least \(1/(1024M)\), a fixed positive number.

## One primitive triple gives a matching

Use the primitive triple \((X_0,Y_0,L_0)=(6272,1695,6497)\) from the Euclidean parameters \(64,49\). Let \(k\) range over odd integers with \(h/(100L_0)\le k\le h/(80L_0)\). By the first distribution estimate, for \(\gg_K h\) of these \(k\) there exists a positive \(d\) with
\[
 K\mid d,\qquad h/4000\le d\le h/2000,\qquad sd\equiv kX_0\bmod p.
\]
Indeed the allowed interval for \(v=d/K\) has length comparable to \(h/K\). Put \(T=kY_0-2d\). It is odd, of absolute value less than \(h/40\). Distinct successful \(k\)'s have distinct \(T\)'s. Equality of \(T\)'s would imply \((sY_0-2X_0)(k-k')=0\bmod p\). The coefficient is a unit for all sufficiently large \(p\), since \(X_0^2-5Y_0^2\) is a fixed nonzero integer.

For each such \(T\), take the starting ranks from the second distribution estimate. Then \(i\) and \(i+d\) have the same palette color, both labels fit in the strip, and
\[
 x_{i+d}=x_i+kX_0 .
\]
Both sides agree modulo \(p\) and are multiples of \(M\); the right side lies in the lift period and is below \(h\). The chord from the odd point of rank \(i\) to the even point of rank \(i+d\) has components \((kX_0,kY_0)\) and length \(kL_0\le h/80\). Its vertical alternative has integral endpoints since \(kX_0\) is even and \(kY_0,kL_0\) are odd. Both endpoints are in the strip because the starting row is between \(2h/5\) and \(h/2+1\). They have opposite parities. Thus this is an actual P edge, regardless of other black cells or the location of the eventual owner.

For a fixed \(T,d\) the \(\gg_K h\) edges \(\{i,i+d\}\) form a graph of maximum degree two; it contains a matching of size \(\gg_K h\). The diagonals from distinct \(k\) have disjoint label sets. This proves the first assertion.

## Many shapes force logarithmically many edges per label on average

Use a dyadic scale \(h^{1/16}\le A\le h^{1/8}/4\). Choose coprime \(a,b\) with \(A\le a<2A\), \(A/4\le b<A/2\), \(M\mid a\), and \(b\equiv1\bmod 2M\). There are \(\gg_M A^2\) choices. Indeed, writing \(a=M c\), the Möbius count of \((c,b)=1\) has a positive main density from \(\prod_{\ell\nmid 2M}(1-\ell^{-2})\), and an error \(O_M(A\log(2A))\). Put
\[
 X_0=2ab,\qquad Y_0=a^2-b^2,\qquad L_0=a^2+b^2 .
\]
These are primitive triples with \(M\mid X_0\), odd \(Y_0,L_0\), and \(X_0,L_0\ll A^2\). For each one the scale interval for odd \(k\) above contains \(\gg h/A^2\) elements. The first distribution estimate applies uniformly and gives \(\gg_K h/A^2\) successful \(k\)'s. The second estimate supplies \(\gg_K h\) witness edges for every resulting \((T,d)\) by the same construction. The bound \(|T|<h/40\) remains valid since \(kY_0\le kL_0\le h/80\).

Distinct choices of primitive parameters and odd scale give distinct pairs \((T,d)\). Indeed \(Y=T+2d\) and \(0<X\le h/80<p\) with \(X\equiv sd\bmod p\) recover the two positive legs. Their greatest common divisor recovers \(k\), and uniqueness of the primitive parametrization recovers \(a,b\) with specified even leg. The dyadic ranges for \(a\) are disjoint. Each scale therefore supplies \(\gg_K h\) distinct pairs, and there are \(\gg\log h\) scales. Witness edges from different differences on the same diagonal are distinct. This proves the second assertion. It explains why the prime averaging that removes the crossed mixed supports cannot also finish P by counting or by proving bounded degeneracy of these canonical bands.


The matching in the single-shape proof also counts remote owners if labels may be omitted entirely. The alternative's pair of rows is
\[
 2i+1+k(Y_0-L_0)/2,\qquad 2i+1+k(Y_0+L_0)/2.
\]
Its gap \(kL_0\ge h/100\) determines \(k\). For fixed \(k\) its row sum determines \(i\). The owners assigned to distinct matched edges are therefore distinct. Also every primary gap in this single-shape matching has absolute value \(<h/200\), since \(Y_0/L_0<0.27\), \(kL_0\le h/80\), and \(2d\le h/1000\). No owner is itself a primary label in the matching. Thus \(\gg_K h^2\) disjoint triples of labels witness the obstruction even if dropping an owner entirely is allowed. Moving an owner alone still leaves the conflict in a saturated board.


## A period that grows with the height

There are absolute constants \(c,c'>0\) such that for all sufficiently large \(h\) and every multiple \(K\) of 14 with \(K\le c\sqrt h\), the matching with distinct owners has at least \(c'h^2/K\) edges. Here the palettes on different diagonals may be different functions of the residue modulo the same \(K\). In particular a common period \(h^{o(1)}\) still leaves \(h^{2-o(1)}\) disjoint obstructions. Moving \(O(h^{2-\eta})\) labels for a fixed \(\eta>0\) cannot repair such a placement.

Use the fixed primitive triple from the matching proof. In coordinates \((k,d)\), the differences of the solutions with odd \(k\) form the lattice
\[
 \mathcal L=\{(k,d):2\mid k,\ K\mid d,\ s d\equiv X_0 k\bmod p\}.
\]
This lattice has covolume \(2Kp\), since the congruence has index \(p\) on \(2\mathbb Z\times K\mathbb Z\). The desired coset is nonempty, for instance \((p,0)+\mathcal L\). Every nonzero lattice vector satisfies \(0\ne X_0^2k^2-20d^2\equiv0\bmod p\). Consequently its Euclidean length is at least \(c_0\sqrt p\) for an absolute constant \(c_0>0\) (the triple is fixed).

A planar lattice of covolume \(V\) and shortest length \(\lambda\) has a fundamental parallelogram of diameter \(O(V/\lambda)\). Extend a shortest vector to a lattice basis and subtract a multiple of it from the other vector until the parallel component has size at most \(\lambda/2\). The perpendicular component then has size \(V/\lambda\), and minimality gives \(\lambda^2\le 2V/\sqrt3\). This proves the diameter bound. In our case the diameter is \(O(K\sqrt p)\). Both sides of the rectangle
\[
 h/(100L_0)\le k\le h/(80L_0),\qquad h/4000\le d\le h/2000
\]
have lengths that are fixed positive multiples of \(h\). Choose \(c\) small enough that for \(K\le c\sqrt h\) the cell diameter is below one quarter of the shorter side. Tiles anchored at coset points of the rectangle cover its portion more than one cell diameter inside its boundary. Comparing areas gives \(\gg h^2/(Kp)\gg h/K\) coset points in the rectangle. Each has different \(k\) since the \(d\)-interval is shorter than \(p\); the earlier injection assigns them different \(T\).

For every one of these pairs use starting ranks \(i\equiv0\bmod14\) with \(h/5\le i\le h/4\) and \(h/4\le x_i\le h/2\). The second distribution estimate with period 14 gives \(\gg h\) such ranks with an absolute constant. The ranks \(i\) and \(i+d\) have the same color for any palette of period \(K\) and belong to the same aligned type. The earlier matching and distinct-owner arguments now give the assertion. The proof allows a palette to change with the height. Placement rules that vary the lift within a residue class remain outside its hypotheses.

