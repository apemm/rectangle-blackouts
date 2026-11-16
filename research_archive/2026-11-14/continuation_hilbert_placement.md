# A deterministic placement that excludes same-parity integral distances

Date: 2026-11-14. Status: proved below, pending independent audit.

A discrete Hilbert order gives a placement of every parity label in width
\(O(h^2)\) with no nonhorizontal integral distance between two odd label
points, or between two even label points. It therefore removes both parity
halves of the family responsible for the relocation price floor. The
placement admits independent local choices while preserving this property.

This is a placement lemma. It does not yet give a valid blackout. Opposite
parity rivals, mixed corner triples, and other label-sea supports remain.

## 1. An elementary discrete ordering lemma

For \(q=2^k\), there is a bijection
\[
H_q:\{0,\ldots,q^2-1\}\longrightarrow\{0,\ldots,q-1\}^2
\]
such that, for distinct ranks \(r,s\),
\[
\max\bigl\{|H_q(r)_1-H_q(s)_1|^2,
             |H_q(r)_2-H_q(s)_2|^2\bigr\}<16|r-s|.       \tag{1}
\]

Here is a complete recursive construction. Start with \(H_1=(0,0)\).
If \((x,y)\) runs through \(H_q\) in its specified order, concatenate
the four lists
\[
(y,x),\qquad (x,y+q),\qquad (x+q,y+q),\qquad
(2q-1-y,q-1-x).                                         \tag{2}
\]
This defines \(H_{2q}\).

Induction gives three facts. The list visits each cell once. Consecutive
cells share an edge. Every aligned rank block of length \(4^j\) visits one
dyadic square of side \(2^j\). Consecutive such squares share an edge,
because the last cell of one and the first cell of the next are adjacent.

To prove (1), let \(b\) be the least power of four at least \(|r-s|\).
Then \(b<4|r-s|\). The two ranks lie in the same aligned block of length
\(b\), or in consecutive blocks. Their cells therefore lie in one square
of side \(\sqrt b\), or in two edge-adjacent such squares. Each coordinate
difference is at most \(2\sqrt b-1\), whose square is strictly below
\(4b<16|r-s|\).

## 2. Full-grid placement

Write a parity label as
\[
e=(i,j),\qquad a_e=2i+1,\qquad b_e=2j+2,
\]
with \(0\le i<A=\lceil h/2\rceil\) and
\(0\le j<K=\lfloor h/2\rfloor\). Choose the least power of two
\(q\ge\max(A,K)\). Embed the label grid in the \(q\)-square, and let
\(r(e)=H_q^{-1}(i,j)\).

Place the two label points in column
\[
x_e=32r(e).                                             \tag{3}
\]
The missing cells of the padded square remain unused. In particular, ranks
are not compressed after deleting labels.

**Theorem 1.** In (3), any two label points of the same parity, in distinct
rows, have nonintegral Euclidean distance. The span of the label columns
is below \(32q^2\), hence \(O(h^2)\).

Proof. For labels at rank difference \(t>0\), put \(X=|x_e-x_f|=32t\).
For odd points the vertical gap is \(y=2(i_e-i_f)\). For even points it is
\(y=2(j_e-j_f)\). In either case (1) gives
\[
0<y^2<64t=2X.
\]
Therefore
\[
X^2<X^2+y^2<X^2+2X+1=(X+1)^2.
\]
There is no integer square strictly between these consecutive squares.

The same proof works for any increasing choice of integer columns satisfying
\[
x_f-x_e\ge32\bigl(r(f)-r(e)\bigr)
\quad\text{whenever }r(f)>r(e).                          \tag{4}
\]
It also works after restricting to any subset of labels, provided their
original ranks are retained.

## 3. Period-seven profile blocks and local choices

The placement can use the existing T1 profile and its collars. Within one
profile, write the odd and even rows as
\[
a_e=a_0+14i_e,\qquad b_e=b_0+14j_e.
\]
All labels of that profile have this form. Pad the coordinate ranges to a
power-of-two square and assign the Hilbert ranks as before. More generally,
if both row progressions have step \(d\), (1) gives
\[
y^2<16d^2t.                                            \tag{5}
\]
Thus any increasing column assignment with
\[
x_f-x_e\ge8d^2\bigl(r(f)-r(e)\bigr)                    \tag{6}
\]
has the same no-integral-distance property. The step \(8d^2\) is an integer.

For T1, take \(d=14\), so \(8d^2=1568=7\cdot224\). For an integer
\(M\ge1\), assign each label an arbitrary private choice
\(\xi_e\in\{0,\ldots,M-1\}\), and put
\[
x_e=1568\bigl(Mr(e)+\xi_e\bigr).                       \tag{7}
\]
If \(r(f)-r(e)=t\ge1\), then
\[
Mr(f)+\xi_f-Mr(e)-\xi_e
\ge M(t-1)+1\ge t.
\]
So (6) holds for every assignment of the private choices. All columns are
period-zero columns for the period-seven sea. The map is injective.

