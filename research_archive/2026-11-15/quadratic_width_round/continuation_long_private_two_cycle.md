# Long directed P two-cycles with a linear half-factor

15 November 2026. There are actual Hilbert two-cycles whose slot gap
and smaller half-factor are both proportional to the ambient height.
They defeat the nonempty own-row private-slot filler at arbitrarily
large heights. They also survive any sublinear cutoff applied to
their own gaps or half-factors, and any sublinear diagonal band.

This does not prove survival of the full small-factor endpoint
deletion. An endpoint could participate in a different event with
a small factor. That union-of-events condition remains unchecked.

Independent review checked the two macro ranks, both orientation
maps, the scale and congruences, owners, midpoint exclusion, and
height comparison. The companion checker passes 720 local filler
assignments across eight full-grid and H7 instances.

## 1. Parameters and a fixed inner pair

Fix \(M\ge1\). Use either \(D=2\) with \(8\mid S\), or
\(D=28\) with \(S=6272\sigma\). Put
\[
 C=(SM)^2,\qquad Y_0=C-1,\qquad L_0=C+1.
\]
The primitive triple \((2SM,Y_0,L_0)\) has smaller half-factor
one. Its scaled copies below have a growing half-factor.

For every sufficiently large power of two \(L\), the Hilbert
square \(H_L\) contains the fixed side-eight construction from
[the private-stub obstruction](continuation_private_parity_stub_obstruction.md).
Write its origin as \((I_0,J_0)\), where \(J_0-I_0=C/D\),
and its rank start as \(r_0\). Its local ranks 2 and 4 give two
cells \(w_1,w_2\) satisfying
\[
 w_{1x}+w_{1y}=w_{2x}+w_{2y},\qquad
 w_{2y}-w_{1x}=w_{1y}-w_{2x}=C/D-1.
\tag{1}
\]
Both inner orientations, identity and negative swap, satisfy (1).
The inner ranks are \(r_0+2,r_0+4\).

## 2. A second scale makes the rank gap grow

The standard side-32 Hilbert order has
\[
 H_{32}(292)=(6,20),\qquad H_{32}(908)=(20,6).
\tag{2}
\]
Both cells have identity terminal orientation. For example, their
base-four addresses are 10210 and 32030; each has an even number
of swaps and an even number of negative swaps.

Inside a square of side \(B=32L\), take the two ranks
\[
 r_A=292L^2+r_0+2,\qquad
 r_B=908L^2+r_0+4.
\]
Their cells are
\[
 p=(6L+w_{1x},20L+w_{1y}),\qquad
 q=(20L+w_{2x},6L+w_{2y}).
\]
Equation (1) gives
\[
 p_x+p_y=q_x+q_y,\qquad
 q_y-p_x=p_y-q_x=C/D-1.
\tag{3}
\]
The rank gap is
\[
 d=r_B-r_A=616L^2+2=2t,
 \qquad t=308L^2+1.
\tag{4}
\]
The integer \(t\) is odd, and \(t\equiv1\pmod D\) for
both \(D=2\) and \(D=28\).

## 3. The outer translation realizes both directed P edges

Embed this side-\(B\) square with origin \((I,J)\), where
\[
 T=J-I=\frac{308}{D}Y_0L^2.
\tag{5}
\]
For power-of-two \(L\ge64\), \(T/B\) is an even integer.
The usual two diagonal macro-cells therefore provide a containing
block of identity or negative-swap orientation. A negative swap
preserves both equalities in (3), because the two coordinate sums
are equal. Thus either orientation works.

For both opposite-parity roles, the signed row difference is
\[
 D(T+C/D-1)+D-1
 =DT+C-1
 =Y_0t.
\]
At equal private offsets, the horizontal difference is
\(SMd=2SMt\). Therefore the two directed edges both have
\[
 X=2SMt,\qquad Y=Y_0t,\qquad
 L_{\mathrm{hyp}}=L_0t,
\tag{6}
\]
and smaller half-factor
\[
 a=(L_{\mathrm{hyp}}-Y)/2=t.
\tag{7}
\]

## 4. In-strip completions and external owners

Put \(z=(t-1)/D=(308/D)L^2\). For an odd endpoint with
index \(i\), and an even endpoint with index \(j\), the common
rows are
\[
 D(i-z),\qquad 1+D(j+1+z).
\tag{8}
\]
Their owner is
\[
 (i_*,j_*)=(j+1+z,i-1-z).
\tag{9}
\]
This holds for either direction.

Choose the least suitable even macro anchor, so that
\(2z+B\le I<2z+4B\). Choose
the ambient side, still a power-of-two multiple of \(B\), at
least four times \(J+B+z\). It can be chosen within a fixed
factor of that quantity. Then all rows in (8) are in the strip,
and the ambient height satisfies
\[
 h=\Theta_{S,M,D}(L^2)=\Theta_{S,M,D}(t).
\tag{10}
\]
Both endpoints and owners have positive margins proportional to
\(h\), with constants depending on the fixed parameters.

The midpoint rank \((r_A+r_B)/2\) lies inside the outer block.
Since \(z>B\), the lower common row lies below every row of
that block and the upper common row lies above every row of that
block. In particular neither can be an own-row stub at the midpoint.
The owner in (9) is outside the block in both coordinates, so its
private interval cannot contain the midpoint column.

Every label is double somewhere in its private interval. Choose
any double offset of the first endpoint. The other endpoint's
same-offset slot is nonempty. Its even row triggers one directed
edge, while its odd row triggers the other. Equations (8)--(9)
then give an actual two-rectangle collision for every possible
own-row parity filler.

## 5. What survives, and what is not yet checked

The slot gap \(Md\), the half-factor \(a=t\), and the
hypotenuse are all \(\Theta(h)\). Thus the displayed edges
pass any filters of the form \(q>h^{\gamma+o(1)}\) and
\(a>h^{\delta+o(1)}\), for fixed \(\gamma,\delta<1\).
This includes the current numerical scales \(h^{2/3-o(1)}\)
and \(h^{1/3-o(1)}\).

The endpoint diagonals are \(T+O(L)=\Theta(h)\). The owner
diagonals are \(-T-2z+O(L)=-\Theta(h)\). Hence all these
labels survive a diagonal band of width \(o(h)\).

These facts do not establish survival of a deletion that removes
every label involved in any small-factor event. The same endpoint
could have another P neighbor with a small half-factor. Nor have
the full common square filters or the multiple-leg band union been
checked for this family. The unconditional result is the long,
genuine directed two-cycle and its private-filler obstruction.
