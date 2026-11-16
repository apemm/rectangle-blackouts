# A period-seven sea for the Hilbert placement (design H7)

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: with a mod-4 row alignment (196 residue blocks, row step d = 28, S = 6272 sigma), the Hilbert period-seven board leaves only three label-sea residual families, R2s, FW and 6PT. Every other multi-label sea support is excluded for every choice, T2's allowed triangles disappear, and a new class of harmless parked triangles takes their place. If the P family, the label-only supports and the three residual families are avoided, m_h <= 6272 sigma M (h + 28)^2 + C h^2. The aligned profiles rest on a Lemma AP4 that is not audited. Audited in audit_hilbert_sea_design_h7.md (correct with fixable gaps).

# Result

## Status

partial

## Summary

With a mod-4 row alignment (196 blocks, d = 28, S = 6272σ), the Hilbert period-seven board leaves only three label-sea residual families: R2s, FW and 6PT. Every other multi-label sea support is excluded for every choice. T2's allowed triangles disappear, and a new class of harmless parked triangles (PT) takes their place. If P, the label-only supports and the three residual families are avoided, m_h ≤ 6272σM(h+28)^2 + C h^2.

## Statements

SETTING (design H7). Split the non-exceptional labels by (a mod 28, b mod 28), with a the odd row and b the even row. That gives 14 x 14 = 196 aligned blocks. Each block is a mixed-residue or a zero-residue block in the sense of T2 Section 1.

For each block take a T1 profile pi = (L, F, H, g) with the extra mod-4 conditions L ≡ F ≡ a+2 and H ≡ b+2 (mod 4) (Lemma AP4 below). Inside a block the rows are a = a0 + 28i and b = b0 + 28j. Pad (i, j) to a power-of-two square of side Q ≤ 2(h/28+1), and let r be the Hilbert rank (original ranks kept). Fix a power of two σ ≥ 1, put S = 8·28^2·σ = 6272σ, and place label e at x_e = x_0 + S(M r_e + ξ_e) with 0 ≤ ξ_e < M. Every other core column holds s_pi(x): F if 7|x, L if chi_7(x) = -1, H if chi_7(x) = 1. Unused slots keep F. The collars are N1's BL4 (P, Phi, staircase C_H..C_{h-1}, then row h). Windows are separated by D = 2W_h+1 columns of row h. The exceptional labels are placed by the positional lemma (T1 Section 5, compatible_profile Section 1).

THEOREM H7 (reduction; proved here modulo the inputs listed under gaps). Let h ≥ h0. Every violation of (V1)-(V5) of block_sea_classification.md lies in one block window, involves at least 2 labels of that core, and belongs to exactly one of these families:
 (P) a label-label vertical rival (opposite-parity points of two labels);
 (Λ3) a label-only tilted three-black rectangle, not all of one parity;
 (Λ4) a label-only mixed four-support with nonvertical side, not all of one parity;
 (R2s) a two-sea mixed support whose side is (label point A of e, sea point B) and whose diagonal is (same-parity label point C of f, sea point D), with B and D in the same sea row;
 (FW) a parked triangle PT (defined below) with s = F whose white corner W falls in an occupied slot column;
 (6PT) two PTs with a common white corner and six distinct black corners.
Here a PT is a right angle at a label point A of e, with other end a same-parity point C of a different label f and third corner a sea point. Every PT whose W is not in a label column is white and parked. It is harmless and must be allowed: it is not a constraint.

COROLLARY (conditional width). If in every block some choice ξ avoids (P), (Λ3), (Λ4), (R2s), (FW) and (6PT), then the board is a valid blackout and
 m_h ≤ 6272·σ·M·(h+28)^2 + C1·h^2,
with C1 ~ 1.6·10^5 (collars) plus the exceptional-label constant. So bounded σM gives m_h = O(h^2), and σM ≤ (log h)^b gives exponent b. The other residual families are not needed for this bookkeeping.

