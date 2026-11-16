# Weighted cap rows extend the stretched six-point count

15 November 2026. Under the uniform two-parameter triangle estimate,
the physical-divisor argument extends to nonconstant central cap
values. With the reviewed \(h^{5/6+o(1)}\) bad-row bound, the expected
long same-parity six-point count is
\(h^{23/12+\varepsilon+o(1)}\) for any fixed
\(0<\varepsilon<1/12\).

The
[reviewed mechanical sampling lemma](continuation_mechanical_triangle_sampling.md)
supplies the probability input below. The stated cap geometry and
bad-child probability remain explicit hypotheses. Fixed physical anchor
plateaus and pairs on different fold branches remain outside its scope.

## 1. Cap hypotheses and central candidates

Use a padded \(N\times N\) Hilbert square, \(N=\Theta(h)\).
An aligned dyadic square of side \(L\) occupies one rank interval
of length \(L^2\). Its cap value in a specified coordinate is a
boundary value
\[
 c_Q=jL\quad\hbox{or}\quad c_Q=(j+1)L-1.
 \tag{1}
\]
The actual orientation can restrict which side and coordinate occur.
Counting both choices only enlarges the family.

A central candidate at any rank of this node has physical row
\[
 g_\theta(c_Q-U),
 \tag{2}
\]
with the same central monotone bounded-gap map and the same index
offset as the raw core. Raw points can be included as side-one
candidates. Bounded row shifts and the fixed interpolation multiplicity
change the constants only when their candidate-union hypotheses are
verified.

Assume the realized total cap functions retain the reviewed square-root
locality bound. Thus nearby hubs at rank distance \(O(K)\) have physical
row difference \(O(\sqrt K)\).

The probabilistic input is uniform: for every two prescribed central
candidate indices at the first hub and partner, the probability of
their prescribed first parked triangle with a long nonzero increment
is at most \(P_h\). The statement includes the listed ancestor choices
before conditioning on which caps are selected.

## 2. Weighted near-row pairs at unequal depths

Fix a coordinate and a dyadic side \(L\). For each potential cap node,
assign all \(L^2\) ranks of its interval to its boundary value \(c_Q\).
Let \(M_L(c)\) denote the resulting rank mass at value \(c\).
There are at most \(C N/L\) squares at one boundary coordinate.
Consequently
\[
 M_L(c)\le CNL.
 \tag{3}
\]
The support of \(M_L\) lies in the union of two arithmetic grids of
step \(L\), and its total mass is \(O(N^2)\).

For sides \(L_1,L_2\) and \(W\ge1\), define the weighted pair count
\[
 \mathcal P(L_1,L_2;W)
 =\sum_{|c_1-c_2|\le W}M_{L_1}(c_1)M_{L_2}(c_2).
 \tag{4}
\]
For a fixed \(c_1\), there are at most \(C(W/L_2+1)\) permitted
values of \(c_2\). Using (3) and the total mass at level \(L_1\),
\[
 \mathcal P(L_1,L_2;W)
 \le CN^3(W+L_2).
 \tag{5}
\]
Interchanging the two sides gives the sharper symmetric bound
\[
 \mathcal P(L_1,L_2;W)
 \le CN^3\bigl(W+\min(L_1,L_2)\bigr).
 \tag{6}
\]
No equality of depths or cap orientations is assumed.

If both partner rows use central candidates and their physical row
difference is \(O(\sqrt K)\), monotonicity and bounded positive gaps
force \(|c_1-c_2|\le C\sqrt K\). Summing (6) over the
\(O(\log h)\) side choices up to \(L_{\max}\) gives at most
\[
 CN^3(L_{\max}+\sqrt K)\log^2h
 \tag{7}
\]
candidate partner pairs, including their ancestor labels. This counts
all potential nodes, rather than conditioning on the selected caps.

## 3. Large selected caps are rare

Assume each selected good cap node has a bad-cap child. This is the
reviewed first-good-ancestor construction. Also assume that each
potential child's cap coordinate is bad with unconditional probability
at most \(Cb/h\), where
\[
 b=h^{5/6+o(1)}.
 \tag{8}
\]
The source random-embedding argument supplies this bound when each
bad physical row has only \(O(1)\) index preimages. A fixed good anchor
cannot be a bad witness.

