# Transfer of the classes, ratio graphs and sea to stride 4u

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: every class, ratio-graph, sea and gluing part carries over to stride 4u (u odd) except the placement rule, which needs the u-twist p rho_s = u s - kappa (mod 16l); without it every l-adic step breaks. Family IV does exist at (4u, 1): the ratio graph R_IV(u) and the R_FF(u) cubic are re-derived, the finiteness bounds the board needs are re-proved, and both are checked at definition level. Not covered here: the deep layer at stride 4u and the shape counts behind Theorem U. Not audited yet.

# Result

## Status

partial

## Summary

Every class, ratio-graph, sea and gluing part I was given carries over to the stride-4u board L***(u) (u odd) except one: the placement rule must change to p*rho_s = u*s - kappa (mod 16l). The rule as specified ("everything else unchanged") breaks every l-adic step. Family IV does exist at (4u,1). Its graph R_IV(u) and the R_FF(u) cubic are re-derived, all needed finiteness bounds are re-proved, and both forms are checked at definition level.

## Statements

Setting: u odd, u >= 3; s = 4u, sigma = 2u, Delta_u = 4u^2 + 1, P0 = max(40h, (8u^2+4)h). In L***(u), label (i,j) of class (s,k) sits at slot n = u*i + p*t + b_tau (column 4n), with p prime in (P0, 2*P0].

(R) PLACEMENT RULE (proved). Under the rule as specified, rho_s = p^-1 (s - kappa) mod 16l, the invariant N := u*Ds - p*Dt satisfies N = (u-1)*Ds (mod 16l). It is not 0 mod l, so the l-adic proofs fail: U1(a), threshold Proposition 1(b) (the (E;O,E) kill), Proposition 1(c), and the l-type realisation of B7ee and D18 in Theorem U. Repair: rho_s := p^-1 (u*s - kappa) mod 16l. Equivalently, slot n = u*j - kappa_tau (mod 16l). With the repair, N = 0 (mod 16l), each residue still holds one diagonal, the width is unchanged, and the failed steps hold again (proofs below). heavy_light Proposition R, which is audited for every even stride, gives the same rule. I do not claim an explicit violation under the unrepaired rule. What I prove there is that the kill's proof fails and only a 2-adic constraint, v2(c2) >= 7, is left.