UNCONDITIONAL PIECES (proved; σ a power of 2): (Λ3) is empty for h ≤ 3.6·10^8 σ^4 and (Λ4) for h ≤ 2.2·10^7 σ^4. In mixed blocks the bounds are 1.2·10^11 σ^4 and 7.7·10^9 σ^4. (FW) is empty for h ≤ 6.1·10^10 σ^4, (P) for h ≤ 4096σ^2, and 6PT with distinct sea offsets for h ≤ 1.75·10^5 σ^2. None of these is asymptotic.

## Proofs

NOTATION. Work in one block. Label columns differ by multiples of S, so v2(X) ≥ v2(S) = 7 + log2 σ and 49 | X.

Normalized residues mod 7 (T2 Section 1):
- Label columns are 0. The odd label row is 0. The even label row is 5 (mixed block) or 0 (zero-residue block).
- L has row 0 and columns {3,5,6}. F has row 3 and column 0. H has row 1 and columns {1,2,4}.
- The physical parities are O odd, E even, L and F odd, H even.

Three tools:
- (Hil) For same-parity points of two labels, the Hilbert locality bound and x_f - x_e ≥ S·Δr give y^2 < 16·28^2·Δr ≤ 2|X|/σ, with y ≡ 0 mod 28.
- (Al) For every label row y and sea row s, v2(s-y) = 0 if the parities differ and = 1 if they agree. This is the Lemma AP alignment, and only mod 4 is used. The rows of a block are fixed mod 4 per parity.
- (Bulk) Label rows lie in [C1, h-C1] with C1 = 10^5. L ≤ 28, F ≤ 24000 and h-H ≤ 783.

LEMMA S1 (mod-7 sieve). Every corner triple and every mixed quadruple has a mod-7 shadow. The equations are (P1-V)·(P2-V) ≡ 0, |B-A|^2 ≡ |D-C|^2 and (B-A)·(C+D-A-B) ≡ 0, together with the row-sum parity y_A+y_B ≡ y_C+y_D. These have solutions only for the following patterns with at least two label points.

Corner triples, as vertex | ends:
- same-parity label vertex with a sea end (O|OL, O|OF, O|OH, E|EL, E|EF, E|EH);
- O|EL (mixed block), and every cross-parity label-vertex pattern (zero-residue block);
- the sea vertex H|OE (mixed block only);
- label-only patterns.

Mixed quadruples, as side|diagonal:
- a same-parity label pair against a same-row sea pair, in either role (OO|LL, LL|OO and so on);
- the same-type R2 patterns XS|XS;
- EH|OL (mixed block only);
- label-only patterns.

No pattern with exactly one sea point survives. So all six one-sea roles of T2's table and of t1_cost Lemma 1 are gone, and so is every 3-label four-support with a sea point. The nonhorizontal R1 and R3 are gone too.

Hand check of the main cases:
- Sea vertex with equal-parity ends: x^2 + (r-s)^2 ≡ 0 forces x ≡ 0 and r ≡ s, but F has row 3, not 0 or 5.
- R3 low/high side with a cross diagonal: (Δx)^2 ≡ 3 or x_H^2 ≡ 0 (mixed), or (Δx)^2 ≡ 6 or 3 (zero). All are impossible.
- R1 nonhorizontal: excluded by the norm condition, or by parity for the L/F pair.

Script: mod7_sieve.py, output out_sieve.json.

