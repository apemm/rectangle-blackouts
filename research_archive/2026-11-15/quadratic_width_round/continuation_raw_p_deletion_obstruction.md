# The initial sampled P graph cannot be repaired by a power-saving deletion alone

15 November 2026. This note concerns the unpermuted central row model,
with independent parity fields and offsets. An independent uniform
count-function phase is added to each parity; this changes occurrence
equations only by a bounded error and preserves the proved row kernels.

In this model a fixed angular sector already contributes
Omega(h^2 log h) expected genuine P edges. The expected squared degree
is h^{o(1)} at each raw label. Consequently no adaptive deletion with
expected size h^{2-epsilon}, for fixed epsilon>0, can cover the initial
P graph. This does not rule out changing the permutations or finding
an exceptional row realization. It identifies a limitation of deleting
the P conflicts of the first sampled layout.

The claim that these norm pairs are fatal uses full row-pair ownership:
all four binary class-pair blocks of the physical profile, or an
equivalent complete family of its required odd/even doubles, must
eventually be present. An owner may lie in another class-pair block.

## 1. The precise central model

Fix a power-of-two column stride S>=2048. Use a padded Hilbert square
of side N=Theta(h), with columns x_r=Sr. The odd physical pool consists
of rows3 modulo4 above h/2; the even pool consists of rows0 modulo4.
Rounding their endpoints changes only bounded constants.

For each parity independently, sample a count function F with derivative
between1/3 and2/3, as in
[the multiscale row model](continuation_multiscale_row_sampling.md),
and a phase phi uniform on[0,1). The binary word is

\[
 w(n)=\lfloor F(n+1)+\phi\rfloor-\lfloor F(n)+\phi\rfloor.
 \tag{1}
\]

Choose either one of its two occurrence lists. Independently sample an
integer index offset U uniformly in an interval of length Theta(h).
At raw coordinate i, the physical row is the row-pool value of occurrence
i-U, whenever that occurrence lies in the original pool. Only such
genuine points are counted below.

We use offsets with the following complete-fiber property. There is
an interior raw coordinate square of side c h such that, for each raw
coordinate in that square, every physical row in the fixed intervals
used below corresponds to an allowed value of U. The property also holds
in an O(sqrt(h)) enlargement of the square.

This is compatible with the padded model. For example, take N between
32h and64h, put the raw square near(N/2,N/2), of side h/10, and take
each U uniformly from[N/2-h,N/2+h]. Every occurrence index in either
physical pool is between0 and h/4. Thus the required U=i-occurrence_index
lies in the specified offset interval. All padding margins are fixed
multiples of h.

Conditional on F, a physical pool index n belongs to either selected
class with probability between1/3 and2/3, by averaging phi in (1).
If it belongs, exactly one offset U places it at any prescribed eligible
raw coordinate. Consequently, uniformly on these complete fibers,

\[
             {c\over h}\le \Pr(y_i=y)\le {C\over h}.
 \tag{2}
\]

The parity fields, phases, and offsets are independent. Therefore the
probability of two prescribed opposite-parity rows is between c/h^2
and C/h^2 on the complete fibers.

The existing two-row kernel also remains valid, conditionally on the
other parity:

\[
 \Pr(y_{j_1}=z_1,y_{j_2}=z_2)
 \le {K_h\over h(1+|j_1-j_2|)},
 \qquad K_h=(\log h)^{O(1)}.
 \tag{3}
\]

For a repeated coordinate the event is impossible unless its prescribed
rows agree, and then the denominator in (3) is h. One may condition on
the phase before applying the old bounded-error strip argument. Adjacent
physical occurrence gaps are at most12, since the pool step is4 and
class index gaps are at most3.
The usual Hilbert bound gives squared same-parity row displacement
less than2304 times the rank gap. This choice of S also preserves
same-parity nonhorizontal integral-distance exclusion.

## 2. A sector containing h log h different norm vectors

There are at least c_S h log h distinct integer triples(X,Y,L) with

\[
 X^2+Y^2=L^2,\quad S\mid X,\quad Y=1\pmod4,
 \tag{4}
\]

and, for fixed sufficiently small constants specifying an open sector,

\[
 .145h<X<.155h,\qquad .20h<Y<.21h,
 \qquad .02h<(L-Y)/2<.03h.
 \tag{5}
\]

Here and below the decimal endpoints merely select a nonempty open
region; shrinking them slightly is harmless.

To prove the count, use the primitive parametrization

\[
 (X,Y,L)=\ell(2mn,m^2-n^2,m^2+n^2),
 \tag{6}
\]

with m divisible by S/2, n odd, gcd(m,n)=1, and ell=3 modulo4.
For each such ell<=h^{1/4}, take(m,n) in a fixed small rectangular
neighborhood of

\[
 \left(\sqrt{.230h/\ell},\sqrt{.025h/\ell}\right).
\]

A sufficiently small rectangle gives (5). Elementary Möbius inversion
counts c_S h/ell+O_S(sqrt(h/ell) log h) coprime pairs in this rectangle.
Indeed, only odd common divisors need be removed, and their main-term
sum is the positive product over odd primes of(1-p^{-2}); the accumulated
boundary error is O(R log R) at scale R=sqrt(h/ell).

The error is smaller than the main term uniformly for ell<=h^{1/4}.
The primitive parametrization and its common scale ell are unique, so
different choices do not overcount. Summing h/ell over ell=3 modulo4
proves the claim. The odd leg is3 modulo4 before scaling and1 modulo4
after it; S divides the even leg.

