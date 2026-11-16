# A polynomially shorter window for the remaining six-point supports

15 November 2026. In the independently stretched two-arm scaffold,
all parked-six supports with span greater than \(h^{2-\kappa}\)
have subquadratic incidence for every fixed
\[
 0<\kappa<1/42.
 \tag{1}
\]
This includes nonconstant caps, opposite fold arms, and random anchor
hubs. The conclusion is an incidence bound with an explicit positive
exponent margin. It does not provide an occupancy-preserving repair
or prove the complete quadratic-width construction.

## 1. Keep the polynomial factors

Put \(K=h^\kappa\), and apply the long-support reduction at span
\(h^2/K\). Choose a cap-side cutoff \(L_*=h^l\), rounded dyadically,
and a near-top anchor window of width \(E=h^e\). The original labels
in the top window of width \(2E\) are relocated as in the
[independent-arm scaffold](continuation_independent_arm_v_map.md).

The source local-anchor geometry needs \(h^2/K\gg h\).
The three-row sampling estimate needs
\[
 h/K\gg\sqrt K.
 \tag{2}
\]
These hold whenever \(\kappa<1\) and \(\kappa<2/3\), respectively.
They do not require \(K\) to be polylogarithmic.
All divisor arguments have magnitude bounded by a fixed power of \(h\),
so their divisor counts remain \(h^{o(1)}\).

The bad-row bound stays \(b=h^{5/6+o(1)}\). Thus
\[
 \Pr(\text{some selected cap has side}>L_*)
 \le h^{11/6-2l+o(1)}.
 \tag{3}
\]
In particular, take \(l>11/12\).

## 2. Nonanchor same-parity supports

Retain the explicit factors in
[the two-arm nonanchor count](continuation_two_arm_nonanchor_six_count.md).
There are \(O(K^2)\) offset pairs, \(O(\sqrt K)\) possible integer
hub-row differences, and a prescribed-increment probability factor
\(CK/h^2\). The weighted partner-distance kernel contributes at most
\[
 Ch^3\left[L_*+(\sqrt K+\log h)\log^2h\right]
 \tag{4}
\]
after summing dyadic partner depths. Hub ancestors and divisor choices
contribute only \(h^{o(1)}\).

The same-arm count is bounded in the same way, using the near-row mass
instead of the reciprocal kernel. Therefore
\[
 \mathbb E N_{\mathrm{nonanchor}}
 \le h^{1+o(1)}K^{7/2}
       \left[L_*+\sqrt K\,h^{o(1)}\right].
 \tag{5}
\]
In the parameter range used below, \(L_*\gg\sqrt K\), so its exponent
is
\[
 1+l+\tfrac72\kappa.
 \tag{6}
\]

## 3. Same-parity anchor hubs

Choose \(e<1-\kappa\). Then \(E=o(h/K)\), so no anchor can be a
partner in a long support. The anchor is good and its maximum atom is
\[
 h^{o(1)}/E.
 \tag{7}
\]
The prime-gap even pool and the odd pool remain available at the
near-one exponents used below. The fixed bad-row set has smaller
order than either pool.

In
[the random-anchor hub count](continuation_random_anchor_hub_six_count.md),
the retained polynomial factors are \(K^2\) for the offsets and
\(\sqrt K\) for the integer hub difference. The conditional
two-partner row estimate has no additional factor \(K\).
Thus
\[
 \mathbb E N_{\mathrm{anchor}}
 \le h^{2+o(1)}K^{5/2}L_*/E.
 \tag{8}
\]
Its exponent is
\[
 2+l-e+\tfrac52\kappa.
 \tag{9}
\]

## 4. Opposite-parity supports

The candidate list in
[the opposite-parity count](continuation_two_arm_opposite_parity_six_count.md)
has size \(h^{5+o(1)}K^4\): two offset choices contribute \(K^2\),
and the second partner progression contributes the other \(K^2\).

For a prescribed increment, a nonanchor triangle has probability at
most \(CK/h^2\). An anchor-hub triangle has probability at most
\(h^{o(1)}/(hE)\). Since \(e<1-\kappa\), the latter is the larger
bound for sufficiently large \(h\). Parity independence therefore gives
\[
 \mathbb E N_{\mathrm{opposite}}
 \le h^{3+o(1)}K^4/E^2.
 \tag{10}
\]
Its exponent is
\[
 3+4\kappa-2e.
 \tag{11}
\]
This bound itself does not require the cap-size cutoff.

## 5. An explicit compatible choice

For a fixed \(\kappa\) satisfying (1), put
\[
 g=\frac1{12}-\frac72\kappa>0,\qquad
 l=\frac{11}{12}+\frac g4,\qquad
 e=1-\kappa-\frac g4.
 \tag{12}
\]
Then \(l>11/12\), \(e<1-\kappa\), and \(e\) remains close to one.
The cap failure probability (3) is
\[
 h^{-g/2+o(1)}=o(1).
 \tag{13}
\]
The respective exponents (6), (9), and (11) are
\[
 2-\frac{3g}{4},\qquad
 2-\frac g2,\qquad
 1+6\kappa+\frac g2.
 \tag{14}
\]
Each is strictly below two. Hence, for some
\(\eta_\kappa>0\),
\[
 \mathbb E N_{\mathrm{long}}\le h^{2-\eta_\kappa+o(1)}
 \tag{15}
\]
on the deterministic short-cap candidate family.
Joint averaging excludes larger selected caps and retains this
incidence bound. The argument does not condition triangle
probabilities on the cap event.

The top-window relocation has internal cost
\[
 h^{1+e+o(1)}
 =h^{2-\kappa-g/4+o(1)}=o(h^2),
 \tag{16}
\]
and the cap-relocated labels retain cost \(h^{11/6+o(1)}\).
The same strict margins absorb the stated subpolynomial relocation
factor in the incidence accounting when a valid support repair is
separately available.

## 6. What the window statement means

The new counting cutoff is \(h^{2-\kappa}\), for any fixed
\(\kappa<1/42\). The result applies to the complete long parked-six
family in the stated enlarged two-arm scaffold, with its fixed-size
candidate refinements and anchor extensions.

It does not say that the counted supports can all be removed while
keeping every core slot occupied. Some supports involve only singleton
options, and repairing one family can create an occupancy requirement
elsewhere. It also does not resolve P or the remaining three- and
four-point systems. Those obligations remain part of the full-board
problem.

Independent review: the complete written proof passed a separate review
of the geometric parameter range, retained \(K\)-powers, prime-anchor
pool range, strict exponent margins, and incidence-only conclusion.