LEMMA S2 (2-adic kills under (Al), with v2(X) ≥ 2).
- (a) Right angle at a sea point with ends in two labels of opposite parity: v2((y_A-s)(y_C-s)) = 1. Then one of x_A-x_V, x_C-x_V is odd and the other ≡ 2 mod 4, so their difference X is odd. Contradiction. So T2's allowed triangles, and their six-cell events, disappear.
- (b) Right angle at a label point A, with the other end in another label of opposite parity and a sea point S: Xξ = -(y_C-y_A)(s-y_A) has v2 equal to v2(s-y_A) ≤ 1 < 2. Contradiction. So O|EL dies. Without (Al) it is fatal: W is even and lies in an L column. It has PT-like unbounded incidence, so the alignment is necessary at bounded M.
- (c) EH|OL. Write A = (0,b) and B = (u,H) for the side, C = (X,c) and D = (X+v,L) for the diagonal, with m1 = H-b and m2 = L-c. (Al) gives m_i = 2μ_i with μ_i odd, so u^2-v^2 = 4(μ2^2-μ1^2) has v2 ≥ 5. Perpendicularity reads u(2X+v-u) = -m1·Z with Z = c+L-b-H ≡ 2 mod 4, so the left side has v2 exactly 2.
 - If u is odd, then v2(v-u) = 2 and v2(u+v) = 1, so v2(u^2-v^2) = 3.
 - If u is even, then v2(u) = 1 and v2(v) ≥ 2, so u^2-v^2 ≡ 4 mod 16.
 Both contradict v2 ≥ 5.

LEMMA S3 (Hilbert kills).
- (a) A same-parity label pair against a horizontal sea pair (Lemma F, horizontal R1 and horizontal R3) needs |C-D| to be an integer with δ ≠ 0. Placement Theorem 1 excludes this (X^2 < X^2+δ^2 < (X+1)^2). If δ = 0, both segments are horizontal and D-C = ±(B-A), which is degenerate.
- (b) Same-parity label-only right angles are excluded by slopes, and so are all-same-parity label-only mixed supports. The mixed-supports note, Section 2, applies with α = 2/σ.
- (c) Thresholds. Write G = 2^{2v2(S)}·7^{2v7(S)} in mixed blocks and G = 2^{2v2(S)}·7 in zero-residue blocks.
 - Angles. For a same-parity leg (X1,Y1) and a cross leg (X2,Y2), X1·X2 = -Y1·Y2 forces G | Y1. Then |Y2| > σ|Y1|S/2 ≥ σGS/2.
 - Mixed supports. The even-component case gives the same bound. In the odd-component case, steps (8)-(13) of the mixed note with α = 2/σ and G | (p+q) give |Y| > σSG/32.
 - Rivals. 4j(Y+j) = X^2, and j, Y+j have opposite parity, so one of them is divisible by 2^{2v2(S)-2}.
 This yields the stated thresholds.

LEMMA S4 (parked triangles). Take a PT: vertex A, C = A + (X,δ), S = A + (ξ,m) with m = s - y_A, and Xξ = -δm. Then W = C + (ξ,m) = S + (X,δ). Its column ≡ ξ (mod 7), so it has the sea type s unless it is a label column, and its row is s+δ ≠ s with the same parity as s. If W is in the strip and in a sea column, it is white, and its column's only black point has the parity of row(W): this is condition (V2). A label column requires 7 | ξ, so s = F and S sits on a slot column. That case is (FW).

FW also needs ξ ≡ 0 mod S, so v2(δ) ≥ 2v2(S)-1 and v7(δ) ≥ 4, since 7 ∤ (F-y). It also needs |δ| < 2h/(Sσ), which follows from |δ||m| ≥ S|X| > Sσδ^2/2. Together these give the FW threshold.

The PTs cannot be treated as constraints. The heuristic first-moment incidence per label is ~ (3/K)·Σ_{g | m, g > K^2 M/16} log(16g/(K^2 M)), with K = 112σ. This is unbounded in h, of order (log h)^2/σ on average.

LEMMA S5 (structure of R2s). Write A = (0,y), B = (u,s), C = (X,y+δ), D = (X+v,s), m = s-y, P = u-v and t = 2X+v-u. The equations are equivalent to ut = -mδ, P(2u-P) = δ(δ-2m) and X = (P+t)/2.