There are at most \(h/14+1\) coordinates on either axis. The padded square
has side below \(2(h/14+1)\), so the core span is
\[
<6272M(h/14+1)^2=O(Mh^2).                               \tag{8}
\]
The constant number of profile families changes only the implied constant.
Independent choices of the \(\xi_e\) remain available, but their supports
are small, disjoint sets near predetermined ranks. They are not the broad
independent slot laws covered by the existing relocation floor.

This construction does not give a cost proportional to the size of a
sparse label set. A set of heavy diagonals still uses the original grid's
rank span, which can be \(\Theta(h^2)\). The bound (8) is nevertheless
quadratic when \(M\) is bounded.

## 4. Exactly which obstruction disappears

Lemma F of `relocation_price_floor.md` starts with same-parity label points
\(C,D\), a nonzero row gap \(y\), and
\[
X^2+y^2=L^2.
\]
It then uses two sea points in one row at the columns
\(x_C+(X-L)/2\) and \(x_C+(X+L)/2\) to create a fatal symmetric difference.
Theorems 1 and (6) prevent the first equation for every such pair. They
therefore remove the entire Lemma F family, for both parities, regardless
of where the proposed sea pair lies. No bound on \(L\) is needed.

The same argument removes any two-sea horizontal-side support whose
label-pair reduction requires a same-parity nonhorizontal integral
distance. It does not remove other two-sea roles solely because they have
four black cells.

There is also no tilted right angle among three odd label points, or among
three even label points. Indeed, every nonhorizontal same-parity segment
has \(y^2<2|X|\), and every horizontal separation in (3) is at least 32.
Consequently every same-parity segment has slope of absolute value below
one. Two such nonzero segments cannot be perpendicular, since the product
of their slopes has absolute value below one. A vertical segment cannot
occur between distinct label columns. The same reasoning holds for (7).

The following are still unresolved for this placement:

- Opposite-parity vertical rivals. Their vertical gap is
  \(b_f-a_e\), which is not controlled by one coordinate difference in (1).
- Mixed corner triples with two label points of one parity and one of the
  other parity.
- Other two-label mixed supports involving different sea rows.
- Three-label and four-label events from T2.

The existing one-label profile theorem still applies to each chosen
period-zero column. The N1 layout would accept (7) if every remaining T2
event were excluded. Neither this note nor the existing N1 theorem proves
that last assertion.

## 5. Why the independent-slot floor does not contradict this

