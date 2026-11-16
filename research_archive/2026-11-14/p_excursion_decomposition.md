# The P system splits into excursions between diagonal cells

15 November 2026. Problem 001. Continues continuation_gap_mixing_audit.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: at S = 32 and M >= 3, the P candidate graph splits exactly into the Hilbert curve's excursions between consecutive main-diagonal cells, and no constraint joins two excursions at any height. So the global P system needs no boundary conditions: it is solvable exactly when every excursion is, and each excursion of scale B is a fixed system that recurs unchanged at every large h. The weighted 4-core is empty in all excursions of scale <= 512 and nonempty in both scale-1024 excursions, so it is nonempty at every h >= 8,404,993. Found independently in p_cross_scale_chains.md. Audited in ../2026-11-15/audit_p_excursion_decomposition.md (correct with fixable gaps).

# Result

## Status

partial

## Summary

The P candidate graph at S = 32, M >= 3 splits exactly into the Hilbert curve's excursions between consecutive diagonal cells. No constraint joins two excursions, at any height. So the global P system needs no boundary conditions: it is solvable exactly when every excursion is. Each excursion of scale B is a fixed system that recurs unchanged at every large h. With these pieces I located the weighted 3- and 4-cores. The 4-core is empty in all excursions of scale <= 512, but it is nonempty in both scale-1024 excursions, so it is nonempty at every h >= 8,404,993.

## Statements

Setting: full grid, label e = (i,j) with rows a = 2i+1, b = 2j+2, T = j - i. Ranks come from H_Q with recursion (2) of continuation_hilbert_placement.md, and they are not compressed. Placement x = S(M r + xi). A candidate constraint is a triple (v, w, delta) with r_v < r_w, d = r_w - r_v and q = Md + delta, |delta| <= M-1, that has a cross pair (odd row of one label, even row of the other) with (Sq)^2 + Y^2 = L^2. Every statement below uses only this Pythagorean condition, so it also holds for any subset of the candidates: the strip-restricted set at any h, the genuine rivals, and any label subset with ranks retained.

Notation. For 0 <= x < Q-1, let B_x = 2^{v2(x+1)}. D_x = [x+1-B_x, x+1+B_x)^2 is the aligned main-diagonal block of side 2B_x whose centre is (x+1, x+1), and o_x in {id, swap} is its orientation (Theorem A). The excursion E_x is the set of labels whose rank lies in [rho(x,x), rho(x+1,x+1)), and E_{Q-1} is the set of labels from rho(Q-1,Q-1) to the end. P_B^o is the local candidate system (no strip test, no owner test) on the excursion of scale B inside a diagonal 2B-block of orientation o. Tail_B^o is the final excursion of a diagonal B-block of orientation o.

PROVED (S = 32, every M >= 3, every h)

(A) Shape of the excursions. H_Q visits the diagonal cells in the order (0,0), (1,1), ..., (Q-1,Q-1). E_x has (4B^2+2)/3 labels, with B = B_x. It is the diagonal cell (x,x), then the staircase blocks of sides 1, 2, ..., B/2 (the fourth children of the chain D1, D1.3, D1.3.3, ... of D_x), then the off-diagonal child O2(D_x) of side B. Its off-diagonal labels all lie on one side of the diagonal, with 1 <= |T| <= 2B-1: T > 0 when o_x = id and T < 0 when o_x = swap.

Lemma A' (rank-length bound). If a constraint has an endpoint z with |T_z| <= 2s-1, for an integer s >= 1, then d <= s^2.

Lemma B (no entry from the left). Let E be any aligned main-diagonal block, of any side and position. No constraint joins a label of rank < rho(E) to a label of E. In particular, no constraint ever joins two disjoint main-diagonal blocks.

THEOREM E (excursion decomposition). For every diagonal cell (x,x) with x >= 1, no constraint has rho(v) < rho(x,x) <= rho(w). Equivalently, every component of the candidate multigraph lies inside a single excursion E_x.

Corollary L (links). Call the staircase blocks and O2 of an excursion its links. Inside E_x, constraints join only labels of the same link or of two consecutive links.