Two consequences:
- (i) P divides N = δ(2m-δ), and N ≠ 0 by (Bulk). So each pair (e,f) and role forbids at most 2τ(|N|) gaps: R2s is a P-type pair family.
- (ii) Put a = P-t and b = u+v-t. Then ab = t^2+δ^2, u = (a+b)/2 + t and X = a/2 + t. For fixed (e, s, role, t, b), the condition ut = -mδ is a quadratic in δ, so it has at most 2 roots, each determining X.
So R2s satisfies a finite-factor lemma with factor pair (t,b), with no Hilbert input. A prescribed set of R factor pairs costs M ≥ 48R+1 greedy choices: 12 role and sea combinations, 2 roots and 2 earlier ranks each.

For s in {L,H} with 7 ∤ m, a 7-adic computation gives P' ≡ t' (mod 7) and hence v7(δ) = v7(X) ≥ 2. Real solutions exist: r2s_search.py finds 5 typed solutions in the h = 420 toy without (Hil). The Hilbert bound does not kill the b = 1 subfamily.

LEMMA S6 (V3 among parked triangles). Parked tilted rectangles with at least 2 labels are only PTs: T1 gives none with at most 1 label, and (Λ3) is forbidden.

Two PTs R, R' at the same W have the same sea row s, because W's column has a single type. They therefore have the same δ, and S'-S = (X-X', 0). If they share a black corner:
- sharing S gives the label-only support {A,C,A',C'} (excluded by S3(b) when all one parity, otherwise Λ4 or Λ3);
- sharing A leads to a rectangle with a vertical side through a label column, which is impossible;
- sharing C forces R = R';
- A = C' gives an R2s support.
Otherwise the six corners are distinct, which is (6PT). Since x_A' - x_A ≡ ξ - ξ' (mod S), either ξ = ξ', or |ξ-ξ'| ≥ S > 2h·sqrt(2/(σS)) fails. In the first case C and C' are the two points of one label f, and X' = X·m'/m.

COMPLETENESS (proof of H7(ii)). Rival pairs with at least 2 labels are (P). For mixed quadruples, count the sea points: 0 gives Λ4; 1 is impossible by S1; 2 splits into R1/R3 (S1 and S3(a)), cross R2 (S1 and S2(c)) and same-type R2, which is R2s. For corner triples: 0 sea points gives Λ3; 1 sea point at the vertex is impossible (S1 and S2(a)); 1 sea point with a label vertex and a cross end is impossible (S2(b)); with a same-parity end it is a PT, which is parked by S4 except for FW. A fully black rectangle contains such a triple, and its W is white unless FW. V3 pairs are handled by S6. Zero-label and one-label violations are excluded by T1 or AP4. Locality (2W_h+1) and N1 Claim (d) confine any violation to one core neighbourhood, where the board agrees with the infinite periodic sea carrying that core.

LAYOUT AND WIDTH.
- N1 Claim (d) and Lemma C apply verbatim, with "E_J avoided" replaced by "the six families avoided".
- Each block has one Hilbert core, so N1's intra-block separations (BL3) are not needed.
- Lemma TR covers the collar stages, since 2H-L > h, 2L-H < 1 and filter (7) hold.
- J5 glues the windows, which have row-h tails and separation D. Inside L***, N1(e) handles the switch z and the row-1 windows of Proposition partial unchanged.
- Each core spans less than S·M·Q^2 ≤ 32σM(h+28)^2, and 196 blocks give 6272σM(h+28)^2.
- The collars cost 196 · 2 · (2+783) · D ~ 1.54·10^5 h^2, and the separations about 98h^2.
- The exceptional labels cost O(h^2).
- Constant tails give every larger width.

