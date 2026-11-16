# Consequences of the residue-restricted cap law

15 November 2026. Apply
[the offset-residue restriction](continuation_cap_boundary_residue_offsets.md)
to the independently sampled two-arm or multiscale V-map scaffold. It
preserves all existing upper probability estimates by a bounded density
comparison and makes the maximum selected cap side
`L_*=h^(5/6+o(1))`. The consequences below concern incidence counts, not
an occupancy-preserving repair theorem.

## 1. Optimized polylogarithmic long-six regime

Let the long-support parameter K be polylogarithmic. Write the anchor
window as E=h^e and the maximum cap side as h^l, where l=5/6+o(1).
The reviewed count bounds give these exponents:

| Quantity | Exponent |
| --- | --- |
| Same-parity nonanchor long-six incidence | 1+l |
| Same-parity anchor-hub long-six incidence | 2+l-e |
| Opposite-parity long-six incidence | 3-2e |
| Intrinsically forced odd-stub P incidence | 3/2+e/2 |
| Labels incident to the top anchor window | 1+e |
| Initial cap and bad-row relocation | 1+5/6+o(1) |

Choose e=8/9. Then the dominant two quantities agree:

`2+5/6-8/9 = 3/2+(8/9)/2 = 35/18`.                 (1)

The remaining displayed exponents are 11/6, 11/9, 17/9, and
11/6+o(1), respectively. Thus the combined listed incidence and
initial relocation budget is `h^(35/18+o(1))`.

The anchor pool input remains applicable: 8/9 is larger than its stated
fixed-modulus short-interval exponent 32/37. The forbidden-row count
`h^(5/6+o(1))` is smaller than the pool size `h^(8/9+o(1))`. Long
triangle partners cannot be anchors because h/K is larger than E.

The previous genuine-source factor and own-gap cleanup still has its
separate external relocation budget. It is not included in (1) unless
its existing choices are also imposed. No repair cost is inferred by
equating a support count with a number of safely erasable points.

## 2. A larger polynomial long-support window

For any fixed

`0<kappa<1/21`,                                      (2)

set K=h^kappa and put

`g=1/6-(7/2)kappa>0`, `e=1-kappa-g/2`.               (3)

Keep the exact cap bound h^(5/6+o(1)), and choose E=h^e. The reviewed
quantitative count formulas become

`nonanchor <= h^[1+5/6+(7/2)kappa+o(1)]
             = h^[2-g+o(1)]`,

`same-parity anchor <= h^[2+5/6-e+(5/2)kappa+o(1)]
                      = h^[2-g/2+o(1)]`,

`opposite parity <= h^[3+4kappa-2e+o(1)]
                  = h^[1+6kappa+g+o(1)]`.           (4)

All three exponents are strictly below two. In particular,
`1+6kappa+g=7/6+(5/2)kappa<9/7` in (2).
The top-window and forced-odd P terms have exponents

`2-kappa-g/2` and `2-kappa/2-g/4`,                    (5)

also strictly below two. The anchor exponent e lies between 11/12 and
20/21, so the same prime-pool input applies. Moreover

`1-kappa-e=g/2>0`,                                  (6)

which gives the strict separation between the long increment h/K and
the anchor window. The old large-cap failure event disappears entirely.

Consequently the existing long-six incidence reduction extends to
horizontal spans above `h^(2-kappa)` for every fixed kappa in (2).
The conclusion does not cover all smaller spans or solve the singleton
parity constraints.

## 3. Inputs and limits

The arithmetic powers in (4) are exactly those recorded in
[the polynomial-window count](continuation_polynomial_long_six_window.md):
K^(7/2) for nonanchor same-parity supports, K^(5/2) for anchor hubs,
and K^4 for opposite parity. All constants are fixed before h grows.
The multiscale sampling version changes only logarithmic factors.

The residue restriction is applied separately to each parity and before
cap selection. Counts are still made on deterministic potential cap
forms, with selection discarded before sampling. Bounded density, not
new independence between offsets and their own fields, transfers them.

The remaining construction tasks include compatible singleton choices,
shorter parked-six supports, and a repair that preserves occupancy
without creating new supports. The new exponent is a quantitative
improvement to the reviewed scaffold reduction, not a threshold theorem.

Independent review: the full written consequence passed a separate
review of the exponents, prime-pool margins, polynomial K factors,
anchor-partner exclusion, and construction scope.
