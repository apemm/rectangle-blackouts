# Cross-block right angles and the rigid 2-adic layout

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Two independent derivations. Both prove that a rigid 2-adic block order removes every tilted right angle among label points, at width O(h^2) times the largest number of classes of one diagonal. So the label scaffold costs O(h^2) if chi(Gamma) is finite. Not audited yet.

# Derivation 1: algebra of the configuration and the rigid rule

## Status

partial

## Summary

The derivation is correct, and its exact form is N = q(10t' - T'), c2 = 8qt'. The R-black case never happens, and the load constant is off. No O(h^2) construction found: the only class-independent kill is the rigid 2-adic rule, which reduces the cross-block problem to bounded per-diagonal chromatic number.

## Statements

Setting. Stride 4 with constant-offset classes. Class c has offset s_c (j = i + s_c, T_c = 2s_c + 1), slot set S_c, and block position M_c, an integer multiple of a prime p > 20h. Slot i sits at column 4(i + M_c), with odd point (4(i+M_c), 2i+1) and even point (4(i+M_c), 2(i+s_c)+2). Write n(c) = s_c - M_c and N = n(c') - n(c0) = Δs - ΔM.

THEOREM 1 (exact form; proved). Let V be the even point of slot i0 of c0, P the odd point of slot i0+t1 of c0 (t1 != 0), and Q the even point of slot iQ of c' != c0. Put c2 = j_Q - j_V, g = gcd(|t1|,|T0|), t' = t1/g, T' = T0/g, b = 10t' - T'. The angle at V is right iff b divides N and, with q = N/b, c2 = 8qt' (equivalently iQ - i0 = 8qt' - Δs). The fourth corner R = P+Q-V lies in the column of slot iQ+t1 of c', in the odd row 2(i0+t1+c2)+1 = 2(iQ+t1+Δs)+1. The earlier formulas hold: u = -Δs + 8t1N/(10t1-T0), and m = |b| = |10t1-T0|/gcd(T0,t1) must divide N. In addition, c2 is a nonzero multiple of 8, and (V, t1, c') admits at most one Q.

THEOREM 2 (bounds; proved). Assume distinct blocks satisfy |M_c - M_c'| >= 20h+1, which holds when M is in pZ. Then every configuration of Theorem 1 has:
(a) |T'| > 294|t'|, hence |t1| < |T0|/294, and the vertex class has |T0| > 294;
(b) |q| >= 19 and |c2| >= 152;
(c) |N| <= (K-1)(10 + |T'|/|t'|)/8 <= (K-1)(|T0|+10)/8 < h(h+9)/16;
(d) Δs != 0, so two classes of the same diagonal never form such an angle, and R is never black;
(e) if N has a prime factor l > 1.035h, no configuration exists between c0 and c' in either role. Without the 20h spacing, l >= 2.25h suffices.

THEOREM 3 (fatality; proved, given the audited axis owner lemma). A configuration with slot iQ+t1 occupied in c' and 0 <= i0+t1+c2 <= A-1 is fatal. R is white in a double column that has a black even point, so an axis rectangle and the tilted rectangle VPRQ both have presentation {R}. If the slot is empty or outside the block, R's column is a sea column, and fatality depends on the sea. Correction to the derivation: the "R black, fully black" branch never occurs, and the row condition on R must be added. Remark: a fully black tilted rectangle that has a lattice point inside one side is invalid on its own (proof below), so that branch would have been fatal.

THEOREM 4 (transfers and immunity; proved).
(a) v2(q) = v2(N). If v2(N) >= ν for every pair of blocks of distinct diagonals with |N| < h(h+9)/16, and 2^(ν+3) >= K, there is no configuration. This is Lemma 1 of partial_power_of_two_rule.md in the present notation.
(b) If 5 does not divide T0, then v5(q) = v5(N). More generally, vl(q) = vl(N) for every prime l that does not divide b.
(c) If every slot of c0 lies in one residue class mod 2^a, then 2^a divides t', 2^(a+3) divides c2, and c' must have the same j-residue mod 2^(a+3). Classes from different residues mod 2^a never interact.
(d) A class whose slot differences all exceed (h-1)/294 is never c0 and never the c' of a configuration with R's slot occupied.
(e) Stride s = 2σ: c2(2(σ^2+1)t1 - T0) = 2σ^2 t1 N, so v2(c2) = 1 + 2v2(σ) + v2(t1) + v2(N). The rule needs 2^(1+2v2(σ)+ν) >= K.

THEOREM 5 (conditional scaffold, i.e. reduction to layers; proved, modulo the cited in-block and cross-block reductions: the 11 November reattack note, Sections 2 and 3, rechecked there; Proposition 1 of 12 November; Lemma 4 of stride_menu.md, not audited). Let 2^ν be the least power of 2 >= K/8, and colour each diagonal properly in G_T^(4) with χ_T colours. Put B = max over ρ mod 2^ν of Σ_{s ≡ ρ} χ_{T_s}, a sum over at most ceil((h-1)/2^ν) <= 17 diagonals. Place the k-th class of diagonal s at M ≡ 0 (mod p), M ≡ s (mod 2^ν), in the k-th free period of its residue. Then:
- the width is at most 4p·2^ν·B + 4A <= 20h^2 B + 2h;
- the label points contain no tilted right angle (so no corner triple among label points) and no rival pair inside a class.
So if max_T χ_T is bounded, the cross-block problem is solved in width O(h^2). Conversely, this layout has width >= 4p2^ν(χ_max - 1) >= 5h^2(χ_max - 1), because two classes of one diagonal are at least p2^ν apart.

NOT PROVED: any layout of width O(h^2) with O(1) fatal labels per class, unconditionally; any obstruction theorem for general layouts.

## Proofs

0. NOTATION. A = ceil(h/2), K = floor(h/2), 0 <= i <= A-1, 0 <= j <= K-1, T = 2(j-i)+1, so |T| <= h-1. Columns are x = 4(i + M_c) and n(c) = s_c - M_c, so x/4 = j - n(c). Take V in c0 at slot i0, P in c0 at slot i0+t1, and Q in c' at slot iQ, with u = iQ - i0, Δs = s' - s0, ΔM = M' - M0 and N = Δs - ΔM.

1. PROOF OF THEOREM 1. The legs are
VP = (4t1, (2(i0+t1)+1) - (2(i0+s0)+2)) = (4t1, 2t1 - T0),
VQ = (4(u + ΔM), 2(u + Δs)) = (4(c2 - N), 2c2), with c2 = u + Δs = j_Q - j_V.
The dot product is 16t1(c2 - N) + 2c2(2t1 - T0) = 2c2(10t1 - T0) - 16t1N. So the angle is right iff c2(10t1 - T0) = 8t1N. Divide by g: c2·b = 8t'N with b = 10t' - T'. T' is odd, so b is odd. Also gcd(b,t') = gcd(T',t') = 1, so gcd(b, 8t') = 1 and b divides N. With q = N/b we get c2 = 8qt'. Conversely, N = qb and c2 = 8qt' give c2 b = 8t'N. Substituting c2 = u + Δs gives u = 8qt' - Δs = -Δs + 8t1N/(10t1 - T0), which is the earlier formula. Since 10t1 - T0 is odd and nonzero, u is unique. Its integrality condition is |b| = |10t1 - T0|/g dividing N, as stated. The fourth corner is R = P + Q - V = (4(i0+t1+u+ΔM+M0), 2(i0+t1+c2)+1). Its column is that of slot iQ+t1 of c', and i0+t1+c2 = iQ+t1+Δs. Finally c2 != 0, because c2 = 0 would force N = 0, while N = Δs - ΔM with |ΔM| >= p > |Δs|.

2. PROOF OF THEOREM 2. j_V and j_Q lie in [0, K-1], so |c2| <= K-1, and hence 8|q||t'| <= K-1. Also |Δs| <= (K-1)+(A-1) = h-2, so |N| >= |ΔM| - (h-2) >= 19h+3. Then
19h+3 <= |q||b| <= ((K-1)/(8|t'|))(10|t'| + |T'|) < (h/(16|t'|))(10|t'| + |T'|).
This gives 304|t'| < 10|t'| + |T'|, which is (a). Next, |b| <= |T'|(1 + 10/294) < 1.035(h-1), so |q| > 19h/(1.035h) > 18.3, which gives (b). The middle inequality above, with |T'|/|t'| <= |T0|, gives (c). For (d): if Δs = 0 then N = -ΔM ≡ 0 (mod p). But |q| <= (K-1)/8 < p and |b| <= 10(K-1)/8 + h - 1 < 2.25h < p, so the prime p cannot divide qb = N != 0. For (e), the same argument works with l in place of p: l > |q|, and l > |b| (|b| < 1.035h under the spacing, |b| < 2.25h in general).

3. PROOF OF THEOREM 3. Suppose slot iQ+t1 is occupied in c'. Its column is a double with odd row 2(iQ+t1)+1 and an even row. R's row is 2(iQ+t1+Δs)+1, which differs from the odd row because Δs != 0, so R is white. R lies in an odd row (part A), and its column has a black point in the even row (part B). By the axis owner lemma (lower_bound_windows.md, audited), some axis rectangle has presentation {R}. The tilted rectangle VPRQ has black corners V, P, Q and presentation {R}, so it is a distinct rectangle with the same presentation. That is fatal (Definition valid, sec2_prelim.tex). R must also lie in the grid, which is the row condition. Otherwise R is in a singleton or sea column, and the outcome depends on that column's letter.
Remark on fully black rectangles. Let R1 have black corners V, P, R, Q in that cyclic order, and let the side VQ contain a lattice point p0 strictly inside it. Put q0 = p0 + (P - V). Then R2 = {V, P, q0, p0} and R3 = {p0, q0, R, Q} are lattice rectangles with C(R2) Δ C(R3) = {V, P, Q, R}, which is black. By Lemma diff they have the same presentation. In Theorem 1, VQ = 4q(T' - 2t', 4t') with |q| >= 1, so such a p0 exists.

4. PROOF OF THEOREM 4.
(a) b is odd, so v2(q) = v2(N) >= ν, and then |c2| = 8|q||t'| >= 2^(ν+3) >= K > |c2|, a contradiction. Pairs with |N| >= h(h+9)/16 cannot interact by Theorem 2(c).
(b) If l does not divide b, then vl(q) = vl(N). For l = 5: b ≡ -T' (mod 5), and 5 does not divide T', which divides T0.
(c) 2^a divides t1 = g t' with g odd, so 2^a divides t'. Then 2^(a+3) divides c2 = j_Q - j_V.
(d) c0 needs |t1| < |T0|/294 <= (h-1)/294. With R's slot occupied, c' contains slots iQ and iQ+t1 at the same gap.
(e) For stride s = 2σ, VP = (s t1, 2t1 - T0) and VQ = (s(c2 - N), 2c2). The dot product is s^2 t1(c2 - N) + 2c2(2t1 - T0). Setting it to zero and dividing by 2 gives c2(2(σ^2+1)t1 - T0) = 2σ^2 t1 N. The bracket is odd, which gives the valuation identity.

5. PROOF OF THEOREM 5.
Positions. M ≡ 0 (mod p) and M ≡ s (mod 2^ν) fix M mod p2^ν by CRT, and p is odd. Residue ρ has demand D(ρ) <= B, so B periods suffice. The width is at most B·p2^ν M-units plus one block, that is 4pB2^ν + 4A columns. Bertrand gives p < 40h, and 2^ν < K/4.
No tilted right angle among label points:
- Odd vertex: x ≡ 4i (mod p) and p > 10h. By the reattack note, Section 2, one leg is horizontal.
- (E;O,O) and (O;E,E): the dot product is odd.
- Both ends outside the vertex's block: blocks are more than 78h columns apart, so |X1X2| > h^2 > |Y1Y2|.
- One end outside: the in-block leg has slope > 36 in absolute value. An even-even leg in a constant-offset block has direction (4,2), so that end is odd. This is the (E;O,E) type.
- Inside one block: no right angle (Proposition 1 of 12 November).
- The rule n(c) ≡ 0 (mod 2^ν) holds for all c, so Theorem 4(a) removes the (E;O,E) type.
Rival pairs. Within a class, there are none because classes are independent in G_T. Across blocks, a rival pair spans fewer than h columns, so its two points lie in one block.
Lower bound. Two classes of one diagonal occupy distinct M in the same class mod p2^ν, so they are at least p2^ν > 20h·K/8 apart. Hence width >= 4p2^ν(χ_max - 1).

6. LOAD (heuristic, corrected constant). For a random block order with one class per block position (diagonal uniform), a fixed (g, t', q) is realised with probability about 1/P (block spacing P = Ch), and the three other slots are occupied with probability ρ^3. Summing over admissible (g, t', q):
E(fatal per label) ~ (ρ^3/(4C)) Σ_{g | T0, T0/g > 294} ln(T0/(294g)) at C = 20,
not ρ^3 τ(T0) ln h/320. Computed exact counts of admissible triples divided by P at h = 10^6:
- T0 = 999983 (prime): 0.096, against ln(T0/294)/80 = 0.102;
- T0 = 765765 (τ = 96): 1.26, against τ ln h/320 = 4.14.
Averaged over T0 <= h, the divisor sum is about (ln(h/294))^2/2, which matches the log^2 load of the 11 November note.

7. WHY THE TARGET IS NOT REACHED (analysis, not a theorem).
(i) A kill that holds for every slot set needs every interacting pair's N to avoid F(T0) = {q(10t' - T0/g)}. The only global mechanisms found are valuation transfers (Theorem 4(a,b)) and rough differences (Theorem 2(e)). Both need all interacting n(c) congruent modulo a modulus >= K/8 (2-adic) or > 1.035h (odd prime), and that is rigid. By CRT with M ≡ 0 (mod p), each diagonal gets one slot per period of length >= 2.5hK. So the cost is governed by max_T χ_T, as in Theorem 5. Tying Δs to Δc (s_c = c + const in a run, with an odd prime l > 1.035h dividing P - 1) is this odd-prime rigid rule, with one class per diagonal per run.
(ii) Partial rules mod 2^v with 2^v = K/R pool about 2R diagonals per residue, and leave survivors with |t'| < R/8 and a divisor-weighted load. Splitting j-windows or j-residues (Theorem 4(c)) is equivalent to pooling: width about 1.25h^2(2R·avg χ + max χ).
(iii) For R = 16 the survivors are exactly t1 = ±g with g | T0 and g < |T0|/294, q = ±2^v, c2 = ±2^(v+3) and N = ±2^v(±10 - T0/g): 4τ'(T0) exact values per vertex class. This is the sparsest non-rigid structure found, and I found no layout that avoids it at bounded pooling.
(iv) Sparse immune classes (Theorem 4(d)) cost about h/2 columns per label, so they can absorb only O(h) excess labels. Excess labels from diagonals with χ_T above a fixed bound are about h times the number of such diagonals.

## External results used

- Axis owner lemma (lower_bound_windows.md, audited): used in Theorem 3.
- Lemma diff and Definition valid (papers/extremal/sections/sec2_prelim.tex): used for fatality and for the remark on fully black rectangles.
- Rechecked Sections 2 and 3 of research_archive/2026-11-11/quadratic_threshold_reattack.md, and Proposition 1 of research_archive/2026-11-12/arc_classes_monotone_partition.md: the in-block, odd-vertex and steep-leg reductions used in Theorem 5.
- Lemma 4 of research_archive/2026-11-13/stride_menu.md (not audited): the same reductions for general even strides, used only in Theorem 4(e) and the stride remark.
- Bertrand's postulate: a prime p with 20h < p < 40h.

## Checks

Script folder: the matching scripts_ folder of this directory. Every run took under a few seconds.

(1) check_param.py: brute force over all (V even in c0, P odd in c0, Q even in c'), against the parametrization of Theorem 1, on random classes with small spacing so that configurations exist. Runs (h, P, classes): (40,3,6), (40,5,6), (60,7,6), (60,1,8), (50,11,8), (44,47,4). The configuration counts were 1, 6, 23, 4, 45 and 1, and the two sets were identical in every run.

(2) count_fatal.py at h = 2000, p = 40009, one full class per diagonal, fatal configurations counted with R's slot occupied and R in the grid:
- random order: 546 and 235 configurations (3 and 2 bad class pairs);
- rigid rule with 2^7 = 128 >= K/8 = 125: 0;
- 2^6: 1380; 2^5: 1318.
The width was about 80h^2 columns in all layouts, so the rigid rule costs nothing when demand is balanced.

(3) triples.py: exact counts of admissible (g, t', q) at h = 10^5 and 10^6. They support the corrected load formula (prime T0 = 999983: 0.096 against 0.102) and show that the earlier τ ln h/320 overestimates composite T0 by a factor of 3 to 4. A first version had a loop bug, which returned 0 for prime T0. I fixed it and reran.

All proofs in this result were re-read line by line by me only; there was no independent audit.

## Gaps

- No construction of width O(h^2) with no fatal cross-block configurations (or O(1) per class) is proved unconditionally. Theorem 5 needs max_T chi(G_T^(4)) bounded. Ledger rows T31 and T34 prove that related graphs (the odd Pythagorean graph and the in-strip palette) have unbounded chromatic number. I did not check whether they imply max_T chi(G_T^(4)) -> infinity.
- No obstruction theorem for general (non-rigid) layouts. The heuristic first-moment count suggests that full classes cannot avoid fatal configurations at constant C once ln h > 160. That rests on independence assumptions and is not a proof. Single-pair obstructions are impossible, since primes N are always safe (Theorem 2(e)).
- Theorem 5 relies on unaudited inputs: Lemma 4 of stride_menu.md, used for stride 4 as in the rechecked Sections 2 and 3 of the 11 November reattack note, and limit_graph_gamma.md for the reading through chi(Gamma). It does not address mixed quadruples (T21 gives explicit mixed collisions in CRT layouts) or the sea.
- Theorem 3 uses the axis owner lemma as audited in lower_bound_windows.md. I did not re-derive that lemma. When R's slot is empty, fatality depends on the sea letter of R's column and on whether the presentation {R} is unique; I did not analyse this.
- The load formula in Proof item 6 is heuristic (random block order, uniform diagonals). Only the triple counts are exact.

## Missing estimate

To reach width O(h^2) by this route, one of the following is needed:
(A) max_T chi(G_T^(σ)) bounded for some finite stride menu. Theorem 5 and its stride version then finish the cross-block part.
(B) A non-rigid layout with Σ_{c0} #{c' : N(c0,c') ∈ F(T0), with alignment} = O(#classes), where F(T0) = {q(10t' - T0/g)}. The forbidden density at block distance d is about Σ_{g | T0, T0/g > 16Cd} 1/(8Cd), and its sum over d is the divisor-weighted log^2 load.
(C) A class-shape rule that removes the divisor-gap pairs (gaps g t', g | T0, g < |T0|/294) without multiplying the class count.

## Next steps

- Check whether T31/T34, or the SAT bound chi(Gamma) >= 7, implies max_T chi(G_T^(4)) -> infinity. If it does, Theorem 5 becomes a proved obstruction for every rigid (valuation-rule) layout, and the cross-block problem must be solved non-rigidly.
- Study the R = 16 survivor family of Proof item 7(iii): exactly 4τ'(T0) values N = ±2^v(±10 - T0/g), with j-shift exactly ±2^(v+3). Look for a matching of heavy-residue classes to borrowed slots that avoids these exact values. This is the sparsest non-rigid structure found.
- Combine Theorem 2(d) with the layer problem: classes of one diagonal never interact, so a heavy diagonal's classes can sit in consecutive blocks. Only boundary pairs with other diagonals need control. Bound the cost of such clusters.
- Audit Theorems 1 to 4 independently and add them to the ledger. Replace the load constant τ(T0) log h/320 with the divisor-weighted (1/(4C)) Σ_{g|T0} ln^+(T0/((16C - 26)g)) in partial_power_of_two_rule.md and in the earlier notes.

# Derivation 2: first moment under a random order, and the rigid rule

## Status

partial

## Summary

I checked the derivation and it is correct, with five corrections. The fatal first moment under a random block order is about 0.06 Phi_lambda(T0)/lambda per label, not rho^3 tau log h/320 (proved upper bound O(h^2 log^2(h/lambda)/lambda)). A 2-adic rigid layout provably removes every cross-block (E;O,E) angle, and in fact every tilted right angle among label points. It costs at most 2h max_T M_T block positions, which is O(h^2) width if chi(Gamma) < infinity.

## Statements

Setting: stride 4, one-prime scaffold. Labels (i,j) sit in constant-offset classes. A class of diagonal s (T = 2s+1, j = i+s) sits at position pos (an integer), on columns 4(i + P pos). P is a prime with P > 20h. A = ceil(h/2), K = floor(h/2), M_T is the number of classes of diagonal T, C = sum_T M_T, and lambda = P/h.

(A) Derivation [proved; brute-force check]. Take V = the even point of slot i0 of class c0, P' = the odd point of slot i0+t1 of class c0 (t1 != 0), and Q = the even point of slot i0+u of class c'. Put Dc = pos(c') - pos(c0) != 0, Ds = s' - s0, N = Ds - P Dc and c2 = u + Ds. The angle at V is right iff c2 (10 t1 - T0) = 8 t1 N, so c2 = 8 t1 N/(10 t1 - T0) and u = c2 - Ds. This is the earlier formula. Put g = gcd(t1, T0), t1' = t1/g, e' = (10 t1 - T0)/g (odd, coprime to t1'). Then u is an integer iff e' | N, and then c2 = 8 t1' n with n = N/e'. The fourth corner is R = (4(i0+u+t1+P pos(c')), 2(i0+t1+c2)+1): it is in the column of slot iQ+t1 of c', in the odd row 2(iQ+t1+Ds)+1.
Corrections:
 (A1) Ds != 0 always (see B2), so R is never black when that slot is occupied. The "fully black" case does not occur.
 (A2) Fatal also needs R in the grid: 0 <= i0+t1+c2 < A. This is not automatic.
 (A3) If slot iQ+t1 of c' is empty, R's column is a singleton. It is fatal when the singleton is in an even row (axis owner lemma). It is a candidate harmless triple only when the singleton is in an odd row other than row(R).
 (A4) Exact ranges: |t1| <= K|T0|/(8(P-h) - 10K) < K/147. Only divisors d = |T0|/g >= (8(P-h) - 10K)/K (about 16 lambda) contribute. |Dc| <= (K(h+10)/8 + h)/P < h/(16 lambda) + 1.
 (A5) The load has a 1/lambda factor, and the log is per large divisor (see F).

(B) Two locality facts [proved]. (B1) The bounds in A4. (B2) Two blocks of the same diagonal never form a cross-block (E;O,E) angle, at any distance.

(C) Rigid 2-adic layout [proved]. Let 2^r be the least power of 2 with 2^(r+3) >= K. Suppose that s_c - P pos(c) = kappa (mod 2^r) for every class c, with kappa fixed. Then:
 - the label points have no tilted right angle at all;
 - no two label points form a rival pair;
 - every class is still monotone and P-free (classes independent in G_T(h)).
Placing the classes of residue rho = s mod 2^r at positions P^{-1}(rho - kappa) + 2^r k, k = 0, 1, ..., uses fewer than 2^r max_rho N_rho <= 16 2^r max_T M_T < 4K max_T M_T <= 2h max_T M_T positions, where N_rho = sum over s = rho (mod 2^r) of M_s. The width is at most 8Ph max_T M_T + 4A <= 320 h^2 max_T M_T + 2h, taking P in (20h, 40h].

(D) Limits of rigidity [proved]. (D1) Every rigid layout uses at least 2^r (max_T M_T - 1) >= (K/8)(max_T M_T - 1) positions. (D2) chi(G_T(h)) <= chi(Gamma) for every T and h, by the map i -> i/T. (D3) Scaling: suppose some finite subgraph of Cay(Z, D_T0^inf) has chromatic number B+1, uses L-values below H and spans a length l. Then every diagonal cT0, with c odd and c <= min((h-1)/H, n_(cT0)(h)/l), has chi(G_(cT0)(h)) >= B+1. That is at least c_B h diagonals for large h.

(E) Conditional corollary [proved given D2]. If chi(Gamma) = B < infinity, then for every h the labels split into at most B(h-1) constant-offset P-free classes. In the rigid layout these have no tilted right angle among label points, use at most 2Bh positions, and fit in width at most 320 B h^2 + 2h. So the cross-block (E;O,E) bottleneck is removed in width O(h^2). Mixed quadruples and the sea are not addressed.

(F) First moment under a uniformly random order [upper bound proved; order and constant numerical]. E <= 3.3 (max_T M_T) h^2 (1 + log^+(h/(8 lambda)))^2 / lambda. For one class kappa0 of diagonal T0, the expected number of bad (partner, distance) pairs is at most 2.2 (max M) Psi(T0)/lambda, with Psi(T) = sum over d | T, d >= 8 lambda, of (1 + log(d/(8 lambda))). Numerically, in the one-class-per-diagonal model, E/(sum over labels of Phi_lambda(T0)) is about 0.06/lambda (0.0054, 0.0027-0.0030, 0.0015 at lambda = 10, 20, 40). Here Phi_lambda(T) = sum over d | T, d > 16 lambda, of (phi(d)/d)(log(d/(16 lambda)) - 1).

NOT PROVED: m_h = O(h^2); chi(Gamma) < infinity; any lower bound on E; that random-order repairs (deletion, LLL, regions) cannot reach O(h) extra classes (heuristic only).

## Proofs

Notation as in the theorem. Points: odd point of slot i in a class at position p is (4(i+Pp), 2i+1). The even point is (4(i+Pp), 2(i+s)+2). P is prime, P > 20h.

1. THE DERIVATION (A). V = (4(i0+P p0), 2(i0+s0)+2), P' = (4(i0+t1+P p0), 2(i0+t1)+1), Q = (4(i0+u+P p'), 2(i0+u+s')+2). Then VP' = (4t1, 2t1 - T0) and VQ = (4(u + P Dc), 2c2) with c2 = u + Ds. The dot product is 16 t1(u + P Dc) + 2c2(2t1 - T0). Substitute u = c2 - Ds: 16 t1(c2 - N) + 4 t1 c2 - 2 T0 c2 = 0, that is, c2(10t1 - T0) = 8 t1 N. Solving for u gives the earlier u = -Ds + 8t1 N/(10t1 - T0).
10t1 - T0 is odd and equals g e'. gcd(e', t1') = gcd(10t1' - T0/g, t1') = gcd(T0/g, t1') = 1. So (10t1 - T0) | 8t1N iff e' | 8t1'N iff e' | N. This is the earlier "m | N" with m = |e'|. Then c2 = 8t1'N/e' = 8t1'n.
R = P' + Q - V has column 4(i0+u+t1+Pp') and row 2i0+2t1+1 + 2(i0+u+s')+2 - 2(i0+s0) - 2 = 2(i0+t1+u+Ds)+1 = 2(i0+t1+c2)+1. This gives A2: R is in the grid iff 0 <= i0+t1+c2 < A.
When slot iQ+t1 of c' is occupied, its column is a double with odd row 2(iQ+t1)+1. That differs from row(R) because Ds != 0 (B2). So R is white, and the column has an even black point. By the axis owner lemma (lower_bound_windows.md, audited) some axis rectangle has presentation {R}. The tilted rectangle VP'RQ shows only R, so the configuration is fatal. When the slot is empty, the same lemma makes an even-row singleton fatal, which is A3.
Brute-force check (check1_formula.py): all (E;O,E) triples with V,P' in one block and Q in another, found by geometry for (h,P) = (40,11), (48,23), (41,37). The formula sets agree exactly (49, 31 and 4 instances). The fourth-corner and m | N claims held in every instance.

2. LOCALITY (B). (B1) |Ds| <= h-2 (s ranges over -(A-1)..K-1), and |N| >= P|Dc| - h + 2 >= P - h > 0. From |c2| <= K-1: |N| = |c2||e'|/(8|t1'|) <= (K-1)|e'|/(8|t1'|), and |e'| <= 10|t1'| + d with d = |T0|/g <= h-1. This gives |N| <= (K-1)(1.25 + h/8), so |Dc| <= ((K-1)(h+10)/8 + h)/P. From |t1'|(8(P-h)) <= 8|t1'||N| <= (K-1)(10|t1'| + d) we get |t1'|(8(P-h) - 10K) < Kd, and hence the bound on |t1|. For t1' >= 1 we need d > (8(P-h) - 10K)/K.
(B2) If Ds = 0 then N = -P Dc. Also |e'| <= 10A + h < P, so gcd(e', P) = 1, and e' | N forces e' | Dc, hence |e'| <= |Dc|. But |N| = P|Dc| <= (K-1)|e'|/8 <= (K-1)|Dc|/8, which gives P <= K/8. That is false.

3. CLASSIFICATION FOR STRIDE 4 (re-derived; this is needed in C). Every column satisfies x = 4i (mod P) for the point's slot i.
 - (O;O,O): the dot product is 20 Di1 Di2 (mod P). Since |Di| < A < P and P does not divide 20, one leg has Di = 0, so it is horizontal. The other leg is then vertical, and the angle is axis-aligned.
 - (O;O,E): the dot product is 2 Di1 (8i2 + 2j2 - 10i0 + 1) (mod P). The bracket is odd and has absolute value at most 18A + 2K + 1 < P. So Di1 = 0, and again the angle is axis-aligned.
 - (O;E,E) and (E;O,O): the dot product is 16(..) + odd·odd, which is odd.
 - Inside one class, consider the legs along a line, (4d, 2d), and across, (4d, 2d ± T). Along with along gives 20 d1 d2 != 0. Along with across gives d1(20 d2 ± 2T), where the bracket is 2 mod 4. Two across legs from one vertex give 16 d1 d2 + (2d1 ± T)(2d2 ± T), which is odd. So a class has no right angle (Proposition 1).
 - Positions are distinct integers, so blocks are more than 4(P - A) > 36h apart. If both ends leave V's block, then |X1 X2| > h^2 > |Y1 Y2|. If exactly one end Z leaves, the in-block leg W satisfies |Y_W|/|X_W| = |X_Z|/|Y_Z| > 1. An in-block leg between two even points has slope 1/2. So in (E;E,E) and (E;O,E) the in-block leg must be V to an odd point P'. Then t1 != 0, since t1 = 0 gives a vertical leg and an axis-aligned angle.
 - Hence every tilted right angle among label points is the cross-block (E;O,E) type of part 1.
 - Rival pairs need a horizontal distance below h, so they lie inside a block, and independence in G_T(h) excludes them (rival lemma, sec5).
None of this uses the order of the positions.

4. THEOREM C. Under the rule, N = Ds - P Dc = (s' - P p') - (s0 - P p0) = 0 (mod 2^r), and N != 0 by B1. In a configuration, c2 = 8 t1 N/(10 t1 - T0) is an integer with an odd denominator. So v2(c2) = 3 + v2(t1) + v2(N) >= r + 3, and c2 != 0, which gives |c2| >= 2^(r+3) >= K. But c2 = j_Q - j_V and 0 <= j < K, so |c2| <= K - 1. This is a contradiction. With part 3, no tilted right angle among label points remains. This also covers t1 values outside the range in B1.
Cost: a residue rho is a set of consecutive values of s in a window of length h - 1, so it holds at most ceil((h-1)/2^r) <= 16 diagonals, because 2^r >= K/8 >= (h-1)/16. Residue rho uses the positions P^{-1}(rho - kappa) + 2^r k with k < N_rho, all below 2^r N_rho, and those positions satisfy the rule. Also 2^r < K/4. Columns are at most 4(A - 1) + 4P(2^r max N_rho).
Brute-force check (check3_rigid.py, geometry only, P just above h, where random layouts have many angles):
| (h, P) | random layout (E;O,E) angles | rigid layout (E;O,E) angles |
| --- | --- | --- |
| (40, 41) | 2 | 0 |
| (48, 53) | 12 | 0 |
| (64, 67) | 9 | 0 |
| (80, 83) | 15 | 0 |
| (72, 101) | 12 | 0 |
Realistic case (check4_rigid_cost.py, formula count, greedy stride-4 classes, lambda = 20, h = 4000): rigid 0 fatal against random 2271. Positions used: 2851 = 2.85h at h = 1000, 16111 = 4.03h at h = 4000, 31459 = 3.93h at h = 8000. That is about 1.2 to 1.5 times C. max N_rho = 45, 63, 62 against means 37.5, 42.2, 44.4, and max M_T = 12, 17, 19.

5. D. (D1) The M classes of one diagonal share one residue mod 2^r, so they sit at distinct positions in one progression of step 2^r, and the largest is at least 2^r(M-1).
(D2) For stride 4, (4d)^2 + (2d+T)^2 = T^2(20r^2 + 4r + 1) with r = d/T. An integer is a rational square iff it is a square. So i ~ i' in G_T(h) implies that i/T ~ i'/T in Gamma (both signs are covered by the ± in Gamma).
(D3) Q(cT, cd) = c^2 Q(T, d), so c·S_T0^inf is contained in S_(cT0)^inf with L scaled by c, and a translate of cW lies in G_(cT0)(h) under the stated size conditions.

6. F (upper bound). Uniform order: Pr[pos(k') - pos(k0) = Dc] = (C - |Dc|)/(C(C-1)) <= 1/(C-1). Fix V and t1. The integer n (with N = e'n) determines N, hence Dc and Ds (since P > 2h), hence T'. At most M_(T') classes can be there, and each contributes at most 1 for the given i0. So E <= (max M/(C-1)) sum_V Z(T0), where Z counts the valid (t1, n).
Parametrize by d = |T0|/g, k = |n|, t1' and the sign of n. From |c2| = 8|t1'|k <= K-1 we get 1 <= |t1'| < K/(8k), and |N| = k|e'| lies in [kd - 1.25K, kd + 1.25K]. Validity needs |kd - P Dc'| <= 1.625h for some Dc' >= 1. For a fixed Dc' that allows at most 4.25h/d values of k, each with kd >= P Dc'/2 (since P > 3.25h). Each such k carries at most K/(2k) <= Kd/(P Dc') pairs (t1', sign). Also k < K/8 forces Dc' <= Kd/(4P) <= d/(8 lambda). Summing, Z_d <= (4.25hK/P)(1 + log(d/(8 lambda))) <= (2.125h/lambda)(1 + log(d/(8 lambda))), and Z_d = 0 for d < 8 lambda. So Z(T0) <= 2.125 h Psi(T0)/lambda, which is the per-class bound (it does not depend on i0).
Summing, sum_V Psi <= (h/2) sum over odd d in [8 lambda, h) of (h/d + 2)(1 + log(d/(8 lambda))) <= 1.5 h^2 (1 + L)^2, with L = log^+(h/(8 lambda)). With C - 1 >= h - 2 this gives E <= 3.3 max M h^2 (1+L)^2/lambda for h >= 100.

Numbers (check2_moment.py, exact expectation):
| h | lambda | model | E | per label | E/(sum Phi) |
| --- | --- | --- | --- | --- | --- |
| 1000 | 20 | full or greedy | 0 | 0 | — |
| 4000 | 20 | full | 4304 | 1.08e-3 | 0.0030 |
| 4000 | 20 | greedy | 1490 | 3.7e-4 | 0.0010 |
| 8000 | 20 | full | 35699 | 2.23e-3 | 0.0027 |
| 4000 | 10 | full | 17811 | — | 0.0054 |
| 8000 | 40 | full | 8626 | — | 0.0015 |
At h = 1000 there are no configurations because all divisors are below 16 lambda e. The pair (8000, 40) gives E/h = 1.078 against 1.076 for (4000, 20), consistent with E = (h^2/lambda) F(h/lambda).
Split by tau(T0) (h = 8000, full): per label 1.98e-3 (tau <= 2), 2.18e-3 (3-4), 2.42e-3 (5-8), 2.74e-3 (tau > 8). The ratio to Phi is 0.0024 to 0.0033 in every group, so Phi_lambda, not tau(T0) log h, carries the T0 dependence.

7. REPAIRS (heuristic, from F). The bad events live on pairs of classes, and u does not depend on i0. Each class has about c Psi(T0)/lambda expected bad partners, and the mean of Psi over T is about (1/4) log^2(h/(8 lambda)).
 - LLL: it needs this count to be at most about 1/4 for every class, so lambda >= max_T Psi(T) = h^(o(1)).
 - Deletion or alteration: the rate does not depend on how many classes a region holds (the local composition is what counts), so moved classes see the same rate and nothing decays.
 - Regions for offsets with many divisors: the rate comes from every divisor above 8 lambda and tends to infinity for typical T. Also, by D3 the chromatically rich diagonals have positive density. At h^2/4 columns per region that costs Theta(h^3).
 - Random-like layouts therefore need lambda of order log^2 h, that is width h^2 log^2 h, which is no better than T1.
 - The rigid layout is the one structured layout I found that has zero load. Its cost is 2^r max_rho N_rho.

## External results used

- Axis owner lemma (research_archive/2026-11-13/lower_bound_windows.md, audited per the target).
- Rival lemma (papers/extremal/sections/sec5_threshold.tex) and criterion (sec2_prelim.tex, Lemma criterion).
- Definition of Gamma and its relation to G_T(h): limit_graph_gamma.md. Only the elementary embedding D2 is used, re-proved here. The equality lim max_T chi(G_T(h)) = chi(Gamma) (its T2, unaudited) is not used for the upper bound.
- Bertrand's postulate (a prime in (20h, 40h]), for the explicit width constant.

## Checks

Scripts are in the script folders of this directory. All runs used py, each took under 60 s and well under 1 GB, and the repository was not touched.
- common.py: stride-4 distance sets and greedy P-free classes.
- check1_formula.py: brute-force geometry against the formula at (40,11), (48,23), (41,37). The sets agree (49, 31, 4), and the R and m | N claims held.
- check3_rigid.py: geometry-only count of (E;O,E) cross-block angles, random against rigid, at (40,41), (48,53), (64,67), (80,83), (72,101). Random gave 2, 12, 9, 15, 12; rigid gave 0 every time.
- check2_moment.py: exact random-order first moment at h = 1000, 4000, 8000 with lambda = 10, 20, 40, in the full and greedy models, split by tau(T0).
- check4_rigid_cost.py and check4b_cost_only.py: rigid cost at h = 1000, 4000, 8000, and the formula fatal count at h = 4000 (rigid 0, random 2271).

## Gaps

- No independent audit. I re-read Parts 1 to 6 line by line once.
- Theorem C cites the rival lemma (sec5) and the audited axis owner lemma. Part 3 re-derives the stride-4 classification (Lemma 4, Proposition 1') in full. Other strides would rely on the unaudited stride_menu.md Lemma 4.
- The O(h^2) conclusion is conditional on chi(Gamma) < infinity, which is open. limit_graph_gamma.md expects chi(Gamma) = infinity. If so, the rigid layout costs at least (K/8)(max_T chi(G_T(h)) - 1) positions, which is superlinear.
- The first-moment lower bound (order h^2 log^2(h/lambda)/lambda) is numerical (h <= 8000) and heuristic only. Only the upper bound is proved.
- That random-order repairs (deletion, LLL, regions) cannot reach O(h) extra classes is heuristic: the per-class rate is a first moment, with no matching concentration or lower bound.
- Mixed quadruples between blocks and the sea are untouched. The rigid layout fixes the block order, so any random-order argument for mixed quadruples would not apply to it.
- The fatal/harmless split for empty R-slots (A3) depends on the sea and on the uniqueness of the presentation {R}. I did not analyse it, and the rigid layout makes it moot.

## Missing estimate

To finish this bottleneck with the rigid layout, one needs a constant B such that, for every h, each diagonal T has a partition into at most B sets independent in G_T(h). chi(Gamma) <= B implies this. The menu analogue also suffices: min over sigma in F of chi(G_T^sigma(h)) <= B, with one rigid region per stride and 2^(r+1+2 v2(sigma)) >= K. Then the cross-block (E;O,E) family, and every tilted right angle among label points, is gone in width at most 320 B h^2 + 2h.
If chi(Gamma) = infinity, a different structured order is needed. It is a list-assignment problem: at block distance D, a block of diagonal T0 forbids a fraction of about tau_{>16 lambda D}(T0)/(4 lambda D) of the possible diagonals, so each block has about Psi(T0)/lambda forbidden (position, diagonal) combinations. The order must avoid all of them while keeping O(h) positions. Every 2-adic rule of modulus 2^r' < K/8 still costs at least 2^r'(max M - 1) positions and leaves a per-block load of about tau(T0) log R, with R = K/2^(r'+3).

## Next steps

- Audit Theorem C and Part 3 (short and elementary). If they pass, add a ledger row: 'rigid 2-adic layout: no tilted right angle among label points, width <= 8Ph max_T M_T', conditional on bounded M_T.
- Attack chi(Gamma) directly. It now decides whether the label scaffold costs O(h^2), as well as the partition question.
- Check mixed quadruples and the sea against the rigid layout. Its residue structure (s = P·pos + kappa mod 2^r) may make the mixed-quadruple arithmetic tractable, and it is the natural target now.
- Compute max_rho N_rho for the stride menu (about 1.2h classes, one rigid region per stride) to get the practical constant.
- If chi(Gamma) = infinity is expected, study the sparse list-assignment problem in the missing estimate. A Haxell-type independent-transversal argument fails by a factor of about tau·log R/2, so it needs extra structure.