LEMMA AP4 (adaptation of T1, proof sketch). For each class, L mod 28 is forced (odd, ≡ a mod 7, ≡ a+2 mod 4), and so are H mod 28 and F mod 28.
- H: take 28 candidates in [h-783, h]. Each j ≤ 27 in filter (7) excludes at most one of them.
- F: take 784 candidates in [2000, 2000+21952]. Each j ≤ 783 in filter (8) excludes at most one.
- Margins (6) and (9) hold for bulk rows [10^5, h-10^5].
- T1 Sections 2 to 6 use only residues mod 7, parities, the filters and the margins, so the one-label theorem, the hole-choice property and the collars carry over unchanged.

CHECKS (sanity only; each run under 60 s). Script folder scripts_hb1_sea/.
- mod7_sieve.py checks Lemma S1.
- toy_roles.py brute-forces an aligned toy block: h = 420, label columns ≡ 0 mod 28 placed at random, 30 labels, mixed and zero-residue blocks, 4 runs. The only multi-label roles found are PT, label-only, and horizontal pairs, which the toy has because it has no Hilbert placement. Nothing unexpected appeared.
- toy_control.py is a misaligned control. It produces exactly the predicted killed families H|OE, H|EO and O|EL.
- pt_census.py runs a real Hilbert block (S = 6272). The mean number of PT candidates per label is 0.067, 0.10 and 0.06 for M = 1, 2, 4 at h = 4·10^4 (max 2-3), and 0.13 at h = 8·10^4 with M = 2.

## External results used

- Placement Theorem 1 and the Hilbert locality bound max(Δi^2, Δj^2) < 16|Δr| (continuation_hilbert_placement.md, audited), in the profile form y^2 < 16d^2·Δr.
- Mixed-support note, Sections 2-3 (audited): the all-same-parity exclusion and the parity-case inequalities, reused with α = 2/σ and 7-adic factors.
- T1 profile theorem (filled_mod7_profile_cover.md, audited) and its mod-4 adaptation AP4 (unaudited): one-label substitution at any period-zero column, the hole-choice property and the collars.
- T2 Section 1 (block split, normalized residues); t1_cost Theorem B (1a), (2a) and the Lemma AP alignment idea (unaudited).
- N1 layout: Lemma C, Lemma TR and Claim (d) (unaudited). J5 gluing (audited A9). Paper sec5: the 2W_h+1 locality, Lemmas rival, sea and chain, and the reduction lemma. sec2: Lemma diff and Lemma mixedeq.
- The criterion (V1)-(V5) of block_sea_classification.md, whose proof rests on the audited axis-owner lemma and Lemma 2 of lower_bound_windows.md.

## Checks

Scripts, run one at a time with py, each under 60 s, in scripts_hb1_sea/:
- mod7_sieve.py, with output out_sieve.json.
- toy_roles.py: 4 aligned runs with no unexpected roles.
- toy_control.py: misaligned control. The killed families appear, so the detector works.
- r2s_search.py and r2s_hilbert.py: R2s algebra checked against the defining equations by assertions. Typed solutions exist. Note that r2s_hilbert.py scans only s in {L, F}, so its zero count is not a general claim.
- r2s_notype.py: the same search without sea-type constraints.
- pt_census.py: PT candidates in a real Hilbert block.

By hand: the mod-7 cases of S1, S2(a)-(c), the R2s identities ab = t^2+δ^2, u = (a+b)/2+t, X = a/2+t, and all the threshold constants (3.6e8, 1.2e11, 2.2e7, 7.7e9, 6.1e10, 4096, 1.75e5, all times the stated powers of σ).

## Gaps

