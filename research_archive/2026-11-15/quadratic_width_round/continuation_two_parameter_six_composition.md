# A two-parameter probability unlocks the coarse six-point count

15 November 2026. This is a conditional counting theorem. A uniform
\(h^{-2+o(1)}\) probability for one prescribed long parked triangle
would combine with the proved Hilbert affine-section estimates to give
a subquadratic same-parity count for each fixed nonreflection slope.
No such probability is assumed to follow from the original single
row-offset model.

## 1. Explicit hypotheses

Let \(H_N\) be a raw Hilbert square, \(N=\Theta(h)\), and let core
columns be \(Sp\), with fixed stride \(S\). A random row map is applied
to one coordinate \(f(p)=H_N(p)_\alpha\). Require:

1. Its physical row increments are bounded above and below by fixed
   multiples of raw index increments, up to a fixed additive error.
2. For every fixed hub \(r\), first partner \(p_1\), nonzero sea offset
   \(\xi_1\), and fixed sea row, the probability of the prescribed first
   parked triangle with the required long nonzero increment is at most
   \(P_h\). This is an unconditional probability bound.
3. The first triangle's positional indices are chosen before the random
   parameters. The estimate is uniform over any bounded candidate
   choices included in the model.

The proposed random mechanical stretch is a possible source of
Hypothesis 2. Its proof and its compatibility with caps, interpolation,
and row exclusions are separate from this theorem.

Fix a pair of offsets \(\xi_1,\xi_2\ne0\), with
\[
 |\xi_i|\le CK,\qquad
 t=(\xi_1-\xi_2)/S\in\mathbb Z\setminus\{0\}.
 \tag{1}
\]
Consider common-completion pairs with hubs \(r,r+t\), common physical
increment \(\delta\), and partners \(p_1,p_2\). Their exact relation is
\[
 \xi_2p_2-\xi_1p_1
 =(\xi_2-\xi_1)r+\xi_2t-\delta v/S,
 \tag{2}
\]
where \(v\) is the physical row difference between the hubs.

Hilbert locality and Hypothesis 1 imply
\[
 |v|\le C\sqrt K,\qquad
 |f(p_2)-f(p_1)|\le C\sqrt K.
 \tag{3}
\]
Also \(|\delta|<h\) for an in-strip event.

## 2. Coarse candidate positions

Choose a dyadic tile side \(R\mid N\), write \(Q=N/R\), \(B=R^2\),
and assume
\[
 B\ge C h\sqrt K.
 \tag{4}
\]
Write \(p_i=BJ_i+e_i\), \(0\le e_i<B\).
For a fixed hub \(r\), equation (2) shows that
\[
 \xi_2J_2-\xi_1J_1
 \tag{5}
\]
belongs to \(O(K)\) integer values. The bounded correction
\(\delta v/S\) is absorbed by (4). The list is determined by \(r\)
and the positional parameters, without fixing their random values.

Call a raw coordinate row exceptional if it is within \(C\sqrt K\)
of an \(R\)-grid boundary. There are
\(O(N\sqrt K/R+1)\) such rows. If \(f(p_1)\) is not exceptional,
(3) puts both partner rows in the same coarse row
\[
 Y=\lfloor f(p_1)/R\rfloor=\lfloor f(p_2)/R\rfloor.
 \tag{6}
\]

For a slope \(a/b\), define the averaged affine-section quantity
\[
 \mathcal A_Q(a,b)=
 \sum_{Y=0}^{Q-1}\ \max_{c\in\mathbb Z}
 \#\{(J_1,J_2):
       H_Q(J_i)_\alpha=Y,\ aJ_2-bJ_1=c\}.
 \tag{7}
\]
One can maximize over the finitely many coordinate-complement states
as well. This changes only a fixed factor.

For each coarse pair, there are at most \(R^2\) first-partner
positions. No enumeration of the fine second partner is needed:
the event requires that at least one second partner exists in that
coarse tile. Thus for each hub, the number of nonexceptional first
partners that can participate is at most
\[
 CK R^2\mathcal A_Q(\xi_2,\xi_1).
 \tag{8}
\]
This is a deterministic superset, chosen before the random row map.
Overcounting the same first partner in several coarse pairs is harmless.