COROLLARY R (exact reduction, no boundary condition).
(a) xi solves the candidate P system at height h if and only if its restriction to each E_x solves the system induced on E_x. Solutions chosen independently on the excursions always combine, with no boundary list and no certification.
(b) For x < Q-1, the system induced on E_x at height h is contained in a rank translate of P_{B_x}^{o_x}. Equality holds whenever h >= 8B^2 + 16B + 1 and D_x lies in the Corollary A1 interval for side 2B. The system on E_{Q-1} is contained in a translate of Tail_Q^id, which is contained in P_Q^swap.
(c) Hence the candidate P system is M-solvable at every height if and only if P_B^o is M-solvable for every B = 2^b and both orientations. At a single height, solvability of P_B^o for all B <= Q suffices.
(d) Each block system decomposes the same way: G_{2B}^{o,cand} is the disjoint union, over its 2B - 1 interior diagonal cells, of translates of P_{B_x}^{o_x}, together with Tail_{2B}^o.

COROLLARY C (location of the weighted M-core). K_M(h) is the disjoint union over x of K_M(E_x(h)). For x < Q-1, K_M(E_x(h)) is contained in the translate of K_M(P_{B_x}^{o_x}), with equality in the A1 range of (b).

EXACT COMPUTATION (my own builder; candidate version; it reproduces every archived count)
M = 3:
- K_3(P_B^o) is empty for B <= 128 in both orientations, and for (256, id).
- (256, swap): 2313 labels, all in O2, T in [-489, -194].
- (512, id): 43508 labels, all in O2, T in [349, 1020].
- (512, swap): 60046 labels (56590 in O2, 3133 in the 256-link, 323 in the 128-link), T in [-1019, -177].
- (1024, id): 519350 labels (484266 in the 1024-link, 34573 in the 512-link, 511 in the 256-link), T in [349, 2047].
- (1024, swap): 550332 labels, T in [-2043, -177].
- Tails: Tail_512^id has 3134, Tail_512^swap has 0, Tail_1024^id has 48205, Tail_1024^swap has 29122.

M = 4:
- K_4(P_B^o) is empty for B <= 512, and K_4(Tail_B^o) is empty for B <= 1024.
- (1024, id): 176459 labels (175080 in O2, 1379 in the 512-link), T in [771, 2047].
- (1024, swap): 248191 labels (247120 in O2, 1071 in the 512-link), T in [-2043, -735].

Consequences:
- (i) At every h, reverse peeling solves every excursion of scale <= 128 at M = 3 and every excursion of scale <= 512 at M = 4.
- (ii) K_4(h) is nonempty at every h >= 8,404,993 = h0(2048). Degeneracy certificates for M = 4 therefore cannot extend past that height.
- (iii) The archived cand certificates for G_1024^id and G_1024^swap are 3-choice solutions. My builder confirms them: 0 violations and 0 mod-3 violations, for both cand and gen constraints. Restricted to excursions, they 3-solve every excursion of scale <= 512 at every height, and the final excursion whenever Q <= 1024. So the M = 3 candidate P problem at S = 32 is exactly the family {P_B^o : B >= 1024}, plus the final excursion when Q >= 2048.
- (iv) Refutation: removing every main-diagonal block of side <= 256 does not leave a 2-degenerate graph at any h >= 528385. The 2313-label core of P_256^swap lies entirely in an off-diagonal block of side 256. The same holds for side <= 512 at h >= 2,105,345, by the 43508-label core inside O2 of P_512^id.

## Proofs

1. ORDER AND SHAPE (A). By recursion (2), H_{2q} lists its quadrants in this order:
- Q1 = (y, x), the transpose, on [0,q)^2;
- Q2 = (x, y+q), with T > 0;
- Q3 = (x+q, y+q), on [q,2q)^2;
- Q4 = (2q-1-y, q-1-x), with T < 0.
Diagonal cells lie only in Q1 and Q3, and a transpose fixes diagonal cells. By induction, H_q visits its diagonal in increasing order, so H_{2q} does too, because Q1 precedes Q3. The same holds for the transposed curve, and by Theorem A every main-diagonal block is id or swap.

