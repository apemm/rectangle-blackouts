# Census of the sea families in the rigid layout

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: without fillers, the only sea family with order-1 load per label is odd-odd M2c inside a class. It is a fixed ratio graph R_IV on slots, the same on every diagonal. Four families are proved empty only below explicit thresholds. Conditions (1) to (4) on the deep layer leave five filler families uncovered. Not audited yet.

# Result

## Status

partial

## Summary

Without fillers, the Corollary B layout has exactly one sea family with order-1 load per label: odd-odd M2c inside a class (family IV). It is a fixed ratio graph R_IV on slots, the same on every diagonal, that the colouring of G_T does not see. Every other family without fillers is proved empty, either outright or for h up to 2550 to 81632; four of these still lack a proved count beyond that range. Conditions (1) to (4) leave five filler families uncovered.

## Statements

SETTING L(k). This is the layout of sea_row3_split.md, Corollary B:
- stride 4 and the rigid rule n(c) = s_c - M_c = kappa (mod 2^nu), with M_c in pZ and p prime in (20h, 40h];
- region types by (i mod 2^k, s mod 2), with k >= 3. Classes are G_T-independent sets split by i mod 2^k;
- a row-1 sea when the shifted slot is odd and a row-3 sea otherwise;
- the exceptional labels relocated: i = 0, i = 2, and j in {0, 1} in the row-3 types;
- in each block zone, any deep layer that satisfies (1) to (4).
Optional refinements, each costing a constant factor in width:
- (Hnu): 2^nu >= K;
- (Hs): within a region, every s mod 16 lies in a half-window {c, c+2, c+4, c+6};
- (Hp): p = 3 (mod 4).
L* denotes L(4) with (Hnu), (Hs) and (Hp).
In row-3 types, write u = (y - r0)/2 for odd label points. By the shift invariance of sea_row3_split 2(i), everything below is stated for a row-r0 sea.

A (RECONCILIATION). The notes describe the same objects under different names. The dictionary is in the proof, section 1. In short:
- t1's R3 = M2a (two shallow witnesses), or deep M2a / S2 / S5 when the witnesses are fillers.
- t1's R1 = a diagonal pair of two sea points. With shallow points it never occurs. With fillers it is a generic deep quadruple.
- t1's R2 = M2c (BH16's S4 'FS/So' when one sea point is a filler, 'Fo/Fo' when both are).
- t1's Lemma 1 one-sea supports = M1C (sea point on the diagonal). The sea point on the side never occurs.
- 'Three labels and a sea point' = M1C again, or a deep one-filler quadruple, or a V3 collision.
- t1's two-label sea triangles = X1, X2, Pa, Pb, Pc. t1's cross-EH and intra-class EH are Pa and Pc shapes.
- mixed_quadruples S1 = M1C, S2b = M2c, and S2a = M2a or the impossible diagonal pair.

B1 (TYPE II; proved). In L(3), a type-II mixed quadruple of label points has roles (1,-1) and Sigma != 0.
- (-1,-1) with Sigma != 0 is empty. New: d, d' = 0 (mod 8) and S odd give v2(Dj) >= nu + 5.
- (-1,-1) with Sigma = 0 is empty under (Hnu) (new), or under p = ±2 (mod 5).
- (1,1) is empty under (Hp); (1,-1) with Sigma = 0 is empty.
- For (1,-1): Sigma = 0 (mod 2^k), v2(Ds) = v2(Sigma) >= k, Dpos = 0 (mod 2^k) and |Sigma||Dpos| <= h/156.
- So type II is empty for h <= 9900 (k = 3) and for h <= 39900 (k = 4).

