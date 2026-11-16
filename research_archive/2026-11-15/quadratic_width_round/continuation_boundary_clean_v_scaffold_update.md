# Current parameters for the boundary-clean V scaffold

15 November 2026. Boundary-clean cap selection and restricted offset
residues improve the compatible V scaffold without changing its original
one-coordinate cap filling. Use

`b=h^(5/6+o(1))`, `L_*=O(b)`, `E=h^(11/12)`.          (1)

The listed structural, initial cap-P, and polylogarithmic long-six costs
are at most `h^(23/12+o(1))`. This is a reduction with counted residual
incidences. It is not an occupancy-preserving repair theorem.

## 1. Compatible changes to the existing scaffold

Start with the independently reviewed
[multiscale V integration](continuation_multiscale_v_integration.md).
Include the fixed interpolation and permutation enlargement in the
forbidden-row count b before choosing parameters.

Apply the following changes in this order.

1. Choose the independent good parity anchors in the near-top window E.
   Keep the existing prime-gap condition and reflected high-sea version.
2. Conditional on each parity's arm fields and anchor, restrict its
   offset to avoid the bad residues modulo L_0, where L_0 is the least
   dyadic integer at least 16 max(1,b).
3. Declare a node dirty if any of its four boundary-coordinate values
   is bad, including dirty leaves. Select maximal first boundary-clean
   ancestors of all dirty nodes.
4. Use the compatible original filling: only the common-coordinate role
   is capped on each selected interval. Keep the other total function
   unchanged. Apply the original even preference at nongenuine ranks.

The [residue lemma](continuation_cap_boundary_residue_offsets.md)
makes every selected cap have side at most L_0. Its new law has density
at most four relative to the old joint law. The
[boundary-clean selection lemma](continuation_boundary_clean_movable_caps.md)
keeps expected total cap area O(hb log h), and all raw options outside
selected caps are good.

This version retains the original at-most-one-projected-coordinate
coarse pair and its existing bounded-error interpolation provenance.
The optional movable two-corner menu is not needed for this update.
Its separate bidirectional-P extension is available but is not silently
substituted here.

## 2. The audited costs

For polylogarithmic K, the incidence bounds become:

| Quantity | Bound |
| --- | --- |
| Top-window labels placed in the external relocation set | h^(23/12+o(1)) |
| Boundary-clean caps and bad-row labels | h^(11/6+o(1)) |
| Actual nonanchor P touching a selected cap | h^(11/6+o(1)) |
| Actual anchor P touching a selected cap | h^(15/8+o(1)) |
| Same-parity nonanchor long-six supports | h^(11/6+o(1)) |
| Same-parity anchor-hub long-six supports | h^(23/12+o(1)) |
| Opposite-parity long-six supports | h^(7/6+o(1)) |

The P rows use the
[dirty-child incidence lemma](continuation_dirty_child_cap_p_incidence.md):

`h^o(1)[h b+h^(3/2)b/sqrt(E)]`.                      (2)

The same-parity anchor row uses h^2 L_*/E. The nonanchor row uses
h L_*, and the opposite-parity row uses h^3/E^2. Substitution of (1)
gives the displayed exponents. The short-interval prime input and the
bad-row subtraction both have strict margins. The long increment h/K
exceeds E, so anchors remain impossible as long triangle partners.

No separate large-cap failure event is needed. Bounded-density transfer
also preserves the earlier genuine central two-cycle and fixed short-
cycle estimates within their stated scopes.

## 3. Initial intrinsic stubs versus later forced choices

An initial intrinsically forced odd point is a nongenuine rank whose
even option is bad. Every such rank is in a selected cap, because all
dirty leaves were covered. Its actual P incidence is therefore counted
in (2). For the fixed fine refinement, use the already established
bounded-error form and its deterministic nearby dirty-cap witness;
arbitrary interpolation without that witness is outside this claim.

Later deliberate erasures are different. Removing an even point from a
genuine double leaves an odd singleton outside the cap set. Such a point
is not charged to (2). It requires its own previously proved long-gap
qualification or a new choice/repair argument. Similarly, changing
singleton parities can make an optional point mandatory in the final
assignment without giving it an initial dirty-cap witness.

The genuine-source small-factor and own-gap cleanup remains a separate
o(h^2) external-relocation objective. Its near-quadratic chosen budget
need not be bounded by h^(23/12+o(1)), so the latter exponent must not
be presented as a bound for all subsequent cleanup costs.

## 4. Remaining obligations

The compatible core stays occupied, and the old same-parity geometry,
row-filter inputs, and guarded collar hypotheses retain their fixed
constants. The exact final excess count still requires the stated
external relocation and full label partition conditions, including
the original O(h) profile-boundary labels.

None of these counts selects a consistent collection of singleton
parities or proves that an additional cap repair will not regenerate
P or parked-six supports. Shorter six supports, general forced paths,
and the full residual choice system remain open.

The polynomial long-six incidence window from the
[residue-cap consequence](continuation_residue_cap_incidence_improvement.md)
extends separately to every fixed kappa<1/21, with its corresponding
anchor exponent. Formula (1) is the optimized polylogarithmic-K choice.

Review status: the consolidated dependency and parameter statement passed
an independent written review. The review also checked the fine-edge
witness: changed interpolation edges have both options good, while an
unchanged edge can inherit a bad option only from a neighboring coarse
rank, now covered by a dirty cap. The separate near-quadratic cleanup
budget and later deliberate stubs remain explicit.
