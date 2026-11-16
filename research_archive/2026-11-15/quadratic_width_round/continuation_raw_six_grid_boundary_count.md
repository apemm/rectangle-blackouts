# Dyadic row boundaries are a sparse part of the raw six-point count

15 November 2026. A counting partition removes the raw row-boundary
cases from the long same-parity parked-six problem at subquadratic
expected cost. It does not delete physical rows or change the cap
construction. In the remaining raw candidates, both nearby hub rows
and nearby partner rows share their high dyadic row bits.

The estimate concerns uncapped raw coordinates, or four raw values on
one common affine branch of the fold. General cap-constant candidates
and fold-branch crossings remain separate.

## 1. Uniform first-partner count at a fixed hub

Use the notation of
[the raw same-parity reduction](continuation_same_parity_raw_6pt_reduction.md).
The Hilbert square has side \(N=\Theta(h)\), its chosen coordinate is
\(f\), and the physical row formula is \(\rho+D(f(r)-U)\).
The stride \(S\) and row step \(D\) are fixed. The common row offset
\(U\) is uniform on an interval of \(\Theta(h)\) integers.

Let the support span be at least \(h^2/K\), where \(K\) is a fixed
power of \(\log h\) or smaller. The local-anchor estimates give
\[
 |\xi_i|,|t|\le CK,
 \qquad |\ell|\ge ch/K,
 \qquad |f(r+t)-f(r)|\le C\sqrt K.
 \tag{1}
\]
There are \(O(K^2)\) sea-offset pairs. Their difference fixes the
hub rank displacement \(t\).

For a fixed hub \(r\), offsets, and vertical increment \(D\ell\),
the first partner lies in one row and one rank progression:
\[
 f(p)=f(r)-\ell,
 \qquad p\equiv r\pmod {d_\ell},
 \qquad d_\ell=\frac{|D\ell|}{\gcd(|D\ell|,|S\xi_1|)}.
 \tag{2}
\]
In particular \(d_\ell\ge ch/K^2\). The uniform row/progression
packing bound gives
\[
 \#\{p\text{ satisfying (2)}\}
 \le C(N/\sqrt{d_\ell}+1)\le C\sqrt h K.
 \tag{3}
\]
There are only \(O(h)\) possible \(\ell\)'s. The affine partner
relation fixes the second partner after the first is chosen. Thus the
number of positional candidates at each fixed hub and offset pair is
at most
\[
 C h^{3/2}K.
 \tag{4}
\]
This is a uniform bound, rather than an average over hubs. Every accepted
candidate fixes at most one \(U\), so its probability is at most \(C/h\).

## 2. Exceptional hub rows

Choose a power of two \(R\) dividing \(N\), and assume
\(CK\ll R\le N\). Partition coordinate values into the intervals
\([jR,(j+1)R-1]\). Let \(\mathcal B\) consist of values within
\(B=C_2K\) of one of their boundaries, with \(C_2\) large enough
for (1). Then
\[
 |\mathcal B|\le C NB/R=O(hK/R).
 \tag{5}
\]
Every raw coordinate value is visited at exactly \(N\) ranks.
Consequently the number of hubs with \(f(r)\in\mathcal B\) is
\(O(h^2K/R)\). Use (4), sum the offset pairs, and multiply by the
single-offset probability \(C/h\). These candidates contribute at most
\[
 C h^{5/2}K^4/R
 \tag{6}
\]
in expectation.

If \(f(r)\notin\mathcal B\), the two hub values \(f(r),f(r+t)\)
belong to the same dyadic row interval. Both therefore have the same
high \(\log_2(N/R)\) row bits.

## 3. Exceptional partner rows must also be removed

The hub exclusion alone does not align the partners' row bits. For each
fixed hub, the first partner row is \(f(r)-\ell\). At most
\(|\mathcal B|=O(hK/R)\) values of \(\ell\) place it in
\(\mathcal B\). For each such increment, (3) gives
\(O(\sqrt h K)\) first partners. Summing all \(O(h^2)\) hubs and
\(O(K^2)\) sea-offset pairs and dividing by the offset interval length
again gives (6).

Outside these two exceptional families, both equalities
\[
 \left\lfloor\frac{f(r)}R\right\rfloor
 =\left\lfloor\frac{f(r+t)}R\right\rfloor,
 \qquad
 \left\lfloor\frac{f(p_1)}R\right\rfloor
 =\left\lfloor\frac{f(p_2)}R\right\rfloor
 \tag{7}
\]
hold. The second uses the exact row relation
\(f(p_2)-f(p_1)=f(r+t)-f(r)\).

Taking a nearest admissible power of two \(R\asymp h^{3/4}\)
bounds the total exceptional expectation by
\[
 h^{7/4+o(1)}.
 \tag{8}
\]
More generally any fixed \(1/2<\varepsilon<1\), with
\(R\asymp h^\varepsilon\), gives
\(h^{5/2-\varepsilon+o(1)}\).

## 4. What transfers to the refined and folded union

A fixed refinement and a bounded permutation replace each original rank
by one of a bounded number of ranks at bounded distance, and each row
index by a bounded integer shift. Enumerate these choices first.
The first-partner condition remains a rank progression, possibly with
a shifted residue and with its modulus reduced by a fixed factor.
The lower bound \(ch/K^2\) and (3) remain valid after changing constants.
The same is true of the number of eligible \(\ell\)'s and of the
bounded multiplicity of raw hubs. Increase the grid-boundary thickness
by a fixed constant to include the row shifts. Thus (6)--(8) hold for
that finite raw-candidate union as well.

They also hold if all four row values use one common nonconstant affine
fold branch. Its sign may reverse; applying that common affine formula
to the coordinate differences changes only signs and fixed origins.
No alignment between the sampled offset and the dyadic grid is needed:
the grid is defined on raw coordinate values and partitions the count.

This argument does not apply to a cap-constant plateau. A fixed raw
coordinate value has exactly \(N\) Hilbert visits, but a selected cap
value can occupy many more ranks. Nor does (7) automatically follow when
the four values use different fold branches. Those subfamilies need
separate estimates.

## 5. Remaining structural target

After this counting partition, the raw affine-row correlation can be
studied with matching high row bits on each of its two nearby row pairs.
This is a valid simplification of a simultaneous Hilbert recursion.
It does not prove contraction of that recursion under the rational rank
map, classify all exceptional affine symmetries, or solve any residual
choice system. The
[exact dyadic-reflection count](continuation_dyadic_reflection_six_count.md)
handles one such symmetry subfamily separately.

These are expectation bounds over unconditioned row offsets. Turning
them into an occupancy-preserving repair, or combining them with a
particular previously chosen offset, requires its own justification.

Independent review: pending the written boundary-count audit.