The arbitrary-law extension RL in `congruence_slot_lists.md` requires a
lower effective support size \(N'\) relative to the full block size \(N\).
In (7), each label has at most \(M\) permitted slots among
\(\Theta(Mh^2)\) period-zero slots. Thus \(N'/N=O(h^{-2})\), even before
the restriction to one profile is considered. Its parameter
\[
R_2=\frac{nN'}{7M_0N(\log h)^3}
\]
does not satisfy the polynomial lower bound used in the price floor.
The construction uses a deterministic dependence between the rows and the
allowed column locations, not a reduction of the count of broad-list
independent events.

## 6. An explicit surviving rival

The unmodified constant-spacing placement is invalid for an infinite family
of parameter pairs, regardless of the filler sea.

Take \(S=2^e\) with \(e\ge5\), put \(q=S^2/4\) and \(h=2q\), and use
columns \(x_r=Sr\) on the whole \(q\)-square. Since
\(q=2^{2e-2}\), the recursion (2) gives, at
\(r=q^2/4+2\),
\[
H_q(r)=(1,q/2+1),\qquad H_q(r+1)=(1,q/2).
\]
Indeed, these are the third and fourth cells of the second quadrant, whose
internal order has an odd number of recursive levels.

Take the odd point of the first label and the even point of the second:
\[
C=(Sr,3),\qquad D=(S(r+1),q+2).
\]
Their difference has horizontal component \(S\), vertical component
\(q-1\), and length \(q+1\), since
\[
S^2+(q-1)^2=4q+(q-1)^2=(q+1)^2.
\]
The vertical segment with the same midpoint and length has endpoints
\[
P=(Sr+S/2,2),\qquad Q=(Sr+S/2,q+3).
\]
All rows lie in \([1,h]\). The segments \(CD\) and \(PQ\) are the
diagonals of a nondegenerate tilted rectangle. The complete label set also
contains the label with rows \(\{2,q+3\}\), in a different column \(z\).
Together with \(P,Q\), that label forms an axis rectangle. The symmetric
difference of the two corner sets consists of four label points, all black.
Consequently the rectangles have the same presentation, whatever fillers
are chosen. This is an actual vertical-rival obstruction, not merely a
necessary arithmetic test.

For \(S=32\), this displayed construction is at \(h=512\). It is found in
the census below. This does not rule out local choices, recoloring, or a
different Hilbert-based placement. It rules out treating (3) alone as a
completed construction.

## 7. A separate bound for label-only tilted right angles

This observation concerns the full-grid coordinates of Section 2. Suppose
every label column is divisible by \(S=2^e\), \(e\ge3\), and increasing
rank differences give horizontal separation at least \(S|r-s|\). The local
choices \(x_r=S(Mr+\xi_r)\) satisfy these assumptions.

**Theorem 2.** If \(S^4\ge64h\), the label points contain no tilted right
angle. This gives an explicit label-only construction in width
\(O(h^{9/4})\). It does not exclude opposite-parity rivals or mixed
label-sea supports.

Proof. Three points of one parity cannot form a right angle: (1) implies
\(y^2<64|X|/S\) for every same-parity segment. Since \(|X|\ge S\), its
slope has absolute value strictly below \(8/S\le1\).

If both endpoints have parity opposite to the vertex, both vertical leg
components are odd, while both horizontal components are even. Their dot
product is odd and cannot vanish.

It remains to consider one same-parity leg \((X_1,Y_1)\) and one
opposite-parity leg \((X_2,Y_2)\). Here \(Y_2\) is odd. For a tilted right
angle, \(X_1,X_2,Y_1\) are nonzero. If \(X_2=0\), orthogonality forces
\(Y_1=0\) and the angle is axis-aligned. Orthogonality gives
\[
X_1X_2=-Y_1Y_2.
\]
Since both horizontal components are divisible by \(S\), and \(Y_2\) is
odd, \(S^2\mid Y_1\). Thus \(|Y_1|\ge S^2\). By (1),
\[
|X_1|>\frac{S}{64}Y_1^2,
\]
and \(|X_2|\ge S\). Consequently
\[
|Y_2|=\frac{|X_1X_2|}{|Y_1|}
>\frac{S^2}{64}|Y_1|\ge\frac{S^4}{64}\ge h,
\]
contradicting the strip height.

Choosing the least power of two \(S\ge\max\{8,(64h)^{1/4}\}\) gives
\(S=O(h^{1/4})\) and the stated span. At fixed \(S=32\), the theorem
explains why label-only tilted angles are absent throughout the small
census range. It gives no asymptotic conclusion at constant \(S\).

## 8. Checks and remaining target

The accompanying script `check_hilbert_placement.py` checks the recursive
ordering, exact integer distances, and local choices at small sizes. The
proofs of (1) and Theorem 1 do not depend on those finite checks.

The ordering properties and (1) passed all pair checks through \(q=32\).
The no-integral-distance conclusion passed exact integer checks through
\(q=16\), for private-choice counts \(M=1,2,7\), both in the full-grid
coordinates and in the period-seven profile coordinates.

The script also counted all opposite-parity pairs with integral distance
\(L<h\) in the constant-spacing full-grid placement. It enumerates the
integer factorizations
\[
uv=(X/2)^2,\qquad L=u+v,\qquad y=v-u,
\]
with \(u,v\) of opposite parity. No floating-point square-root test is
used. These are candidate rivals; the census does not test every pair's
vertical completion against the strip boundary.

| Stride | Height | Candidate pairs | Mean incidence per label | Maximum incidence |
|---:|---:|---:|---:|---:|
| 32 | 128 | 0 | 0 | 0 |
| 32 | 256 | 0 | 0 | 0 |
| 32 | 512 | 5,565 | 0.16983 | 2 |
| 32 | 1,024 | 26,501 | 0.20219 | 4 |
| 32 | 2,048 | 155,479 | 0.29655 | 5 |
| 64 | 128 to 1,024 | 0 | 0 | 0 |
| 64 | 2,048 | 42,780 | 0.08160 | 2 |

The early zeros are forced by a general 2-adic obstruction, rather than
evidence for a new asymptotic bound. If \(2^e\mid X\) and \(y,L\) are odd,
one of \(u=(L-y)/2\), \(v=(L+y)/2\) is odd and the other is divisible by
\(2^{2e-2}\). Hence
\[
L=u+v\ge2^{2e-2}+1=S^2/4+1.
\]
No such pair can occur when \(h\le S^2/4+1\).

The concrete next question is whether the unused choice in (7), or a
different rank-preserving choice satisfying (6), can exclude the remaining
T2 events with \(M=(\log h)^b\) for some \(b<1.3108172\). A constant \(M\)
would give a quadratic core, but no such completion is proved here.
