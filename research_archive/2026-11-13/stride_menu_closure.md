# Closing the stride menu

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: at stride 4u, R_IV(u) with its Lemma IV weights and (B8) densities, the R_FF(u) cubic with its FF' analogue, the deep layer, the A4 shape counts, Theorem K and K7 all close by proof, and the three transfer notes agree once two small discrepancies are fixed. Theorem N_menu (several stride chains, one admissible pair per chain, each diagonal at its lightest stride, Theorem E for diagonals heavy at every stride) has no open mathematical hypothesis, but every new step still needs a second reader. Its exponent x_m (1.4295 for two strides) is conditional on those audits. Not audited yet.

# Result

## Status

partial

## Summary

At stride 4u, R_IV(u), its Lemma IV weights and (B8) densities, the R_FF(u) cubic with its FF' analogue, the deep layer, the A4 shape counts, Theorem K and K7 all close by proof, and the three transfer notes agree once two small discrepancies are fixed. Theorem N_menu has no open mathematical hypothesis; everything new still needs a second reader.

## Statements

Setting. u is odd. Delta_u = 4u^2 + 1 and P_u = max(40, 8u^2 + 4), so P_3 = 76. L***(u) is L***U (consolidated_board_v4) with these changes:
- (B1) and (B4) are taken at sigma = 2u.
- (B2'): l is prime in (1.04h, 2.08h] with (Delta_u/l) = -1. p is prime in (P_u h, 2P_u h] with p = 3 (mod 4) and (Delta_u/p) = -1.
- (B5'): rho_s = p^(-1)(u s - kappa) (mod 16l). The slot is n = u i + p t + b_tau and the column is 4n, so rho_tau = u(iota + sigma) - kappa_tau (mod 16).
At u = 1, L***(1) is L***U.

THEOREM R4 (exact R_IV(u); proved here, not audited). Every in-class odd-odd label-label M2c with shallow A and C in L***(u) is an edge (q m, p m), m odd, of R_IV(u). The pair (al, be) is coprime and odd with 0 < al < u be and v2(u be - al) >= 3. Put F_u = 4(al - 2u be)^2 + be^2, D0 = u be - al and g = gcd(F_u, D0). Then g divides Delta_u, q = al F_u/g, p = (al F_u + 4be^2 D0)/g, and Di = (p - q)m. In-class even-even M2c is empty.

LEMMA IV(u) (proved). The bounds are q > al be^2, p > 4u be^3/Delta_u and p <= (128u^3/27 + 4u) be^3. For every fixed C, the sums over lambda of tau(q)^C/q and of tau(p)^C/p are finite. The edges with max(p, q) > h^(1/2)/32 touch O_u(h^(11/6) log h) labels. q is odd, and every (B8) event is a union of residue classes of i mod lcm(32, q) <= h^(1/2). So (B8) and Theorem D (i), (ii) hold at stride 4u.

THEOREM FF(u) with LEMMA FF'(u) (proved). A same-row in-class 2L2F has side {L1, F1}, diagonal {L2, F2} and L2 - L1 = (4ut, 2t). Such a configuration satisfies (P - 8ut)(P^2 + 4t^2) = 8tY1(P - 4ut). For t < 0, Y2/Y1 = V_u/U_u at a/b = P/(2t), where:
- U_u = (a - 4ub)(a^2 + b^2) and V_u = a^3 - 4u a^2 b - 3ab^2 + 4u b^3;
- gcd(U_u, V_u) divides 8u Delta_u;
- the sums over shapes of 1/|U_u'| and of tau(|U'|)^C gcd(64, |U'|)/|U'| are finite;
- the tail over shapes with |U'| > W is O_u(W^(-1/3)), and the number of shapes with |U'| <= X is O_u(X^(2/3)).
For t > 0 (D12), |Di| <= 210. The old D3 (T2) is a point of this family; it needs no separate cell.

LEMMA DL (deep layer; proved, part (a) by the argument given in the proof). (a) Every obstruction with at most one label is stride-free. Its verdict depends only on the label's rows, on the slot residue n = rho_tau (mod 16) and on the (B6) filler law in n - rho0 (mod 4). (b) Every deep-layer item with two or more labels is re-derived at stride 4u from Lemma C (C1)-(C7) and U1(a), U1(d). So the deep layer is covered at stride 4u: stride_transfer_core is right, and the deep-layer gap in stride_transfer_ratio is resolved.

THEOREM K(u) (proved modulo the unaudited items below). Assume K8' in L***(u). Then every (V1)-(V5) violation lies in a cell of the merged table of v4 section 3 that is E, C or W. No cell is open. K7 holds at stride 4u with the constants of Lemma IV(u) and FF'(u).

PROPOSITION U(u) (proved). The A4 (I.2 and II), B7, D8, D17 and D18 shape counts hold at stride 4u. Each realisable shape fixes a nonzero integer below (1.04h)^2 or below (P_u h)^2, so at most one pair (l, p) realises it. Hence min over Adm_u of Y^(u) <= 512 C_u h^(9/5+2eps).

THEOREM N_menu (CONDITIONAL; hypotheses (N0)-(N9) are listed in the proof with their status). Take a menu U of odd u including u = 1, with no nonempty subset product of the Delta_u a square, for example {1, 3}. Build the board as follows:
- one chain L***(u) per u, each with its own minimising pair (l_u, p_u);
- a diagonal T is light iff min_u kappa_T^(u) < B/4, and it then goes to the least minimising u;
- a diagonal is heavy iff it is heavy at every stride;
- one Theorem E instance, one weighted Theorem D group with kappa = max_u kappa(u), and one Proposition partial instance;
- one switch z, with every chain a separate J5' window left of z.
Then M <= C h^2 (B + Lambda^(beta_m(a)+2) B^(-a) + Lambda^2/B) ell^C + C m h^2 ell + o(h^2). So m_h <= C h^2 (log h)^(x_m) (loglog h)^C, with x_2 = 1.4295234 for U = {1, 3}. NOT PROVED: m_h = O(h^2), and any unconditional exponent below 1.4967429.

## Proofs

0. RECONCILIATION OF THE THREE TRANSFER NOTES

All three notes, stride_transfer_core (core), stride_transfer_ratio (ratio) and stride_transfer_table (table), agree on the twisted rule (B5') and on the residue conditions (B2'). The census note used the untwisted rule. That is harmless, because its (S2) shows that cross-class families are empty at the heights it tested. Eight points needed a decision.

D1. The range of p.
- Core and ratio use (8u^2+4)h, and stride_menu_heavy_count uses max(40, 8u^2+4). The table uses 8u^2 + 8 (80h at u = 3).
- stride_menu Lemma 4 at s = 4u needs only p > (s^2/2 + 4)h = (8u^2+4)h, so I fix P_u = max(40, 8u^2+4).
- The table's thin margins were computed at 80h. At 76h the core's values hold instead: Proposition 1(c) needs 1.0216h, L-adic (i) needs 1.021h, and rigid Theorem 2(e) needs (1 + 37/1715)(h - 1) < 1.0216h.
- I re-derived the 2(e) bound. From c2(2 Delta t1 - T0) = 8u t1 N with |N| > (P - u)h and |c2| < h/2, we get |2 Delta t' - T'| > 16u(P - u)|t'|. So |b'| < (1 + Delta/(8u(P - u) - Delta))(h - 1). At u = 3 and P = 76 this is 1 + 37/1715.
- All three margins are below 1.04h < l. The general condition is 8u(P - u) > 26 Delta, which holds for every u.

D2. The g of R_IV(u).
- Ratio uses g = gcd(F_u, D0), and the table uses g_T = gcd(al F_u, 4be^2 D0).
- Section 1 proves that ratio's g gives the exact edge set.
- g_T is larger by a divisor of gcd(al, u), so the table's graph is a superset. A superset is harmless for upper bounds: its weights are at most u times larger.
- My check found g_T != g on 74 of 426 pairs (u in {1, 3, 5}, be <= 21), and only where gcd(al, u) > 1. Brute force over the integrality conditions matched ratio's formula on all 426 pairs.

D3. The content bound gcd(U_u, V_u).
- Ratio and the table give 8u Delta_u, and the census gives 2s(s^2+4) = 32u Delta_u. These are consistent; section 3 proves 8u Delta_u.

D4. The Feo kill.
- Core proves it from (C1)-(C4) alone. The table uses a different parametrisation with u. Both are valid; section 4 checks the core's version.

D5. The A4, D8, D17 and D18 shape counts.
- Core and ratio mark them open, and the table re-derives them.
- I confirm the table from mixed_quadruples Theorems 3 and 4, which are written for a general stride s and audited as A-3. See section 5.

D6. The deep layer.
- Ratio says it is not covered, and core says it carries over verbatim. Core is right; see section 4.
- Ratio's example, 'c_Q = c_P mod 2^(nu+1)' in saw (iii-a), is replaced by a proof that uses only (C1)-(C4).

D7. The lower bound on q.
- Ratio proves q > al be^2 exactly. The table's 'q >= c_u al be^2' is weaker and consistent with it.

D8. The upper bound on p.
- The table's p < (16u^3 + 5u)be^3 is valid but crude. The exact bound is p <= C_u(x, 1) be^3 <= (128u^3/27 + 4u)be^3 (section 2). At u = 1 this is below the 21 be^3 of v4 [F15].

1. THEOREM R4

Take B and D odd label points of one class, with A and C shallow in sea row r.
- In a class, D - B = (4u Di, 2Di), so e = Di and Delta = 4ue. In a type, Di = 0 (mod 32), so a = v2(e) >= 5.
- delta = v2(4ue) = a + 2, because u is odd. So in ratio_graph Corollary 5, tau = 2.
- sea_row3 Theorem A gives c = v2(y_B - r).
  - In row-1 types, iota is odd, so y_B = 2i + 1 = 3 (mod 4) and c = 1.
  - In row-3 types, iota is even, so y_B = 1 (mod 4) against r = 3, and again c = 1.
  - For even label rows, c = 0.
- ratio_graph Theorem 4 (audited, A-10, any stride, a >= 4) gives tau = c - zeta + 1. So odd-odd needs (c, zeta) = (1, 0), and even-even would need zeta = -1, which is impossible. So in-class even-even M2c is empty.
- With (c, zeta) = (1, 0), b = v2(n1) = a + 1, so r' := n1/e = 2al/be with al and be odd and coprime.

Integrality. The M2c equations are (I1) e u2 = n1(Delta + w) and (I2) (Delta - 2n1)w = e^2 + n1^2, with u2 = 2v and z = -(Delta + w) (audited block_sea Theorem 2).
- (I2) gives w = e(1 + r'^2)/(4u - 2r'). (I1) then gives v = al e F_u/(4be^2 D0).
- u2 > 0 and e > 0, so 0 < al < u be.
- The integer conditions are n1 = 2al e/be, v, and z = -v be/al. Then w is an integer automatically.
- gcd(be, 2al) = 1, so be | e. Also gcd(be, al F_u) = 1, because F_u = 4al^2 (mod be). So be^2 | e. Write e = be^2 e2.
- Then v = al e2 F_u/(4D0) and z = -e2 F_u be/(4D0). gcd(be, D0) = gcd(be, al) = 1, and F_u is odd, so z is an integer iff (4D0/g) | e2, where g = gcd(F_u, D0).
- So e2 = 4D0 m/g, and v is then an integer automatically. This gives v = q m, e = 4be^2 D0 m/g and v + e = p m.
- q is odd, so v odd forces m odd. v2(e) = 2 + v2(D0) >= 5 gives v2(D0) >= 3.
- Modulo D0, al = u be, so F_u = Delta_u be^2 (mod D0). Since gcd(be, D0) = 1, g | Delta_u.

Sanity check. The script in my script folder brute-forced the integrality conditions for u in {1, 3, 5} and be <= 21. It found 0 mismatches with this formula on 426 pairs.

2. LEMMA IV(u) AND (B8) AT STRIDE 4u

Bounds.
- |al - 2u be| > u be, so F_u > Delta_u be^2 >= g be^2, hence q > al be^2.
- p g = be^3 C_u(x, 1) with x = al/be in (0, u) and C_u(x, 1) = 4x^3 - 16u x^2 + (16u^2 - 3)x + 4u = 4x(x - 2u)^2 - 3x + 4u.
- C_u' has roots near 2u/3 (a maximum) and 2u. So on (0, u), C_u > min(C_u(0), C_u(u)) = min(4u, 4u^3 + u) = 4u. That gives p > 4u be^3/Delta_u.
- Also C_u <= max 4x(x - 2u)^2 + 4u = 128u^3/27 + 4u, which gives the upper bound on p.

Weights.
- tau(n) << n^eps, and there are at most u be values of al per be.
- Sum over lambda of tau(q)^C/q << sum over be of be^(-2+2eps) times the sum over al < u be of al^(-1+eps), which is << sum over be of be^(-2+3eps) < infinity.
- Sum over lambda of tau(p)^C/p << sum over be of u be · be^(-3+3eps) < infinity.

Tail at Y = h^(1/2)/32.
- max(p, q) = p > Y forces be > c_u Y^(1/3), which is about h^(1/6).
- An edge touches labels only if p m <= h, so be <= (Delta_u h/(4u))^(1/3).
- The labels with q | v on one diagonal number at most h/(2q) + 1.
- So the tail touches at most 2 · 2h times the sum over the tail lambda of (h/q + 1) labels. This is << h^2 times the sum over be > c h^(1/6) of (1 + log(u be))/be^2, plus h · u h^(2/3). That is O_u(h^(11/6) log h).

(B8).
- The vertex is v_f = i + (1 - r0)/2, which is affine in i.
- q is odd, so {q | v_f} is one residue class mod 32q inside the type, with density 1/q.
- The designated q-end is in Bad_split only if the partner is monochromatic, which has probability <= 2/B.
- So Theorem D (ii) holds with Q_T = {q_lambda} and c_q = multiplicity. Theorem D-weighted needs only kappa = sup over T of the sum over Q_T of c_q tau(q)^C/q < infinity.
- Theorem D (i) holds: Y ∩ T is a function of chi_{T,tau}. The independence is unchanged, since R_IV(u) is (l, p)-free (Lemma U3).

3. THEOREM FF(u)

The cubic. Use Lemma mixedeq with A = L1, B = F1, D = L2, C = F2 and Dv = (4ut, 2t).
- The general cubic P^3 - 2aP^2 + ((Y1-Y2)^2 - 4bY1)P - 2a(Y2^2 - Y1^2) = 0, at (a, b) = (4ut, 2t) and Y2 = Y1 - 2t, factors as (P - 8ut)(P^2 + 4t^2) = 8tY1(P - 4ut).
- All three notes' forms agree with this. The table's inhomogeneous form is (P - 8ut)(P^2 + w^2) = 8tY1(P + 2uw), and I re-expanded it.
- Put P = 2tm. Then Y1 = t(m - 4u)(m^2 + 1)/(2(m - 2u)) and Y2 = t(m^3 - 4u m^2 - 3m + 4u)/(2(m - 2u)), so Y2/Y1 = V_u/U_u.
- Since Y1 V_u' = Y2 U_u', Y1 = mu|U'| and Y2 = mu|V'|.
- n_y = t, and the corner F1 + n is in the grid, so t > 0 forces t <= h - y_F1 <= 210. That is D12, covered by R_FF^+ (Di = 0 (mod 32), so at most 6 neighbours on each side).

Content.
- U - V = 4b^2(a - 2ub).
- Let r be an odd prime dividing both. r does not divide b (else U = a^3 (mod r)), so r | a - 2ub, and then U = -2u b^3 Delta_u (mod r). So r | u or r | Delta_u.
- If r | Delta_u: a - 4ub and a + 2ub are r-units. With k = v_r(a - 2ub), a^2 + b^2 = (a - 2ub)(a + 2ub) + Delta_u b^2 gives min(v_r(U), k) <= v_r(Delta_u).
- If r | u: r | a, a^2 + b^2 is an r-unit, and min(v_r(a - 4ub), k) <= v_r(u).
- 2-part: b even makes U odd. a and b odd give v2(U) = 1. b odd and a even give v2(U) = 1 when v2(a) = 1, and when v2(a) >= 2 they give v2(gcd) <= v2(4b^2(a - 2ub)) = 3.
- So gcd(U, V) | 8u Delta_u. The script checked this for u in {1, 3, 5, 7, 9}, |a| <= 600 and b < 120.

Lemma FF'(u).
- Put k = a - 4ub != 0. Then a^2 + b^2 = (16u^2+1)(b + 4uk/(16u^2+1))^2 + k^2/(16u^2+1).
- A unimodal sum is at most 2 max + integral, so for each k the sum over b of 1/(a^2 + b^2) is at most 2(16u^2+1)/k^2 + pi/|k|.
- So the sum over shapes of 1/|U| is at most the sum over k != 0 of (2(16u^2+1)/|k|^3 + pi/k^2) < infinity. Since |U'| >= |U|/(8u Delta_u), the same holds for 1/|U'|.
- With exponent 1 - eps the same splitting gives the tau^C-weighted sum: per k it is << |k|^(-2+3eps), which is summable.
- Tail: split at |k| = W^(1/3).
  - The part with |k| > W^(1/3) is << W^(-1/3).
  - For |k| <= W^(1/3), the minimum of a^2 + b^2 is k^2/(16u^2+1) << W/|k|. The condition a^2 + b^2 > W/|k| leaves two b-tails with sum << (W|k|)^(-1/2), and summing over |k| <= W^(1/3) gives << W^(-1/3).
- Count: |k|(a^2 + b^2) <= X' needs |k| << X'^(1/3) and O(sqrt(X'/|k|) + 1) values of b, so O(X'^(2/3)) shapes.
- [G11]: on a type, depth Y - 2i - 1 (or Y - 2j - 2) moves in steps of 64, so the density of m | depth is at most gcd(64, m)/m.
- The modulus is lcm(32, m) <= h^(1/2) at the cutoff.
- R-e for FF is h^2 W^(-1/3) + h · h^(2/3) = O(h^(11/6)) at W = h^(1/2)/32.

D3. SAW Proposition 5 (T2) has in-class vector (-8t, -4t), which is the stride-4 slope. It is the shape 5:7, m = 3, of this cubic at u = 1. At stride 4u every same-row in-class Fo/Fo or Fe/Fe is a point of the cubic above, so D3 is part of D12/D13.

D14 (ll/FF in a class).
- |L2 - L1|^2 = 4 Delta t^2 with t = 32t''. |F2 - F1|^2 = 16Dmu^2 + 64Dw^2 with Dmu = Dw (mod 4) and |Dw| <= 3. Equal lengths give 256 Delta t''^2 = Dmu^2 + 4Dw^2.
- Dw odd gives 5 (mod 8). Dw = +-2 gives v2 = 2 against v2 >= 8.
- Dw = 0 makes Delta a square, which is impossible since (2u)^2 < Delta < (2u+1)^2.

D15. Dv = (4u Di, 2Di) is in 128Z x 64Z, which meets two_filler Lemma 1's hypotheses (Dx = 0 (mod 16), Dy = 0 (mod 32)).

4. LEMMA DL (THE DEEP LAYER)

(a) At most one label.
- The verdict of a configuration with at most one label (both points allowed) and fillers depends on:
  - the type constants (r0, y_P, tau_T, c_tau, T*);
  - the label's rows (2i+1, 2j+2) and its slot residue mod 16;
  - the filler law (B6) in n - rho0 (mod 4);
  - whether other columns that the configuration meets are label columns.
- Under (B5') and (C1), the first three are those of a stride-4 label of the same type and rows. b_tau is free, so every phase mod 16 occurs at stride 4.
- The last item matters only through the colour of a white corner W. In v4 every one-label E verdict is that no right angle exists, that W lies outside the grid, or a row (near-band) condition. Every parked verdict puts W in a shallow column or at a filler offset != 0. By (C1), label columns sit at offset 0, so neither kind of verdict depends on which offset-0 slots hold labels.
- This covers SAW Theorem 1 (1)-(6), Lemmas 2 and 3, J1*, (Phi), saw (i) and (ii), D-1L3F (Theorem 1(6), V2-4, S1L), FFo, FFe, S3-S5, S10-S13, D9, R-b and R-c, and sea_row3 Theorem A.
- Two caveats. I checked this against v4's verdict reasons and K4 constants, not by re-reading every source proof line by line. And the census note's (C2) instance (FFo with a label vertex, W in another label's column) is near-band, as this argument predicts.

(b) Two or more labels: each item, re-derived.
- Feo (core 5(ii); I re-derived it). Put g = n_V - n_P, t = n_Q - n_P and f = y_V - y_P. Then t = 0 (mod 16) by (C1), and f = 8(w + c) (mod 64).
  - Q-vertex: the dot product is even plus odd·odd, which is nonzero.
  - P-vertex: 16gt = -f(y_Q - y_P). At offset w in {0, 2}, v2(f) = 3 while v2(LHS) >= 9. At odd w, v2(f) is 4 or 5 while v2(LHS) >= 8. t = 0 means Q is P's own even point, and then fT != 0.
  - V-vertex: 16g(g - t) = f(y_Q - y_V). For w even, v2(f) = 3 against v2(LHS) >= 6. For w odd, v2(LHS) = 4, so v2(f) = 5 fails. If v2(f) = 4, then 1 = g(g - t) = f'(y_Q - y_V) = f' tau_T (mod 4), against f' tau_T = 3 by (C4): c = 1 needs w = 1, f' = 1 and T = 3 (mod 4); c = 3 needs w = 3, f' = 3 and T = 1 (mod 4).
  - The proof uses no slope, so ratio's 'c_Q = c_P mod 2^(nu+1)' is not needed.
- Foo, filler vertex. alpha1 alpha2 = -4e1e2 forces w = 2. e1 = e2 (mod 8) by (C2), and Dslot = 0 (mod 16) by (C1). That gives w'^2 + e1e2 = (Dslot/4)^2 = 0 (mod 16), so w'^2 = 7 (mod 8), which is impossible.
- Foo, label vertex. alpha(4u eps + DM) = -4e eps.
  - In a class, u alpha + e = alpha + e (mod 2), which is odd, so the equation fails.
  - Across classes, eps = 0 forces alpha = 0, a filler in a label column. Otherwise u alpha = -e (mod p) with |u alpha + e| < p, so u alpha = -e exactly. Then alpha DM = 0, so alpha = 0 and e = 0, which is impossible.
- Fee. Filler vertex: parity. Even vertex: 8 alpha(u eta - Dn_u) = -d eta with d odd.
  - In a class, 8u alpha = -d, a parity contradiction.
  - Across classes, l | Dn_u gives 8u alpha = -d (mod l). |8u alpha + d| <= u h/(2(P_u - 1.5u)) + h < 1.021h < l, so equality holds, again a parity contradiction.
  - eta = 0 forces alpha = 0.
- LLL (A1): Lemma 4 at s = 4u plus the 2(e) bound of D1.
- ll/FF: D14 above.
- v3 Proposition F.
  - F1: |delta| >= p - uA - O(1) forces n_x = 0.
  - F2 (odd-odd): Dx = 2u Dy + 4DM. Mod p, Dy(2u n_x + n_y) = 0, and |n_x| < h/(4(P_u - u)), so 2u n_x + n_y = 0. Then 4n_x DM = 0 and n = 0. The even-even version is the same mod l, using Dn_u in 16lZ.
  - F3 with n_y >= 1: |Dx| < 106h + 2 < 4(p - uA).
- BH16 A3: delta = u eps (mod 16) with u odd, so A1 excludes the pair.
- Lemma Q3 (3L1F). It uses only (L1)-(L3) and (Phi).
  - Odd-odd differences are (4(u Di + p Dt), 2Di), which lie in 64Z^2, because the slot difference is 0 (mod 16) by (C1) and Di = 0 (mod 32).
  - Even-even differences lie in 64Z x 32Z.
  - So Q3, Lemma N and the (K-a) to (K-d) residues transfer word for word.
- FFo/FFo at one W: same i in two classes gives x_L2 - x_L1 = 4DM with |DM| >= p, against |beta| < 3h/8.
- S2 uses (L1), and S6-S8 use A(ii) (core section 4(iv)). B3 uses A(iii) (table), D8 uses the same-i fact Dx = 4DM, and A2 and A5 use core sections 3 and 4(i).
Conclusion: the deep layer at stride 4u is covered.

5. PROPOSITION U(u) (the shape counts)

A4, I.2.
- mixed_quadruples Theorem 3 (general s, audited A-3), with s = 4u and the block offset sP Dc read as 4p Dt, gives n2 = 8ua(u Ds - 2DM)/U' with U' = 2 Delta_u a + T0. That is U' n2 = 8ua(2N_u - u Ds) with N_u = u Ds - DM, which is the table's identity.
- Skeleton count: E1 is |(4ua, 2a + T0)| = |(4ub, 2b + T')|. The map (T', b) -> (2b + T', 4ub) is injective into the representations of 16u^2 a^2 + (2a + T0)^2 < 2h^2, so there are at most 4 tau skeletons.
- n2 runs over multiples of 8ua/gcd(U', ua), and the sum over T0 of gcd(U', ua) is <= C h tau(ua). So the total over all pairs is h^(2+o(1)).
- Each (skeleton, n2) fixes N_u, which is nonzero with |N_u| <= h^2/(16u) + O(uh) < (1.04h)^2. It also fixes DM = u Ds - N_u, with |DM| < (P_u h)^2.
- 16l | N_u and p | DM, so at most one pair realises it.

A4, II.
- E2 reads 4u Sigma U1 + H U2 = 0 with U1 = 4(u Dj - Dn_u), so 16u Sigma | H U2.
- The identity X^2 + Y^2 = U2^2(H^2 + 16u^2 Sigma^2) gives r2 <= h^(o(1)).
- The triple count is <= sum over Sigma of (8h^2 tau(16u Sigma)/(16u|Sigma|) + 2h) = O(h^2 log^2 h).
- The skeleton fixes Dn_u, so at most one l.

B7, D17, D18 and D8.
- The shape fixes Dx and Dy. Then DM = Dx/4 - u Dy/2 for odd points and Dn_u = u Dy/2 - Dx/4 for even points (U1(d)). For D8, same i gives Dx = 4DM.
- Cross-class thresholds are lower bounds and only get stronger (|Dx| >= 4(p - uA) > 298h at u = 3).
- #P_u >> P_u h/log h: the conditions p = 3 (mod 4) and (Delta_u/p) = -1 have joint density 1/4, because chi_(-4) chi_(Delta'_u) is the character of Q(sqrt(-Delta'_u)), which is nonprincipal.

So Theorem U's averages hold with the same orders, and V4-2 gives min over Adm_u of Y^(u) <= 512 C_u h^(9/5+2eps).

6. THEOREM K(u) AND K7(u)

Section 0 (the kinds of obstruction) is stride-free; it needs only K8'.

K8' holds:
- label columns 4(u i + p t + b) are distinct, because within a class u i varies and across classes |p Dt| >= p > u|Di|;
- every double is a label column {2i+1, 2j+2};
- Theorem D/E blocks (N1) and Proposition partial are stride-free.

Section 1 (localisation).
- Margins and J5' are unchanged.
- J4 becomes 4(16lp - uA) > 2600h^2.
- Distinct diagonals occupy distinct residues mod 16l, because u is a unit mod 16l and |Ds| < h < 16l.
- Cross-class |Dx| >= 4(p - uA).

Section 2. (L1)-(L3) and (Phi) were checked in section 4(b).

Section 3. block_sea Theorems 1-2 concern points in columns = 0 (mod 4), and sea_row3 Theorem A concerns single deep points; both are stride-free. Same-parity row differences are multiples of 8. Rival pairs with a row-3 shallow point involve one label.

Sections 4-6. The deep triples (section 4(b)), the compositions of deep quadruples (parity), Q3, and the rival pairs are covered. In-class (o,e) rival pairs are excluded by G_T^(2u) (Proposition 1', any even stride). Cross-class (o,e) rival pairs need |t| < 2h < 4(p - uA).

Section 8 (Q4) uses p and q only through being in the grid.

So with the table's cell verdicts (section 1 of the table; the contested cells are re-checked in sections 1-5 here), every cell is E, C or W.

K7(u): Lemma IV(u) (p <= (128u^3/27 + 4u)be^3), Lemma FF'(u) with [G11], R_FF^+ with q = 1 and c_1 <= 12, and the cutoff h^(1/2)/32.

7. THEOREM N_menu: ASSEMBLY AND HYPOTHESES

Assembly.
- Assignment: i(T) depends only on the deterministic kappa^(u), so the colourings remain independent over T.
- On a light T, deg G_T^(i(T))[tau] <= 2 kappa^(i(T)) < B/2, so Proposition 3 holds.
- A chain that holds a subset of the light diagonals is L***(u) with fewer classes. Every cell proof quantifies over the classes present, and every count is an upper bound over realised shapes.
- The chains are separate windows left of z, each with row-1 tails (the (B9) sequence) and pairwise gaps of 2W_h + 1. J5' then glues them, and the window count grows by m.
- Theorem E receives the heavy labels in S, with Delta = H^U(B/4) <= C 4^a h Lambda^(beta_m(a)) B^(-a).
- There is one Theorem D group. Its probability >= 1/4 holds at every pair, because Bad_split is (l, p)-free.
- n_rel is the sum over u of n_rel^(u) = O(m(h^(2-eps_D) + h^(11/6) log h + h^(9/5+2eps))).
- Width: the light part is 136314.88 (sum over u of P_u) B h^2 (1 + o(1)), which is 2.9 times v4's at {1, 3}, plus O(m h^2 ell).
- The exponent is max(x, beta_m(a) + 2 - ax, 2 - x), so x_2 = 1.4295234 (recomputed: x_1 = 1.496743 and x_2 = 1.429523).

Hypotheses and status.
- (N0) h >= max(10^10, h_PNT^U, h_D), where h_PNT^U is non-explicit and comes from the PNT in progressions mod 4Delta'_u for each u. External.
- (N1) v4's (H3) and (H4). Audited.
- (N2) The heavy count. It is heavy_light Theorem 1(b) in its menu form (A-5, audited for menus of even strides with the Kronecker Lemma 2). stride_menu_heavy_count Theorem M1 restates it and is not audited. heavy_diagonals_sharp Lemma 1 is a lower bound and is not needed.
- (N3) core Theorem T: Lemma C, U1 and U3, and the p-adic and l-adic kills. Proved, not audited.
- (N4) The table's Theorem T(u) cell verdicts, with D1 applied (P_u = max(40, 8u^2+4) and margins 1.022h, 1.021h, 1.0216h). Proved, not audited.
- (N5) R4, Lemma IV(u), FF(u), FF'(u), (B8)(u) and K7(u): sections 1-3. Proved here, not audited. They agree with ratio sections 3-4 and table B6/D13 up to D2.
- (N6) Lemma DL: part (b) proved here, part (a) proved by the occupancy argument against v4's verdict reasons. Not audited.
- (N7) Theorem K(u). Proved modulo (N3)-(N6), not audited.
- (N8) Proposition U(u). Proved here from A-3 at general s, not audited.
- (N9) The menu assembly. It is proved by reading J5', Theorem D-weighted (whose sup over T allows Q_T to depend on T), Theorem E and Proposition partial; all four are stride-free. Not audited.

Nothing mathematical is open for N_menu beyond these audits.

## External results used

- Quadratic (Jacobi) reciprocity and the PNT in arithmetic progressions modulo 4Delta'_u (non-explicit). They give the densities 1/2 for l and 1/4 for p, because chi_(-4) chi_(Delta'_u) is nonprincipal. Textbook; not looked up.
- tau(n) << n^eps. Standard.
- No other external result is new. Dirichlet/Mertens enter only through the audited heavy_light Theorem 1(b) (A-5).

## Checks

Analytic work came first. Then one sanity script ran once with py -I, in well under 60 s: scripts_close/check_close.py. It checked three things:
- R_IV(u): brute force over the integrality conditions of (I1) and (I2) with Delta = 4ue (n1, v and z integers), for u in {1, 3, 5}, odd be <= 21 and 0 < al < u be. On all 426 pairs, the first three solutions equal (q m, (p - q) m) with g = gcd(F_u, u be - al), and (I1) and (I2) are asserted on each solution. The table's g differs on 74 pairs, giving a superset. The bounds q > al be^2, p >= 4u be^3/Delta_u and p <= (128u^3/27 + 4u) be^3 hold, and g divides Delta_u.
- gcd(U_u, V_u) divides 8u(4u^2+1) for u in {1, 3, 5, 7, 9}, |a| <= 600 and b < 120.
- x_1 = 1.496743 and x_2 = 1.429523, by a grid minimisation.

Read: stride_transfer_core, stride_transfer_ratio, stride_transfer_table, census_stride12 (statements), stride_menu_heavy_count, ratio_graph_r_iv, additive_class_split, obstruction_table_completeness and its audit, and consolidated_board_v4. I also read parts of saw_residual_families (iii-a, iii-b), deep_layer_sawtooth (Theorem 1, Proposition 5), v3_and_cross_block (Theorem B, Propositions D-F), threshold_families (Theorems 2-3), mixed_quadruples (Theorems 3-4), ap_hypothesis_henriot (Theorem D-weighted), heavy_light_split and its audit (menu form), and sea_census_rigid (B2).

The repository was only read. No git command was run and the web was not used.

## Gaps

- No item here has had a second reader. The ones that most need one are: Theorem R4's integrality reduction (section 1), Lemma IV(u) and FF'(u), the Feo, Foo and Fee re-derivations at stride 4u, the A4 I.2/II identities read from mixed_quadruples at s = 4u, and the D1 margins at P_u = 76.
- Lemma DL(a) (one-label cells are stride-free) rests on v4's stated verdict reasons and K4 constants. I did not re-read SAW Theorem 1(1)-(6), saw (i)/(ii), S1L or V2-4 line by line for hidden uses of which offset-0 slots hold labels.
- The table's cell verdicts marked V were classified by their inputs in stride_transfer_table. I re-derived only the contested cells: A1, A3 (4(b), 4(c)), A4, A5, B6, D5, D6, D12-D16, Q3 and FFo/FFo.
- D15 relies on two_filler Lemma 1's hypotheses (Dx = 0 mod 16, Dy = 0 mod 32) as quoted in the table. I did not re-open two_filler_row_lemma.
- Theorem N_menu is conditional on (N3)-(N9) being audited. Its exponent x_2 = 1.4295 is not an unconditional result; Theorem N stays at 1.4967429.
- h_PNT^U is non-explicit, and the menu's constant is sum P_u/40 times v4's (2.9 for {1,3}), so the gain is only asymptotic.
- The definition-level census at stride 12 used the untwisted rule and p = 3, 7 mod 20, so it gives no numerical test of the twisted-rule cells. Cross-class cells need h near 10^4 (blocks) and h > 2*10^6 (A1).
- The far goal m_h = O(h^2) is not addressed. By Theorem LB, menu-heaviness at relocation price Lambda^2 cannot go below 1.3108.

## Missing estimate

None for the mathematics of the stride-4u board or the menu board. What remains is second readings of the items under (N3)-(N9). The far goal still needs a heavy relocation price below Lambda^2 or a finer heaviness measure, since menus bottom out at 1.3108.

## Next steps

- Audit sections 1-3: Theorem R4's integrality reduction, Lemma IV(u) (both bounds and the tail) and FF'(u) (content bound 8u Delta_u, the tail W^(-1/3) and the count X^(2/3)).
- Audit the twisted-rule cells at P_u = 76: A1 (2(e) margin 1 + 37/1715), Proposition 1(c), L-adic (i), Fee, Foo with a label vertex, A5, mixed_quadruples 4(c), and Proposition F F2 in both parities.
- Audit Lemma DL(a) by re-reading SAW Theorem 1, saw (i)/(ii), S1L and V2-4 for any use of which offset-0 slots hold labels. Optionally run the stride-12 census again with the twisted rule and (37/p) = (37/l) = -1.
- Fix the spec in one place: P_u = max(40, 8u^2+4), the twisted rule, (B2'), and the exact R_IV(u) g = gcd(F_u, u be - al). Then write Theorem N_menu for U = {1, 3} with the (N0)-(N9) list and add ledger rows marked 'proved, not audited'.

