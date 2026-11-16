# An adversarial check of the Hilbert route

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: the uniqueness lemma and the factor-one two-choice theorem are correct. A new fatal family of right angles on two labels and one filler shows that three choices can never complete the period-seven board of the continuation report as specified. No obstruction to bounded S and M in general was found. The mod-4 row alignment of design H7 (hilbert_sea_design_h7.md) removes this family. Not audited yet.

# Result

## Status

partial

## Summary

Both audited lemmas are correct. I found a new fatal two-label/one-filler right-angle family, which proves that 3 choices can never complete a period-seven Hilbert board. No obstruction to bounded S and M in general.

## Statements

(A) Checks of the two claims.
(A1) The uniqueness lemma (Section 7 of continuation_hilbert_factor_one_choices.md) is correct. Fix a focal label, a factor a, a role and a side. Then at most one candidate slot gap q exists, over the full candidate multigraph and for any S >= 8. The profile version needs S >= 4d.
(A2) The factor-one two-choice theorem is correct. Every factor-one candidate at a label has the same gap q and the same sign. The rule xi = 0 on odd-q components, and xi = floor(r/d0) mod 2 on even-q components, removes every factor-one pair.

(B) Family F1: two labels and one sea point.
Let V and Q be label points of opposite parity from distinct labels. Write X = x_Q - x_V (nonzero), Y = y_Q - y_V (odd) and s for a sea row. Put E = (x_V + u, s) and W = Q + E - V = (x_Q + u, s + Y), where u = -Y(s - y_V)/X.
Suppose four things hold: u is an integer; E is black (u is nonzero mod 7 with sea row s at that residue, or u = 0 mod 7, s = F and the hole holds F); W's row is in [1, h]; and, if u = 0 mod 7, W's hole also holds F. Then V, Q, E are three black corners of a tilted rectangle whose fourth corner W violates (V2) or (V1), so the board is invalid.
Necessary conditions:
- 2^(v2(S) + v2(q)) divides s - y_V, so the vertex has the parity of s.
- If u is a unit mod 7, then v7(Y(s - y_V)) = v7(S) + v7(q).
- If s = F, then v7(Y(F - y_V)) >= v7(S) + 1 + v7(q).

