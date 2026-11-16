# Random good caps fill a row-filtered Hilbert core

15 November 2026. A random translation inside one padded Hilbert square gives
a fully occupied arithmetic core with no black point in a prescribed bad
row. The additional relocated labels number only
\(O(nb\log(2n))\), where \(n\) is the larger row-class size and \(b\)
is the total number of bad rows. The coordinate Hölder constant does not
increase.

Padding slots are filled by good-row singletons, not left empty. Selected
Hilbert squares are filled by singleton caps at a good common endpoint row.
This repairs the arbitrary bad-row obstruction at a cost that is
subquadratic for the current R2s exceptional-row bound. It introduces new
singleton P and mixed supports, which still require control.

## 1. The cap lemma

Let \(f_0,f_1\) be two real coordinate functions on a finite ordered rank
set, with
\[
 |f_\alpha(r)-f_\alpha(s)|\le C\sqrt{|r-s|}
 \qquad(\alpha=0,1).                                      \tag{1}
\]
Suppose \(I=[\ell,u]\) is a rank interval with
\(f_\alpha(\ell)=f_\alpha(u)=v\). Replace every column of \(I\)
by the single point of parity \(\alpha\) at value \(v\). Outside
\(I\), retain any subsets of the original points. Then the surviving
points of each parity still satisfy (1).

For a point outside \(I\), compare with the endpoint of \(I\) facing
that point. Its distance in ranks is no larger than the distance from any
rank inside \(I\). Two points inside the cap have equal values. The same
argument applies to any collection of pairwise disjoint cap intervals:
between two caps of the same parity, use their two facing endpoints. Their
rank distance is at most the distance between the two selected cap points.

The conclusion concerns the surviving partial parity functions. There need
not be a point of each parity at every rank.

## 2. Embed and clamp the row rectangle

Let the genuine labels be the complete product
\[
 [0,n_0-1]\times[0,n_1-1],\qquad n=\max(n_0,n_1).
\]
Each coordinate has a prescribed good set \(G_\alpha\), assumed nonempty.
Write \(b_\alpha=n_\alpha-|G_\alpha|\) and
\(b=b_0+b_1\). Physical rows are
\(\rho_0+D i\) and \(\rho_1+D j\), with opposite parity and fixed step
\(D\). The symbols \(b_\alpha\) count bad rows.

Choose a power of two \(N\) with \(4n\le N<8n\), and choose
independently and uniformly
\[
 U_\alpha\in\{1,\ldots,N-n_\alpha-1\}.
\tag{2}
\]
Use the standard Hilbert order \(H_N\) of the entire \(N\)-square.
The genuine row rectangle occupies coordinates
\(U_0+[0,n_0-1]\) and \(U_1+[0,n_1-1]\). Every genuine label occurs
at exactly one rank.

Let \(l_\alpha=\min G_\alpha\), \(u_\alpha=\max G_\alpha\), and
define the coordinate functions
\[
 f_\alpha(r)=
 \operatorname{clip}(H_N(r)_\alpha-U_\alpha,
                    l_\alpha,u_\alpha).
\tag{3}
\]
Clipping is 1-Lipschitz. The standard Hilbert bound therefore gives
\[
 |f_\alpha(r)-f_\alpha(s)|^2<16|r-s|\quad(r\ne s).
\tag{4}
\]
Every original good coordinate is unchanged. A coordinate outside its
genuine range clips to a good boundary value. Some original bad coordinates
also clip to a good boundary value, which only helps fill their slots.

Each nontrivial dyadic Hilbert square is a consecutive rank interval. Its
entry and exit are adjacent corners, so one coordinate has a common value
at both endpoints. Choose that coordinate as its cap coordinate. After
clipping, the endpoint values remain equal. For a leaf choose either
coordinate by a fixed convention.

Call a node good-cap when this clipped common value belongs to the
corresponding \(G_\alpha\). The root is always good-cap: its common
coordinate is either 0 or \(N-1\), and (2) places both outside the genuine
coordinate interval.

## 3. Expected area of the caps

Fix a dyadic node and its cap coordinate \(c\), of parity \(\alpha\).
It is bad-cap only when \(c-U_\alpha\) is an original bad index between
the first and last good indices. Each bad index permits at most one choice
of \(U_\alpha\). Thus
\[
 \Pr(\text{node is bad-cap})
 \le\frac{b_\alpha}{N-n_\alpha-1}
 \le\frac{b}{N-n-1}.                                      \tag{5}
\]
At every fixed depth, the node areas sum to \(N^2\). There are
\(1+\log_2N\) depths, so
\[
 \mathbb E\sum_{\text{bad-cap nodes }Q}|Q|
 \le\frac{N^2b(1+\log_2N)}{N-n-1}
 =O(nb\log(2n)).                                         \tag{6}
\]
No independence between nodes is required.

