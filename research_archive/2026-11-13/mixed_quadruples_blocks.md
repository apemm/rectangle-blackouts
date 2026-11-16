# Mixed quadruples in the block scaffold

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Not audited yet.

# Result

## Status

partial

## Summary

Label-only mixed quadruples in the stride-s one-prime scaffold: proved that none lie in one block or span three or four blocks, and that exactly two two-block types survive, with exact equations and heuristic loads of O(polylog h / h) per label. The row-1 sea brings back mixed quadruples with one or two sea points, even inside a single block.

## Statements

SETTING (used throughout). h >= 4, A = ceil(h/2), K = floor(h/2). Stride s = 2*sigma is even. P is a multiple of a prime p > max(20h, (s^2/2+4)h). Class c is a subset of one diagonal with offset T_c (odd, |T_c| < h). The label at slot i of class c has its odd point at (s(i+Pc), 2i+1) and its even point at (s(i+Pc), 2i+1+T_c). Put w = (s,2), W = s^2+4 = 4(sigma^2+1), and Q_T(d) = s^2 d^2 + (2d+T)^2. A mixed quadruple is the paper's obstruction (2): a pair {A,B} (the side) and a pair {C,D} (the diagonal), with B-A not vertical, |D-C| = |B-A|, C+D-A-B = 2n where n is a nonzero integer vector with n.(B-A) = 0, D-C != +-(B-A), and p = A+n, q = B+n in rows 1..h. Write U = B-A and V = D-C. A, B, C, D are label points unless stated otherwise.

THEOREM 1 (block patterns) [proved]. Every mixed quadruple of label points has one of three patterns: (I.1) all four points in one block; (I.2) A and B in one block, C and D in another block; (II) A and C in one block, B and D in another block (up to renaming C and D). In particular no mixed quadruple of label points meets three or four blocks.

THEOREM 2 (one block) [proved]. For any even s and any subset of one constant-offset diagonal placed at stride s, there is no mixed quadruple of type (I.1). P-freeness is not needed.

