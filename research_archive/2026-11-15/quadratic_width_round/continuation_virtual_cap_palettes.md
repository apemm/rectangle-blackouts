# Good caps supply a two-parity singleton palette

15 November 2026. The good-cap construction has more flexibility than its
initial one-parity filling. Two total virtual row functions preserve the
original Hölder constant. Every rank has a good singleton choice, and all
but \(O(hb)\) ranks have both choices. No additional labels are relocated.

The optional singleton choices introduce their own P and higher-arity
constraints. The P subsystem has an exact directed-path test, including the
extra forced choices created by any genuine doubles that remain fixed.

## 1. Keep both virtual coordinate functions

Use the offsets, clipped functions \(f_0,f_1\), and disjoint selected caps
from [the good-cap theorem](continuation_random_good_caps.md). For each
parity \(\alpha\), define
\[
 \widetilde f_\alpha(r)=
 \begin{cases}
 v_Q,&r\text{ belongs to a selected cap }Q\text{ of parity }\alpha,\\
 f_\alpha(r),&\text{otherwise}.
 \end{cases}                                               \tag{1}
\]
Here \(v_Q\) is the good common endpoint value of the cap. In particular,
on a cap of the opposite parity, keep the original clipped coordinate.

Apply the cap endpoint lemma separately to each parity's own caps, retaining
that coordinate at every other rank. This proves the total-function bound
\[
 |\widetilde f_\alpha(r)-\widetilde f_\alpha(s)|^2
 <16|r-s|\qquad(r\ne s).                                  \tag{2}
\]
The proof does not require the opposite-parity coordinate to be absent.

Every rank has at least one good virtual value. On a selected cap its cap
coordinate is good. Outside the caps, every rank with two bad clipped
coordinates has already been covered. Moreover, a replacement in (1) is
always good, so
\[
 \{r:\widetilde f_\alpha(r)\notin G_\alpha\}
 \subseteq\{r:f_\alpha(r)\notin G_\alpha\}.
\]
For every original bad index, exactly one coordinate line can have that
unclipped value. Thus
\[
 \#\{r:\widetilde f_\alpha(r)\notin G_\alpha\}
 \le N b_\alpha.                                         \tag{3}
\]
At most \(Nb\) ranks lack one of the two good options.

## 2. Use the palette without introducing duplicate doubles

At every surviving genuine double outside the selected caps, retain its
original pair. Its two virtual coordinates are its original good rows.
At every other rank, choose exactly one good virtual coordinate. Even if
both virtual rows are good, do not introduce a new double there.

All genuine pairs covered by caps, or incident to a bad row, remain in the
same relocation set as before. The occupied-slot count, genuine-double
count, and exact \(m+q_h\) bookkeeping are unchanged.

Equation (2) holds for every selection of the singleton options. After
multiplying by the physical row step, the same fixed stride excludes
nonhorizontal same-parity integral distances. Every selected row is good
and lies in the bulk. The arithmetic interval remains occupied and has no
row-\(F\) point, so the FW exclusion also survives.

The support family must now be compiled from all good virtual options.
Changing a singleton's parity can add a black point absent from the first
one-parity cap filling. Therefore this choice model is not justified by
black-point erasure monotonicity alone. Its P, \(\Lambda_3\),
\(\Lambda_4\), and 6PT constraints still need simultaneous control.

The fixed-block object permutations remain available. An object carries its
one or two virtual singleton options to its chosen slot. The old rank
distance is at most \((2k-1)\) times the new distance, so the same inflated
constant and effective locality parameter from the cap note apply uniformly
to both the parity options and the permutations.

## 3. Even preference reduces the exceptional source count

One admissible default filling chooses even at every singleton rank where
the virtual even value is good, and otherwise chooses odd. Its exceptional
odd-only source set is
\[
 J=\{r:\widetilde f_1(r)\notin G_1\},
 \qquad |J|\le N b_1=O(hb).                               \tag{4}
\]
No cap-area logarithm is needed. With the current R2s bound this is
\(h^{11/6+o(1)}\), while the relocated-label count remains
\(O(hb\log(2h))\).

The actual-P incidence proof in
[the singleton-source count](continuation_cap_stub_p_incidence.md)
still applies to this default filling. Its two-unclamped case becomes
simpler: every source in \(J\) has an original bad clipped even value,
which restricts the even offset to at most \(b_1\) choices. The P norm
then fixes the other offset. There is no need to select a bad-cap-child
witness for the source. The possible odd cap coordinate and the possible
even endpoint coordinate still range over \(O(\log h)\) ancestors.

The one-clamped endpoint estimate is unchanged. For two clamped endpoints,
the deterministic bound is \(O(|J|\mathcal D_h)\). Joint offset averaging
therefore still yields the same \(h^{23/12+o(1)}\) bound on actual
potential P incidence from \(J\), uniformly over fixed-block permutations.

This incidence bound concerns the default even-preference sources, or their
specified constraint union. An arbitrary parity assignment can introduce
many additional odd singleton sources; (4) does not bound that larger set.
Also, the pure-odd-cap boundary-collar observation from the earlier filling
does not apply to this variant: an odd cap can now contain even choices.

## 4. The exact P test for the singleton choices

