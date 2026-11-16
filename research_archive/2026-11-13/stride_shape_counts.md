# Shape counts at stride 4u

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: at stride 4u every counted family of Theorem U keeps its order of labels hit: A4 (I.2 and II(1,-1)) and D8 at h^(1+o(1)), and D17, D18 and B7 at O(h^(9/5+eps) log h). The label-vertex cells Foo and FFo of v3 Theorem B are empty. Theorem U holds pointwise in each stride chain, with that chain's own pair (l_u, p_u). Not audited yet.

# Result

## Status

proved

## Summary

At stride 4u, every counted family of Theorem U keeps its order of labels hit: A4 (I.2 and II(1,-1)) and D8 at h^(1+o(1)), D17, D18 and B7 at O(h^(9/5+eps) log h). The label-vertex cells Foo and FFo of v3 Theorem B are empty. Theorem U holds pointwise in each stride chain, with that chain's own pair (l_u, p_u). Proved, not audited.

## Statements

SETTING. Fix an odd u >= 3 and the chain L***(u) of stride_transfer_core.md:
- Delta_u = 4u^2+1 and P_u = 8u^2+4.
- Adm_u = L_u x P_u, where L_u = {l prime in (1.04h, 2.08h] : (Delta_u/l) = -1} and P_u = {p prime in (P_u h, 2P_u h] : p = 3 (mod 4), (Delta_u/p) = -1}.
- Label (i, j) of subclass (s, k) has t = rho_s + 16lk, with p rho_s = u s - kappa (mod 16l). Its slot is n = u i + p t + b_tau. Its odd point is (4n, 2i+1) and its even point is (4n, 2j+2).
- For two labels write DM = p Dt and N = Dn := u Ds - p Dt. Then N is in 16lZ (U1(a) at stride 4u).
- I use Lemma C (C1)-(C7) and U1(a)-(d) at stride 4u, as in stride_transfer_core.md.
- Every statement holds for h >= h0(u), with constants depending on u. The menu has finitely many u, so one h0 works for all of them.

