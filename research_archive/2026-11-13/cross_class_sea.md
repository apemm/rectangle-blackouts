# Sea families inside and across classes in the rigid layout

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Not audited yet.

# Result

## Status

partial

## Summary

The rigid rule together with p = ±2 mod 5 kills every M2a made of two label points. Across classes, X1 and X2 survive every 2-adic and mod-p rule I found, and in rigid layouts their per-label loads stay positive. Inside a class, X1 and M2c have orientations with out-degree bounded by a divisor function, and the degeneracy observed up to h = 1024 is at most 2. I.2 and II get rigid-coordinate forms with partial 2-adic kills; a full kill of I.2 holds only under a prime-pattern hypothesis.

## Statements

Setting. Stride 4, one prime p > 20h, rigid layout of rigid_layout_cross_block.md. Class c sits at block M_c, a multiple of p. Its offset is s_c, with T_c = 2s_c + 1 and n(c) = s_c - M_c. A, K, i, j are as in that note. Write Ds = s' - s0, DM = M' - M0, Dn = n' - n0 = Ds - DM. "Rigid" means n(c) = kappa mod 2^nu for every c. Families and the validity criterion are those of block_sea_classification.md, and I.2 and II are those of mixed_quadruples_blocks.md.

L0 (coordinates; trivial). The label point of slot i in class c has column x = 4(i + M_c) = 4(j - n(c)). Its row is 2i+1 for the odd point and 2j+2 for the even point. Under the rigid rule, every even point satisfies x/4 = j - kappa (mod 2^nu), and every odd point satisfies x/4 = i (mod p).

(a) INSIDE ONE CLASS (proved unless marked).
A1 (X1 criterion and degree). In a class of offset T, an X1 triple with G = the odd point of slot 2u (u odd) and F = the even point of slot k exists iff
 (k - 3u)^2 - u(5u + T) is a perfect square r^2 >= 0, and 2k + T + 4u + 1 <= h.
On the diagonal, N_u := u(5u + T) > 0. The F's of a fixed G correspond to factorizations N_u = e1 e2, so there are at most tau(N_u) + 1 of them. The G's of a fixed F correspond to factorizations of D_F = (2k + T)(10k + T) > 0, so there are at most 2 tau(D_F). Orient each edge from its G end. The out-degree is then at most tau*(h^2/4) + 1, with tau*(n) = max over m <= n of tau(m).
A2 (M2c parametrization). Take an intra-class M2c with B and D deep. Then D - B = (4t, 2t) with t > 0, u2 = y_B - 1 >= 1, and lambda = n1/t = alpha/beta in lowest terms with 0 < lambda < 2. Then
 t = 2(u2/alpha)(2beta - alpha) beta^2 / F, with F = (alpha - 4beta)^2 + beta^2,
 alpha | u2, and F | 10 u2/alpha.
Each B therefore has at most sum over f | 10u2 of r_2(f) <= 4 tau(10u2)^2 partners D, all at higher slots.
 2-adic table:
 - (I) alpha and beta odd: v2(t) = v2(u2) <= 1.
 - (II) alpha odd, beta = 2 mod 4: v2(t) = 3.
 - (III) 4 | alpha, beta odd: v2(t) is 2 or 3.
 - (IV) alpha = 2 mod 4, beta odd: v2(t) = 2 + v2(z) + v2(beta - alpha/2) >= 3, which is unbounded.
 Splitting a class by i mod 4 removes family (I). Splitting by i mod 16 removes all families except (IV).
A3 (class count). Each diagonal splits into at most 3 chi(G_T) (2 tau*(h^2) + 8 tau*(10h)^2 + 3) classes that are independent for G_T, X1, M2c and X2 together. The factor 3 is the v2(i) mod 3 split of the note, which removes X2. The other factor is h^{O(1/loglog h)}. This is NOT a constant factor. Proving a constant factor is open.
A4 (numerics only). On full diagonals up to h = 1024 (T = 1, -1, 3, -3, 15, 105, -315, 945), the degeneracies of the intra-class X1 and M2c graphs are at most 2. Smallest-last colouring of G_T u X1 u M2c uses at most one more colour than G_T. The maximum degrees grow: X1 reaches 23 and M2c reaches 5 at h = 1024.

