# Refinement onto spacing four preserves the same-parity exclusions

15 November 2026. A row-step-four cap core can be refined onto every
fourth column at a fixed width cost. The refined functions have a few
45-degree pairs, but these pairs cannot form a right triangle. A stronger
cone lemma excludes every nondegenerate same-parity side/diagonal mixed
four-support. These are geometric statements about the inserted points.
They do not prove a complete sea construction or its end collars.

This replaces the geometric part of the failed
[spacing-two sea candidate](continuation_even_lattice_refinement.md).
That note's unparked cross-parity triangle remains a valid obstruction
to its proposed sea extension.

## 1. The refinement and its only exceptional pairs

Let the total coarse row functions \(f_0,f_1\) have opposite row parities.
For each \(\alpha\), assume
\[
 |f_\alpha(r)-f_\alpha(s)|^2\le C^2|r-s|,
 \qquad |f_\alpha(r+1)-f_\alpha(r)|\le4,
 \tag{1}
\]
and assume all values of that function have one fixed residue modulo four.
Choose an integer
\[
 M\ge\max\{2,C^2/4\}.
 \tag{2}
\]
At fine rank \(t\), with physical column \(x=4t\), use the total options
\[
 F_\alpha(t)=f_\alpha(\lfloor t/M\rfloor).
 \tag{3}
\]
For distinct fine ranks, write \(X=4|t-u|\). Every same-parity pair satisfies
\[
 |F_\alpha(t)-F_\alpha(u)|^2\le2X,
 \tag{4}
\]
except possibly when \(t,u\) are the consecutive ranks \(Mr-1,Mr\)
across a coarse seam. The exceptional nonzero vector is then
\((\pm4,\pm4)\).

To prove this, let \(k\) be the coarse-rank distance. For \(k=0\) the row
difference vanishes. For \(k=1\) its square is at most 16, so (4) holds
whenever \(|t-u|\ge2\). The remaining case is exactly a seam pair.
For \(k\ge2\),
\[
 |t-u|\ge M(k-1)+1,
 \qquad C^2k\le2C^2(k-1)\le8M(k-1)<8|t-u|.
\]
The fixed residue assumption makes every nonzero adjacent coarse
increment equal to \(4\) or \(-4\).

It follows that every same-parity pair lies in the closed horizontal cone
\[
 |\Delta y|\le |\Delta x|.
 \tag{5}
\]
Indeed, a pair satisfying (4) has \(X\ge4\), hence
\(\sqrt{2X}<X\). Equality in (5) is possible only at a seam pair.
Because \(M\ge2\), two seam edges never meet at a common fine rank.

## 2. Integral distances and right triangles

Every nonhorizontal same-parity pair has nonintegral Euclidean length.
For a pair satisfying (4),
\[
 X^2<X^2+(\Delta y)^2\le X^2+2X<(X+1)^2.
\]
An exceptional pair has length \(4\sqrt2\).

There is also no right triangle whose three vertices all use one parity.
Each nonzero side has nonzero horizontal component, because there is at
most one point of that parity in each column. If two legs are perpendicular,
their slopes have product \(-1\). By (5), their absolute slopes are at most
one. They must therefore have slopes \(+1\) and \(-1\), so both legs must
be exceptional seam pairs.

If their horizontal components have the same sign, their other endpoints
occupy the same column, which is impossible. If the signs differ, the two
seam edges are consecutive fine edges meeting at the right-angle vertex.
This is impossible by the final observation of Section 1.

In particular, no hidden rectangle can have all four vertices in one
parity. These conclusions survive every erasure or choice of the available
points, since the total functions already satisfy the assertions.

## 3. A cone lemma for mixed four-supports

The next fact needs only (5), without the seam information.

**Cone lemma.** Let \(\mathcal B\) be a set with at most one point per
column and with
\[
 |y_P-y_Q|\le |x_P-x_Q|\quad(P,Q\in\mathcal B).
 \tag{6}
\]
Then \(\mathcal B\) cannot contain a nondegenerate four-point support in
which one black pair is the opposite side of a displayed pair and the
other black pair is the complementary diagonal for that displayed pair.

