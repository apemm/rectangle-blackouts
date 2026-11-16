# Fixed dyadic residue rules do not exclude Hilbert right angles

14 November 2026. Independently reviewed, including the recursive
address and refinement argument. This extends the actual configuration in
[the mixed-collision note](continuation_hilbert_recursive_obstruction.md).
For every fixed power of two, an unmodified Hilbert placement has a
three-label black right angle whose ranks and both label coordinates
are all divisible by that power. Thus a class rule depending only on
fixed dyadic residues of these three integers cannot make every class
right-angle-free.

The result concerns residue rules. It does not exclude classes defined
by Hilbert orientation, valuations, or an arbitrary finite coloring.
It also does not assert that local column choices preserve the angle.

## Exact ranks and coordinates

Let \(S=2^e\), with \(e\ge3\), and let \(L=4^k\), with \(k\ge0\).
Set
\[
 u=S^2L^3/2,\qquad D=u^2/L,\qquad
 q=4u^2,\qquad h=2q,
\]
\[
 \rho=u^4+8L^2u^2,\qquad t=2u^2,
 \qquad I=u^2+2Lu,\quad J=2Lu.
\]
Use the standard recursive order \(H_q\) and columns \(x_r=Sr\).
Its following three values are exact:
\[
\begin{array}{c|c}
 r&H_q(r)\\ \hline
 \rho&(I,J)\\
 \rho+L^2&(I+L,J)\\
 \rho+L^2t&(I+Lu,J+Lu).
\end{array}                                                   \tag{1}
\]

Here is a direct recursive verification. First use a coarse square of
side \(4D=q/L\). Its aligned square of side \(2u\), with origin
\((D+2u,2u)\), has identity orientation and starting rank
\(D^2+8u^2\). Its quadrant address is
\[
 0,1,\underbrace{0,\ldots,0}_{2e+4k-3\text{ copies}},2.
\]
There are \(2e+4k-2\) coordinate swaps, an even number. The rank
contributions of its two nonzero digits are \(D^2\) and \(8u^2\).
Applying the affine quadrant maps gives the stated origin.

The exponent of \(2u\) is \(2e+6k\), also even. Its local ranks
\(0,1,t\) therefore have coordinates \((0,0),(1,0),(u,u)\).
Their remaining quadrant addresses contain only digits zero, one,
and two. All maps on these three addresses are translations and
coordinate swaps; no coordinate is reflected.

Now refine every coarse cell to a square of side \(L\) and select its
first rank. The three selected ranks are multiplied by \(L^2\), and
their coordinates are multiplied by \(L\). No additional offset
appears, because the addresses have no reflecting quadrant. This proves
(1).

## The black right angle

Use the odd point in the first label and the even points in the other
two labels. Their rows are
\[
 a=2u^2+4Lu+1,\qquad b=4Lu+2,\qquad c=6Lu+2.
\]
Call the resulting points \(A,B,C\), in increasing rank order. Then
\[
 A-B=(-SL^2,t-1),\qquad
 C-B=(SL^2(t-1),2Lu).
\]
Their dot product vanishes since
\[
 2Lu=S^2L^4.
\]
Both vectors are nonzero and neither is horizontal or vertical.
The fourth corner \(W=A+C-B\) has
\[
 x_W=S\bigl(\rho+L^2(t-1)\bigr),\qquad
 y_W=2u^2+6Lu+1.
\]
It lies strictly between the first and last displayed columns and
satisfies \(1\le y_W\le8u^2=h\). The three label coordinates are
also in the \(q\)-square. Consequently this is an actual in-strip
tilted right angle, not an infinite-grid or padded-label artifact.

All three ranks in (1) are divisible by \(L^2\), and all six label
coordinates are divisible by \(L\). Given any fixed modulus \(2^b\),
choose \(k\) so that \(L=4^k\) is divisible by \(2^b\).
Every rule
\[
 \operatorname{class}(r,i,j)
   =F(r\bmod2^b,i\bmod2^b,j\bmod2^b)
\]
then assigns these three labels to one class. The same conclusion
holds for any finite collection of dyadic residue tests, by taking
their largest modulus.

The black right angle alone disproves automatic angle exclusion.
No claim about the color or uniqueness of the fourth corner is needed.
The numerical checker below also checks that the fourth corner is in
the strip, without assuming anything about its assigned label.

## Verification

[The sparse recursive checker](check_hilbert_recursive_mixed.py) checks
(1), the dot product, the fourth corner, and the divisibilities for
several values of \((S,L)\). It evaluates only the specified ranks,
so the very large board dimensions do not require allocating a board.
The proof above applies to every stated \(S,L\), independently of
those finite checks.