THEOREM 3 (type I.2) [proved]. In type I.2, each pair has exactly one odd point and one even point. Rename so that A and C are odd. Then A is the odd point of slot i0 in class c0 (offset T0), B is the even point of slot i0+a in class c0, C is the odd point of slot iC in class c' = c0 + Dc (offset T'), and D is the even point of slot iC+b in class c', with Dc != 0, a != 0 and 0 < |a| < 2h/(39 s^2). The type holds exactly when
 (E1) Q_{T0}(a) = Q_{T'}(b), with (b,T') not in {(a,T0), (-a,-T0)};
 (E2) m((s^2+4)a + 2T0) = -2 s^2 a P Dc - (2a+T0)(T'-T0), where m = iC + iD - i0 - iB;
 and the strip condition holds: rows 2i0+1+n2 and 2i0+2a+1+T0+n2 lie in [1,h], where n2 = m + (T'-T0)/2.
 With T = 2s_c + 1 and Ds = s_{c'} - s_{c0}, (E2) reads m = -Ds + s^2 a (Ds - 2P Dc)/((s^2+4)a + 2T0), and n2 = s^2 a (Ds - 2PDc)/((s^2+4)a+2T0).
 For s = 4: m(10a+T0) = -16aPDc - (2a+T0)Ds, that is m = -Ds + 8a(Ds - 2PDc)/(10a+T0). This is the analogue of the earlier right-angle equation, with N replaced by Ds - 2PDc.
 b = 0 (C and D the two points of one label) is impossible when class c0 is P-free (independent in G_{T0}^(sigma)), because it forces a in S_{T0}. So every surviving I.2 quadruple uses four distinct labels.
 Given (A's label, a, c'), there are at most 2 values of b and at most 1 value of m. The quadruple is fatal outright, whatever the colours of p and q: it needs only the three slots i0+a (in c0), iC and iC+b (in c') to be occupied and the strip condition to hold.
 The reflection subfamily b = -a, T' = T0 + 4a (R2 axis-aligned) is exactly the template of ledger T21, carried over to this scaffold.

THEOREM 4 (type II) [proved]. In type II, each block contributes one odd point and one even point. Write g = C - A = (s d, eta) and g' = D - B = (s d', eta'), with eta = 2d + tau T0 and eta' = 2d' + tau' T'. Here tau = +1 if A is odd and -1 if A is even, and tau' is defined the same way for B. Write U = (s(P Dc + k), U2), where k = iB - iA, U2 = 2k + base and base = e_B T' - e_A T0 (e = 0 for an odd point, 1 for an even point). Put Sigma = d + d', G = |g'-g|^2 and Theta = tau T0 d' - tau' T' d. Then Theta != 0, and the type holds exactly when
 (E*) 4 U2 Theta = Sigma G, and
 (E2) s^2 Sigma (P Dc + k) + U2 (eta + eta') = 0,
 together with the strip condition. If Sigma != 0, these combine into G M = 4 s^2 Theta (base - 2 P Dc), with M = (s^2+4)Sigma + 2(tau T0 + tau' T'), and |Sigma| < 2h/(19 s^2). If Sigma = 0, then U2 = 0 (the side is horizontal) and G = -2 s^2 (d'-d)(P Dc + k).
 Up to symmetry there are three role types. (OO-side, EE-diagonal) = (tau,tau') = (1,1). (EE-side, OO-diagonal) = (-1,-1). (OE-side, EO-diagonal) = (1,-1), which is the same as (-1,1).
 (a) (1,1) with Sigma != 0 is impossible for every P that is a multiple of p.
 (b) (1,1) with Sigma = 0 forces k = 0 and X^2 + (s(d'-d))^2 = -2 s^2 (d'-d) P Dc, where X = 2(d'-d) + T' - T0. It is impossible if p = 3 mod 4.
 (c) (-1,-1) with Sigma = 0 is impossible if sigma^2 + 1 is a quadratic nonresidue mod p. For s = 4 that means p = +-2 mod 5. For s = 2 it means p = +-3 mod 8.
 (d) (1,-1) has no Sigma = 0 case, because U2 is odd.
 Survivors: (1,-1) and (-1,-1) with Sigma != 0. They obey the equations above, and both legs g and g' are short and steep, with |d|, |d'| = O(h/s^2).

THEOREM 5 (sea points: row-1 sea in every column not divisible by s) [proved].
 (S2a) A mixed quadruple whose two sea points form the side pair, or form the diagonal pair, does not exist, for every even s.
 (S1) A mixed quadruple with exactly one sea point (x0,1) and three label points needs x0 even. Hence it does not exist for s = 2. If 4 | s and x0 = 2 mod 4, the sea point cannot lie on the side. On the diagonal (C = sea point), D must be an odd point with V2 = y_D - 1 = 0 mod 4, and A, B must have the same parity with U2 = 2 mod 4.
 (S2b) With A = (x0,1) and C = (x0',1) sea points and B, D label points, put u = xB - x0, w = xD - x0', Dx = xD - xB and Dy = yD - yB. The type holds exactly when (u-w)(u+w) = Dy (yB + yD - 2) and u(2Dx + u - w) = -(yB - 1) Dy, together with the strip condition. B and D have the same parity, and Dy != 0. For given (B, yD, d = u - w), at most one column of D works.

COMPUTED (sanity checks, not proofs). Type I.2 and type II quadruples exist, each checked from the definition. Type S1 (s = 4, 8) and type S2b (s = 2, 4) exist inside a single block, at about 0.1 and about 0.5 incidences per label respectively.

NOT PROVED: any bound on m_h, any statement about the loads beyond heuristics, S1 for sea columns with v2(x0) >= v2(s) (strides 8, 12, 20), and S2b across blocks.

## Proofs

NOTATION. The facts used repeatedly: in-block |dx| <= s(A-1) < sh/2. For points in different blocks |dx| >= s(P-(A-1)) > 19sh, because A - 1 < h and P > 20h. Every row difference is at most h-1. |n2| <= h-1, because row(A) and row(A)+n2 both lie in [1,h].

PROOF OF THEOREM 1.
(i) Suppose A and B are in one block. Then |V1|^2 = U1^2 + U2^2 - V2^2 <= s^2(A-1)^2 + (h-1)^2 < (19sh)^2. So C and D are in one block. The symmetric argument shows that if C and D are in one block, so are A and B. Hence either both pairs are in-block or both cross blocks.
(ii) Suppose both pairs cross blocks. From n.U = 0 we get |2n1| = 2|n2||U2|/|U1| <= 2(h-1)^2/(19sh) < h/(9s). But 2n1 = sP(cC + cD - cA - cB) + s(iC + iD - iA - iB). If L = cC + cD - cA - cB is nonzero, then |2n1| > sP - 2s(A-1) > 19sh, a contradiction. So L = 0. Next, ||U1| - |V1|| = |V2^2 - U2^2|/(|U1|+|V1|) < h/(19s). Since |U1| = sP|cB - cA| + O(s(A-1)), and the same holds for V, we get |cB - cA| = |cD - cC|. Otherwise ||U1| - |V1|| > 19sh. Equal sums and equal absolute differences give {cC, cD} = {cA, cB}, so exactly two blocks are involved and the pattern is II. []

PROOF OF THEOREM 2. All points lie on base + i w + epsilon (0,T). Write U = a w + alpha e, 2n = m w + mu e and V = b w + beta e, where e = (0,T), w.w = W = 0 mod 4, w.e = 2T and e.e = T^2. Here alpha, beta are in {-1,0,1} and mu is in {-2,...,2}. Then
 (E2) U.2n = amW + 2T(a mu + alpha m) + alpha mu T^2 = 0,
 (E1) a^2 W + 4a alpha T + alpha^2 T^2 = b^2 W + 4b beta T + beta^2 T^2.
Case alpha and mu both odd: the left side of (E2) is odd, a contradiction.
Case alpha = 0: then a != 0, and (E2) gives a(mW + 2T mu) = 0. So 2(sigma^2+1) m = -T mu, and mu is even. If mu = 0, then m = 0 and n = 0. If mu = +-2, then C and D have the same parity, so beta = 0, and (E1) gives b = +-a, so V = +-U.
Case alpha = +-1: then mu is in {-1,0,1}. It cannot be odd, so mu = 0, and (E2) becomes m(aW + 2T alpha) = 0. The bracket is 2 mod 4, so m = 0 and n = 0.
Every case is excluded. []

PROOF OF THEOREM 3. Write m = iC + iD - iA - iB and nu = (eC+eD)T' - (eA+eB)T0. Then 2n = (2sPDc + sm, 2m + nu). Integrality of n forces an even number of even points. If both pairs have the same parity, U = a w and V = b w, and (E1) gives b = +-a, so V = +-U. A pair of equal parity together with a pair of mixed parity gives an odd number of even points. So both pairs are mixed. Swapping inside a pair is a symmetry, so we may take A and C odd: U = (sa, 2a+T0) and V = (sb, 2b+T'). Then |U|^2 = Q_{T0}(a) and |V|^2 = Q_{T'}(b), which gives (E1). The product U.2n = s^2 a(2PDc + m) + (2a+T0)(2m + T' - T0) = 0 rearranges to (E2).
The coefficient (s^2+4)a + 2T0 is nonzero: it is 2 mod 4 when a is odd, and when a is even it is congruent to 2T0, which is not 0 mod 4 since T0 is odd. So m is unique.
Bound on a: |s^2 a (2PDc + m)| = |U2||2n2| <= 2(h-1)^2, and |2PDc + m| >= 2P - 2(A-1) > 39h. So |a| < 2h/(39 s^2).
n != 0, because n1 = s(PDc + m/2) and |m| < 2A < 2P. V = U iff (b,T') = (a,T0). V = -U iff (b,T') = (-a,-T0).
Case b = 0: then Q_{T0}(a) = T'^2 with |T'| < h, which is exactly a P conflict between slots i0 and i0+a (stride_menu Proposition 1', set S_T). A P-free class excludes it.
The two forms of (E2) follow by substituting T' - T0 = 2Ds and adding Ds((s^2+4)a + 2T0) to both sides. The row of p is row(A) + n2 with n2 = m + Ds.
Fatality: C(R1) = {A,B,p,q} and C(R2) = {C,D,p,q}. If A, B, C, D are black, both presentations equal {p,q} minus S, whatever the colours of p and q. []

PROOF OF THEOREM 4.
Parity. If A, C have the same parity and B, D have the same parity, then g = d w and g' = d' w. In that case U.w = s^2(PDc + k) + 2U2 != 0, since s^2(P-(A-1)) > 76h > 2h. Then E2 = Sigma (U.w) forces Sigma = 0, so n = 0. One mixed pair together with one equal pair gives an odd number of even points. So each block holds one odd point and one even point.
Equations. E2 is U.(g+g') = 0. E1 is equivalent to 2U.(g'-g) + G = 0. Both contain U1 = s(PDc + k) linearly. Eliminating it gives 4U2(d'eta - d eta') = Sigma G, and d'eta - d eta' = Theta. Expanding E2 gives the second equation.
Theta != 0: if Theta = 0, then Sigma G = 0. G = 0 means V = U. Sigma = 0 with d != 0 forces eta' = -eta, so g' = -g and n = 0. d = 0 with d' != 0 forces eta = 0, so C = A. d = d' = 0 is the case below.
Combined form. Substitute k = (U2 - base)/2 into E2 to get 2s^2 Sigma P Dc + U2 M = s^2 Sigma base. Then use U2 = Sigma G/(4N1).
Bound on Sigma: s^2|Sigma||PDc + k| = |U2||eta + eta'| <= 2(h-1)^2 and |PDc + k| > 19h.
Sigma = 0: E2 reduces to U2(eta + eta') = 0. Since 2n = (0, eta + eta') != 0, we get U2 = 0. Then E1 gives G = -2s^2(d'-d)(PDc + k). If d = d' = 0, then G = (eta'-eta)^2 = 0 and V = U.
(a) For (1,1) we have base = 0, so E2 = s^2 Sigma P Dc + kM. Reducing mod p gives kM = 0 mod p. Since |k| < A < p and |M| < (s^2+4)(2h/(19s^2)) + 4h < 5h < p, either k = 0 or M = 0. Each choice turns E2 into s^2 Sigma P Dc = 0, a contradiction.
(b) For (1,1) with Sigma = 0: U2 = 2k = 0 gives k = 0, and E1 gives G = -2s^2(d'-d)PDc. Mod p, (s(d'-d))^2 + X^2 = 0. For p = 3 mod 4 this forces p | s(d'-d). But 0 < s|d'-d| < sh <= (s^2/2+4)h < p, a contradiction.
(c) For (-1,-1) with Sigma = 0: C and D are odd, so V = (s(PDc + k'), 2k'). U = (s(PDc+k), 0). Mod p, E1 becomes s^2 k^2 = W k'^2. If k' = 0, then k = 0 and T' = T0, so V = U. Otherwise W, and hence sigma^2 + 1, is a square mod p.
(d) For (1,-1), U2 = 2k + T' is odd, so U2 != 0 and Sigma = 0 is impossible. []

PROOF OF THEOREM 5.
(S2a) Take both sea points on the side. Then U = (x0'-x0, 0), so |U| is an integer L. C and D have the same parity, and V2 != 0, because otherwise V = +-U. If C and D are in one block, V = Di w and |V|^2 = 4(sigma^2+1)Di^2, which is not a square because sigma^2 < sigma^2+1 < (sigma+1)^2. If they are in different blocks, |V1| > 19sh and 0 < V2^2 < 2|V1| + 1, so |V1| < |V| < |V1| + 1. The case with both sea points on the diagonal is the same with U and V exchanged.
(S1) 2n1 = (sum of three label columns) +- x0 must be even. Label columns are 0 mod s, and s is even, so x0 is even. For s = 2 every sea column is odd.
Sea on the side with 4 | s and x0 = 2 mod 4: U1 = xB - x0 = 2 mod 4 and 2n1 = 2 mod 4, so U1 n1 = 2 mod 4. Hence U2 n2 = 2 mod 4. In E1, U1^2 = 4 mod 32 and V1^2 = 0 mod 16. If U2 is odd, the left side is 5 or 13 mod 16, which is not a square mod 16. If v2(U2) = 1, the left side is 8 mod 32, and V2^2 cannot be 8 mod 16.
Sea on the diagonal: U1^2 = 0 mod 16 and V1^2 = 4 mod 32. So U2^2 = 4 + V2^2 mod 16. This forces V2 = 0 mod 4 and U2 = 2 mod 4.
(S2b) Here 2n2 = yD - yB, so B and D have the same parity. E1 gives u^2 - w^2 = (yD-1)^2 - (yB-1)^2. E2 is u(xC + xD - xA - xB) + (yB-1)(yD-yB) = 0, where xC + xD - xA - xB = 2Dx + u - w. If Dy = 0, then u = +-w. The case u = 0 puts x0 = xB = 0 mod s, so that point is not a sea point. The case u = w gives B = D. The case u = -w gives n = 0. []

CHECKS (scripts in the script folder, all run with py).
- brute_mixed.py enumerates all mixed quadruples among full diagonals from the definition. At h = 600, s = 2, P = 12007 and offsets [-265,-261,-239,-499] it found 76 quadruples. All 76 are type I.2 with one odd and one even point in each pair, so there were no one-block, type-II or three-block cases. xcheck.py solves (E1)+(E2) for the same blocks and gets exactly 76 that pass the definition. The other 12 solutions fail only the strip condition (asserted).
- enum_types.py (I.2, h = 600, s = 2) found 1189 quadruples that pass the definition, 624 of them in the reflection subfamily. dbg_I2.py found no I.2 solution that fits the slot ranges at h <= 240 for s = 2, or at h = 700 for s = 4.
- enum_II.py at h = 500, s = 2, P = 10007 found 142 type-II quadruples, each checked from the definition, all with roles (1,-1). Example: T0 = -423, T' = 149, d = d' = -1, k = -143, Dc = 1, A = (426,427), C = (424,2), B = (20154,290), D = (20152,139). This run took about 2 minutes, over the 60-second rule. It found no (1,1) solutions at all. enum_II2.py (bounds on Sigma and d'-d) at h = 240 with P = 1 mod 4 found 172 equation solutions, all (-1,-1) with Sigma = 0. None fit the slot ranges. At h = 300 it found none for P = 1 or 3 mod 4.
- sea1.py (one sea point, one block): none for s = 2. For s = 4 and 8 the sea point is always on the diagonal. For s = 4 it found 10 distinct quadruples per 100 labels at h = 200, T = 1, for example A = (4,4), B = (8,6), C = (6,1), D = (8,5). For s = 8 there are also hits with x0 = 4 mod 8.
- sea2.py (two sea points, side and diagonal): all hits are in-block with B and D of the same parity. At s = 4, T = 1 there were 47 hits for 100 labels at h = 200 and 97 for 200 labels at h = 400. With two blocks there were no cross-block hits at (h,s) = (400,4) or (600,2). Example at h = 200, T = -21: A = (130,1), B = (52,27), C = (70,1), D = (124,63).

EARLIER DERIVATION (checked line by line). The legs (4t1, 2t1-T0) and (4(u+PDc), 2c2), with c2 = u + Ds, give 16t1(PDc+u) = 2c2(T0-2t1). Adding Ds(10t1-T0) gives u(10t1-T0) = Ds(T0-2t1) - 8t1PDc and u = -Ds + 8t1N/(10t1-T0). Since 10t1 - T0 is odd, gcd(10t1-T0, 8t1) = gcd(T0,t1), so u is an integer iff m | N. R = P + Q - V has row 2(iQ+t1) + 1 + 2Ds and lies in the column of slot iQ + t1 of class c'. If that slot is occupied, R is either white in a double column (Ds != 0) or black, making a fully black rectangle (Ds = 0), and both cases are fatal. If the slot is empty, the configuration is harmless only when that column's singleton is in an odd row other than row(R). All of this is correct. The load constant is heuristic: my count gives about rho^3 tau(T0) log h / 160 (both signs of t1, a window of length K for c2, P = 20h), against the stated /320. The order is the same.

HEURISTIC LOADS (not proved; random block order, slot density rho, about 1.2h classes, nu(T') = share of classes with offset T').
- I.2: E(label) ~ rho^3 sum_{|a| < 2h/(39s^2)} sum_{(b,T') in R(a)} nu(T') A g_a/(s^2 |a| P), where R(a) is the set of representations N_a = X^2 + (sb)^2. This is about rho^3 r log h/(24 s^2 h).
- II with Sigma != 0: about rho^3 log^2 h/(s^2 h^2) per label. The horizontal subfamilies are about rho^3 log h/(s^2 h) per label, and Theorem 4 (b) and (c) remove them by the choice of p.
- Right angles (E;O,E): Theta(rho^3 tau(T0) log h).
So label-only mixed quadruples are lower order, with a total of O(h polylog h) over the board. The sea families S1 and S2b are not lower order: they are 3-label and 2-label in-class constraints that depend on the rows.

COMPARISON WITH THE LEDGER. T14 (D_3 = O(h^(3+eps)), D_4 = O(h^(5+eps)), a margin of h^(-1+eps) per label at the permutation scale) is consistent with the O(polylog/h) loads here. Theorem 1 adds structure that T14 does not have: no one-block, three-block or four-block cases. T21 (CRT scaffold) is the I.2 reflection subfamily with R2 axis-aligned. It survives in the stride scaffold, with 624 verified instances at h = 600, but at load O(1/h) per label.

## External results used

- None. Paper sec2 Lemma mixedeq and sec5 Definition obstruction (2); stride_menu.md Proposition 1' (definition of S_T and P-freeness); lower_bound_windows.md axis owner lemma (for the earlier derivation only).

## Checks

Scripts in the matching scripts_ folder of this directory brute_mixed.py (definition-level brute force), enum_types.py and dbg_I2.py (I.2 equations), xcheck.py (brute force against equations, 76 = 76, strip-only failures asserted), enum_II.py and enum_II2.py (type II, vectorized), sea1.py (one sea point), sea2.py (two sea points, side and diagonal). Every reported hit was re-checked from the definition (|U| = |V|, n integral, nonzero and perpendicular, V != +-U, p and q in the strip).

## Gaps

- Loads are heuristic: random block order, independent slot occupancy and the heuristic gcd/integrality densities. No rigorous expected-count or local-lemma bound is proved.
- Type II (-1,-1) with Sigma != 0 is neither eliminated nor found: there were zero equation solutions in the runs at h = 300 and 500 (P = 3 mod 4), but the h = 500 run used an incomplete bound on d.
- S1 is analysed only for s = 2 and for sea columns with x0 = 2 mod 4 when 4 | s. Sea columns with v2(x0) >= 2 (strides 8, 12, 20) are open, and hits with x0 = 4 mod 8 exist for s = 8. S1 with three blocks or across blocks was not searched.
- S2b across blocks: not eliminated (a divisor of N of size about 38sh would be needed) and not found in the runs.
- Theorem 4 (b) and (c) need p in a residue class (p = 3 mod 4, and sigma^2 + 1 a nonresidue). Such primes p in (20h, Ch] exist for large h by the prime number theorem in arithmetic progressions. I did not check an explicit range.
- The computed counts (S1 about 0.1 and S2b about 0.5 per label in one block) come from full diagonals at h <= 400 only. Their growth with h is not established.
- No independent audit of any proof here. Every proof was re-read line by line by me only.
- Rule breach: one script (enum_II.py, h = 500) ran about 2 minutes, over the 60-second limit, and a second over-long run was stopped.

## Missing estimate

For label points alone, a rigorous version of the heuristic per-label loads O(polylog h / h) for I.2 and II, for example a first-moment count over random block orders, would let an alteration or local-lemma step remove them at constant cost. For the sea, a bound or an elimination for the in-block families S1 (4 | s, sea on the diagonal) and S2b (2-label, row-dependent) is missing. Equivalently, a sea design (for example row 1 only in odd columns, or a stride with a different 2-adic structure) that kills S2b inside blocks, with the in-class conflict graph kept of bounded degree.

## Next steps

- Choose p with p = 3 mod 4 and (sigma^2+1 | p) = -1 (for s = 4: p = 3 or 7 mod 20). This removes both horizontal type-II subfamilies.
- Settle type II (-1,-1) with Sigma != 0: either prove a mod-p elimination or run a complete search with the rigorous bound |d'-d| = O(h/s^2).
- Make the I.2 and II load counts rigorous under a random class order, and check that they are compatible with the (E;O,E) right-angle load.
- Classify S2b inside one block. B and D are on the same line w, so D - B = Di w, and the equations depend only on (row of B, Di). This gives a row-dependent distance graph that the class colouring must also avoid. Measure its degree as h grows.
- Test whether a row-1 sea restricted to odd columns kills S2b and S1 in-block (2-adic analysis with u, w odd), and what it costs in columns = 2 mod 4.
- Finish S1 for strides 8, 12, 20 (sea columns with v2(x0) >= 2) and S1 and S2b across blocks.