Translate the black side endpoints to \(A=0,B=u\). Write the displayed
pair as \(t,u+t\), so \(u\cdot t=0\). If the second black pair is a
diagonal completing that displayed diagonal, it has the form
\[
 C=t+(u-v)/2,\qquad D=t+(u+v)/2,
 \qquad |u|=|v|.
 \tag{7}
\]
Orient \(u\) and \(v\) to have positive horizontal components. This only
orders each pair. Under the light-cone map
\[
 (x,y)\longmapsto(x+y,x-y),
\]
their images \(U,V\) have nonnegative coordinates and equal norm.
If \(U\ne V\), their difference has two strictly opposite signs: equal
norm forbids one distinct nonnegative vector from dominating the other
coordinatewise. Thus the image of \(w=(u-v)/2\) has strictly opposite signs.

The image \(T\) of \(t\) satisfies
\[
 U_1T_1+U_2T_2=0.
\]
Since \(U\ne0\) is nonnegative, \(T\) has weakly opposite signs, or is
zero. This includes a zero coordinate when \(u\) lies on a cone boundary.
One of \(T+w\) and \(T-w\), in light-cone coordinates, consequently has
two strictly opposite signs. But these are the coordinate images of
\(C-A\) and \(D-B\). One of those pairs satisfies
\(|\Delta y|>|\Delta x|\), contradicting (6).

Finally, \(U=V\) means \(v=u\) in the chosen orientation. Formula (7)
then makes \(\{C,D\}=\{t,u+t\}\): the purported black diagonal is the
displayed pair itself. It does not define a second nondegenerate rectangle.
The unoriented case \(v=-u\) is the same case with the endpoints swapped.
This excludes the degeneracies without assuming that the cone is open.

Apply the cone lemma separately to each refined parity graph. Every
all-one-parity mixed four-support is absent. A mixed support using both
parities is outside this conclusion.

## 4. Application to total cap functions and exact occupancy

Start with raw Hilbert coordinate lists of physical row step four.
Adjacent raw values differ by at most four. Clipping preserves this
bound. A cap replacement sets one coordinate to its common endpoint
value. Its two endpoint values therefore remain unchanged, and its
internal increments vanish. Disjoint replacements preserve the adjacent
increment bound, including comparisons across cap boundaries.

The total virtual functions from
[the cap palette construction](continuation_virtual_cap_palettes.md)
therefore satisfy (1), with a fixed physical Hölder constant. Their
values remain in their fixed residue classes modulo four.

At least one option is good at every coarse rank, hence at every fine
rank. Retain a genuine double only at its designated coarse column
\(4Mr\). Fill every other fine column \(4t\) with exactly one good
virtual option. Do not replicate a genuine double at its other copies.
This gives full occupancy of the spacing-four lattice while preserving
the number of genuine double labels and all conclusions of Sections 1–3.

The width and the number of intrinsically one-option ranks increase by
at most the fixed factor \(M\). Any existing exceptional-label count is
unchanged, because the extra occupied columns are singletons. Whether a
particular bad-row theorem supplies the required good sets for a new sea
profile remains a separate hypothesis.

The construction does not allow an arbitrary permutation of the coarse
objects afterward. That can destroy the adjacent increment condition.
Any choice system using such permutations needs another interpolation
argument or a direct proof of the same bounds.

## 5. Scope of the geometric gain

The spacing-four core has no nonhorizontal same-parity integral pair,
no same-parity right triangle, no same-parity hidden rectangle, and no
same-parity side/diagonal mixed four-support. This is enough to reuse
those particular exclusions in a separately proved sea classification.

It does not remove cross-parity P constraints, cross-parity mixed
supports, or collisions of parked triples. It also does not prove the
classification of the proposed low-row sea profiles, the corresponding
R2s bad-row estimate, or the filled end collars. Those dependencies must
be checked before asserting a valid complete board or quadratic-width
threshold.

Independent review: the complete written geometry proof passed a separate
review, including the closed-cone boundary case, the degenerate diagonal
case, the isolated seams, and cap adjacent-increment preservation.