B2 (TYPE I.2; proved). In L(k): a, b, m and Ds are all = 0 (mod 2^k), and Dpos = 0 (mod 2^k). Also v2(n2) = 3 + v2(a) + v2(Ds) and |a|(320|Dpos| - 18) < h. So I.2 is empty for h <= 20336 (k = 3) and for h <= 81632 (k = 4). I.2 quadruples come in translation families indexed by (c0, c', a, b); each family holds up to about h/2 quadruples.

B3 (2-ADIC LAW FOR M2c; proved). Take M2c with A and C shallow in row r0, B and D label points of one region (any classes, any blocks), e = (y_D - y_B)/2, a = v2(e) and b = v2(n1). Assume (Hnu).
(i) Even-even: (a, b) = (3, 2).
(ii) Odd-odd (k >= 3): either b = a + 1 and v2(e + DM) = a, or b = a and v2(e + DM) = a - 1.
Corollaries:
(C1) In L(4) with (Hs) and (Hnu), there is no even-even M2c at all, inside or across classes.
(C2) An odd-odd M2c inside a class is exactly an edge of R_IV^(k) (B4). This is family (IV) of cross_class_sea A2.
(C3) In L* an odd-odd M2c across classes needs Ds = 0 (mod 16) and |Dpos| >= 16, so it is empty for h <= 2550.

B4 (ORDER-1 FAMILY; proved, except for the colouring). R_IV^(k) is the set of pairs (q m, p m), m odd, of odd u-values, where
- lambda = (al, be) runs over odd coprime pairs with 0 < al < be and v2(be - al) >= k - 2;
- F = 4(al - 2be)^2 + be^2 and g = gcd(F, be - al), which is 1 or 5;
- q = al F/g and p = (al F + 4(be - al) be^2)/g.
Two odd label points of one class form a fatal M2c iff their u-values form an edge with u_D <= (h - r0)/2. R_IV does not depend on T, on the block or on the region. The first edges are (109, 181), so h >= 363, and (349, 749), so h >= 1499 for k = 4. There are c_k X + o(X) edges below X, with c_3 ~ 0.0075 and c_4 ~ 0.0020 (numerical). So the M2c load inside classes is Theta(1) per label, about 0.015/chi' (k = 3) and 0.004/chi' (k = 4), where chi' is the class count of G_T. The total is Theta(h^2), which the relocation rule cannot absorb. Splitting each class by a proper colouring psi of R_IV removes this family at cost chi(R_IV). Numerically R_IV is bipartite with degeneracy 2 up to X = 2*10^6. That chi(R_IV) is finite is NOT proved.

B5 (CONDITIONS (1) TO (4) ARE INCOMPLETE; proved by exhibited instances). These families with a filler are untouched by (1) to (4):
- M2c with a filler, for example A, C shallow, B an odd label, D a hole. Its deep pair is not Pythagorean, so (2) says nothing about it.
- Tilted-side deep quadruples, for example side Ho / diagonal Ho.
- Rival pairs with a filler.
- Fatal deep triples with a filler (S1, S3).
- Fully black tilted rectangles with a filler.
- V3 between a filler triple and an SLL triple.
A complete list must add (5) no fatal triple and no fully black rectangle with a filler corner, (6) no mixed quadruple with a filler outside (2), and (7) no rival pair with a filler, and must widen (3) to every parked triple. Condition (1), with the label residue, does kill X1, X2 and M1C with fillers (Theorem A).

B6 (COMPLETE LIST WITHOUT FILLERS, in L* with the psi split).
EMPTY:
- V1 (all shapes);
- V2: X1, X2, and any LLL triple;
- V4: M2a with a label diagonal, M1C, the shallow diagonal pair, a single shallow side point, I.1, II except (1,-1), and all even-even M2c;
- V5: all rival pairs;
- M2c inside a class (after the psi split).
EMPTY ONLY UP TO A THRESHOLD, NO PROVED COUNT BEYOND IT: I.2 (h <= 81632), II(1,-1) (h <= 39900), odd-odd M2c across classes (h <= 2550).
OPEN: V3 between two parked SLL triples (Pa, Pb, Pc). There is no threshold. The census found 0 among 6.2*10^5 parked triples.
Boundary labels and junctions: no new family beyond the cited locality and Lemma block arguments and condition (4).
ORDER 1 PER LABEL: only R_IV (without the psi split), plus whatever deep-layer families conditions (5) to (7) leave.

## Proofs

0. CONVENTIONS. I use the audited results block_sea_classification Theorems 1 and 2 (the M2c equations, including the converse), the criterion (V1)-(V5), the rigid Theorem C, mixed_quadruples Theorems 1 to 4 and A1/A3 of deep_layer. I also use sea_row3_split Theorem A and Corollary B, which are unaudited and taken as given. The facts used throughout:
- (R) Slots of one class are = iota (mod 2^k). Every class within reach lies in the same region type, so s0 = s' (mod 2) and every slot difference is = 0 (mod 2^k).
- Rigid: Dn = Ds - DM = 0 (mod 2^nu), with 2^nu >= K/8, or >= K under (Hnu).
- Odd label rows: u = (y - r0)/2 is odd in every type.

1. RECONCILIATION (part a). Sea point = shallow point S (row r0, column != 0 mod 4) or filler F/H (deep column).
- Side SS, diagonal ll: block_sea M2a = t1 R3 = mixed_quadruples S2a(side). With FF witnesses it is deep_layer A2: S2 (label + hole), S5 (cross-block label + label), BH16 'FF/Fo'.
- Side ll, diagonal SS: never occurs (block_sea 2(i)) = t1 R1 = S2a(diagonal). With FF it is a generic deep quadruple.
- Side lS, diagonal lS: block_sea M2c = t1 R2 = mixed_quadruples S2b. With a filler it is BH16 S4 'FS/So'; census name 'side So / diag HS'. With two fillers it is 'Fo/Fo'; census 'Ho/Ho'.
- One sea point on the diagonal: M1C = t1 Lemma 1 roles (a,c|b,s), (a,c|d,s), (c,s|...) = mixed_quadruples S1. One sea point on the side, the roles (a,s|..): impossible by block_sea 2(iii). 'Three labels and a sea point' as a 4-point support is the same M1C with three distinct labels.
- Corner triples SLL: X1, X2 (fatal), Pa, Pb, Pc (parked) = t1 'two-label sea triangles'. t1's B2 'cross-EH' and B3 'intra-class EH' are Pa and Pc shapes, with H the even sea row.
- V3 among parked SLL triples = t1 (v), 'V3 collisions among parked cross-EH'.
- Deep triples with fillers: S1 = 'FFo', S3 = 'Feo', census 'V2 (V=F; e,o)'.
- Rival pairs with a filler: BH16 K3, 'Fe'.
- t1 (iii) = I.2/II. t1 (vi) = M2c families (II) and (IV), plus S1 and S2b inside a class.
- t1's Theorem B and Proposition D concern AR regions (the T1 profile sea L, F, H at stride 2 sigma). They do not transfer to the stride-4 shallow sea; there the kills are Theorem A and Corollary B and the results below.
Correction found: mixed_quadruples Theorem 5 S2a, the cross-block case, uses V2^2 < 2|V1| + 1. That fails for h >= 154, because V2^2 <= (h-1)^2 while 2|V1| only exceeds 152h. The conclusion survives in Corollary B through A1, A3 and the mod-16 odd rows.

2. B1, TYPE II. Re-derived from L0 of cross_class_sea. In (-1,-1), A and B are even, C and D are odd, and d = iC - iA, d' = iD - iB. Then U = (4(Dj - Dn), 2Dj) and 2n = (4 Sigma, 2 Sigma - T0 - T'). The equation U.2n = 0 gives Dj(5 Sigma - S) = 4 Sigma Dn, with S = s0 + s' + 1.
- By (R), Sigma = 0 (mod 8) and S is odd, so 5 Sigma - S is odd.
- If Dj != 0, then v2(Dj) = 2 + v2(Sigma) + v2(Dn) >= nu + 5 > log2(K) > log2|Dj|. This is a contradiction.
- If Dj = 0, then Sigma Dn = 0. Here |Dn| >= p - h > 0, which forces Sigma = 0.
- When Sigma = 0, Dj = 0 and U is horizontal. E1 becomes (delta - Ds)^2 + 4 delta^2 = 8 Dn delta, with delta = d' - d = -2d, w = v2(delta) >= 4, and |delta| <= h/19 (from 152 h|delta| <= 5 delta^2 + 2h|delta| + h^2).
- Under (Hnu), nu >= w + 2. The right side then has v2 = 2 + 2w, so v2(delta - Ds) = 1 + w. Dividing by 4^(1+w) gives 1 = -1 (mod 8). This is a contradiction. Alternatively, mixed_quadruples 4(c) with p = ±2 (mod 5) kills it.
- (1,1) is impossible by 4(a) and 4(b) (needs p = 3 mod 4). (1,-1) with Sigma = 0 is impossible by 4(d).
- For (1,-1): (2Dj + T0)(Sigma - Ds) = -8 Sigma (Dj - Dn) (C2, re-derived). So v2(Sigma - Ds) >= 3 + v2(Sigma), which forces v2(Ds) = v2(Sigma) >= k. Rigid: p Dpos = DM = Ds (mod 2^nu), so Dpos = 0 (mod 2^min(k,nu)) and Dpos != 0.
- E2 gives 16|Sigma|(p|Dpos| - A) <= 2(h-1)^2. Hence |Sigma||Dpos| <= h/160 + |Sigma|/40 <= h/156, using |Sigma| < h/152.
- With |Sigma|, |Dpos| >= 2^k this gives 4^k <= h/156. []