Verdict by part (with the repaired rule):
1. G_T and the colouring law (B4). Proposition 1' holds verbatim at any even stride. Lemma 2 holds with sigma = 2u, in its Kronecker-character form (Delta_9 = 325 gives the field Q(sqrt 13)). heavy_diagonals_sharp Proposition 3(a),(b) holds verbatim with kappa_T^(u) = |D_T^(2u)|.
2. R_IV. Family IV EXISTS at (4u,1) for every odd u. Corollary 5 depends only on v2(mu) - v2(nu) = 2, and inside a class Delta = 4u*e gives v2(Delta) = a + 2. Re-derived graph (Theorem R4): edges (q*m, p*m), m odd, over coprime odd pairs (al, be) with 0 < al < u*be and v2(u*be - al) >= k - 2. Here F_u = 4(al - 2u*be)^2 + be^2, g = gcd(F_u, u*be - al) divides Delta_u, q = al*F_u/g and p = (al*F_u + 4(u*be - al)*be^2)/g. Even-even in-class M2c is empty. Lemma IV(u): q >= al*be^2 and p >= 4u*be^3/Delta_u. The graph has O_u(X) edges on [1,X], the sums of tau^C/q and tau^C/p are finite, and the R-e set has O_u(h^(11/6) log h) labels.
3. R_FF. Theorem F at r = 4u holds (re-derived by hand from Lemma mixedeq): U = (a - 4ub)(a^2 + b^2), V = a^3 - 4u*a^2*b - 3a*b^2 + 4u*b^3, and gcd(U,V) divides 8u*Delta_u. F2(i) holds verbatim for odd u: in-class Fo/Fo needs a odd, b even, w = 0, v2(A) = beta + 1 and v2(t) = 2*beta + 4, with 2u < a/b < 4u. R_IV(u) lies on the same cubic via (a,b) = (4u*be - 2al, be). R_FF^+ holds verbatim (|Di| <= 210, at most 6 neighbours on each side). The sum of 1/|U| is finite, and the shapes with |U'| <= H number O_u(H^(2/3)).
4. Bad_split and Theorem D. (B8) and the two hypotheses of Theorem D hold in the same form, with kappa = max over the menu of kappa(u) < infinity. Theorem DC with Lemma M transfers. M0 needs a bounded root count at the primes dividing disc C_u (for u = 3: 2^4 3^3 19 43). That count is supplied by Hensel clustering. additive_class_split Lemmas 1, 2 and 4 are re-derived (item 3). truncated_additive_split is not used by the board; its Lemmas A-C transfer with constants depending on u.
5. Theorem U. The template U2 and Lemma U3 hold verbatim. U1 needs (a') Dn := u*Ds - p*Dt = 0 (mod 16l) and (d') Dx/4 - u*Dy/2 = DM for odd points and -Dn for even points. The bound for B7 transfers verbatim. The A4, D8, D17 and D18 shape counts must be re-derived in their source notes (NOT DONE).
6. sea_census_rigid. B3 in class transfers verbatim, and B4 is replaced by R_IV(u). B1 is re-derived: Dj(Delta_u*Sigma - S) = 4u*Sigma*Dn with |Sigma| < h^2/(8u(p - 1.5u*h) - h). Proposition 1(c) holds under the repair, with the margin |Delta_u*Sigma - S| < 1.022h < l at u >= 3. The Sigma = 0 analogue gives Delta_u(delta - Ds)^2 - (2u*Ds)^2 = 0 (mod p), so the condition p = +-2 (mod 5) becomes (Delta_u/p) = -1. B2 is not re-derived.
7. sea_row3_split. Theorem A transfers verbatim, because its conditions concern rows of deep points only. Corollary B: (H1)-(H4) hold. The excluded low label-label M2c needs |Di| in {1,2}, which the mod-32 split excludes. Shallow M2a between even labels is still excluded by A1, because delta = u*eps (mod 16) and u is odd.
8. Heavy-light. Proposition R holds verbatim (any even stride). Theorem 1(b) for the menu is audited and gives the heavy count h*Lambda^(beta_m(a))*B^(-a) with beta_m(a) = ((1 + 3^(a/m))/2)^m - 1.
9. Gluing. J3 and J5 hold verbatim. J4 holds with spacing 4(16lp - uA) > 2600h^2. Theorem E/N1 blocks do not depend on the stride. Several stride families sit as separate regions in the rigid chain. Their 2W_h+1 pure-filler margins make every seam (J1*, J2, cell L1) independent of the stride, at O(h^2) per stride.

CONDITIONAL CONSEQUENCE (not proved). Suppose the parts outside this route transfer: the deep layer (SAW*, D1-D21), the A4/D8/D17/D18 counts, and the residue conditions on l and p. Then the menu {4u_1, ..., 4u_m} gives m_h <= C h^2 (log h)^(x_m) (loglog h)^C, with x_m = min_a (beta_m(a) + 2)/(1 + a): 1.4295 for m = 2 and 1.3690 for m = 5.

## Proofs

NOTATION. u is odd. Label (i,j), s = j - i, T = 2s + 1. Slot n = u*i + p*t + b_tau, and both points of the label are in column 4n. Inside a class (fixed t), two labels differ by (4u*Di, 2Di). Classes are split by i mod 32 (types).

1. THE PLACEMENT RULE.
(E;O,E) identity. Let V be the even point of label (i0,j0) in class c0, P the odd point of slot i0 + t1 in c0, and Q the even point of a label in class c'. Then VP = (4u*t1, 2t1 - T0) and VQ = (4(u*DI + DM), 2c2), where DI = iQ - i0 = c2 - Ds, c2 = jQ - j0 and DM = p*Dt. VP.VQ = 0 gives 8u*t1*(u*c2 - u*Ds + DM) = c2(T0 - 2t1), so
 c2(T0 - 2*Delta_u*t1) = -8u*t1*N, with N := u*Ds - DM.
