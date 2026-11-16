# The threshold families under a random prime modulus

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: with the rigid modulus 16 l for a random prime l near h, the mixed quadruples I.2 and II hit B h^(1+o(1)) labels in expectation. Cross-class M2c reduces to one count N_h, which is open. Not audited yet.

# Result

## Status

partial

## Summary

Swapping the 2-adic rigid modulus for 16*l, with l a random prime in (1.04h, 2.08h] and l = ±2 (mod 5), keeps Theorem C. Over random (l, p), I.2 and all of type II with Sigma != 0 then hit B' h^{1+o(1)} labels in expectation (proved, not audited). In every rigid layout, cross-class M2c reduces to one layout-free Diophantine count N_h, which is open. V3 has only a structural lemma.

## Statements

NOTATION. L* as in sea_census_rigid.md. B' = the class bound per diagonal in a region type. A2/A3 below are the classes of pairs (l, p) defined there. "Labels hit" = the labels in some quadruple of the family.

LEMMA 0 (the cheap randomizations do not help in L*; proved). Take L* with any fixed p, and look at I.2 or II. Every realized quadruple has |Dt| < 2^nu, where Dt is the block-position difference. Hence Dt is the centred residue of p^{-1} Ds (mod 2^nu), and the set of realized diagonal-level tuples (T0, T', Dt, shape) depends on p alone.
- A random kappa changes nothing, because N is independent of kappa.
- Random period indices, or a random class order, change only which of the at most B' classes of T' sits at offset Dt from a given class of T0. That is a factor of at most B'.
- One prime per region leaves the expectation unchanged, by linearity.
So none of the suggested modifications improves the first moment of these families beyond a constant factor. In L*, Sum_p #realized(p) <= #{(sigma, n2) : 2^(nu+1) | Ds + U n2/(8a)}. This is a deterministic count with a fixed CRT condition, and its trivial bound is h^{2+o(1)}. That is the "one factor 1/h" of the note.

LAYOUT L*_l. Same as L*, except that the rigid rule is n(c) = s_c - M_c = kappa (mod 16 l), with M_c in pZ. Here l is prime, l in (1.04h, 2.08h] and l = ±2 (mod 5); p is in (20h, 40h] with p = 3 or 7 (mod 20).
PROPOSITION 1 (compatibility; proved):
(a) Width per region type <= 4p * 16 l * B' + 4A <= 5330 h^2 B'. Each residue mod 16l holds at most one diagonal. This is a constant factor, about 33 times the SAW type width.
(b) Theorem C holds: no tilted right angle among label points, and no rival pair. The proof uses rigid Theorem 2(e) for the l-part and the unchanged mod-p classification.
(c) II(-1,-1) with Sigma != 0 stays empty, by an l-adic version of B1. II(1,1), II(1,-1) with Sigma = 0 and II(-1,-1) with Sigma = 0 stay empty, by mixed_quadruples 4(a)-(d) and the residues of p.
(d) SAW Lemma 4(b) (no even-even cross-block A2 pair) holds, using (5/l) = -1. Lemma 4(a), Corollary B (it needs nu >= 2) and every intra-class result (R_IV, T2, in-class even-even M2c) are unchanged.
(e) LOST: B3's (C1) kill of even-even M2c across classes, and B3's law across classes. Both need 2^nu >= K.

THEOREM 2 (I.2; proved). Draw (l, p) uniformly from the admissible pairs. Then E[#labels hit by I.2] <= B' h^{1+o(1)}, where o(1) comes from max tau(n), n <= 2h^2.

THEOREM 3 (type II with Sigma != 0, every role, so II(1,-1) included; proved). The skeleton count is #skel_II <= h^{2+o(1)}. In L*_l, E[#labels hit by II] <= B' h^{1+o(1)}.

COROLLARY 4. By Markov and a union bound, some admissible (l, p) has I.2 and II together hitting O(B' h^{1+o(1)}) labels. The relocation rule absorbs them in width h^{1+o(1)} tau*(h)^2 = o(h^2).

PROPOSITION 5 (cross-class M2c reduction; proved). Let N_h be the number of integer 4-tuples (n1, w, e, u2) with n1 != 0, e, u2 >= 1, e + u2 <= h - 1, the identity e w u2 = n1(e^2 + (n1 + w)^2), |Delta| >= 78h for Delta = e u2/n1 - w, and the shallowness conditions. N_h is layout-free. In L*, and in L*_l, for every parity combination, E_p (or E_{l,p}) of the labels in cross-class M2c is O(N_h log h). Trivially N_h <= h^{2+o(1)}. Needed but OPEN: N_h <= h^{2-delta}.

LEMMA 6 (V3 structure; proved). A parked SLL triple (Pa, Pb or Pc) is determined by its white corner W together with one label corner adjacent to W: F or G for Pa and Pb, G for Pc. So two distinct parked triples at one W have disjoint adjacent-label sets. This alone does not bound V3.

## Proofs

Conventions. Points and equations are those of the notes. mixed_quadruples Thm 3 (s = 4): n2 = 8a(Ds - 2DM)/(10a + T0), with DM = p Dt and Dn = Ds - DM = N. The fixed facts are:
- |a| < h/312;
- |T0|, |T'| < h and |n2| <= h - 1;
- U := 10a + T0 is odd and nonzero;
- p > 20h, so any nonzero integer below (20h)^2 has at most one prime factor in (20h, 40h];
- likewise, any nonzero integer below (1.04h)^2 has at most one prime factor in (1.04h, 2.08h].
#p >= (1/4 - o(1)) 20h/log h (residues 3, 7 mod 20), and #l >= (1/2 - o(1)) 1.04h/log h (residues ±2 mod 5), by the prime number theorem in progressions (the same non-explicit input the notes already use for p = ±2 mod 5). So #l #p >= c h^2/log^2 h.

LEMMA 0.
- I.2: from B2, |a|(320|Dt| - 18) < h, so |Dt| < h/300 < 2^nu.
- II: E2 gives U1 = -H U2/(4 Sigma) with |H| < 2h and |U2| < h. So |4 DM| <= |U1| + 4h <= h^2/2 + 4h, hence |Dt| < h/150 < 2^nu.
Rigid: p Dt = DM = Ds (mod 2^nu), so Dt is the centred residue of p^{-1} Ds, which is fixed by (Ds, p). The I.2 and II equations contain only T0, T', Ds, Dn, Dt and the slot data, not kappa or the period index. Placing classes in periods only decides which class of T' is at offset Dt from a class of T0, which is at most B' pairs per tuple. Expectation is linear over regions.
- Last claim: the I.2 identity (below) gives N = (Ds + U n2/(8a))/2. In L*, N = 0 (mod 2^nu) is a fixed congruence. Each (sigma, n2) is realized for at most one p, because p | Ds - N.

1. THE I.2 IDENTITY. Since Ds - 2DM = 2N - Ds: (10a + T0) n2 = 8a(2N - Ds). So N = (Ds + U n2/(8a))/2. With g = gcd(U, a) (U is odd), 8a/g divides n2.

2. PROPOSITION 1.
(a) Positions are t = p^{-1}(s - kappa) (mod 16l). Since 16l > h > the range of s, residues hold at most one diagonal. The k-th class of a diagonal sits at rho_s + 16 l k, with k < B'. Columns are at most 4p * 16 l * B' + 4A, and 4 * 40h * 16 * 2.08h = 5325 h^2.
(b) Derivation 2, part 3 (audited) reduces every tilted right angle among label points to the cross-block (E;O,E) type. It uses only M in pZ and p > 20h. Then N = Dn = 0 (mod l), and N != 0 because |DM| >= p > |Ds|. So N has the prime factor l > 1.035h, and rigid Theorem 2(e) gives no configuration. Rival pairs are as before.
(c) C3/B1: Dj(5 Sigma - S) = 4 Sigma Dn, with S = s0 + s' + 1 and |S| <= h - 1.
- If Dj != 0: l | Dj(5 Sigma - S), and |Dj| <= K - 1 < l. So l | 5 Sigma - S. But |5 Sigma - S| < 5h/152 + h < 1.04h < l, so 5 Sigma = S. Then 4 Sigma Dn = 0, so Sigma = 0, a contradiction.
- If Dj = 0: Sigma Dn = 0, so Sigma = 0, a contradiction.
The other cases use only the residues of p.
(d) In SAW Lemma 4(b), the A2 equation f1(f1 + 4 delta) = eps^2 holds, with eps - delta = n(c') - n(c) = 0 (mod l). Mod l this becomes (f1 + 2 eps)^2 = 5 eps^2. With (5/l) = (l/5) = -1 we get l | eps, and |eps| < K < l, so eps = 0, which is the lemma's conclusion. Corollary B and deep_layer A3 need only the rule mod 4, which 16l keeps.
(e) B3 uses v2(Dn) >= nu > v2(e), and that is lost when the 2-power is 16.

3. THEOREM 2. A skeleton is sigma = (a, T0, T', b) satisfying E1. For fixed (a, T0), the map (T', b) -> (2b + T', 4b) is injective into the representations of N_a = 16a^2 + (2a + T0)^2 < 2h^2 as a sum of two squares. So there are at most r_2(N_a) <= 4 tau(N_a) skeletons.
For each sigma, the admissible n2 are multiples of 8a/g with |n2| < h, at most hg/(4|a|) + 1 of them.
Each (sigma, n2) fixes N, which is nonzero with |N| <= (h + 1.1h * h/16)/2 < h^2/14 < (1.04h)^2. Realization needs 16l | N and p | Ds - N, with |Ds - N| < (20h)^2. So each (sigma, n2) is realized by at most one pair (l, p).
Since Sum over T0 of gcd(a, T0) <= 3h tau(a), we get Sum_{l,p} #realized <= max tau * Sum_a Sum_T0 (h gcd(a, T0)/(4|a|) + 1) <= h^{2+o(1)}.
Each realized tuple fixes T0, T' and Dt, which gives at most B' class pairs. Each class pair gives one translation family (iC - i0 is fixed by E2) of at most A quadruples, so at most 4A labels. So E[labels] <= 4A B' h^{2+o(1)} log^2 h/(c h^2) = B' h^{1+o(1)}.

4. THEOREM 3. Let g = C - A = (4d, eta) and g' = D - B = (4d', eta'). Put Sigma = d + d', Dd = d' - d, H = eta + eta' and De = eta' - eta.
- E2 (U.(g + g') = 0) gives 4 Sigma U1 + H U2 = 0.
- E1 (2U.(g' - g) + G = 0) gives 2U2(De Sigma - Dd H) = -Sigma(16 Dd^2 + De^2).
Multiplying by 16 Sigma and completing squares gives the exact identity
 X^2 + Y^2 = U2^2 (H^2 + 16 Sigma^2), with X = 16 Sigma Dd - U2 H and Y = 4 Sigma (De + U2).
Because U1 = 4(Dj - Dn) is a multiple of 4, we need 16 Sigma | H U2. U2 = 2Dj + T0 is odd, so the right side is positive and at most 5h^4.
For fixed (Sigma, U2, H), the map (Dd, De) -> (X, Y) is injective, so there are at most r_2 <= h^{o(1)} skeletons. The number of triples with 16 Sigma | H U2, |Sigma| < h/152, |U2| < h and |H| < 2h is at most Sum_Sigma (8h^2 tau(16 Sigma)/(16|Sigma|) + 2h) <= C h^2 log^2 h.
(Sigma, Dd, H, De, U2) recovers (d, d', eta, eta', U2), hence T0, T' and Dj. So #skel_II <= h^{2+o(1)}.
E2 then fixes Dn = Dj + U2(Sigma - Ds)/(8 Sigma), with |Dn| <= h/2 + h^2/8 < (1.04h)^2 and Dn != 0. So each skeleton is realized by at most one (l, p). k = Dj - Ds is fixed, so a family is a translation in iA, with at most 4A labels. The same arithmetic as in Theorem 2 gives B' h^{1+o(1)}.

5. PROPOSITION 5. From the audited M2c equations, B3 writes (I1) e u2 = n1(Delta + w) and (I2) (Delta - 2n1) w = e^2 + n1^2. Then (I2) gives Delta = 2n1 + (e^2 + n1^2)/w. Substituting into (I1) gives e u2 w = n1((n1 + w)^2 + e^2), and so Delta = e u2/n1 - w.
Cross-block means |Delta| >= 4(p - A) >= 78h. A shape fixes B's row (one slot index of B), D's row, and Delta.
- Odd-odd: DM = Delta/4 - (iD - iB) is fixed. This needs p | DM: at most one p, since |DM| < h^2/8. Then j_B is free (at most K values), and s_D is forced by the rigid rule.
- Even-even: Dn = (jD - jB) - Delta/4 is fixed, which needs 16l | Dn, or 2^nu | Dn in L*. Then Ds is forced mod p, so it is unique, and s_B is free.
- Mixed parity: the rigid rule fixes the free index of one label, and p | DM fixes the other's, up to at most h values each with at most one p.
In every case Sum over the random primes of #instances <= K N_h. So E[#instances] <= K N_h log h/(c h) = O(N_h log h), and each instance hits 2 labels. The trivial bound N_h <= h^{2+o(1)} comes from fixing (n1, e), which leaves w | n1(n1^2 + e^2).

6. LEMMA 6.
- Pa and Pb: the angle at W is right, so G is on the line through W perpendicular to F - W. Also E = F + G - W must be in the sea row, so y_G = r0 + y_W - y_F. F - W is neither horizontal nor vertical (the rectangle is tilted), so the line meets that row once.
- Pc: E is on the perpendicular to G - W through W, in row r0, so E is fixed in the same way.

## External results used

- Prime number theorem in arithmetic progressions mod 5 and mod 20, non-explicit; the notes already use it.
- Quadratic reciprocity: (5/l) = (l/5).
- r_2(n) <= 4 tau(n), and tau(n) = n^{O(1/log log n)}.

## Checks

Scripts are in the script folders of this directory. Each ran with py in under 60 s, and the repository was not touched.
- m2c_shapes.py and m2c_thr.py: a definition-level enumeration of M2c shapes, each re-checked against n1((Delta-n1)^2+e^2) = e u2(Delta-2n1).
  - span >= 78h: 0 shapes at h = 250, 500, 1000;
  - span >= 4h: 4 shapes (h = 250) and 42 (h = 500);
  - span >= 20h: 0 shapes up to h = 1000.
- m2c_max.py: confirms the parametrization by (n1, w, e) and the identity e w u2 = n1((n1+w)^2 + e^2), with an assert on every hit. The maximum Delta/h is 2.2 at h = 40 and 6.06 at h = 80.
- m2c_ratio.py: large-span shapes exist (Delta/(e+u2+1) up to 7818).
- m2c_cross_count.py: N_h = 0, 190 and 1558 at h = 5000, 20000 and 60000.
Theorems 2 and 3 were not checked numerically.

## Gaps

- Nothing here is audited. Every proof was checked once, by me only.
- Prop 1(b) is the step to audit first. It relies on rigid Theorem 2(e), proved in the rigid note but never audited, and on the audited Derivation 2 part 3.
- Prop 1(c) quotes C3 of cross_class_sea.md (unaudited, re-derived in sea_census B1).
- Prop 1(d) assumes that SAW Lemma 4(b) concludes eps = 0 from exactly f1(f1+4 delta) = eps^2 and eps = delta (mod modulus). I read that from the note's lines 94-96 only.
- L*_l was not checked against heavy_light_split / t1_cost_decomposition: the T1 heavy-block switch column, and anything else that may use 2^nu >= K/8.
- L*_l loses B3 (C1): even-even M2c across classes is no longer empty. It joins the N_h family.
- Proposition 5 needs N_h <= h^{2-delta}, which is NOT proved. Every one-parameter fixing gives h^{2+o(1)}, so a genuine two-divisibility or point-counting argument is needed.
- Numerics for N_h (definition-checked): 0 at h = 5000, 190 at h = 2*10^4 and 1558 at h = 6*10^4. That local growth is about h^1.9, likely an onset effect, and it is NOT evidence for h^{2-delta}. I found a structured subfamily e = m^2/c (m = n1 + w) of heuristic size h^{1+o(1)}.
- Large-span shapes do exist, for example Delta = 7818(e+u2+1) at e = 10186854, so cross-class M2c is not empty for large h.
- V3 among parked SLL triples is not bounded. Lemma 6 is only the structural first step.
- The prime counts #l and #p use the non-explicit prime number theorem in progressions (mod 5 and mod 20). No explicit h0 is given.
- Theorems 2 and 3 are first-moment bounds over random (l, p), not bounds for every prime. Their o(1) is max tau, not polylog; I did not optimise it.
- Lemma 0 shows only that the suggested randomizations leave the first-moment argument unchanged. It does not prove that I.2 or II actually hit h^2 labels in L*.

## Missing estimate

One count closes cross-class M2c in both layouts:
N_h = #{(n1, w, e, u2) : e w u2 = n1(e^2 + (n1+w)^2), e + u2 < h, e u2/n1 - w >= 78h} <= h^{2-delta}.
The heuristic is h^{1+o(1)}. Two divisibilities are implicit: e | n1(n1+w)^2 and w | n1(n1^2 + e^2). A hyperbola-method or determinant-method argument over the conics n1 e^2 - u2 e m + n1 m^2 + u2 n1 e = 0 (m = n1 + w) is the natural tool. For V3, a count of pairs of parked triples sharing W, using Lemma 6, is still needed.

## Next steps

- Audit Prop 1(b)-(d) and Theorems 2-3. They are short: the I.2 identity, the II conic identity X^2 + Y^2 = U2^2(H^2 + 16 Sigma^2), and the integrality 16 Sigma | H U2.
- Decide between L* and L*_l. L*_l turns I.2 and II into proved h^{1+o(1)} loads. In exchange, even-even cross M2c moves from empty to the N_h family, and cross odd-odd M2c needs N_h in both layouts.
- Check L*_l against heavy_light_split, t1_cost_decomposition and the SAW Corollary 6 cost line.
- Attack N_h <= h^{2-delta} with Vieta jumping on n1 e^2 - u2 w e + n1 m^2 = 0 (roots multiply to m^2), or with a dyadic split over (n1, e, w). Extend the m2c_cross_count.py census to h = 1.2*10^5 with a faster divisor routine.
- For V3: classify pairs of parked triples at one W by type (Pa/Pa, Pb/Pb and Pc/Pc only, since Pa and Pb have W columns that differ mod 4). Then reduce each pair type to a layout-free shape count, as in Proposition 5.