If a selected cap has side greater than \(L_{\max}\), a bad witness
child has side greater than \(L_{\max}/2\). Summing the numbers of
potential nodes over these dyadic levels gives \(O(N^2/L_{\max}^2)\).
A union bound therefore yields
\[
 \Pr(\text{some selected cap has side}>L_{\max})
 \le C h b/L_{\max}^2.
 \tag{9}
\]
Choose a dyadic threshold
\[
 L_{\max}\asymp h^{11/12+\varepsilon},
 \qquad 0<\varepsilon<1/12.
 \tag{10}
\]
Then the right side of (9) is \(h^{-2\varepsilon+o(1)}=o(1)\).

The small-cap incidence estimate below remains unconditional.
Equation (9) can be combined with it in a joint parameter selection.
One does not condition the triangle probability on the absence of
large selected caps.

## 4. Apply physical divisibility

Use the exact identities from
[the stretched partner-divisor count](continuation_stretched_partner_divisor_count.md):
\[
 \Delta=p_1-p_2+t,\qquad
 S^2t(r-p_1)=S\xi_2\Delta-\delta v,\qquad
 \delta\mid S\xi_1\xi_2\Delta.
 \tag{11}
\]
For long supports, \(\Delta\ne0\). This conclusion uses only actual
hub locality and the in-strip bound \(|\delta|<h\), so it survives
cap selection.

For every candidate partner pair from (7), enumerate the signed
divisors \(\delta\), the \(O(\sqrt K)\) possible integer values of
the actual hub difference \(v\), and the unique rank \(r\) supplied
by (11). Enumerate the first hub's \(O(\log h)\) central ancestor
candidates. The second hub's row condition may be discarded for an
upper bound. All enumerated indices precede the random parameters.

After the \(O(K^2)\) offset choices and the elementary divisor bound,
the candidate count is at most
\[
 h^{3+o(1)}(L_{\max}+\sqrt K)
 \tag{12}
\]
for polylogarithmic \(K\). Every actual witness determines one of these
candidates, whose first triangle occurs with probability at most \(P_h\).
Thus
\[
 \mathbb E N_{\mathrm{central},\,L\le L_{\max}}
 \le P_h\,h^{3+o(1)}(L_{\max}+\sqrt K).
 \tag{13}
\]
If \(P_h\le h^{-2+o(1)}\), equations (10) and (13) give
\[
 \mathbb E N_{\mathrm{central},\,L\le L_{\max}}
 \le h^{23/12+\varepsilon+o(1)}.
 \tag{14}
\]
The exponent is strictly below two. Together with (9), this permits a
joint choice with no larger selected caps and the displayed incidence
bound. Other nonnegative objectives can be included by the usual joint
Markov selection.

The minimum in (6) also gives a sharper mixed-depth consequence. If
at least one partner cap has side at most \(L_0\), allow the other
partner and both hubs to have arbitrary dyadic sides up to \(N\).
The same proof gives
\[
 \mathbb E N_{\min(L_1,L_2)\le L_0}
 \le h^{1+o(1)}(L_0+\sqrt K).
 \tag{15}
\]
In particular, a raw/cap partner pair has expected count \(h^{1+o(1)}\)
without truncating the cap side. The larger exponent in (14) is needed
only for pairs with two large capped partners. This statement still
requires central, nonconstant candidate formulas at every endpoint
used by the probability argument.

## 5. Scope

The estimate includes both capped partners, unequal cap depths, and
raw/cap mixtures, provided every endpoint used by the triangle
probability has a nonconstant central candidate formula. It also extends
to a prescribed common injective fold branch if its boundary-coordinate
grids differ only by fixed signs and translations.

Fixed physical anchors do not satisfy the assumed first-triangle
probability in all cases. Partners on different fold branches need not
have nearby raw cap indices, so (7) is not automatically available.
The incidence bound alone also does not specify a safe erasure.
Those limitations are separate from the weighted mass estimate (6).

Independent review: the complete written proof passed a separate review
of the unequal-depth weighted mass, rare-large-cap estimate,
parameter-independent divisor list, and unconditional expectation.