(b) BETWEEN CLASSES.
B1 (M2a killed; proved). Assume the rigid rule with nu >= 2, and p = ±2 mod 5. Then no M2a configuration has both deep points C and D among the label points, in the same block or in different blocks. Even-even pairs die by the rigid rule alone. Odd-odd pairs need (5/p) = 1, and they need v2(DM) in {0,1}. As a special case, Proposition 5's forbidden offsets D + (±4k(k+1), ±(4k+2)) are automatic between label points.
B2 (X1 across classes; equation proved, survival numerical). X1 with F the even point of label (i_F, j_F) and G the odd point of slot i_G = 2 mod 4 holds iff
 Delta^2 - (2j_F + 1)(i_G/2) = r^2, with Delta = (i_F - i_G) + DM and 2j_F + 2i_G + 2 <= h.
The equation does not involve the diagonal of G or n(c_G). So the rigid rule only fixes Delta mod 2^nu (Delta = j_F - j_G), and p only fixes Delta mod p (Delta = i_F - i_G). Neither gives a local obstruction, because Delta^2 - M = r^2 is a norm form.
B3 (X2 across classes; equation proved, survival numerical). Take V the odd point of slot i_V (i_V even, at least 2) and G the even point of slot i_G. X2 holds iff
 2a(Di + DM) = i_V(2Di + T_G),
with a an integer, a != 0 mod 4, g = 2Di + T_G in [1, h-1] and Di = i_G - i_V. Here E = (x_V + a, 1). Consequences:
 - a is fixed mod p by the two labels, so each pair of labels has at most one block offset at which X2 holds;
 - v2(i_V) = 1 + v2(a) + v2(Delta), with Delta = (j_G - j_V) - Dn;
 - under the rigid rule, Delta = j_G - j_V (mod 2^nu).
 So no rule on n(c) or on p removes X2.
B4 (M2c across classes; identities proved). With w = sigma - n1 one has (Delta - 2n1) w = e^2 + n1^2 and e u2 = n1(Delta + w). The shallow conditions read w != 0 mod 4 and 2n1 + w != 0 mod 4. Odd-odd pairs need n1 and e even. The heuristic load is O(polylog h/h) per label. Numerically, 0 cross-class instances were found.
B5 (heuristic loads). X2 has about c log(h/160)/(20 chi) per label and X1 about c tau(2j_F + 1) log h/(160 chi). Neither is O(1) once chi is bounded. Both need a shallow point E within h/76 columns of a block.

(c) MIXED QUADRUPLES.
C1 (I.2, rigid form; proved). n2 (10a + T0) = 8a(2Dn - Ds), so v2(n2) = 3 + v2(a) + v2(2Dn - Ds).
 - Ds = 0: killed in every one-prime layout.
 - Ds = 0 mod 2^nu and 2^nu >= h/8 (one more doubling than K/8): killed under the rigid rule.
 - Otherwise only the identity v2(n2) = 3 + v2(a) + v2(Ds) holds, and I.2 survives.
C2 (II with (1,-1); proved, in every layout). (2Dj + T0)(Sigma - Ds) = -8 Sigma (Dj - Dn). Hence v2(Ds) = v2(Sigma) and Sigma = Ds mod 2^(v2(Sigma)+3). Since 0 < |Sigma| < h/152, no pair with 2^(v2(Ds)) > h/152 is of this type.
C3 (II with (-1,-1); proved). Dj (5 Sigma - S) = 4 Sigma Dn, with S = s0 + s' + 1. Under the rigid rule, v2(Dj) + v2(5 Sigma - S) >= nu + 2 + v2(Sigma).
C4 (II with (1,1) and Sigma = 0; proved). (Ds + 5 delta)^2 - 20 delta^2 = 8 delta Dn, with delta = d' - d. The rigid rule kills it when v2(delta) <= nu - 2, and p = 3 mod 4 kills it in all cases.
C5 (variant; conditional). Assume H'(h): there is a prime p in (20h, Ch] such that p - 1 has a prime factor l1 > 1.035h and 2p - 1 has a prime factor l2 > 1.04h. Build a chunked linear layout: chunk k holds the k-th class of every diagonal at block mu = s + lambda_k, and chunks are h/280 + 2 positions apart. This layout has no label-only tilted right angle and no I.2, and its width is at most about 4C h^2 chi_max. H'(h) is a prime-pattern condition that I cannot prove for every h. The layout does not kill type II.

## Proofs

