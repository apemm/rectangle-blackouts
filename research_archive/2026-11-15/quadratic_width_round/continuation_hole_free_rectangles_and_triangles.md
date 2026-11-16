# Hole-free orders for filtered rectangles and diagonal triangles

15 November 2026. There are explicit bijective orders of genuine rectangular
and triangular label sets with a uniform square-root locality bound. No padded
labels or deleted rank positions occur. The constants are independent of the
side length and, for the triangles, of the width of a removed diagonal band.

The construction addresses occupancy and same-parity locality. It does not
solve the new P constraints, the remaining mixed supports, or the joins between
different filled profile cores.

## 1. A rectangular recursion

Write \(R_{a,b}=[0,a-1]\times[0,b-1]\cap\mathbb Z^2\). Assume
\[
 \max(a,b)\le 2\min(a,b)+2.                                      \tag{1}
\]
There is a bijection \(H_{a,b}:[0,ab-1]\to R_{a,b}\) satisfying
\[
 \|H_{a,b}(r)-H_{a,b}(s)\|_\infty^2\le81|r-s|.                  \tag{2}
\]
If \(|a-b|\le1\), the constant 81 can be replaced by 32.

The reference entry and exit corners are \((0,0)\) and \((a-1,0)\).
These need not be the actual endpoints of the order. For example, the two
reference corners coincide on a vertical terminal line. The proof uses
distances to these reference corners, not exact endpoint identities.
If one side has length one, enumerate that line. Otherwise put
\(a_0=\lfloor a/2\rfloor,a_1=\lceil a/2\rceil\), and similarly
\(b_0,b_1\). Concatenate these four recursive orders:
\[
\begin{array}{c|c|c}
 &\text{recursive dimensions}&\text{coordinate map}\ \hline
1&(b_0,a_0)&(u,v)\mapsto(v,u)\\
2&(a_0,b_1)&(u,v)\mapsto(u,v+b_0)\\
3&(a_1,b_1)&(u,v)\mapsto(u+a_0,v+b_0)\\
4&(b_0,a_1)&(u,v)\mapsto(a-1-v,b_0-1-u).
\end{array}                                                     \tag{3}
\]
These are disjoint quadrants covering the rectangle. Their prescribed joins
have distance one. Each child again satisfies (1): if the smaller parent
side is \(s\), its larger child side is at most \(s+1\), and its smaller
child side is at least \(\lfloor s/2\rfloor\). Thus its larger side is
at most twice its smaller side plus two. Every terminal line has length at
most four. All coordinate maps in (3) preserve the infinity norm.

Let \(\ell\) be the larger side of a nonterminal rectangle and \(s\ge2\)
its smaller side. Every child has at least
\[
 \lfloor s/2\rfloor\lfloor\ell/2\rfloor
 \ge \frac{(\ell-1)^2}{16}                                    \tag{4}
\]
cells. Indeed, \(\ell-1\le2s+1\le8\lfloor s/2\rfloor\), while
\(\lfloor\ell/2\rfloor\ge(\ell-1)/2\).

For a cell at local rank \(r\), follow first children until it leaves the
first child or reaches a terminal line. The prescribed entry corner stays
fixed during this descent. At the first departure, the prefix contains a
whole child, so (4) bounds the distance to the entry corner. On a terminal
line the distance is at most three. The same argument with last children
gives, for a rectangle containing \(N\) cells,
\[
 d_\infty(H(r),\text{entry})\le4\sqrt{r+1},\qquad
 d_\infty(H(r),\text{exit})\le4\sqrt{N-r}.                    \tag{5}
\]

For ranks \(r<s\), take their lowest common recursive rectangle. If their
children are not consecutive, an intervening child and (4) give the stronger
bound \(16(s-r)\) in (2). For consecutive children, let \(u\) be the
number of cells from \(r\) to the end of its child, and \(v\) the number
from the start of the next child through \(s\). Then \(u,v\ge1\) and
\(u+v=s-r+1\). Equation (5) and the distance-one prescribed join give
\[
 d_\infty(H(r),H(s))
 \le4\sqrt u+1+4\sqrt v
 \le\sqrt{32(s-r+1)}+1\le9\sqrt{s-r}.
\]
If both points are in one terminal line, its length is at most four and the
same conclusion holds directly. This proves (2).

For near-square rectangles every child remains near-square. A direct even/odd
check improves (4) to \((\ell-1)^2/5\); terminal lines have length at most
two. Thus (5) has coefficient \(\sqrt5\). The final coefficient is
\((\sqrt{20}+1)^2<32\), proving the stated improvement.

## 2. A triangular recursion with an absolute constant