## 3. Each vector is a genuine P event with probability Omega(1/h)

Fix a raw source rank r whose cell lies in the interior square from
Section1. For a vector in (4)--(5), let q=X/S and use the odd point at r
and the even point at r+q. Hilbert locality puts the latter cell within
O(sqrt(h)) of the former, so both lie on complete fibers.

Allow the odd source row a to range over the rows3 modulo4 in
[.60h,.61h]. Prescribe the even target row b=a+Y; it lies in
[.80h,.82h] and is0 modulo4. There are Theta(h) choices of a.
Their events are disjoint. Equation (2) and independence therefore give

\[
                         \Pr(b-a=Y,\ a\in[.60h,.61h])
                                  \ge c/h.
 \tag{7}
\]

The other row coordinate of each endpoint differs by O(sqrt(h)) from
the corresponding coordinate of the other endpoint. Hence both endpoint
labels are genuinely inside their physical pools on this event. Their
own-row gaps are Theta(h).

Write t=(L-Y)/2. The alternative vertical pair has rows a-t and b+t.
They lie respectively near .58h and .84h, inside the strip. In (6),
t=ell n^2=3 modulo4. Thus a-t is even0 modulo4, while b+t is odd3
modulo4 and remains above h/2. Its owner belongs to the same full physical
profile. It need not belong to the same sampled binary class pair;
including all four class-pair blocks supplies it elsewhere if necessary.

The two common corners are white in the raw central layout. At their
midpoint column, an odd point is within O(sqrt(h)) of a, whereas the
odd alternative b+t differs from a by at least .22h. The even point
is within O(sqrt(h)) of b, whereas the even alternative a-t differs
from b by at least .22h. This also follows directly from uniform
same-parity Hölder control. The axis owner therefore supplies a genuine
rectangle collision, not only an out-of-strip norm candidate.

All the specified horizontal gaps and smaller half-factors are Theta(h).
Every source has expected degree at least c log h in this subgraph.
There are Theta(h^2) eligible source ranks. Distinct positive X give
distinct target ranks, so

\[
                         \mathbb E|E(G)|\ge c h^2\log h.
 \tag{8}
\]

This is a statement about the initial raw profile, before the cap and
other cleanup choices. It does not assume survival under those choices.

## 4. A uniform subpolynomial second moment

Let D_r be the outgoing degree at a fixed source in the restricted graph
above. Condition on the odd field, hence on its source row a. For two
candidate targets, let d be their difference in raw even coordinates.
If d>=1, occurrence-list Lipschitz control forces

\[
                            |Y_1-Y_2|\le12d.
 \tag{9}
\]

Put T_h=max_{m<=h^2} tau(m)=h^{o(1)}. For each nonzero odd Y, the
factorization(L-X)(L+X)=Y^2 gives at most T_h admissible pairs(X,L).
Thus there are at most C h R T_h^2 pairs of norm vectors with
|Y_1-Y_2|<=24R. In a dyadic class R<=d<2R, each prescribed pair of
target rows has probability at most K_h/(hR), by (3). Ignoring the
remaining rank and sector restrictions only enlarges the count.

For d=0 one must have Y_1=Y_2. There are at most h T_h^2 such vector
pairs, each with conditional probability at most K_h/h. The possible
d are at most O(sqrt(h)), by locality. Summing their dyadic classes gives

\[
                    \mathbb E D_r^2
                         \le C K_h T_h^2\log h=h^{o(1)}.
 \tag{10}
\]

The same argument, with the parity roles reversed, bounds the incoming
degree. It applies uniformly even when a raw rank lies outside the
chosen source square: invalid genuine-row events are simply absent.
For the undirected degree d_G(r), therefore,

\[
                      \mathbb E\sum_r d_G(r)^2=h^{2+o(1)}.
 \tag{11}
\]

## 5. Adaptive deletions do not remove these expected edges cheaply

Let Z be any random set of raw label vertices, chosen with complete
knowledge of all sampled fields. By Cauchy--Schwarz on the joint space
of realizations and vertices,

\[
 \mathbb E\#\{e\in E(G):e\cap Z\ne\varnothing\}
 \le \mathbb E\sum_{r\in Z}d_G(r)
 \le \left(\mathbb E|Z|\right)^{1/2}
       \left(\mathbb E\sum_r d_G(r)^2\right)^{1/2}.
 \tag{12}
\]

If E|Z|<=h^{2-epsilon}, the right side is
h^{2-epsilon/2+o(1)}. This is smaller than (8). In particular, an
almost-sure vertex cover of this initial P graph cannot have an
expected fixed power saving below h^2. Equivalently, (8), (11), and
(12) give the lower bound h^{2-o(1)} for its expected size.

The statement remains meaningful when Z contains vertices removed by
several adaptive cleanup rules: only its expected size matters. It
does not analyze newly created points, altered ranks, different slot
permutations, or a deliberate change in the sampling law.
The fatal-collision interpretation continues to require the full set
of row-pair owners. Relocating an owner as an intact double does not
remove the collision; permanently dropping required owners is outside
the saturated-profile target.

An exceptional realization could still have far fewer P edges. No
positive lower bound on every realization, no chromatic obstruction,
and no failure of a simultaneous permutation choice is asserted.

## Review status

The complete saved note passed an independent written review. That
review checked the phase/offset lower atoms, conditional even-row
kernel, repeated-coordinate case, incoming-degree bound, primitive
sector count, in-strip white corners, and joint-space adaptive-deletion
inequality. The full-physical-profile owner qualification records a
clarification from that review.
