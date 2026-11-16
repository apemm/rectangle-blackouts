# Transfer of the obstruction table to stride 4u

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: the merged obstruction table carries over to stride 4u once the placement rule gets the u-twist and the residue conditions on p and l use 4u^2 + 1 in place of 5. With these changes no cell opens, every count keeps its order, and the thin l-margins come out at about 1.02h, below 1.04h. Under the rule with no twist, the l-adic kills of A1, A3, A5, S8 and Fee are lost, and for Fee an explicit fatal configuration is given at h = 2 x 10^7. Not audited yet.

# Result

## Status

partial

## Summary

The merged obstruction table carries over to the stride-4u board once two board-level changes are made. The placement rule needs a u-twist, rho_s = p^(-1)(u s - kappa) mod 16l, and the mod-5 residue conditions on p and l become ((4u^2+1)/p) = ((4u^2+1)/l) = -1 (for u = 3, 37 replaces 5). With these changes no cell opens, every count keeps its order, and the three thin l-margins come out at about 1.02h < 1.04h. As literally specified ('everything else unchanged'), L***(u) loses the l-adic kills of A1, A3, A5, S8 and Fee. For Fee I give an explicit position-level fatal configuration at h = 2*10^7.

## Statements

THEOREM T(u). This is proved here and not audited. It is conditional on the audited inputs (H3) and (H4) of consolidated_board_v4.md, exactly as Theorem N is.

