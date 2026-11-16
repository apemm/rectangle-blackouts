# Three choices on the recurring block cores

15 November 2026. Problem 001. Continues continuation_gap_mixing_audit.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (exact finite certificates): at S = 32, every weighted 3-core of the recurring main-diagonal block systems G_256, G_512 and G_1024, in both orientations and with or without the owner filter, has a 3-choice assignment; each is mod-3 certified, extends to the whole block by reverse peeling, and was checked by an independent second program; every 4-core is empty. A nesting corollary transfers the B = 1024 certificates to every main-diagonal block with B <= 1024. So, given Corollary A1 of hilbert_p_height_independent_cores.md (checked by brute force at h0(32) = 2305 in audit_gap_mixing_full_components.md), these blocks never obstruct M = 3 at any large h. This does not prove the global P system is 3-solvable. The shift quotient with independently solved two-gap pieces fails on these cores (some piece pairs are fully blocked). The four B = 1024 certificates at M = 3 (id and swap, gen and cand) are saved in scripts_gm2_core_exact/certificates_B1024_M3.npz; extract one array with numpy and pass it to verify_full.py. Audited in audit_gap_mixing_block_cores.md (correct with fixable gaps; an independent checker confirms all four saved certificates).

# Result

## Status

proved

## Summary

At S = 32 the recurring block systems never block M = 3: every weighted 3-core of G_256, G_512 and G_1024 (both orientations, with and without the owner filter) has a 3-choice assignment. Each one is even mod-3 certified, extends to the whole block, and was checked by a second, independent program. M = 4 is trivial because every 4-core is empty. No UNSAT certificate was needed. The shift-quotient theorem with independently solved two-gap pieces fails on these cores, because some piece pairs are fully blocked.

## Statements

