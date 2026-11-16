# The ladder filler layer against the nodal-cubic families

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: homogeneous Fo/Fo and Fe/Fe split into 2-adic levels; no fixed-period layer removes them (node branch); a ladder layer with class-slot period about h^(1/3) removes all of them and keeps most SAW* results. Not audited yet.

# Result

## Status

partial

## Summary

Homogeneous Fo/Fo and Fe/Fe split into 2-adic levels j. A layer with a fixed period cannot remove them, and the reason is the curve's node branch. A ladder layer whose class-slot period grows like h^{1/3} removes all of them. It keeps most of the SAW* results, but the pure gap and the one-label families are not re-proved.

## Statements

Setting. I use (n, Y) units: n is the slot and Y is the row divided by 4. Two labels L1 and L2 of one class sit at L2 - L1 = (2d, d). The fillers are U = F1 - L1 = (x1, u) and V = F2 - L2 = (x2, v), with p = x1 - x2 and q = x1 + x2. Classes are split by i mod 2^k. Four parity hypotheses are assumed:
- (H1) labels sit at slot offset 0 mod 4;
- (H2) a filler at an even offset has depth u = 2 mod 4 (hole), and one at an odd offset has u = 0 mod 4 (base);
- (H3) 8 | d;
- (H4) the label rows are fixed mod 2^{k+1} per class.
SAW and SAW* satisfy all four.

THEOREM 1 (classification of homogeneous Fo/Fo, proved). Assume (H1)-(H3) and both fillers in one row. Every solution of F(p,u,v) = 0 falls in exactly one of two branches.
- (B) Base branch: both fillers are bases at the same offset, v2(d) = 3, v2(p) >= 5, and m = p/d = alpha/beta with 4 | alpha and beta odd.
- (L_j) Hole level j, for j >= 2: both fillers are holes at offset 0, with v2(x1) = v2(x2) = j, v2(d) = 2j+1, v2(p) = j+2 and v2(q) = j+1. In the parametrization, alpha is odd and v2(beta) = j - 1. The two filler slots differ by 2d - p, which has 2-adic order exactly j+2.

Converse (proved). Take any coprime pair with alpha odd, beta even and 2 < alpha/beta < 4. Its primitive vector w/g has g in {1, 5}. Scale it by lambda = 2·odd, choosing lambda mod 16 to match the class residue of u. The result is a d < 0 configuration that satisfies every SAW* congruence: offset 0, both fillers in row T*-24, t = 2d = 0 mod 2^{2j+2}, and Lemma mixedeq. It is fatal whenever its two filler slots are fillers and the depth of L1 is divisible by u_w/g.

Corollary. The d < 0 homogeneous Fo/Fo shapes of SAW* are exactly {alpha odd, beta even, 2 < alpha/beta < 4}. Splitting classes by i mod 32 removes only (B). No further class split, label-residue choice or T* shift removes any level j: such a change fixes only u mod 2^{k-1}, and the choice of lambda absorbs that.

THEOREM 1' (Fe/Fe, proved). With even label points and fillers in one row, v2(t) = tau is odd and the fillers sit at slot order (tau-5)/2.
- tau = 5 gives bases.
- tau = 7 gives offset-2 holes.
- tau = 2j+5 gives offset-0 holes at level j.
- The two filler slots differ by a number of order (tau-1)/2.

LEMMA 2 (height threshold, proved). A level-j Fo/Fo shape needs h >= 1 + (64/5)·8^{j-1}. A level-j Fe/Fe shape needs h >= (8/5)·8^{j+2}.

THEOREM 3 (no periodic kill; exact reason). Let the rows of the offset-0 fillers be periodic in the slot with period 2^E·P', where P' is odd. Then every level j >= max(2, E-2) survives: F1 and F2 land in one row whenever both slots are fillers. The surviving shapes are explicit: alpha coprime to 2P', P' | beta, and also alpha != 2beta mod 5 when 5 | P'. This gives two consequences.
- (a) The non-class levels max(2, E-2) <= j <= k-1 are present under the all-slots-occupied convention. They are nonempty whenever E <= k+1.
- (b) The class levels j >= max(k, E-2) put both fillers on class-residue slots. They exist in real classes, where those slots are empty, for every h >= 1 + (64/5)·8^{j-1}.