Let x+1 = odd * B. Then D = D_x = [x+1-B, x+1+B)^2 is aligned. (x,x) is the last diagonal cell of D1 = [x+1-B, x+1)^2, and (x+1,x+1) is the first cell of D3. So E_x consists of three parts, in rank order:
- (x,x);
- the part of D1 after (x,x);
- all of O2(D), which has B^2 labels.

Write a diagonal block F as Q1(F), Q2(F), Q3(F), Q4(F). Unrolling F = Q1(F) + Q2(F) + Q3(F) + Q4(F) along the Q3-chain of D1 shows that the part of D1 after (x,x) is the union of the fourth children of D1, D1.3, D1.3.3, .... These have sides B/2, B/4, ..., 1, so their total size is (B^2-1)/3. Hence |E_x| = 1 + (B^2-1)/3 + B^2 = (4B^2+2)/3.

For an id block, O2 lies in T > 0. D1 has orientation swap, and the fourth child of a swap block is the transpose of (2q-1-y, q-1-x), which also lies in T > 0. The Q3 children keep the orientation, so the whole staircase lies in T > 0. A swap D gives the mirror image. All labels lie in D, so |T| <= 2B-1.

2. TWO INPUTS. For a constraint (v, w) there is a cross pair with Y = |2U+1|, where U = j_w - i_v or U = j_v - i_w (L1 with c = 1, D = 2).
- Then U - T_w is i_w - i_v or j_v - j_w, and U - T_v is j_w - j_v or i_v - i_w. Locality max(Di^2, Dj^2) < 16d therefore gives |U - T_z| < 4 sqrt(d) for z = v, w.
- L^2 = X^2 + Y^2 > X^2 forces L >= X + 1, so Y^2 >= 2X + 1 = 2Sq + 1. Since q = Md + delta >= M(d-1) + 1, with S = 32 and M >= 3 we get (*) Y^2 >= 192(d-1) + 65 = 192d - 127.
- Finally Y <= 2|U| + 1.

3. PROOF OF LEMMA A'. Suppose d >= s^2 + 1. By section 2:
- Y < 2(|T_z| + 4 sqrt(d)) + 1 <= 4s - 1 + 8 sqrt(d);
- with (*), g(d) := sqrt(192d - 127) - 8 sqrt(d) < 4s - 1.

g is increasing for d >= 1. Indeed g'(d) > 0 iff 24 sqrt(d) > sqrt(192d - 127), which is 576d > 192d - 127. So g(d) >= g(s^2+1) = sqrt(192s^2 + 65) - 8 sqrt(s^2+1). Now check g(s^2+1) >= 4s - 1:
- For s = 1, g(2) = 16.0312 - 11.3137 = 4.717 >= 3.
- For s >= 2, sqrt(192s^2 + 65) > 13.856s and 8 sqrt(s^2+1) < 8s + 4/s. So g > 5.856s - 4/s, and this is >= 4s - 1 because 1.856s + 1 >= 4/s.

This contradicts g(d) < 4s - 1. QED.

4. PROOF OF LEMMA B. Let E = [x0, x0+s)^2, and let w be at rank offset m in [0, s^2), so w is in E. Let v be at rank rho(E) - k with k >= 1, so d = k + m >= m + 1.
- Let R be the least power of two with R^2 >= m+1. Then R <= s.
- The first R^2 ranks of E are the diagonal block [x0, x0+R)^2. This is the iterated Q1 child, which sits at the lower-left corner for both orientations. So |T_w| <= R - 1 < 2 sqrt(m+1) - 1 <= 2 sqrt(d) - 1. (If R >= 2, then (R/2)^2 < m+1; if R = 1, then 1 < 2.)
- Hence |U| < 6 sqrt(d) - 1, so Y < 12 sqrt(d) - 1.
- With (*): 192d - 127 < 144d - 24 sqrt(d) + 1, that is, 48d + 24 sqrt(d) < 128. This fails for d = 2 (129.9) and for every d >= 2, so d = 1.
- Then k = 1 and m = 0, so w = (x0, x0), T_w = 0 and |U| < 4. That gives Y <= 7. But by T1, Y = k'|E^2 - O^2| >= 2E - 1 >= S - 1 = 31. Contradiction.