Setting: S = 32. G_B^o, for o in {id, swap}, is the main-diagonal block system of Corollary A1 in hilbert_p_height_independent_cores.md. "gen" means the owner of the completion rows lies outside the block (the archive's G_B^o). "cand" means there is no owner test. Constraint counts match the archive exactly.

THEOREM 1 (exact finite certificates, computer-checked). For B in {256, 512, 1024}, o in {id, swap} and version in {gen, cand}:
(a) M = 3. The whole block system G_B^o has an explicit assignment xi: [0, B^2) -> {0,1,2} that violates none of its constraints. The assignment is mod-3 certified: for every constraint (r, u, delta), xi_u - xi_r is not congruent to delta mod 3. Equivalently (Lemma 2), all three shifts (xi + kappa) mod 3 are solutions. Nothing is unsatisfiable, so no UNSAT certificate exists or is needed.
(b) M = 4. The weighted 4-core of every one of these 12 systems is empty, so reverse peeling solves each of them. The assignments were built and checked.
Sizes of the 3-cores (labels / constraints / components; distinct gaps per component):
- gen B1024 id: 40136 / 81898 / 5; 318, 234, 59, 81, 43. This matches the archive.
- gen B1024 swap: 42125 / 84944 / 5; 297, 248, 52, 73, 50.
- cand B1024 id: 94026 / 189559 / 10; largest 368, 313, 225, 134.
- cand B1024 swap: 91481 / 183683 / 10; largest 376, 273, 220, 133.
- gen B512 id: 3134 / 6197 / 2; 59, 73. This matches the archive.
- gen B512 swap: 2295 / 4461 / 2; 81, 50.
- cand B512: 3134 (id), 2313 (swap).
- B256, every version and orientation: the 3-core is empty.

COROLLARY 3 (nesting; proved, plus a check). The cand system of a diagonal 2B-block, restricted to its two diagonal children, is exactly the cand systems G_B^{o∘swap} (Q1) and G_B^{o} (Q3), shifted in rank. Also, gen is a subset of cand. So the two cand B = 1024 certificates solve, by restriction, every gen and cand main-diagonal block system G_B^o with B <= 1024, in both orientations, at M = 3.

COROLLARY 4 (meaning for large h; conditional on Corollary A1, which is unaudited). Corollary A1(i) can never yield an obstruction to M = 3 at S = 32 from a main-diagonal block of side B <= 1024. The same holds for the larger cand systems. Under the global candidate definition (X = S(Md + delta), a cross-parity Pythagorean pair, completion rows in [1, h]), those cand systems are the induced candidate systems on such blocks at every h >= 2B^2 + 8B + 1. Any block obstruction to M = 3 would need B >= 2048, or off-diagonal blocks, or interaction with labels outside the block. This does NOT prove that the global P system is 3-solvable at any h.

PROPOSITION 5 (shift quotient with independent two-gap pieces fails on these cores; computer-checked). I partitioned each core into pieces whose induced constraints carry at most two gaps, avoiding the exceptional pairs {3, 9k+4} and {3, 9k+5}, and gave each piece a mod-3 certified assignment found independently. Some pairs of pieces then carry crossing constraints with all three values of c_e. The counts are 5 pairs (B512 id), 15 (B1024 id) and 8 (B1024 swap). So the mod-3 quotient of Theorem II.1 is unsatisfiable (Lemma 6), and the exact quotient is unsatisfiable too wherever it was decided. Trivial singleton pieces with an exactly solved quotient do work: that quotient is the mod-3 certified system, and Theorem 1(a) solves it.

## Proofs

Lemma 1 (an empty core is solvable; this is L9 with K empty). Peel the labels in some deletion order v_1, v_2, .... When v_k is deleted, it has at most M-1 distinct triples to labels still present. Assign the labels in reverse deletion order. When v_k's turn comes, the labels already assigned are exactly the ones present at its deletion, so at most M-1 triples bind it. Given the other endpoint's value, each triple forbids at most one value of xi_{v_k}, so a value remains. QED.
The same proof holds verbatim for the mod-M certified system, since a certified triple also forbids exactly one value given the other end. So a certified core solution extends to a certified solution of the whole system. That is how the full certified assignments were built.

Lemma 2 (certified iff all shifts solve; any M). Let y take values in Z_M, and let c' in [0, M-1] be the residue of y_u - y_r. For a shift kappa, the integer difference D(kappa) = ((y_u + kappa) mod M) - ((y_r + kappa) mod M) is congruent to c', and it lies in [-(M-1), M-1]. If c' = 0, then D = 0 for every kappa. If c' >= 1, then D = c' for exactly M - c' shifts and D = c' - M for exactly c' shifts. The integers delta with |delta| <= M-1 and delta ≡ c' mod M are {0} when c' = 0 and {c', c' - M} otherwise. Each of them equals D(kappa) for some kappa. So a constraint (r, u, delta) holds under every shift iff delta is not congruent to c', that is, iff y is certified on it. QED.
In the certified system, delta ≡ q (mod M) because q = M d + delta. So the certified constraint on a pair reads y_u - y_r ≢ q (mod M): it depends only on the gap.

Corollary 3. By Theorem A, a diagonal 2B-block of orientation g has a Q1 child with orientation g∘swap at rank offset 0, and a Q3 child with orientation g at rank offset 2B^2; I checked the recursion in hilbert_array. Inside a child, every odd and even row is shifted by the same constant 2c, and every rank by a constant. So for two labels of the child, X, Y, L, d and delta are unchanged. Every odd leg Y <= 2B-1 that can occur inside the child is admitted by the B-system. The cand version has no owner condition. So the induced constraints are exactly the cand system of the child, and restricting a solution gives a solution. Induction gives every B <= 1024. gen is a subset of cand because it is the same enumeration with an extra filter. Computer check: I restricted the cand B1024 certificates to ranks [0, 512^2) and [2*512^2, 3*512^2). Against cand G_512^swap and G_512^id respectively, the result was 0 violations, for both parent orientations. (Restricting by mistake to Q4, which is off-diagonal, gave about 74000 violations. So the check is sensitive.)

Corollary 4. By Corollary A1 (unaudited), G_B^o(gen) occurs as genuine rivals at every h >= h0(B). Its part (i) needs an unsolvable G_B^o, and Theorem 1 with Corollary 3 excludes that for B <= 1024. For the induced-candidate claim: for blocks in the A1 range, the proof of A1 gives completion rows in [1, h], and Y <= 2B-1 holds automatically inside the block. So local and global candidates between two labels of the block coincide.

Lemma 6 (blocked pair). In the mod quotient, the crossing constraint e forbids kappa_Q - kappa_P ≡ c_e. If the crossing constraints between P and Q realise all M residues, then every value of kappa_Q - kappa_P is forbidden. QED.

How the certificates were computed. All scripts are in the script folder and ran one at a time, each in under 60 s.
- build_core.py is my own numba builder. It enumerates the legs from divisor pairs of Y^2 and keeps distinct triples (r, u, delta).
- The weighted M-core uses the distinct-triple degree, as in L9.
- dpll.py is a complete solver: DSATUR order, forward checking, singleton-domain (unit) propagation, chronological backtracking, and optional random restarts.
- extend.py extends a core solution by reverse peeling (Lemma 1) and asserts zero violations against the builder's list.
- verify_full.py is an independent checker and shares no code with the others. It computes the Hilbert cells by a per-rank digit recursion and asserts that the result is a unit-step path and a bijection. It finds the legs by an isqrt scan over X = 32k. It then checks the actual placed columns x_r = S(M r + xi_r): every pair at a relevant rank distance whose real column gap and real cross-pair row gap form a Pythagorean triple, with the owner test for gen, counts as a violation.

DPLL effort (decisions tried, M = 3, integer system). Every core was nearly backtrack-free.
- gen B1024 id: 18421 for the 27836-label component; the whole core took under 1 s.
- gen B1024 swap: 16423 and 10094 for the two large components.
- cand B1024 id: 29403 for 43508 labels.
- cand B1024 swap: 35150 for 50931 labels.
- B512: about 1100 per component.
The mod-3 certified system was harder in two places. The 24221-label component of gen B1024 swap needed 1188401 decisions (15 s). The 43508-label component of cand B1024 id hit a 3M-decision limit with the default order, then was solved after a random restart (14828 decisions). Every component of every system is SAT in both modes.

Shift-quotient experiment (quotient.py). Greedy union along constraints, in order of gap frequency, by rank, or at random, never letting a piece exceed two induced gaps.
- B512 id (frequency order): 663 pieces (169 with 0 gaps, 112 with 1, 382 with 2), all certified-solvable; 2606 adjacent piece pairs, of which 106 have 2 forbidden shifts and 5 have 3; quotient 3-core 615 pieces; the mod quotient is UNSAT after 3 decisions. The exact quotient (forbidding only the shift pairs that really violate) is also UNSAT after 3 decisions.
- B512 id, rank and random orders: the mod quotient is UNSAT the same way.
- B1024 id (frequency order): 10965 pieces; 15 pairs with 3 shifts forbidden; mod and exact quotients both UNSAT.
- B1024 swap (rank order): 12540 pieces; 8 fully blocked pairs; mod quotient UNSAT; the exact-quotient search did not finish within 60 s.

## External results used

- Corollary A1 and Theorem A of hilbert_p_height_independent_cores.md (unaudited): diagonal blocks are id or swap, have contiguous ranks, and embed as genuine rivals for h >= 2B^2+8B+1. Used only in Corollaries 3 and 4.
- L9 of gap_mixing_full_components.md (the M-core reduction), Theorem II.1 and Prop. I.6 of gap_mixing_round1_synthesis.md. I re-proved what I used, in Lemmas 1, 2 and 6.
- No published theorem was used.

## Checks

Reproduction against the archive: gen constraint counts 229/216 (B32 id/swap), 1726 (B64), 48419 (B256 id), 250953 (B512 id), 1205405 (B1024 id) and 1202041 (B1024 swap). Core sizes 3134/6197 (B512 id), 40136/81898 (B1024 id) and 42125 (B1024 swap), and the B1024 id component gap counts 318, 234, 81, 59, 43, all match exactly. verify_full.py independently recounted the distinct constraint triples, with the same totals as the builder: all 16 systems at B256 and B512 (M = 3, 4; id, swap; gen, cand), plus B1024 gen id 1205405, gen swap 1202041 and cand id 1344642 at M = 3. Sensitivity test: an all-zero assignment gave exactly the 119665 delta=0 triples of gen B512 id as violations, and a random assignment gave exactly the builder's 61639. Final verification of the full assignments, 0 violations each: 12 systems at M = 3; 12 systems at M = 4; and the 3 shifts of each of the 12 certified M = 3 assignments (36 runs). Each B1024 check ran in 4 parts of under 25 s. Nesting check: the restrictions of the cand B1024 certificates to the Q1 and Q3 children had 0 violations against cand G_512. Files are in scripts_gm2_core_exact/: build_core.py, core_stats.py, dpll.py, csp.py, extend.py, quotient.py, verify_full.py. The certificates are full_<o>_<v>_B<B>_M<M>[_cert].npy (int8, one value per local rank) plus the core edge lists and solutions (*_core.npy, *_int3_sol.npy, *_mod3_sol.npy). script folder size is 33 MB. The repository was only read, and I ran no git command. pysat was not used.

## Gaps

- Theorem 1 is a finite, computer-assisted statement. It rests on my builder plus an independent checker, with no human-checkable rule. No structural reason is known for why these cores are 3-solvable, or even certifiably so.
- Corollary 4 depends on Corollary A1 of hilbert_p_height_independent_cores.md, which is still unaudited. Without it, the results are statements about the finite systems G_B^o alone.
- Nothing here proves that the global P system is 3-solvable at any height. A block's labels have constraints to labels outside the block. Off-diagonal blocks, whose systems depend on h and on the offset T0, were not tested. The owner-inside constraints are included only in the cand version, which is the full induced candidate set but says nothing about how the block meets the rest of the graph.
- No obstruction to bounded M was found. A block obstruction to M = 3 at S = 32 would need B >= 2048 or off-diagonal blocks. Statement D, which is heuristic, predicts that core density grows like (log B)^2/S, so the question is open for larger B. Per the target's no-census rule, I did not build B = 2048.
- M = 4 is settled only for these blocks (B <= 1024), and only through empty 4-cores. A 4-core is expected to appear at some larger B.
- Shift quotient: Proposition 5 refutes only independently chosen piece assignments with greedy two-gap partitions. Coordinated piece choices always exist, since restricting the certified global solution gives them. But choosing them is the original problem, so no proof-free route through Theorem II.1 was found.
- Only the P family is covered. R2s, FW, 6PT, Lambda3, Lambda4, the sea and the collars are untouched. The second program I wrote is independent of the builder, but no second person has audited either.

## Missing estimate

Bounded M for P needs a structural reason for 3-solvability, or certified 3-solvability, of the M-cores. Gap counting cannot supply it, and independent two-gap pieces cannot either (Proposition 5). On the obstruction side, one would need an UNSAT core of G_B^o for some B >= 2048, or of an off-diagonal block. The data points the other way: the cores are nearly backtrack-free, and even the stronger certified system (y_u - y_r ≢ q mod 3) is solvable.

## Next steps

- Audit Corollary A1. Corollary 4 and every height-independence claim depend on it.
- Treat the certified system y_u - y_r ≢ q (mod 3) as the primary object. It depends only on gaps and is shift-invariant. Look for a rule that coordinates pieces, for example piece assignments drawn from parametrised families such as block-rule phases phi or Beatty phases c, with a quotient over (phi, kappa) rather than kappa alone.
- If a block obstruction is still wanted, one exact test at B = 2048 (gen, M = 3) is the only remaining block-level candidate. It needs a chunked build to stay under 60 s per run. It is a single fixed system, not a census.
- Test whether certified block solutions can be glued across neighbouring diagonal blocks. Use Theorem II.1 with whole blocks as pieces, using the fact that each block admits all three shifts.
- Record in the ledger: Theorem 1 (finite, two-program checked), Corollary 3 (nesting, proved), Lemma 2 (certified iff all shifts solve), and Proposition 5 (the independent-piece shift quotient fails).

