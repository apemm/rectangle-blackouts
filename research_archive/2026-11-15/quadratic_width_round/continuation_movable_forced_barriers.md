# Good-row palettes admit movable forced barriers

15 November 2026. A missing-parity interval can be filled from its two
good endpoint rows, leaving only a short movable barrier. The same-parity
Hölder constant increases by at most two. Return intervals, whose two
endpoint rows agree, disappear completely. No additional genuine labels
need to be relocated.

This gives a weighted criterion for hitting every direct intrinsically
forced P edge. The criterion has not been proved for the actual R2s bad
sets. Longer forced paths and newly available support choices remain
separate questions.

## 1. Compress one interval of unavailable options

Let a total virtual row function \(f\) satisfy
\[
 |f(r)-f(s)|\le C\sqrt{|r-s|}                              \tag{1}
\]
on a finite integer rank interval. Let \(G\) be its good-row set, and
assume the first and last ranks have good values. Every maximal interval
of unavailable options therefore has two good anchor ranks \(\ell<u\).
All intermediate values are bad. Write
\[
 L=u-\ell,\qquad g=|f(u)-f(\ell)|.
\]
Equation (1) gives \(g^2\le C^2L\).

If \(g=0\), offer that common good row at every intermediate rank.
This is the cap endpoint operation. Suppose instead that \(g>0\) and
\(L\ge16\). Set
\[
 d=\left\lceil\frac{g^2}{4C^2}\right\rceil,
 \qquad w=d-1.                                            \tag{2}
\]
Choose any integer
\[
 p\in\mathcal P_{\ell,u}:=
 \left[\ell+\lceil L/4\rceil,
       \ell+\lfloor3L/4\rfloor-d\right]\cap\mathbb Z,
 \qquad q=p+d.                                            \tag{3}
\]
Offer \(f(\ell)\) at ranks \(\ell<r\le p\), and offer
\(f(u)\) at ranks \(q\le r<u\). Leave the \(w\) ranks
\(p<r<q\) unavailable in this parity. They form its forced barrier.
The choice set in (3) is nonempty: \(d\le\lceil L/4\rceil\),
and in fact
\[
 |\mathcal P_{\ell,u}|\ge L/8\qquad(L\ge16).              \tag{4}
\]
For a nonreturn interval with \(L<16\), retain its original unavailable
interior. This harmless finite-size convention avoids rounding cases.

The new unavailable count in a nonreturn interval is at most
\[
 \min\left\{L-1,\frac{g^2}{4C^2}+14\right\}.             \tag{5}
\]
For a long interval it is strictly less than \(g^2/(4C^2)\).

## 2. All interval choices preserve a uniform geometric bound

Apply the operation independently to every unavailable interval. The
resulting partial good-row function has Hölder constant at most \(2C\),
uniformly over every choice in (3).

Within one interval, two points using the same anchor row have equal
values. Points using opposite anchor rows are at rank distance at least
\(d\), so (2) gives their required \(2C\) bound. Return intervals
have one constant value.

For an inserted point in the left part of a nonreturn interval, its rank
is at most \(\ell+3L/4\). Its distance to the left anchor is therefore
at most three times its distance to the right boundary. The reflected
statement holds for a right-part insertion. When comparing points in
different unavailable intervals, choose the facing anchor for a return
interval and the assigned anchor for a nonreturn interval. Any excess
of the anchor distance over the point distance is at most three times
the intervening portions inside the two intervals. These portions are
disjoint parts of the point-to-point rank segment. Thus the chosen
anchors are at distance at most four times the point distance. Applying
(1) proves the \(2C\) bound. The same comparison applies when only
one point is inserted and the other is an original good rank.

This proof uses only good anchor values and (1). It does not require a
bound on the lengths of bad-row runs, or on the distances between good
rows.

## 3. Apply the operation separately to the two cap palettes

The clipped Hilbert virtual functions have good values at the first and
last rank, so the preceding construction applies to both parities. A rank
with an unavailable even option has a good odd option, and conversely.
The two original unavailable rank sets are disjoint.

At every newly filled rank, retain its old good singleton option and add
the copied good option of the other parity. Choose exactly one of the
available rows when the singleton is eventually assigned. At a surviving
genuine double, retain its original pair. Such a double had two good
options already, so it is unaffected by this operation.

The surviving row functions of each parity satisfy the \(2C\) bound
uniformly over all singleton selections. Every rank remains occupied,
and all row values are good. There is no new double label and no change
to the previously specified relocation set or excess count. The stride
can be enlarged by a fixed factor of four before choosing the good-row
filters, so that the same-parity distance exclusion uses the new constant.
Any locality-dependent R2s filters must use that enlarged constant too.

Only barrier ranks remain intrinsically forced. Their surviving good
row is unchanged. Thus any direct intrinsic odd-to-even P edge after
this operation was already an edge between the original forced rows.
The added options cannot create a new *intrinsic direct* edge. They can
create P edges involving optional choices, and can create mixed supports.

## 4. A weighted hitting criterion

Choose the parameter \(p\) uniformly and independently for every long
nonreturn interval in both parities. A fixed interior rank belongs to
the barrier for at most \(w\) choices of \(p\). Therefore its
probability of remaining intrinsically forced is at most
\[
 \pi(r)=
 \begin{cases}
 0,&\text{its interval is a return interval},\\
 1,&\text{its nonreturn interval has }L<16,\\
 \min\{1,2g^2/(C^2L)\},&\text{its interval has }L\ge16.
 \end{cases}                                               \tag{6}
\]
The sharper value \(\min\{1,w/|\mathcal P_{\ell,u}|\}\)
can always replace the last line.

Let \(\mathcal E\) be the original direct P edges from intrinsically
forced odd objects to intrinsically forced even objects, at fixed ranks.
The two endpoints of such an edge lie in intervals of different missing
parities. Their barrier choices are independent. Consequently
\[
 \mathbb E\#\{\text{remaining direct intrinsic P edges}\}
       \le\sum_{(r,s)\in\mathcal E}\pi(r)\pi(s).          \tag{7}
\]
If the right side is less than one, some choices of the barriers remove
every direct intrinsic forced edge. Equivalently, the ranks that acquire
new parity options form a vertex cover of \(\mathcal E\), with a
uniform geometric extension already proved in Section 2.

Equation (7) is also useful without the less-than-one hypothesis: it
charges a residual edge to two localized nonreturn intervals, weighted
by their squared endpoint-row gaps relative to their rank spans. It is
more informative than a count of all forced vertices or all P edges.

The current \(h^{23/12+o(1)}\) incidence estimate does not bound the
weighted sum in (7) by less than one. Intervals with \(L\) comparable
to \(g^2/C^2\) can have survival weight of constant order. Proving a
useful weighted estimate for the actual R2s filters is still required.
Even if (7) removes every direct forced edge, the full singleton P test
also excludes directed paths through optional objects and forces caused
by fixed genuine doubles. Those conditions and the higher-arity families
are not settled here.

Independent review checked the complete written argument, including the
cross-interval facing-anchor comparison, the integer placement count,
empty barriers, return intervals, and independence between opposite
missing parities. The stated geometric and direct-edge conclusions passed.
