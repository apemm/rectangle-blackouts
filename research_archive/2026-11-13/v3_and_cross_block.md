# V3 collisions and cross-block families

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: V3 between parked SLL triples is empty in L**. In SAW* with two constant-cost changes, the only V3 family left hits h^(1+o(1)) labels in expectation over p. S3-low is empty. One cross-block branch reduces to a count N_e(h), which is open. Not audited yet.

# Result

## Status

partial

## Summary

Four of the six families are empty or harmless. V3 between parked SLL triples is empty in L**. In SAW* with two constant-cost changes (R1: fix s mod 16 per region type; R2: relocate the O(h) labels with 2i+1 <= 177), the only V3 pairs left are family (d), which hits h^(1+o(1)) labels in expectation over p. (c) and (f) are empty, and so are most of the (e) shapes. One (e) branch reduces to a single count, N_e(h) <= h^(2-delta), which I could not prove.

## Statements

SETTING. One region R_tau of L** (full_layout_junctions.md): stride 4, rigid rule n(c) = s_c - M_c = kappa (mod 2^nu) with 2^nu >= K, M_c in b_tau + pZ, distinct m_c, p prime in (20h, 40h] with p = 3 or 7 (mod 20), sea row r0 in {1,3}, and the exclusions of (P5) (near band: 2i+1 >= T* - 128). Filler layer SAW* of saw_residual_families.md: classes split by i mod 32, and T* = y_P + 32 (T = 3 mod 4) or y_P + 48 (T = 1 mod 4) (mod 64), T* >= h - 63. Where stated, I add two constant-cost changes:
 (R1) s is fixed mod 16 in each region type, not the pair {c, c+4}. This doubles the type count, keeps (Hs), and gives M_c - M_c' = 0 (mod 16) inside a region.
 (R2) The labels with 2i+1 <= 177 are relocated. There are O(h) of them.
Notation: lambda(P) = 2y_P - x_P. Then lambda = 2 - 4M_c exactly for odd label points and lambda = 4 + 4n(c) exactly for even ones. Also u_V = (y_V - r0)/2, which is odd for odd label points.

THEOREM A (SLL triples; L** only, with no SAW, R1 or R2). Let a tilted rectangle have one shallow corner E and two label corners among its black corners (at least 3).
 (i) E is never the corner opposite W, for any parities of the two labels. So Pa and Pb are empty, and so are X1-type configurations.
 (ii) With E adjacent to W, vertex V and other end G, the points V and G are odd points of ONE class: G = V + (4t, 2t) with t > 0 and t = 0 (mod 16), E = V + (u_V, -2u_V), W = V + (u_V + 4t, 2t - 2u_V), and row(W) = r0 + 2t. Even-even Pc and mixed-parity Pc/X2 are empty.
 (iii) W determines the triple. Hence V3 between two parked SLL triples (O2(d)) is EMPTY.

THEOREM B (complete list of parked triples; SAW*, R1, R2). Every tilted rectangle with 3 black corners and white W in R_tau is one of the following.
 - W in a shallow column: the intra-class Pc of Theorem A, or an SLF-Pc: V an odd label point, E shallow (adjacent to W), G a HOLE filler with G - V = (4gamma, g), 2a gamma = u_V g, a = x_E - x_V. Here either G is at slot offset 0 (row T*-24, v2(gamma) = 2, a odd) or at offset 2 (row T*-8, v2(gamma) = 1, a = 2 mod 4). Always v2(g) = 3, and W = G + (a, -2u_V).
 - W in a deep column: only FFo with vertex V an offset-0 hole (row T*-24), label end L (odd), other end F2 at offset o2 in {1,2,3}: W = L + (4beta, 8o2), with alpha' beta = E1 o2, E1 = (T*-24-y_L)/8, and V = L + (-16alpha', 8E1).
 - EMPTY: Pb with one label and one filler (needs 2i+1 <= 90, removed by R2); Pc with a filler vertex and a label end; SFF; FFe (every vertex type); Fee; Feo (every vertex type, any blocks, W anywhere); Foo with a label vertex (needs only p > 20h); Foo with a filler vertex (needs R1); LLL; FFF.

