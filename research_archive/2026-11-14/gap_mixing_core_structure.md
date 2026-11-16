# M-core components as certified colourings

15 November 2026. Problem 001. Continues continuation_gap_mixing_audit.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (partial): the shift-quotient route is exactly mod-M certified colouring of the M-core, a DP colouring with cyclic covers in which each constraint forbids one residue difference y_u - y_r = q (mod M) depending only on the gap. Splitting into pieces with at most two gaps is never the real restriction. The real cores at B = 512 and 1024 are certified-3-colourable, so they give no obstruction, but they have no local Brooks-type slack. No bounded-M structure theorem is proved. Not audited yet.

# Result

## Status

partial

## Summary

The shift-quotient route is exactly mod-M certified colouring (DP-colouring with cyclic covers) of the M-core. Splitting into pieces with at most two gaps is never the real restriction. The real cores at B = 512 and 1024 are certified-3-colourable, so these blocks give no obstruction, but the cores have no local Brooks-type slack. No bounded-M structure theorem is proved.

## Statements

Setting as in gap_mixing_round1_synthesis.md. Ranks are integers. A constraint (r, u, delta) with r < u and |delta| <= M-1 has gap q = M(u-r) + delta. An assignment y: K -> Z/M is "certified" on a constraint set E if y_u - y_r is not congruent to delta mod M for every (r, u, delta) in E. E(K) is the constraint set induced on the weighted M-core K (L9).

