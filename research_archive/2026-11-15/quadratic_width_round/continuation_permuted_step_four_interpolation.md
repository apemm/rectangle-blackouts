# Bounded permutations survive spacing-four interpolation

15 November 2026. Bounded permutations of genuine good doubles can be
combined with the spacing-four refinement. Expanding each forbidden row
set by a fixed radius makes every newly interpolated value good. A fixed
mesh separates the unit row changes and retains the same-parity geometric
exclusions from
[the refinement lemma](continuation_step_four_refinement.md).

The theorem preserves local permutation variables and exact occupancy.
It does not solve their P or higher-arity constraints, and it does not
provide a collar theorem.

## 1. Coarse hypotheses and which objects can move

Work in row-index coordinates: physical rows of role \(\alpha\) are
\(\rho_\alpha+4z\), with opposite parities for the two roles. Let the
total coarse functions \(f_0,f_1\) on \(0,\ldots,R-1\) satisfy
\[
 |f_\alpha(r)-f_\alpha(s)|\le C_0\sqrt{|r-s|}.
 \tag{1}
\]
Assume each consecutive coordinate pair changes in at most one coordinate,
and by at most one index unit. Let \(B_\alpha\) be the actual forbidden
index set for role \(\alpha\). Every coarse rank has at least one value
outside its forbidden set. Every retained genuine double has both values
outside their actual forbidden sets.

Partition the ranks into consecutive blocks of at most \(k\) ranks,
where \(k\) is fixed independently of height. Define
\[
 C_1=C_0\sqrt{2k-1},\qquad
 D=\max\{1,\lceil C_1\rceil\},\qquad
 B_\alpha^{+D}=\{z:\operatorname{dist}(z,B_\alpha)\le D\}.
 \tag{2}
\]
When \(B_\alpha\) is empty, its enlargement is empty. Only genuine
doubles whose two coordinates avoid \(B_\alpha^{+D}\) may move.
Permute any such doubles within their own blocks. Fix every other object,
including all caps and singletons. This gives one permutation \(\pi\)
of the ranks, fixing all nonmoving objects. Put
\[
 g_\alpha(r)=f_\alpha(\pi(r)).
\]
For distinct ranks,
\[
 |\pi(r)-\pi(s)|\le |r-s|+2(k-1)
                    \le(2k-1)|r-s|.
\]
Consequently \(g_\alpha\) has Hölder constant \(C_1\), and its
adjacent coordinate differences have magnitude at most \(D\).

Call an edge \((r,r+1)\) changed if either endpoint is moved by
\(\pi\). One endpoint is then a moved genuine double. For each role,
the other endpoint is within \(D\) index units of its value. Every
integer between the two endpoint values therefore avoids the actual
forbidden set \(B_\alpha\). Thus both coordinates are good throughout
the interpolation of a changed edge.

On an unchanged edge, the old one-coordinate unit-step property remains.
Interpolating that edge uses only its two original coordinate pairs.
Both pairs have a good option. No intermediate pair with two bad options
is introduced.

The enlargement has size at most \((2D+1)|B_\alpha|\). If complete
permutation freedom among all remaining doubles is wanted, one may first
treat this enlarged set as forbidden and relocate its incident labels.
The resulting exceptional-label bound changes only by a fixed factor.
Alternatively, retain other good doubles but keep them fixed, as in the
statement above.

## 2. An explicit common interpolation schedule

Choose
\[
 G=8D,\qquad M=32D^2.
 \tag{3}
\]
Both are fixed constants. At fine rank \(t\), use physical column
\(4t\). Anchor coarse rank \(r\) at fine rank \(Mr\).

For the edge \((r,r+1)\), move coordinate \(\alpha\) monotonically
from \(g_\alpha(r)\) to \(g_\alpha(r+1)\), one index unit at each of
the first \(|g_\alpha(r+1)-g_\alpha(r)|\) mesh points
\[
 Mr+G,\ Mr+2G,\ldots,Mr+DG.
\]
Hold its value between changes. The last coarse block is constant.
Because \(DG<M\), each coordinate reaches the next anchor value before
that anchor. Since \(M\) is a multiple of \(G\), successive changes
in any one coordinate are separated by at least \(G\) fine ranks,
including changes in adjacent coarse blocks.

Write the resulting total index functions as \(F_\alpha(t)\), for
\(0\le t<MR\). The good-value argument in Section 1 shows that every
fine rank has a good option. On changed edges both options are good.

## 3. Only isolated unit jumps can violate the square bound

