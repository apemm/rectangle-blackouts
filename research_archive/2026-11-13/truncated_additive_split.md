# A truncated additive split against the ratio graphs

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: colour each light (T, type) greedily against G_T and all ratio-graph edges of height at most (log h)^2, and split at random only against the larger heights. The Bad_split term Lambda^3/B becomes Lambda^(4/3+eps), and the exponent of Theorem N drops from 1.5 to 1.49674. A split with O(1) parts and no bad edges up to height h^(1/2) would bound chi(R_IV) on polynomial ranges, which is open. Not audited yet.

# Result

## Status

proved

## Summary

A truncated additive split removes the Bad_split term. Each light (T, tau) is coloured greedily against G_T plus every R_IV, R_FF and R_FF^+ edge of height at most H0 = (log h)^2, which adds O((log h)^(4/3)) classes and needs no removal. The random split then handles only the heights in (H0, h^(1/2)], with weight O(H0^(-1/3+eps)). The term Lambda^3/B becomes Lambda^(4/3+eps), and Theorem N's exponent drops from 1.5 to theta* = min_a (3+3^a)/(2(1+a)) = 1.49674 (a = 0.912; 1.49675 at a = 0.91). Conditional on the same hypotheses as Theorem N.

## Statements

THEOREM N' (CONDITIONAL; same hypotheses as Theorem N as corrected by audit_consolidated_board.md: (AP) with modulus up to 32 h^(1/2), the J3-Bad sets of Q1 to Q4 of size O(h^(2-delta)), and the audits U1 to U8 together with the completeness of K2, K4 and the obstruction table).
Notation: Lambda = log h, ell = loglog h. B = ceil(Lambda^x) is the heavy threshold. H0 = ceil(Lambda^y). N_IV(H) = #{lambda : q_lambda <= H}. N_FF(H) = #{coprime (a,b), b > 0, U != 0 : |U'(a,b)| <= H}. N0 = N_IV(H0) + 8 N_FF(H0) + 7, and B' = B + N0.
Modify L*** in two places.
(B4') On each light (T, tau), colour I(T, tau) greedily in increasing i against the union of:
 - G_T;
 - R_IV^(<=H0), the R_IV edges (q m, p m) with q_lambda <= H0;
 - the eight depth graphs R_FF^-(<=H0), the pairs with depth ratio |V'|/|U'| over shapes with |U'| <= H0 (4 filler rows, odd and even depths);
 - R_FF^+, all pairs with 0 < |i - i'| <= 210.
 Let c_T be the number of colours used. Split each colour class into K_T = floor(B'/c_T) subclasses by iid uniform colours psi_T, independent across T.
(B8') The Theorem D blocks (weighted form) receive Bad_res. This is, in each final subclass, the shallow end of every monochromatic RESIDUAL edge: R_IV edges with q_lambda > H0 and max(p, q) <= h^(1/2), and R_FF edges with H0 < |U'| <= h^(1/2). R_FF^+ and the edges of height <= H0 are never monochromatic. Everything else is as in L*** (B1) to (B10), with B' in place of B as the number of classes per (T, tau).
Then, for every m >= M, L*** with (B4') and (B8'), truncated to columns 1..m, is a valid blackout with m + q_h points, and
 M <= C h^2 (B' + Lambda^(E(a)+1) B^(-a) + C_eps Lambda^2 H0^(-1/3+eps) (1 + Lambda/B)) ell^C1 + c0 n_rel tau*(h)^2 + C h^2 ell^2,
with N0 <= C H0^(2/3). With x = theta(a) = (E(a)+1)/(1+a) and any y in (3(2 - theta), 3 theta/2] = (1.5098, 2.2451] (for example y = 2), this gives
 m_h <= C h^2 (log h)^(theta*) (loglog h)^C1, with theta* = min_a (3 + 3^a)/(2(1 + a)) = 1.496743 at a = 0.9124 (1.496745 at the note's a = 0.91).
The Bad_split term Lambda^3/B is replaced by Lambda^(4/3+eps) (at y = 2), which is of lower order. The exponent is exactly the heavy-light trade-off value, and the bound sum over light T of c_T = O(h) is not needed.
PROPOSITION O (proved implication; why the literal target is chi-hard). Suppose a split of the non-exceptional labels of one light (T, tau) has no monochromatic R_IV^(5) edge of height <= h^(1/2) outside a set E_{T,tau}. Suppose also that the u-values of the type fill every u = u0 (mod 32) in [U1, U1 + X], with U1 <= X/(2Y). If |E_{T,tau}| Y < X/(64Y) - 1, the split has at least chi(R_IV^(5) restricted to [1, Y]) parts. In particular, with |E_{T,tau}| <= h^(1-delta) and X of order h, it has at least chi(R_IV^(5) restricted to [1, c h^(delta/2)]) parts. So a split with O(1) parts per class and a bad set of O(h^(2-delta)) labels in total would bound chi(R_IV^(5)) on polynomial ranges. That is open: chi(R_IV) < infinity is open.

## Proofs

0. INPUTS (status as recorded in the folder)
- additive_class_split.md, Lemma 1 (R_FF shapes: Y1 = mu|U'| and Y2 = mu|V'|, d < 0 iff t < 0), Lemma 2 (gcd(U,V) | 40) and Theorem 5's back-degree argument. Audited, correct with fixable gaps. Adopt the audit's fix: every light label whose even row is >= the lowest filler row of its type goes to the exceptional set (O(h) labels).
- ratio_graph_r_iv.md and Lemma IV of polylog_relocation_diluted.md: q = al F/g >= al be^2/5, p >= be^3/5, F < 17 be^2, p < 21 be^3 (audited).
- Theorem D, weighted form, of polylog_relocation_diluted.md (audited modulo (AP), with the audit's corrections). Its cost is C(rho kappa ell^C |D| h Lambda^2 ell^C1 + h^2 ell).
- (AP) (ap_hypothesis_henriot.md, audited with fixable gaps).
- Heavy_light Theorem S: the sum over light T of (kappa_T + 1) is <= C h Lambda (audited).
- saw_residual_families (iii-b): d > 0 forces 2d <= h - y_F. In L*** fillers are >= h - 210 (consolidated K4), so the slot difference |t| = 2d <= 210.
- Proposition R and J4 hold for any family of G_T-independent classes with at most B' classes per diagonal; width is linear in B'.

1. LEMMA A (shape counts; proved).
(a) N_IV(H) <= 2(5H)^(2/3).
- q_lambda <= H forces al be^2 <= 5H with al < be.
- The count is at most the sum over be of min(be, 5H/be^2).
- The terms with be <= (5H)^(1/3) contribute <= (5H)^(2/3)/2. The terms above contribute <= 5H/(5H)^(1/3) = (5H)^(2/3).
(b) N_FF(H) <= C H^(2/3).
- |U'| >= |U|/40 (Lemma 2), so |U| <= 40H.
- Put k = a - 4b != 0. Then |U| = |k|(17(b + 4k/17)^2 + k^2/17).
- |U| <= X forces |k| <= (17X)^(1/3) and, for each k, at most 2(X/(17|k|))^(1/2) + 1 values of b.
- Summing over k gives O(X^(1/2) X^(1/6) + X^(1/3)) = O(X^(2/3)).
(Check: shape_counts.py in the script folder gives N_FF(H)/H^(2/3) between 1.58 and 1.83 for H from 100 to 30000. Also N_IV^(5)(H) = 0, 0, 0, 1, 5, 13 at H = 100, 300, 1000, 3000, 10^4, 3*10^4.)
So N0 <= C H0^(2/3).

2. LEMMA B (tails; proved). For every eps in (0, 1/6):
 kappa_IV(>H) := sum over lambda with q_lambda > H of (tau(q)^C/q + tau(p)^C/p) <<_eps H^(-1/3+eps), and
 kappa_FF(>H) := sum over shapes with |U'| > H of tau(|U'|)^C/|U'| <<_eps H^(-1/3+eps).
Proof for R_IV:
- Use tau(n)^C <<_eps n^eps.
- q <= al F < 17 al be^2 < 17 be^3, so q > H forces be > (H/17)^(1/3).
- The q-weights sum to at most C times the sum over be > (H/17)^(1/3) of be^(-2+2eps) times the sum over al < be of al^(-1+eps), which is << H^(-1/3+eps).
- The p-weights: p >= be^3/5 and there are <= be admissible al per be. The sum over be > (H/17)^(1/3) of be (be^3)^(-1+eps) is << H^(-1/3+eps).
Proof for R_FF:
- |U'| > H implies |U| > H, and |U'|^(-1+eps) <= 40|U|^(-1+eps). Write |U| = |k| Q with Q = 17 z^2 + k^2/17 and z = b + 4k/17.
- |k| >= H^(1/3): for fixed k, the sum over b of Q^(-1+eps) is at most 2 max + integral = O(|k|^(-1+2eps)). Multiplied by |k|^(-1+eps), this is |k|^(-2+3eps). Summing over |k| >= H^(1/3) gives H^(-1/3+eps).
- |k| < H^(1/3): we need Q > H/|k| >= H^(2/3) > 17 k^2/17. So 17 z^2 > (16/17) H/|k|. The sum of (17 z^2)^(-1+eps) over such b is << (H/|k|)^(-1/2+eps). Multiplied by |k|^(-1+eps), this is << H^(-1/2+eps) |k|^(-1/2). Summing over |k| < H^(1/3) gives H^(-1/2+eps) H^(1/6) = H^(-1/3+eps).
This is consistent with the audited tails (Y^(-1/3) for both families, audit_additive_class_split issue 1 and Lemma FF').

3. LEMMA C (truncated additive split; proved). On each light (T, tau), (B4') uses c_T <= kappa_T + N0 colours. Each colour class is G_T-independent and has no edge of R_IV^(<=H0), of the eight R_FF^-(<=H0) or of R_FF^+.
Proof. A greedy colouring in a fixed order uses at most 1 + (maximum back-degree) colours, and back-degrees of a union in one order add. Order by increasing i inside the type.
- G_T: the earlier neighbours of i are i - d with d in D_T, at most kappa_T of them.
- R_IV^(<=H0): u(i) = (2i+1-r0)/2 is increasing on a type (r0 is fixed by i mod 32). An edge (q m, p m) has q < p, so its later end is p m. The earlier neighbour for lambda is u q/p, which needs p_lambda | u. There is at most one per lambda in S0 = {q_lambda <= H0}, so at most N_IV(H0).
- R_FF^-(<=H0), each of the 8 depth maps: delta_o(i) = Y_o - (2i+1) and delta'_o(i) = Y_o - (2i+1+T). Y_o is constant on a type, so the map is injective and decreasing in i. The later end of a pair is the shallower label, at depth mu|U'| (Lemma 1). The deeper partner has depth delta|V'|/|U'|, so there is at most one per shape with |U'| <= H0, at most N_FF(H0) per map.
- R_FF^+: labels of a type are 32 slots apart, so at most floor(210/32) = 6 earlier labels lie within slot distance 210.
- The total back-degree is <= kappa_T + N_IV(H0) + 8 N_FF(H0) + 6, which gives c_T <= kappa_T + N0.
Each fatal in-class pair of family IV is an R_IV edge (sea_census_rigid B4, 'only if', audited). Each homogeneous Fo/Fo or Fe/Fe pair with both depths positive is an R_FF^- edge of the map of its common filler row (d < 0), or an R_FF^+ pair (d > 0, |t| <= 210). So a class has no such pair with height <= H0, and no d > 0 pair at all. No label is removed here, unlike Theorem 5, because the back-degree is bounded by the number of shapes of height <= H0, not by divisor counts of u.
Light means kappa_T <= B - 1, so c_T <= B' - 1 and K_T = floor(B'/c_T) >= 1. Then c_T K_T <= B' and 1/K_T <= 2 c_T/B'. So there are at most B' final subclasses per (T, tau).

4. LEMMA D (residual random split; proved, given the inputs). Let f be a label in colour class c of (T, tau).
- f is in Bad_res only if some residual edge at f has both ends in c and equal psi_T colours.
- Each lambda gives at most two edges at f (f = q m or f = p m), each needing q_lambda | u_f or p_lambda | u_f. Each shape and map gives at most one edge with f as its shallow end, needing |U'| | delta(f).
- Each such edge is monochromatic with probability 1/K_T <= 2 c_T/B'.
So P(f in Bad_res) <= rho_T times the sum over q in Q_T^res of 1[q | (u_f or delta(f))], with rho_T = 2c_T/B' and Q_T^res the residual moduli (all in (H0, h^(1/2)]). Each condition is an AP in i on one diagonal, with modulus <= 32 h^(1/2) (the audit's form of (AP)). Bad_res ∩ T depends only on psi_T and on the deterministic colouring, so it is independent across T. This is the hypothesis of the weighted Theorem D with kappa^res = kappa_IV(>H0) + 8 kappa_FF(>H0) <<_eps H0^(-1/3+eps) (Lemma B).
- The colouring does not depend on (l, p) or on positions. Later removals (Proposition partial sets chosen after (l, p), Bad_res) only delete vertices, so the classes stay G_T-independent and edge-free. The order of choices of K6 (classes, then psi, then (l, p)) is unchanged.
- Closure (J3): every residual violation in a final subclass has its shallow end in Bad_res. R_IV relocates the q-end or both ends; R_FF the depth-|U'| end, which by Lemma 1 fixes the edge, as in Lemma FF'. The edges of height <= H0 and R_FF^+ have no violation. Edges of height > h^(1/2) go to Proposition partial, unchanged. Supersets are allowed in J3, and removed labels become SAW* holes, which the filler families already count as fillers (K8).

5. WIDTH.
- Light regions: as in section 3 of consolidated_board.md, with B' classes per (T, tau): 512 x (4p 16l B' + 4A) <= 5.5e6 B' h^2. Proposition R, J4, Lemma L-adic and the first-moment families need only G_T-independent classes, at most B' per diagonal. The A4 count B h^(1+o(1)) becomes B' h^(1+o(1)), still o(h^2/tau*^2).
- Heavy (Theorem E), unchanged: C h^2 Lambda^(E(a)+1) B^(-a) ell^C.
- Theorem D, with groups D_j = {T light : c_T in [2^(j-1), 2^j)}, rho_j = 2^(j+1)/B' and O(log B') groups. They succeed simultaneously because the groups use disjoint psi variables (audit fix).
  - The sum over j of rho_j |D_j| is <= (4/B') sum over light T of c_T <= (4/B')(C h Lambda + h N0) <= 4C h Lambda/B + 4h.
  - So the cost is <= C kappa^res ell^C h^2 Lambda^2 (Lambda/B + 1) ell^C1 + C h^2 ell log B' <= C_eps h^2 Lambda^2 H0^(-1/3+eps)(1 + Lambda/B) ell^C1 + C h^2 ell^2.
- Proposition partial: n_rel unchanged, O(h^(11/6+o(1)) + h^(2-delta)) + O(h).
This gives the bound in the statement.

6. EXPONENT.
- With B = Lambda^x and H0 = Lambda^y, the terms have exponents x + o(1) (B' <= B + C Lambda^(2y/3)), E(a) + 1 - a x, 2y/3, 2 - y/3 + eps and 3 - x - y/3 + eps.
- If 2y/3 <= x and y > 3(2 - x), the last three are below x. The minimum is then the heavy-light value theta(a) = (E(a)+1)/(1+a) at x = theta(a), and min over a of (3 + 3^a)/(2(1+a)) = 1.496743 (a = 0.9124). At a = 0.91, theta = 2.85876/1.91 = 1.496745.
- Admissible y: (3(2 - theta*), 1.5 theta*] = (1.5098, 2.2451].
- At y = 2: N0 = O(Lambda^(4/3)), and the Bad_res cost is h^2 Lambda^(4/3+2eps) ell^C. At x = theta*, Lambda/B < 1, so the (Lambda/B) part is h^2 Lambda^(0.836+eps).
- Old exponent: max(x, 2.8588 - 0.91x, 3 - x) = 1.5 at x = 1.5. New exponent: 1.49675 (a = 0.91). The loss of 0.0033 is gone, without sum over light T of c_T = O(h). (expo.py in the script folder checks the arithmetic.)

7. PROPOSITION O (proved implication).
- R_IV^(5) edges preserve u mod 32, and m -> m m' with m' odd preserves edges (Lemma 2 of ratio_graph_r_iv, audited).
- Let F be a connected subgraph of R_IV^(5) with vertices in [1, Y], all = v0 (mod 32). Then for odd m = m1 (mod 32) with m1 v0 = u0 and m in [U1, (U1 + X)/Y], the copy m F lies in the type's u-values. The edges of m F have height <= Y <= h^(1/2). If U1 <= X/(2Y), there are at least X/(64Y) - 1 copies.
- A point of E lies in at most |V_F| <= Y copies (u = m w determines m). So if |E| Y < X/(64Y) - 1, some copy avoids E, and the split restricted to it is a proper colouring of F. Hence the number of parts is >= chi(F).
- Take F a component of R_IV^(5) restricted to [1, Y] of largest chromatic number. With |E| <= h^(1-delta) and X of order h, Y = c h^(delta/2) works.
- This is the audit's quantitative extension of Corollary 3, adapted to a residue class mod 32 and an interval of u. It shows that the literal target (O(1) parts with no monochromatic small-height edge, or with an h^(2-delta) bad set) would bound chi(R_IV^(5)) restricted to [1, h^(delta/2)] by the number of parts on that (T, tau). The hybrid avoids this: it pays the colouring cost only up to height H0 = polylog, where the back-degree is trivially bounded, and it dilutes the rest.

8. THE OTHER CANDIDATES, BRIEFLY.
- Degeneracy of the small-height part on [1, h]: it is unbounded. The hypercube {N prod over lambda in S of rho_lambda} of additive Proposition 7 embeds in [1, h] with dimension of order log h/log H. So degeneracy cannot give O(1) colours up to height h^(1/2). Up to height H it is <= N_IV(H) + 8 N_FF(H) + 6 (Lemma C), which is what is used here.
- Stride (8,1): it kills in-class family IV (ratio_graph_r_iv Corollary 5(ii), with the audit's hypothesis v2(y - r) = 1). But it does not touch the SAW* filler family R_FF, which would need its cubic re-derived at slope 4. It also reopens chi(Gamma) over Q(sqrt17), rigid Theorem C, mixed_quadruples 1-4 and the deep layer. It is not needed for this target.
- Additive split with fewer removals: (B4') is the additive split truncated at height H0. It removes nothing, and its class count is additive (kappa_T + O(H0^(2/3))), not multiplicative.

## External results used

- None beyond standard facts: tau(n) <<_eps n^eps; a sum of a unimodal function at unit-spaced points is at most 2 max + integral. All other inputs are notes of research_archive/2026-11-13 (weighted Theorem D, Lemma IV, additive Lemmas 1 and 2, Theorem S, Proposition R, (AP)), cited with their audit status.

## Checks

Analytic work first; computation only as a sanity check. Two scripts in scripts_ratio_split/, each run once with py -I, under 60 s:
- shape_counts.py: enumerates the R_IV lambdas (k = 4 and k = 5) and the R_FF shapes, asserting g in {1,5} and gcd(U,V) | 40.
  - N_FF(H)/H^(2/3) is 1.58, 1.63, 1.83, 1.76, 1.78 and 1.80 at H = 100 to 30000, confirming the H^(2/3) count.
  - N_IV^(5)(H) is 0, 0, 0, 1, 5, 13 and N_IV^(4)(H) is 0, 0, 1, 5, 12, 31.
  - The truncated FF tail times H^(1/3) is about 2.8 at small H, consistent with H^(-1/3) decay (truncated at 30000, so it is a lower bound).
- expo.py: theta* = min_a (3+3^a)/(2(1+a)) = 1.496743 at a = 0.91242; the admissible y-range for H0 = Lambda^y is (1.5098, 2.2451]; the old max at x = 1.5 is 1.5, and the new max at a = 0.91 is 1.49679 at x = 1.4967.
By hand: the greedy back-degree count; both tail sums with the eps loss; the group-cost sum with B' and Theorem S; the dilation copies count in Proposition O.
Read: consolidated_board.md, polylog_relocation_diluted.md and its audit, additive_class_split.md and its audit, ratio_graph_r_iv.md and its audit, audit_consolidated_board.md, the R_FF parts of saw_residual_families.md, heavy_light_split.md (Proposition R, Theorem S, Theorem 3), and the Theorem D / R_FF lines of obstruction_table_completeness.md and two_filler_row_lemma.md. The repository was only read. No git commands.

## Gaps

- Theorem N' is a conditional implication. It inherits every hypothesis of Theorem N as corrected by audit_consolidated_board.md: (AP) with modulus up to 32 h^(1/2) (proved in ap_hypothesis_henriot.md, audit with fixable gaps), the J3-Bad sets of Q1 to Q4 at O(h^(2-delta)) (closed by the round-10 notes, not yet audited), U1 to U8, and the completeness of the K2 and K4 lists and of the obstruction table. Nothing here proves m_h = O(h^2).
- Lemmas A to D, Theorem N' and Proposition O are new and have had no second reader. They are short and elementary (greedy back-degree, the two H^(-1/3+eps) tail sums, the weighted Theorem D bookkeeping with B' in place of B).
- The literal target is NOT met: there is no split with O(1) parts and no monochromatic edge (or an h^(2-delta) bad set) for heights up to h^(1/2). Proposition O shows this would bound chi(R_IV^(5)) on [1, h^(delta/2)], which is open. The residual heights (H0, h^(1/2)] still go to Theorem D blocks, so the result still needs (AP) and the weighted Theorem D. Only their cost drops, to h^2 Lambda^(4/3+eps).
- Constants: N0 <= C H0^(2/3) with C about 15 (N_FF(H) is about 1.8 H^(2/3), times 8 maps). At H0 = Lambda^2, N0 exceeds B for every practical h. B' = O(B) holds for all h, but with a large constant, so the gain is asymptotic only. In practice the greedy uses far fewer colours: the measured superset back-degree with ALL shapes is at most 15 to 20 at h of 2e5 to 1e6 (additive_class_split, combined.py). The constant C_eps in Lemma B is not explicit.
- I assumed, as consolidated_board.md does, that every place that uses 'at most B classes per (T, tau)' (Proposition R, J4, J6 width, the first-moment families A4, B7 and D8, and Lemma L-adic) is linear in or monotone in the class count, so that B' = O(B) changes only constants. I re-checked Proposition R's statement and the width formula, but not every first-moment count's dependence on the number of classes.
- Lemma C uses audit issue 3's fix of additive_class_split (labels whose even row is at least the lowest filler row go to the exceptional set, O(h)). It also uses the SAW* bound |t| <= 210 for d > 0 from 2d <= h - y_F with fillers >= h - 210 (consolidated K4), which I did not re-derive from Lemma mixedeq.

## Missing estimate

None for removing the Bad_split term: with (B4') and (B8') the term is h^2 Lambda^(4/3+eps), and the near-goal exponent is the heavy-light value 1.49674. Below 1.4967 on this board, the binding trade-off is B against Lambda^(E(a)+1) B^(-a), the heavy-light split (Theorem E on heavy diagonals). Any further gain must come from there (for example a larger stride menu, as in heavy_light Theorem 3), not from the class split. The literal no-bad-set version needs a bound on chi(R_IV^(5)) restricted to [1, h^(delta/2)] (Proposition O), which is open.

## Next steps

- Audit Lemmas A to D and Theorem N' (about one page): the greedy back-degree bound kappa_T + N0, the two H^(-1/3+eps) tails, and the group sum (4/B')(C h Lambda + h N0).
- Edit consolidated_board.md: replace (B4) and (B8) with (B4') and (B8'), set H0 = ceil(Lambda^2), and change Theorem N's width to C h^2 (B' + Lambda^(E+1) B^(-a) + Lambda^(4/3+eps)) ell^C1 + ... with exponent 1.4967. Drop the line that makes 1.4967 conditional on the sum of c_T being O(h). Move R_FF^+ from (B8) to the deterministic colouring.
- Check that every first-moment family (A4, B7, D8, D11) and every width count uses the class count only linearly, so that B' = B + O(Lambda^(4/3)) changes only constants.
- For practical h, use the real greedy colour count (measured at most about 20 extra colours with all shapes), not the worst-case N0, in any explicit-constant version.
- The next exponent gain on this board has to come from the heavy-light trade-off (stride menus), since the class split no longer costs anything in the exponent.

