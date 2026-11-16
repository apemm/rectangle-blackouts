# Multiscale row sampling and central P three-cycles

15 November 2026. A complementary row partition with independent slope
variables at every dyadic scale supplies a joint three-row probability
estimate. In the central genuine model, it gives an expected
\(h^{7/4+o(1)}\) count for P three-cycles in all directions. The same
sampling retains the earlier two-row nonconstant-fold estimate, up to
polylogarithmic factors. It does not settle singleton parity choices,
longer cycles, or a full construction.

## 1. A complementary partition with bounded gaps

Work first in a physical residue-index interval \([0,H)\), where
\(H=\Theta(h)\). Let \(2^J\ge H\) be the least such power of two.
For each \(0\le j\le J\) and each aligned interval
\(I_{j,k}=[k2^j,(k+1)2^j)\subset[0,2^J)\), independently sample
\(Z_{j,k}\) uniformly on \([-1,1]\). Set
\[
 \epsilon_j={1\over16(j+1)^2},\qquad
 C'(x)={1\over2}+\sum_{j=0}^J\epsilon_jZ_{j,k_j(x)},
 \qquad C(x)=\int_0^x C'(t)\,dt.                     \tag{1}
\]
Values at dyadic boundaries do not affect the integral. Since
\(\sum_j\epsilon_j<1/6\),
\[
                    1/3<C'(x)<2/3.                 \tag{2}
\]
Define the binary row word
\[
             w(n)=\lfloor C(n+1)\rfloor-\lfloor C(n)\rfloor,
              \qquad 0\le n<H.                    \tag{3}
\]
It has values in \(\{0,1\}\). Its two classes partition every original
row. Each three consecutive positions contain a one and a zero, because
the increase of both \(C(x)\) and \(x-C(x)\) over an interval of length
three exceeds one. Thus both occurrence lists have successive gaps at
most three.

Write \(F=C\) for the one class and \(F=x-C\) for the zero class.
If \(p_i\) is the zero-indexed occurrence list, then
\[
                     F(p_i)=i+O(1),                \tag{4}
\]
uniformly. For ones this follows directly from (3); for zeros the prefix
count is \(n-\lfloor C(n)\rfloor=\lceil n-C(n)\rceil\).
The list length \(n_F\) satisfies
\(n_F=F(H)+O(1)\). Both lists have length \(\Theta(h)\).

Use independent fields (1) for the two parity pools. The two complementary
classes within one parity remain dependent. Every estimate below is for
one fixed class pair; take a finite union afterward. Independently choose
raw-coordinate offsets from fixed integer intervals of size \(\Theta(h)\),
using bounds on the maximum possible class lengths.

Fixed sampled good anchors can be injected into each class before folding.
Each insertion changes every prefix count by at most one, so (4), the
endpoint count, and all bounds below retain a uniformly bounded error.
The largest gap cannot increase. Injected occurrences remain nongenuine
in classes where the row was originally absent. Thus original-label
coverage and the bounded-jump occupancy construction are preserved.

This sampling does not have a single global approximation
\(p_i=\alpha i+O(1)\). Arguments requiring that approximation must be
replaced, rather than silently reused.

## 2. The local slope variables

