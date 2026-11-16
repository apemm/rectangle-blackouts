# A dirty child controls P incidence at a boundary-clean cap

15 November 2026. A selected boundary-clean cap has a dirty child.
Keeping that witness in the row-sampling calculation gives an additional
bad-row factor. For either the compatible one-coordinate filling or the
two-corner menu, every actual P edge touching a selected cap has expected
total incidence

`h^o(1) [h b + h^(3/2) b/sqrt(E)]`,                  (1)

where b bounds each forbidden-row set and E is the near-top anchor
window. This is an incidence statement. It does not choose compatible
parities for the cap singletons or repair all the counted edges.

## 1. Deterministic witnesses and sampled row forms

Use the [boundary-clean cap rule](continuation_boundary_clean_movable_caps.md)
with either of its two fillings. Every selected cap Q has an immediate
dirty child. Enumerate that child, one of its boundary coordinates d,
and a forbidden physical row z at that coordinate. There are only a
fixed number of child-coordinate choices. The bad row z has at most b
choices in its parity.

Every point in the two-corner menu is a good original endpoint-coordinate
value of Q, or a retained raw-coordinate value from the bounded-size
fallback. In the compatible original filling, the uncapped coordinate
is instead the original raw-coordinate form at that rank. The proof
below treats all these as fixed raw-index candidates in the same way.
Every other retained point is also good. In this exact menu a bad witness
coordinate therefore cannot have the same raw index as an endpoint of
the same parity in the P edge. Coincident exact-menu cases can be discarded.
For a bounded physical-error extension, retain those cases: a zero
index gap leaves only O(1) endpoint values, and the two-row kernel is
O(1/h), so the same calculation below still applies. No zero-gap
extension case is silently removed.

Fix the two rank positions, all potential ancestor and endpoint forms,
and a signed norm height Y. Write the cross-parity equation as

`B-A=Y`.                                             (2)

For a fixed horizontal displacement, there are h^o(1) possible signed
Y by integer norm factorization. All target physical values are fixed
before sampling their own parity parameters.

The row maps have a global bounded-gap Lipschitz bound in raw coordinate
index. Consequently, for raw indices c and d in one parity,

`|F(c-U)-F(d-U)|<=C|c-d|`.                            (3)

The prescribed two-nonanchor-row kernel is

`h^o(1)/[h(1+|c-d|)]`.                               (4)

It holds for the multiscale independent-arm model, including opposite
arms. The one-row nonanchor kernel is C/h. Conditional on the anchors,
the two parity parameter families are independent. The residue-restricted
offset law changes these upper bounds by a fixed density factor.

## 2. Two nonanchor P endpoint rows

Suppose A and B are nonanchor values. If the dirty coordinate has A's
parity, let d_0 be its raw-index distance from A's endpoint coordinate.
For a fixed forbidden row z, (3) leaves only O(1+d_0) possible integer
values of A. Each such A fixes B by (2).

The prescribed pair (A,z) costs at most
`h^o(1)/[h(1+d_0)]` by (4). The independent prescribed B costs C/h.
Summing the O(1+d_0) values of A cancels the distance denominator.
Summing over the b possible z gives

`Pr((2) and this dirty-child witness) <= b h^o(1)/h^2`. (5)

If the dirty coordinate has B's parity, exchange the two roles. The
same proof applies. The geometric bound (3) is used before discarding
the actual branch and cap-selection conditions. The target interval in
this argument is a deterministic interval around the fixed row z, not
an interval chosen after seeing the sampled field.

## 3. At least one anchor endpoint

Each parity anchor has maximum atom h^o(1)/E and is good. Condition on
all anchors when applying the row kernels.

If exactly one endpoint is an anchor and the dirty witness has that
anchor's parity, the bad-coordinate event costs at most Cb/h uniformly
in the anchor. The other parity's prescribed nonanchor row costs C/h.
This gives the stronger bound b h^o(1)/h^2.

If the dirty witness has the nonanchor endpoint's parity, use (4) for
that endpoint together with z. For fixed z and raw-index gap d_0,
(3) allows O(1+d_0) possible values of the nonanchor endpoint. Equation
(2) fixes one anchor value for each. Its atom bound h^o(1)/E and the
two-row kernel cancel the same O(1+d_0) factor. Therefore

`Pr((2) and this dirty-child witness) <= b h^o(1)/(hE)`. (6)

If both endpoints are anchors, (2) fixes one anchor from the other.
It costs h^o(1)/E. Conditional on both anchors and the arm fields,
the dirty coordinate has bad-row probability at most Cb/h through its
offset. Thus (6) also holds in this case. A dirty coordinate itself
cannot be an anchor, since all anchors are good.

## 4. Sum actual positional candidates

There are O(h^2) core ranks. An actual in-strip P has horizontal span
at most h-1, hence O(h) possible rank gaps at fixed stride. At each
endpoint there are O(log h) potential cap-corner forms. Charging the
selected endpoint to its dirty child adds only a fixed factor and b
was already included in (5). Summing (5) gives

`E N_nonanchor <= h b h^o(1)`.                       (7)

For an anchor endpoint within E of the strip boundary, the actual
in-strip condition improves the horizontal span to O(sqrt(Eh)).
Indeed if one black row is a>=h-E and the other is b, the two vertical
alternative rows being in [1,h] imply

`L<=2h-a-b`,

and hence `X^2=L^2-(a-b)^2<=4(h-a)(h-b)<=4Eh`.
The reflected lower-anchor case is identical. Use only these actual
rank gaps when summing (6). Their contribution is

`h^2 sqrt(Eh) * b h^o(1)/(hE)
 =h^(3/2) b h^o(1)/sqrt(E)`.                         (8)

Equations (7)–(8) prove (1). They count all selected-cap endpoints,
not just the intrinsically forced ones. If both endpoints belong to
selected caps, charge either one and allow constant overcounting.

All potential ancestor forms, dirty-child coordinates, and norm heights
are enumerated before sampling. Selection, boundary cleanliness and the
particular movable-barrier position are discarded only after retaining
their necessary dirty-child and good-endpoint conditions.

## 5. Consequences and limits

Outside the selected caps, both original row options are good because
every dirty leaf was covered. Thus every intrinsically forced odd point
of either filling lies in a selected cap, and its P incidence is
included in (1). In particular this improvement is already available
with the compatible original filling; it does not require activating
the optional two-corner menu or extending any old P2 proof.

For b=h^(5/6+o(1)), the anchor choice E=h^(11/12) gives

`h b=h^(11/6+o(1))`,

`h^(3/2)b/sqrt(E)=h^(15/8+o(1))`.                    (9)

The long-six anchor-hub term h^2 b/E and the top-window crop hE then
both have exponent 23/12. The previous prime-pool and anchor-partner
separation hypotheses have strict margins at this exponent. These are
conditional quantitative consequences of (1), not a safe repair rule.

The argument concerns coarse corner forms and fixed finite bounded-error
extensions with an explicit deterministic dirty witness. It does not
cover arbitrary interpolation that loses this provenance. It also does
not make the cap incidence graph satisfiable: two forced singleton
choices can still conflict. Replacing or moving a barrier requires
control of the full new support union.

Independent review: two independent written reviews passed the fixed-
target summation, dirty-child witness, both anchor-parity cases, actual
horizontal-span restriction, and exponent calculations. The bounded-size
fallback and zero-index-gap bounded-error cases are included explicitly.