THEOREM R (what the shift-quotient route can do; proved).
(R1) Every assignment produced by Theorem II.1, in its greedy form or in its quotient form, is a certified assignment of E(K). The quotient form means any kappa that solves the quotient constraints kappa_Q - kappa_P != c_e.
(R2) Conversely, suppose E(K) has a certified assignment y. Then II.1 applies with the single piece K. It also applies with the M pieces P_c = y^{-1}(c). Each P_c has no internal constraint whose gap is divisible by M, and it carries the constant rule y^{P_c} = 0. Any number of gaps is allowed: this is the k0 = 0 clause of audited Theorem 1, and it is certified. The quotient is solved by kappa_{P_c} = c.
(R3) Hence the following are equivalent:
 (a) some decomposition of K into pieces with mod-M certified assignments has a solvable shift quotient (the target's structure theorem, in any form);
 (b) E(K) is certified-M-colourable.
The restriction "at most two gaps per piece" (or "s gaps with M >= 2s") is never the binding one, because pieces with no internal M-divisible gap work for any number of gaps. The greedy count ("at most M-1 distinct (Q, c_e) per piece") is only a sufficient criterion for (b).
(R4) Monotonicity. If some subsystem of E(K) has no certified assignment, then no decomposition of type (a) exists, at any piece granularity. Every obstruction to the route is a certified-UNSAT subsystem, and nothing else is.

LEMMA CC (certified core; proved). Peel from K, repeatedly, every label with fewer than M distinct classes (w, rho). Here w is a neighbour and rho in Z/M is the forbidden value of y_w - y_v. Call the result K_c. Then K_c is contained in K. Every certified assignment of E(K_c) extends to a certified assignment of E(K), and from there by L9 to a global integer solution. So the route at M works iff E(K_c) is certified-M-colourable.

LEMMA G (gains; proved). The certified problem is DP-colouring (correspondence colouring) with M colours. Each constraint is the cyclic matching y_u = y_r + delta, and its gain is delta, which is congruent to q mod M. Around every closed walk, the signed sum of the deltas is congruent mod M to the signed sum of the gaps. A component is balanced iff some potential phi gives q_e congruent to phi(u) - phi(r) on every edge. On a balanced component, switching by phi turns the certified problem into proper M-colouring of the underlying simple graph. Theorem II.1 is "switch each piece by y^P, then DP-colour the contracted gain graph".

LEMMA C' (3-adic gain support; proved from audited inputs). Suppose 3 does not divide S and 3 divides M. Every constraint whose cross pair has 3 not dividing Y has gain congruent to 0 mod 3. Through L1 (c + DU = eta Y), at M = 3 in the full grid every constraint with nonzero gain has an edge diagonal U congruent to 1 mod 3. On the near-isosceles backbone of T4 at S = 32, M = 3, the gain of v_{n,sg} is n(n + sg) mod 3. That is 2 when (n mod 3, sg) is (1, +1) or (2, -1), and 0 otherwise.

PROPOSITION P3 (residue-split profile; proved, conditional on a design change). If 3 does not divide S, 3 divides D and 3 does not divide c, then at M = 3 every P candidate constraint has delta = 0. The P system is then exactly proper 3-colouring of a simple graph whose edges join ranks at distance q/3, and certified equals integer. Caveat: the normalized designs S = 8 D^2 sigma force 9 | S when 3 | D, so this hypothesis is incompatible with them as written.

PROPOSITION GP (Gallai peeling is valid; proved using a published theorem). Take a connected set C of labels that each have exactly M certified classes in the current graph. If some block of C is not K_n^k or C_n^k, then C can be removed and coloured last, for every assignment of the rest.

EXACT FINITE CERTIFICATES (computation; S = 32, M = 3, the block systems G_B^o of Corollary A1).
 - The certified core equals the integer core in every case: 3134/6197 (B = 512 id), 2295/4461 (512 swap), 40136/81898 (1024 id), 42125/84944 (1024 swap). No label pair in any of these cores carries two constraints.
 - All four cores are certified-3-SAT, and every model was verified.
 - Gallai peeling (Proposition GP) removes 0 labels at B = 512 (both orientations) and 411 of 40136 at B = 1024 id.
 - Conditional on the unaudited Corollary A1: none of these fixed systems obstructs the route at any height.

WHAT BOUNDED M THE ARGUMENT GIVES: none, for all h. No argument proved here or in the archive bounds the certified colouring threshold of K uniformly in h.

## Proofs

1. PROOF OF R1. Let xi_r = (y^P_r + kappa_P) mod M for r in piece P.
 - Internal constraint (r, u, delta) with both ends in P: xi_u - xi_r is congruent to y^P_u - y^P_r, which by hypothesis is not congruent to delta.
 - Crossing constraint e = (r in P, u in Q, delta): xi_u - xi_r is congruent to (y^Q_u + kappa_Q) - (y^P_r + kappa_P). This is congruent to delta exactly when kappa_Q - kappa_P is congruent to delta + y^P_r - y^Q_u = c_e. That is the definition of c_e in II.1.
 - The greedy form chooses kappa avoiding every forbidden class. The quotient form solves kappa_Q - kappa_P != c_e on the quotient core and extends by peeling.
In both forms, every constraint of E(K) satisfies xi_u - xi_r not congruent to delta mod M, so the output is certified. QED.

2. PROOF OF R2. One piece: there are no crossing constraints, and y itself is the piece assignment. M pieces: let P_c = {v : y_v = c}.
 - An internal constraint of P_c has y_u - y_r = 0. Certification gives that delta is not congruent to 0. Since delta is congruent to q mod M (q = M(u-r) + delta), the internal gaps of P_c are all non-divisible by M. The constant rule 0 is certified on P_c, because the difference 0 is not congruent to delta. This is audited Theorem 1, clause k0 = 0, read mod M, with no limit on the number of gaps.
 - For a crossing constraint, c_e = 0 - 0 + delta = delta. Put kappa_{P_c} = c. Then kappa_Q - kappa_P = y_u - y_r, which is not congruent to delta. So the quotient is solved. QED.

3. PROOF OF R3 AND R4. R3 is R1 together with R2. For R4, a certified assignment of E(K) restricts to a certified assignment of every subsystem, and R1 says the route always produces one.

4. PROOF OF LEMMA CC.
 - A class (w, rho) at v is determined by a triple (w, delta) through rho = delta or -delta mod M. So the number of classes is at most the number of triples, and certified peeling removes at least what integer peeling removes. A core of a subgraph lies in the core of the graph, so K_c is contained in K.
 - Extension: assign K_c first, then the peeled labels in reverse deletion order. When v is assigned, each class (w, rho) with w already assigned forbids the single residue y_w - rho. Fewer than M classes leave a free residue, so the extension stays certified on E(K).
 - L9 then extends to all labels with integer constraints, because certified implies integer-satisfied. QED.

5. PROOF OF LEMMA G.
 - delta = q - M(u-r), so delta is congruent to q mod M.
 - On a closed walk, the signed rank differences sum to 0, so the signed sum of q = M d + delta is congruent to the signed sum of delta.
 - Switching: put z = y - phi. Then z_u - z_r is not congruent to delta - (phi(u) - phi(r)). With delta congruent to q_e congruent to phi(u) - phi(r), every edge forbids z_u = z_r.
 - The DP form: the edge (r, u, delta) is the perfect matching (r, c) to (u, c + delta) on Z/M. Restricting it to sublists leaves a matching, which is a cover in the sense of Bernshteyn, Kostochka and Pron (Definition 6). QED.

6. PROOF OF LEMMA C'.
 - Squares mod 3 lie in {0, 1}. If 3 divides neither X nor Y, then X^2 + Y^2 is congruent to 2 mod 3, which is not a square. So 3 divides X = Sq. Since 3 does not divide S, 3 divides q, and since 3 divides M, 3 divides delta. (This is Lemma C of hilbert_p_height_independent_cores.md, re-derived.)
 - In the full grid, Y = |2U + 1|, and 3 divides 2U + 1 iff U is congruent to 1 mod 3.
 - Near-isosceles: q = n(Sn/2 + sg) = n(16n + sg) at S = 32, and 16 is congruent to 1 mod 3. The four nonzero cases of n(n + sg) mod 3 are:
   - n = 1 mod 3, sg = +1: 1 * 2 = 2.
   - n = 1 mod 3, sg = -1: 1 * 0 = 0.
   - n = 2 mod 3, sg = +1: 2 * 0 = 0.
   - n = 2 mod 3, sg = -1: 2 * 1 = 2.
   - n = 0 mod 3 gives 0.
 - Consistency: 3 divides Y = 32n + sg iff 2n + sg is congruent to 0 mod 3, which is exactly the two residue-2 cases. QED.

7. PROOF OF PROPOSITION P3. Y = |c + DU| is congruent to |c| mod 3, which is nonzero. Apply Lemma C'. Then 3 divides delta and |delta| <= 2, so delta = 0. Every constraint forbids xi_u = xi_r, and since |delta| < M, its rank difference is q/3. QED. On the caveat: S = 8 D^2 sigma with 3 | D gives 9 | S.

8. PROOF OF PROPOSITION GP. Let R be the labels that remain after C is removed; they are coloured first. For v in C, the current certified degree is deg_C(v) + deg_R(v) = M, with parallel classes counted with multiplicity. The residual list has size at least M - deg_R(v) = deg_C(v). Each constraint inside C restricts to a matching between the residual lists, so this is a cover of the multigraph C with |L(v)| >= deg_C(v).

External theorem (Bernshteyn, Kostochka and Pron, "On DP-coloring of graphs and multigraphs", Siberian Math. J. 2017, arXiv:1609.00763, Theorem 9). I read its statement in the arXiv HTML version. In my words:
 - Hypotheses: G is a connected multigraph. A cover assigns disjoint colour sets L(v), and for each pair of vertices the edges between L(u) and L(v) form a union of e_G(u, v) matchings, which need not be perfect.
 - Definition: G is DP-degree-colourable if it is colourable from every cover with |L(v)| >= deg(v).
 - Conclusion: G fails to be DP-degree-colourable iff every block of G is K_n^k or C_n^k (complete graph or cycle, each edge of multiplicity k).
So if some block of C is not of that form, C is colourable from its residual lists whatever R received.

Remark (proved, the same argument). In a minimal non-certified-colourable subsystem, the components of labels with degree exactly M must be GDP-trees. Otherwise Proposition GP would remove them, which contradicts minimality. Zero Gallai reduction therefore means the core has the local structure of a DP-critical graph.

9. COMPUTATIONS (sanity checks and exact finite certificates; no census). I wrote an independent builder from the stated definitions: the recursion-(2) Hilbert array, all legs with S | X and odd Y <= 2B - 1, both slots and both roles, and the owner outside the block.
 - Its constraint counts equal the archive's: 1726 (B = 64), 48419 (256), 250953 (512 id), 250053 (512 swap), 1205405 (1024 id) and 1202041 (1024 swap). Its integer 3-cores equal the archive's: 3134/6197 at B = 512 and 40136 labels at B = 1024 id. The B = 256 3-core is empty, as archived.
 - SAT encoding: one-hot variables. For the certified problem, a clause forbids (y_r = c, y_u = c + delta mod M). For the integer problem, the clause applies only when 0 <= c + delta < M. The solver is CaDiCaL 1.5.3 through pysat. Every returned model was checked against every core constraint by assertion. No UNSAT result is claimed anywhere.
 - Pre-registered predictions: the certified core is a proper subset of the integer core (wrong; they are equal) and certified SAT at B = 512 (right). For Gallai peeling: a partial reduction (wrong; there was none at B = 512, and only 1% at B = 1024).
 - Structure of the B = 512 id core:
   - No label pair carries two constraints, and 55 triples have two witnesses.
   - Weighted degrees run from 3 to 10, with mean 3.95.
   - Distinct gaps per label are 1 to 7 (mode 3), and they equal the distinct factors per label almost exactly. This agrees with the uniqueness lemma.
   - 81 distinct (q, Y) vectors occur. 3100 of 6252 witnessed edges come from near-isosceles vectors (L = X + 1). The dominant vector is n = 17, sg = -1: (q, Y, a) = (4607, 543, 271^2), with 1130 edges.
   - The core lies in T in [-364, -177].
   - Lemma C' has 0 violations.
   - The delta = 0 subgraph has 380 components; 2 are non-bipartite, and the largest has 607 labels.

## External results used

- Bernshteyn, Kostochka and Pron, 'On DP-coloring of graphs and multigraphs', Siberian Math. J. 58 (2017); arXiv:1609.00763, Theorem 9, statement read from the arXiv HTML version. Hypotheses in my words: G is a connected multigraph. A cover gives disjoint colour sets L(v), and between L(u) and L(v) the edges form a union of e_G(u, v) matchings, which need not be perfect. G is DP-degree-colourable if it is colourable from every cover with |L(v)| >= deg(v). Conclusion: G is not DP-degree-colourable iff every block of G is K_n^k or C_n^k. Used only in Proposition GP and its remark.
- CaDiCaL 1.5.3 through pysat, used only to find certified and integer assignments of finite cores. Every model was verified independently, and no UNSAT result is used.
- Internal, audited: Theorem 1 and Section 5 of continuation_gap_mixing_audit.md; T1 of hilbert_p_family_counts.md; the uniqueness lemma of continuation_hilbert_factor_one_choices.md. Internal, unaudited: Theorem II.1 and L9 (gap_mixing_round1_synthesis.md, gap_mixing_full_components.md), L1 and T4 of gap_mixing_full_components.md, and Corollary A1 and Lemma C of hilbert_p_height_independent_cores.md. I re-derived Lemma C.

## Checks

Proved by hand: Theorem R (R1 to R4), Lemma CC, Lemma G (including the DP-cover form), Lemma C' with the near-isosceles gain table, Proposition P3 and Proposition GP from BKP Theorem 9.

Scripts are in scripts_gm2_core_theory/. The folder is 24 KB. Each script ran with py -B, one at a time, in 0.8 s to 39.5 s and well under 1 GB.
 - cert_core.py builds G_B^o independently and computes the integer and certified M-cores. It runs integer and certified SAT on them and verifies every model by assertion. Its constraint counts equal the archive's at B = 64, 256, 512 (id and swap) and 1024 (id and swap), and so do its core sizes. Results: certified core = integer core in all four cases, and all are certified-SAT.
 - core_structure.py computes factors, vectors, multiplicities, degrees and the delta = 0 subgraph, and checks Lemma C' (0 violations).
 - gallai_peel.py runs Gallai peeling under Proposition GP. It removed 0 labels at B = 512 (id and swap) and 411 of 40136 at B = 1024 id.

The repository was only read. No git command was run, and nothing was written to either repository.

## Gaps

- No structure theorem for the M-core of the actual Hilbert P graph is proved, at any bounded M. The route's target is therefore not reached. By Theorem R the target is equivalent to certified M-colourability of K (equivalently of K_c), uniformly in h, and I have no argument for that. The archive's gap-count lemmas (T3, H1, H2) do not bear on it, because R2 makes the gap count per piece irrelevant.
- No obstruction is proved either. The four G_B^o cores at B = 512 and 1024 are certified-3-SAT, so these blocks cannot supply one. Larger blocks (B >= 2048), off-diagonal blocks and H7 blocks were not examined, by the no-census rule.
- SAT of a G_B^o core certifies nothing about the full candidate graph at large h. G_B^o omits owner-in-block constraints, and the full graph contains much more than these blocks. The block statements also depend on Corollary A1 of hilbert_p_height_independent_cores.md, which is still unaudited.
- The greedy (degeneracy) form of II.1 was not tested on any natural decomposition. R2 shows that the solvable-quotient form exists whenever certified SAT holds, but the greedy class condition can fail for that decomposition, and no natural piece choice is known to satisfy it.
- Proposition GP relies on Theorem 9 of Bernshteyn, Kostochka and Pron, read from the arXiv HTML statement (the PDF was not readable in this session). Its hypotheses match the residual covers here; I did not re-prove it.
- Proposition P3 needs 3 | D with 3 not dividing S. That is incompatible with the normalized designs S = 8 D^2 sigma, so it is a statement about a different design, whose same-parity exclusion would need a new argument.
- Nothing here is audited. Theorem R, Lemmas CC, G and C' and Propositions P3 and GP are short and should go to an independent reader. The near-isosceles gain formula and the core statistics are from one implementation, cross-checked only against the archive's counts.
- R2s multiplicity on one label pair is not addressed. The only related observation is that no pair in these P cores carries two constraints, which is data, not a theorem.

## Missing estimate

The single missing statement is: for some fixed M, the weighted M-core K of the Hilbert P candidate graph is DP-M-colourable for the cyclic cover with gains q mod M, uniformly in h. Theorem R shows that every piece decomposition is only a way of proving this. Lemma CC lets you replace K by the certified core K_c. Two facts make any proof global:
 - the low-degree labels of the real cores induce GDP-forests, so there is no Brooks-type local slack;
 - the mean degree is about 3.95, above every sparse-graph colouring threshold I know.
For M = 3, a uniform answer needs either a global certified rule (a switching phi under which most gains become 0, plus a 3-colouring of the delta = 0 graph) or a certified-UNSAT subsystem that recurs at large h.

## Next steps

- Send Theorem R, Lemma CC, Lemma G, Lemma C' and Proposition GP to an independent audit. They take a few lines each. Record in the ledger that the shift-quotient route is equivalent to certified M-colourability of the core, and that 'at most two gaps per piece' is not a real restriction.
- Retarget the structural work from gap counts to gains. By Lemma C', at M = 3 the nonzero-gain edges sit only on diagonals with 3 | Y (U = 1 mod 3 in the full grid). Test whether a switching phi built from L1 (for example, phi depending on the edge diagonal and the near-isosceles index n) balances most of the core. If it does, the core reduces to 3-colouring the delta = 0 graph plus few residual gains.
- Run one exact certificate on G_2048^id at M = 3: certified core, then certified SAT, split into runs under 60 s. A certified-UNSAT core would kill the route at all h >= h0(2048), conditional on Corollary A1. A SAT result extends the evidence that the route has room.
- Audit Corollary A1 of hilbert_p_height_independent_cores.md. Every block-based statement here and in gap_mixing_full_components.md depends on it.
- Look for a published DP-colouring theorem for sparse multigraphs with three colours (a DP analogue of the Kostochka-Yancey bound). Then compare its density threshold with the maximum average degree of the real cores, which is at least 3.95. This would show whether any sparsity theorem could ever apply.
- Evaluate the residue-split design of Proposition P3 (3 | D, 3 not dividing S): check whether a same-parity exclusion survives without S = 8 D^2 sigma. Under that design, P at M = 3 is plain graph 3-colouring, and the full Gallai/Brooks toolkit applies directly.