Every interval of length \(d\ge4\) inside \([0,H]\) contains an aligned
dyadic interval of length between \(d/4\) and \(d/2\). The variable
attached to that interval changes an integral of \(F'\) across it by
\(\pm\epsilon_j|I|Z_{j,k}\). Its coefficient has magnitude at least
\[
                   c d/\log^2(2h).                 \tag{5}
\]
It affects no integral over a disjoint interval. Variables selected from
two disjoint intervals are distinct and independent, even when their
dyadic levels differ. All other variables can be conditioned upon.

We use this only when the target physical rows and chosen intervals are
fixed before sampling the relevant parity field. In particular, for a
cross-parity P pattern one may condition on the entire opposite-parity
field and its offset first. Selecting intervals after observing the same
field would not justify the argument.

## 3. Three prescribed central rows

Fix three raw coordinate indices \(k_0,k_1,k_2\) and three target
physical residue indices \(y_0,y_1,y_2\), independent of this parity's
field and offset \(U\). A bounded target error is permitted. In the
central branch the necessary conditions are
\[
                         F(y_i)+U=k_i+O(1).          \tag{6}
\]
They follow from (4), and their error bound is uniform over all shared
parameters. The targets need not be integer residue indices, since
\(F\) is Lipschitz and the original physical error is bounded.

Sort the raw indices and let \(d_1,d_2\ge0\) be their two adjacent
gaps, retaining repetitions. Put
\[
                         Q=(1+d_1)(1+d_2).           \tag{7}
\]
Then
\[
 \Pr(\text{all three prescribed rows})
                 \le {C\log^4(2h)\over h Q}.        \tag{8}
\]

First suppose both \(d_i\) exceed a sufficiently large fixed constant.
If the event is possible, (2) and (6) force the corresponding target rows
to have the same order and adjacent distances \(\Theta(d_i)\).
Choose one dyadic subinterval in each target gap as in Section 2.
Subtract the first equation in (6) from the second, and the second from
the third. Each difference contains one of these two variables with
coefficient of magnitude at least \(c d_i/\log^2(2h)\), and contains
none of the other. Conditional on all remaining variables, the permitted
area in their two-dimensional square is at most
\(C\log^4(2h)/(d_1d_2)\).
For every fixed realization of the field, any one equation in (6)
permits only \(O(1)\) integer offsets \(U\), costing \(O(1/h)\).
This proves (8) without independence assumptions about the bounded errors.

If just one raw gap is bounded, use a single interval between the extreme
target rows. The two-row argument gives
\(C\log^2(2h)/(h(1+\max(d_1,d_2)))\), which implies (8).
If both gaps are bounded, the single-offset bound \(O(1/h)\) suffices.
These cases also cover repeated raw coordinates.

## 4. The joint bound for a central P three-cycle

Consider three genuine central objects with raw cells
\((i_r,j_r)\), \(r=0,1,2\). Specify three signed integral P heights
\(Y_r\) for the fixed horizontal edges of a directed cycle. The edge
requirements are
\[
                         b_{r+1}-a_r=Y_r,
                         \qquad r\pmod3.             \tag{9}
\]
Condition on the odd field, its offset, and all sampled anchors. The odd
rows are now fixed, so (9) prescribes all three even target rows before
the even field and offset are sampled. Apply (8) to the three even raw
indices. Reversing the roles of the two parities gives another bound.
Let \(Q_0,Q_1\) be (7) for the three odd and three even raw coordinates.
Taking the smaller of these two bounds, rather than multiplying them,
gives
\[
 \Pr(\text{the specified cycle})
       \le {C\log^4(2h)\over h\max(Q_0,Q_1)}.         \tag{10}
\]

The same conclusion holds for fixed bounded provenance and bounded-error
central forms from cleared interpolation or permutations. Condition on
the base opposite-parity rows and use the uniform errors in (6).
Eligibility or good-row conditions may be discarded. This does not
include arbitrary cap-coordinate forms or different fold branches.

If bounded copies of one raw object occur, impose the usual own-gap
cutoff tending to infinity. Their bounded horizontal separation cannot
support P, since \(X^2\ge2|Y|+1\). Otherwise raw-cell multiplicity is
one. In either case all counting below has at most bounded multiplicity.

## 5. Count all directions

An actual P has horizontal span less than \(h\). The first object has
\(O(h^2)\) possibilities and the second has \(O(h)\). Factorization
of the first fixed horizontal leg leaves \(h^{o(1)}\) possible signed
heights \(Y_0\). Uniform same-parity locality implies
\[
                         |Y_1-Y_0|=O(\sqrt h).       \tag{11}
\]
For each of these \(O(\sqrt h)\) possible heights, factoring
\((L-X)(L+X)=Y_1^2\) gives \(h^{o(1)}\) horizontal legs and hence
third columns. The closing gap has \(h^{o(1)}\) height choices.
Consequently the total rank-and-height candidate count is
\[
                              h^{7/2+o(1)}.          \tag{12}
\]
The signed calculation (11) does not require the heights to share a sign.

Translate the first raw cell to \((0,0)\); write the next two as
\((u,v)\), \((w,z)\). All four coordinates have magnitude
\(O(\sqrt h)\). For a one-dimensional pair \((u,w)\), the number with
\(Q(0,u,w)\le T\) is
\[
                              O(T\log(2h)).          \tag{13}
\]
Indeed sorting the three positions reduces to a constant number of
orders and two nonnegative adjacent gaps \(a,b\), with
\((1+a)(1+b)\le T\). The elementary divisor sum counts these.
Therefore the number of quadruples with
\(\max(Q_0,Q_1)\le T\) is \(O(T^2\log^2(2h))\), and dyadic
summation gives
\[
 \sum_{\max(Q_0,Q_1)\le T}{1\over\max(Q_0,Q_1)}
                              =O(T\log^2(2h)).       \tag{14}
\]
This is an overcount by grid coordinates, so no special Hilbert
independence is assumed.

For each fixed rank triple, there are only \(h^{o(1)}\) triples of norm
heights. Thus (10) and (14), summed over the first object, bound the
expected contribution with \(\max(Q_0,Q_1)\le T\) by
\[
                               h^{1+o(1)}T.          \tag{15}
\]
For the complementary range use (12) and (10), giving
\[
                               h^{5/2+o(1)}/T.       \tag{16}
\]
Choose \(T=h^{3/4}\). Equations (15)--(16) prove
\[
          \mathbb E\#\{\text{central genuine P three-cycles}\}
                              \le h^{7/4+o(1)}.      \tag{17}
\]
There is no restriction to a fixed direction palette and no determinant
exception. The same bound applies to their incident genuine objects.

## 6. Recover the two-row nonconstant-fold estimate

This field also preserves the probability estimate needed by the
long-triangle and random-anchor-hub arguments. Let the original physical
index range have fixed endpoint \(H\). Inverting (4) on each
nonconstant fold branch gives the following normalized equations for a
prescribed physical index \(y\):
\[
 \sigma F(y)+tF(H)+U=k+O(1),                         \tag{18}
\]
with
\[
 (\sigma,t)=(1,0)\text{ centrally},\quad
 (-1,0)\text{ on the left},\quad
 (-1,2)\text{ on the right}.
\]
The right formula uses \(n_F=F(H)+O(1)\), including bounded anchor
insertions. Branch conditions may be omitted in upper bounds.

Subtract (18) for two fixed target rows. The resulting field expression
has the form
\[
                    \int_0^H w(x)F'(x)\,dx
                       =k_1-k_2+O(1).               \tag{19}
\]
For all nine branch pairs, \(w\) has one sign, takes values in
\(\{0,\pm1,\pm2,\pm3\}\), and is constant on the at most three
intervals determined by the two target rows. To check the sign, equal
branches give a signed interval; central/left gives a signed sum of two
prefixes; central/right gives that sum minus twice the whole interval;
left/right gives a signed interval plus or minus twice the whole interval.
In every case its magnitude is at least one between the two targets.

If (19) is possible, (2) implies
\[
 \int|w|\,dx\asymp|k_1-k_2|+O(1),\qquad
 \int|w|\,dx\ge|y_1-y_2|.                           \tag{20}
\]
When the first quantity is large, one constant nonzero interval of \(w\)
has length at least a fixed multiple of it. Its dyadic slope variable
from Section 2 restricts (19) to probability
\(O(\log^2(2h)/(1+|k_1-k_2|))\). Conditional on the field, either
equation in (18) allows only \(O(1)\) offsets. For small differences
the single-offset bound suffices. Hence
\[
 \Pr(\text{two prescribed nonconstant rows})
       \le {C\log^2(2h)\over h(1+|k_1-k_2|)}.        \tag{21}
\]
In particular, if their prescribed physical separation is \(\delta\),
the bound is \(O(\log^2(2h)/(h(1+|\delta|)))\).
It is uniform in independently sampled inserted anchors and in specified
cap boundary candidates. Cap selection is not conditioned upon.

Thus the \(h^{-2+o(1)}\) probability for a prescribed long triangle,
and the reciprocal-index estimate used with random anchor hubs, remain
available. Their separate deterministic counts must still be checked
against the new sampling wherever they used more than bounded gaps,
uniform locality, and (21). In particular a conclusion relying on a
single global affine stretch is not transferred by this note alone.

## 7. Bidirectional P survives the change of sampling

The earlier \(h^{3/2+o(1)}\) genuine-endpoint bound for bidirectional
P templates has a direct replacement under this field. Require the same
one-base-pair representation and selected-cap geometry as in
[the joint-P note](continuation_mechanical_p_joint_constraints.md): a fine
target has bounded error from one specified virtual pair with at most one
selected cap coordinate; retained genuine sources lie outside all selected
cap squares. Coordinate-form candidates are enumerated before selection.
Keep the own-gap condition used there to exclude bounded copies of the
same raw object.

Fix a genuine central source \(r\), one target candidate \(s\), and
the two signed norm heights in
\[
                         b_s-a_r=Y_1,\qquad
                         b_r-a_s=Y_2.                \tag{22}
\]
Suppose both target coordinates are nonconstant forms at deterministic
raw or cap-boundary indices \(c_0,c_1\). Condition first on the odd
field and offset. The two even target values are then specified; (21)
gives \(h^{-1+o(1)}/(1+|c_1-j_r|)\), for any target fold branch.
Interchanging the parities gives the bound with \(|c_0-i_r|\).
Consequently
\[
 \Pr((22))\le {h^{o(1)}\over
                    h(1+\max(|c_0-i_r|,|c_1-j_r|))}. \tag{23}
\]
No independence between those two applications is asserted.

The geometric projection sum from Section 4 of the joint-P note is
unchanged: actual P limits the raw target ranks to an \(O(h)\) interval,
and the weighted sum of reciprocal projected distance is
\(O(\sqrt h\log^2(2h))\), over all dyadic cap depths. Its denominator
cannot vanish for an actual selected-cap target and a retained genuine
source, since the projection lies in the selected square. For an
uncapped coincident raw object, bounded horizontal separation and the
own-gap cutoff exclude actual P. Bounded provenance changes these
statements only by fixed constants or the same bounded-copy exclusion.
Summing (23) over sources and divisor-many height pairs therefore gives
\(h^{3/2+o(1)}\).

If a target coordinate is a constant anchor, a simpler bound applies.
For example, condition on all sampled anchors and suppose \(b_s\) is
fixed. The first equation of (22) specifies the genuine odd source row.
Its offset has only \(O(1)\) possible values for each odd field, costing
\(O(1/h)\). Then condition on that entire odd field and offset, so
\(a_s\) is fixed too. The second equation specifies the genuine even
source row, costing another \(O(1/h)\) in the independent even offset.
The argument also covers two constant target coordinates, bounded row
errors, and the parity-reversed case. Thus these candidates have
probability \(O(h^{-2})\). Their \(h^{3+o(1)}\) rank, form, and
height possibilities contribute only \(h^{1+o(1)}\).

This proves the same \(h^{3/2+o(1)}\) exceptional genuine-endpoint
bound under the multiscale sampling, including nonconstant target fold
branches and anchor targets. It still does not choose a consistent
parity for all remaining singleton points.

## 8. Geometric compatibility and limits

Coverage, gaps at most three, injective bad-row preimages, and the
maximum-size choice of offset intervals suffice for the existing
anchor insertion and good-cap occupancy lemmas. Conditioning on the
field leaves at most three offsets per bad physical value under the
fold. The cap-area and bad-child expectations retain their stated orders.
The occurrence lists and their folds have a uniform Lipschitz constant,
so the same-parity square-root geometry also survives.

The three-cycle theorem concerns central genuine objects. It does not
choose the parity left at erased objects, extend (17) to all folded and
cap-constant objects, control arbitrary directed cycle lengths, or prove
the Hall conditions for private choices. The full construction remains
open at those steps and at any other untranslated residual family.

## Review status

Sections 1--6 and the geometric compatibility statements passed an
independent written review. That review checked target independence,
the selected disjoint dyadic variables, offset fibers, repeated gaps,
all-direction height enumeration, the product-gap sum, and all nine
one-signed fold coefficient cases. The bidirectional-P compatibility
corollary in Section 7 passed a separate independent written review,
including the conditional target rows, reciprocal max-distance kernel,
one-cap projection sum, and sequential two-offset bound for anchor targets.
