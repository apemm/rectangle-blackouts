# A degree-capped colouring removes the Bad_split term

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: Theorem DC. A deterministic greedy colouring with a cap on the number of shape moduli dividing each label coordinate (Lemma M, a k-th moment bound) leaves no monochromatic ratio edge in any class. It sends a Lambda^(-2)-sparse set to the weighted Theorem D. The classes no longer depend on (l, p). Theorem N stays at 1.4967429. Route L drops to 1, and Proposition 5 under (F) to h^2 (log h)^eta for every eta > 0. Stride (8,1) does not help, and whether chi(R_IV) is finite is still open. Not audited yet.

# Result

## Status

partial

## Summary

The Bad_split term can be removed without bounding chi(R_IV). A degree-capped deterministic colouring (Theorem DC) rests on a new k-th moment bound for the number of shape moduli dividing a label coordinate (Lemma M). It sends a Lambda^(-2)-sparse, AP-structured label set to the weighted Theorem D and leaves no monochromatic ratio edge in any class. Route L drops from 1.2493 to 1 (its value without Bad_split). Proposition 5 under (F) drops from 1 to any eta > 0. Theorem N stays at 1.4967429, because the heavy-light trade-off binds there. Stride (8,1) does not help: R_FF survives it 2-adically, and by a dilation argument R_FF alone is chi-hard in the same sense as R_IV. Whether chi(R_IV) is finite stays open. Bohr colourings with tame characters, or with Haar-almost-every character, provably fail.

## Statements

Notation as in consolidated_board_v2.md (board L***, stride (4,1), SAW*). Lambda = log h, ell = loglog h. Coordinates of a label f: x_IV(f) = u_f, with back-moduli p_lambda (R_IV^(4)), and the 8 depth maps x_j(f) = delta_o(f) or delta'_o(f), with back-moduli |U'_s| over all coprime shapes s = (a,b). The back-degree is b_j(f; H] = #{s : m_s <= H, m_s | x_j(f)}. "Later end" means the end with larger i (truncated_additive_split Lemma C). Status labels: PROVED means proved here and not audited. CONDITIONAL lists its hypotheses.

