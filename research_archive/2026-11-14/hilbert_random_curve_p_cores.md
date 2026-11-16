# P cores under a random curve

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (obstruction to a method): under the branching king-step model of a random Hilbert-type curve, a weighted 3-core exists for S = 32, M = 3 with probability at least 1 - exp(-c h), with a computer-found witness. The first moment controls only the curve-dependent part of a core count. Whether cores stay bounded for K0 >= 4 depends on an energy bound (E) for Pythagorean legs, which is arithmetic and unchanged by randomization. Randomization breaks up the large self-similar cores (Hilbert G_512 has a 3134-label 3-core, random blocks at most 32 labels) but makes small cores common. Conditional on (E) and a local-limit bound for the curve, P alone would cost width O(h^2 log h). Not audited yet.

# Result

## Status

obstruction

## Summary

A random Hilbert-type curve does not give bounded P cores by a first moment. Independent orientations break locality, so the curve has to be the branching "king-step" Model K. Under Model K, a weighted 3-core exists for S = 32, M = 3 with probability at least 1 - exp(-c h) (proved, with a computer-found witness). The first moment can only control the curve-dependent part. Whether cores stay bounded for K0 >= 4 then depends on an additive-energy bound for Pythagorean legs, which is arithmetic and unchanged by randomization. Data agree: randomization breaks up the large self-similar cores (Hilbert G_512 has a 3134-label 3-core, random blocks have cores of at most 32 labels) but makes small cores common. No new width.

## Statements

SETTING. Labels e = (i,j), odd row 2i+1, even row 2j+2, T = j - i. Placement x_e = S(M r_e + xi_e). The P candidate multigraph is the archive's: in-strip, triples (r,s,delta) deduplicated, weighted degree. A quadtree order is a bijection H from ranks to the cells of the q-square in which every aligned dyadic square of side 2^a is an aligned rank interval of length 4^a.

THEOREM 1 (independent orientations break locality; proved). Model I: at every node, the child order is chosen uniformly from the 8 Hamiltonian paths of the 4-cycle of children (the dihedral images of the Hilbert U), independently at each node, and each child is generated recursively and independently. For q >= 16, the probability that locality (1), max(Di^2, Dj^2) < 16|Dr|, holds is at most 1/2. More precisely, at every node of side s >= 16, the first two children have consecutive boundary ranks whose cells differ by at least s/4 + 1 in one coordinate with probability at least 1/2. So "independent random orientation at each node" is not compatible with locality. Repairing it with column gaps costs, by the same count, about S q^2 log q extra columns, which is a log factor.

THEOREM 2 (Model K, a random curve that keeps locality; proved). Type of a block = (entry corner, exit corner), entry != exit, so 12 types. A plan for a node of type (A,B) consists of:
- an order of the 4 children that is a Hamiltonian path of K4 from child(A) to child(B);
- an entry and exit corner for each child, with the first child entered at A, the last child exited at B, entry != exit when the child side is at least 2, and each child's exit cell king-adjacent to the next child's entry cell.
Every node picks a plan uniformly from the valid plans for its type. Children are then generated independently given their types.
(a) This is a quadtree order. Consecutive cells are king-adjacent. Each block starts and ends at its entry and exit corner cells.
(b) Locality (1) holds with the constant 16.
(c) Conditional on the plans at all nodes of side > 2^a, the internal orders of the aligned 2^a-blocks are independent, and the law of each depends only on its type.
(d) The Hilbert order of the placement note lies in the support.
(e) Plan counts: 2 at side 2; 8 or 37 at side 4; 2 or 6 at every side >= 8.

THEOREM 3 (corner atoms survive in every corner-entry curve; proved). Let H be any corner-entry quadtree order with king-adjacent consecutive cells (this includes Hilbert and every Model K realization). For every r = 0 mod 4^a, the vector H(r + 4^a) - H(r) lies in {(2^a - 1)u + w : u, w in {-1,0,1}^2, u != 0, w != 0}, a set of at most 64 vectors. Each coordinate of the difference takes at most 9 values. So for these ranks, the cross-parity gap |2T_r + 1 + 2Dj| at gap 4^a takes at most 9 values. Pointwise equidistribution of partner offsets at a fixed gap therefore fails for every such random curve, on a 4^(-a) fraction of ranks. Only a 4-adically reduced form can hold. Lemma: sum over x <= W of 2^(v_4(x)) x^(-1/2) <= 4 sqrt(W), against 2 sqrt(W) for the plain sum, so the reduced form loses at most a factor of about 2 on averages.