Consider every rank at which both clipped values in (3) are bad. Its leaf
is bad-cap. Ascend to the first good-cap ancestor, which exists because the
root is good-cap. Take the inclusion-maximal nodes among all these chosen
ancestors. They are disjoint and cover every rank with two bad clipped
values. Each selected node has a bad-cap child, and its area is four times
that child's area. Therefore
\[
 \sum_{\text{selected caps }Q}|Q|
 \le4\sum_{\text{bad-cap nodes }Q}|Q|.                     \tag{7}
\]
Choose offsets for which the sum in (6) is at most its expectation. The
selected cap area is then \(O(nb\log(2n))\).

The choice of offsets has an exact finite derandomization. For each parity
\(\alpha\), let \(w_\alpha(c)\) be the sum of the areas of all dyadic
nodes whose raw cap coordinate is \(c\) in that parity. If
\(B'_\alpha\) is the set of bad indices between \(l_\alpha\) and
\(u_\alpha\), then the total bad-cap area is exactly
\[
 W(U_0,U_1)=W_0(U_0)+W_1(U_1),\qquad
 W_\alpha(U)=\sum_{j\in B'_\alpha}w_\alpha(U+j).             \tag{7a}
\]
Choose each offset separately to minimize its one-dimensional sum over the
finite interval in (2). Each minimum is at most its mean, so this deterministic
choice satisfies (6). Searching all pairs of offsets is unnecessary.

## 4. Fill every slot and count the relocated labels

Fill every selected cap by its good cap singleton. In the remaining ranks:

* At a genuine label with two original good coordinates, retain its double.
* At every other noncap rank, use the even clipped coordinate whenever it
  is good. Otherwise use the odd clipped coordinate.

If a genuine label has one original good coordinate, its clipped coordinate
is good, so the second rule can fill its slot. It might instead choose a
new good even boundary value when the original even coordinate was bad and
clipped outward; that label is already included in the relocation set.
At a padding rank, at least one coordinate is outside its genuine range and
clips to a good boundary row.
The only remaining case would have two bad clipped coordinates. It was
covered by a selected cap. Thus every rank is nonempty. Every surviving row
is good, and the cap lemma gives (4) for all surviving same-parity points.

Relocate each genuine label that is incident to a bad row, and every
remaining genuine label whose rank was covered by a cap. The first set has
size at most \(n_1b_0+n_0b_1\le nb\), and the second has size at most
the selected cap area. Hence the total is
\[
 n_E=O(nb\log(2n)).                                       \tag{8}
\]
All other genuine labels occur exactly once as doubles. Padding and caps
are singletons and introduce no duplicate row-pair label.

There are \(N^2=O(n^2)\) occupied arithmetic slots. If the intervening
profile sea and collars contribute one black point per ordinary column,
then the core has one point per column plus one point for each unrelocated
double. An external filled construction for the \(n_E\) relocated pairs
restores the exact total \(m+n_0n_1\). Applying this to the fixed family of
residue blocks gives \(m+q_h\), subject to the cited external relocation
and join conditions.

## 5. Consequences for the H7 core and their limits

Assume the good rows satisfy the profile's residue, bulk, square-filter,
and side-owner conditions. Physical displacement in (4) is bounded by
\(16D^2|r-s|\). A fixed stride \(S\ge8D^2\), with the additional H7
divisibility requirements, therefore preserves the strict exclusion of
nonhorizontal same-parity integral distances. All occupied slots have bulk
rows rather than the filler row \(F\).

The no-F-source argument from
[the occupied-core theorem](../continuation_full_occupancy_permutations.md)
therefore still excludes FW: it only requires a fully occupied arithmetic
interval with no row-\(F\) point, together with the row alignment and bulk
conditions. It does not require two black points at each slot. Any R2s
support requiring a black point in the designated bad side-owner set is
absent because every surviving black point lies in a good row.

The symmetric small-variable estimate in
[the R2s refinement](continuation_r2s_small_u_refinement.md) gives
\(b=h^{5/6+o(1)}\), including the smaller square-filter exclusions.
Equation (8) therefore gives
\[
 n_E=h^{11/6+o(1)}.
\]
The cited positional relocation cost \(n_ET(h)^2+O(h^2)\), where
\(T(h)=h^{o(1)}\), is consequently \(O(h^2)\). There are only constantly
many residue cores, each with quadratic width. This is a conditional
quadratic-width repair of the bad-row and filler-hole issue.

The cap operation adds black singleton points at some ranks. Therefore its
remaining P, \(\Lambda_3\), \(\Lambda_4\), and 6PT supports must be
tested for the resulting point set; they are not subsets of the original
full-double support family. No complete blackout is asserted here.

There is also a specific incompatibility with the odd-stub P cleanup:
an odd-only cap or padding singleton cannot have its odd point erased
without emptying that slot. The earlier half-factor and slot-gap cleanup
cannot therefore be applied automatically to every new singleton P event.
This theorem and the occupied triangular P cleanup are distinct partial
constructions until that compatibility problem is resolved.

The repair does not contradict
[the two-parity extension obstruction](continuation_two_parity_extension_obstruction.md).
That obstruction retains every original good point. The caps here relocate
some additional good labels, with the quantified bound (8).

## 6. Isolate the singleton sources, then clean the genuine doubles

With the even preference in Section 4, every noncap odd-only singleton has
a bad clipped even value. For each bad even index there are at most \(N\)
ranks with that second coordinate. Odd caps account for at most the selected
cap area. Thus the set \(J\) of odd-only singleton ranks satisfies
\[
 |J|\le N b_1+\sum_{\text{selected caps }Q}|Q|
      =O(nb\log(2n)).                                    \tag{9}
\]
No later odd-point erasure at a genuine double adds a rank to \(J\): it
leaves an even-only singleton.

The one-source version of the P cleanup applies to every remaining genuine
double, even when the other P endpoint is a cap or padding singleton. Let
the odd source at rank \(r\) belong to the genuine double \((a_e,b_e)\),
and let the even endpoint at rank \(s\) have row \(y\). Since the source's
even mate \(b_e\) remains present, the surviving-even Hölder bound gives
\[
 |(b_e-a_e)-(y-a_e)|=|b_e-y|\le C\sqrt{|s-r|}.               \tag{10}
\]
Therefore the same own-row-gap bands used in
[the divisibility cleanup](continuation_divisibility_factor_cleanup.md)
cover the odd source of every small-half-factor P candidate. The other
endpoint need not belong to a genuine double. Each possible own-row gap
still supports at most \(h\) genuine labels, so its exceptional-label
count is unchanged.

Here is a quantitative combined reduction. Set \(\Lambda=\log(2h)\),
take fixed positive constants \(\gamma,\eta\), and let
\[
 B_h=\left\lfloor\frac{\gamma h}{T(h)^2\Lambda^2}\right\rfloor,
 \qquad
 A_h=\left\lfloor\frac{\eta h^{1/3}}
                         {T(h)^{8/3}\Lambda^4}\right\rfloor.
\tag{11}
\]
Erase the odd point of every remaining genuine double whose own row gap has
absolute value at most \(B_h\), and of every remaining genuine double in
the factor-band exceptional set for \(a\le A_h\). Relocate those complete
pairs. The two additional sets have sizes at most
\[
 O(hB_h)+O(h^{7/4}A_h^{3/4}\log(2A_h)),
\tag{12}
\]
so their total internal relocation cost is \(O(h^2/\Lambda^2)\).
Every erased slot retains its even point. Good-row membership, occupancy,
the same-parity bound, and FW exclusion all persist.

Consider any remaining actual in-strip P event whose odd source is not in
\(J\). Its source must be a remaining genuine double. Its hypotenuse and
horizontal leg satisfy \(X=S q\le L\le h-1\). Equation (10) and the
own-gap deletion give
\[
 Y\ge B_h-C\sqrt h\ge c_1\frac{h}{T(h)^2\Lambda^2},
\tag{13}
\]
for all sufficiently large \(h\). The half-factor \(a=(L-Y)/2\) exceeds
\(A_h\), because every smaller candidate lost its odd source. Hence
\[
 q=\frac{2\sqrt{a(Y+a)}}S
 \ge c_2\frac{h^{2/3}}{T(h)^{7/3}\Lambda^3},
 \qquad
 L-X\ge c_3\frac{h}{T(h)^4\Lambda^4}.                       \tag{14}
\]

This gives a single occupied good-row core in which all actual P events
either have an odd source in the explicitly bounded set \(J\), or lie in
the long-gap, large-half-factor regime (14). No triangular order or
diagonal-hole compression is needed for this combined reduction. The
exceptional rows and the added caps have already been included in (8).

The set \(J\) is a residual support location, not a set of slots that can
be emptied. Its size alone does not bound the number of incident P events.
For an odd cap interval, actual P sources are further confined to its two
boundary collars of at most \(\lfloor(h-1)/S\rfloor\) ranks: there is no
even point inside that cap, and an actual P horizontal leg is at most
\(h-1\). Short caps and interactions with opposite-parity stubs remain.

The new \(\Lambda_3,\Lambda_4\), and 6PT supports also remain. The
conditional quadratic budget and exact excess count do not establish that
these residual constraints can be satisfied simultaneously.

## 7. Fixed-block permutation choices remain available

Fix a positive integer \(k\), independent of \(h\). After constructing
the caps and marking all exceptional genuine labels, regard each occupied
rank as one object: a surviving double or a singleton stub. Permute these
objects arbitrarily inside consecutive rank blocks of size at most \(k\).
Every slot remains nonempty, every object's rows remain good, and all
double labels and singleton counts are unchanged.

If two objects end at rank distance \(q\ge1\), their original rank
distance is at most
\[
 q+2(k-1)\le(2k-1)q.
\]
Consequently their same-parity physical row displacement satisfies
\[
 |y-y'|^2<16D^2(2k-1)q.                                   \tag{15}
\]
Choose the actual H7 stride in advance as \(S=8D^2\sigma\), with fixed
admissible power-of-two \(\sigma\ge2k-1\). Then (15) still implies
\(|y-y'|^2<2Sq\), uniformly over every allowed permutation. The FW proof
also remains valid because all columns of the same arithmetic interval
remain occupied and contain no filler row.

The R2s bad-row set must be computed using the weakened locality parameter
\[
 \sigma_{\rm eff}=\sigma/(2k-1),                           \tag{16}
\]
or the still weaker fixed value 1. Using the actual \(\sigma\) without
this adjustment would overstate the geometric restriction. A sufficient
choice is the row set admitted by the source's R2s inequalities with
\(\sigma_{\rm eff}=1\), discarding any unnecessary lattice-congruence
restrictions. The averaged \(h^{5/6+o(1)}\) count still applies to this
fixed-parameter superset. Thus the good sets, offsets, and caps can all be
chosen before the permutation variables.

For the P exceptional sets in Section 6, use the uniform constant
\(C=4D\sqrt{2k-1}\) from (15). They then cover every relevant genuine
odd source for every allowed permutation. Their band counts and relocation
exponents are unchanged. Marking and odd erasure therefore commute with
the choice of object permutations: an erased double becomes its even stub
and travels as that object. Every unmarked genuine odd source keeps its
even mate in the same object throughout.

The number of odd-only singleton objects is still bounded by (9), although
their rank set changes with the permutation. An odd cap's pure interior
loses at most \(k-1\) ranks at each edge. Its actual-P boundary collars
therefore enlarge by at most \(k\), in addition to the horizontal range
\(\lfloor(h-1)/S\rfloor\).

This retains bounded local permutation variables in the combined reduction.
It does not assert that the remaining P and higher-arity constraints admit
a simultaneous assignment of those variables.

## Review status

The complete written proof was independently reviewed on 15 November 2026.
The review checked clipped boundary values, first-good ancestors and maximal
cap selection, the bad-child area charge, the translation expectation,
same-parity endpoint comparisons, padding occupancy, and the exact excess
count. It also checked the stated incompatibility with automatic odd-only P
erasure and the distinction from retaining every original good point.
Section 6 received a separate complete written review, including the even
preference at clipped boundary slots and the one-source use of the surviving
even mate. An independent checker,
[check_random_good_caps.py](check_random_good_caps.py), also passed 30
arbitrary-good-set cases and 678,909 exact same-parity locality comparisons;
its output is [check_random_good_caps.json](check_random_good_caps.json).
Those finite checks include cap maximality and area, good-row occupancy,
the odd-only count, and exact excess accounting. They do not test full-board
rectangle validity.
Section 7 received a separate complete written review of the fixed-block
rank bound, effective locality parameter, independent choice of good sets,
and uniform marking of P source bands. Its scope is a block size fixed
independently of height.