Fix the positions of the objects and any genuine doubles that are to remain
double. Each singleton object has a variable \(x_v\in\{0,1\}\), where
1 chooses its good odd option and 0 chooses its good even option. An object
with only one good option has that fixed value.

For a geometric P event using the odd option of singleton \(u\) and the
even option of singleton \(v\), avoidance is exactly
\[
 x_u\le x_v.                                              \tag{5}
\]
Unavailable options can be omitted; alternatively the corresponding fixed
value makes their clauses automatic.

Fixed genuine doubles add two kinds of forces. A P edge from their odd
point to singleton \(v\)'s even option forces \(x_v=1\). A P edge from
singleton \(u\)'s odd option to their even point forces \(x_u=0\).
Any P between two fixed genuine doubles must be excluded separately.
Inconsistent forces at one singleton already make the system impossible.

Let \(F_1\) and \(F_0\) include both the intrinsic one-option forces
and these double-induced forces. Add a directed edge \(u\to v\) for
every nontrivial constraint (5). Assuming no fixed-double P event, the
singleton P system is solvable if and only if there is no directed path
from \(F_1\) to \(F_0\), including a path of length zero.

Necessity follows by propagating (5). For sufficiency, assign 1 precisely
to the vertices reachable from \(F_1\), and assign 0 to every remaining
vertex. No forced-zero vertex is reached, and the assigned-one set is
closed under outgoing edges.

Before accounting for the fixed doubles, the intrinsic forced-one and
forced-zero sets have sizes at most \(Nb_1\) and \(Nb_0\), respectively.
The full graph can have additional double-induced forces and long paths.
Neither the sparse intrinsic force sets nor the incidence estimate proves
the required path exclusion. Higher-arity constraints are also outside
this directed-path test.

## 5. Switching to a band-safe odd option does not propagate unfiltered P

The two total virtual functions provide a counterfactual even mate for every
odd option, even when that mate is bad or is not selected. Write the physical
virtual values of object \(v\) as \(a_v,b_v\), and let
\(d_v=b_v-a_v\). Use the fixed uniform constant \(C\) after any allowed
block permutations. For an odd source at \(a_v\) and any selected even
endpoint \(y_w\), at slot gap \(q\),
\[
 |d_v-(y_w-a_v)|=|b_v-y_w|\le C\sqrt q.                    \tag{6}
\]
Goodness or selection of \(b_v\) is unnecessary: the estimate is between
values of the total virtual even function.

Fix the physical own-gap threshold \(B_h\) and half-factor threshold
\(A_h\) from the cap note. Call an available odd option band-safe when
\(|d_v|>B_h\) and it avoids every factor band
\[
 |d_v\mp Y(a,q)|\le C\sqrt q+1,
 \qquad
 Y(a,q)=S^2q^2/(4a)-a,                                    \tag{7}
\]
for \(1\le a\le A_h\), positive integer \(q\), and positive odd
integral \(Y(a,q)<h\). The range of \(q\) is finite, namely
\(q\le2\sqrt{a(h+a)}/S\). Call the other available odd options
band-unsafe.

Every outgoing P candidate from a band-safe option has half-factor greater
than \(A_h\), by (6)--(7). For an actual in-strip P, \(S q\le h-1\),
so (6) also gives
\[
 Y\ge B_h-C\sqrt h.
\]
It follows that all its actual outgoing P events satisfy the long-gap bounds
from the divisibility cleanup, including \(q\ge h^{2/3-o(1)}\).
This conclusion is uniform over the selected virtual even options and the
fixed-block permutations. No count of all virtual band-unsafe options is
asserted.

The reverse estimate holds at the even target as well. Its virtual odd mate
gives
\[
 |d_w-(b_w-a_v)|=|a_w-a_v|\le C\sqrt q.
\]
Thus band-safety of either endpoint's virtual own gap already places the
edge in the long-gap, large-half-factor family, whether its mate is selected
or not. Every genuinely unfiltered P edge has band-unsafe virtual own gaps
at both endpoints.

For the broader source-based family consisting of all P events out of
\(J\), an even singleton target with an available band-safe odd option can
still be switched to that option. Every
incoming P using its even point disappears. Every newly available outgoing
P belongs to the already separated long-gap family. Thus these switches can
be made simultaneously without creating a cascade of unfiltered P sources.
One may in particular choose the band-safe odd option at every singleton
that has one.

This switches away some broadly classified \(J\)-source edges, but those
edges already satisfy the long-gap conclusion by the target test. It does
not solve the genuinely unfiltered unsafe-to-unsafe family. The remaining
unsafe choices still require the directed-path test, and no forced-path
exclusion is proved. The analogous even erasure at a genuine double can
remove a broader \(J\)-source edge while retaining its band-safe odd
point, with its complete pair relocated.

A singleton switch adds an odd black point that was absent from the default
filling. Consequently the higher-arity constraints must be controlled on the
full virtual-option support family. Only the statements about the P split,
good rows, locality, occupancy, and FW follow from this switching argument.

## Review status

The complete written note was independently reviewed on 15 November 2026.
The review checked both total coordinate functions, the bad-line count,
singleton-only use of the palette, exact excess accounting, the default
source set and its incidence transfer, and the fixed-double qualifications
in the directed-path criterion. Arbitrary parity assignments remain outside
the default source-count estimate.
Section 5 was added afterward and awaits a separate written review.