- The six residual families (P), (Λ3), (Λ4), (R2s), (FW) and (6PT) are not shown to be avoidable at bounded M. For every one of them only average or heuristic incidences, absence thresholds and per-pair or per-factor bounds are known, not worst-case per-label bounds. The corollary width is conditional on avoiding all six.
- Lemma AP4, the mod-4-aligned T1 profiles, adapts the audited T1 proof with larger windows. I checked it by reading only, and it is not audited. verify_filled_mod7_profiles.py has not been rerun with the mod-28 conditions. Lemma AP (the mod-16 version in t1_cost_decomposition.md) is also unaudited.
- N1, including Lemma C, Lemma TR, Claim (d) and Lemma RL, is unaudited. I reuse it with the Hilbert core in place of the dyadic classes.
- Lemmas S1-S6 and Theorem H7 are new and unaudited. S1 is a finite mod-7 statement, checked by hand and by script. S2(c) and S5 are short computations that I did once.
- The (FW), (6PT) and (R2s) families, and every family involving F points on slot columns, are not monotone under deleting labels: emptying a slot creates F points. Lemma RL therefore does not apply to them, and their candidates must be counted over all occupancy states.
- The PT incidence estimate (unbounded, order (log h)^2/σ) is a first-moment heuristic, calibrated only by a census at h ≤ 8·10^4. It is used only to argue that PTs must be parked rather than constrained. Their harmlessness is proved and does not depend on it.
- Remark, not used in the theorem: label-only right angles with an even vertex have an odd white corner in a column ≡ 0 mod 7. They are parked when that column is an F column. So the hypothesis on Λ3 can be weakened to odd-vertex angles, angles whose W is in a label column, and their V3 collisions. I have not worked out the extra six-cell types this creates.
- The exceptional-label blocks, built by the positional lemma in binary backgrounds with collars to row h, are cited from compatible_profile_threshold Section 1. I did not re-derive their tails.

## Missing estimate

To get m_h = O(h^2) from H7, a bounded M (with σ = 1) is needed that avoids, in each block, all of (P), (R2s), (FW), (6PT), (Λ3) and (Λ4). Concretely this needs worst-case or induced-average control of the candidate constraints. Two of the families are pair families with a factor structure:
- P, with factor a = (L-|Y|)/2;
- R2s, with factor pair (t,b) satisfying ab = t^2+δ^2. Each such factor forbids at most 4 earlier choices for each of 12 role and sea combinations, so at most 48.
The local criterion of continuation_hilbert_local_factor_budget, M > 8·max_U avg F_U, is the natural target for the two families together. The other two sea families have three or four labels and are sparse: FW needs h > 6·10^10 σ^4, and 6PT needs shared slot residues. A product-form local lemma over the private choices would handle them if their candidate counts per label are at most M^2/C, uniformly over labels.

Growing σ like a power of log h lowers every average incidence by powers of σ, but it removes no family deterministically, because every threshold is polynomial in σ: σ^4 for Λ and FW, σ^2 for P and 6PT. So the trade-off does not close the problem by itself.

## Next steps

- Have a second reader audit Lemmas S1-S6, especially S2(c) (the 2-adic kill of EH|OL), the S5 parametrization (ab = t^2+δ^2, P | N, the two roots per (t,b)) and the S6 reduction of shared-corner collisions.
- Audit Lemma AP4 and rerun verify_filled_mod7_profiles.py with the mod-28 conditions: L ≡ F ≡ a+2 and H ≡ b+2 (mod 4), H in [h-783, h], F in [2000, 23952].
- Run a census of R2s per label in a real Hilbert block (S = 6272, h about 10^5), using the (t,b) parametrization: enumerate (t,b,root) per label and check the rank and offset of f. Add it to the P census to test the joint criterion M > 8·max avg F.
- Merge the R2s factor pairs into the P local factor budget, as one constraint multigraph with two factor types, and test whether three or four choices certify the in-strip P ∪ R2s family at h = 2048 and 4096 in the profile placement.
- Prove or refute a bound on 6PT in the subcase ξ = ξ'. That subcase is a 3-label configuration (e, f, e') with C and C' the two points of f and X' = X·m'/m. A 2-adic or 7-adic kill looks plausible but was not found.
- For the gap-(2) work: only odd-vertex label-only angles, and those with W in a label column, are fatal. Even-vertex ones are parked in F columns, which may shrink the angle family that has to be excluded.