LEMMA M (moments of shape-divisor counts; PROVED, using audited Lemma B of truncated_additive_split and two elementary counts). Let M be the multiset {p_lambda} or {|U'_s|}. For k >= 1, A >= 0 and 0 <= H0 < H1, put
 S_k^A(H0,H1) := sum over ordered k-tuples of distinct shapes with all m_{s_i} in (H0,H1] of tau(L)^A / L, where L = lcm(m_{s_1}, ..., m_{s_k}).
Then S_k^A(H0,H1) <= C_{k,A,eps} (1 + log H1)^{c_{k,A}} H0^(-1/3+eps), where the factor H0^(-1/3+eps) is read as 1 when H0 = 0. For the R_IV family the log factor can be dropped: S_k^A(0, infinity) <= C_{k,A}.

COROLLARY A (density colouring of R_IV; PROVED). For all Y >= 1 and D >= k >= 1, deleting at most C_k Y / C(D,k) vertices from R_IV^(4) restricted to [1,Y] leaves a graph whose back-degree in increasing order is below D, so it is D-colourable. Equivalently, deleting eps Y vertices leaves chromatic number <= C_k eps^(-1/k), for every k.

THEOREM DC (degree-capped class colouring; CONDITIONAL on the hypotheses of v2 Theorem N, on weighted Theorem D (A-18) applied to a deterministic set, and on (AP)). Fix eta in (0,1). Put k = ceil(2/eta), D = ceil(Lambda^eta) and H1 = ceil(Lambda^7). Replace (B4) and (B8) of v2 as follows.
 (B4-DC) On each light (T,tau), let Y1 be the set of non-exceptional labels with b_j(f; H1] >= D for some coordinate j. Let Y2 be the set of those with m_s | x_j(f) for some s with m_s in (H1, h^(1/2)/32]. Send Y = Y1 ∪ Y2 to one weighted Theorem D group, with rho = 1. Colour the remaining labels of I(T,tau) greedily in increasing i against G_T, the R_IV edges, the 8 R_FF^- maps (all of height <= H1) and R_FF^+.
 (B8-DC) Bad_split is empty. Heights above h^(1/2)/32 go to R-e, as in v2.
Then:
 (a) c_{T,tau} <= kappa_T + 9(D-1) + 7.
 (b) Every class is G_T-independent and contains no in-class R_IV, R_FF^oo, R_FF^ee or R_FF^+ edge of height <= h^(1/2)/32.
 (c) The relocation costs <= C_eta h^2 ell^(C_eta), plus <= h^(2-eps) labels sent to Proposition partial.
 (d) The classes are deterministic and independent of (l,p), so step 2 (psi) of K6 disappears.

COROLLARY E (exponents under what is proved here).
 (i) Theorem N with DC: M <= C h^2 (B + 9 Lambda^eta + Lambda^(E(a)+1) B^(-a)) ell^C + c0 n_rel tau*(h)^2 + C_eta h^2 ell^(C_eta). The exponent is theta* = 1.4967429, unchanged, because Bad_split is gone and the heavy-light term binds. This is CONDITIONAL on N-1, N-3, N-4, K2/K4, (AP) and weighted Theorem D.
 (ii) Route L, CONDITIONAL on (Pc), (Eq) and (Bal) and on the hypotheses of (i): the exponent is 1, which equals its value without Bad_split. Was 1.2493. For a fixed moment order k the exponent is 1.24935 (k = 1), 1.13982 (2), 1.09547 (3), 1.05627 (5), 1.02458 (10), and 1 for every k >= 37.
 (iii) Proposition 5, CONDITIONAL on (F) and the hypotheses of (i): m_h <= C_eta h^2 (log h)^eta for every eta > 0. Was exponent 1. Without Bad_split the bound was powers of ell only. Here the gap is Lambda^eta.
 (A weaker intermediate result, also proved: a uniform random proper colouring against heights <= H0 gives 1.1798 for Route L and 4/5 for Proposition 5. DC supersedes it.)

THEOREM F (general-stride cubic; PROVED from Lemma mixedeq). Take stride (mu,nu) with r = mu/nu. Consider an in-class quadruple with side {L1,F1} and diagonal {L2,F2}, where L2 - L1 = (mu t, 2 nu t) and F1, F2 lie in one row. Put U = F1 - L1 = (alpha1, Y1), V = F2 - L2, P = alpha1 - alpha2 and m = P/(2 nu t) = a/b. Then:
 Y1 = nu t (r-m)(m^2+1)/(r-2m), alpha1 = nu t (m^2+1)/(2m-r), n = nu t (r-m, 1);
 Y2/Y1 = V_r/U_r, with U_r = (a-rb)(a^2+b^2), V_r = a^3 - r a^2 b - 3ab^2 + r b^3 and U_r - V_r = 2b^2(2a-rb).
d < 0 (t < 0) with both depths positive holds iff r/2 < m < r. At r = 4 this is the audited (iii-b) cubic.

THEOREM F2 (2-adic admissibility of in-class Fo/Fo; PROVED). Rows follow the SAW* rule: depth Y1 = 8(w+c) (mod 64), where w is F1's slot offset mod 4 and c is in {1,3}. Classes have t = 0 (mod 32). Write A = alpha1/4 and beta = v2(b).
 (i) Stride (4,1): a odd, b even, w = 0 (both fillers in the hole row T* - 24), v2(A) = beta + 1, v2(t) = 2 beta + 4, and 2 < m < 4. Conversely, for beta in {1,2}, every admissible shape and every pair of labels in one class with depths 8 o1 and 8 o2, o2/o1 = |V'|/|U'|, gives a fatal quadruple. Its fillers are never label slots.
 (ii) Stride (8,1), same rule, 4 < m < 8: three families. (alpha) a odd, b even, w = 0, v2(A) = beta + 1. (beta) b odd, v2(a) = 2, w odd, w + c = 2 (mod 4). (gamma) b odd, v2(a) >= 4, w odd, w + c = 4.
R_IV (a = 2 mod 4, b odd) and R_FF^oo (a odd, b even) are 2-adically disjoint subfamilies of one cubic over m in (2,4).

PROPOSITION O_FF (R_FF alone is chi-hard; PROVED). Let G be the graph on odd integers with o ~ o |V'_s|/|U'_s| (when |U'_s| divides o) over the shapes of F2(i) with beta in {1,2}. Its edges preserve o mod 16 and are invariant under odd dilation. Take a type whose odd depths 8o fill o = c_tau (mod 8) on [o1, o1 + X] with o1 <= X/(2Y). Take F, a connected subgraph of G on [1,Y]. Then any partition of the type's labels outside a set E into classes with no in-class Fo/Fo violation has at least chi(F) classes whenever |E| Y < X/(16Y) - 1. So O(1) classes with h^(2-delta) bad labels in total force chi(G restricted to [1, c h^(delta/2)]) = O(1). Unlike Proposition O, there is no 2-adic compatibility caveat.

THEOREM B (Bohr colourings of R_IV^(k) and G; PROVED). R_IV^(k) is the induced subgraph, on odd integers, of the Cayley graph of Gamma (positive rationals with odd numerator and denominator, a free abelian group) with generators rho_lambda^(±1). Its chromatic number is finite iff S_k is not a set of chromatic recurrence in Gamma. A Bohr colouring of R_IV^(k) or G cannot come from:
 (a) a character Gamma -> T^d that is continuous for finitely many places (the archimedean place plus finitely many p-adic places), for example theta_p = c log p plus Dirichlet-character or finitely many free corrections;
 (b) Haar-almost every character Gamma -> T^d.

PROPOSITION S (stride (8,1); inventory plus F2 and O_FF). Stride (8,1) removes in-class R_IV only under v2(y - r) = 1. It keeps in-class R_FF, with three 2-adic families, and it forces a re-derivation of about 20 of the 26 audited inputs. It does not change theta*. With DC, it brings no gain.

OPEN: chi(R_IV^(5)) < infinity or growth. Bipartiteness of G (numerically bipartite on [1, 3·10^7]). A Bad_split cost of ell^C, rather than Lambda^eta, in Proposition 5.

## Proofs

0. INPUTS AND CONVENTIONS
I use the following audited inputs:
- Lemma mixedeq (P1);
- additive_class_split Lemmas 1, 2 and 4: R_FF shapes, Y1 = mu|U'|, gcd(U,V) | 40;
- truncated_additive_split Lemmas A, B and C: N(H) = O(H^(2/3)), the tails sum of tau^C/m over m_s > H being << H^(-1/3+eps) for both families with any fixed C, and the later ends;
- polylog Lemma IV (g | 5, p > be^3/5);
- weighted Theorem D (A-18), with (AP) for moduli up to h^(1/2);
- V2-3 (an edge-presence event is a union of O(1) classes of i mod lcm(32,q));
- heavy_diagonals_sharp: Proposition 3, Proposition 5, Route L and their exponent tables.

1. PROOF OF LEMMA M

M0, multiplicities. Let R(n) be the number of shapes with back-modulus n.
- FF family. |U'| = n means (a-4b)(a^2+b^2) = ±g'n with g' | 40. Put delta1 = a - 4b, a signed divisor of g'n. Then (4b + delta1)^2 + b^2 = ±g'n/delta1 is a quadratic in b with at most 2 roots. So R_FF(n) <= 64 tau(40n) <= C tau(n).
- IV family. p_lambda = n is odd, and C(al,be) = gn with g in {1,5}, where C = 4al^3 - 16al^2 be + 13 al be^2 + 4be^3.
  - Box. C = alF + 4(be-al)be^2 > be^3, and since F < 17be^2, C < 21be^3. So every solution lies in [1, N^(1/3)]^2, with N = gn.
  - Roots. Each primitive solution gives a projective root of C mod N. The disc of C(x,1) is 6832 = 2^4·7·61, and that of V(x,1) is 1708 = 2^2·7·61 (both checked by script). The x^3 and y^3 coefficients are 4, so there are no roots at infinity for odd p.
  - For odd p not in {7, 61}, Hensel gives at most 3 roots mod p^e.
  - For p in {7, 61}, v_p(disc) = 1. Factor f = (x-s)q over Z_p. Then v_p(disc q) = 1, so q has no root mod p^2. There are at most 2 roots mod p and at most 1 mod p^e for e >= 2.
  - So there are at most 3^omega(N) root classes.
  - Lattice. The fibre of a root class lies in a lattice of covolume N. Let v be its shortest vector. Every lattice point outside Zv is at distance >= N/|v| >= N/rho from the line Rv. The box lies in the disc of radius rho = sqrt2 N^(1/3), and N > 512 (since p >= 749) gives N > 4 rho^2. So only ±v can be primitive points in the box.
  - Hence R_IV(n) <= 4·3^omega(5n) <= 12 tau(n)^2.

M1, local weight. Let W_A(d) be the sum of tau(m_s)^A/m_s over the shapes with d | m_s <= H1. Then
 W_A(d) = sum over e <= H1/d of R(de) tau(de)^A/(de) <= (C tau(d)^(A+2)/d) · sum over e <= H1 of tau(e)^(A+2)/e <= C_A tau(d)^(A+2) (1 + log H1)^(2^(A+2))/d.

M2, gcd sums. Use gcd(m,L) = sum over d | gcd(m,L) of phi(d). Then the sum over s of gcd(m_s,L) tau(m_s)^A/m_s equals the sum over d | L of phi(d) W_A(d). By M1 this is <= C_A (1 + log H1)^c · sum over d | L of tau(d)^(A+2) <= C_A (1 + log H1)^c tau(L)^(A+3).

M3, nesting. Write L_j = lcm(m_1, ..., m_j). Since lcm(L,m) = L m/gcd(L,m),
 1/L_k = product over j of gcd(m_j, L_{j-1})/m_j, and tau(L_k) <= product of tau(m_j).
Let Phi_j be the sum over s_{j+1}, ..., s_k of the product over i > j of gcd(m_i, L_{i-1}) tau(m_i)^A/m_i.
- Claim: Phi_j <= K_{k-j} tau(L_j)^(B_{k-j}), with K_0 = 1 and B_0 = 0.
- Step: Phi_{j-1} <= K tau(L_{j-1})^B · (sum over s_j of gcd(m_j, L_{j-1}) tau(m_j)^(A+B)/m_j). By M2 this gives B_{k-j+1} = 2B_{k-j} + A + 3 and K_{k-j+1} = C (1 + log H1)^c K_{k-j}.
- So S_k^A <= K_{k-1} · (sum over s_1 with m_1 in (H0,H1] of tau(m_1)^(A+B_{k-1})/m_1).
- That sum is << H0^(-1/3+eps) by Lemma B, or O(1) by Lemma 4 / Lemma IV when H0 = 0.

Uniform IV version. For the round box of M0, the primitive points of a covolume-d lattice in a disc of radius R number at most C(R^2/d + 1). If d > 4R^2, there are at most 2. Otherwise:
- lines parallel to v are d/|v| apart;
- at most 2R|v|/d + 1 of them meet the disc, each with at most 2R/|v| + 1 points;
- the line through 0 has 2 primitive points;
- |v| <= 1.08 sqrt d, and AM-GM finishes.
So #{s : d | p_s, p_s ~ X} <= C rho*(d)(X^(2/3)/d + 1). Summing over dyadic X >= d with the tau weights gives W_A(d) <= C rho*(d) tau(d)^A / d with no log factor. M2 and M3 then hold uniformly.

Corollary A. #{u <= Y : b(u) >= D} <= sum over u of C(b(u),k)/C(D,k) <= (sum over k-sets of floor(Y/L))/C(D,k) <= Y S_k^0/C(D,k). Off this set the greedy colouring in increasing u uses at most D colours.

2. PROOF OF THEOREM DC
(a) Greedy in increasing i. G_T contributes at most kappa_T back-neighbours. R_IV contributes one per lambda with p_lambda | u (the later end is p m). Each R_FF^- map contributes one per shape with |U'| | delta (the later end is the shallower label at depth mu|U'|, Lemma 1). Off Y1 this is at most D - 1 per coordinate. R_FF^+ contributes at most 6, since the slot step is 32 and the range is 210. The colour count is at most kappa_T + 9(D-1) + 7.
(b) Take an in-class edge {f', f} with both ends kept and f its later end in coordinate j. If its height exceeds H1, then m_s | x_j(f) with m_s > H1, so f is in Y2, a contradiction. Otherwise f' is a back-neighbour counted in b_j(f; H1] < D, and the greedy colouring separates the two. Fatal in-class family-IV and homogeneous Fo/Fo and Fe/Fe pairs are edges of these graphs (B4 "only if", Lemma 1, audited). This includes v2's R-b exclusion for even rows near the filler band. J3 in hitting-set form (V2-1) then applies.
(c) Pointwise, 1[f in Y] <= sum over j of C(b_j(f;H1], k)/C(D,k) + sum over j and s with m_s in (H1, h^(1/2)/32] of 1[m_s | x_j(f)]. The first term is the sum over k-sets S of 1[lcm S | x_j(f)]/C(D,k). So Y satisfies the weighted hypothesis:
- rho = 1;
- weights c_q equal to (#k-sets with lcm q)/C(D,k), or to 1 for a single m_s;
- moduli lcm(32, q) <= 32 H1^k < h^(1/2), so (AP) applies (V2-3 makes each event O(1) residue classes of i);
- independence across diagonals holds trivially, because Y is deterministic;
- rho = 1 >= (log h)^(-C').
Its kappa is <= 9[S_k^C(0,H1)/C(D,k) + kappa(>H1)] <= C_k (log H1)^(c_k) k^k Lambda^(-2) + C Lambda^(-7/3+7eps), by Lemma M and Lemma B, using C(D,k) >= (D/k)^k >= Lambda^2/k^k. Weighted Theorem D then costs C(kappa ell^C h^2 Lambda^2 ell^(C1) + h^2 ell) <= C_eta h^2 ell^(C_eta), plus |E| <= h^(2-eps) sent to Proposition partial (R-g). Only non-exceptional labels enter Y, which is the v2-audit form of rule 2.
(d) Immediate.

3. PROOF OF COROLLARY E
(i) Replace v2's Theorem D Bad_split term by (c), and B by B' = B + 9 Lambda^eta + 16. The classes are G_T-independent, at most B' per (T,tau). Proposition R, J4, A4, B7, D8, D17, D18 and L-adic are linear in the class count or independent of it (truncated audit, issue 6). The exponent is max(x, E(a) + 1 - a x, eta), minimised at theta* = min_a (3+3^a)/(2(1+a)) = 1.4967429.
(ii) In Route L each piece is coloured by DC: G_T-piece back-degree <= w, plus 9D + 7, with no B0. Its Bad term becomes the cost (c). Width exponents are max(d, b1, q+d, 1), the heavy term is 2 - phi(q + b1), and relocation is 2 - k d (for D = Lambda^d). Take d = eta <= d0 = 0.0273749, q = 1 - eta and b1 = 1. phi is increasing for y >= 1/2 (dphi/dy = ln 2y), and phi(2 - d0) = 1, so 2 - phi(2 - eta) <= 1, and the exponent is 1. The scan (routeL_dc.py) reproduces 1.24935 at k = 1, the old random split, as a consistency check.
(iii) In Proposition 5 the classes are translates; DC colours each with 9D + 7 colours. The width is O(h^2 B Lambda^eta) with B = O(ell). The uncovered labels cost h^2 Lambda^(-1). The relocation costs C_eta h^2 ell^(C_eta). The total is C_eta h^2 Lambda^eta ell^C.

4. PROOF OF THEOREM F
- Lemma mixedeq gives 2n = 2(Dx,Dy) + V - U, n·U = 0 and |V| = |U|, with Y2 = Y1 - Dy.
- So 2n = (2Dx - P, Dy), (2Dx - P) alpha1 + Dy Y1 = 0, and P(alpha1 + alpha2) = Y2^2 - Y1^2 = Dy^2 - 2 Dy Y1.
- Eliminating alpha1 gives (2Dx - P)(P^2 + Dy^2) = 4 Dy Y1 (Dx - P).
- P = Dx is impossible (the left side is nonzero, the right side is 0).
- With Dx = mu t, Dy = 2 nu t and P = 2 nu t m, the formulas follow, and alpha1 = Y1/(m - r).
- Y2/Y1 and U_r - V_r are direct expansions. The sign condition is (r-m)/(r-2m) < 0.
- At r = 4 this is the factorisation of additive Lemma 1 (audited).

5. PROOF OF THEOREM F2
Put A = alpha1/4. Then t = 4A(2a - rb)b/(a^2+b^2) and Y1 = 4A(a - rb)/b. F2's slot offset is (mu/4)t + A - P/4, with P = 2ta/b. The allowed v2(Y1) are 3 (w + c odd), 4 (w + c = 2 or 6) and 5 (w + c = 4). Also w odd <=> v2(A) = 0, w = 2 <=> v2(A) = 1, and w = 0 <=> v2(A) >= 2.

r = 4:
- b odd, a odd: v2(t) = 2 + v2(A) >= 5 forces w = 0, but then v2(Y1) = 2 + v2(A) >= 5 is not 3. Impossible.
- b odd, v2(a) = 1: v2(Y1) = 3 + v2(A). Each w contradicts the allowed values.
- b odd, 4 | a: v2(t) = 4 + v2(A) forces w even, so v2(Y1) would have to be 3, but it is >= 5. Impossible.
- b even, a odd: v2(Y1) = 2 + v2(A) - beta. w odd or w = 2 gives v2(Y1) <= 2, which is too small. So w = 0, v2(A) = beta + 1 and v2(t) = 2 beta + 4. The same-row condition holds because v2(P/4) = beta + 3 >= 4.
Converse: given o1 = mu|U'|, A = 2 o1 b/(a - 4b) is an integer ((a - 4b) | U'), and t = 16 o1 b^2 (a - 2b)/U is an integer (U = gU' with g in {1,5}, and 5 | g implies 5 | a - 2b). Then t < 0, v2(t) >= 6 and P, n are integers. The fillers have slot offsets = A (mod 16), with A = 4 or 8 (mod 16) when beta is in {1,2}. Every label slot of R_tau is rho_tau (mod 16) by [F1], so the fillers are SAW* fillers in row T* - 24. The corner rows are y_L + t >= y_L2 + |t| >= 1. The rectangles are distinct (V ≠ ±U, since t < 0). With the support black, both rectangles show the same corners, so the quadruple is a violation.

r = 8, same scheme:
- (alpha) is the b-even case unchanged.
- b odd, v2(a) = 2: v2(a - 8b) = 2 and v2(a - 4b) >= 3. So v2(Y1) = 4 + v2(A), which needs w odd and w + c in {2, 6}.
- v2(a) = 3: v2(Y1) >= 6, which never occurs.
- v2(a) >= 4: v2(Y1) = 5 + v2(A), which needs w odd and w + c = 4. Here v2(t) = 5.
- v2(a) = 1, or a and b both odd: contradiction as at r = 4.

6. PROOF OF PROPOSITION O_FF
- Signs. U and V are negative on (2,4), and |U| - |V| = -4b^2(a - 2b) has v2 = 2 + 2 beta >= 4, with g odd. So o2 - o1 = mu(|V'| - |U'|) = 0 (mod 16).
- Copies. A connected F has all of its vertices in one odd class v0 mod 8. Copies m F with m = c_tau v0^(-1) (mod 8), m in [o1, (o1 + X)/Y], number at least X/(16Y) - 1. A point of E lies in at most |V_F| <= Y copies.
- Types fill a full class. For i = iota (mod 32), o = (Y0 - 2i - 1)/8 steps by 8.
- An E-free copy consists of present labels of the type. By F2(i), each of its edges is fatal within a class, so the partition restricted to the copy colours F properly.

7. PROOF OF THEOREM B
Reformulation:
- If u and v are odd and v/u = p/q in lowest terms, then q | u. So R_IV^(k) is the induced subgraph described above.
- Dilating by a common odd denominator embeds every finite subgraph of the Cayley graph into it. de Bruijn–Erdős then gives equal chromatic numbers.
- Finite chromatic number means a finite colouring with no x ~ x s, which is the negation of chromatic recurrence.
- A character phi with ||phi(s)|| >= eps on S_k gives a (1/eps + 1)-colouring.
(a) Take D = 2^(k-2) times the product over p in P of p^j, put be = al + D with al -> infinity and gcd(al, D) = 1. Then rho - 1 = 4D be^2/(al F) <= 4D/al -> 0. For p in P (p ≠ 5), F = 5be^2 (mod p) is a unit, so v_p(rho - 1) = v_p(D) = j. For p = 5, F = 5be^2 + 8D be + 4D^2 has v5(F) = 1, so v5(rho - 1) = j - 1. Letting j -> infinity, rho_lambda -> 1 at every place of P ∪ {infinity}, so phi(rho_lambda) -> 0. For G, the same works with a = 2b + D, D odd, b = 2 (mod 4) and b -> infinity: rho - 1 = 4b^2 D/|U| -> 0 and U = -10b^3 (mod p).
(b) Choose lambda_j with al_j = l_j, a new prime larger than every prime factor of the earlier p, q, and not 5 or 17, with be_j = l_j (mod 2^(k-2)). Then F = 17be^2 (mod l_j) is a unit, so v_{l_j}(q_j) = 1 and l_j does not divide p_j. The exponent matrix restricted to the columns l_j is triangular with nonzero diagonal, so the rows are Z-independent. Every nontrivial Fourier coefficient of theta -> (phi(v_j))_j vanishes, so the push-forward is Haar on (T^d)^J. Hence P(all ||phi(v_j)|| >= eps) = (1 - (2eps)^d)^J -> 0. Take a union over rational eps.
Remark on Peres–Schlag and LLL: every event depends on theta_3, theta_5 and so on, so the dependency degree on [1,Y] is about N(Y) and nothing beats the union bound, chi <= C Y^(2/3).

8. PROPOSITION S (inventory, read from v2's hypothesis list and the ratio, stride_menu and saw notes)
Must be redone at stride (8,1):
- G_T moves to Q(sqrt17) (64d^2 + (2d+T)^2 = L^2), and heavy_diagonals Lemma 1 and Theorem 2 must be redone in Z[(1+sqrt17)/2] (class number 1, unit 4 + sqrt17 of norm -1). The Rankin exponents keep their form, so theta* is unchanged.
- p > max(68h, 40h) (stride_menu 1c), a width factor >= 1.7.
- The deep layer gains fillers in columns = 4 mod 8, which requires redoing SAW Theorem 1 (A-9), the SAW* Feo kill (A-12, whose P- and V-vertex valuations use the (4,1) geometry), Table J1* and the seams (A-21), and BH16 A1–A3 (A-22).
- block_sea Theorems 1 and 2 (A-1), rigid Theorem C (A-2), mixed_quadruples 1–4 (A-3) and the v3 cells (A-15) all use Delta = mu Dt.
- two_filler (A-20) needs the cubic of Theorem F at r = 8.
- Lemma N and Q3 (A-23), Q4 (A-24), Theorem K (A-25), and K2/K4/S1L (A-26). S1L uses slot offsets mod 4 on the (4,1) class line.
- Cross-class M2c needs counts for v2(DM) in {a-2, a-1} (odd-odd) and v2(Ds - DM) in {a-3, a-2} (even-even), plus a separate even-even case for a <= 3. These are open.
- In-class R_FF survives (F2(ii)), and O_FF transfers verbatim to any SAW*-type stride-8 layer with dilation closure.
Unaffected: P1–P3, A-14, A-16, A-18, A-19, and Theorems D and E in form.

## External results used

- de Bruijn–Erdős compactness theorem (only for the Cayley reformulation in Theorem B).
- Hensel's lemma for simple roots, and the factorisation over Z_p of a polynomial with a mod-p factorisation into coprime factors (standard).
- Elementary facts about 2D lattices (covolume <= lambda_1 times distance to the line; reduced bases) and the Fourier characterisation of Haar measure on tori (standard).
- The standard divisor-sum bound: the sum over e <= X of tau(e)^r/e is <<_r (log X)^(2^r).
- No published theorem beyond these was used. Huxley's and Stewart's root-count bounds were avoided by an elementary argument at p = 7 and 61.

## Checks

Analytic work first. Each script below ran once (or a few times) with py -I, under 60 s and well under 1 GB, in scripts_badsplit/. The repository was only read, and I ran no git commands.

- fofo_adm.py (raw mixed-pair equations, no parametrisation) and fofo_param.py (parametrisation of Theorem F, each solution re-verified by the raw equations, 0 failures).
  - Stride (4,1): 15 solutions, all in the type (w=0, a odd, v2 b in {1,2}, v2 A - v2 b = 1, v2 t = 2v2 b + 4). Examples: (a,b) = (5,2), t = -320; and (9,4).
  - Stride (8,1): 30 solutions in exactly the predicted families: (alpha) (9,2), (17,4); (beta) (20,3) with w = 1 and w = 3; (gamma) (16,3), (32,7). There are none with v2(a) = 3, as predicted.
- bip_ff.py (union-find with parity).
  - R_IV^(4) on [1, 2·10^6]: 313 shapes, 4057 edges, bipartite. This matches the earlier numerics.
  - G (stride 4, v2 b in {1,2}) on [1, 2·10^6]: bipartite.
  - The full b-even family on [1, 3·10^7] (4891 shapes, 604429 edges): bipartite. The smallest ratios are 101/53, 103/87, 175/111 and 689/241.
- moments.py.
  - disc C(x,1) = 6832 and disc V(x,1) = 1708.
  - Max multiplicity R(n) is 1 (IV) and 3 (FF), with R/tau^2 <= 0.25.
  - Factorial moments over x <= 4·10^6, for FF |U'| over all shapes with m in (2,4): E[C(b,k)] = 0.504, 0.224, 0.135, 0.103 for k = 1..4. P(b >= D) = 0.36, 0.097, 0.030, 0.0105, 0.0043, 0.0018 and 3.4e-4 at D = 8. The tail is geometric-like, with the ratio slowly decreasing, which fits the sub-exponential heuristic.
  - R_IV: E[b] = 0.00404 and max b = 2.
- expo.py: Route L reproduces 1.2493225. The truncated uniform variant gives 1.1798335 (closed form; a coarse grid gives 1.193). Proposition 5 truncated gives 0.8.
- routeL_dc.py: d0 = 0.0273749 and phi(2) = 1.0320. The degree-cap Route L exponents are 1.24935, 1.13982, 1.09547, 1.05627, 1.02458 and 1.0 at k = 1, 2, 3, 5, 10 and 40.

Read in full: ratio_graph_r_iv.md and its audit, additive_class_split.md and its audit, truncated_additive_split.md and its audit, consolidated_board_v2.md, and heavy_diagonals_sharp.md. Read in part: saw_residual_families.md (iii-b), stride_menu.md (1), polylog_relocation_diluted.md (Theorem D, its weighted form, Lemma IV), and Lemma mixedeq in sec2_prelim.tex. The ledger (2026-11-09) has no stride rows; T22 (the CRT Cayley-graph equivalence) is the nearest analogue.

## Gaps

- Nothing new here has had a second reader: Lemma M, Corollary A, Theorem DC, Corollary E, Theorems F, F2 and B, and Proposition O_FF.
- Theorem DC applies weighted Theorem D (A-18) to a deterministic set with rho = 1 and composite moduli lcm(S) <= 32 Lambda^(7k). The D1-D3 proofs were written for random sets. I checked that they use only the pointwise bound P(f in Y) <= rho_f, independence (trivial here), Chebyshev (the variance is 0 here) and (AP) for q <= h^(1/2). An auditor should confirm that nothing else needs non-degenerate randomness.
- The constants c_k and B_k in Lemma M grow doubly exponentially in k (B_{j+1} = 2B_j + A + 3, with log exponent 2^(B+2)). The bounds are asymptotic only, and k >= 37 is needed for Route L to reach exactly 1.
- Proposition 5 reaches Lambda^eta, not powers of ell. Heuristically, primorial-type N have exp(c y^(2/3)/log y) modulus divisors, so P(b >= D) >= exp(-(log D)^(3/2+o(1))). The degree-cap method then needs D >= exp(c ell^(2/3)) and cannot reach ell^C. This heuristic is not proved.
- Route L stays conditional on (Pc), (Eq) and (Bal), and Proposition 5 on (F). Theorem N stays conditional on N-1, N-3, N-4, K2/K4 completeness, (AP) and weighted Theorem D. Nothing here proves m_h = O(h^2).
- Route (a) is not resolved: chi(R_IV^(5)) < infinity, infinity, or a growth rate, is open. Theorem B excludes only tame or Haar-generic Bohr characters, and Katznelson's question (Bohr versus chromatic recurrence) blocks the converse.
- Bipartiteness of G (the stride-4 Fo/Fo depth graph) is open. It is bipartite on [1, 3·10^7] by union-find. No odd-relation certificate was computed, so O_FF gives chi >= 2 only.
- Theorem F2(ii) and the stride-(8,1) part of Proposition S transplant the SAW* row rule to stride 8. No stride-8 layer was specified, and the inventory is a reading of the hypothesis list, not a proof.
- The Fe/Fe 2-adic families (b = 0 mod 4 with v2(b) = 2 + v2(A)) were derived in outline only and not brute-forced. DC does not need them, because it uses the superset graphs.

## Missing estimate

None is missing for removing Bad_split in the exponent sense: Theorem DC with Lemma M does it at a cost of Lambda^eta. Two things remain. (1) To bring Proposition 5 from Lambda^eta down to powers of ell, the board needs either a relocation price below Lambda^2 for the divisor-rich set {b >= D}, or chi of R_IV together with the 8 R_FF maps on [1,h] at most ell^C. The heuristic in Gaps says the degree cap alone cannot do it. (2) The literal target, O(1) parts with an h^(2-delta) bad set, is still chi-hard: it needs bounds on chi(R_IV^(5)) (Proposition O) and on chi(G) (Proposition O_FF) on [1, h^(delta/2)]. Both are open, and no stride change avoids them.

## Next steps

- Audit Lemma M (M0-M3, about one page) and Theorem DC (a)-(d). In particular, confirm that weighted Theorem D accepts a deterministic Y with rho = 1 and moduli lcm(S).
- Edit consolidated_board_v2.md: replace (B4)/(B8) and truncated (B4')/(B8') by (B4-DC)/(B8-DC), drop psi from K6, and state Theorem N with the term C_eta h^2 ell^(C_eta) in place of the Bad_split term.
- Restate Route L and Proposition 5 in heavy_diagonals_sharp.md with the DC piece colouring, giving exponents 1 and eta. The binding hypotheses are now (Pc), (Eq), (Bal) and (F) alone, so effort should move there.
- Add ledger rows: 'Lemma M: k-th factorial moments of shape-modulus divisor counts are O_k((log H1)^(c_k) H0^(-1/3+eps))'; 'Theorem DC: Bad_split replaced at cost Lambda^eta'; 'Theorem F2: in-class Fo/Fo at (4,1) needs a odd, b even, hole-row fillers'; 'R_IV density-colourable: chi after deleting eps Y vertices <= C_k eps^(-1/k)'.
- Do not pursue stride (8,1): it removes in-class R_IV only, keeps R_FF (F2(ii), O_FF), and forces about 20 audited inputs to be redone.
- Optional: run the 2-adic odd-relation search (the f2sys/oddrel pipeline of ratio_graph_r_iv) on G to decide whether G is non-bipartite.
- For powers of ell in Proposition 5: study whether the divisor-rich labels {b >= D}, which are multiples of lcm's of smooth shape values, admit a relocation cheaper than Lambda^2 (a loophole of relocation_price_floor.md).