0. Coordinates (L0). The column of slot i of class c is 4(i + M_c), and j = i + s_c, so i + M_c = j - n(c). The rows follow from the label definition. Every claim below uses only L0, the equations quoted from the notes, and the size facts: |x| differs by at least 4(p - A) > 78h between blocks, every row difference is below h, and p > 20h.

A1. Take X1 (block_sea Theorem 1(B)). E = (x_E, 1) is the vertex, F is in an even row, so F is an even label point, and G is in a row = 5 mod 8, so G is the odd point of slot i_G = 2u with u odd. The theorem's condition is |x_F - x_G|/2 = d + M/d with d | M and M = (y_F - 1)(y_G - 1)/4. In one class, |x_F - x_G|/2 = 2|k - 2u|, y_F - 1 = 2k + T and y_G - 1 = 4u, so M = (2k+T)u, which is odd. Two positive odd numbers d, e with de = M and d + e = 2|t| (t = k - 2u) exist iff t^2 - M = r^2 with d = |t| - r. Substituting t = k - 2u gives (k - 3u)^2 - u(5u+T) = r^2.
 - Fixed G: (k - 3u - r)(k - 3u + r) = N_u. Each factorization e1 e2 = N_u with e1 <= e2 fixes k = 3u + (e1 + e2)/2, so G has at most tau(N_u) + 1 partners.
 - N_u > 0: slot 2u carries a label only if j = 2u + s >= 0, that is 2s >= -4u, so 5u + T = 5u + 2s + 1 >= u + 1.
 - Fixed F: multiply 4u^2 - (6k + T)u + k^2 = r^2 by 16. This gives (8u - 6k - T)^2 - 16r^2 = (2k + T)(10k + T) = D_F, with both factors positive. So F has at most 2 tau(D_F) partners.
 - Brute-force check: x1star.py compares a geometric enumeration (E in row 1, a column = 2 mod 4, right angle, W white in an even row) with this predicate on 10 diagonals at h = 64. The edge sets are identical.

A2. In one class, B and D of equal parity give D - B = (4t, 2t), and e = t > 0. block_sea's M2c equation n1((Delta - n1)^2 + e^2) = e u2 (Delta - 2n1) with Delta = 4t becomes n1((4t - n1)^2 + t^2) = t u2(4t - 2n1).
 - n1 != 0 because u2 >= 1. The boundary case u2 = 0 is excluded; those labels act as sea points.
 - Divide by t^3 with lambda = n1/t: lambda F(lambda) = (u2/t)(4 - 2lambda), where F(lambda) = (4 - lambda)^2 + 1. lambda = 2 is impossible, so t = 2u2(2 - lambda)/(lambda F(lambda)). Then t > 0 forces 0 < lambda < 2.
 - With lambda = alpha/beta: z = -t u2/n1 = -u2 beta/alpha is an integer, and gcd(alpha, beta) = 1, so alpha | u2.
 - Divisibility: gcd(F(alpha,beta), beta) = gcd(alpha^2, beta) = 1, and modulo 2beta - alpha we have F = 5beta^2, so gcd(F, 2beta - alpha) | 5. Hence t in Z forces F | 10 u2/alpha.
 - Degree: (X, Y) = (alpha - 4beta, beta) satisfies X^2 + Y^2 = F, so the number of lambda is at most the sum over f | 10u2 of r_2(f) <= 4 tau(10u2)^2. Each lambda gives one t.
 - 2-adic table. It uses v2(t) = 1 + v2(u2) - v2(alpha) + v2(2beta - alpha) + 2v2(beta) - v2(F) and v2(z) = v2(u2) + v2(beta) - v2(alpha) <= 1 (z != 0 mod 4).
  - (I) F = 2 mod 4.
  - (II) v2(beta) = 1 is forced, and v2(u2) = 0.
  - (III) v2(2beta - alpha) = 1.
  - (IV) v2(2beta - alpha) = 1 + v2(beta - alpha/2).
  - In (II) to (IV), v2(n1) >= 2, so 2n1 - z != 0 mod 4 follows from z != 0 mod 4.
 - Check (m2c.py): every intra-class M2c found by the note's predicate on all diagonals at h = 80 and h = 200 (359 and 2412 edges) satisfies alpha | u2 and F | 10u2. Families seen: (I) everywhere, (II) with v2(t) = 3 at h = 200. degen.py enumerates through the parametrization and re-checks every edge with the predicate.