(i) Unrepaired rule. p*rho_s = s - kappa gives DM = Ds (mod 16l), so N = (u-1)*Ds (mod 16l). This is nonzero mod l whenever Ds != 0 (mod l) (l > u, so l does not divide u - 1). Nothing then forces l | c2, so the kill of threshold Proposition 1(b) does not go through. Inside a type Ds = 0 (mod 16), so N = 0 (mod 16) still holds, and the only remaining consequence is v2(c2) = 3 + v2(t1) + v2(N) >= 7. That is the partial 2-adic rule, which by itself is known to leave survivors at stride 4 (rigid Theorem 4(a)). I did not construct an explicit survivor here. The same N carries U1(a), the l-adic B1 kill and the l-type realisation (sections 5 and 6), so all of these lose their proofs.
(ii) Repaired rule p*rho_s = u*s - kappa (mod 16l). Now DM = u*Ds (mod 16l), so N = 0 (mod 16l). N != 0, because |u*Ds| < u*h < p <= |DM| when Dt != 0. Since l does not divide 8u, l | c2(T0 - 2*Delta_u*t1).
- Bound on t1: |X1 X2| = |Y1 Y2| with |X2| >= 4(p - uA), |Y1| < h and |Y2| < h. So |t1| < h^2/(16u(p - uA)).
- Hence 2*Delta_u*|t1| < (4u^2+1)h^2/(8u(p - uA)). At u = 3 and p > 76h this is < 0.0207h, and for every u >= 3 with p > (8u^2+4)h it is < h/(16u)(1 + o(1)).
- So |T0 - 2*Delta_u*t1| < 1.021h < l, and the number is odd, hence nonzero mod l. Also |c2| < K < l. So c2 = 0, which forces t1*N = 0, a contradiction.
- Positions: t ranges over one residue class mod 16l per diagonal, and s -> u*s mod 16l is injective on |s| < h because gcd(u, 16l) = 1. So each residue still holds one diagonal, and the mod-16 rule reads n = rho_tau := u(iota + sigma) - kappa + b_tau (mod 16).
- Cross-check: heavy_light Proposition R (audited, any even s) puts class c at columns s(i + p*m_c) with p*m_c = s_c - kappa. In board units (4 columns) this is M = u*p*m_c, so u*s_c - M = u*kappa: the repaired rule up to the constant.
(iii) Lemma 4 at the board placement. Columns satisfy x = 4u*i + 4b (mod p), so the mod-p case analysis of stride_menu Lemma 4 runs unchanged:
- (O;O,O): the dot product is 4*Delta_u*Di1*Di2 (mod p), and p does not divide 4*Delta_u.
- (O;O,E): the bracket is 2 (mod 4) and < (8u^2+4)h < p.
- Blocks are 4(p - uA) > h apart.
So only the (E;O,E) type is left, and (ii) kills it.

2. G_T AND (B4). Proposition 1' is proved for every even s. At s = 4u it gives monotone, rival-free, right-angle-free classes whenever a class is G_T^(2u)-independent and is placed at columns 4u*i + const, which is the board placement. Lemma 2: X' = 2*Delta*d + T satisfies X'^2 - Delta*L^2 = -sigma^2 T^2, and Y^2/n = 4(sigma^2+1)h^2/(sigma^2 T^2) <= 8h^2/T^2 < (3h/T)^2, so the bound holds with tau(4u^2). For Delta_9 = 325 = 5^2 * 13, the prime 5 is inert in Q(sqrt 13), so the Kronecker-character form of g_sigma is needed and suffices. Proposition 3(a),(b) uses only deg <= 2|D_T ∩ 32Z| <= 2*kappa_T < B/2 and the conditional uniformity of chi(v), so it holds verbatim. On a menu, T is light iff min over u of kappa_T^(u) < B/4. Then T takes u(T) = argmin, a deterministic choice, so independence across T is kept. Proposition 4(a) still holds: two classes of one diagonal are >= 4(16lp - uA) > 2600h^2 apart (this is also the J4 constant).