3. B2, I.2. A and B are in one class, so a = 0 (mod 2^k). The same holds for b, and m = 2(iC - i0) + b - a = 0 (mod 2^k).
- E2 can be written (18a + T0)Ds = 16 a N - m(10a + T0), with N = Dn = 0 (mod 2^nu). So v2(Ds) >= min(k, v2 m) >= k.
- Rigid: Dpos = 0 (mod 2^k), for nu >= k; for small h and nu < k use mod 2^nu.
- n2 = 8a(2N - Ds)/(10a + T0), so v2(n2) = 3 + v2(a) + v2(Ds).
- |Ds - 2DM| >= 40h|Dpos| - h, |n2| <= h - 1 and |10a + T0| < 10|a| + h give |a|(320|Dpos| - 18) < h. Then |a|, |Dpos| >= 2^k gives the thresholds.
- E1 and E2 do not contain i0, so every admissible (c0, c', a, b) is a translation family.
Why no count bound: a family needs (i) T' in the E1 set of (T0, a), of size at most r_2(N_a); (ii) e = (10a + T0)/gcd(a, T0) dividing Ds - 2p Dpos; and (iii) p^{-1}Ds mod 2^nu smaller than h/(300|a|). Averaging over the prime p controls only one congruence, and the other two are fixed CRT residues of (T0, a, T'). The best bound I can prove is E_p[#families per class] << log^2 h. That gives B h^{2+o(1)} quadruples: no improvement.

4. B3, M2c. block_sea M2c: n1 z = -e u2, and tau^2 + tau z + e(u2 + e) = 0 with tau = Delta - n1 (audited). Put sigma = -(tau + z) and w = sigma - n1. Then
 (I1) e u2 = n1(Delta + w), and (I2) (Delta - 2n1) w = e^2 + n1^2,
and z = -(Delta + w). So v2(z) = v2(Delta + w), and shallowness (z != 0 mod 4) gives v2(z) in {0, 1}. Label columns give Delta = 0 (mod 4).
(i) Even-even. u2 = y_B - r0 is odd, so a = b + v2(z).
- By (R), e = (iD - iB) + Ds is even.
- Delta = 4(e - Dn), with v2(Dn) >= nu > a under (Hnu). So v2(Delta) = a + 2.
- If b = a: w is odd and v2(e^2 + n1^2) = 2a + 1. But v2(Delta - 2n1) = min(a + 2, a + 1) = a + 1. Since a >= 1 this is a contradiction.
- If b = a - 1: v2(w) = 1 and v2(e^2 + n1^2) = 2b. Here v2(Delta - 2n1) = min(b + 3, b + 1) = b + 1, so I2 forces b + 2 = 2b, that is b = 2 and a = 3.
(ii) Odd-odd. u2 = 2u with u odd, so a + 1 = b + v2(z) and b is a + 1 or a. Also Delta = 4(e + DM), and a >= 3 by (R).
- If b = a + 1: w is odd, v2(rhs) = 2a and v2(2n1) = a + 2 < 2a. Hence v2(Delta) = a + 2, that is v2(e + DM) = a.
- If b = a: v2(w) = 1, v2(rhs) = 2a + 1 and v2(2n1) = a + 1 < 2a. Hence v2(e + DM) = a - 1.
Neither step uses the sign of e, so the low shapes of the row-3 types (e in {-1, -2}) are covered as well.
(C1) e = Ds (mod 16), and (Hs) gives v2(Ds) in {1, 2} or Ds = 0 (mod 16). So v2(e) != 3.
(C2) DM = 0 inside a class. Only b = a + 1 remains, that is lambda = n1/t with v2(lambda) = 1: family (IV).
(C3) v2(e + DM) in {a, a - 1} with a >= 4 needs v2(DM) = a - 1 >= 3, or v2(DM) > a. Under (Hs) this means Ds = 0 (mod 16), so Dpos = 0 (mod 16). An M2c spans at most 2((h-1)^2/4 + h) columns, while 4(16p - h/2) >= 1278 h. So h >= 2550 is needed.

5. B4, R_IV. In (IV), alpha = 2 al and beta = be, with al and be odd. al divides u by A2 (z = -u be/al is an integer), and z is odd.
- t = 4(u/al)(be - al) be^2/F, with gcd(F, be) = 1 and gcd(F, be - al) dividing 5 (since F = 5 be^2 mod be - al). Hence u = q m and u_D = u + t = p m.
- v2(t) = 2 + v2(be - al), so the mod 2^k split keeps exactly v2(be - al) >= k - 2.
- 2n1 - z = -z (mod 4), so C is shallow.
- The converse is block_sea's audited M2c converse.
- A definition check (riv.py) confirms the 5 smallest edges, including (109, 181) and (349, 749), and the full census at h = 401 found exactly this pair.
- Edge counts give the density. Each edge has both ends in one residue class, so per slot there are about 2 c_k 2^(k-2) edges; each is fatal when both ends share a G_T colour.

6. B5. Instances from the census at h = 65 (iota = 0):
- M2c with a hole: A = (-26,3) and C = (54,3) shallow, B = o(64,33), D = H(-24,57). Here D - B = (-88, 24), and 4·22^2 + 12^2 = 2080 is not a square, so (2) does not apply. The board satisfies (1).
- Rival pairs: F(1632,51) with e(1644,16), different parities.
- S3: o(9392,7), e(9424,50), F(9412,55), with W = (9404,2).
- Ho/Ho at h = 81.
None of them is a horizontal-witness quadruple or a parked triple, so (2) and (3) do not apply.

7. B6. The 'empty' items come from Theorem C, block_sea Theorems 1 and 2, Theorem A / Corollary B, mixed_quadruples Theorems 1 to 4, and B1 to B3. Junctions: every tilted obstruction or V3 pair spans at most 2W_h columns, so buffers of 2W_h + 1 separate the regions. Axis rectangles are handled globally by the parity-edge rule. The region-gap and buffer junctions are condition (4). The relocated labels use Prop. partial and Lemma block, as cited in sea_row3_split. No new family arises.

8. CENSUS (part c). My own engine, validated on 12 random full boards (h = 5 to 7) against a naive hash of all rectangles: every invalid presentation matched (0 missed, 0 extra). The boards are BH16 deep layer with all 16 region types. Block spacing is reduced to p = 67 (h = 65, 466 labels) and p = 83 (h = 81, nu = 3, 898 labels), stated as a stress test. Every violation contains a filler.
- At h = 81: S2 'Ho+axis' 1636; Ho/Ho 300; rival Fe 368 and He 268; M2c with a hole 156; S3 46. There were no cross-block configurations.
- At h = 65: 830, 346, 232, 114 and 34 (same families).
Labels and shallow points only, true p (large.py, M2c by exact enumeration, each hit re-checked from the definition):
- h = 401, all 16 types, 39602 labels, k = 3: 596 M2c, all inside classes. Even-even hits all have (a, b) = (3, 2); odd-odd hits all have b = a + 1, slots (109, 181). There are 0 M2c across classes, 0 fatal SLL and 0 V3 among 193289 parked SLL triples.
- With k = 4: 0 M2c, 0 V3 among 89097.
- h = 601, 8 types, 44701 labels: 667 M2c, all inside classes; 0 fatal SLL; 0 V3 among 333621.
- Stress spacing p = 211 and 307: 0 M2c across classes, and the law of B3 holds in every hit.

## External results used

- None outside the repository. Internal inputs: block_sea_classification Theorems 1-2 and criterion (audited); rigid_layout Theorem C (audited); mixed_quadruples Theorems 1-4 (audited, with 4(b),(c) conditional on p); deep_layer A1, A2, A3 and BH16; cross_class_sea L0, A2, C2, C3, B4 (unaudited; the parts used were re-derived); sea_row3_split Theorem A and Corollary B (unaudited); t1_cost_decomposition names and Lemma 1.

## Checks

Scripts are in the script folders of this directory. All ran with py, each under 60 s, and the repository was not touched.
- census.py: the definition-level engine (numba). It enumerates every tilted rectangle with at least 2 black corners from black pairs, hashes presentations, and matches axis rectangles through the parity-edge rule.
- validate.py, validate2.py: 12 random full boards (h = 5 to 7) against a naive hash of all rectangles. All invalid presentations matched.
- board.py, driver.py, examples.py: the BH16 Corollary B boards, family classification and examples (h = 49, 65, 81; p = 67, 83, 163, 277).
- large.py, m2c_v2.py: exact M2c and SLL enumeration on true-p rigid layouts (h = 401 and 601; stress p = 211, 307), every hit re-checked from the definition.
- riv.py, riv_char.py: R_IV edges, the definition check of the smallest edges, density, degeneracy and bipartiteness up to 2*10^6. No small Legendre or Liouville character 2-colours R_IV.

## Gaps

- Nothing here is audited. B1 to B3 are elementary, and I re-derived each 2-adic step once. B3 rests on the audited M2c equations, B1 on the audited mixed_quadruples Theorems 1 to 4, and both on the unaudited sea_row3_split Corollary B and Theorem A, and its shift invariance for the row-3 types.
- chi(R_IV) is finite is NOT proved. Bipartiteness and degeneracy 2 hold numerically for X <= 2*10^6. Without it, family (IV) is a Theta(h^2) family that the relocation rule cannot absorb.
- No O(h^(2-delta)) count is proved for I.2, II(1,-1), odd-odd M2c across classes, or V3 between parked SLL triples. The first three are proved empty only below h = 81632, 39900 and 2550 (in L*). V3 has no threshold and only numerical evidence: 0 collisions among 6.2*10^5 parked triples at h = 401 and 601.
- The refinements (Hnu), (Hs), (Hp) and the psi split are my additions, at constant width cost. Compatibility with BH16 is clear because they only refine regions. Compatibility with an arbitrary deep layer satisfying (1) to (4) is assumed.
- Conditions (5) to (7) of B5 are necessary additions. I give no deep layer satisfying them. The census uses BH16, which fails (2) through S2, so it cannot show which filler families survive a layer that does satisfy (1) to (4). B5 shows only that (1) to (4) do not mention them.
- The census boards are small (h <= 81, under 900 labels, reduced spacing). There, cross-block label configurations never occurred. The junction buffers and relocated-label regions were not simulated, and axis rectangles were matched by the parity-edge rule, which assumes the rest of the board.
- The density constants c_3 and c_4 and the per-label loads are numerical. The Theta(1) claim needs only c_k > 0, which the explicit edges with positive density give (m odd up to X/p).

## Missing estimate

Two estimates are missing.
(i) chi(R_IV) < infinity. R_IV is the T-independent ratio graph u ~ (p_lambda/q_lambda) u of B4. A 2-colouring would turn family (IV) into a factor-2 class split.
(ii) A count O(h^(2-delta)) for I.2, II(1,-1), odd-odd M2c across classes and V3 between parked SLL triples. Each family needs two independent arithmetic coincidences of size about 1/h: a divisibility e | (Ds - 2p Dpos) or an E1 representation, and the residue p^{-1}Ds mod 2^nu falling in a short window. Averaging over p gives only one factor 1/h, so a second source of randomness or an equidistribution input for these CRT residues is needed. For the deep layer, one needs a filler rule satisfying (1), (2), (3') and (4) to (7).

## Next steps

- Audit B1 (the II(-1,-1) kill) and B3 (the 2-adic M2c law). Both are short. Then add ledger rows: 'Corollary B layout: type II reduces to (1,-1)', 'even-even M2c dies under i mod 16, (Hs) and (Hnu)', and 'odd-odd M2c inside a class = R_IV'.
- Attack the bipartiteness of R_IV. Look for odd cycles through multiplicative relations prod rho_lambda^(±1) = 1, or for a valuation or character argument restricted to edges with q m <= X.
- Revise the deep-layer specification to (1), (2), (3'), (4) to (7). Then search for patterns y(n mod 2^t) scored by census.py on BH16-style boards at h of about 65 to 81, counting M2c with a filler, tilted-side quadruples, rival pairs with a filler, and S3.
- For V3 between parked SLL triples, try a structural proof using the fact that W and the label corner adjacent to it determine each triple. Run the exact census at h = 801 to 1201 on all types.
- Look for a second randomization of the rigid layout that leaves Theorem C intact (for example the class order inside residues together with a family of primes p) and gives the missing 1/h for I.2, II(1,-1) and odd-odd M2c across classes.