THEOREM 4 (recurrence of local patterns; proved). Fix an offset class: aligned 2^a-blocks with j0 - i0 = c, lying in a mid-strip range where every internal constraint has its completion in the strip and its owner outside the block. Then the internal constraint system depends only on c and the internal order. Suppose that for every type tau, p(tau) = P(the internal system has a weighted k-core | type tau) >= p > 0. Then P(the global candidate graph has weighted degeneracy < k) <= (1 - p)^N, where N is the number of such blocks.

COROLLARY 5 (S = 32, M = 3; computer-assisted, one implementation). Take 8x8 blocks with j0 - i0 = 16. For every one of the 12 types, an admissible internal order gives a 4-label weighted 3-core:
- ranks r, r+5, r+6, r+11;
- two factors: a = 225 with the vector (X,Y,L) = (480,31,481), q = 15, and a = 256 with (544,33,545), q = 17;
- multigraph: a 4-cycle with two doubled edges.
Hence p >= 1/(6 * 37^4 * 2^16) > 10^(-12) rigorously; the empirical per-block frequency is 0.005 to 0.09. With N >= h/16 - 90 (h >= 4096), under Model K:
 P(weighted degeneracy <= 2) <= exp(-10^(-12)(h/16 - 90)).
So no random curve of this type allows a degeneracy certificate for M = 3. For comparison, deterministic Hilbert has degeneracy exactly 2 up to h = 16384, and its first proved 3-core needs h >= 528385.

THEOREM 6 (exploration lemma; proved, used conditionally). Suppose (H_Lambda) holds: for every finite label set R and every v in R, the sum over w not in R of ess sup P(v ~ w | ranks of R) is at most Lambda. Then for every label e0, E[number of u-vertex subtrees containing e0] <= (4 Lambda)^(u-1). If 4 Lambda < 1, then with probability 1 - O(N^(-1)) every component has fewer than 3 ln N / ln(1/(4 Lambda)) + 1 vertices.