Two disjoint diagonal blocks occupy disjoint rank intervals (Theorem A), and a constraint between them would enter the later one from the left. QED.

5. PROOF OF THEOREM E. Use strong induction on x; rho(x,x) increases with x by (A).
Let s = 2^{v2(x)}. Put E = [x, x+s)^2 and D = [x-s, x+s)^2. D is aligned with side 2s, E is its third child, and rho(x,x) = rho(E) = rho(D) + 2s^2. Suppose rho(v) < rho(x,x) <= rho(w).
- (i) If w is in E, this contradicts Lemma B.
- (ii) Otherwise rho(w) >= rho(D) + 3s^2.
  - If rho(v) >= rho(D), then v lies in the first two children of D, so |T_v| <= 2s - 1. Also d >= 3s^2 - (2s^2 - 1) = s^2 + 1, which contradicts Lemma A'.
  - If rho(v) < rho(D), then x - s >= 1, because rho(0,0) = 0 is the global start. Then rho(v) < rho(x-s, x-s) <= rho(w) with x - s < x, which contradicts the induction hypothesis.
QED.

The excursions are exactly the rank intervals between these cuts, so every constraint stays inside one of them.

6. COROLLARY L. In rank order the links are L_1, ..., L_{n+1}, with sides 1, 2, ..., B/2, B. A link of side s_a lies in [x+1-2s_a, x+1-s_a) x [x+1-s_a, x+1), or its transpose, so 1 <= |T| <= 2s_a - 1. O2 has side B and 1 <= |T| <= 2B - 1.

Suppose a constraint joins L_a and L_b with a <= b - 2. Its rank length is at least s_{b-1}^2 + 1. Its endpoint in L_a has |T| <= 2s_a - 1 <= 2s_{b-1} - 1, so Lemma A' gives d <= s_{b-1}^2. Contradiction. QED.

7. COROLLARY R.
(a) Theorem E makes each excursion a union of components.
(b) Candidate constraints between two labels depend only on their local coordinates and their rank difference. The global set at height h adds the strip test and possibly the owner test, so it is a subset of the local candidate set. For x < Q-1, E_x lies in D_x, so the system is contained in a translate of P_{B_x}^{o_x}.
  - Equality: the audited Corollary A1 shows that for D_x in the interval (2B)^2/2 <= x+1-B <= (h - 4B^2 - 4B - 1)/2, every completion row lies in [1, h] and L <= h - 1. So local and global candidates coincide on D_x, and that interval contains both orientations once h >= 2(2B)^2 + 8(2B) + 1.
  - E_{Q-1} lies in the top block, which is id. Put the top block as Q1 of a virtual swap block P of side 2Q. Then E_{Q-1} becomes the staircase part of P_Q^swap, with the same local geometry.
(c) Combine (a) and (b). For the converse, take h >= h0(2B).
(d) Apply (A) and Theorem E inside the block.
QED.

8. COROLLARY C. The weighted core of a disjoint union is the union of the cores, and cores are monotone under subgraphs. QED.