3. R_IV AT (4u,1) (Theorem R4). Take the audited M2c equations (block_sea Theorem 2, rewritten as (I1) e*u2 = n1(Delta + w) and (I2) (Delta - 2n1)w = e^2 + n1^2). These do not depend on the stride. The 2-adic tie law (ratio_graph Theorem 4) uses only these equations, a >= 4 and v2(z) <= 1.
- Inside a class Delta = 4u*e, so delta - a = 2 for every odd u. Corollary 5 then forces (c, zeta) = (1, 0) for odd-odd pairs (family IV) and gives no solution for even-even pairs.
- Write r = n1/e, so v2(r) = 1 and r = 2al/be. (I2) gives w = e(1 + r^2)/(4u - 2r). Then (I1) with u2 = 2v gives 2v = r*e((r - 4u)^2 + 1)/(4u - 2r) = al*e*F_u/(2be^2(u*be - al)). Positivity forces 0 < al < u*be.
- z = -v*be/al must be an integer, so al | v.
- gcd(F_u, be) = 1, and modulo u*be - al we have F_u = (4u^2 + 1)be^2, so g := gcd(F_u, u*be - al) divides Delta_u. Hence v = q*m with m odd, and v + e = p*m.
- v2(e) = 2 + v2(u*be - al), so the mod-2^k split keeps exactly the pairs with v2(u*be - al) >= k - 2.
- The corner C is shallow because 2n1 = 0 (mod 4). The converse is block_sea's audited converse.
- Lemma IV(u): |al - 2u*be| > u*be gives F_u > Delta_u*be^2, so q >= al*be^2. On [0, u] the cubic C_u(x,1) = 4x^3 - 16u*x^2 + (16u^2 - 3)x + 4u is smallest at the endpoints, with minimum 4u, so p >= 4u*be^3/Delta_u. Since al < u*be, the sum over lambda of 1/q is at most the sum over be of (1 + log(u*be))/be^2, which is finite. Pairs with p > Y have be >> Y^(1/3), with tail << Y^(-1/3) log Y. There are << h^(2/3) pairs with q <= h. As in polylog Lemma IV, the R-e set therefore has O_u(h^(11/6) log h) labels.
- q is odd ([G11]).
- Dilation (Lemma 2 and Corollary 3 of ratio_graph) holds verbatim.
Smallest edges: u = 3 gives (101,109) at k = 3 and (1165,1453) at k = 5; u = 9 gives (1157,1189) at k = 5.

4. R_FF AT (4u,1).
- Theorem F re-derived: put A = L1, B = F1, D = L2 and C = F2 in Lemma mixedeq, with U = F1 - L1 = (alpha1, Y1), V = F2 - L2 and L2 - L1 = (4ut, 2t). This gives 2n = (8ut - P, 2t), (8ut - P)alpha1 + 2t*Y1 = 0 and P(alpha1 + alpha2) = 4t^2 - 4t*Y1. Eliminating alpha1 gives 8t*Y1(4ut - P) = (8ut - P)(P^2 + 4t^2). With P = 2tm: Y1 = t(4u - m)(m^2 + 1)/(4u - 2m) and Y2/Y1 = V/U for the U, V of the statement. At u = 1 this is the audited (iii-b) cubic.
- Content: U - V = 4b^2(a - 2ub). An odd prime l dividing both divides a - 2ub. Then U = -2ub^3*Delta_u (mod l), so l | u or l | Delta_u. For l | Delta_u, v_l(a^2 + b^2) = v_l(Delta_u) once v_l(a - 2ub) > v_l(Delta_u). For l | u, min(v_l(U), v_l(a - 2ub)) <= v_l(u). So gcd(U,V) divides 8u*Delta_u.
- F2(i): Y1 = 4A(a - 4ub)/b and t = 8A(a - 2ub)b/(a^2 + b^2). The four cases of the stride-4 proof use only v2(a - 4ub) and v2(a - 2ub), which are the same for every odd u:
  - b odd, a odd: v2(t) = 2 + v2(A) >= 5 forces w = 0, but then v2(Y1) >= 5 while w + c is odd. Impossible.
  - b odd, v2(a) = 1: v2(Y1) = 3 + v2(A), which matches no w. Impossible.
  - b odd, 4 | a: v2(t) = 4 + v2(A) forces w even, so v2(Y1) should be 3, but v2(Y1) >= 5. Impossible.
  - b even, a odd: w = 0, v2(A) = beta + 1 and v2(t) = 2*beta + 4. The same-row condition holds because v2(ut) >= 6 and v2(P/4) = beta + 3. Fillers sit at slot offsets = 4 or 8 (mod 16), so never on a label slot.
- Finiteness: |U| = |k|(a^2 + b^2) with k = a - 4ub, and a^2 + b^2 >= k^2/(16u^2 + 1). So the sum of 1/|U| is at most the sum over k of (2(16u^2+1)/k^2 + pi/|k|^2)·C, which is finite. Shapes with |U| <= X number O(X^(2/3)) (|k| << X^(1/3)), and the tail is << W^(-1/3).
- R_FF^+: the d > 0 bound N_y = 2d <= H0 involves rows only, so |Di| <= 210 and Di = 0 (mod 32) give at most 6 neighbours on each side.

