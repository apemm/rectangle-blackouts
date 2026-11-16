# One Pythagorean direction reduces to a path matching problem

15 November 2026. For one fixed Pythagorean slope, the same-parity distance
exclusion makes the singleton implication graph a union of paths after
the large own-gap cutoff. Movable genuine doubles can then be placed
exactly when a finite bipartite matching condition holds. This is a
positive choice theorem for one direction, not a proof of its uniform
Hall hypothesis or a simultaneous solution for several directions.

## 1. Every vertex has at most one predecessor and successor

At each inserted column \(x_v\), let \(a_v,b_v\) be its total odd and
even virtual row options. Assume each parity graph has no nonhorizontal
integral distance. Fix a nonzero rational slope
\[
 \mu=q/p,\qquad p>0,\qquad p^2+q^2=z^2,
 \qquad \gcd(p,q)=1,                                    \tag{1}
\]
where the integers \(q,z\) are nonzero. This is one unoriented line
direction; slope \(-\mu\) is a different direction unless zero.

Draw a directed edge \(u\to v\) when the odd option at \(u\) and
the even option at \(v\) give a P constraint along a line of slope
\(\mu\). It is enough to retain actual in-strip constraints; omitting
owner or endpoint conditions only gives a sufficient overgraph.

Two even neighbors of one odd point would lie on the same rational
Pythagorean line. The difference of any two integer points on that line
is an integer multiple of \((p,q)\), and has integral nonhorizontal
length. This contradicts the even-parity distance exclusion. Thus
outdegree is at most one. The same argument for odd neighbors gives
indegree at most one.

## 2. Large own gaps exclude cycles

Assume all considered vertices satisfy
\[
 |d_v|=|b_v-a_v|\ge B_h,\qquad B_h/\sqrt h\to\infty,
\]
and the total virtual functions have the usual fixed square-root locality
bound. An actual in-strip edge has horizontal and rank distance \(O(h)\).
Consequently
\[
 b_v-a_u=d_u+O(\sqrt h)=d_v+O(\sqrt h).                  \tag{2}
\]
For sufficiently large \(h\), an edge preserves the sign of \(d_v\),
and its horizontal displacement has sign
\(\operatorname{sgn}(d_u/\mu)\). This sign is constant along a
connected directed component. Columns therefore increase strictly along
the component, or decrease strictly. There are no directed cycles.

Together with Section 1, every nontrivial component is a directed path.
Vertices with a small virtual own gap do not satisfy this conclusion and
must be treated separately. The statement applies to the induced system
after their exclusion, not automatically to forced unsafe singleton rows.

## 3. Exact matching criterion for movable doubles

Suppose singleton choices use one of the two virtual rows, with some
intrinsically forced odd or even values. Each genuine object has a finite
set of allowable slots at which both options are good and its double
could be placed. Different objects have disjoint allowable slots, as in
private-slot constructions. Every object must be doubled exactly once;
all other slots remain singletons.

On a path \(v_1\to\cdots\to v_n\), singleton P avoidance says that
odd choices cannot be followed later by even choices. Let
\(\ell\) be the last forced-even position, or zero if absent, and
\(u\) the first forced-odd position, or \(n+1\) if absent.
The intrinsic singleton system is feasible precisely when \(\ell<u\).
A double may occur only at an available position
\[
 \ell<j<u.                                               \tag{3}
\]
It forces every preceding vertex to be even and every following vertex
to be odd. Hence at most one double may lie on each path.

Form a bipartite graph whose left vertices are genuine objects and whose
right vertices are directed paths. Join an object to a path if one of its
allowable slots satisfies (3). Then the one-direction P system is solvable
if and only if all intrinsic path systems are feasible and this bipartite
graph has a matching covering every object.

Necessity follows from the preceding paragraph. For sufficiency, choose
one allowed slot on each matched path. Fill before that slot evenly and
after it oddly, putting its object's double at the slot. On unmatched
paths, choose any threshold between the forced-even and forced-odd
positions. This fills every column and excludes every edge of the chosen
direction.

Equivalently, the remaining condition is Hall's inequality: every family
of objects must have at least that many available path neighbors. One
simple sufficient condition is that each object meets at least \(K\)
available paths and each path meets at most \(K\) objects. Counting
bipartite edges proves Hall's inequality directly.

If the allowable slots of an object have diameter less than the minimum
P gap, then monotonicity from Section 2 puts its slots on distinct paths.
This gives many path neighbors when the slots remain inside the forced
window (3). It does not bound how many different objects one long path
can meet.

## 4. The remaining mathematical requirements

The near-linear gap cutoff makes each fixed private block shorter than
every remaining edge, so the final distinct-path observation applies to
band-safe available choices. A uniform path-incidence or Hall bound would
therefore give a genuine bounded-width repair for this one direction.
Neither the gap cutoff nor the degree-one property proves that bound.

In fact, those abstract hypotheses alone cannot prove a uniform private
palette theorem. Fix any \(M\ge1\), put
\[
 X_0=4M,\quad Y_0=4M^2-1,\quad Z_0=4M^2+1,
\]
and take a large \(t\equiv1\pmod4\). Use \(M+1\) objects,
indexed \(i=0,\ldots,M\), with
\[
 h=8Y_0t,\quad a=4Y_0t+3,\qquad
 a_i=a+4i,\quad b_i=a+Y_0t+4(i-1).
\tag{4}
\]
Their private columns are \(4(Mti+j)\), \(0\le j<M\).
At every common private offset \(j\), the edge \(i\to i+1\)
has vector \((X_0t,Y_0t)\), an integral multiple of the same
Pythagorean direction. Its vertical alternative rows are
\[
 a+4i-t,\qquad a+4i+4M^2t,
\]
both in the strip for sufficiently large \(t\). The own gaps,
P slot gaps, and half-factors are all \(\Theta_M(h)\). Distinct
objects have distinct row pairs, and all their same-parity private
options satisfy \((\Delta y)^2<2|\Delta x|\) when \(t\) is large.

Each common-offset path can contain at most one double. There are only
\(M\) offsets but \(M+1\) objects, so the compulsory double placement
is impossible even for this one-direction subsystem. This is an exact
path-consumption obstruction for every fixed private size \(M\).
As a rectangle obstruction it presumes the indicated remote owners are
available. No actual Hilbert embedding, good-row survival, or complete
higher-support audit is asserted. An argument using additional structure
of the actual folded order is still possible, but the abstract locality,
large-gap, and degree-one assumptions alone are insufficient.

Combining opposite slopes or different primitive directions increases
indegree and outdegree and can create directed cycles. The path matching
criterion does not extend automatically to that union. Similarly, new
slot choices must still preserve the geometric hypotheses and higher-arity
exclusions of the actual core construction.

## Review status

The full note passed an independent written review, including the degree-one
property, own-gap sign, forced windows, exact matching criterion, and the
all-size private-path obstruction. The actual Hilbert embedding and owner
qualifications remain explicit.