Let \(q=|t-u|\). First suppose \(q\le M\). The interval meets at
most two interpolation blocks, so one coordinate changes at most
\(2D\) times. If it changes \(j\ge2\) times, then
\[
 q\ge G(j-1),\qquad
 j^2\le4D(j-1)\le q/2.
 \tag{4}
\]
The middle inequality holds for every integer \(2\le j\le2D\).
The absolute coordinate difference is at most \(j\), even if successive
changes have different signs. If there is only one change and \(q\ge2\),
the same square bound holds. If there is no change it is immediate.

For \(q\ge M\), let \(r=\lfloor t/M\rfloor\) and
\(s=\lfloor u/M\rfloor\). Each interpolated value differs from its
left anchor by at most \(D\), and \(|r-s|\le q/M+1\le2q/M\).
Therefore
\[
 |F_\alpha(t)-F_\alpha(u)|
 \le C_1\sqrt{2q/M}+2D,
\]
and
\[
 |F_\alpha(t)-F_\alpha(u)|^2
 \le(4C_1^2+8D^2)q/M\le3q/8<q/2.
 \tag{5}
\]
Thus, in physical coordinates, every same-role pair satisfies
\[
 |\Delta y|^2\le2|\Delta x|,
 \tag{6}
\]
except for an adjacent fine pair containing one unit index jump. Its
physical vector is \((\pm4,\pm4)\). Such exceptional edges are
separated by at least \(G\ge8\) fine ranks in each role.

Exactly as in the original refinement theorem, every same-parity pair
lies in the closed horizontal cone \(|\Delta y|\le|\Delta x|\), with
equality only on those isolated exceptional edges. The norm gap excludes
nonhorizontal integral distances, the isolated edges exclude same-parity
right triangles, and the cone lemma excludes nondegenerate same-parity
side/diagonal mixed supports.

## 4. Why total cap functions have the required unit-step property

The clipped or folded raw Hilbert coordinate pair changes by at most one
index unit in one coordinate at each step. Each scalar clipping or folding
map is 1-Lipschitz, so it can only remove or reverse such a unit change.
Within a selected cap, that cap's coordinate is constant and the other
coordinate remains the clipped raw function. Hence the property still
holds on every internal cap edge.

At a cap boundary, the constant coordinate equals the original coordinate
at the boundary endpoint. Both coordinate pairs on the edge are therefore
the original clipped pairs. This also applies to adjacent caps of opposite
parities, since their boundary endpoint values are unchanged. Disjoint
caps consequently preserve the one-coordinate unit-step property for
the two total virtual functions.

This is stronger than bounding each coordinate increment separately.
That stronger fact is what guarantees a good option throughout every
unchanged interpolation edge.

## 5. Occupancy, exceptional counts, and candidate unions

Keep each genuine double only at its anchor \(Mr\). Every other fine
rank chooses exactly one good virtual option. This preserves every
retained genuine label exactly once and occupies every spacing-four slot.
The width increases by the fixed factor \(M\).

If \(J\) original coarse ranks have a forbidden even option, then at
most \(2MJ\) fine ranks lack a good even option. Changed edges contribute
none. An unchanged interpolation edge can lack a good even option only
if one of its two coarse endpoints did. The constant final block obeys
the same bound. Thus the previous \(O(hb\log h)\) estimate for such
coarse ranks remains \(O_{k,C_0}(hb\log h)\). The sharper bound from
the total-cap palette transfers in the same way when its hypotheses hold.

Before choosing permutations, every fine coordinate belongs to a finite
candidate set of the form
\[
 f_\alpha(v)+e,
 \qquad |v-r|\le k-1,\qquad |e|\le D,
 \tag{7}
\]
where \(r\) is its coarse block index. Thus estimates based on a uniform
finite union of raw/cap affine-coordinate candidates acquire only a fixed
factor. In particular, adding a bounded index offset does not change
which row-offset variable an affine candidate fixes.

Equation (7) is a candidate-union statement, not an automatic transfer of
every prior theorem. Any estimate that uses actual Hilbert injectivity,
raw row equality, a particular sea, or a collar still needs its stated
hypotheses checked. Prior deliberate option erasures remain in force at
their original anchors. The occupancy proof concerns row-forbidden sets;
it does not guarantee occupancy after arbitrary new rank-specific bans
on the interpolated singleton options. Such bans require a separate
nonempty-option check.

The interpolation supplies local permutation freedom within a quadratic
occupied scaffold. Simultaneous avoidance of the remaining cross-parity
and parked-triangle systems, as well as valid joins, remains separate.

Independent review: the complete written proof passed a separate review
of changed-edge clearance, unchanged unit steps, both mesh estimates,
isolated exceptional pairs, the bad-option count, and the finite
candidate union.