5. BAD_SPLIT, THEOREM D, DC, THEOREM U.
- u_f = (2i + 1 - r0)/2 and the eight depths Y_o - 2i - 1 and Y_o - 2j - 2 depend on rows only. They are affine in i within a type, so V2-3 and ap Lemma 4 hold verbatim, with modulus lcm(32, q) <= h^(1/2) at the cutoff h^(1/2)/32.
- The weighted hypothesis allows Q_T to depend on T, so kappa = max over u of (kappa_IV(u) + kappa_FF(u)) < infinity.
- Lemma M, M0 for the IV family: C_u(al,be) = g*n with g | Delta_u. C_u lies between 4u*be^3 and C'_u*be^3, which bounds the box. Primes not dividing disc have <= 3 roots mod p^e. For p | disc with delta = v_p(disc), the root count is bounded by Hensel clustering: if e > 2*delta and f(x) = 0 (mod p^e), then v_p(f'(x)) <= delta (because disc = A*f + B*f'), so x is within p^(e - delta) of one of the <= 3 p-adic roots. That gives <= 3p^delta classes mod p^e. disc C_3 = 2^4 * 3^3 * 19 * 43, and in general the discriminant of V_{4u}(x,1) is 4(r^4 + 9r^2 + 27) with r = 4u. So R_IV(n) <= C_u tau(n)^2.
- M0 for the FF family: R_FF(n) <= C tau(8u*Delta_u*n).
- Lemmas M1-M3 do not use the stride. So DC (a)-(d) holds with constants depending on u.
- Theorem U: U1(a') and (d') are computed in section 1. U1(b) holds because 0 <= u*i < uA < p, so division by p recovers (u*i, t), and s is recovered from u*s mod 16l. U3 holds because in-subclass vectors are (4uDi, 2Di) and (4uDi, 2(Di + s) + 1) and the filler row depends on the slot mod 4.
- B7: its shape count N_h^int is stride-free. Odd-odd is p-type with DM = Delta/4 - u*e, and |DM| < h^2/8 + uh/2 < P0^2. Even-even is l-type with 16l | Dn under the repair.

6. SEA NOTES.
- B1 at (4u,1): 2n = (4u*Sigma, 2Sigma - T0 - T') and U = (4(u*Dj - Dn), 2Dj) give Dj(Delta_u*Sigma - S) = 4u*Sigma*Dn. |u*Dj - Dn| >= p - 1.5uh gives the Sigma bound. If Dj != 0, the prime l divides Delta_u*Sigma - S, which is smaller than l, so Delta_u*Sigma = S, and then Sigma = 0, a contradiction. If Dj = 0, then Sigma = 0 directly.
- The Sigma = 0 case: (delta - Ds)^2 + 4u^2*delta^2 = 8u*delta*Dn, and Dn = u*Ds (mod p) gives Delta_u(delta - Ds)^2 = (2u*Ds)^2 (mod p).
- B3 in class: v2(4ue) = a + 2, so the stride-4 proof applies word for word.
- sea_row3 2(iii): B - D = (4ut, 2t) with t = e in {1,2} is impossible in a class. |beta| <= 6h is far below the block gap.
- (H4): in different blocks |Dx| >= 4(p - uA) > 2h; in one class, Dy = 2 needs Di = 1.
- A3: in a type, Dn = u*Dj (mod 16), so delta = u*eps (mod 4). A1 needs eps odd with delta even, or eps = 2 (mod 4) with delta = 0 (mod 4). Both fail for odd u.

7. GLUING. J5 is stride-free. Every region begins and ends with 2W_h+1 columns of pure SAW*-shift, whose rows depend only on the type. So every seam with Sea(r0,g) or all-g is the stride-4 seam, and no violation (span <= 2W_h + 1) meets two regions. A menu of m strides adds O(m h^2) columns. WE receives the labels that are heavy for every stride (cost C h^2 Lambda^(beta_m(a)+2) B^(-a) ell^C). One WD group serves all strides.

CHECKS (scripts in the script folder, each well under 60 s; analytic work came first).
- riv_u.py / run2.py: a definition-level search of in-class M2c at stride 4u (row-1 sea, every witness A found through the divisors of e(y_B - 1)) matched the predicted R_IV(u) edge set exactly, in both directions: u = 3 at h = 2400, 2600 and 3000 (mod 8 and mod 32 classes), u = 5 and u = 9 at h = 2400, and u = 1 at h = 8000 (edge (1237,3829), k = 5).
- fofo_u.py: at u = 1 it recovers (5,2) at t = -320 and (7,2) at t = -960. At u = 3 it finds nothing below h = 5000, which is consistent with the smallest predicted depth of 21320.
- fofo_construct.py: builds predicted Fo/Fo quadruples at u = 3, 5, 9 (for example (23,2) with depths 21320/28360 and t = -3520) and confirms every condition of Lemma mixedeq and every 2-adic prediction.
- disc.py: computes the discriminants.

## External results used

- None beyond those already used in the audited notes: Hensel's lemma, in the clustering form proved inline in section 5, and the resultant identity disc = A*f + B*f'.

## Checks



## Gaps

- The deep layer at stride 4u is NOT covered: SAW*/SAW*-shift, the label-filler cells D1-D11 and D14-D21, the Feo kill, L-adic (i)/(ii), S1L and the Q3/Q4 low-row lemmas. These use the (4,1) class line (slot offset to row), for example 'c_Q = c_P mod 2^(nu+1)' and 'slot offsets mod 4 on the class line'. They are outside this route and must be redone. full_layout_junctions §0 says these parts do not exist for stride 12. That is wrong for the shallow/deep split and the sigma = 2 2-adic laws covered here, but it is still unchecked for the deep layer.
- The Theorem U shape counts for A4 (I.2 and II skeletons), D8, D17 and D18 must be re-derived at stride 4u in threshold_families, v3_and_cross_block and two_filler_row_lemma. Only B7 and the template were transferred.
- The residue conditions on l and p are stride-4 (Q(sqrt 5)) arithmetic. I derived only the II(-1,-1), Sigma = 0 analogue, which needs (Delta_u/p) = -1. The l-condition of threshold Proposition 1(d) (SAW Lemma 4(b)) and mixed_quadruples 4(a),(b),(d) were not redone. sea_census B2 (I.2) was not redone either.
- Under the rule as literally specified, I proved only that the l-adic proofs fail. I did not construct an explicit (E;O,E) survivor.
- Theorem F and F2 were unaudited in degree_capped_colouring. I re-derived both by hand at r = 4u, but no second reader has checked this note.
- The R_FF definition-level search at u = 3 was not run at the heights where the family first appears (h > 28000). The u = 3 instances were checked constructively only.
- The constants depend on u: P0 = (8u^2+4)h widens the light regions by about (8u^2+4)/40, and kappa(u) and the R-e constant grow with u. This is fine for a fixed menu, and none of it is explicit.
- The exponent x_m (1.4295 for m = 2, 1.3690 for m = 5) is CONDITIONAL on the parts not covered here. Theorem N's exponent is not changed by this note.

## Missing estimate

None for the parts assigned here, once the placement rule is repaired. For the full stride-4u board, three things are still missing: (1) the deep-layer cells (SAW*-shift with labels on a slope-1/(2u) line), (2) the A4/D8/D17/D18 shape counts at stride 4u, and (3) the quadratic-residue conditions on l and p with Delta_u in place of 5.

## Next steps

- Amend the L***(u) specification: rho_s := p^-1 (u*s - kappa) mod 16l (slot n = u*j - kappa_tau mod 16l), p prime in (P0, 2*P0] with P0 = max(40h, (8u^2+4)h), and p = 3 (mod 4) with (Delta_u/p) = -1 in place of p = 3, 7 (mod 20).
- Use a menu with u_i = 1 (mod 2^K), K about 7, for example built by CRT with primes p_i | 4u_i^2 + 1 dividing exactly once. Then 4u = 4 and 16u^2 = 16 modulo 2^(K+2), and multiplying by u preserves every residue mod 2^K. So every purely 2-adic case analysis of the deep layer carries over word for word, and only the size bounds and the residue conditions on l and p change. With u = 3 the classes 1 and 3 mod 4 swap, which can matter for the four sawtooth rows. (This is a recommendation, not checked cell by cell.)
- Redo the deep-layer cells (SAW Theorem 1, the saw_residual kills, BH16 A3, L-adic, S1L, Q3/Q4) at stride 4u, starting with the SAW* Feo kill and L-adic (i), which use the class-line slope.
- Redo threshold Theorems 2-3 (I.2/II skeletons, where 10a + T0 should become 2*Delta_u*a + T0), v3 Proposition D and two_filler Theorem 3 at stride 4u, then reapply Theorem U with U1(a'), (d').
- Have a second reader audit sections 1, 3 and 4 of this result: the repaired rule, R_IV(u) and Theorem F/F2 at r = 4u.