9. CONSEQUENCES.
- (i) An empty core means reverse peeling succeeds (L9 of gap_mixing_full_components.md).
- (ii) Take K_4(P_1024^o), which is nonempty, together with (b) at h0(2048) = 2*2048^2 + 8*2048 + 1 = 8,404,993.
- (iii) G_1024^{o,cand} contains a translate of every P_B^{o'} with B <= 512, for both o', and of Tail_B for B <= 1024 (by (d), and by Theorem A both orientations occur at each scale). A solution restricts to each of them, and the restrictions transfer to every height by (a) and (b).
- (iv) The cores of P_256^swap and P_512^id lie entirely in O2(D_x). That block is disjoint from every diagonal block of side <= B, and it occurs at every h >= h0(2B) by (b).

## External results used

- Hilbert locality max(Di^2, Dj^2) < 16|Dr| for the recursion-(2) curve, ranks not compressed: Theorem 1 and Section 1 of continuation_hilbert_placement.md (audited). Used in Lemmas A' and B.
- T1 normal form of hilbert_p_family_counts.md (audited). Used only for Y >= 2E - 1 >= S - 1 = 31.
- L1 edge-diagonal identity (2U + 1 = eta Y in the full grid) and the bound Y^2 >= 2X + 1 from L2(iv), gap_mixing_full_components.md, audited in audit_gap_mixing_full_components.md.
- Theorem A (diagonal blocks are id or swap, with contiguous ranks and the child orientation rule) and Corollary A1 (the block system embeds unchanged in the A1 interval, both orientations, for h >= 2B^2 + 8B + 1), hilbert_p_height_independent_cores.md, confirmed by audit_gap_mixing_full_components.md. Used only in Corollary R(b) and its consequences (ii) to (iv).
- L9 reverse peeling, audited. Used for the meaning of empty cores.
- Archived certificates scripts_gm2_core_exact/certificates_B1024_M3.npz (gap_mixing_block_cores_m3.md, not audited). Re-verified here with an independent builder. Used only in consequence (iii).
- No published theorem was used, and no web source was consulted.

## Checks

All scripts are in scripts_gm3_global_core/ (172 KB). Each ran with py -I, one at a time, in 0.5 s to 22 s and well under 1 GB. I only read the repository, ran no git command, and left Kagey-Problems untouched.

- excursions.py (B, orient, M, version) is my own builder. It builds the Hilbert curve from recursion (2) and the vectors from divisor pairs of Y^2 with 32 | X. It scans both slots and both roles, applies the owner test for gen, and keeps distinct triples.
  - It reproduces the archive exactly: 229 and 216 constraints (B32 id and swap, gen), 1726 (B64), 48419 (B256), 250953 and 250053 (B512 gen), 1205405 and 1202041 (B1024 gen), and 1344642 and 1341364 (B1024 cand).
  - Core sizes also match: 3134, 2295 and 2313 at B512; 40136, 42125, 94026 and 91481 at B1024; every 4-core empty.
  - For every system with B <= 1024, both orientations, both versions, M = 3 and 4, it finds 0 constraints joining two excursions and 0 constraints entering any diagonal sub-block from an earlier rank. It also confirms the excursion lengths (4B'^2+2)/3. At B = 1024 this covers the whole global candidate graph for h <= 2048.
- one_excursion.py builds P_B^o directly; the excursion is closed by Theorem E. At side 1024 it reproduces the excursion cores 43508 (id) and 60046 (swap) found in the full block. At side 2048 it gives:
  - M = 4: 3150814 constraints, 4-core 176459 (id); 3153976 constraints, 4-core 248191 (swap).
  - M = 3: 2403112 constraints, 3-core 519350 (id); 2409750 constraints, 3-core 550332 (swap).
- check_links.py tests Corollary L and Lemma A'. At sides 1024 and 2048 the maximum link-side ratio on any constraint is 2. Lemma A' (d <= ceil((|T|+1)/2)^2 at the endpoint with smaller |T|) held on every constraint. About 99.4% of constraints stay inside one link (499497 of 502517; 2391690 of 2403125 incidences).
- check_certs.py verifies the archived certificates_B1024_M3.npz with my builder. The cand certificates, id and swap, have 0 violations and 0 mod-3 violations against cand and against gen. The gen certificates satisfy gen only, as expected.
- I checked these proofs by hand: (A), section 2, Lemma A' (including s = 1 and the monotonicity of g), Lemma B (including the boundary case d = 2, where 129.9 > 128, and d = 1 by T1), Theorem E (both cases of the induction), Corollary L, and Corollary R (including the virtual parent for E_{Q-1}).

## Gaps

- The bounded-M P problem at S = 32 is not solved. By Corollary R it is now equivalent to M-solvability of every excursion system P_B^o; for M = 3 only the excursions of scale B >= 1024 (and the final excursion when Q >= 2048) remain open. No rule solving P_B^o for all B is known, and no obstruction was found.
- Where the core sits inside an excursion (almost all of it in the O2 link and the next one or two links, with |T| from about 177, or about 735 at M = 4, up to 2B-1) is exact data for B <= 1024 only. It is not proved for general B.
- Excursions of scale B larger than about sqrt(h/8), including the final excursion E_{Q-1}, are cut by the strip. For them Corollary R gives only an inclusion in P_B^o, so their actual cores at a given h are not located. Most labels of the grid lie in such excursions. For M = 4 and 4096 < h < 8,404,993 I did not locate the 4-core.
- The nonempty 4-cores of P_1024^o and the 3-cores at B = 1024 come from one implementation, mine. It reproduces every archived count up to B = 1024: 229, 216, 1726, 48419, 250953, 250053, 1205405, 1202041, 1344642 and 1341364 constraints, and the core sizes 3134, 2295, 2313, 40136, 42125, 94026 and 91481. The B = 2048 excursions have no second implementation and no audit.
- Consequence (iii) for M = 3 rests on the archived certificates, which I re-verified with an independent builder. The block_cores note itself is not audited.
- Solvability at M = 3 of the cores of P_1024^id (519350 labels) and P_1024^swap (550332 labels) was not tested. I had no SAT solver in scope, and I did not want to start a larger census.
- This covers the P family only, for the full grid (c = 1, D = 2). R2s, FW, 6PT, Lambda3 and Lambda4, the sea and the collars are untouched. The excursion theorem may fail for those families.
- I did not prove the transfer to profile boards (H7 with D = 28, S = 8 D^2 sigma, offset c). The constants in Lemmas A' and B depend on Y = |c + DU|, and a quick estimate suggests the transfer needs roughly sigma M >= 3 and |c| <= D/2. That remains unchecked.
- The general-stride version is only sketched: the same proof works whenever S >= 16, SM >= 96 and S(M+1) >= 128 (for example S = 64, M >= 2). I checked S = 64, M = 2 by hand but did not write it out.
- Nothing here is audited. Lemmas A' and B, Theorem E and Corollary R are short, and they should go to an independent reader.

## Missing estimate

After Theorem E, the P question at S = 32 has no gluing part left. One needs an M such that every excursion system P_B^o is M-solvable, for every B = 2^b and both orientations. Each P_B^o is a fixed finite system: a path of off-diagonal links of sides 1, 2, ..., B/2, B ending in the O2 block, with constraints only inside a link or between consecutive links.

For M = 3 the open cases are B >= 1024, whose 3-cores have 519350 (id) and 550332 (swap) labels at B = 1024. Every case with B <= 512 is certified. For M = 4, peeling already fails at B = 1024.

The cores grow faster than the excursions. At M = 3 the core is 0.7%, 12 to 17%, and 37 to 39% of the excursion labels at B = 256, 512 and 1024. So a structural rule for P_B^o must cope with cores that fill a growing fraction of the O2 block. The natural object is the O2 link alone, an off-diagonal Hilbert block of side B with T in [1, 2B-1], which carries almost all of every core.

## Next steps

- Audit Lemmas A' and B, Theorem E and Corollary R. They are under a page and carry the whole reduction. Record in the ledger that P components never cross a diagonal visit of the curve (S = 32, M >= 3), and that the global P system is the disjoint union of the excursion systems P_B^o, with no boundary conditions.
- One exact certificate on a fixed system: test 3-solvability of the 3-cores of P_1024^id and P_1024^swap, splitting the work into runs under 60 s. A solution extends M = 3 to every excursion of scale <= 1024 at every height. An UNSAT core would, by Corollary R(b), block M = 3 for the candidate system at every h >= 8,404,993. A genuine-rival obstruction would need the gen version.
- Retarget structural work to single links. Almost all of every core lies in the O2 link: 100% at (512, id) and (256, swap), and about 93% to 99% at B = 1024. Look for a choice rule on an off-diagonal block of side B, adjacent to the diagonal, that tolerates the few links between consecutive blocks (about 0.6% of constraints).
- Write out the profile-board version (D = 28, offset c, S = 8 D^2 sigma) of Lemmas A' and B, so that the excursion theorem covers H7.
- Check whether the excursion argument extends to the other families (R2s, FW, 6PT, Lambda3 and Lambda4). Any family whose constraints obey a rank-length bound like Lemma A', with a cross-pair diagonal tied to T, would split the same way.
- Update gap_mixing_block_cores_m3.md and gap_mixing_full_components.md where they say that other components may attach to a block. By Lemma B nothing enters a diagonal block from the left, and by Theorem E full components and M-core components never leave their excursion.