A3. Orient X1 edges from the G end (out-degree at most tau*(h^2/4) + 1) and M2c edges from B to D (out-degree at most 4tau*(10h)^2). The union then has an orientation of out-degree k, so its degeneracy is at most 2k and its chromatic number at most 2k + 1. On each colour class of a proper colouring of G_T, apply that colouring and then the v2(i) mod 3 split (block_sea D2, not audited).

B1. Use block_sea Theorem 2's M2a criterion: y_C = y_D mod 2, y_C != y_D, L = |D - C| an integer, and either L = 2 mod 4, or L = 4 mod 8 with 8 | Dx. Equal row parity means both points are odd or both are even. Dx != 0, and Dx = 0 mod 4.
 - Put f = L - |Dx| > 0. Then f(2|Dx| + f) = Dy^2 and L = f mod 4.
 - Case L = 2 mod 4. Then f = 2delta' with delta' odd, Dy = 2eps, |Dx| = eps^2/delta' - delta', and eps is odd (otherwise |Dx| would be odd).
 - Case L = 4 mod 8. Then f = 4delta'' with delta'' odd, Dy = 4o with o odd, and |Dx| = 2(o^2/delta'' - delta'').
 - Even-even: Dy = 2Dj and Dx = 4(Dj - Dn). Write sigma = sign(Dx).
  - First case: (eps - 2sigma delta')^2 - 5delta'^2 = -4sigma delta' Dn. The left side is 1 - 5 = 4 mod 8, and the right side is 0 mod 8 when 2 | Dn.
  - Second case: (o - 2sigma delta'')^2 - 5delta''^2 = -2sigma delta'' Dn. The left side is 4 mod 8, and the right side is 0 mod 8 when 4 | Dn.
  - Under the rigid rule with nu >= 2, both cases are impossible.
 - Odd-odd: Dy = 2Di and Dx = 4(Di + DM).
  - The same algebra gives (eps - 2sigma delta')^2 - 5delta'^2 = 4sigma delta' DM, and in the second case the right side is 2sigma delta'' DM.
  - Mod 8: DM must be odd (first case) or = 2 mod 4 (second case). This also re-proves block_sea (D1) when DM = 0.
  - Mod p: DM = 0 mod p, and 0 < delta' < |eps| < p, so 5 is a square mod p. That is false for p = ±2 mod 5.
 - Check (cross2.py, cross_m2a.py), at h = 300, p ~ h as a stress test:
  - random order: 1570 even-even and 0 odd-odd at p = 307 (307 = 2 mod 5); 1593 even-even and 2683 odd-odd at p = 311 (311 = 1 mod 5);
  - rigid layout: 0 even-even at both primes; 0 odd-odd at p = 307 and 798 at p = 311;
  - every odd-odd hit had v2(DM) = 0, as predicted.

B2. This repeats A1 with |x_F - x_G|/2 = 2|Delta|, where Delta = x_F/4 - x_G/4 = (i_F - i_G) + DM, and L0 gives Delta = (j_F - j_G) - Dn. The equation contains only the slots, j_F and DM. "Not killed" is shown by examples, not by a theorem:
 - rigid layout with G_T-greedy classes at h = 300 and p = 307 (stress test): 996 cross X1 (0.044 per label), against 852 in a random order;
 - realistic p > 20h with random classes (chi = 4): 0.0005 per F at h = 1600 and 0.0018 per F at h = 2400 (realistic.py).

B3. Insert L0 into block_sea's X2 condition a = (y_V - 1)(y_G - y_V)/(x_G - x_V), with y_V - 1 = 2i_V, x_G - x_V = 4(Di + DM) and g = 2Di + T_G. This gives the equation. g is odd, which gives the valuation identity.
 - Reduction mod p: 2a Di = i_V(2Di + T_G). Since |a| <= h/76 < p/2, the labels fix a, and then they fix DM.
 - Numbers:
  - stress test at h = 300: rigid 3197 (0.142 per label), random 3350;
  - realistic p, chi = 4: 0.0040, 0.0055 and 0.0060 per V at h = 800, 1600 and 2400.

B4. From block_sea: tau^2 + tau z + e(u2+e) = 0 with tau = Delta - n1, and n1 z = -e u2. Put sigma = -(tau + z). Then tau sigma = e(u2 + e) and n1(tau + sigma) = e u2. Subtracting gives (tau - n1)(sigma - n1) = e^2 + n1^2, z = -(Delta + w), and u2 e = n1(Delta + w).
 - Delta = 0 mod 4 turns the shallow conditions into conditions on w.
 - Parity: with n1 odd, Delta - 2n1 = 2 mod 4, which forces e odd, w odd and u2 odd, so B is an even point. Odd-odd pairs (u2 even) therefore need n1 and e even.
 - Sampled count (m2cross.py), 3000 points B at h = 300 and p = 307: 0 cross-class instances. The same enumerator finds 184 intra-class instances at h = 200 (m2intra_test.py), which validates it.

B5 (heuristic, not proved). For X2: per V, the sum over odd g of the number of a <= 2i_V g/(4p) with a | 2i_V g is about (h/2) log(h/160) c(i_V). Each choice determines the column and row of G, which is present with probability about 1/(p chi). So the load per label is about log(h/160)/(20 chi) up to a gcd factor. X1 is analogous, with small divisors of M = (2j_F + 1)i_G/2.
 - Locality: |a| <= h^2/(4(p - h)) < h/76, and in X1 |x_F - x_E| = 2d <= h/78. So E always lies within h/76 columns of a block.

C1. Insert DM = Ds - Dn into the note's n2 = 8a(Ds - 2PDc)/(10a + T0). 10a + T0 is odd and |10a + T0| < 1.04h < p.
 - Ds = 0: n2(10a + T0) = -16a DM with p | DM, so p | n2 and |n2| >= p > h (n2 = 0 would force DM = 0).
 - v2(Ds) >= nu: v2(2Dn - Ds) >= nu, so |n2| >= 2^(nu+3) >= h, against |n2| <= h - 1.
 - Check (i2.py and i2v.py): 17 I.2 quadruples in the rigid layout at h = 300 and p = 307. All 17 pass the definition directly (|U| = |V|, n integral, nonzero and perpendicular, V != ±U, p and q in the strip). All have v2(Ds) = 0. The random order gave 0.

C2. The note's (E2) is U.(g + g') = 0. By L0, U = (4(Dj - Dn), 2Dj + T0), and eta + eta' = 2Sigma - 2Ds + T0 - T0. Halving gives the identity, with 2Dj + T0 odd.
 - If v2(Ds) != v2(Sigma), then v2(Sigma - Ds) <= v2(Sigma) < 3 + v2(Sigma), a contradiction.

C3. In the same way, U = (4(Dj - Dn), 2Dj) and eta + eta' = 2Sigma - T0 - T'.

C4. Insert X = 2(delta + Ds) and PDc = Ds - Dn into the note's X^2 + 16delta^2 = -32 delta PDc.
 - Rearranged: (Ds + 5delta)^2 - 20delta^2 = 8delta Dn.
 - If nu >= v2(delta) + 2, then reducing mod 2^(2v2(delta)+5) forces ((Ds + 5delta)/2^(v2(delta)+1))^2 = 5 (mod 8), which is impossible.
 - delta != 0, since d = d' = 0 gives V = U.

C5. In chunk k, s = mu - lambda_k and M = p mu.
 - Right angles: N = Ds - DM = -(p - 1)Dmu, so l1 | N. Theorem 2(e) of the rigid note applies.
 - I.2: 2Dn - Ds = Ds - 2DM = -(2p - 1)Dmu, so l2 divides the right side, and l2 does not divide 10a + T0 because |10a + T0| < 1.04h < l2. Hence l2 | n2, which forces |n2| > h.
 - Chunks are separated by more than the interaction ranges: |DM| <= h^2/16 + h for right angles and |DM| < 0.07h^2 for I.2. The other reductions of Theorem 5 (in-block, odd vertex, steep legs, rival pairs) do not depend on the order of the blocks.
 - Width: there are chi_max chunks of about h(1 + 1/280) positions each, at 4p columns per position.

## External results used

- block_sea_classification.md: criterion (V1)-(V5), Theorem 1 (X1, X2, Pa-Pc), Theorem 2 (M2a, M2c, M1C), (D2) v2(i) mod 3 split. Not audited.
- mixed_quadruples_blocks.md: Theorems 3 and 4 (equations of I.2 and II, |Sigma| < 2h/(19 s^2), (1,1) Sigma=0 equation). Not audited.
- rigid_layout_cross_block.md: Theorems 1, 2(c),(e), 4(a), 5 (rigid layout, ranges). Not audited.
- Elementary: r_2(f) <= 4 tau(f); quadratic reciprocity for (5/p).

## Checks

Scripts are in the script folders of this directory. All were run with py, one at a time. Each run took under 35 s, except the killed h = 400 batch.
- x1star.py: geometric brute force against the A1 predicate, 10 diagonals at h = 64. The sets were identical.
- m2c.py: A2 necessity at h = 80 and h = 200, with the 2-adic family census.
- degen.py: degeneracies and colourings at h = 256 and h = 1024.
- layout.py: rigid, random and region layouts.
- cross.py, cross2.py and cross_m2a.py: cross-class M2a, X1 and X2, with the even-even and odd-odd split and the v2(DM) histogram.
- m2cross.py and m2intra_test.py: sampled cross-class M2c, and the check of the enumerator on intra-class pairs.
- realistic.py: p > 20h with p = ±2 mod 5, at h = 800, 1600 and 2400.
- i2.py and i2v.py: I.2 enumeration in the rigid and random layouts at h = 160 and h = 300; i2v.py also checks the definition.
These are sanity checks, not proofs.

## Gaps

- A3 is not a constant factor. I did not prove that X1 or M2c inside one class has bounded degeneracy. The bound of 2 is numerical, for h <= 1024 and 8 diagonals.
- A2 family (IV) (alpha = 2 mod 4, beta odd) survives every split by i mod 2^k. I did not search it, beyond noting that it needs h of about 363 or more.
- B2 and B3: 'not killed' rests on examples. The examples with G_T-independent classes used p ~ h (stress test). The examples at realistic p > 20h used random classes. I ran no layout with both G_T classes and p > 20h.
- B4 and B5 are heuristic. I proved no first-moment bound for cross-class X1, X2 or M2c in the rigid layout, which is deterministic.
- C1 to C4 are partial kills only. No rule I found kills type II with (1,-1) or (-1,-1) and Sigma != 0. C5 depends on the unproved prime-pattern hypothesis H'(h). The chunked layout needs p = 1 mod l1-type conditions, and with the 2-adic version (p = 1 mod 2^nu) it cannot also have p = 3 mod 4. So II with (1,1) and Sigma = 0 then survives when 2^(nu-1) | d' - d.
- Everything here depends on block_sea_classification.md (Theorems 1 and 2, D2) and mixed_quadruples_blocks.md (equations E1, E2, II), neither of them audited. I re-derived only what is shown above. None of my proofs is independently audited.
- Fillers, boundary labels (u2 = 0, odd row 1) and V3 collisions are not treated.
- Rule note: one batch of three runs at h = 400 hit the 60 s timeout and was killed with no output. All other runs took under 35 s.

## Missing estimate

With the row-1 sea, the bottleneck is now the cross-class X2 relation 2a(Di + DM) = i_V(2Di + T_G), followed by X1. Each is a two-label fatal relation with E within h/76 columns of a block. Its heuristic load is about log(h/160)/(20 chi) per label, and no congruence rule on n(c), on M_c or on p touches it, because a is fixed mod p by the two labels. To reach O(h^2) one needs one of the following. (i) A slot or order selection that avoids, for every pair of blocks less than h/80 positions apart, the at most one offset per label pair at which X2 holds, at O(1) cost per class. (ii) A sea that is not in row 1 within h/76 columns of any block (only about 1/40 of the columns). That brings back the deep-layer problem of block_sea, now confined to block zones.

## Next steps

- Audit B1 (short and elementary). If it passes, add a ledger row: 'rigid rule with nu >= 2 and p = ±2 mod 5: no M2a among label points'. Combine it with the note's p = 3 mod 4 (II with (1,1) and Sigma = 0), which means taking p = 3 or 7 mod 20.
- Test the X2 locality: move the sea within h/76 columns of blocks to a high row r > (h+1)/2 (as in Proposition 3) and recount every obstruction near blocks. The rest of the width can keep the row-1 sea.
- Compute cross-class X2 in a rigid layout with G_T classes and p > 20h at h of about 1000-2000 (classes from cached greedy colourings) to fix the constant in B5.
- Try to prove degeneracy <= C for intra-class X1 with A1's factorization structure (edges come from factorizations of N_u = u(5u+T)), or find subgraphs whose minimum degree grows.
- Settle M2c family (IV) at h >= 400 and decide whether a v2-based split removes it.