THEOREM S1 (A4, I.2 at stride 4u). Setting of mixed_quadruples Theorem 3 with s = 4u, block offset sP Dc read as 4p Dt (4b_tau cancels inside a type), and U* := 2 Delta_u a + T0 (odd).
- (E1) 16u^2 a^2 + (2a+T0)^2 = 16u^2 b^2 + (2b+T')^2, with (b, T') not equal to +-(a, T0).
- (E2) m U* = -16u a DM - (2a+T0) Ds, with m = iC + iD - i0 - iB. Equivalently n2 U* = 8ua(2N - u Ds), so N = (u Ds + U* n2/(8ua))/2, with n2 = m + Ds.
- 0 < |a| < h/(8u(2P_u - u)), which is h/3576 at u = 3.
- 0 < |N| <= (h-1)^2/(16u) + 1.5uh < (1.04h)^2, and 0 < |DM| = |u Ds - N| < (P_u h)^2.
- The shape set Sigma_I2 of pairs (skeleton (a, T0, T', b), n2) has |Sigma_I2| <= h^(2+o(1)). It does not depend on (l, p), the class datum Xi, kappa or b.
- Each shape is realised by at most one (l, p) in Adm_u. Hence E_{Adm_u} X_{I.2} <= 4A h^(2+o(1))/(#L_u #P_u) = h^(1+o(1)).

THEOREM S2 (A4, type II at stride 4u). Put g = C - A = (4ud, eta), g' = D - B = (4ud', eta'), Sigma = d+d', Dd = d'-d, H = eta+eta', De = eta'-eta, G = 16u^2 Dd^2 + De^2, and U = B - A = (U1, U2) with U1 = 4(uk + DM), k = iB - iA.
- E2 reads 4u Sigma U1 + H U2 = 0, and E1 reads 2(4u Dd U1 + De U2) + G = 0.
- With Sigma != 0 these imply X^2 + Y^2 = U2^2 (H^2 + 16u^2 Sigma^2), where X = 16u^2 Sigma Dd - U2 H and Y = 4u Sigma (De + U2). They also imply 16u Sigma | H U2.
- The roles carry over:
  - (1,1) with Sigma != 0 is empty for every p;
  - (1,1) with Sigma = 0 is empty, since p = 3 (mod 4);
  - (-1,-1) with Sigma = 0 is empty, since (Delta_u/p) = -1;
  - (-1,-1) with Sigma != 0 is empty by the l-adic kill (core 4(iii));
  - (1,-1) with Sigma = 0 is empty by parity.
- Survivor (1,-1) with Sigma != 0: there are at most h^(2+o(1)) skeletons (Sigma, Dd, H, De, U2). Each fixes T0, T', k, DM = U1/4 - uk and N = u Dj + H U2/(16u Sigma), with 0 < |N| < (1.04h)^2 and 0 < |DM| < (P_u h)^2. So each skeleton is realised by at most one (l, p), and E X_II <= h^(1+o(1)).

THEOREM S3 (D8, v3 family (d) at stride 4u). In a V3 pair of SLF-Pc triples, V1 and V2 are odd label points with the same i in different subclasses, and the holes are in one row.
- x_V2 - x_V1 = (e1 - e2)(4G - R) = 4DM, with DM = p Dt != 0, DM = 0 (mod 16), and |x_V2 - x_V1| >= 64p. So the family is empty unless 64p <= 2W_h + 1, which needs h > 128 P_u.
- The shape (y_V, hole row, gamma1, gamma2) is layout-free, with at most h^(1+o(1)) shapes. Shapes are p-type, and E X_D8 <= 2h · h^(1+o(1))/#P_u = h^(1+o(1)).

THEOREM S4 (label-vertex cells of v3 Theorem B at stride 4u).
- (a) Foo with a label vertex is EMPTY. Write O2 - O1 = (4(4u eps + DM), 8eps) and V - O1 = (4 alpha, 8e). The right angle reads alpha(4u eps + DM) = -4e eps.
  - Within a class: u alpha + e = 0, but u alpha + e is odd.
  - Across classes: mod p, u alpha + e = 0, and |u alpha + e| < p, so DM = 0, a contradiction.
- (b) FFo with a label vertex is EMPTY. The proof uses rows only (R-b), word for word.
- (c) Consequences:
  - v3 Theorem A(ii) at stride 4u: the only two-label SLL Pc is intra-class, G = V + (4ut, 2t), t > 0, t = 0 (mod 32), a = u_V/u, so it exists only when u | u_V. It is parked.
  - A(iii) at stride 4u: W determines the SLL triple.
  - Theorem C at stride 4u: every V3 pair in R_tau is family (d).
  - Proposition D: as in S3.
  - Proposition E: the Feo kill, as in the core.
  - Proposition F at stride 4u: F1 and F3 with n_y >= 1 are word for word. F2 holds with the mod-p step 2u n_x + n_y = 0.

THEOREM S5 (D17 and D18 at stride 4u).
- two_filler Lemma 1 holds word for word in L***(u), by (C1)-(C4). So df != 0 is empty for odd-odd and for even-even.
- The df = 0 branch with n_y <= -1 has the same layout-free shape set as at stride 4. It maps at most 4-to-1 per filler row onto E0(Q) witnesses with Q < 3h, so |Sigma_tau| <= 16 h^(o(1)) Sum_{Q<3h} |E0(Q)| << h^(9/5+eps).
- The n_y >= 1 branch is empty, because |Dx| <= 106h + 2 < 4(p - u(A-1)).
- D17 (odd-odd) is p-type, with DM = Dx/4 - u Dy/2. D18 (even-even) is l-type, with N = -(Dx/4 - u Dy/2), and both are nonzero.
- So E X_D17 <= 2h|Sigma_tau|/#P_u and E X_D18 <= 4h|Sigma_tau|/#L_u, both O(h^(9/5+eps) log h).
- B7 (cross-class M2c) carries over the same way: odd-odd is p-type with DM = Delta/4 - u e, and even-even is l-type. E X_B7 = O(N_h^int log h) = O(h^(9/5+eps) log h).

THEOREM U(u) (pointwise, per chain). For each type tau of L***(u) and each F in {A4-I.2, A4-II, B7, D8, D17, D18}:
- X_F(Xi, kappa, b; l, p) <= Y_F^(tau,u)(l, p) := lam_F Phi_F #{sigma in Sigma_F^tau realisable at (l, p)}. This holds for every class datum Xi with (Xi1)-(Xi3) (independence in G_T^(2u) for (Xi4)), every kappa and b, and every (l, p) in Adm_u.
- The averages over Adm_u are h^(1+o(1)) (A4, D8) and O(h^(9/5+eps) log h) (B7, D17, D18).
- Lemma U3 holds at stride 4u.
- So each chain u of a menu board can take its own (l_u, p_u) in Adm_u that minimises Y^(u) = Sum_tau Sum_F Y_F^(tau,u). Then Sum_F X_F^(u) <= 512 C_u h^(9/5+2eps).
- Over a menu of m strides the total is O(m h^(9/5+2eps)) = O(h^(2-delta)). The relocation rule then absorbs it in width o(h^2).

## Proofs

CONVENTIONS. A = ceil(h/2) and K = floor(h/2).
- Inside a type, b_tau is constant, so the column of label slot i of subclass c is 4u i + 4p t_c + const. This is the mixed_quadruples (MQ) setting at s = 4u, w = (4u, 2), W = s^2 + 4 = 4 Delta_u, with the block offset s P Dc replaced by 4p Dt.
- The MQ proofs use the block offset in only two ways. Mod p it vanishes, and 4p Dt is 0 (mod p). Its size is bounded below: points of different subclasses are at least 4(p - u(A-1)) > (32u^2 + 16 - 2u)h columns apart (298h at u = 3). In-block |dx| <= 4u(A-1).
- Both properties hold, so MQ Theorems 1 and 2 carry over. This is transfer_table A3 (Theorem 1: R; Theorem 2: V).
- Size thresholds (U1 at stride 4u): |Dx| <= 2W_h and |Dy| < h. So |DM| <= h^2/8 + uh/2 + 1 and |N| <= h^2/8 + 1.5uh + 1, both below (1.04h)^2 for h >= 2u and far below (P_u h)^2. Hence a nonzero DM has at most one prime factor in (P_u h, 2P_u h], and a nonzero N has at most one in (1.04h, 2.08h].
- Prime counts. Delta_u = 1 (mod 4) and is not a square, since (2u)^2 < Delta_u < (2u+1)^2. By Jacobi reciprocity, (Delta_u/q) = (q/Delta_u), which is a nonprincipal real character mod Delta_u. Its product with chi_4 is also nonprincipal, because the conductors are odd and 4. The PNT in progressions mod 4Delta_u (non-explicit) gives #L_u >= (1/2 - o(1)) 1.04h/log h and #P_u >= (1/4 - o(1)) P_u h/log h. Also gcd(p, 16l) = 1 and gcd(u, 16l) = 1, because l > 2u.

1. PROOF OF S1 (I.2).
- Points:
  - A = (4u i0 + O0, 2i0+1), the odd point of slot i0 in c0;
  - B = A + (4ua, 2a + T0);
  - C = (4u iC + O', 2iC + 1), in c' with O' - O0 = 4p Dt and Dt != 0 (I.2 has two blocks, MQ Theorem 1);
  - D = C + (4ub, 2b + T').
- Then 2n = C + D - A - B = (4um + 8p Dt, 2m + 2Ds), with T' - T0 = 2Ds. So n2 = m + Ds.
- U · 2n = 16ua(um + 2DM) + 2(2a + T0)n2 = 2[m U* + 16ua DM + (2a+T0)Ds]. This is checked symbolically (sympy residual 0), and its vanishing is (E2).
- Multiply out: n2 U* = m U* + Ds U*. Use E2 and 2 Delta_u a - 2a = 8u^2 a. This gives n2 U* = 8u^2 a Ds - 16ua DM = 8ua(2N - u Ds). Sympy checks this modulo E2.
- Parity. Equal-parity pairs give U = a w and V = b w, so V = +-U. One mixed pair with one equal pair gives an odd number of even points, so n is not integral. So each pair is one odd point and one even point. This is MQ's argument, which is stride-free.
- U* is odd, hence nonzero, so m is unique.
- b = 0 would need 16u^2 a^2 + (2a+T0)^2 = T'^2, that is a in S_T0^(2u). G_T^(2u)-independence (Xi4) excludes it.
- Bound on a. E2 is 8ua(um + 2DM) = -(2a+T0)n2. Here |2a+T0| and |n2| are at most h-1, and |um + 2DM| >= 2p - 2u(A-1) > (2P_u - u)h. So 0 < |a| < h/(8u(2P_u - u)). Also a != 0, since U is not vertical.
- N != 0. N = 0 would give p Dt = u Ds with |u Ds| < uh < p, so Dt = 0.
- Size of N. n · U = 0 gives |n1| = |2a+T0||n2|/(4u|a|) <= (h-1)^2/(4u). Here n1 = 2um + 4DM, so |DM| <= (h-1)^2/(16u) + u(A-1), and |N| <= |DM| + u|Ds| <= (h-1)^2/(16u) + 1.5uh.
- Skeletons. For fixed (a, T0), the map (T', b) -> (2b + T', 4ub) is injective into the representations of N_a = 16u^2 a^2 + (2a+T0)^2 < 2h^2 as a sum of two squares. So there are at most r_2(N_a) <= 4 tau(N_a) = h^(o(1)) skeletons.
- Values of n2. Let g = gcd(U*, 8ua) = gcd(U*, ua), using that U* is odd. Then (8ua/g) | n2, so there are at most 2hg/(8u|a|) + 1 values of n2.
- Sum over T0: Sum_{T0} gcd(2 Delta_u a + T0, ua) <= Sum_{d | ua} d(2h/d + 1) <= 3h tau(ua).
- So |Sigma_I2| <= h^(o(1)) Sum_{0<|a|<h} (3h^2 tau(ua)/(4u|a|) + 2h) = h^(2+o(1)).
- Template U2, type "both". The shape fixes N (realisation needs 16l | N) and DM = u Ds - N (realisation needs p | DM). Each is nonzero and below its threshold, so at most one (l, p) realises it.
- Anchor A, with free index i0 (Phi <= A). The label of A is (i0, i0 + s0). The other points are B = A + U, C = A + (4ue + 4DM, 2e) with e = (n2 - Ds + a - b)/2, and D = C + V. Each depends only on (sigma, n2), and 4p Dt = 4DM involves no separate p.
- By U1(b), each label point determines its label. So lam = 4, and Sum_{Adm_u} X <= 4A|Sigma_I2|. Then E X <= 4A h^(2+o(1)) log^2 h / (c P_u h^2) = h^(1+o(1)).
- Changes from the stride-4 proof (threshold Theorem 2 with its audit): 10a + T0 -> 2 Delta_u a + T0, 8a -> 8ua, Ds -> u Ds in the N formula, and (20h)^2 -> (P_u h)^2. Nothing else changes.

2. PROOF OF S2 (type II).
- Equations. A and C lie in one block, B and D in the other (MQ Theorem 1). So g = (4ud, eta) and g' = (4ud', eta'), and U1 = 4(uk + DM). Sympy checks this from coordinates.
- E2 is U · (g + g') = 4u Sigma U1 + H U2 = 0. E1 is |U + g' - g|^2 = |U|^2, which is 2(4u Dd U1 + De U2) + G = 0. Both are checked from true coordinates (residual 0).
- Eliminating U1 gives 2U2(De Sigma - Dd H) = -Sigma G. Then X^2 + Y^2 - U2^2(H^2 + 16u^2 Sigma^2) = 16u^2 Sigma [Sigma G + 2U2(De Sigma - Dd H)] = 0. This is a sympy identity.
- Integrality: H U2 = -16u Sigma (uk + DM), so 16u Sigma | H U2.
- Roles (re-derived):
  - (1,1): U2 = 2k and H = 2Sigma + T0 + T'. Mod p, E2 gives 2k(2 Delta_u Sigma + T0 + T') = 0. Both factors are below p in size, so k = 0 or the bracket is 0. Either way 16u Sigma DM = 0, which is impossible when Sigma != 0.
  - (1,1) with Sigma = 0: k = 0, and E1 gives 32u Dd DM + 16u^2 Dd^2 + X'^2 = 0 with X' = De. Mod p, with p = 3 (mod 4), p divides 4u Dd < p. So Dd = 0, then De = 0, and V = U.
  - (-1,-1) with Sigma = 0: core section 3, using (Delta_u/p) = -1.
  - (-1,-1) with Sigma != 0: the core 4(iii) l-adic kill.
  - (1,-1) with Sigma = 0: U2 = 2k + T' is odd, and E2 then forces H = 0, so n = 0.
- Survivor (1,-1) with Sigma != 0.
  - |Sigma| <= |H||U2|/(4u|U1|) < 2h^2/(16u(p - uA)), and |H| < 2h, |U2| < h.
  - Triples (Sigma, U2, H) with N0 := 16u|Sigma| dividing H U2: at most Sum_Sigma Sum_{d | N0} (2h/d + 1)(2h d/N0 + 1) <= Sum_Sigma tau(N0)(4h^2/N0 + 4h) = h^(2+o(1)).
  - For fixed (Sigma, U2, H), (Dd, De) -> (X, Y) is injective, since Sigma != 0 and u != 0. U2 is odd and Sigma != 0, so the right side is positive and at most C_u h^4. That gives r_2 <= h^(o(1)) skeletons per triple.
  - Recovery: d = (Sigma - Dd)/2, d' = (Sigma + Dd)/2, eta = (H - De)/2, eta' = (H + De)/2, T0 = eta - 2d, T' = 2d' - eta', Dj = (U2 - T0)/2, Ds = (T' - T0)/2, k = Dj - Ds. Then U1 = -H U2/(4u Sigma), DM = U1/4 - uk and N = u Ds - DM = u Dj + H U2/(16u Sigma). This matches transfer_table A4.
  - Sizes: |U1| <= h^2/(2u), so |DM| <= h^2/(8u) + uh/2 and |N| <= h^2/(8u) + uh < (1.04h)^2.
  - DM != 0 and N != 0, because Dt != 0 (as in section 1).
  - So the type is "both", with anchor A, Phi <= A, and B = A + U, C = A + g, D = B + g'. Hence E X <= 4A h^(2+o(1))/(#L_u #P_u) = h^(1+o(1)).

3. PROOF OF S4 AND THE THEOREM B/C CONSEQUENCES.
Filler facts, from (C1) and (C4):
- a filler at slot n has offset w = (n - rho0) mod 4, and every label slot is congruent to rho0 (mod 4);
- for a label point O and a filler V, alpha := n_V - n_O = w (mod 4);
- (y_V - y_O)/8 = e with e = w + c_tau (mod 8), and c_tau odd;
- odd label points of one type differ in row by 2Di with Di = 0 (mod 32).
(a) Foo with label vertex O1, ends V (filler) and O2 (odd label).
- Write Di = 4 eps, with eps = 0 (mod 8). Then O2 - O1 = (4 delta, 8 eps) with delta = u Di + DM = 4u eps + DM, and V - O1 = (4 alpha, 8e).
- The right angle at O1 is 16 alpha delta + 64 e eps = 0, that is alpha(4u eps + DM) = -4e eps. This is a sympy identity.
- In-class (DM = 0, eps != 0): u alpha + e = 0. But u alpha + e = alpha + e = 2w + c_tau, which is odd (mod 2). Contradiction.
- Across classes with eps != 0: |eps| < h/8 < p. Mod p the equation reads 4 eps (u alpha + e) = 0, so p | u alpha + e.
  - Size: |delta| >= p - u(A-1), so |alpha| <= 4|e||eps|/|delta| < h/(16(P_u - u)). Then |u alpha + e| < uh/(16(P_u - u)) + h/8 < p, so u alpha + e = 0.
  - Then alpha DM = 0. alpha = 0 forces e = 0 and V = O1, while alpha != 0 forces DM = 0. Both contradict.
- Across classes with eps = 0: alpha DM = 0 gives alpha = 0, so V would be a filler in a label column, which (B6) forbids.
- The stride-4 proof is the case u = 1. The only change is alpha -> u alpha in the parity and size steps.
(b) FFo with label vertex L.
- The row of W is y_F1 + y_F2 - y_L >= 2(T* - 24) - y_L.
- R-b gives y_L < T* - 320, so the row of W is above T* + 272 >= h + 86.
- This uses rows and (B6) only, both unchanged.
(c) Consequences.
- A(ii), both odd. Write G - V = (4(u Di + DM), 2Di) and E - V = (a, -2u_V). The right angle is (u Di + DM)a = u_V Di.
  - Di = 0 forces a = 0, so E is not shallow.
  - Mod p: ua = u_V. If Dt != 0, then |a| < h/(4(P_u - u)), so |ua - u_V| < p, so ua = u_V, then a DM = 0 and u_V = 0. But u_V is odd.
  - So Dt = 0 and a = u_V/u, which is odd, so E is shallow and W is in row r0 + 2Di.
  - This corrects one sentence of stride_transfer_core section 3. For an odd vertex, f = y_V - r0 is even, so 2ua = f does not give a contradiction. It gives this parked triple, as transfer_table S6 says.
- A(iii). Put t = (y_W - r0)/2, c' = (1 - r0)/2 and i_V = u a - c'. Then x_W - 4ut - 4b + 4uc' = Delta_u a + 4p t_c, with 0 < Delta_u a < 4p. So W determines (a, t_c), hence V and G. A numeric check found 0 failures in 20000 random cases.
- Theorem C.
  - SLL/SLF: the W rows are r0 + 2t (2t = 0 mod 64) and r0 + g (g = 8 mod 16). They never agree.
  - SLF/SLF: the holes are in one row, otherwise Di = 8, which contradicts (C2). So the two V have the same i. If they are in one class, then gamma1 gamma2 = u g/8, which fails on valuations (stride-free). Otherwise it is family (d).
  - FFo/FFo at one W: same o and same i. Across classes |beta1 - beta2| = p|Dt| >= p > 3h/4. The FFo filler-vertex analysis uses only slot offsets mod 4 and is word for word.
- Proposition F2 at stride 4u: Dx = 2u Dy + 4DM. If Dy != 0, mod p we get 2u n_x + n_y = 0, because |n_x| < h/298. Then 4 n_x DM = 0, so n = 0. If Dy = 0, then X^2 - delta^2 = 4e^2 with |e| <= 3, as before.
- Propositions E and F1: as in transfer_table D5 and D16. F3 with n_y >= 1: |Dx| <= 106h + 2 < 298h.

4. PROOF OF S3 (D8).
- The SLF-Pc relations 2a gamma = u_V g, W = G + (a, -2u_V), and the hole valuations use only (C1)-(C4) and one label, so they hold word for word.
- In family (d), y_V1 = y_V2 gives i1 = i2. So x_V2 - x_V1 = 4(u·0 + p Dt) = 4DM. The factorization phi(gamma1) - phi(gamma2) = (e1 - e2)(4G - R) is a sympy identity.
- Both slots are congruent to rho_tau (mod 16), so DM = 0 (mod 16) and v2(x_V2 - x_V1) >= 6.
- At offset 0, 4G - R is odd. At offset 2, v2(4G - R) = 1.
- The odd prime p divides one of the two factors. Either way |x_V2 - x_V1| >= 64p.
- Shapes: (y_V, hole row in {T*-24, T*-8}, gamma1, gamma2) with gamma_k | u_V g/2, so at most 2h max tau^2 = h^(1+o(1)).
- DM = (x_V2 - x_V1)/4 is nonzero and below h^2/8 + 1, so the type is p-type.
- Anchor V1: its row fixes i, and phi = s1 (Phi <= h). V2 = V1 + (4DM, 0). G_k, E_k and W are fixed by the shape. U1(b) fixes V2's label.
- So E X <= 2h · h^(1+o(1))/#P_u.

5. PROOF OF S5 (D17, D18, B7).
two_filler Lemma 1 needs four inputs:
- Dx = 0 (mod 16) and x_Fi - x_Li = 4 o_i (mod 16): (C1) gives label slots congruent mod 16, so Dx = 0 (mod 64), and n_F - n_L = o (mod 4);
- f_o - y_L = 8(o + c_tau) (mod 64) for odd labels, and odd for even labels: (C4);
- Dy = 0 (mod 32): (C2) gives mod 64 for odd points, and (C3) gives mod 32 for even points;
- (N): n_x = 2(o2 - o1) (mod 8) and X1 = 4 o1 (mod 16), which follow from these.
The proof itself is pure 2-adic algebra on (E1) and (E2) and never sees the stride.
- The df = 0 branch with n_y <= -1. The map (y_L1, Dy, f, k, w) -> (Q, e, n1, X, Y) = (A' + 2N', N', k, Dx - 2k, W'_x - k) uses only (E1), (E2) and rows. Its positivity step (X, Y >= 1) needs |Dx| > 2k, with k < h/2, and the cross-block bound gives |Dx| >= 298h.
- So the shape set is the stride-4 set or a subset of it. Per type there are 4 filler rows, and |Sigma_tau| <= 16 h^(o(1)) Sum_{Q<3h} |E0(Q)| << h^(9/5+eps) by point_counts Theorem A (audited, stride-free).
- The n_y >= 1 branch: |X1||n_x| <= 210h gives |Dx| <= 106h + 2 < 298h <= 4(p - u(A-1)), so it is empty.
- Types:
  - odd-odd: Dx = 4(u Di + DM) and Dy = 2Di, so DM = Dx/4 - u Dy/2 is fixed by the shape, and DM != 0 across subclasses (p-type);
  - even-even: Dx/4 - u Dy/2 = -N, nonzero by U1(a), with |N| < (1.04h)^2 (l-type).
- Anchor L1: its row fixes i1 (odd) or j1 (even). With phi = s1, Phi <= h (D17) or 2h (D18). L2, F1 and F2 are fixed relative to L1, and U1(b) fixes L2's label.
- two_filler Proposition 4 needs 4 · 298h > 420^2, so h >= 148, a fortiori.
- B7. The M2c equations (I1) and (I2) are stride-free (shallow points in row r0 and columns not divisible by 4, label columns divisible by 4). Corollary B gives N_h^int << h^(9/5+eps). Odd-odd: DM = Delta/4 - u e with e = (y_D - y_B)/2. Even-even: N = u e - Delta/4. Anchor B, phi = s_B. So E X_B7 <= 2h N_h^int (1/#P_u + 1/#L_u).

6. PROOF OF THEOREM U(u).
- U1 at stride 4u is core section 2.
  - (a) N in 16lZ, with Dt = 0 iff c1 = c2 iff N = 0. This uses that u is a unit mod 16l and |u Ds| < p.
  - (b) n - b = u i + p t with 0 <= u i <= u(A-1) < p, so (i, t) is unique. rho_s is injective because u is invertible mod 16l and 16l > h.
  - (c) t fixes (s, k).
  - (d) Two odd points: Dx/4 - u Dy/2 = DM. Two even points: Dx/4 - u Dy/2 = -N.
  Each uses only (Xi1)-(Xi3).
- Template U2 is unchanged. Fillers sit at T* - 24 + 8((n - rho0) mod 4), with rho0 from (B5'). Shallow columns are those not divisible by 4. Both are fixed by position.
- Per (sigma, phi, l, p) there is at most one configuration, whatever Xi, kappa and b are, and realisation needs only p | DM(sigma), 16l | N(sigma), or both. So the pointwise bound X_F <= Y_F^(tau,u)(l, p) holds, and Sum_{Adm_u} Y_F is at most lam Phi |Sigma| times #L_u (p-type), #P_u (l-type) or 1 (both).
- The averages are those of S1-S5. Each is uniform in u up to the prime-count constants, and better by the factor 40/P_u in the 1/#P_u terms.
- U3: in-subclass vectors are (4u Di, 2Di) and (4u Di, 2(Di+s)+1), and translations by 4(pt + b) keep the column residues mod 4 and the sawtooth phase. So R_IV(u), R_FF(u), Bad_split and R-e are (l, p)-free.
- Per chain. In the menu board of stride_menu_heavy_count Theorem W, each stride chain is its own J5 window, more than 2W_h from the others. So every counted configuration lies in one type region of one chain.
  - X^(u) depends only on (Xi^(u), kappa, b, l_u, p_u). By the pointwise form, each (l_u, p_u) can be chosen as a deterministic minimiser of Y^(u) over Adm_u, independently across u and before chi.
  - Then Y^(u)(l_u, p_u) <= avg <= 512 C_u h^(9/5+2eps).
  - Every E cell and the width bound t < 16 l_u B hold at every admissible pair.
  - The residue conditions of different chains never interact, so no joint density 2^(-m-1) for a single global p is needed.

## External results used

- Jacobi reciprocity: (Delta_u/q) = (q/Delta_u) for odd primes q not dividing Delta_u, because Delta_u = 1 (mod 4). (q/Delta_u) is a nonprincipal real character mod Delta_u, because Delta_u is not a square. This is textbook material and I did not look it up.
- Prime number theorem in arithmetic progressions mod 4 Delta_u (non-explicit), used for #L_u >= (1/2 - o(1)) 1.04h/log h and #P_u >= (1/4 - o(1)) P_u h/log h.
- r_2(n) <= 4 tau(n), and tau(n) = n^(o(1)).
- point_counts_power_saving Theorem A and Corollary B (audited in the repository): |E0(Q)| << Q^(4/5+eps) and N_h << h^(9/5+eps). Both are layout-free.

## Checks

Analytic first. I read these notes in full: stride_transfer_core, stride_transfer_table, threshold_families_random_prime and its audit, mixed_quadruples_blocks, v3_and_cross_block (plus the relevant lines of its audit), two_filler_row_lemma, point_counts_power_saving, uniformity_first_moments and its audit. I read the relevant parts of consolidated_board_v4 (B0-B10, V3-2, V3-4, the obstruction table and K4) and of stride_menu_heavy_count (Theorem W, and the per-chain primes in section 5).

One script ran with py -I in a few seconds: check_shapes_u.py in my script folder, scripts_shapes/. It computed the points from L***(u) coordinates, slot n = u i + p t + b and column 4n. It checked these with sympy:
- the I.2 form U·2n = 2[mU* + 16uaDM + (2a+T0)Ds] and the recovery n2U* = 8ua(2N - uDs);
- the II equations E1 and E2 and U1 = 4(uk + pDt);
- the II conic identity X^2 + Y^2 = U2^2(H^2 + 16u^2 Sigma^2);
- the Foo label-vertex dot product alpha(4u eps + DM) + 4e eps;
- the D8 factorisation.
All residuals were 0. It also tested the A(iii) inversion at stride 4u on 20000 random cases (u in {3, 5, 7, 9}): 0 failures.

The repository was only read. I ran no git command and did not use the web.

## Gaps

- Nothing here is audited. The proofs were derived once, by me.
- The proofs use these unaudited inputs: stride_transfer_core.md (Lemma C, U1 at stride 4u, the l-adic kills 4(i)-(iv), and the Feo and Foo-filler kills) and stride_transfer_table.md (MQ Theorem 1 at stride 4u, the Theorem 4 roles, and the D5 and D16 re-derivations). These are used as stated. I re-derived only U1(a), (b) and (d), MQ Theorem 1's size steps, and the II roles (1,1) and (1,-1).
- Theorem C(u) is complete only if v3 Theorem B's list of parked triples is complete at stride 4u. I re-derived the label-vertex cells, A(ii) and A(iii), and the SLF and FFo pair steps. The other cells (FFe, Fee, Feo, Pb, Pc with a filler vertex, SFF) I took from the core and the table as stride-free or re-derived there.
- One correction to stride_transfer_core section 3: the claim that 'A(ii) both odd, in-class, 2ua = f contradicts f odd' is a slip, because f = y_V - r0 is even for an odd vertex. The correct conclusion is the parked intra-class Pc with a = u_V/u, which exists when u | u_V and is harmless (transfer_table S6). My A(iii)(u) shows that such triples never share W.
- The p-range differs between notes: P_u = 8u^2+4 in the core and in the menu (max(40, 8u^2+4)), and c_u = 8u^2+8 in the table. My margins use P_u h as the lower end. Any dyadic range with lower end at least (8u^2+4)h works.
- Constants and h0 depend on u: PNT in progressions mod 4 Delta_u (non-explicit), and thresholds such as h >= 2u. A finite menu is needed so that one h0 works for every chain.
- Theorem U(u) needs, for chain u, that the Theorem D event has positive probability at every fixed (l_u, p_u). That is part of (V_u) (the D-group at stride 4u), and I did not check it. I also did not treat the in-class families R_IV(u) and R_FF(u) (D12, D13) or the heavy count over Q(sqrt Delta_u).
- The numerical checks test only the identities and the A(iii) inversion. There is no definition-level brute force of L***(u) families. Cross-class families need h > 128 P_u (about 10^4) even to fit in one window, so small-h censuses would be vacuous.

## Missing estimate

None for the families in scope. Every counted family keeps its order at stride 4u: A4 and D8 at h^(1+o(1)) on average, and B7, D17 and D18 at O(h^(9/5+eps) log h). Per chain the pointwise minimum is at most 512 C_u h^(9/5+2eps). For (V_u) outside this route, the open items are still R_IV(u), R_FF(u) and FF' (D12, D13), the Theorem D group at stride 4u, and the heavy count in Q(sqrt Delta_u).

## Next steps

- Have a second reader audit S1 and S2, about 1.5 pages. Check the bound on a, the N size bound (h-1)^2/(16u) + 1.5uh, the Sum over T0 of gcd(U*, ua), and the type-II triple count with 16u Sigma | H U2.
- Audit S4(a) and A(ii)/A(iii) at stride 4u, and correct the sentence in stride_transfer_core section 3 ('in-class 2ua = f contradicts f odd'): for an odd vertex it gives the parked Pc with a = u_V/u.
- Add K4 lines for L***(u): |a| < h/(8u(2P_u - u)); |N_I2| <= (h-1)^2/(16u) + 1.5uh; |N_II| <= h^2/(8u) + uh; Foo |alpha| < h/(16(P_u - u)); D8 >= 64p; F3 and D17 with 106h + 2 < 4(p - u(A-1)); two_filler Proposition 4 needs h >= 148.
- In the menu board spec, fix one pair (l_u, p_u) per chain, chosen as a minimiser of Y^(u), and record Theorem U(u) in pointwise form for each chain.
- Close the rest of (V_3): R_IV(3), R_FF(3) with FF', and the Theorem D group at stride 12.