PROPOSITION 7 (rigidity reduction; proved as a statement about the method). Fix a set U of u labels, their ranks, and the type of each constraint (role, delta, and the leg's Y). The constraints are then equations j_b - i_a = c or i_b - j_a = c, with c in a two-element set fixed by Y. They form a bipartite graph Gamma_C on {i_t} and {j_t}. The randomness of the curve enters only through the 2u - 2 relative coordinates of the cells, so it pins at most 2u - 2 equations. The other |C| - 2u + #components(Gamma_C) >= |C| - 2u + 1 equations are cycle relations "alternating sum of the c's = 0". Whether these hold is decided by arithmetic, not by the curve. A weighted K0-core has |C| >= K0 u/2, so:
- K0 <= 3 needs no relation, and Theorem 4 applies (cores are present whenever a positive-probability local pattern exists);
- K0 >= 5 needs at least (K0/2 - 2)u + 1 relations.
So any first-moment bound on K0-cores with K0 >= 5, under any random curve, needs a deterministic bound on the number of solutions of these relation systems among Y-values that carry prescribed legs (an additive-energy bound). Randomization cannot supply it.

CONDITIONAL STATEMENT (not proved). Assume (H_Lambda') (H_Lambda after grouping the at most 2 slot partners of each (q, role, side) into one exploration step) for Model K tiles with Lambda < 1/4. Assume also the energy bound (E): for every relation system on at most C log h vertices, the number of consistent Y-assignments is at most C^(#relations) times the count in the random model. Under both, the core number of each tile is bounded by an absolute K0. Then M = K0 + 1 with the C4' strides (or Theorem G grading) gives width O(h^2 log h), b = 1, for P alone. For full boards this also needs the H7 inputs (A).

NOT PROVED: bounded K0 for any S; anything at constant S with M of order log h; any width improvement.

## Proofs

1. THEOREM 1. In a uniformly random Hamiltonian path of the 4-cycle of children (8 paths: 4 starts times 2 directions), each child is the last vertex of exactly 2 paths, so the last child is uniform over the 4 children; by symmetry the first child is uniform too. Recursing with independent choices, the last cell of a block is uniform over the block's cells, and so is the first cell. Let v be a node of side s >= 16. Its first two children F and G are consecutive in a 4-cycle path, so they are squares of side s/2 that share a side. The last cell of F is uniform on F and independent of the first cell of G. With probability 1/2 it lies in the half of F farther from the shared side. In that case the two cells, at rank difference 1, differ by at least s/4 + 1 >= 5 in the coordinate perpendicular to the shared side, and (1) needs that difference squared to be below 16. Apply this at the root. Gap cost: the archive's same-parity proof needs X > 2 Dcoord^2 for every pair. A boundary at child side 2^l has a jump of at least 2^(l-1) with probability at least 1/2, and there are about 3 * 4^(L-l-1) such boundaries, so the expected forced extra width is at least c S * 4^L per level and c S q^2 log q in total. QED.

2. THEOREM 2.
(a) Induction on side. The first cell of the node is the first cell of the first child, which is entered at corner A. The child containing the parent corner A has A as its own corner of the same index, so the node starts at its A cell; the end at B is the same argument. Inside a child, consecutive cells are king-adjacent by induction. Across children, the plan requires it. At side 2 the children are cells, and any two cells of a 2x2 block are king-adjacent. Each node fills its square with 4 consecutive rank sub-intervals, so aligned squares are aligned rank intervals.
Existence of plans for every type was checked by enumeration (assertion in plans_for) at child sides 1, 2 and 4. For child side >= 3, two corner cells of different children are king-adjacent exactly when they are mirror images across the shared side, or both sit at the shared corner of diagonal children. That pattern is the same for every child side >= 3, so side 4 covers all larger sides. Counts are 2; 8 or 37; 2 or 6.
(b) Let b be the least power of 4 with b >= |r - s|, so b < 4|r - s|. The two ranks lie in one aligned b-block or in two consecutive ones. Consecutive aligned b-blocks are squares of side sqrt(b) containing king-adjacent cells (the exit of one and the entry of the next), so the squares share an edge or a corner. Each coordinate difference is then at most 2 sqrt(b) - 1, whose square is below 4b < 16|r - s|.
(c) The plans in a subtree are drawn independently given the subtree's type.
(d) Hilbert recursion (2) at a node of type (corner (0,0), corner (1,0)) visits the children in the order (0,0), (0,1), (1,1), (1,0), which is a path of K4 from child(A) to child(B). Its children's corner cells are edge-adjacent, hence king-adjacent. So every Hilbert plan is a valid plan, and the Hilbert order has positive probability. QED.

3. THEOREM 3. The rank r = 0 mod 4^a starts an aligned block beta of side 2^a, so H(r) is beta's entry corner cell. H(r + 4^a - 1) is beta's exit corner cell, so H(r + 4^a - 1) - H(r) = (2^a - 1)u with u in {-1,0,1}^2 \ {0}. H(r + 4^a) is king-adjacent to H(r + 4^a - 1). Adding a step w gives the set; each coordinate is (2^a - 1)u_c + w_c with u_c, w_c in {-1,0,1}, which is at most 9 values. For the sum, write x = 4^b x' with 4 not dividing x'. Then the sum equals the sum over b of the sum over x' <= W/4^b of x'^(-1/2), which is at most the sum over b of 2 sqrt(W/4^b) = 4 sqrt(W). QED.

4. THEOREM 4. Only the differences j - i (local differences plus c) enter Y, so with the strip and owner conditions satisfied the internal system depends only on c and the internal order. Its constraints are also members of the global candidate multigraph. Condition on all plans of nodes of side > 2^a. By Theorem 2(c), the internal orders of the N blocks are independent, and each block contains a weighted k-core with conditional probability at least p. Weighted degeneracy is monotone under subgraphs, so P(degeneracy < k) <= E[product over blocks of (1 - p(tau_I))] <= (1 - p)^N. QED.

5. COROLLARY 5. The witness search is types8.py: random Model K orders of each type of an 8x8 block at offset 16, with every pair, delta and role tested against all legs of Y <= 51. A witness was found for all 12 types after 11 to 208 samples. Each witness has ranks (r, r+5, r+6, r+11) with these constraints:
- the two pairs at gap 5 carry delta = 0 (q = 15, Y = 31) and delta = 2 (q = 17, Y = 33);
- the two pairs at gap 6 carry delta = -1 (q = 17).
Every vertex has weighted degree 3. The vectors are 480^2 + 31^2 = 481^2 and 544^2 + 33^2 = 545^2, the near-axis vectors E = S/2 = 16, O = E -+ 1 of T1.
The same pattern occurs in the global Model K census at h = 4096, S = 32 (two copies; see Checks).
Genuineness:
- the owner's two rows differ by L >= 481, while a block label's rows differ by at most 47, so the owner is outside the block;
- every Y <= 51 has L <= (51^2 + 1)/2 = 1301, so completion rows lie in [1, h] when 4 i0 + 35 - 1301 >= 2 and 4 i0 + 63 + 1301 <= 2h;
- so i0 = 0 mod 8 in [328, h/2 - 341] works, which gives N >= h/16 - 90.
Witness probability given its type: one 8x8 node (at most 6 plans), four 4x4 nodes (at most 37 plans each), sixteen 2x2 nodes (2 plans each), so at least 1/(6 * 37^4 * 2^16), about 1.36 * 10^(-12). Then 1 - p <= exp(-p). QED (computer-assisted).

6. THEOREM 6. Each subtree containing e0 corresponds to exactly one pair (rooted plane tree with u vertices, embedding with children listed in label order). There are at most 4^(u-1) plane trees. Fix a shape and list the vertices in BFS order w_1, ..., w_(u-1). The event E_t that the edge (w_p(t), w_t) is present depends on the ranks of w_p(t) and w_t, and the earlier E_s are measurable with respect to the ranks of R_(t-1) = {e0, w_1, ..., w_(t-1)}. So
 P(E_1 and ... and E_t) <= ess sup P(E_t | ranks of R_(t-1)) * P(E_1 and ... and E_(t-1)).
Sum over w_(u-1) first, for fixed earlier choices: (H_Lambda) bounds that sum by Lambda. Iterating gives Lambda^(u-1). A connected graph on at least u0 vertices has a connected subset of exactly u0 vertices. Sum over e0 and use the union bound. QED.
Remark (slot clumping, evidence, not proved): given the ranks of v and w at a slot x of a leg q with delta >= 1, the label at rank r_v + x + 1 is king-adjacent to w. It repeats the same Y with probability of order 1/3, and it then satisfies the second slot of the same q. That is the archive's path-clumping mechanism, and it survives randomization. So (H_Lambda) can hold with Lambda < 1/4 only after the slot partners of each (q, role, side) are grouped into one step. The fixed-factor lemma bounds each group by 2.

7. PROPOSITION 7. Role 0 between a (earlier) and b gives Y = |2(j_b - i_a) + 1|, so j_b - i_a is (Y-1)/2 or -(Y+1)/2. Role 1 gives i_b - j_a in a two-element set the same way. Every constraint is therefore an edge {i_a, j_b} or {i_b, j_a} of the bipartite graph Gamma_C, labelled by a constant. The system is solvable exactly when the alternating sum of the constants vanishes around every cycle of a cycle basis; the cycle space has dimension |C| - 2u + #components. Its solutions are fixed by #components free values, two of which are the common translation. Given the ranks and types, the curve law enters only through the event that the cells land on the solution set, which involves at most 2u - 2 free relative coordinates; the cycle conditions are statements about the constants alone. A weighted K0-core has |C| >= K0 u/2, which exceeds 2u - 2 by at least (K0/2 - 2)u + 2, and #components >= 1 gives the stated count. For K0 = 3 and u >= 4, |C| = 3u/2 <= 2u - 2, so no relation is needed, and Corollary 5 is an instance. QED.
Consequence: E[number of K0-cores] = sum over (U, ranks, types consistent with all relations) of P(cells in the solution set). The random curve controls the last factor. Counting consistent type assignments is the energy problem (E) and does not depend on the curve. Single-factor repetitions (all Y equal) are the trivial solutions, and the fixed-factor lemma b^- <= 4F^- caps them per vertex. Divisor-rich windows (many legs per q in a short Y-window) are where (E) could fail.

8. WHAT THIS MEANS FOR THE TARGET.
(i) Randomization removes the exact self-similar atoms (translations and transpositions of quarters; Theorems A and B of hilbert_g_for_p) but keeps 9-valued corner atoms (Theorem 3). It realizes every locally admissible pattern on about h/B independent near-diagonal blocks (Theorem 4). So fixed finite cores at fixed (S, M) appear whp, for example 3-cores at S = 32, M = 3.
(ii) The first moment works for configurations with no forced relation (|C| <= 2u - 2), given an exploration bound. Denser cores need (E).
(iii) Hubs: expected degree depends on the diagonal Y_e through short-window counts of P vectors, so hubs are whole diagonals. By Markov's inequality, the diagonals with lambda >= Lambda * mean number at most about h/Lambda. Relocating them at cost h^(2-delta) needs Lambda >= h^delta, which leaves labels with lambda up to h^delta, so the Proposition partial route does not work with only first-moment information. Graded choice counts M_e proportional to 1 + lambda_e (Theorem G of hilbert_tiling_assembly) pay for hubs on average instead.
(iv) No width follows unconditionally. Conditional width: see the Theorem field.

## External results used

- No published theorem was used. Only standard facts: the cycle space of a graph has dimension |E| - |V| + #components; the number of rooted plane trees with u vertices is the Catalan number C_(u-1) <= 4^(u-1); Markov's inequality.
- Archive inputs, used as stated: the T1 normal form (audited), the fixed-factor lemma b^- <= 4F^- (audited), Corollary A1's argument that owners lie outside the block (unaudited, re-derived for 8x8 blocks), and the Theorem G and C4' assembly (unaudited), for the conditional width only.

## Checks

All scripts are in scripts_hb3_rc_core/ (randcurve.py, bandcore.py, coredump.py, gblock.py, types8.py). Each ran with py -B in under 60 s and well under 1 GB. Neither repository was touched.

1. Model K sanity (randcurve.py loc): on 200000 random pairs, worst Dcoord^2/Dr = 5.27 < 16. The largest step between consecutive cells is 1, so every step is a king step. At q = 64, every aligned block is a square and the order is a bijection.
2. Validation against the archive: my builder with the Hilbert order reproduces (1024, 8, 3) exactly (250365 constraints, mean 1.910, degeneracy 4, 3-core 33462). The block systems give G_64, G_128, G_256 = 1726, 10130, 48419 constraints, degeneracy 2, and G_512 = 250953 constraints with a 3134-vertex 3-core, all as in hilbert_p_height_independent_cores.md.
3. Hilbert against Model K, full grid, (h, S, M) = (1024, 8, 3):
- Hilbert: 3-core 33462, 4-core 4603, degeneracy 4.
- Model K, seeds 1 and 2: 3-cores 30455 and 30680, 4-cores 2751 and 2906, degeneracy 4.
- By band (Y in dyadic ranges), the cores sit where the band mean degree is 2.3 to 4.0 (Y in [2^3, 2^8)). The bulk band Y in [2^9, 2^10) has mean 0.93 and 3-core 107 (Hilbert) or 24 (Model K). Cores follow local density, not curve self-similarity.
4. Model K at (4096, 32, 3): degeneracy 3, 3-core of 15 labels (the archive's Hilbert census gives 2). The core has three components:
- a single-factor 'ladder' of 6 consecutive ranks (factor a = 25, q = 5, Y = 231, gaps 1 and 2) closed by one label at gaps 35 to 40 (factors 1575 and 1792);
- two copies of the 4-label pattern of Corollary 5.
At (2048, 16, 3), Model K also has degeneracy 3.
5. Diagonal blocks at S = 32, M = 3 (Model K, random types):
- B = 128: 1 of 12 samples has a 3-core (7 labels).
- B = 256: 2 of 8 (10 and 7 labels).
- B = 512: 2 of 4 (4 and 32 labels).
- Hilbert: none below B = 512, then 3134 labels at B = 512.
Randomization breaks up large cores and makes small cores common.
6. types8.py found a witness 3-core for all 12 types of an 8x8 block at offset 16, after 11 to 208 samples each. All witnesses have ranks (r, r+5, r+6, r+11).
By hand I checked: the uniform-endpoint argument for Model I, the Model K induction and the locality proof, the corner-atom set, the 4-adic sum, the conditional-independence argument, the genuineness ranges in Corollary 5, the exploration lemma, and the cycle-space count in Proposition 7.

## Gaps

- The main target is not reached. No bounded-K0 core theorem is proved under any random curve, at S of order log h or otherwise, and no statement is proved at constant S with M of order log h.
- Hypothesis (H_Lambda') (an exploration bound with slot groups) is not verified for Model K. Proving it needs a conditional local-limit bound for relative cell positions in the multi-type branching structure, including the corner atoms of Theorem 3. I only showed that the ungrouped (H_Lambda) cannot hold with small Lambda, and that argument (slot clumping) is a sketch, not a proof.
- The energy bound (E) on consistent Y-assignments for cycle relations among P vectors in short windows is unproved, and I found no counterexample. Proposition 7 shows it is the arithmetic core of the problem once the curve is random.
- Corollary 5 rests on one implementation (types8.py, with gblock.vectors) that was not independently verified. The rigorous probability bound, 10^(-12), is tiny. The empirical per-block rate (0.005 to 0.09) is evidence only.
- Model K is one natural constrained randomization. I did not prove that every locality-preserving random quadtree curve needs a corner-entry or king-step structure, so Theorem 3 is stated for corner-entry curves only.
- Theorem 1's gap-insertion cost (an extra log factor) is an expected-count estimate for the archive's proof method, not a lower bound for every repair.
- The hub discussion uses Markov's inequality only. No large-deviation bound for short-window counts of P vectors is proved, so the claim that relocation fails is a statement about first-moment information.
- The conditional width O(h^2 log h) for P alone also needs the C4' or Theorem G assembly, which is unaudited, and for full boards the unaudited H7 inputs (A). Nothing here is audited.

## Missing estimate

(E), an energy bound for Pythagorean legs. Fix stride S and slack M. For a configuration of u <= C log h labels with prescribed ranks and roles, the constraint graph Gamma_C has a cycle basis of R = |C| - 2u + 1 relations of the form sum of +-c_k = 0, where c_k is (Y_k - 1)/2 or -(Y_k + 1)/2 and Y_k carries the leg S q_k with q_k = M d_k + delta_k. The estimate needed: the number of tuples (Y_k) satisfying all relations, with Y_k in windows of width w_k of order sqrt(d_k) around the configuration's diagonal, is at most C^R times the product of the window leg counts divided by the product of the relation ranges. Repeated factors (all Y equal) count as trivial solutions and are capped by the fixed-factor lemma. Add a conditional exploration bound for Model K, Lambda' < 1/4 after slot grouping, which is a local-limit statement P(H(r+x) - H(r) = z | history) <= C 4^(v_4(x))/x. Together these give whp bounded cores per tile, and so b = 1 for P alone. Without (E), randomization proves nothing beyond configurations with |C| <= 2|U| - 2.

## Next steps

- Test (E) directly. For small S and h, enumerate 4-cycles and 6-cycles of Gamma_C (Y1 - Y2 + Y3 - Y4 = 0 with Y_k carrying legs S q_k and q-sums within slot slack). Compare the counts with the random-model prediction, separating trivial single-factor solutions. A large excess at divisor-rich Y would be the arithmetic obstruction.
- Prove a local-limit lemma for Model K at one pair: P(H(r+x) - H(r) = z) <= C 4^(v_4(x))/x, using the 12-type transition matrix of plans (it is finite). Then try the conditional version that (H_Lambda') needs.
- Re-run the Model K block census with stride grading (S of order log B) to measure whether the small-core rate per block decays fast enough to give no K0-core whp for K0 = 4 at tile scale. Use gblock.py in chunks of under 60 s.
- Combine the factor-one rank-parity rule with Model K. The 4-label 3-core uses two near-axis factors (E = S/2, O = E -+ 1). A two-factor generalization of the parity rule might remove that pattern, along with M = 3 degeneracy failures generally.
- Keep the deterministic Hilbert curve for large-scale structure and randomize only small blocks (sides below a threshold). This keeps Hilbert's degeneracy 2 at small scale (no Corollary 5 patterns) while breaking the self-similar giant cores. Check whether this mixed curve beats both pure versions.
- Ask an independent reader to audit Theorems 1 to 4 and Proposition 7, and to re-run types8.py with a separate Pythagorean enumerator.