THEOREM C (V3; SAW*, R1, R2). Every V3 pair in R_tau is a pair of SLF-Pc triples of family (d): V1 and V2 are odd label points with the SAME i in DIFFERENT classes, and G1, G2 are holes in the same row. In particular:
 (b) FFo/FFo, FFe, FFo/SLF and every one-label pair other than family (d) are empty;
 (c) V3 between a filler triple and an SLL triple is EMPTY;
 all V3 at a deep-column W are EMPTY.

PROPOSITION D (family (d), the audit's cross-block Pc|Pc collisions). Put N = u g/2 and gamma_k = G e_k with gcd(e1, e2) = 1, and R = N/(G e1 e2), which is an integer. Then x_V2 - x_V1 = (e1 - e2)(4G - R) = 4(M2 - M1), with M2 - M1 in pZ \ {0}.
 (1) In L**, |x_V2 - x_V1| >= 16p > 320h, and >= 32p under R1. Since the pair must fit in 2W_h + 1 columns, the family is empty for h < 640 (resp. about 1280).
 (2) It SURVIVES at true spacing. A definition-level census finds realized (shape, p) pairs at h = 3000 (4 over 1329 primes) and h = 5000 (44 over 2101 primes). Example at h = 3000: y_V = 1243, hole row 2915, gamma1 = -15732, a1 = -33, gamma2 = -519156, a2 = -1, difference 2013664 = 32·62927, with p = 62927 = 7 (mod 20).
 (3) For p drawn uniformly from the admissible primes, E_p[#labels in family (d)] <= h^(1+o(1)). The relocation rule absorbs this.

PROPOSITION E (f, S3-low). In SAW*, no three points {filler, odd label point, even label point} form a right angle at all (any vertex, any blocks, one label or two). So S3-low (W in row 2, row-3 types) is EMPTY. Under R1 no deep-only corner triple has its white corner in row 1 or 2.

PROPOSITION F (e, cross-block two-label quadruples with two fillers; odd-odd unless stated).
 (F1) Side two fillers, diagonal two labels: EMPTY. A horizontal side is S5, killed by audited Lemma 4.
 (F2) Side two odd labels of different classes, diagonal anything: EMPTY. This holds for any mixed quadruple, by a mod-p argument.
 (F3) Side {L1, F1}, diagonal {L2, F2} (the inhomogeneous cubic). Write n = (C+D-A-B)/2, so n_y = (Dy - (f1-f2))/2.
  - If n_y >= 1, then |Dx| < 45h. Cross-block needs |Dx| >= 78h (odd) or >= 74h (even), so this branch is EMPTY, for oo and ee alike.
  - If n_y <= -1, everything reduces to one count. Put N' = -n_y, A' = f2 - y_L1, df = f1 - f2, Y1 = A' + df, k = |n_x|. Then
   N_e(h) = #{(y_L1, Dy, f1, f2, k, w) : k(w^2 + (N'-df)(N'+A')) = w N' Y1, k even, |Dx| >= 78h}.
   This gives E_p[#labels hit] = O(N_e(h) log h). Trivially N_e <= h^(2+o(1)), and heuristically N_e = h^(1+o(1)). NEEDED (OPEN): N_e(h) <= h^(2-delta). The census found N_e = 0 for h <= 2000, and the largest |Dx| over all shapes (with no span threshold and no 2-adic filters) was about 28h for h <= 1500.
NOT PROVED: N_e <= h^(2-delta); the even-even version of the n_y <= -1 branch; even-even side-two-labels quadruples; deep-only mixed quadruples with p or q in rows 1-2 in row-3 types (other than S3-low).

## Proofs

0. FACTS USED.
(L) Odd label point of class c: (4n, 2i+1) with n = i + M_c, so lambda = 2 - 4M_c. Even point: (4n, 2j+2), so lambda = 4 + 4(s_c - M_c) = 4 + 4n(c). In one region: (a) M_c in b_tau + pZ, and distinct classes have distinct M_c; (b) M_c - M_c' = s_c - s_c' (mod 2^nu), which is = 0 mod 4 in L** and = 0 mod 16 under R1; (c) i is fixed mod 16 (mod 32 in SAW*), and j = i + s is fixed mod 2; (d) n(c) = kappa (mod 2^nu) with 2^nu >= K.
(N) Point coordinates differ by less than h in rows. Any two points of one class are close in columns. Points of different classes are at least 4(p - h) > 76h apart in columns.
(S) SAW* rows. Holes (offsets 0, 2) sit at rows T*-24 and T*-8, bases (offsets 1, 3) at T*-16 and T*. Relative to y_P (mod 64), the offsets o = 0,1,2,3 sit at +8, +16, +24, +32 when T = 3 (mod 4), and at +24, +32, +40, +48 when T = 1 (mod 4). So a hole-to-label row difference has v2 = 3, and a base-to-label difference has v2 in {4, 5}. Label slots have offset 0.

1. THEOREM A.
(i) Let E be the corner opposite W, so E is the right-angle vertex of F and G. Write a = x_F - x_E, c = x_G - x_E, f = y_F - r0, g = y_G - r0, so that ac + fg = 0. By (L), c - a = x_G - x_F = 2(y_G - y_F) - (lambda_G - lambda_F).
 - F, G both even: lambda difference = 0 (mod 4), so c = a (mod 4). If x_E is odd, ac = 1 (mod 4); f and g are odd with f = g (mod 4) by (L)(c), so fg = 1 (mod 4). The sum is 2 (mod 4). If x_E = 2 (mod 4), then ac = 4 (mod 8) while fg is odd. Contradiction either way.
 - F, G both odd: f = 2u_F, g = 2u_G with u_F = u_G (mod 4) by (L)(c). If x_E is odd, ac is odd and fg is even. If x_E = 2 (mod 4), put a = 2a', c = 2c'. Then a'c' = -u_F u_G, and c' - a' = 2(u_G - u_F) + 2(M_G - M_F) = 0 (mod 4) by (L)(b). So a'c' = 1 but -u_F u_G = -1 (mod 4).
 - Mixed parity: y_G - y_F is odd, so c - a = 2 (mod 4). If x_E is odd, ac = a(a+2) = 3 (mod 4) and fg = 2 (mod 4). If x_E = 2 (mod 4), ac = 0 (mod 4) and fg = 2 (mod 4).
(ii) Let V be the vertex, with E - V = (a, -f), f = y_V - r0, and G - V = (4gamma, g). The right angle gives 4 gamma a = f g, and W = G + (a, -f) has row r0 + g.
 - V odd, G even: v2(fg) = 1 < 2.
 - V even, G odd: fg is odd.
 - Both even: f is odd, and 4gamma = 2g - 4Dn with Dn in 2^nu Z by (L)(d). If v2(g) <= nu, then v2(gamma) = v2(g) - 1 and v2(a) = -1. So v2(g) >= nu+1, which gives |g| >= 2^(nu+1) >= 2K > |g|. Contradiction.
 - Both odd: Dx := x_G - x_V = 2g + 4DM with DM in pZ. Reducing a·Dx = f g mod p gives g(2a - f) = 0 (mod p), and 0 < |g| < h < p, so 2a = f (mod p). If DM != 0, then |Dx| >= 4p - 2h and |a| < h^2/(78h) < h. If DM = 0, then a = f/2. In both cases |2a - f| < 3h < p, so 2a = f exactly, and then Dx = 2g and DM = 0. So V and G lie in one class, G = V + (4t, 2t), a = u_V (odd, so E is shallow), and t = 0 (mod 16) by (L)(c). The formula for W follows.
(iii) Given W, the value g = 2t is fixed. Also x_W - 2g = 4n_V + u_V = 5i_V + 4b_tau + 4p m + const, where m is the class's m. Since 0 <= 5i_V < 4p, i_V is fixed mod 4p and hence fixed, so m, V and G are fixed. Two distinct parked SLL triples therefore never share W.
Brute-force check (sll_check.py, sll_check2.py): synthetic L** regions at h = 201 and 241 with p > 20h, cross-block pairs within reach, and i fixed mod 4 or mod 32. All SLL triples found are intra-class odd Pc (2438 and 4292 of them), with 0 W collisions. Control: with i fixed only mod 2, 304 Pb-type (E vertex) triples appear, as (i) predicts.

2. THEOREM B.
A corner triple has at most one shallow corner (block_sea Theorem 1, audited). W lies in a shallow column iff exactly one corner is shallow.
2a. One shallow corner E and corners F, G deep. By block_sea Theorem 1, the parked cases are Pa, Pb and Pc. X1 and X2 are absent because odd deep rows are r1 (mod 8) (SAW Theorem 1(1), audited).
 - Two labels: Theorem A.
 - Two fillers: SAW Theorem 1(3) (audited).
 - One label and one filler: Pa needs two even rows, which is impossible.
 - Pb needs W row y_L + y_F - r0 <= h with y_F >= T* - 16 >= h - 79, so y_L <= 82. R2 removes these labels.
 - Pc with a filler vertex has g = y_L - y_F < -104, so W is below row 1.
 - Pc with V an odd label and G a filler: 4a gamma = 2u_V g. If G is a base (gamma odd), v2(g) >= 4 by (S), so v2(a) >= 3 and E is not shallow. If G is a hole (gamma even), v2(g) = 3, which gives the stated valuations of gamma and a.
 - Pc with an even label vertex has g odd, so it is X2-shaped and absent.
2b. All three corners deep. Then W lies in a deep column (x_W = sum of columns, = 0 mod 4).
 - LLL: rigid Theorem C (audited).
 - FFF: SAW Theorem 1(3).
 - FFe. Filler vertex: E - V = (4alpha, d1) with d1 odd, and F2 - V = (4beta, 8e2) with e2 in {±1, ±2, ±3} and beta = e2 (mod 4). The right angle gives 2 alpha beta = -d1 e2, so 1 + v2(alpha) + v2(e2) = v2(e2). Impossible. E vertex: 16 alpha beta = -d1 d2 with d1 d2 odd. Impossible.
 - FFo, label vertex: W row = y_F1 + y_F2 - y_L <= h needs y_L >= 2T* - 48 - h. Non-near-band labels have y_L < T* - 128, which forces T* < h - 80. But T* >= h - 63.
 - FFo, filler vertex V at offset o_V: put e_k = (row difference)/8. The right angle gives alpha beta = -4 e1 e2 with e2 = o2 - o_V, beta = e2 (mod 4) and alpha = -o_V (mod 4). By (S), e1 = -1 - o_V or -3 - o_V (mod 8). For o_V = 1 or 3: v2(alpha beta) = v2(e2) < 2 + v2(e1) + v2(e2). For o_V = 2: alpha = 2 (mod 4) and e1 odd, so 1 + v2(e2) != 2 + v2(e2). So o_V = 0, with V a hole at a label slot. Then e2 = o2 in {1,2,3} (e2 = 0 would make a horizontal leg) and alpha = 4alpha'. W sits at offset o2, row y_L + 8o2, and is white because the filler there is at T* - 24 + 8o2 != y_L + 8o2.
 - Fee. Filler vertex: impossible by parity. Even-label vertex E1 with ends V and E2: write E2 - E1 = (4delta, 2eta), so delta = eta - Dn with Dn in 2^nu Z, and the right angle gives 8 alpha delta = -d eta with d odd. If v2(eta) < nu, then v2(delta) = v2(eta) and 3 + v2(alpha) + v2(eta) = v2(eta). So |eta| >= 2^nu >= K, but |eta| <= K - 1.
 - Feo (any vertex). This re-derives saw_residual (iii-a) for SAW*. V-vertex: t(16g + 2f) = 16g^2 + f kappa'. For holes, v2(f) = 3 gives valuations 4 against 3, so no t. For bases with v2(f) = 5, t is odd. For bases with v2(f) = 4, f' = 1 (T = 3) or f' = 3 (T = 1) (mod 4), and kappa' = f - T_P (mod 8), so g^2 + f' kappa' = 2 (mod 4) and t = 2 (mod 4). In every case Q is at offset != 0. P-vertex: 16gt = -f(y_Q - y_P). Holes give 5 against 3. Bases give v2(t) = v2(f) - 4 in {0, 1}. Q-vertex: impossible by parity. Same label (t = 0): g^2 = f'(T - 16f') = 3 (mod 4).
 - Foo with label vertex O1, ends V (filler) and O2: alpha delta = -4 e eps, with delta = 4eps + DM and eps = 0 (mod 8). Inside a class, alpha = -e. But alpha = o_V (mod 4) and e = c + o_V (mod 4) with c odd by (S), so alpha + e is odd. Across classes, reducing mod p gives alpha = -e (mod p). Also |alpha| <= 4|e||eps|/(p - h/2) < h, so alpha = -e exactly, hence delta = 4eps and DM = 0. Contradiction.
 - Foo with filler vertex V: as for FFo, the valuations force o_V = 2 and e_k odd with e1 = e2 (mod 8). With D = alpha2 - alpha1 = 4(e2 - e1) + DM, we get (2 alpha1 + D)^2 = D^2 - 16 e1 e2. Under R1, v2(D) >= 3, so 2 alpha1 + D = 4w with w odd, and w^2 + e1 e2 = (D/4)^2. The left side is 2 (mod 8) and the right side is 0 (mod 4). Contradiction. Without R1 the case DM = 4 (mod 8) (classes at s and s+4) is not excluded.

3. THEOREM C.
 - Shallow-column W: SLL/SLL is empty by Theorem A(iii).
 - SLL/SLF: the W rows are r0 + 2t with 2t = 0 (mod 32), against r0 + g with g = 8 (mod 16). They never match. This settles (c).
 - SLF/SLF: equal W row gives equal g. If the holes have different offsets, their rows differ by 16, so y_V2 - y_V1 = 16 and Di = 8, which contradicts i fixed mod 16. So the holes share a row, y_V1 = y_V2 (same i), and u and g are common. Then x_W = x_Vk + phi(gamma_k) with phi(gamma) = 4gamma + ug/(2gamma).
  - Same class: then V1 = V2, and phi(gamma1) = phi(gamma2) with gamma1 != gamma2 forces gamma1 gamma2 = ug/8. Its valuation is 0, while v2(gamma1 gamma2) is 4 (offset 0) or 2 (offset 2).
  - Different classes: this is family (d).
 - Deep-column W: only FFo remains. Two FFo triples at one W have y_L1 + 8o = y_L2 + 8o'. With label rows fixed mod 64 this gives o = o' and the same i. Then x_L1 + 4beta1 = x_L2 + 4beta2. Different classes would need |beta1 - beta2| >= p, but |beta| <= 3E1 < 3h/8. So the classes coincide, and then L, beta, alpha', V and F2 coincide too.

4. PROPOSITION D.
 - Factorization: phi1 - phi2 = 4G(e1 - e2) + R e2 - R e1 = (e1 - e2)(4G - R).
 - Offset 0: v2(G) = 2, v2(N) = 2, R odd, so 4G - R is odd.
 - Offset 2: v2(G) = 1, v2(R) = 1, so v2(4G - R) = 1.
 - Since the difference is 4DM with v2(DM) >= 2 (L**) or >= 4 (R1), we get v2(e1 - e2) >= 4 (offset 0) or >= 3 (offset 2) in L**.
 - If p divides 4G - R, then |4G - R| >= p (times 2 at offset 2). If p divides e1 - e2, then 16p or 8p divides e1 - e2. Either way |difference| >= 16p in L**, and >= 32p under R1.
 - First moment: a shape is (u, hole row, gamma1, gamma2) with gamma_k | N = ug/2. There are at most h · max tau^2 = h^(1+o(1)) shapes. Each has a nonzero difference below 2.5h^2 < (20h)^2, so at most one admissible p divides it.
 - A realized shape gives at most h/16 class pairs: c1 is any class holding a label with that i, and c2 is fixed by Dm. So it hits at most h/8 labels.
 - With #P >= c h/log h (prime number theorem in progressions mod 20), E_p[labels] <= (h/8) h^(1+o(1)) log h/(c h) = h^(1+o(1)).
 - Census: d_shapes.py and d_fast.py check the right angle by assert. They give 0 realized pairs at h = 400, 1000 and 2000, and 4 and 44 at h = 3000 and 5000. The example was checked by hand: 15732·33 = 519156 = u g/2 with u = 621, g = 1672.

5. PROPOSITION E. This is Section 2's Feo analysis. It shows that no right-angled triple {filler, odd label point, even label point} exists, whatever the row of W, for row-1 and row-3 types alike. S3-low is the V-vertex case with a base filler. Under R1, Section 2 leaves only FFo, whose W row is y_L + 8o2 >= 178, among the deep-only triples.

6. PROPOSITION F. Use Lemma mixedeq: C + D = A + B + 2n, n.(B-A) = 0, |D-C| = |B-A|, and p = A+n, q = B+n in the grid. All support points are deep, so n_x is even.
(F1) A, B fillers with B - A = (4delta, 8e), and C, D labels with |D-C| >= 78h, so |delta| >= 19h. The condition n_x delta = -2e n_y with |2e n_y| <= 6h forces n_x = 0. Then e != 0 forces n_y = 0, so n = 0, which is degenerate. For e = 0 the side is horizontal, which is S5 (Lemma 4(a), audited).
(F2) Side L1 L2 of odd points in different classes: n_x Dx + n_y Dy = 0 with Dx = 2Dy + 4DM.
 - Dy = 0: X^2 - delta^2 = 4e^2 forces |X| <= 10, which is not cross-block. Here X = Di + DM, and delta, e come from the diagonal's vector D - C = (4delta, 8e) when the diagonal is a filler pair.
 - Dy != 0: mod p, Dy(2n_x + n_y) = 0. With |n_y| < h and |n_x| < h/78, this gives 2n_x + n_y = 0, so 4 n_x DM = 0 and n = 0.
(F3) Put U = F1 - L1, Dv = L2 - L1 and V = F2 - L2 = U + 2n - 2Dv. Then |V| = |U| and n.U = 0 together are equivalent to |Dv - n|^2 = U.Dv. So L2 lies on the circle with diameter pq, and |Dx| <= |n_x| + |U|.
 - Rows give n_y = (Dy - df)/2. The corner q = F1 + n in the grid gives n_y <= h - f1 <= 87.
 - If n_y >= 1: n_x X1 = -n_y Y1 with n_x even and nonzero, so |n_x| >= 2, |X1| >= 4 and |X1| |n_x| <= 87h. Hence |X1| + |n_x| <= 43.5h + 2, and |Dx| <= |X1| + |Y1| + |n_x| < 45h. The same proof works for even labels.
 - If n_y <= -1: write Dv - n = Z and U - Z = W'. Then Z is perpendicular to W', and Z_y = df + n_y, W'_y = A' + N'. So Z_x and W'_x are the roots of z^2 - X1 z + Pi' = 0 with Pi' = (N' - df)(N' + A'). Also n_x X1 = N' Y1 and Dx = Z_x + n_x. Writing w for the small root gives k(w^2 + Pi') = w N' Y1.
 - Labels per shape: at most h/8. A shape fixes DM, so at most one prime divides it. This gives E_p = O(N_e log h).
 - For df = 0 the relation reads A' N' (w - k) = k(w^2 + N'^2). It is homogeneous of degree 1, a cone over a projective cubic surface. Its obvious rational plane (w = 2k, Y1 = n_y) violates the row constraint y_L2 < y_F1.
 - Census: e_census.py, with a direct mixedeq assert on every hit, gives 0 shapes with |Dx| >= 78h at h = 1000 and 2000. e_max.py gives a largest |Dx| of 25.4h, 28.6h and 27.9h at h = 600, 1000 and 1500.

## External results used

- Prime number theorem in arithmetic progressions mod 20 (non-explicit), for #P >= c h/log h; the notes already use it.
- tau(n) = n^(O(1/log log n)) (standard divisor bound).
- Repository (audited): block_sea_classification.md Theorem 1 and criterion (V1)-(V5); deep_layer_sawtooth.md Theorem 1(1),(3) and Lemma 4 as audited; rigid_layout_cross_block.md Theorem C; paper Lemma mixedeq. Unaudited inputs: full_layout_junctions.md (L**), saw_residual_families.md (the SAW* definition).

## Checks

All scripts are in scripts_v3_families/. Each was run with py, under 60 s per height. The repository was not touched.
- sll_check.py and sll_check2.py: synthetic L** regions with the rigid rule, 2^nu >= K and p > 20h, at h = 201 (p = 4027) and h = 241 (p = 4903). They enumerate every tilted rectangle with a row-1 shallow corner and two label corners.
  - Results: only parked intra-class odd Pc (2438 and 4292 triples) and 0 V3.
  - Controls: s fixed only mod 2 gives the same; i fixed only mod 2 gives 304 Pb-type triples.
- d_shapes.py, d_fast.py and d_stats.py: census of family (d), with an assert on the right angle.
  - Realized (pair, p): 0 at h = 400, 1000 and 2000; 4 at h = 3000; 44 at h = 5000.
  - At h = 1000 the largest prime factor of the difference is at most 7h, consistent with the 16p lower bound.
- e_census.py (with a mixedeq assert), e_loose.py, e_max.py and e_maxX1.py: family (e).
  - 0 shapes with |Dx| >= 78h at h = 1000 and 2000, with or without the 2-adic filters.
  - Largest |Dx| is about 28h at h <= 1500.

## Gaps

- Nothing here is audited. Every proof was derived once by me. The brute-force checks are small: SLL triples at h = 201 and 241; censuses for families (d) and (e) up to h = 5000 and 2000.
- Item (e) is not closed. The branch n_y <= -1 of the cubic family needs N_e(h) <= h^(2-delta), which I could not prove. Every slicing by two variables gives h^(2+o(1)), which is the dimension-growth barrier for a 3-fold. For df = 0 the problem is integer points on a cone over an explicit projective cubic surface, and a bound off lines would suffice, but I did not verify the lines or cite a theorem. The even-even version of this branch and the even-even quadruples with a side of two labels were not treated.
- R1 changes L**: the region type has s fixed mod 16 instead of the pair {c, c+4}. The constant doubles. R1 is used only to kill filler-vertex Foo, which survives without it when DM = 4 (mod 8). I did not recheck the other proofs of L** under R1, although it only refines the classes.
- R2 (relocate 2i+1 <= 177) adds O(h) labels to the relocation set. Without it, Pb triples with one label and one filler exist for labels with odd row <= 82.
- Family (d) is bounded only in expectation over the admissible primes p. This needs the same Markov and union-bound choice of p as the other first-moment families. Whether the realized pairs at h = 3000 and 5000 lie inside one region window was not checked against a real class assignment.
- The inputs used are the SAW* definition (unaudited; I re-derived the row congruences I use), SAW Theorem 1(1),(3) and Lemma 4 (audited), block_sea Theorem 1 (audited) and rigid Theorem C (audited). Theorem B's list of deep triples is my own case analysis, and no brute-force check of SAW* with fillers was run.
- Item (f): only corner triples were treated. Deep-only mixed quadruples whose corner p or q lies in row 1 or 2 in the row-3 types were not analysed.

## Missing estimate

One count closes (e): N_e(h) = #{(y_L1, Dy, f1, f2, k, w) : k(w^2 + (N'-df)(N'+A')) = w N'(A'+df), k even >= 2, |Dx| >= 78h} <= h^(2-delta). Here N' = (df - Dy)/2 >= 1, A' = f2 - y_L1 and df = f1 - f2 in {0, ±8, ±16, ±24}. Fixing (k, w) leaves N' among the divisors of one fixed number, and fixing (y_L1, Dy) leaves k among the divisors of N'Y1. Each gives only h^(2+o(1)). The heuristic is h^(1+o(1)). For df = 0 the relation is homogeneous, A'N'(w-k) = k(w^2+N'^2), so a bound for points off lines on that projective cubic surface would suffice. The analogue is needed for even labels.

## Next steps

- Audit Theorem A first. It is short (mod 4, mod p and 2-adic), and it settles O2(d) outright. Then audit Theorem B's list of deep triples and the Feo/Foo/Fee valuations, which settle (b), (c) and (f).
- Decide on R1 (s fixed mod 16 per region type). It is needed only for filler-vertex Foo; the alternative is to bound Foo with DM = 4 (mod 8) directly.
- Add family (d) to the first-moment list, beside I.2 and II (E_p <= h^(1+o(1)) labels), and add R2 to (P5).
- Attack N_e for df = 0 as a cubic-surface count: classify its rational lines and planes against the row and sign constraints, then cite a bound for points off lines. Then handle df != 0 and the even-even branch.
- Run a SAW* brute force with fillers at h of about 400 to 650 to confirm Theorem B's list. Labels survive the exclusions only from h of about 400 on.