(C) Obstruction for M <= 3. Fix S with v7(S) >= 2, for example S = 1568, and M <= 3. Take any block whose labels have a = b (mod 7). Such blocks hold 1/7 of all labels, and the profile recipe gives them endpoint class (0,0). If the block contains labels of both signs of T = b - a, then for every h >= h0 every assignment of private choices contains an F1 configuration. It uses only binary sea columns, so it does not depend on the F/H choices at holes.
(C') If holes keep the filler F, which is the core construction in Section 7 of the profile note, then with S = 1568:
- every a = b (mod 7) block fails for M <= 3, with or without an orientation split and for any L;
- an orientation-blind block fails for every M <= 16.
More generally, with the lower point as vertex, the construction kills every M with 2M - 1 < max(p^(v_p(S)) for p != 7, 7^(v7(S)-1)).
(C'') In a block with a != b (mod 7) of type (lower endpoint = L mod 7, L of the same parity as that endpoint), M <= 3 also fails, again using binary columns only.

(D) A design rule. In a block with a != b (mod 7), choose the profile so that the endpoint = L (mod 7) has the parity opposite to L. Both parities are available, since L ranges over {1, ..., 14}. Then the block has no F1 configuration at all, for every S that is even and divisible by 7, every M, every placement with columns = 0 mod 7, and every hole choice.

Scope. (C) shows that the period-seven route needs M >= 4, and M >= 17 for the natural S = 1568 core with filled holes and no orientation split. It does not show that bounded S and M are impossible. The 3-choice P certificates at h = 2048 and 4096 cannot extend to complete boards of this route.

## Proofs

1. The uniqueness lemma (A1), rederived.
Candidates q1 > q2 have the same focal label, role and side. Put Delta = q1 - q2 and q_k = M d_k + delta_k with |delta_k| <= M - 1.
- Then |M(d1 - d2) - Delta| <= 2M - 2, which gives |d1 - d2| <= Delta/M + 2 - 2/M.
- That bound is below Delta + 1 because M - 2 < Delta(M - 1).
- The same side makes the partners' rank distance exactly |d1 - d2|. The same role makes z1 - z2 one Hilbert coordinate difference. So |z1 - z2| <= 4 sqrt(Delta), and z1 = z2 when d1 = d2.
- With A = S^2/(8a), the candidate equation is T = eps A q^2 - (eps a + 1)/2 - z.
- The smaller-factor condition a^2 < ab = S^2q^2/4 gives S q2 > 2a, hence A(q1 + q2) > S(q1 + q2)/(4 q2) > S/2 >= 4.
- Equal signs give |z1 - z2| = A(q1 + q2) Delta > 4 Delta, a contradiction.
- Opposite signs give A(q1^2 + q2^2) - a = +-(z1 - z2). Since 2A q2^2 - a = |y2| + a > a, the left side exceeds A(q1^2 - q2^2) > 4 Delta, again a contradiction.
For earlier neighbours: one gap per role, at most two ranks per gap, one forbidden choice per rank. That gives at most 4 per factor, so M = 4R + 1 suffices. In the profile version the error is d * 4 sqrt(Delta) and the quadratic difference exceeds S Delta, so S >= 4d suffices. Every step checks.

2. The factor-one theorem (A2), rederived.
- For a factor-one pair, y = eps(S^2q^2/4 - 1) and 2T + 2z + 1 = y, which gives T = eps A q^2 - (eps + 1)/2 - z with A = S^2/8 >= 8.
- Equal signs with q1 != q2 force A|q1^2 - q2^2| < 4(sqrt q1 + sqrt q2) <= 4|q1^2 - q2^2|, which is impossible.
- Opposite signs force A(q1^2 + q2^2) <= 1 + 4(sqrt q1 + sqrt q2) <= 4.5(q1^2 + q2^2), which is impossible. This includes q1 = q2.
- So each label has one gap and one sign, and each component has one gap.
- If M does not divide q, all-zero choices give slot gaps in M Z, which avoid q.
- If q = M d0, a candidate edge forces xi_f = xi_e and rank gap d0. Ranks d0 apart get opposite parities of floor(r/d0), so the actual gap is q +- 1.
- That new gap is not a factor-one pair for the same edge, by uniqueness at the label. Any final factor-one pair is a candidate edge, so it is removed.
The argument is correct, including for subsets and padded ranks.
Sanity check: check_uniqueness.py builds the complete candidate multigraph, with all choices and all factors. Cases: (Q,S,M,h) = (32,8,3,64), (32,8,5,64), (64,8,3,128), giving 1196, 1036 and 7290 constraints. It found no (label, factor, role, side) with two gaps and no label with two factor-one gaps. The recursion and locality (1) were also checked exhaustively through q = 16.

3. Family F1 (B).
- E - V = (u, s - y_V) is perpendicular to Q - V = (X, Y) exactly when Xu + Y(s - y_V) = 0.
- All four legs are nonzero (u != 0 because Y(s - y_V) != 0), so the rectangle V, Q, W, E is tilted.
- x_Q = 0 mod 7, so W's column has the residue of E's column, namely u mod 7.
- Case u a unit mod 7. Both columns are binary, with singleton row s(u) = s. W is white, since its row s + Y != s, and its only black point has parity s, which differs from parity(s + Y) because Y is odd. That violates (V2). The axis owner of the parity edge {s + Y, s} exists in another column, because every parity edge is a double. So the tilted rectangle and that axis rectangle both present {W}.
- Case u = 0 mod 7. E is black only if its column is a hole holding F, so s = F. W's column is either a hole (row F, parity different from F + Y, a violation) or a label column. A label column holds both parities, which violates (V2), or makes W black, which violates (V1).
- Necessary conditions. Y is odd and v2(X) >= v2(S) + v2(q), which gives the 2-adic condition. The 7-adic conditions are v7(u) = 0, or v7(u) >= 1 for an F point.

4. Theorem (C), class (0,0) (a = b = L mod 7).
Take L odd; the case L even is the mirror image (step 6).
- Fix a column i* whose odd row alpha = a0 + 14 i* satisfies alpha = L mod 2^(v2(S)+2) * 3 * 5 * (S without its 2- and 7-parts), and v7(alpha - L) = v7(S) - 1.
- Take a vertical curve adjacency {(i*, j), (i*, j+1)}, so the rank distance is 1 and the slot gap is q in [1, 2M - 1] = [1, 5]. Its even rows b and b + 14 give Y2 = b - alpha and Y1 = b + 14 - alpha. Require v7(Y2) = 1 and t = Y2/7 = 2 or 3 (mod 7), so that t + 2 = 4 or 5 has the same chi. This condition puts j in two classes mod 7.
- Let e be the label of smaller slot and X = x_f - x_e > 0. Both cross pairs share the vertex row alpha, and both use s = L, which has alpha's parity.
- Option 1: vertex (x_e, alpha) with leg to f's even point. Here u1 = Y1(alpha - L)/X, which must have chi(u1) = -1.
- Option 4: vertex (x_f, alpha) with leg to e's even point. Here u4 = -Y2(alpha - L)/X, which must have chi(u4) = -1.
- Divisibility: S q | Y(alpha - L), because alpha - L carries 2^(v2(S)+v2(q)), the odd non-7 part of lcm(1..5) and 7^(v7(S)-1), while Y supplies one more 7.
- u1 and u4 are 7-units, because v7(Y) + v7(alpha - L) = v7(S) and 7 does not divide q.
- u1/(-u4) = Y1/Y2 is a quadratic residue mod 7. So chi(u4) = -chi(u1): exactly one option has chi = -1, and that option fires by (B). E and W lie in binary columns, so hole choices are irrelevant.
- W's rows are L + Y_k, inside the strip. |u| <= h^2/S, which stays inside the profile's unchanged 2W = 2h^2 extension.
- So every value of xi_f - xi_e, and hence every assignment, is fatal.

5. Existence of the adjacency in step 4.
- The recursion makes every aligned 2^k-square of H_Q an image of H_{2^k} under id, transpose, anti-transpose or a half turn, with consecutive ranks.
- check_binary_angle.py verified the following for H_64. In every column, the lower endpoints of vertical curve adjacencies cover all 7 residues. In every row, the left endpoints of horizontal adjacencies cover all 7 residues. (The sizes 8 and 16 fail; 64, 128 and 256 pass.)
- Coverage survives the symmetries, because they map j to j or to c - 1 - j, and survives offsets.
- So each column i* has, in every 64-band, an adjacency with j in any prescribed class mod 7.
- The O(sqrt h) exceptional rows E_h and the range [5000, h - 5000] remove only o(h) of the roughly h/900 candidate bands and of the O(h) admissible alpha. So h0 exists.
- Exact check (check_binary_angle.py, instance.py), with S = 1568 and M = 1, 2, 3: every q and both rank orders fire exactly one option. Example: alpha = 13441, b in {13504, 13518}, L = 1, F = 1005. At q = 1 the corners are V = (1568, 13441), Q = (0, 13504), E = (1028, 1), W = (-540, 64). Row 64 is even, and W's column black point is in row L = 1.

6. The mirror case, (C'') and (C').
- Mirror for L even: use a fixed even row beta, horizontal adjacencies (the row property of H_64), the T < 0 region and vertex beta.
- (C''): in a block of type (lower endpoint 0, upper endpoint 5) with L of alpha's parity, Y1 and Y2 are 7-units with Y1 = Y2 (mod 7). Then v7(alpha - L) = v7(S) makes options 1 and 4 complementary for any vertical adjacency. Checked exactly: check_type05.py, M <= 3.
- (C'), filled holes. Put Y = T_{c0} for a cell c0 and its curve neighbour.
  - In a horizontal step the pair is (a_{c0}, b_{c0}); in a vertical step it is (a_f = a_{c0}, b_{c0}). Either way the vertical gap is T_{c0}.
  - Use s = F at the vertex with F's parity. F - y is a 7-unit for a = b blocks, so take v7(Y) = v7(S) + 1 + A7, where A7 = max v7(q).
  - Then u_q = -Y(F - y_V)/X has v7 >= 1, so E is in a hole.
  - Non-slot condition: S does not divide u_q. This holds if v7(u_q) < v7(S), which is automatic when 2M - 1 < 7^(v7(S)-1). It also holds if v2(u_q) < v2(S), by taking v2(F - y_V) = v2(S) + A2, valid when 2M - 1 < 2^v2(S).
  - W lies in a hole or label column, so it is fatal.
  - Upper vertex (needed after an orientation split): W's row is F - Y, so Y < F is required. Y = 7^3 = 343 < 1000 <= F works when A7 = 0, that is M <= 3.
  - check_filler_angle.py confirms every q for S = 1568: lower vertex M <= 16, upper vertex M <= 3. For S = 2940 and 2520 the thresholds are 3 and 4, and for S = 1792 they reach 24 and at least 39, all as predicted.

7. The design rule (D).
- With a != b (mod 7), Y is a 7-unit.
- F1 needs 7 | Y(s - y_V), so 7 | s - y_V.
- F - y and H - y are units for both label classes, because F = 3g, H = g and the labels are 0 or 5g (mod 7). So s = L and the vertex is the class-0 endpoint.
- The rule gives that endpoint the parity opposite to L, which contradicts the 2-adic condition of (B).
- This holds for binary columns and for holes set to F or H.

8. Families checked and not forced by choices.
- Same-parity F1: W is in the same residue column with the same parity, so it is parked unless it lands on an occupied slot. It can be fatal only through (V3).
- Sea-vertex right angles: X must lie in {d + P/d : d | P}, with P = (y_V - s)(y_Q - s). That is a divisor condition, never a whole window.
- Label-only right angles: one exact equation (X^2 = product, or q1 q2 = N). These exist at fixed S for h of order S^4 (the recursive collision), but each pair forbids a bounded number of gaps.
- P single-pair forcing: this needs 2M - 1 consecutive q with (Sq)^2 + Y_k^2 square for Y_k in {Y1, Y2}. I found no mechanism, and a heuristic count tends to zero.

## External results used

- No published theorem was used, and no web source was consulted.
- Repository notes used as hypotheses (read, not re-audited): criterion (V1) to (V5) and the axis owner lemma (research_archive/2026-11-13/block_sea_classification.md, lower_bound_windows.md); the filled period-seven profile (3), with conditions (1), (2) and (9), the hole choices of Section 6 and the core rule of Section 7 that unused holes keep F (research_archive/2026-11-09/full_problem_push/filled_mod7_profile_cover.md); and the Hilbert recursion (2) and locality (1) (2026-11-14/continuation_hilbert_placement.md).

## Checks

All scripts are in scripts_hb1_skeptic/. Each ran under 60 s and used the standard library only.

- check_uniqueness.py: implements recursion (2) and checks locality (1) exhaustively through q = 16. It builds the complete candidate multigraph of opposite-parity Pythagorean pairs over all local choices. Result: 0 violations of 'one gap per (label, factor, role, side)' and 0 labels with two factor-one gaps, at (Q,S,M,h) = (32,8,3,64), (32,8,5,64), (64,8,3,128), on 1196, 1036 and 7290 constraints.
- check_filler_angle.py: exact big-integer check of the F-option family at h = 10^40 with the sea rule. Every slot gap q in [1, 2M-1] and both signs give a fatal support for these thresholds:
  - S = 1568: M <= 16 (lower vertex), M <= 3 (upper vertex);
  - S = 2940: M <= 3 in both modes;
  - S = 2520: M <= 4 in both modes;
  - S = 1792: M <= 39 (lower; the loop limit) and M <= 24 (upper);
  - S = 1575: M <= 9 and M = 12 (M = 10, 11 fail only because the script does not enforce exact 3- and 5-adic valuations).
  These thresholds agree with the formula derived.
- check_binary_angle.py: line property of H_{2^k}. The minimum number of residues mod 7 per column and row is (3,2), (4,4), (6,5), (7,7), (7,7), (7,7) for k = 3 to 8. It also confirms the hole-independent class (0,0) obstruction for S = 1568 and M = 1, 2, 3.
- check_type05.py: confirms the class (0,5) alive-orientation obstruction for M = 1, 2, 3 over 59 even rows b_e and both step directions.
- instance.py: prints the explicit corners for alpha = 13441, b in {13504, 13518}. Exactly one option fires for each q.

The analytic proofs do not depend on these computations, apart from the H_64 line property used for existence.

## Gaps

- No obstruction for M >= 4 that is independent of hole choices. For M >= 17 at S = 1568 (or for orientation-split blocks with F < 2401 and M >= 4), the F-option construction can land E on a slot column. Then E is black unless a third label chooses that slot, so the instance becomes a three-label constraint. I did not analyse it.
- Hole toggling, the free choice of F or H at each hole (filled_mod7 Section 6), defeats the F-option version (C'). An E hole set to H makes E white, and a W hole set to H parks W. Whether toggling creates new two-label H-hole events was not analysed. The hole-independent version (C) is proved only for class (0,0) blocks without an orientation split, and for alive (0,5) blocks.
- Class (5,5) blocks with a = b (mod 7) under hole toggling: a hole-independent forcing needs a same-column pair with |Delta j| = 7 at a rank distance whose window avoids multiples of 7, with j prescribed mod 49. Its Hilbert existence was not established.
- The claim that a column clique gives an obstruction for M <= 6 in alive (0,5) blocks is only sketched: all slots must agree mod 7 inside the clique. I did not verify that a column segment's Hilbert ranks cover all residues mod 7.
- Existence step of (C): the H_64 line property was verified by computer. The reduction of H_Q to symmetric copies of H_64 is argued from the recursion, not written out in full.
- Not analysed: four-black mixed supports with two labels and two sea points, (V3) collisions, interactions across the 49 blocks at junctions (beyond noting that F1 sea points stay within h^2/S of the vertex), and the boundary transition of the exceptional labels.
- The incidence estimate in missing_estimate is heuristic. It is not proved, and it was not computed numerically.

## Missing estimate

F1 is at least as dense as the P family. Treat Y as a random odd number of size h, and let g = s - y_V for the vertex. Then P[Sq | Yg] is about gcd(Sq, g)/(Sq), and summing over q <= h^2/S gives an F1 candidate degree of about (gcd(S,g)/S) * tau(g') * log h. Averaged over labels in a block where F1 is alive, this is of order tau(S)(log h)^2/S. For S = 1568 that is roughly 0.02 (log h)^2, against a P mean of 0.17 to 0.30 in the census. It is unbounded at fixed S.
A bounded-M completion therefore needs a structural reason, not degree counting. In blocks with a != b (mod 7), rule (D) gives one: F1 vanishes identically. In the 7 blocks with a = b (mod 7), Y = 0 (mod 7) always and no parity or residue choice kills F1. There I would need one of three things:
(i) a bounded-M theorem for difference constraints of the form 'Sq divides Y g', analogous to the factor-uniqueness lemma for P;
(ii) a different profile family for labels with a = b (mod 7);
(iii) an S whose prime-power parts grow, which costs width.
If F1 constraints behaved like random sparse constraints, M would need to grow like D/log D. With width S M h^2 that gives about h^2 (log h)^(2+o(1)), worse than the menu exponent 1.3108. This is a heuristic warning only.

## Next steps

- Add rule (D) to the period-seven Hilbert route: in each block with a != b (mod 7), the endpoint = L (mod 7) gets the parity opposite to L. This removes F1 from 42 of the 49 blocks, for every S and M.
- Treat the 7 blocks with a = b (mod 7) as the hard core. Decide between class (0,0) and (5,5), between an orientation split or none, and on a hole-toggling policy. Then test the hole-independent (5,5) forcing (|Delta j| = 7 pairs) by an exact search on H_{2^k} with j taken mod 49.
- Prove or refute an F1 analogue of the factor-uniqueness lemma: for a fixed vertex row and sea row, bound the number of earlier constraints 'Sq divides Y g' per label by a bounded multiple of something summable. That would decide whether a bounded M can survive F1 in the blocks with a = b (mod 7).
- Extend (C) to M >= 4 independently of holes. For the slot-landing cases of (C'), add the third label whose slot E hits, and search the resulting three-label constraint system for an unsatisfiable core at M = 4 to 17.
- Analyse whether hole toggling creates new events: H-hole sea points as E or W in two-label F1 events with s = H and u = 0 mod 7.
- Rerun the P certificates at h = 2048 and 4096 together with F1 in a scaled profile, to measure F1 incidence against the heuristic tau(S)(log h)^2/S.

