# Transfer of the specification and the 2-adic core to stride 4u

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: the specification and 2-adic core of the board carry over to stride 4u (u odd) once four definitions change: the prime conditions use (4u^2 + 1) in place of 5, the p range becomes (P_u h, 2 P_u h] with P_u = 8u^2 + 4, and the placement rule gets a u-twist, rho_s = p^(-1)(u s - kappa) mod 16l, which also fixes the type phase. Lemma C lists the region congruences. The 512 types, SAW* and Table J1*, Lemma N, Q3, S1L and most of Q4 carry over word for word, and the other steps are re-derived. Still open: the in-class shape families at stride 4u (R_IV(u), R_FF(u), D12 and D13), the A4 shape counts, and the label-vertex cells of v3 Theorem B. Not audited yet.

# Result

## Status

partial

## Summary

The specification and 2-adic core of L***U carry over to stride 4u once four definitions change; the in-class shape families stay open

## Statements

DEFINITION. L***(u), for odd u >= 3. Put Delta_u = 4u^2 + 1 and P_u = 8u^2 + 4. For u = 3 these are 37 and 76. Everything not listed here is as in consolidated_board_v4.md.
- (B0) As in v4, with "stride 4" replaced by "stride 4u".
- (B1) kappa_T = |D_T^(2u)|, the distance set of stride_menu at sigma = 2u. The heavy threshold B/4 is unchanged.
- (B2') CHANGED.
  - l is prime in (1.04h, 2.08h] with (Delta_u/l) = -1. This replaces l = +-2 (mod 5).
  - p is prime in (P_u h, 2 P_u h] with p = 3 (mod 4) and (Delta_u/p) = -1. This replaces p = 3, 7 (mod 20) and the range (40h, 80h].
  - For u = 3: (l/37) = -1; p = 3 (mod 4) and (p/37) = -1; p in (76h, 152h].
- (B3) Unchanged: 512 types tau = (i mod 32, s mod 16), and the same r0, y_P, tau_T and c_tau.
- (B4) Unchanged, with G_T = G_T^(2u).
- (B5') CHANGED.
  - t = rho_s + 16lk, with rho_s = p^(-1)(u s - kappa) (mod 16l).
  - The slot is n = u i + p t + b_tau, in column 4n.
  - Consequently n = u j - kappa_tau (mod 16l) for every label of R_tau.
  - Every label slot of R_tau has n = rho_tau := u(iota + sigma) - kappa_tau (mod 16), and rho0 := rho_tau mod 4.
- (B6) Unchanged as a function of n, with rho0 from (B5'). This covers SAW*-shift, Table J1*, (Phi) and the margins.
- (B7)-(B10) The rules are unchanged. Their constants become the K4 values below.

LEMMA C (region congruences of L***(u); proved). In R_tau:
- (C1) every label slot n = rho_tau (mod 16);
- (C2) odd label rows = y_P (mod 64);
- (C3) even label rows = y_P + tau_T (mod 32);
- (C4) the filler at slot n has row T*_tau - 24 + 8w, with w = (n - rho0) mod 4, and this row is = y_P + 8(w + c_tau) (mod 64);
- (C5) two labels of one subclass have same-parity points differing by (4u Di, 2Di), with Di in 32Z;
- (C6) points of distinct subclasses are at least 4(p - u(A - 1)) > 4(P_u - u/2)h - 4u columns apart, which is more than 298h for u = 3;
- (C7) any two labels of R_tau satisfy Dn = u Dj (mod 16l) and Dn = u Di (mod p).
(C1)-(C4) also hold under the unchanged rule rho_s = p^(-1)(s - kappa). (C7) does not.

THEOREM T (transfer; proved here, not audited). Under (B2') and (B5'):
- (V) These items carry over word for word, because their proofs use only (C1)-(C4), a single label, or lower bounds that (C6) strengthens:
  - the 512 types and their constants;
  - SAW*-shift and Table J1*, with (Phi) and the margins;
  - SAW Theorem 1 (1)-(6), Lemma 2 (CE) and Lemma 3;
  - BH16 A1, A2 and A5;
  - Lemma N and Theorem Q3 (three_label_one_filler and low_rows);
  - Lemma S1L;
  - sea_row3 Theorem A and Corollary B;
  - the SAW* Feo kill (saw (iii-a)), re-proved below from (C1)-(C4) alone;
  - the filler-vertex Foo kill;
  - Q4 Lemmas LR and S, and parts (b), (c) and (e);
  - the K2 item 'sea_row3 M2a -> mod 16';
  - in-class even-even M2c (sea_census B3(i), (C1)): empty.
- (R) These items need a re-derivation, which is done below; each holds with the stated new form:
  - Lemma U1: (a) Dn := u Ds - p Dt is in 16lZ, and Dt = 0 iff c1 = c2 iff Dn = 0; (b) slot injectivity; (c) as before; (d) Dx/4 - u Dy/2 = DM for two odd points and -Dn for two even points;
  - Lemma U3, with in-class vectors (4u Di, 2Di) and (4u Di, 2(Di + s) + 1);
  - BH16 A3;
  - SAW Lemma 4(a), (b);
  - threshold Proposition 1(b): rigid Theorem 2(e) at stride 4u;
  - threshold Proposition 1(c): B1 type II, with Sigma != 0 and with Sigma = 0;
  - threshold Proposition 1(d);
  - Lemma L-adic (i), (ii);
  - Q4(a), the LLL case;
  - J4 and the widths;
  - the ll/FF kill;
  - every K4 line touched by p or u.
- (F) These items fail as stated and are repaired:
  - (F1) the unchanged rule loses l | Dn for every pair of classes of different diagonals; repaired by (B5');
  - (F2) the stride-4 formula for rho0 is wrong when u = 3 (mod 4) and iota + sigma is odd; repaired by (B5');
  - (F3) the residue conditions (5/p) = (5/l) = -1 must become (Delta_u/p) = (Delta_u/l) = -1; repaired by (B2');
  - (F4) SAW Proposition 5 (T2) does not exist at stride 4u. Its cell D3 merges into the same-row Fo/Fo family D12/D13, which obeys the cubic P^3 - 8utP^2 + 4t(t - 2Y1)P - 32ut^2(t - Y1) = 0, with t = Di in 32Z.

NEW MARGINS FOR u = 3 (each below 1.04h):
- Proposition 1(c): |37 Sigma - S| < (1 + 37/1715)h, about 1.022h;
- L-adic (i), (ii): about 1.021h;
- rigid Theorem 2(e): |b| < (1 + 37/1715)(h - 1), about 1.0216h.
For general odd u the excess over 1 is about 1/(16u). Light-region width: 512 · 4 · 2P_u h · 16 · 2.08h · B (1 + o(1)), which is P_u/40 times v4's figure (1.9 for u = 3).

NOT PROVED: the stride-4u in-class shape families (R_IV(u), R_FF(u) with an FF' analogue, and so D12/D13), the stride-4u shape counts of A4, v3 Theorem B's label-vertex cells, heavy_light Theorem 1(b) in Q(sqrt Delta_u), and therefore any bound on m_h from L***(u).

## Proofs

Notation: Delta = Delta_u, P = P_u, A = ceil(h/2), K = floor(h/2). A label (i, j) of subclass (s, k) has t = rho_s + 16lk, M_c = p t, and slot n = u i + M_c + b_tau. Its odd point is (4n, 2i + 1) and its even point is (4n, 2j + 2). Put n(c) := u s_c - M_c. Then n = u j - n(c) + b_tau.

0. WHY (B5') AND (B2') (items F1, F3).
- (F1) Under the old rule p t = s - kappa (mod 16l), n - u j = p t + b - u s = -(u - 1)s - kappa_tau (mod 16l).
  - For two classes with Ds != 0, the class constants differ by (u - 1)Ds mod l. This is nonzero, since l > h > |Ds| and l > u.
  - So the hypothesis 'l | N' of threshold Proposition 1(b)-(d), Lemma L-adic and the D18 count fails for every such pair.
  - This shows only that the proofs lose their hypothesis. I did not show that obstructions then occur.
  - Under (B5'), p t = u s - kappa (mod 16l), so n - u j = b - kappa = -kappa_tau (mod 16l) on the whole type.
  - u is invertible mod 16l (u is odd and l > u is prime). So s -> rho_s is injective on fewer than 16l consecutive s.
  - The sanity script confirms both claims: for (B5'), (n - u j) mod 16l takes 1 value per type; under the old rule it takes 59 to 123 values mod l.
- (F2) rho_tau = u(iota + sigma) - kappa_tau (mod 16). For u = 3 (mod 4), u x = x (mod 4) only when x is even, so the stride-4 formula iota + sigma - kappa_tau gives the wrong rho0 whenever iota + sigma is odd. The audit of three_label_one_filler requires rho0 to be the true slot residue, and so do Lemma N, Lemma S1L and the Feo kill.
- (F3) The residue conditions come from Delta, not from 5. Sections 3 and 4 show where.
- Range of p: stride_menu Lemma 4 at s = 4u needs p > max(20h, (s^2/2 + 4)h) = (8u^2 + 4)h. Every K4 use of p in v4 is a lower bound, a 'one prime factor in range' fact (true a fortiori), or a width.
- Prime counts:
  - Delta = 1 (mod 4), so for odd primes q not dividing Delta, (Delta/q) = (q/Delta') by Jacobi reciprocity, where Delta' is the squarefree part of Delta (Delta' = 13 for u = 9).
  - The conditions are therefore unions of half the classes mod Delta' (and mod 4 for p).
  - The PNT in progressions gives #L >= (1/2 - o(1))1.04h/log h and #P >= (1/4 - o(1))P h/log h, the same densities as v4.

1. LEMMA C.
- (C1): (B5') gives n = u j - kappa_tau (mod 16), and j = iota + sigma (mod 16) on the type.
- (C2) and (C3): rows depend only on (i, j), so they hold exactly as in v4.
- (C4): this is (B6) with the true rho0.
- (C5): same subclass means Dt = 0, so Dn_slot = u Di and Dy = 2Di (or 2Dj = 2Di).
- (C6): distinct subclasses have |Dt| >= 1, and the u i parts span less than u A.
- (C7): this is (B5') together with M_c in pZ.
- (C1) also holds under the old rule: n = (u - 1)i + j - kappa_tau (mod 16l), and (u - 1)i = (u - 1)iota (mod 64) because u - 1 is even and 32 | i - iota.
- Principle: an argument that uses only (C1)-(C4), one label point or one double, or a lower bound on cross-class distance, carries over word for word. The deep layer near a label column depends only on n - rho0 mod 4 and on which offset-0 slots hold labels or holes. The one-label arguments already allow any such occupancy.

2. LEMMA U1 AND LEMMA U3 (re-derived).
- (a) p Dt = u Ds - D(n(c)), so Dn := u Ds - p Dt is in 16lZ.
  - If Dt = 0, then 16l | u Ds, so Ds = 0 (u is a unit and |Ds| < h < 16l), and then k1 = k2.
  - If Dn = 0, then p Dt = u Ds with |u Ds| < u h < p, so Dt = 0.
- (b) Write n - b = u i + p t with 0 <= u i <= u(A - 1) < p. The division algorithm gives (u i, t), hence (i, rho_s, k). rho_s gives s by injectivity.
- (d) Two odd points: Dx = 4(u Di + p Dt) and Dy = 2Di, so Dx/4 - u Dy/2 = p Dt = DM. Two even points: Dy = 2(Di + Ds), so Dx/4 - u Dy/2 = p Dt - u Ds = -Dn.
- Sizes: |Dx| <= 2W_h, so |DM|, |Dn| <= h^2/8 + 1.5u h + O(1) < (1.04h)^2 < (P h)^2. Each nonzero value therefore has at most one prime factor in each range. Theorem U's p-type and l-type shapes then use the new forms: B7 odd-odd DM = Delta_x/4 - u(y_D - y_B)/2; D17 DM = Dx/4 - u Dy/2; D18 Dn = -(Dx/4 - u Dy/2).
- U3: in one subclass, the point differences are (4u Di, 2Di) or (4u Di, 2(Di + s) + 1). The filler offset is (n - rho_tau) mod 4. A translation by 4(p t + b) keeps the shallow columns. So every in-subclass picture is (l, p)-free.
- The sanity script found 0 failures of (a), (b) and (d) on true-prime regions.

3. ITEMS THAT USE p.
- Lemma 4 at s = 4u (A-4, stride_menu) applies to (B5') placements. Block offsets are 4(p t + b); 4b cancels within a type and 4pt = 0 (mod p). The proof uses offsets only mod p and the gap 4(p - u A) > h. So every tilted right angle among label points is of type (E;O,E).
- SAW Lemma 4(a) (odd-odd A2 pair, different blocks). Write D - C = (4 delta, 2 eps) with eps = Di and delta = u Di + p Dt. The A2 condition is 4 delta^2 + eps^2 = L'^2. Mod p this reads Delta eps^2 = L'^2. With (Delta/p) = -1, p | eps, so eps = 0 and there is no pair.
- mixed_quadruples Theorem 4(c) (written for any even stride) needs sigma^2 + 1 = Delta to be a non-residue mod p, which is (B2'). Its block offset sP Dc becomes 4pDt, and its proofs use the offset only mod p.
- II(-1,-1) with Sigma = 0, re-derived. Here Dj = 0 and U = (-4Dn, 0). With delta = d' - d, |U + W|^2 = |U|^2 for W = (4u delta, 2(delta - Ds)) gives (delta - Ds)^2 + 4u^2 delta^2 = 8u Dn delta.
  - Mod p, Dn = u Ds. Rearranging gives Delta(delta - Ds)^2 = (2u Ds)^2 (mod p).
  - With (Delta/p) = -1, p divides both sides. So Ds = 0 and delta = 0, which gives V = U. That case is excluded.
- A(ii) of v3, both odd: 2(u Di + DM)a = f Di gives 2ua = f (mod p), with |2ua - f| < 3h < p. In-class, 2ua = f contradicts f odd.

4. ITEMS THAT USE l (the K2 l-adic items).
- (i) Proposition 1(d), SAW Lemma 4(b): two even points in different blocks. delta = u eps (mod l) by (C7), so Delta eps^2 = L'^2 (mod l). With (Delta/l) = -1, l | eps, and |eps| < K < l gives eps = 0.
- (ii) Proposition 1(b), rigid Theorem 1/2(e) at stride 4u.
  - Take V the even point of slot i0 of c0, P the odd point of slot i0 + t1 of c0, and Q the even point in c'.
  - VP = (4u t1, 2t1 - T0) and VQ = (4(u c2 - N), 2c2), with c2 = j_Q - j_V and N = n(c') - n(c0) in 16lZ \ {0}.
  - The right angle reads c2(2 Delta t1 - T0) = 8u t1 N. Divide by g = gcd(t1, T0) and put b' = 2 Delta t' - T', which is odd.
  - |N| >= p - u h > (P - u)h and |c2| <= K - 1. So |t'| < |T'|/(16u(P - u) - 2 Delta) and |b'| < (1 + Delta/(8u(P - u) - Delta))(h - 1).
  - For u = 1, P = 40 this is 1 + 5/307, Sweep B's figure. For u = 3, P = 76 it is 1 + 37/1715 < 1.022.
  - l | N gives l | c2 b'. But 0 < |c2| < l and 0 < |b'| < l, a contradiction. c2 != 0, because c2 = 0 forces N = 0.
- (iii) Proposition 1(c), B1 type II (-1,-1).
  - Take A, B even and C, D odd, with A, C in c0 and B, D in c'.
  - U = (4(u Dj - Dn), 2Dj) and 2n = (4u Sigma, 2Sigma - 2S), with S = s0 + s' + 1.
  - Then U · 2n = 4[Dj(Delta Sigma - S) - 4u Sigma Dn], checked on true coordinates by the script.
  - From U · n = 0: |Sigma| <= (h/2)(|Sigma| + h)/(4u(p - 1.5u h)), so |Sigma| < h/1715 for u = 3.
  - If Dj != 0, then l | Delta Sigma - S, with |Delta Sigma - S| < 37h/1715 + h < 1.04h < l. So Delta Sigma = S, then 4u Sigma Dn = 0, so Sigma = 0, a contradiction.
  - If Dj = 0, then Sigma = 0, which is section 3.
  - Delta Sigma - S is odd, because Delta is odd, Sigma = 0 (mod 32) and S is odd.
- (iv) Lemma L-adic.
  - Both-even Pc: G - V = (4(u Dj - Dn), 2Dj) and E - V = (a, -f), so 2(u Dj - Dn)a = f Dj.
    - Same class: 2ua = f, which contradicts f odd.
    - Across classes: 2ua = f (mod l), with |2ua - f| <= u h/(2(P - 1.5u)) + h < 1.021h < l. So 2ua = f exactly, the same contradiction.
  - Fee with an even vertex: 8 alpha(u eta - Dn) = -d eta, with d odd.
    - Same class: 8u alpha = -d, which is impossible.
    - Across classes: |8u alpha + d| < 1.021h < l, which is impossible for the same reason.
- (v) J4 and widths.
  - Classes of one diagonal are at least 64lp - 4u(A - 1) > 2600h^2 apart.
  - Each residue mod 16l holds at most one diagonal (rho_s is injective).
  - t < 16lB.
  - Width per type: 4p · 16lB + 4uA + 2(2W_h + 1) + 12.

5. 2-ADIC ITEMS.
- (i) BH16 A3. Two even label points of R_tau have delta = Dn_slot = u eps (mod 16). A1 needs eps odd with delta even, or eps = 2 (mod 4) with delta = 0 (mod 4). Both are impossible, because u is odd. In-type eps = Dj = 0 (mod 16), so A1 already excludes the pair. The even-label lattice reads u y = 2n + 2u + 2 kappa_tau (mod 32).
- (ii) Feo kill (saw (iii-a)), from (C1)-(C4) alone. Put g = n_V - n_P, t = n_Q - n_P and f = y_V - y_P.
  - Q-vertex: the dot product is odd.
  - P-vertex: 16gt = -f(y_Q - y_P). Holes: v2(f) = 3 and g is even, which is impossible. Bases: v2(f) is 4 or 5, so v2(t) <= 1, which is not offset 0.
  - V-vertex: 16g(g - t) = f(y_Q - y_V), where y_Q - y_V is odd.
    - Holes and v2(f) = 5 fail on valuations, since g is odd and t = 0 (mod 4).
    - If f = 16f' with f' odd, then g^2 = f'(y_Q - y_V) (mod 4). By (C2) and (C3), y_Q - y_V = tau_T (mod 16), so f' tau_T = 1 (mod 4) is needed.
    - (C4) gives f' tau_T = 3 (mod 4): w = 1, f' = 1 when c = 1, and w = 3, f' = 3 when c = 3.
  - This needs no lattice and no stride.
- (iii) Foo with a filler vertex.
  - alpha1 alpha2 = -4 e1 e2 forces w = 2.
  - Put Dslot = alpha2 - alpha1, which is 0 (mod 16) by (C1).
  - Then w'^2 + e1 e2 = (Dslot/4)^2 = 0 (mod 16), with w' = (alpha1 + alpha2)/4 an integer.
  - But e1 = e2 (mod 8) by (C2), so e1 e2 = 1 (mod 8), and w'^2 = 7 (mod 8) is impossible.
- (iv) ll/FF (saw (iii-b)). |L2 - L1|^2 = 4 Delta t^2 with t in 32Z, against |F2 - F1|^2 = 16 Dmu^2 + 64 Dw^2 with Dmu = Dw (mod 4). So 256 Delta t'^2 = Dmu^2 + 4 Dw^2.
  - Dw odd gives 5 (mod 8).
  - Dw = +-2 gives v2 = 2.
  - Dw = 0 needs Delta to be a square, but (2u)^2 < Delta < (2u + 1)^2.
- (v) sea_row3.
  - Theorem A's conditions are on single deep points.
  - In 2(iii) the same-class case is B - D = (4ue, 2e) with e in {1, 2} and e = Di in 32Z, which is impossible.
  - The cross-class case is excluded because |beta| <= 6h < 298h.
  - (H4) is redundant (its audit).
- (vi) In-class even-even M2c (sea_census B3(i)). Delta_x = 4ue in-class, so v2(Delta_x) = a + 2 as before. This forces v2(e) = 3, but e = Di = 0 (mod 32).
- 2-adic note: s^2 = 16u^2 = 16 (mod 128), so 4 Delta = 20 (mod 128) and Delta = 5 (mod 32). Every v4 2-adic step that sees the stride only through s^2 + 4 is unchanged. In this route only 'Delta odd and not a square' was needed.

6. SAW PROPOSITION 5 AND D3 (item F4).
- T2 needs C - A to have slope 1/2 in (n, Y) units, but stride-4u label lines have slope 1/(2u). So the configuration is absent.
- For same-row in-class Fo/Fo, put L2 - L1 = (4ut, 2t) and Y2 = Y1 - 2t. Eliminating as in saw (iii-b) gives P^3 - 2aP^2 + ((Y1 - Y2)^2 - 4bY1)P - 2a(Y2^2 - Y1^2) = 0 with (a, b) = (4ut, 2t). Hand check: at u = 1 the T2 point (t = -8, Y1 = 40, P = -48) satisfies it.
- n_y = t. So t > 0 needs t <= 210, which is the stride-free R_FF^+ superset (|Di| <= 210, at most 6 neighbours on each side).
- t < 0 needs the R_FF weights (Lemma FF') redone for the new cubic. That is outside this route.

7. Q4.
- (a) V a label gives an LLL triple, which is empty by section 4(ii) and Lemma 4. FFe and Feo are single-label or covered by (C1)-(C4). Foo is section 5(iii).
- (c) In-class {o, e} rival pairs are exactly S_T^(2u), which G_T^(2u) excludes.
- (d) Lemmas LR and S use row sizes, (C5) row differences and (C6) lower bounds. Case (L) defers to A3/A4, see Gaps.

## External results used

- Quadratic (Jacobi) reciprocity: for an odd prime q not dividing Delta_u, (Delta_u/q) = (q/Delta_u) because Delta_u = 1 (mod 4). Textbook; not looked up.
- Prime number theorem in arithmetic progressions modulo 4 Delta'_u (non-explicit), replacing mod 5 and mod 20, for #L and #P. Delta'_u is the squarefree part of Delta_u.

## Checks

Analytic first. I read these notes in the 2026-11-13 folder:
- in full: consolidated_board_v4, stride_menu, three_label_one_filler, low_rows_row3_types, audit_constant_lists, deep_layer_sawtooth, deep_layer_bh16, sea_row3_split, threshold_families_random_prime;
- the relevant parts: consolidated_board (v1: J1*, L-adic, FF', 3L1F-a, K1-K3), uniformity_first_moments (U1-U3, section 3), saw_residual_families, sea_census_rigid (B1-B4), rigid_layout_cross_block (Theorems 1, 2 and 4(e)), mixed_quadruples_blocks (setting and Theorem 4);
- the verdicts and issue lists of the five audits of the in-scope notes.

One script, check_u.py in my script folder, ran with py -I in a few seconds. It uses true primes:
- (Delta/l) = -1, l in (1.04h, 2.08h];
- p = 3 (mod 4), (Delta/p) = -1, p in (P_u h, 2P_u h].

Runs:
- (h, u) = (1001, 3), (1500, 3), (1201, 5) and (2003, 9);
- 465 to 1953 labels of one type, with random classes.

Results:
- Label slots mod 16 take one value per type under (B5'), and also under the old rule.
- (n - uj) mod 16l takes 1 value under (B5'), but 59 to 123 values mod l under the old rule.
- Slots are injective.
- 0 failures in 20000 pairs of U1(a) and U1(d).
- 0 failures in 20000 triples of three identities on true coordinates: the stride-4u right-angle identity c2(2 Delta t1 - T0) = 8u t1 N, the B1 identity U·2n = 4[Dj(Delta Sigma - S) - 4u Sigma Dn], and the even-even vector (4(u Dj - Dn), 2Dj).

The repository was only read. I ran no git command and did not use the web.

## Gaps

- Nothing here is audited. Every re-derivation (sections 2-7) was checked once, by me only.
- Outside this route but needed for L***(u) to be a board:
  - R_IV(u) (in-class odd-odd M2c). A sketch gives lambda = al/be, F_u = 4(al - 2u be)^2 + be^2, and the gcd dividing Delta_u in place of 5. It is not verified, and Lemma IV's weights at stride 4u are not redone.
  - R_FF(u) with an FF' analogue for the new cubic (D13, now including D3).
  - The A4 shape counts: threshold Theorems 2-3 and mixed_quadruples Theorem 3 at s = 4u. mixed_quadruples is written for general s, but its block offset sPDc must be read as 4pDt.
  - v3_and_cross_block Theorem B label-vertex cells (Foo, FFo) and Propositions D-F.
  - two_filler Theorem 3 (D17/D18). They look stride-free through Dx = Dy = 0 (mod 64), but I did not re-read them.
  - heavy_light Theorem 1(b) in Q(sqrt Delta_u).
- Q4(d) case (L) and Theorem U's D-family averages rely on the A4 shape counts above at stride 4u.
- Obstruction_table Theorem K, (B8)'s q-density claims for R_IV(u), and K7 were not re-read for stride 4u.
- The sanity script tests only positions and the re-derived identities on true coordinates. Cross-class (E;O,E) angles are vacuous at testable h: |t'| < |T'|/3430 for u = 3. So Theorem 2(e) at stride 4u has no numerical test.
- Several strides in one board (the menu) need a separate admissible pair (l_u, p_u) per stride region, each with its own residue conditions, and Theorem U applied per region. I did not write this down.

## Missing estimate

None for the items of this route. For L***(u) to give a width bound, three things are still needed at stride 4u: the in-class shape families R_IV(u) and R_FF(u) with finite weights (analogues of Lemma IV and Lemma FF'); the A4 shape counts h^(2+o(1)); and the heavy count H_d(B/4) in Q(sqrt Delta_u).

## Next steps

- Have the four definitional changes (B2'), (B5') (with the rho0 formula), and the re-derivations of sections 2-5 audited. They are about two pages of algebra.
- Redo R_IV at stride 4u from the M2c equations (I1), (I2) with Delta_x = 4ue: confirm F_u = 4(al - 2u be)^2 + be^2, gcd | Delta_u, the 2-adic split, and Lemma IV's sum of 1/q.
- Redo the same-row Fo/Fo cubic P^3 - 8utP^2 + 4t(t - 2Y1)P - 32ut^2(t - Y1) = 0: find its singular point and parametrisation, and prove an FF' analogue (finite sum of |U'|^(-1+eps)) for the t < 0 branch.
- Re-derive the threshold Theorems 2-3 identities at s = 4u (the I.2 identity has 10a + T0 -> 2 Delta a + T0) to keep A4 at h^(1+o(1)).
- Re-read v3_and_cross_block Theorem B label-vertex cases (Foo, FFo) and Propositions D-F with (C5)-(C7).