Let
\[
 T_n=\{(u,v)\in\mathbb Z_{\ge0}^2:u+v<n\},\qquad
 t_n=|T_n|=n(n+1)/2.
\]
Use the norm
\[
 \|(u,v)\|_\triangle=\max(|u|,|v|,|u+v|).
\]
There is a bijection \(G_n:[0,t_n-1]\to T_n\) with endpoints
\((0,0),(n-1,0)\) and
\[
 \|G_n(r)-G_n(s)\|_\triangle^2\le49|r-s|.                    \tag{6}
\]
Consecutive cells have triangular-norm distance exactly one.

For \(n=1\) use the single cell. For \(n\ge2\), put
\(a=\lceil n/2\rceil\), \(k=\lfloor n/2\rfloor\), and concatenate
\[
\begin{array}{c|c|c}
 &\text{recursive triangle}&\text{coordinate map}\ \hline
1&T_a&(u,v)\mapsto(v,u)\\
2&T_k&(u,v)\mapsto(u,v+a)\\
3&T_{a-1}&(u,v)\mapsto(a-1-v,a-1-u)\\
4&T_k&(u,v)\mapsto(u+a,v).
\end{array}                                                     \tag{7}
\]
The empty third child when \(n=2\) is omitted. The first child is
\(u+v<a\); the second and fourth have \(v\ge a\) and \(u\ge a\).
The third is the remaining inverted triangle. Thus (7) is a disjoint exact
partition, for both parities of \(n\).

All maps preserve \(\|\cdot\|_\triangle\). The endpoints of consecutive
nonempty children differ by triangular norm one. For example, the middle
join is between \((k-1,a)\) and \((a-1,a-1)\), and the last is between
\((a-1,1)\) and \((a,0)\). The first and last endpoints are the prescribed
parent endpoints. This proves the endpoint and consecutive-cell claims by
induction.

For \(n\ge3\), every child has at least
\[
 \frac{(n-1)^2}{9}                                             \tag{8}
\]
cells. When \(n=2a\), the smallest child has \(a(a-1)/2\) cells, and
\(2(2a-1)^2/[a(a-1)]\le9\) for \(a\ge2\). When \(n=2a-1\), the
corresponding ratio is \(8(a-1)/a<8\). Treat \(n\le2\) as terminal.
The diameter of \(T_n\) in the triangular norm is \(n-1\).
The first-child and last-child arguments used in (5) therefore give
\[
 d_\triangle(G_n(r),(0,0))\le3\sqrt{r+1},\qquad
 d_\triangle(G_n(r),(n-1,0))\le3\sqrt{t_n-r}.
\]
At the lowest common parent, nonconsecutive children give \(9(s-r)\).
Consecutive children give
\(3\sqrt u+1+3\sqrt v\le7\sqrt{s-r}\). The terminal case is direct.
This proves (6).

## 3. Removing a fixed diagonal band without padding

In the genuine square label grid \([0,n-1]^2\), fix any integer
\(1\le c<n\). The upper remaining triangle
\[
 U_{n,c}=\{(i,j):0\le i,j<n,\ j-i\ge c\}
\]
is the image of \(T_{n-c}\) under
\[
 (u,v)\mapsto(i,j)=(u,c+u+v).                                  \tag{9}
\]
For differences, the infinity norm after (9) is at most the triangular norm
before it. Hence this genuine label triangle has locality constant 49,
independent of \(c\). Reflection gives the same result for \(i-j\ge c\).
Each triangle occupies one complete arithmetic interval. The removed band
contains at most \((2c-1)n\) labels.

This gives a limited but noncircular short-P exclusion. Suppose physical rows
are \(a_0+Di\) and \(b_0+Dj\), with opposite parity, and distinct occupied
columns have stride \(S\), where \(4\mid S\). A P candidate with slot gap
\(1\le q\le Q\) has an odd vertical gap \(Y\) satisfying
\[
 Y\le\frac{S^2Q^2}{4}-1.                                     \tag{10}
\]
Indeed, its odd integer hypotenuse \(L\) gives positive integers
\((L-Y)/2,(L+Y)/2\) with product \((Sq/2)^2\). Their difference is
\(Y\), which is at most their product minus one.

Within either ordered triangle, even after permutations inside blocks of at
most \(b\) consecutive ranks, candidate rank distance is at most
\((2b-1)Q\). Thus each coordinate changes by at most
\(7\sqrt{(2b-1)Q}\). If
\[
 Dc>|b_0-a_0|+7D\sqrt{(2b-1)Q}+S^2Q^2/4-1,                 \tag{11}
\]
both directed cross-row gaps exceed (10). There is no such P candidate
inside either run. Here \(S,b,Q,c\) are fixed constants independent of
height. The locality constant 49 is chosen before \(c\), so (11) creates
no feedback through the stride. The deleted labels number \(O(h)\).