There are \(O(N^2\sqrt K/R+N)\) exceptional first-partner ranks.
The extra \(N\) term is absorbed by the first term when \(R\le N\)
and \(K\ge1\).

## 3. Count distinct prescribed first triangles

Let \(Z\) count the distinct prescribed first triangles
\((r,p_1,\xi_1,s)\) that belong to at least one common-completion pair
with the fixed offsets. By Hypothesis 2 and the deterministic candidate
superset,
\[
 \mathbb E Z
 \le C P_h\left(
       K N^2R^2\mathcal A_Q(\xi_2,\xi_1)
       +N^4\sqrt K/R\right).
 \tag{9}
\]
This counts first triangles rather than all witnesses. It is exactly
the useful incidence count if removing or modifying their supports is
separately permitted. It is not automatically a count of all distinct
six-point witnesses, since one first triangle might have several
second partners as the random parameters vary.

For a fixed realized row map and fixed first triangle, however, the
common increment \(\delta\), hub difference \(v\), and equation (2)
determine the second partner rank uniquely. Thus the realized witness
count is also at most a fixed multiplicity times \(Z\), for the fixed
offset pair and sea row. This justifies using (9) for that count.

Suppose
\[
 \mathcal A_Q(a,b)\le C_{a,b}Q^{2-\eta}.
 \tag{10}
\]
Since \(R^2Q^2=N^2\), equations (9)--(10) give
\[
 \mathbb E Z
 \le C_{a,b}P_hN^4
        \left(KQ^{-\eta}+\sqrt K/R\right).
 \tag{11}
\]
With \(P_h\le h^{-2+o(1)}\), fixed offsets, and
\(R\asymp h^{3/4}\), this becomes
\[
 h^{2-\eta/4+o(1)}+h^{5/4+o(1)}.
 \tag{12}
\]
There is no divisor-energy multiplication in this argument. The second
probabilistic parameter is what changes the accounting from the
[one-offset composition](continuation_coarse_progression_composition.md).

## 4. Slopes supplied by the proved section bounds

For each fixed reduced odd rational slope outside
\(\{\pm1,\pm5,\pm1/5\}\), the
[modular affine classification](continuation_hilbert_modular_affine_classification.md)
gives (10) with \(\eta>0\). At slopes
\(\pm5,\pm1/5\), the
[averaged slope-five estimate](continuation_hilbert_affine_carry_automaton.md)
also gives (10), with
\[
 \eta_5=2-\log_2(56)/3>0.
 \tag{13}
\]
Inversion, rank reversal, and the permitted complement states handle
the listed variants. Absolute slope one is not covered by (10).

The sea offsets in a spacing-four constant-sea profile have the same
nonzero residue modulo four, hence the same 2-adic valuation. Their
reduced ratio has odd numerator and denominator, as required.

For a growing offset palette, retain all constants and losses in (11).
The available uniform exponent has size
\[
 \eta\ge c/(\sqrt K\log(2K)).
 \tag{14}
\]
It is not a fixed power saving for arbitrary polylogarithmic \(K\).
A divisor or relocation factor written only as \(h^{o(1)}\) need not
be smaller than this decreasing saving. That comparison must be made
explicitly before claiming an affordable complete palette.

If the actual hubs are coarse anchors with stride divisible by sixteen,
the congruence of their offsets excludes the exceptional absolute
ratios \(1,5,1/5\), apart from the equal-offset case with coincident
hubs. This observation does not extend to arbitrary fine interpolation
endpoints.

## 5. Scope

The theorem is conditional on the uniform first-triangle probability
and the raw bi-Lipschitz row behavior in Section 1. It covers a fixed
nonreflection slope, or a finite palette after taking its minimum
positive exponent. A growing palette, cap-constant endpoints, reflection
slopes, and physical support repair still require their separate
arguments. It does not prove the complete quadratic-width construction.

Independent review: the full written conditional theorem passed a
separate review of the deterministic coarse candidate set, unique
realized second partner, boundary count, and exponent accounting.