Let u >= 3 be odd. Define L***(u)' as L***U with three changes.
- (B1'), (B4'): D_T, kappa_T and G_T are taken at stride 4u, that is, sigma = 2u in stride_menu Proposition 1'. In-class distances solve 16u^2 d^2 + (2d+T)^2 = L^2.
- (B2'): l is prime in (1.04h, 2.08h] with ((4u^2+1)/l) = -1. p is prime in (c_u h, 2 c_u h] with c_u = 8u^2 + 8 (80 for u = 3), p = 3 (mod 4) and ((4u^2+1)/p) = -1 (Jacobi symbols; for u = 3 this is (p/37) = (l/37) = -1). No mod-5 condition is needed.
- (B5'): the twisted rule. rho_s = p^(-1)(u s - kappa) mod 16l, and class k of diagonal s sits at t = rho_s + 16lk. Slot n = u i + p t + b_tau, column 4n.
Everything else ((B3), (B6)-(B10), the colouring law, the destinations, Theorems D and E, and the windows) is as in L***U.

Then:
(a) Every cell of the merged obstruction table (consolidated_board_v4 section 3) keeps its verdict (E, C or W) in L***(u)'. Every C cell keeps its order of labels hit (O(h), O(h^(3/2)), O(h^(9/5+2eps)), O(h^(11/6) log h), or the Theorem D or E routing). No cell is open. The cell-by-cell list is in the proof: 'V' marks a verbatim transfer, 'R' a transfer re-derived here, and 'F->R' a cell that fails for the literal board but holds after (B2') and (B5').
(b) The thin margins at u = 3 become: threshold Proposition 1(c) needs 1.020h, Lemma L-adic (i) needs 1.019h, and rigid Theorem 2(e) needs 1.0205h. All are below l > 1.04h, and each decreases in u.
(c) The width has the same form as in v4, with a larger constant. Light regions take at most 512 * 4 * 2c_u h * 16 * 2.08h * B (1+o(1)) columns, about 1.09*10^7 B h^2 at u = 3. The exponent theta* is unchanged, because nothing in (a) touches the heavy/light trade-off.
(d) For the literal L***(u), the kills of A1, of A3 (Proposition 1(c), and Theorem 4(c) whenever (37/p) = +1), of A5 (Lemma 4(a) whenever (37/p) = +1, and Proposition 1(d)), of S8 and of the Fee part of D6 all lose their proofs. The literal board keeps rho_s = p^(-1)(s - kappa), p = 3 or 7 (mod 20) and l = +-2 (mod 5). For Fee there is an explicit fatal configuration at the level of positions and rows (h = 2*10^7, below). The counted cells (A4, B7, D8, D11, D17, D18) keep their counts under either placement rule.

NOT PROVED: anything outside the table. heavy_light Theorem 1(b) and heavy_diagonals_sharp Lemma 1 over Q(sqrt(4u^2+1)), Theorem U's average constants, and the multi-stride menu board are not addressed. Neither is m_h = O(h^2).

## Proofs

0. INVARIANTS OF L***(u)'
Put n_u(c) := u s_c - M_c, with M_c = p t_c + b_tau. For a label (i, j) of class c, n = u i + M_c = u j - n_u(c). So both of its points satisfy x/4 = u j - n_u(c). The twisted rule gives p t_c = u s_c - kappa (mod 16l), hence n_u(c) = kappa_tau := kappa - b_tau (mod 16l). Within a region, Dn_u := n_u(c') - n_u(c) lies in 16lZ. For distinct classes Dn_u != 0, because |DM| >= p > u(h-2) >= u|Ds|.
- (I1) Odd point: x/4 = u i + M_c, so x/4 = u i + b_tau (mod p). Even point: x/4 = u j - n_u(c).
- (I2) Type congruences. i = iota (mod 32) and s = sigma (mod 16) give M_c = u sigma - kappa (mod 16), so every label slot has n = rho_tau^(u) := u(iota + sigma) - kappa + b_tau (mod 16). From this:
  - (L1): label columns are congruent mod 64, and label slots sit at offset 0;
  - (L2): odd-odd differences (4(32ua + 16b), 64a) lie in 64Z^2;
  - (L3): even-even differences lie in 64Z x 32Z;
  - (Phi): unchanged, since (B6) is unchanged;
  - (K-a) to (K-d) of three_label_one_filler hold verbatim.
  The untwisted rule also gives (I2), so (I2) does not separate the two rules.
- (I3) Sizes. In-block |Dx| <= 4u(A-1). Cross-block |Dx| >= 4(p - uA) > 314h at u = 3, and grows with c_u for other u. Two classes of one diagonal are at least 4(16lp - uA) > 5300h^2 apart, which is J4. Each residue mod 16l holds at most one diagonal, because u is invertible mod 16l and 16l > h.
- Dictionary. Every u = 1 equation becomes its stride-4u form by three substitutions:
  - in-class column step 4 Di -> 4u Di;
  - Ds - DM -> N_u := u Ds - DM (= -Dn_u);
  - the label-line norm 20 = 4 * 5 -> 4(4u^2+1).
  At u = 3 the coefficients become: 16d^2 -> 144d^2; 20d^2 -> 148d^2; 10t1 - T0 -> 74t1 - T0; 8t1 N -> 24 t1 N_u; 5 Sigma - S -> 37 Sigma - S; 10a + T0 -> 74a + T0; H^2 + 16 Sigma^2 -> H^2 + 144 Sigma^2.
- identities.py checks every identity below exactly, over 20000 random instances per u in {1, 3, 5, 7}: 0 failures.

1. LABEL-ONLY CELLS
A1 (LLL right angles): F->R.
- stride_menu Lemma 4 at s = 4u needs only x = 4u i + const (mod p) inside a region, p > (8u^2+4)h (76h < 80h) and a gap above h. All three hold by (I1) and (I3). So every tilted right angle among label points has the (E;O,E) form: V the even point of (i0, j0) in class c0, P the odd point of slot i0 + t1 of c0, and Q an even point in class c' != c0.
- With c2 = jQ - j0, the dot product is (P-V).(Q-V) = 2[c2((8u^2+2)t1 - T0) - 8u t1 N_u].
- Put g = gcd(t1, T0), t' = t1/g, T' = T0/g and b_u = (8u^2+2)t' - T'. Then b_u is odd and coprime to 8t', so b_u | u N_u. Set q := u N_u/b_u; then c2 = 8t'q.
- N_u != 0, so q != 0. Also |q| <= (K-1)/8 < h/16.
- From u(p - u(h-2)) <= |q||b_u| <= ((K-1)/(8|t'|))((8u^2+2)|t'| + |T'|):
  - at u = 3 and p > 80h: |T'| > 3622|t'|, so 0 < |b_u| < 1.0205h < l;
  - in general: |T'| > (128u^3 - 24u^2 + 128u - 2)|t'|.
- Twisted rule: l | N_u. Then l | q b_u, and l does not divide b_u, so l | q. That contradicts 0 < |q| < l. This also covers Ds = 0.
- Literal rule: DM = Ds (mod 16l) gives N_u = (u-1)Ds (mod 16l), which is nonzero mod l for every Ds != 0 (l is prime and > h). So the l-step fails for every pair of distinct diagonals. The equation c2 b_u = 8u t' N_u is then the unrestricted (E;O,E) equation of rigid_layout Derivation 2. Its first moment is positive (heuristic), but I give no instance. By the bounds above, instances need h > 2*10^6, because t1 = 0 (mod 32) forces |t'| >= 32 and |q| >= 3756.

A2 (rival pairs): V.
- In class: rival pairs are (4u d)^2 + (2d+T)^2 = L^2, that is d in S_T^(2u), and G_T^(2u)-independence excludes them (Proposition 1').
- Across classes: |t| < 2h < 314h.

A3 (I.1; II(1,1); II(-1,-1); II(1,-1) with Sigma = 0; 3 or 4 classes):
- mixed_quadruples Theorem 2: V, since it is stated for any even stride.
- Theorem 1: R. Replace 19sh by 4(p - uA) and P Dc by p Dt. The proof is the same: |2n1| < h/157, so the t-sum is 0 and |tB - tA| = |tD - tC|.
- Theorem 4 equations: R. In our layout U1 = 4(uk + DM), so the mod-p reductions are unchanged.
  - (a): E2 gives k[(16u^2+4)Sigma + 2(T0+T')] = 0 (mod p), with |bracket| < 5h < p and |k| < A < p.
  - (b): G = -32u Dd DM with G = 16u^2 Dd^2 + X^2. Here p = 3 (mod 4) and 0 < 4u|Dd| < p, so the case is impossible.
  - (c): mod p, 16u^2 k^2 = 4(4u^2+1)k'^2. This needs ((4u^2+1)/p) = -1, so it is F->R: when (37/p) = +1 the congruence is solvable, and the size bound |k - k'| <= h^2/(32u|DM|) is not below 1 for h > 1.3*10^5.
  - (d): V (parity).
- Proposition 1(c), type II(-1,-1) with Sigma != 0: F->R. Use U.2n = 4[Dj((4u^2+1)Sigma - S) - 4u Sigma Dn_u]. E2 gives |Sigma| < 2h^2/(16u(p - uA)) < h/1880 at u = 3. The twisted rule gives l | Dn_u.
  - If Dj != 0: l | (4u^2+1)Sigma - S. Since |(4u^2+1)Sigma - S| < 37h/1880 + h < 1.02h < l, we get (4u^2+1)Sigma = S. Then 4u Sigma Dn_u = 0, so Sigma = 0, a contradiction.
  - If Dj = 0: Sigma Dn_u = 0, so Sigma = 0, again a contradiction.
  - The literal rule gives only l | Ds - DM, so the step fails.
- A-24(d): V.

A4 (I.2, and II(1,-1) with Sigma != 0), counted: R.
- I.2. Write U' = (8u^2+2)a + T0 (odd) and n2 = m + Ds. Then U' n2 = 8ua(2N_u - u Ds), so N_u = (u Ds + U' n2/(8ua))/2. E2 gives |a| < 2h^2/(32up - 16u^2 h), which is below h/3768 at u = 3.
  - Skeletons: (T', b) -> (2b + T', 4ub) maps injectively into the representations of 16u^2 a^2 + (2a+T0)^2 < 2h^2, so there are at most r2 <= 4 tau skeletons.
  - n2 runs over multiples of 8ua/gcd(U', 8ua), and Sum over T0 of gcd(U', ua) <= C h tau(ua).
  - Each (skeleton, n2) fixes N_u, with 0 < |N_u| < h^2/48 + O(h) < (1.04h)^2, and fixes Ds. So DM = u Ds - N_u is fixed with |DM| < (80h)^2.
  - So at most one (l, p) realises it. The twisted rule needs 16l | N_u. The literal rule needs 16l | Ds - DM, which is fixed and nonzero. Either way the count is B' h^(1+o(1)), as before.
- II. With g = (4ud, eta) and g' = (4ud', eta'), E2 reads 4u Sigma U1 + H U2 = 0. The exact identity is X^2 + Y^2 = U2^2(H^2 + 16u^2 Sigma^2), with X = 16u^2 Sigma Dd - U2 H and Y = 4u Sigma(De + U2).
  - Integrality: 16u Sigma | H U2. The number of triples is at most Sum over Sigma of (8h^2 tau(16u Sigma)/(16u|Sigma|) + 2h) <= C h^2 log^2 h.
  - The skeleton fixes Dn_u = u Dj + H U2/(16u Sigma) and Ds, and |Dn_u| < (1.04h)^2.
  - So the count is h^(2+o(1)) skeletons, each with at most one (l, p).
- U1 becomes: |DM| <= |Dx|/4 + u|Di|, and |Dn_u| <= |DM| + u|Ds| < h^2/8 + 3uh/2 < (1.04h)^2. Theorem U's pointwise bound applies to these realisable shapes word for word.

A5 (cross-block A2 pairs): F->R for both parts.
- Odd points: D - C = (4 delta, 2 eps) with delta = u eps + DM. Being Pythagorean needs delta^2 + eps^2/4 to be a square. Mod p this is (4u^2+1) eps^2/4, so ((4u^2+1)/p) = -1 forces p | eps, hence eps = 0.
- Even points: delta = u eps - Dn_u, and the twisted rule gives delta = u eps (mod l). Then ((4u^2+1)/l) = -1 forces eps = 0.
- The literal conditions control (5/.), not (37/.). When (37/p) = +1 the congruence is solvable. For example eps = 32e and delta = 64e^2 - 1 needs p | 64e^2 - 96e - 1, which has discriminant 256 * 37.

2. LABEL AND SEA
- S0, B2, [S10], B4, M7', M9, B8, S13: V. They use rows mod 8 or mod 64, parity, block_sea Theorems 1-2 (stated for any deep layer in columns = 0 mod 4) and sea_row3 Theorem A.
- B1 (X1, X2): V.
  - v3 A(i) needs only (L1): F and G are label points, so c - a = x_G - x_F = 0 (mod 64).
  - Side remark: v3's mixed-parity line 'c - a = 2 (mod 4)' is wrong. In fact c - a = 0 (mod 4), which gives ac = 1 (mod 4) for x_E odd. The sum ac + fg is still 3 or 2 (mod 4), so the conclusion stands.
  - Corollary B M2a (ee): deep_layer A3 becomes delta = u eps (mod 16) with u odd, which still contradicts A1.
- S6 (intra-class odd Pc): R. A right angle needs 2ua = f, so the triple exists only when u | nu_V. It is parked: W is in a shallow column in an odd row.
- S7: R. Mod p, g(2ua - f) = 0. Then |2ua - f| < p gives 2ua = f exactly, so DM = 0 (one class).
- S8 (both even): F->R. The dot product is 2[Dj(2ua - f) - 2a Dn_u]. Mod l, 2ua = f. Since |a| < h/314, |2ua - f| < 1.019h < l, so 2ua = f, which contradicts f odd. This needs l | Dn_u, that is, the twisted rule.
- B3 (A(iii)): R. 2u(x_W - 4ut) - (1 - r0) - 8ub = (8u^2+2) i_V + 8up t_c, and 0 <= (8u^2+2) i_V < 8up. So W fixes i_V, then t_c, then the triple.
- B5: V. In class, Dj = Di = 0 (mod 32), so v2(e) != 3.
- B6 (R_IV): R.
  - The B3 law carries over: Delta = 4(ue + DM) and Delta = 4(ue - Dn_u), with u odd, give the same valuations.
  - In class, (I1) and (I2) with Delta = 4ue and n1 = 2 al e/be give R_IV^(u). Its edges are (q m, p m) with:
    - (al, be) odd and coprime, 0 < al < u be, and v2(u be - al) >= 3;
    - F_u = 4(al - 2u be)^2 + be^2 and g = gcd(al F_u, 4be^2(u be - al)), which divides u(4u^2+1) and is in {1, 3, 37} at u = 3;
    - q = al F_u/g and p = q + 4be^2(u be - al)/g.
  - Checked exactly on 1457 generators. At u = 1 it gives (349, 749) at (al, be) = (1, 5).
  - p < (16u^3 + 5u) be^3 (447 be^3 at u = 3; 21 be^3 at u = 1). Also q >= c_u al be^2. So kappa_IV = Sum 1/q < infinity, Lemma IV's tail at h^(1/2)/32 still costs O(h^(11/6) log h), q is odd, and the events are residue classes of i, so (AP) applies.
- B7: R. A cross-class M2c shape fixes DM = Delta/4 - ue (odd-odd) or Dn_u = u Dj - Delta/4 (even-even). In either case at most one prime realises it, under either rule, and the threshold Delta >= 78h is a superset bound.

3. LABEL AND FILLER
- D1, D2, D4, D4', D7, D9, [S4, S5, S11, S12], D10, D11: V. These cells use only:
  - the filler rows and offsets;
  - the label's own rows;
  - local slot differences between a label and fillers;
  - the row-only counts of saw (i), saw (ii) and SAW Theorem 1(6).
- D3 (T2): R. T2's labels need in-class slope 1/2, but the stride-4u class line has slope 1/(2u). So T2 itself cannot occur. Its stride-4u analogues are points of the R_FF^(u) cubic, which D12 and D13 cover.
- D5 (Feo, SAW* kill): R.
  - V-vertex with a base filler, f = 16f': Di(ug + 2f') = g^2 + f'(16f' - T_Q) - g DM. In one region DM = 0 (mod 16) and T_Q = T_P (mod 32), and the T* rule gives f'T_P = 3 (mod 4). So the right side is 2 (mod 4), while ug + 2f' is odd. Then v2(Di) = 1, against Di = 0 (mod 32).
  - Holes and v2(f) >= 5: valuations 4 against 3 and 4.
  - P-vertex: t = u Di + DM = 0 (mod 16).
  - Same label: g^2 = f'(T - 16f') = 3 (mod 4).
- D6: R.
  - FFe: V.
  - Fee: F->R. 8 alpha delta = -d eta with delta = u eta - Dn_u. In one class 8u alpha = -d, impossible by parity. Across classes, mod l, 8u alpha = -d, and |8u alpha + d| < l.
  - Foo, label vertex: alpha(4u eps + DM) = -4e eps. In class, e + u alpha is odd. Across classes, mod p, u alpha = -e.
  - Foo, filler vertex: D = 4u(e2 - e1) + DM has v2 >= 4.
- D8 (family (d)): V. Same i gives x_V2 - x_V1 = 4DM. Constant only: the family is empty for h < about 10^4.
- D12: V. With df = 0, n_y = Di, so q in the grid forces |Di| <= 210.
- D13 (R_FF^(u)): R.
  - The cubic becomes (P - 8ut)(P^2 + w^2) = 8t Y1(P + 2uw).
  - In the same row, Y2/Y1 = V_u/U_u with U_u = (a - 4ub)(a^2 + b^2) and V_u = a^3 - 4u a^2 b - 3ab^2 + 4u b^3. Checked from Lemma mixedeq on 16011 shapes.
  - gcd(U_u, V_u) | 8u(4u^2+1). Proof: an odd prime r dividing both divides a - 2ub, and then U = -2ub(4u^2+1)b^2. Its valuations are at most v_r(u) or v_r(4u^2+1), and the 2-part is at most 8. The computed values for u = 3 all divide 888.
  - Lemma FF': with k = a - 4ub, U_u = k((16u^2+1)(b + 4uk/(16u^2+1))^2 + k^2/(16u^2+1)). So kappa_FF < infinity and the tail is O(Y^(-1/3)).
- D14: R. In class, equal norms need 256(4u^2+1)k^2 = delta'^2 + 4e^2 with |e| <= 3. Then:
  - e = 0 needs 4u^2+1 to be a square, which it never is;
  - e odd fails by (N2) mod 64;
  - e = +-2 needs a square = -1 (mod 16).
  ll/FF across classes is V (two_filler Proposition 4 needs 4 * 314h > 420^2). FF/ll needs A5.
- D15: V. Lemma 1 needs Dx = 0 (mod 16) and Dy = 0 (mod 32), and Dv = (4u Di, 2Di) gives both.
- D16: R. F2: Dx = 2u Dy + 4DM. Mod p, Dy(2u n_x + n_y) = 0, and |n_x| < h/314, so 2u n_x + n_y = 0. Then n_x DM = 0, so n = 0. F1 and F3 with n_y >= 1 are V.
- D17: R. The df = 0 map to E0(Q) is stride-free, and a shape fixes DM = Dx/4 - u Di.
- D18: R. A shape fixes Dn_u. With p unique given Ds and l fixed by a nonzero integer, at most one l per p works under either rule.
- D19, D20 (Lemma Q3, Lemma N): V, because only (K-a) to (K-d) are used.
- D21 (Q4): V by inspection. Every replacement above uses p and q only through being in the strip.
- D22: R (via A(iii)).
- [V1], [V2], [V3 cross-type], [R4], [D-4F]: V.
- Windows W1-W3 and W5: V. W4 and L1: V; the gaps recounted in (I3) only grow. C2, L3 and L4: V, because they involve only fillers, sea and buffers. J4: R (constant). E3-E5: V.

4. FAILURE WITNESS FOR THE LITERAL RULE (fee_untwisted2.py)
Parameters: h = 2*10^7, u = 3, kappa = b = 0, type (iota, sigma) = (0, 3). Primes p = 1600000163 (= 3 mod 4, (37/p) = -1) and l = 39016777 ((37/l) = -1).
Untwisted placement: s0 = -3672845 sits at t0 = 599582881, and s1 = s0 + 4996896 sits at t0 + 16.
- E1 is the even point of label (6338816, 2665971), in row 5331944.
- E2 is the even point of label (2528, 1326579).
- V is the offset-0 hole, row T* - 24 = 19999945, at the slot of label (6338848, 2666003) of class c0.
- The angle at E1 is exactly right.
- W = V + E2 - E1 lies in row 17321161, inside the grid, in the double column of label (2560, 1326611) of class c1. That column's black rows are 5121 and 2653224.
- So W is white, in an odd row, in a column that has an even black point: a (V2) violation.
Every row lies in [5000, h - 5000], and the span is 1.0*10^11, well inside 2W_h. The configuration is fatal whenever the colouring puts those three labels in colour 0 and label (6338848, 2666003) elsewhere.
The search found 169536 shape solutions over 1760 prime pairs under the literal rule, and 0 over 3275 under the twisted rule, as Section 1 predicts.

5. WIDTH
Per type: 4p * 16lB + 4uA + 2(2W_h + 1) + 12. So M keeps the form C h^2(B + Lambda^(E(a)+1) B^(-a) + Lambda^2/B) ell^C1 + O(h^2 ell) + o(h^2), with a larger C.

## External results used

- Quadratic reciprocity / Jacobi symbols, to state ((4u^2+1)/p) = -1 as a congruence condition on p (for u = 3: (p/37) = -1, since 37 = 1 mod 4).
- The prime number theorem in arithmetic progressions mod 4(4u^2+1) (non-explicit). The new conditions keep the shares of v4: 1/4 of the primes for p and 1/2 for l. It replaces the mod-5 and mod-20 use in h_PNT.
- Nothing else new. Henriot's corrected Theorem 5, tau(n) << n^eps and the product-form local lemma are used exactly as in v4.

## Checks

I wrote three scripts in scripts_transfer_table/. I ran them one at a time with py, each under 60 s.
- identities.py
  - Checks the (E;O,E), I.2, II(-1,-1) and L-adic dot-product identities exactly from point coordinates in the stride-4u layout, plus the type-II algebraic identity: 0 failures over 20000 cases per u in {1, 3, 5, 7}.
  - Checks the R_IV^(u) parametrisation against (I1) and (I2) on 1457 generators: 0 failures. At u = 1 it reproduces (349, 749). At u = 3, g is in {1, 3, 37}.
  - Checks the R_FF^(u) same-row cubic from Lemma mixedeq on 16011 shapes: 0 failures.
  - gcd(U_3, V_3) over |a| <= 1500 and b < 300 takes only divisors of 888. At u = 1 it takes only divisors of 40, which matches additive_class_split.
- fee_untwisted.py: a first search at h = 4*10^6. It found 0 solutions, which is explained by the size bound: this Fee family needs h of about 10^7.
- fee_untwisted2.py: the divisor-driven search at h = 2*10^7 that gives the witness. 169536 shape hits over 1760 prime pairs under the literal rule, against 0 over 3275 under the twisted rule. The instance is re-verified point by point: right angle, W's column and rows, and every row in [5000, h - 5000].
Everything else is analytic. The repository was only read, and I ran no git command.

## Gaps

- No second reader. The cells that most need a check are the twisted-rule ones (A1, A3 Proposition 1(c), A5, S8, D6 Fee), the R_IV^(u) and R_FF^(u) parametrisations with their constants, and the I.2 and II recounts.
- The V (verbatim) cells were classified by reading each cited proof for its inputs, not by re-deriving it line by line: SAW Theorem 1(1)-(6), sea_row3 Theorem A and Corollary B, J1*, low_rows Q4, saw (i) and (ii), point_counts, and Theorem U's structure.
- Outside the table, not checked: heavy_light Theorem 1(b) and heavy_diagonals_sharp Lemma 1. Both are written for Q(sqrt 5) (for example |T| < sqrt5 h/18) and must be restated for Q(sqrt(4u^2+1)). Theorem U's average constants are also unchecked. h_PNT now refers to progressions mod 4(4u^2+1).
- The failure of A1 under the literal rule is shown only as a failed proof step plus a heuristic. No instance is exhibited; by the size bounds one needs h > 2*10^6.
- The Fee witness checks positions and rows only. Whether the random proper B-colouring realises it, by putting three labels in class 0 and one label outside it, is not modelled. Its probability is positive but not computed.
- The multi-stride menu board is not treated: one global p with every ((4u^2+1)/p) = -1, or one prime per stride, and Theorem U across strides.
- Lemma IV's constant was re-derived only to the order O(h^(11/6) log h), not to an explicit constant.

## Missing estimate

None for the obstruction table of L***(u)'. To use the stride-4u board inside Theorem N, or in the stride menu, the inputs outside the table need restating over Q(sqrt(4u^2+1)): the heavy count H_d(B/4) of heavy_light Theorem 1(b) and heavy_diagonals_sharp Lemma 1. The menu also needs a decision on primes: one global p with ((4u^2+1)/p) = -1 for every stride used, with density 2^(-1-#strides), or one prime pair per stride region.

## Next steps

- Write the twisted rule (B5') and the residue conditions (B2') into the board spec for L***(u). The literal 'everything else unchanged' spec is not valid: there is an explicit Fee witness against it.
- Have a second reader check A1, A3 Proposition 1(c), Theorem 4(c), A5, S8 and D6 Fee under the twisted rule, then R_IV^(u) (F_u, the bound p < (16u^3+5u) be^3) and R_FF^(u) (U_u, V_u, gcd | 8u(4u^2+1), 16u^2+1 in FF').
- Restate heavy_light Theorem 1(b) and heavy_diagonals_sharp Lemma 1 for Q(sqrt(4u^2+1)). The one-field proof should give the same E(a).
- For the menu, decide the primes: one global p with every ((4u^2+1)/p) = -1 and p = 3 mod 4, and one l with every ((4u^2+1)/l) = -1, or one pair per stride. Then check Theorem U and K6 step 1 across strides.
- Add the side note to v3_and_cross_block: in Theorem A(i) the mixed-parity line should read c - a = 0 (mod 4). The conclusion is unchanged.