This assertion concerns P pairs internal to a run. P pairs crossing a join,
longer slot gaps, and other support families still require separate treatment.
It also concerns genuine equally spaced row lists. Applying (9) after a
nonlinear compression of filtered rows requires a new argument for the shape
of the removed physical band.

## 4. Square-filtered row lists have bounded gaps

The square filters in the filled period-seven profiles have a useful stronger
property than their \(O(\sqrt h)\) cardinality. Consider any fixed collection
of \(B\) tests of the form
\[
 j(r-c+j)\text{ is a square},\qquad
 j(c-r+j)\text{ is a square},                                 \tag{12}
\]
where \(j\) is a fixed positive integer and each center \(c\) is within
a fixed distance \(C_0\) of either ambient boundary. Put
\(J_{\max}=\max j\) over the fixed collection. The centers may depend
on \(h\). Only the applicable sign with a positive argument is needed.
Fix a row residue modulo \(D\).

Write \(j=t u^2\) with \(t\) squarefree. The integer solutions of
\(j n\) square have \(n=t v^2\). In the part where \(n\ge K\), two
successive solutions differ by at least \(2\sqrt K\). Choose
\[
 K=(D(B+1))^2,
\]
and retain only rows whose distance from either boundary is at least
\(C_0+J_{\max}+K+1\). Wrong-sign arguments are then negative. For all
tests relevant there, the positive argument in (12)
is at least \(K\). Each individual test therefore removes at most one row
from any \(B+1\) consecutive members of the residue class, whose total span
is \(DB\). Their union removes at most \(B\) members. Consequently every
such block contains a good row. If \(r_0<r_1<\cdots\) are the good rows,
\[
 r_{i'}-r_i\le D(B+1)(i'-i)\quad(i<i').                       \tag{13}
\]
There are also at most \(DB\) units of unused row length at either end of
the residue interval.

Each test removes \(O(\sqrt h)\) rows, uniformly in its boundary center.
Thus every fixed residue has \(h/D-O(\sqrt h)-O(1)\) good rows. Two such
lists have sizes satisfying (1) for all sufficiently large \(h\).
Applying the rectangular order to their index product and then using (13)
gives an exact order of every good row pair with
\[
 \max(|\Delta r_A|,|\Delta r_B|)^2
 \le81D^2(B+1)^2\,|\Delta\mathrm{rank}|.                     \tag{14}
\]
There are no missing rank positions caused by the square filters.

For the archived H7 profile cover, take the union of the finitely many
boundary-overhang filters over all chosen profiles. Their number and their
boundary offsets are absolute constants. Enlarge the fixed bulk margin as
just described, assign each ordinary row-residue pair to one of its safe
profiles, and order its complete good-row Cartesian product by (3). There
are only constantly many such products. Their excluded labels still number
\(O(h^{3/2})\); the extra fixed boundary margin contributes only \(O(h)\).

With H7 stride \(S=8D^2\sigma\), it suffices to choose a fixed power of two
\[
 \sigma>\frac{81}{16}(B+1)^2(2b-1)                            \tag{15}
\]
to preserve the strict same-parity inequality \(Y^2<2|X|\) under arbitrary
permutations in rank blocks of size at most \(b\). If all arithmetic slots
of one such run are occupied, the archived full-occupancy argument removes
FW there as well. This resolves the padding issue for these complete
filtered Cartesian products. It does not resolve P, the other mixed
supports, or a label partition that is not a Cartesian product.

## 5. Verification and scope

`check_hole_free_orders.py` independently computes each rank by the explicit
recursive partitions. It checks bijectivity, rectangular endpoint errors,
exact triangular endpoints, prefix/suffix bounds,
and all pairs in 172 rectangular and 32 triangular cases. It also checks
40,000 pairs at larger sizes, including sizes above one million.

The saved run passes 1,036,260 rectangular and 973,896 triangular pair checks.
The largest observed ratios are 16 and \(900/101\), respectively. These
finite ratios are not claimed optimal. The uniform claims follow from
(4), (5), and (8), not from the finite checks.

The positive output is a genuine-label, hole-free local order with absolute
constants, plus a fixed-band short-P repair on a genuine square grid. A full
quadratic construction still needs compatible solutions of the remaining
P and mixed families, and valid joins between the constantly many runs.

Independent review: the rectangular and triangular recursions, locality
constants, and band geometry passed a separate proof audit. The square-filter
gap argument and its H7 scope also passed a separate audit. The reference-corner
convention and the even-factor wording in (10) were clarified during review.
A further independent review added \(J_{\max}\) to the general filter margin,
so wrong-sign affine arguments cannot remain small and positive.