The reason is the branch of the curve through the point (x1:u:x2:v:d) = (0:1:0:1:0), at beta = 0. Near it N-adically, for any modulus N, the slots of F1, F2 and L2 all coincide mod N while the depths stay units. Any rule that sees slots only through residues therefore cannot separate the two fillers.

To remove the class levels k..J_max(h) by rows, the class-slot rows must take at least 2^{J_max-k+1} distinct values, about 0.03·h^{1/3}. This is the size of a clique in the separation graph. That this many rows is forced in every case is not proved.

THEOREM 4 (ladder layer LAD_6(E'); kill proved, the rest partly). Split classes by i mod 64. The bases keep the SAW* rows T*-16 and T*. Offset-2 holes go to row T*-8-32(tau2 mod 4). Offset-0 holes with tau = rel/4 go to row T*-24-32·phi(tau), where:
- tau odd: phi = 1 + 2(((tau-1)/2) mod 4);
- tau = 2 mod 4: phi = 2 + 4(((tau-2)/4) mod 4);
- tau = 4 mod 8: phi = 4 + 8(((tau-4)/8) mod 4);
- tau = 8 mod 16: phi = 8 + 16(((tau-8)/16) mod 4);
- class slots (tau = 0 mod 16): phi = 16((tau/16) mod 2^{E'}).

(i) LAD has the exact staircase property: every filler pair has dy = 0 (and then v2(slot gap) >= 2) or v2(dy) = 3 + v2(slot gap).

(ii) LAD removes:
- the homogeneous Fo/Fo levels 2..5 and the class levels 6 <= j < E'+4;
- the homogeneous Fe/Fe branches tau = 5 (through i mod 64), tau = 7 (through the offset-2 ladder) and the offset-0 levels below E'+4.
With E' = max(0, J_max(h) - 3), where J_max(h) = 1 + floor(log2((5h/64)^{1/3})), no homogeneous two-label two-filler quadruple remains at any h. With E' = 0 the filler window is about 1880 rows; homogeneous Fo/Fo is then absent for h < 419431 and Fe/Fe for h < 2.7·10^7.

(iii) Proved to carry over to LAD:
- no Pythagorean filler pair;
- S2 (Theorem 1(2b));
- no filler right angle, so no Pc, Pb, X1 or X2;
- CE;
- T1;
- the SAW* Feo kill;
- no M2c with two fillers;
- no ll/FF and no FF/ll (a new general parity proof; FF/ll needs i mod 64);
- the d > 0 family is finite.

(iv) The cost is a factor of 2 in classes.

PROPOSITION 5 (exact reductions, proved; counts open).
- Fillers in rows that differ by e: 4du(p - 2D) = (p - 4d)(p^2 + D^2), with D = d + e. So u is a rational function of (p, d), with c = p - 2D | 10(d-e)(d+e)^2 and d | gamma(gamma^2 + e^2), where gamma = c + 2e.
- Cross block, with fillers in one row and inter-label vector (Lx, Ly): Y1 = (P - 2Lx)(P^2 + Ly^2)/(4Ly(P - Lx)).

## Proofs

Notation. Write v2 for the 2-adic order, delta = v2(d) and pi = v2(p). Two identities hold:
- (E1) pq = v^2 - u^2 = -d(2u - d), since v = u - d.
- (E2) p^2 + d^2 = 4d(p + q + u), which is |U - V|^2 = 4(L2 - L1)·U from Lemma mixedeq written in these units.
Both were checked against saw_residual_families.md (iii-b), and eliminating q from them gives F.

THEOREM 1, necessity. By (H2), F1 and F2 have the same type: v = u - d = u (mod 8), and L2's row is congruent to L1's mod 16.

Case 1: both fillers are holes, so x1 and x2 are even and u = 2 mod 4.
- Whether x1 = 0 or 2 (mod 4), p + q + u = 2 (mod 4), so v2(RHS of E2) = delta + 3.
- v2(2u - d) = 2, so v2(pq) = delta + 2.
- In E2, 2pi < 2delta forces pi = (delta+3)/2 with delta odd and >= 5. 2pi > 2delta forces delta = 3. pi = delta forces delta = 2, which is impossible.
- If delta = 3, then pi >= 4, so v2(q) = 5 - pi <= 1. That makes x1 = (p+q)/2 odd or non-integral, which contradicts x1 even.
- So delta = 2j+1 with j >= 2. Then v2(q) = j+1 and v2(p) = j+2, which give v2(x1) = v2(x2) = j and hence offset 0.
- The filler slots differ by 2d - p. Here v2(2d) = 2j+2 > j+2, so this difference has order exactly j+2.

Case 2: both fillers are bases at offsets 1 and 3. Then p = 2 (mod 4), so v2(p^2 + d^2) = 2, while the right side of E2 has order >= 5. This is impossible.

Case 3: both fillers are bases at the same offset. Then q = 2 (mod 4) and p + q + u = 2 (mod 4), so (E2) gives (delta = 3, pi >= 4) or (delta >= 5, pi = (delta+3)/2). (E1) gives pi + 1 = delta + v2(2u - d) >= delta + 3. That rules out the second option and leaves delta = 3 with pi >= 5.

Parameters. Use m = p/d = alpha/beta with gcd(alpha, beta) = 1, so v2(alpha/beta) = pi - delta. This is 1 - j on the hole branch, which gives alpha odd and v2(beta) = j - 1. It is >= 2 on the base branch.

Converse. With the vector w = (b(a^2+b^2), (a-4b)(a^2+b^2), b(-3a^2+8ab+b^2), a^3-4a^2b-3ab^2+4b^3, 4b^2(a-2b)), where a = alpha and b = beta:
- A prime dividing g cannot divide beta. It must divide 4(alpha - 2beta) and alpha^2 + beta^2, so it is 2 or 5.
- With alpha odd, u_w is odd, so g is odd. Writing alpha = 2beta + 5gamma shows v5(g) <= 1. So g is 1 or 5.
- On 2 < m < 4 with kappa < 0, u and v are positive and d is negative.
- With lambda = 2·odd: v2(x1) = 1 + v2(beta) = j, v2(d) = 2j+1 >= 5, and v2(2d) >= 6. So both fillers are offset-0 holes in the single row T*-24, and L2 lies in the class.
- In SAW*, u = 2 or 6 (mod 16), set by T mod 4. Since u_w/g is odd, a residue of lambda mod 16 exists that matches it.
- The grid conditions reduce to two facts. The q-corner row is R + 2d < R. The p-corner row y_L1 + 2d >= y_L2 >= 1.
- V != ±U because d != 0 and u, v > 0.

Theorem 1'. Work in original units with t = i2 - i1: P = X1 - X2, Qs = X1 + X2 and Y1 odd. Then P·Qs = -4t(Y1 - t) and P^2 + 4t^2 = 8t(P + Qs + Y1). The odd factor on the right forces tau = v2(t) odd, pi = (tau+3)/2 and v2(Qs) = (tau+1)/2. Hence v2(X1) = (tau-1)/2 and the slot order is (tau-5)/2. The slot gap t - P/4 has order (tau-1)/2.

Lemma 2. On [2, 4], |m^3 - 4m^2 - 3m + 4| >= 8, so v_w >= 8beta^3/5. With |lambda| >= 2, L2 lies 4·lambda·v_w >= 64beta^3/5 rows below the filler row, and beta >= 2^{j-1}. For Fe/Fe, lambda has 2-order -2, which gives the same bound with beta >= 2^{j+2}.

Theorem 3. On level j the slot gap is 2d - p, which is divisible by 2^{j+2}. If P' | beta, then p, d, x1 and x2 are all divisible by P', because each component of w is divisible by beta and g is coprime to P'. So when j+2 >= E, the two slots are congruent mod the period and share a row.
- For j < k the slots are not class slots.
- For j >= k they are class slots, because v2(x1) >= k.
- Lemma 2 gives where each level first appears.
- The clique: class slots with level j in [k, J] need rows separated across tau''-differences of order j - (k-2) - ... Concretely, the set {4m : m < 2^{J-k+1}} has pairwise differences of order in [2, J-k+2], so the separation requirement is a clique.

Theorem 4.

(i) Staircase property. Each pair type was checked by hand (the cases are listed in Checks), and ladder_check.py confirms it exactly over two periods. Writing the rows as T*-24-32phi, the pair constraint becomes v2(dphi) = v2(dtau) or dphi = 0. Each sub-ladder is a mod-4 staircase in its own variable, and the class part is a mod-2^{E'} staircase. Cross-type pairs have the right order because the residues phi mod 2^{v2(tau)+1} are 1, 2, 4, 8 and 0.

(ii) Kill.
- Level j <= 5: F1 sits at tau1 with v2(tau1 - tau_L) = j - 2, and F2 sits at tau1 + 2^j·odd. The variable of the relevant sub-ladder then moves by 2·odd, which is nonzero mod 4.
- Class levels: tau'' moves by 2^{j-4}·odd, which is nonzero mod 2^{E'} exactly when j < E' + 4.
- Fe/Fe tau = 7: the gap is 8·odd, so tau2 moves by 2·odd and the offset-2 row changes.
- Fe/Fe tau = 5: removed because v2(t) >= 6 under i mod 64.
- The bases cannot carry a kill. Two bases 4·odd apart would need v2(dy) = 5. That moves f' by 2 mod 4 (V-vertex Feo), or makes v2(y_V - y_P) >= 6 (P-vertex Feo). This is why i mod 64 is used.
- Theorem 1 says every homogeneous solution is on one of these levels, so none remains.

(iii) The results that carry over.
- Pythagorean pairs. For a filler pair, v2(dY) = v2(g) + 1, so delta^2 + 4m^2 = 4^a·(5 mod 8), which is not a square.
- Right angles. 16·g1·g2 has order 4 + v2(g1) + v2(g2), while dy1·dy2 has order 6 + v2(g1) + v2(g2).
- Pc. v2(a) = v2(dy) - v2(gamma) - 1 = 2.
- CE. v2(dy) = 3 + v2(g) <= 3 + v2(g).
- T1. With v2(e) != v2(delta), e = ±delta is impossible.
- S2. The proof uses only parity and the two base rows, which LAD keeps.
- Feo. The base rows are unchanged, and every hole row satisfies v2(y - y_P) = 3.
- M2c with two fillers, with b = v2(Delta) = v2(e) now arbitrary >= 2. If c = b, the orders are 3b against 2b+1. If c = b+1, they are 3b+2 against 2b+1. Neither can match.
- ll/FF. Here 2x1 + u = (5d - 2g - e)/2. The norm gives v2(g) = v2(d) = a >= 4, so the left side has order a - 1 >= 3. Parity makes it 2 mod 4.
- FF/ll. Here 5d^2 - d(2g+e) = -2(x1·g + u·e), which needs v2(x1·g' + 2u·e') = a - 1. Bases and offset-2 holes are excluded. Offset-0 holes with v2(x1) >= 3 force a = 3. Level-2 holes need e != 0 at gap order a, which in LAD happens only for a = 4. Under i mod 64, a >= 5.
- d > 0 family: 2d <= H0 bounds the number of shapes.

Proposition 5. Multiplying by p and substituting pq = -D(2u - D) collapses the equation to (p - 4d)(p^2 + D^2) = 4du(p - 2D). Reducing it mod c and mod d gives the two divisibilities. The cross-block form is the same elimination with (2d, d) replaced by L.

Rival pairs with the class staircase (SKETCH, not audited). Let F be a class-slot filler and E an even label on the line y = x/2 + c. Then E - F satisfies delta^2 + 2j·delta - 4j(A_F + j) = 0 with A_F = y_F - x_F/2 - c. So each (F, j) admits at most 2 values of delta, and only when j(5j + 4A_F) is a square. The A_F of one block are distinct. Counting the squares s^2 = 5j^2 (mod 4j) in a window gives at most C·W·(sqrt h + sqrt W)·h^eps pairs per block, about h^{5/6+eps}, where W is the class window, about 7h^{1/3} rows. That is relocatable.

## External results used

- Weak approximation on P^1(Q), that is, density of Q in R x Q_2 x Q_l. It is used only for the existence claims, and explicit (alpha, beta) are given anyway.
- Repository inputs: Lemma mixedeq (sec2_prelim.tex); saw_residual_families.md (iii-b), with the cubic F, the parametrization and SAW*; deep_layer_sawtooth.md and its audit, with Theorem 1, Lemma 2 (CE), robust Pc, Lemma 3, Proposition 5 (T2) and the Feo analysis (SAW* kill); deep_layer_bh16.md A2 (witness form); block_sea_classification.md (V1-V5, the M2c equation in its audited form).

## Checks

Every script is in scripts_layer_no_cubic/. I ran each with py, one at a time, each under 60 s and far under 1 GB. The repository was not touched; the census solver was copied as fofo_cubic_copy.py so that no numba cache was written into the archive.

classify.py (the census solver against the predictions of Theorem 1):
- SAW*, i mod 32, h = 20481, iota = 1: 9 hits, 0 mismatches. The shapes are alpha/beta = 5/2 (3 hits), 7/2 (3), 13/4 (2) and 15/4 (1).
- SAW*, h = 5121, iota = 1, 3, 5: 3 hits, all 5/2.
- SAW*, i mod 64, h = 20481: 6 hits, 0 mismatches.
- SAW, i mod 16, h = 10241: 14 hits. The 3 'mismatches' are exactly the base branch (v2(d) = 3, alpha/beta = 8/3 and 16/5, fillers at odd offsets), plus the d>0 shape 12/1. This is as Theorem 1 predicts.

classify_ee.py (Fe/Fe):
- SAW*, i mod 32, h = 2561: 20 hits. 18 have v2(t) = 5 with base fillers and 2 have v2(t) = 7 with offset-2 fillers.
- i mod 64, h = 5121: 4 hits, all with v2(t) = 7 at offset 2.
- 0 mismatches against Theorem 1'.

node_branch.py 256 1e8. Every shape with alpha odd, beta even <= 256 and 2 < alpha/beta < 4 was placed in a SAW* region and checked from scratch against Lemma mixedeq: perpendicularity, equal lengths, D-C != ±(B-A), and all rows >= 1. There were 0 failures. The weights sum 1/u, for v <= 1e8, are:
- level 2: 4.28e-2;
- level 3: 1.91e-2;
- level 4: 7.89e-3;
- level 5: 1.33e-3;
- level 6: 3.2e-4 (the sums for levels 5 and up are truncated by beta <= 256).
The smallest height needed is 4043 (level 2, which is 7/2, the 53:101 shape), 5515, 38923, 240651 and 731659 for levels 2 to 6. At levels >= 6 (the class levels under the i mod 64 split) both filler slots are class slots.

ladder_check.py:
- E' = 0: 0 staircase violations over all pairs with one end in the first 1024 slots. Offset-0 rows are T*-24 mod 32 and offset-2 rows are T*-8 mod 32.
- Same-row placements at levels 2 to 5 (851712, 422400, 218112 and 100352 placements): 0 in LAD, all of them in SAW*. Class levels 6 to 9 stay in one row in both.
- E' = 4: levels 6 and 7 are killed and level 8 survives, which matches j < E' + 4. The deepest row is T*-7704.

inhom_count.py (no congruences). For X = 500, 1000, 2000, 4000, e = 0 gives 624, 1310, 2709, 5568 solutions (linear). For X = 1000 and 4000:
- e = 2: 186 and 378;
- e = 8: 349 and 709 (503 at X = 2000);
- e = 32: 422 and 985;
- e = 128: 262 and 938.

The 2-adic proofs of Theorems 1, 1' and 4(iii) were derived by hand once, not independently. I re-derived the closed form of Proposition 5 by hand and checked it against F at e = 0.

## Gaps

- LAD's full validity is not proved. Re-proved for LAD: no filler Pythagorean pair, S2, no filler right angle (so no Pc, Pb, X1 or X2), CE, T1, the Feo kill, no M2c with two fillers, no ll/FF or FF/ll, and finiteness of the d>0 family. NOT re-proved: (1) pure-gap mixed quadruples with four fillers. The SAW proof used heights <= 6 Y-units and a bounded enumeration; LAD's heights reach about 450 Y-units and more. (2) Theorem 1(6), the one-label families with three fillers. Its case |k|<|e| used that (e/k)^2-1 is never a square for |e| <= 6. LAD has filler pairs with e = 10, 26, ..., which are hypotenuses, so a linear thick family may appear. A possible fix is to lift the ladder values, phi(r) = r + 4·m_r, so that no filler-pair e is a hypotenuse; this was not done. (3) Parked triples and V3 (with more filler rows). (4) Junctions and the brute-force census. Every window big enough to test LAD needs h > 3700.
- Inhomogeneous counts (fillers in two rows) are not proved. Proposition 5 reduces them to a two-variable mutual-divisibility count. Numerically, without slot congruences, the count grows like sqrt(X) for e != 0 (e = 8: 349, 503, 709 at X = 1000, 2000, 4000), while e = 0 grows linearly. An h^{1-delta} bound per filler row pair is what is needed. LAD turns every killed homogeneous configuration into an inhomogeneous candidate, so this count matters more under LAD than under SAW*.
- The cross-block two-label quadruple is not counted. Only its closed form (Proposition 5) is new.
- The rival-pair bound with a class window W ~ h^{1/3} is a sketch. The note's proved bound (i) becomes vacuous for H0 ~ h^{1/3}. The sketch relies on the distinctness of A_F and a residue count for s^2 = 5j^2 mod 4j, and both need an audit. The non-class part (H0 ~ 1880) is covered by bound (i), with a constant of about H0^{5/2}.
- With a bounded window (E' fixed), Theorem 3 leaves the class-level node branch. It has weight sum 1/u of about 3e-4 at j = 6 (truncated at beta <= 256) and first appears at h about 7·10^5. It still needs a colouring of its ratio graph, or the h-dependent staircase.
- The lower bound of about 0.03·h^{1/3} distinct class rows is a clique bound on the separation graph. It does not prove that every such pair would actually be fatal for every label set.
- Theorem 3 is stated for layers whose rows are periodic in the slot. Layers whose rows depend on the class colouring were not analysed; a bounded set of rows reduces the load only by a constant factor (heuristic).
- Nothing here is audited. M2c with one label and one filler (saw_residual_families.md (ii)) and V3 among parked triples stay open as before.

## Missing estimate

Three estimates would finish this route.

(1) A full validity proof for LAD_6(E'(h)). Two parts are missing:
- (a) No four-filler mixed quadruple. Every filler pair has the exact staircase property v2(dy) = 3 + v2(slot gap) or dy = 0. A 2-adic argument alone does not exclude the quadruple, as the derivation of gamma(G1-gamma) = -4·zeta(Z1-zeta) shows. A height-based argument is needed.
- (b) Theorem 1(6) for LAD's row differences. Lifting the ladder values so that no filler-pair e is a Pythagorean hypotenuse would restore the "never a square" step.

(2) #{(p, d) : |p|, |d| <= h, 4d(p - 2d - 2e) | (p - 4d)(p^2 + (d+e)^2)} = O(h^{1-delta}) for each fixed e != 0 (numerically about C·sqrt(e·h)). Equivalently, count the pairs (d, gamma) with d | gamma(gamma^2 + e^2) and (gamma - 2e) | 10(d-e)(d+e)^2. The only polynomial branch I found is gamma = 0 (p = 2d), which contributes O(sqrt(e·h)).

(3) The same kind of bound for the cross-block form Y1 = (P - 2Lx)(P^2 + Ly^2)/(4Ly(P - Lx)), with L ranging over the label vectors between two blocks.

## Next steps

- Audit Theorems 1, 1', 3 and the kill part of Theorem 4. They are short valuation arguments plus the gcd(w) in {1, 5} lemma. Record the corollary that SAW* d<0 shapes are exactly alpha odd, beta even, 2 < alpha/beta < 4, and that no class split or label residue removes them.
- Decide between two routes. One is to colour only the node-branch ratio graph: levels >= 6, edges with v2(t) = 2j+2 >= 14, and weight below 1e-3 per label. The other is LAD with E'(h) of about (1/3)log2 h - 3, which needs the class window of about 7h^{1/3} rows and the rival-pair sketch.
- For LAD, lift the ladder values (phi(r) = r + 4m_r is free) so that no filler-pair row difference e (Y units) is a Pythagorean hypotenuse. Then redo Theorem 1(6) and the four-filler pure-gap bound with the staircase property.
- Prove the inhomogeneous count N_e(h) = O(h^{1-delta}) through the mutual divisibility d | gamma(gamma^2+e^2), (gamma-2e) | 10(d-e)(d+e)^2. Show that gamma = 0 is the only polynomial branch.
- Extend fofo_cubic to per-slot filler rows and run an exact LAD census of Fo/Fo and Fe/Fe, both homogeneous and inhomogeneous, at h of about 2·10^4.

