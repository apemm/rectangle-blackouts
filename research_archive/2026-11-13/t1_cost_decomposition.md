# Where the two logarithms of T1 come from

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: log^2 h in T1 comes from three separate sources, so the rigid layout does not inherit T1's analysis. (H1') holds for unions of diagonals, so Theorem 4 of heavy_light_split.md depends on (S) alone. Not audited yet.

# Result

## Status

partial

## Summary

In T1, the log^2 h does not come from label-label events alone. Pair events with the sea and the 3- and 4-label budget each carry it too, so the rigid layout does not inherit T1's analysis. I proved four things. Congruence choices kill all fatal two-label sea triangles and all non-horizontal two-sea supports R1 and R3 on rigid regions. Any rigid randomization acts on whole classes. A 2-adic dichotomy holds between stride classes. (H1') holds for unions of diagonals with an extra h^2 loglog h term, so Theorem 4 of heavy_light_split.md now depends on (S) alone.

## Statements

NOTATION. Q = floor(h^2/4), Lambda = 1 + log h, ell = 1 + loglog(3h). A label e has rows a (odd) and b (even), and f has rows c and d. S is a sea point with row s. v(e), C_w and M(w) = min(1, C Lambda/w, C Lambda^3/w^2) are as in T1 (two_moment_threshold_refinement.md, eqs (2) and (3)). G_{e,f} is as in T2 (safe_triangle_pair_first_moment.md, Section 4). "Stride 2 sigma" means columns 2 sigma (i + M_c) = 2 sigma (j - n_c), with M_c in pZ and n_c = kappa mod 2^nu, as in Proposition R of heavy_light_split.md.

LEMMA 1 (PROVED; elementary). Take two labels e and f in distinct columns 0 and X, and a mixed four-cell support with exactly one sea point S = (xi, s). For a fixed role and fixed rows there are at most 2 pairs (X, xi). This covers the roles (a,c|b,s), (a,c|d,s), (a,s|c,d), (a,s|b,c) and their e<->f mirrors (c,s|a,b), (c,s|a,d). Consequence: T2's divisor counts tau(|yz|) for these six table rows overcount. Each contributes O(1) per pair of labels.

THEOREM A (decomposition of T1's width; PROVED as an accounting of the audited T1/T2 bounds together with Lemma 1). T1's per-class pair budget is B(w) = Q ell^{C2}(Lambda^2 + w Lambda)M(w) + h^{1+o(1)}, eq. (4). It splits into the following parts.
 (i) Label-label, from vertical rivals tau((c-a)^2): Q Lambda^2 ell^C M(w).
 (ii) Label-sea, Lambda^2 type: two-sea supports (a,c|s,t) with tau(c-a) tau(c+a-s-t), and horizontal sea sides with a label-label diagonal, tau((c-a)^2). Together Q Lambda^2 ell^C M(w).
 (iii) Label-sea, w Lambda type. Triangles with the right angle at a label point, tau(c-a) tau(s-a) <= w tau(c-a). Two-sea supports (a,s|c,t) and (c,s|a,t). Together Q w Lambda ell^C M(w).
 (iv) O(n_w): lone-point triangles and the one-sea roles of Lemma 1.
After summation over the dyadic classes (T1 (5) to (7): sum M << ell, sum wM << Lambda ell), the parts (i), (ii) and (iii) each give Q Lambda^2 ell^{C+1}. The higher-arity budget (8), with A(w) = Lambda^4 ell^C + w Lambda^{3/2}, gives Q Lambda^2 ell^{C4}. The Lambda^2 there is the square root of Lambda^4 = sqrt(Lambda^8): Cauchy-Schwarz on the second moment of compatible_profile_threshold.md (5). The collars give O(h^2 Lambda/ell) and the exceptional labels O(h^2). So log^2 h appears in three independent places: label-label rivals, label-sea pair events, and the 3- and 4-label budget. Removing the label-label events, as the rigid layout does, leaves the other two in T1's accounting. The branch "label-label events alone carry log^2" of the route is false.

LEMMA AP (aligned T1 profiles; PROVED by inspection of filled_mod7_profile_cover.md Sections 3 to 6, NOT audited). Fix residues o (odd) and epsilon (even) mod 16 for the label endpoints of a region. There are T1 profiles L < F < H, with all of T1's properties (1), (2) and (6) to (10) and its collars, that also satisfy L = F = o + 2 (mod 4), F - L = 8 (mod 16) and H - L = epsilon - o + 4 (mod 8), hence H = epsilon + 2 (mod 4). Cost: larger candidate windows, H in [h - 1568, h] and F of order 10^5, with bulk rows in [2*10^5, h - 2*10^5]. The number of profiles and exceptional labels stays the same up to absolute constants.

ALIGNED RIGID REGION (AR). All labels of the region have odd endpoint = o and even endpoint = epsilon (mod 16). They are placed by Proposition R at stride 2 sigma with p > max(20h, (2 sigma^2 + 4)h) prime, ((sigma^2+1)/p) = -1, 2^nu >= K, and kappa = j0 (mod 8). Then all label columns are = 0 mod 16 sigma. With M_c = -i0 (mod 7) they are also = 0 mod 7, so T1's mod-7 sea applies. Every non-label column holds one sea point, in a row of {L,F,H} from Lemma AP. In Theorem B only the mod-4 alignment of the sea rows is used, and the columns of the sea points are arbitrary.

THEOREM B (two-label sea triangles; PROVED). Let A be a point of label e, C a point of label f (e != f), and S a sea point. Consider tilted right angles with corner set {A, C, S}.
 (B1) If 4 | sigma (for example stride 8), no such right angle exists. This uses neither the mod-7 sea nor any condition on the columns of the sea points.
 (B2) If sigma = 2 mod 4 and an odd prime q | sigma has q not dividing (y - s) for all label rows y and sea rows s of equal parity (for example stride 12 with a mod-3 alignment), the only survivors are "cross-EH". Cross-EH: A and C even points in different classes, S in row H, the right angle at A, Y = x_S - x_A odd, and sigma Dn Y = Dj (sigma Y + H - y_A). With T1's mod-7 sea every cross-EH triangle is parked: its white corner lies in a column whose only black point is in row H, and row(W) is even.
 (B3) Stride 4 (sigma = 2): the survivors are cross-EH, plus intra-class EH with Y = (y_A - H)/2. These exist only in mixed-residue families with chi_7(g) = 1, and all of them are parked.
 In every case T1's sea-rooted "allowed triangles" and their six-cell collisions disappear from AR regions. Fatal two-label sea triangles are absent in every case.

PROPOSITION D (two-sea supports and the 2-adic dichotomy; PROVED).
 (a) Let label columns be = 0 mod 16 and label rows fixed mod 16 per parity, and let the sea rows be as in Lemma AP. Then no mixed support of type R1 (side = two label points of e and f, diagonal = two sea points) or R3 (side = two sea points, diagonal = two label points) exists unless the sea pair is horizontal. Any column layout qualifies, rigid or not.
 (b) If v2(sigma) <= 1, two label points of different classes and equal parity are never at integral distance in an AR region. So horizontal R1 and R3 are also impossible, and R1 and R3 are dead.
 (c) If 4 | sigma, horizontal R1 is still impossible (2-adic perpendicularity). Even-even integral distances escape every 2-adic and mod-p argument used here: for sigma = 4, 16t^2 + (4k)^2 = (2(k^2+1))^2 with t = (k^2-1)/2, and Dn = 4k - t = 0 mod 2^nu is solvable because 17 is a 2-adic square. So horizontal R3 survives when its two sea points are F fillers (needs 7 | xi).
 (d) Dichotomy: cross-EH triangles die exactly when v2(sigma) >= 2, and even-even integral distances die when v2(sigma) <= 1. No sigma lets both 2-adic arguments apply.

PROPOSITION C (rigid randomization acts on classes; PROVED). In a Proposition R layout, every obstruction spans at most W_h ~ h^2/4 columns. So two classes can interact only when they sit in the same or adjacent periods, at a block distance D that is fixed by their diagonals' residues. Any randomization that keeps the rigid rule acts only through period indices. A class's local-lemma budget is therefore the number of partner classes whose fixed offset carries an event for some pair in c x c', and that number is at most the sum of the per-label counts over the up to n_T labels of c. So T1's per-label first-moment step cannot pay for a surviving two-label sea family at width O(B h^2) unless the family's per-label count is O(B/h). Surviving families must be killed deterministically.

THEOREM E ((H1'') for unions of diagonals; PROVED modulo T1/T2's audited estimates re-indexed per diagonal, NOT audited). Let H be any set of diagonals, Delta = |H| (the row degree), and S the non-exceptional labels on diagonals in H. Then S, with T1's profiles, separations, collars and constant row-h tails, has an obstruction-free strip configuration of width at most C (Delta h Lambda^2 ell^{C1} + h^2 ell). For H = all diagonals this is T1. Heavy_light's (H1') as literally stated (no additive term) is not given by this method when Delta < h ell/Lambda^2. The h^2 ell term is enough for every use below.

COROLLARY F (CONDITIONAL on (S), on the unaudited inputs of heavy_light_split.md, and on Theorem E). Theorem 4 of heavy_light_split.md holds with (H1') replaced by Theorem E: m_h <= C h^2 (log h)^{theta_F} (loglog h)^{C1}, for example theta = 1.369 with the menu {2,4,8,12,20}.

REMARK G (payoff check). Hypothesis: chi(G_T^sigma(h)) <= C0 (1 + w_sigma(T))^c. Take B = C0 (1 + 3 loglog h)^c. Then the number of B-heavy diagonals is << h (log h)^{-2.875}; this step is PROVED, by Rankin with z = 6 and Lemma 3' of heavy_light_split.md. The label scaffold then has width O(h^2 (loglog h)^c), as the orchestrator stated. By Theorem E and (S), m_h = O(h^2 (loglog h)^{max(c, C1)}). This uses the coarse weight groups of Theorem E. With T1's dyadic classes alone the collar term would be h^2 log h/loglog h, and that term would dominate.

## Proofs

0. INPUTS QUOTED. T1, two_moment_threshold_refinement.md: (3) n_w <= C Q M(w); (4) sum_{f in C_w\{e}} G_{e,f} << Q ell^{C2} (Lambda^2 + w Lambda) M(w) + h^{1+o(1)} =: B(w); (5) sum_w M(w) << ell; (7) sum_w w M(w) << Lambda ell and sum_w B(w) << Q Lambda^2 ell^{C2+1}; (8) N_w << B(w) + sqrt(n_w Q) sqrt(A(w)) + n_w + 1 with A(w) = Lambda^4 ell^{C3} + w Lambda^{3/2}; (9) sum sqrt(n_w) << sqrt(Q ell); (10) sum sqrt(w n_w) << sqrt(Q Lambda) ell. T2, safe_triangle_pair_first_moment.md: (7), Henriot's one-variable weighted moments, uniform in constant terms O(h): sum_t tau(C)^s tau(A^2) << h Lambda^{beta(s)+2} ell^{C_s}, sum_t tau(C)^s tau(A) tau(B) << h Lambda^{beta(s)+2} ell^{C_s}, and sum_t tau(C)^s tau(A) << h Lambda^{beta(s)+1} ell^{C_s} for distinct forms; (9) 1_{C_w}(f) <= C w^{-s} sum_{r in f, t in S} tau(|r-t|)^s; the role table of Section 4; (14) and (16). compatible_profile_threshold.md (5): sum_{J ∋ e, |J| = k} G_J^2 <= C Q^{k-1} (Lambda^8 ell^C + v(e)^2 Lambda^3), proved from sharper_polylogarithmic_threshold.md (2), which is uniform in the constant terms of the forms on any box.

1. LEMMA 1. Put e at column 0 (rows a, b), f at column X != 0 (rows c, d) and S = (xi, s), with xi not in {0, X}. Write (N) for |B-A|^2 = |D-C|^2 and (P) for (B-A).(C+D-A-B) = 0.
(a,c|b,s): (P) gives X(xi - X) + yz = 0 with y = c - a and z = b + s - a - c, so xi = X - yz/X. Then (N) gives X^2 (y^2 + 2yz - (s-b)^2) = y^2 z^2. If the bracket is nonzero, X^2 is fixed, so there are at most 2 values of X and one xi for each. If the bracket is 0, then yz = 0. y = 0 forces xi = X, which puts S in f's column; z = 0 also forces xi = X.
(a,c|d,s): (P) gives X xi + yz = 0 with z = d + s - a - c. (N) gives X^2 (y^2 - 2yz - (s-d)^2) = y^2 z^2. The degenerate cases force xi = 0.
(a,s|c,d): (N) gives xi^2 = (d-c)^2 - (s-a)^2, so there are at most 2 values of xi, and (P), xi(2X - xi) + (s-a)(c+d-a-s) = 0, then fixes X.
(a,s|b,c): (P) gives xi(X - xi) + k = 0 with k = (s-a)(b+c-a-s). (N) gives xi^2 ((s-a)^2 + 2k - (c-b)^2) = k^2. k = 0 forces X = xi.
The mirror roles follow by exchanging e and f. Numerical check (lemma1_check2.py): 48 genuine supports, generated geometrically in all four patterns, each have exactly 2 solutions, a mirror pair, on a grid with |X|, |xi| <= 300.

2. THEOREM A. Go through T2's role table using Lemma 1. Rows (a,c|b,s) and (a,c|d,s) are Lambda^2 rows in T2 but O(1) here. Rows (a,s|c,d), (a,s|b,c), (c,s|a,b) and (c,s|a,d) are w Lambda rows in T2 but O(1) here. The surviving divisor-type rows are exactly those listed in (i) to (iii); their factors and estimates are T2's own (Section 4, the vertical-rival paragraph, the horizontal-side paragraph, and table rows 1, 5 and 8). Summation uses T1 (5) to (7). Part (iii) gives Q ell^C Lambda sum_w w M(w) << Q Lambda^2 ell^{C+1}, because each label's private weight averages Lambda: sum_e v(e) << Q Lambda, by T1 (2). The higher-arity term and the collars are T1 (11) and Section 3. These are statements about T1's bounds, that is, about the method. I prove no lower bounds, apart from T11's rival lower bound, which is quoted.

3. LEMMA AP. The proof in filled_mod7_profile_cover.md uses only the residues mod 7 (1), the parities (2), the square filters (7), (8) and (10), the margins (9) and (6), and the Section 6 collars. My additional conditions are congruences mod 16. They are compatible with (1) and (2) by CRT; for example L = o + 2 mod 4 is odd. Each condition shrinks the candidate sets by a bounded factor. Choose H among the at least 28 candidates in [h - 56*28, h] with the right class mod 56; each j <= L - 1 <= 27 excludes at most one candidate, as in T1. Then M = h - H <= 1568. Choose F among more than 1568 candidates of the right class mod 112 in a window of length about 1.8*10^5 starting at 4000. For fixed j, two bad values of F are separated by more than 2 sqrt((h - 2*10^5)/1568), which exceeds that window length for large h. The margins (9) and (6) and the outer-margin checks of Section 4 hold for bulk rows in [2*10^5, h - 2*10^5], with T1's argument unchanged. The exceptional rows (10) remain O(sqrt h) for each of the boundedly many profiles. The mixed-support, triangle and rival arguments of Sections 2 to 6 use no other property of L, F and H. I checked this by reading those sections, not by an audit.

4. THEOREM B. Basic facts. (F1) In AR, X = x_C - x_A = 0 mod 16 for any two label points. (F2) Every label point of label (i,j) has x = 2 sigma i (mod p). (F3) Points in different classes have |X| > 2 sigma (p - h) > 38 sigma h. Points of the same class have X = 2 sigma Di and Dy = 2 Di when both are odd or both are even. (F4) Every sea row s satisfies v2(s - y) = 0 if s and y have opposite parity, and v2(s - y) = 1 if they have equal parity. Here y is any label row; this is the alignment.
Vertex at S. Put alpha = x_A - x_S and gamma = x_C - x_S, so alpha - gamma = 0 mod 16 and alpha gamma = -Pi with Pi = (y_A - s)(y_C - s).
 (1a) A and C of opposite parity: by (F4), v2(Pi) = 1, so alpha - gamma is odd. Contradiction.
 (1b) Equal parity, s of the other parity: Pi = (y_A - s)^2 = 1 mod 8, because y_A = y_C mod 16. alpha and gamma are odd with alpha = gamma mod 8, so alpha gamma = 1 mod 8, but alpha gamma = -Pi = 7 mod 8. Contradiction.
 (1c) Equal parity, s of the same parity: Pi = 4 Pi' with Pi' = 1 mod 4. v2(alpha) = v2(gamma) = 1, since otherwise alpha - gamma is not = 0 mod 4. Write alpha = 2 alpha' and gamma = 2 gamma' with alpha' = gamma' mod 8, so alpha' gamma' = 1 mod 4. But alpha' gamma' = -Pi' = 3 mod 4. Contradiction.
Vertex at A (the vertex at C is symmetric). S = A + (Y, s - y_A) with Y != 0 and XY = -(y_C - y_A)(s - y_A).
 (2a) Opposite parity: y_C - y_A is odd, so v2(s - y_A) >= v2(X) >= 4. This contradicts (F4).
 (2b) Both odd, different classes: by (F2), X = sigma (y_C - y_A) (mod p). If y_C = y_A, then S lies in A's column, which is impossible. So p | (sigma Y + s - y_A). Since |sigma Y| <= sigma h^2/|X| < h/38, we get |sigma Y + s - y_A| < p, so sigma Y = y_A - s. Then (X - sigma(y_C - y_A)) Y = 0. Since |X| > sigma h, this forces Y = 0. Contradiction.
 (2c) Both even, different classes: X = 2 sigma (Dj - Dn) and Dy = 2 Dj, with Dj != 0, Dn != 0 and 2^nu | Dn. The equation becomes sigma Dn Y = Dj (sigma Y + m) with m = s - y_A and v2(m) <= 1. If v2(sigma Y) != v2(m), then v2(Dj) = v2(sigma) + v2(Dn) + v2(Y) - min(v2(sigma Y), v2(m)) >= nu + 1 > log2 K, which is impossible because |Dj| < K. For 4 | sigma we always have v2(sigma Y) >= 2 > v2(m): (B1). For v2(sigma) = 1 equality needs Y odd and v2(m) = 1, that is s = H: these are the cross-EH triangles of (B2) and (B3).
 (2d) Same class, same parity: Y = (y_A - s)/sigma. For 4 | sigma, y_A - s is odd or = 2 mod 4, so Y is not an integer. For sigma = 2 mod 4 with q | sigma, q does not divide y_A - s, so again no Y. For sigma = 2, Y = (y_A - s)/2 needs s of the same parity. T1's mod-7 sea then kills s = L (Y = 0 mod 7, a filler or label column) and s = F (Y = 2g mod 7, nonzero). For s = H, Y = 2g (mixed-residue) or 3g (zero-residue) mod 7 is an H column iff chi(2g) = 1 or chi(3g) = 1. In zero-residue blocks g is free, so choose chi(g) = 1 there.
Parking: W = C + (Y, H - y_A). Its column is = Y (mod 7), the residue of S's column, so it is an H column. row(W) = y_C + H - y_A is even, the parity of H. So W is parked.
Numerical check (thmB_check.py, thmB_random.py; the toy has no mod-7 pattern, the sea points may sit in any non-label column, and every row in {L,F,H} is tested). Rigid h = 160 and 200, stride 4: only intra-class Y = (y_A - s)/2 triangles occur (those of 2d), and none at stride 8. Random columns = 0 mod 4: exactly the predicted survivors (same-parity vertex triangles, and sea-vertex triangles of case 1c only). Random columns = 0 mod 8: same-parity vertex triangles only. A misaligned control (H = epsilon mod 4) produces mixed-parity and sea-vertex triangles.

5. PROPOSITION D. (a) R1 and R3 both require |P1P2|^2 = xi^2 + Ds^2. Row-sum parity forces the sea pair to have the parity pattern of the label pair.
 Same-parity labels: X^2 + Dy^2 = 0 mod 256. The sea pair is {L, F}, since {H, H} is horizontal, so Ds = +-(F - L) = 8 phi with phi odd. Then xi = 8 xi' and xi'^2 + phi^2 = 0 mod 4, which is impossible.
 Mixed-parity labels: both Dy and Ds are odd, so xi^2 = Dy^2 - Ds^2 (mod 16) forces xi = 0 mod 4 and Dy = +-Ds (mod 8). But Dy = +-(epsilon - o) and Ds is in +-{H - L, H - F} = +-{epsilon - o + 4} (mod 8), using F = L mod 8. These classes differ, so this is impossible as well.
 (b) Even-even, different classes: |P1P2|^2 = 4 Dj^2 (sigma^2 u^2 + 1) with u = 1 - Dn/Dj, a 2-adic unit because v2(Dn) >= nu > v2(Dj). The bracket is = 2 mod 8 when sigma is odd and = 5 mod 8 when sigma = 2 mod 4, so it is not a 2-adic square. Odd-odd: |P1P2|^2 = (sigma^2 + 1)(y2 - y1)^2 mod p, which is a nonsquare because ((sigma^2+1)/p) = -1. Same class: 4 Di^2 (sigma^2 + 1) is never a square.
 (c) Horizontal R1: n2 = s - (y1 + y2)/2 has v2 <= 1, and perpendicularity gives n1 = -n2 Dy/X with v2(n1) = v2(n2) - v2(sigma) - 1 + ... < 0 when 4 | sigma. The identity in the statement is checked directly.
 (d) Combine (b), (c) and step 2c.
Checks (r13_check.py, r13_control.py): random columns = 0 mod 16 at h = 400 with aligned rows give 0 R1 and 0 R3 events (6 horizontal R3 events, as allowed). A misaligned control gives 18 R1 and 2 R3 events. Rigid layouts at h = 200 and 640 show no integral cross-class distances; at these sizes 2 sigma p is too close to h^2 for the test to say anything about stride 8.

6. PROPOSITION C. Block distances are D = r(c') - r(c) + 2^nu (k' - k), where the residue r is a function of the diagonal. An event needs 2 sigma p |D| <= W_h, so |D| < h/(160 sigma) < 2^nu, which forces |k' - k| <= 1. The rest follows from the union bound over the pairs in c x c'.

7. THEOREM E. Work within one profile, as in T1. Any label of S on diagonal T is f_{T,i} with rows 2i+1 and 2i+T+1, both affine in i. Within a profile the admissible i form a progression mod 7, also affine.
 (E1) Class sizes. By the one-form moments of T2 (7) with s = 1, 2, uniform in T: |S ∩ C_w ∩ diag T| << h M(w), so n_w << Delta h M(w).
 (E2) Pairs, for weight w <= Lambda^3, dyadic classes. For e in S ∩ C_w, sum over f in S ∩ C_w of G_{e,f}. By Theorem A and Lemma 1, every role that is not O(1) has a geometric factor in one endpoint of f only. For each T in H the sum over i is one of T2 (7) with forms affine in i. The class forms 2i+1-t and 2i+T+1-t come from T2 (9). The bounds are uniform in T, so the minimum over s in {0,1,2} gives h ell^C (Lambda^2 + w Lambda) M(w) per diagonal. Form coincidences, such as T = t - a, occur on O(1) diagonals per e. There I bound the sum by sum_i (sum_k tau(C_k)) tau(A) << h Lambda^3, without the class restriction. T2's slice exceptions cost h^{1+o(1)}. One-sea roles and lone-point triangles cost O(n_w). Total: B_S(w) << ell^C Delta h (Lambda^2 + w Lambda) M(w) + h Lambda^3 + h^{1+o(1)}. Note: if I had kept T2's tau bound for the rows (a,c|d,s) and (c,s|a,d), the factor c + a - d - s = a - s +- T would be constant on each diagonal, and the sum over T in H would not average. Lemma 1 removes this problem.
 (E3) Higher arity. For J ⊆ S and k = 3, 4: sum_J G_J^2 << (Delta h)^{k-1} (Lambda^8 ell^C + v(e)^2 Lambda^3). This is the proof of compatible_profile_threshold.md (5) with each other label parametrized by (T, i). For k >= 3 both forms remain nonconstant on the box, because an f contributing both endpoints puts +-T_f plus another label's row into the row-sum factor. Then sharper_polylogarithmic_threshold.md (2) applies uniformly. Six-cell events: (15) stays a nontrivial linear equation in the i's, which gives (Delta h)^{k-1} h^{-1+o(1)}. Cauchy-Schwarz gives (n Delta h)^{(k-1)/2} (Lambda^4 ell^C + v(e) Lambda^{3/2}). This step is checked by inspection only.
 (E4) Local lemma as in T2 (17), with N_w = C0 (B_S(w) + sqrt(n_w Delta h) A(w)^{1/2} + n_w + 1). Summing with T1 (5), (7), (9) and (10) at Delta h in place of Q gives << Delta h Lambda^2 ell^{C1}.
 (E5) Weights above Lambda^3, coarse groups. Take G = (W, W^{4/3}] with W >= Lambda^3. Use 1_G(f) <= (v(f)/W)^2 and v(e) <= W^{4/3}. The same per-diagonal estimates with s = 2 give a pair budget << ell^C Delta h (Lambda^5/W^2 + Lambda^4 W^{-2/3}) << ell^C Delta h Lambda^{1+1} (note 4 - 2/3*3 = 2). The bound n_G << Delta h Lambda^3/W^2 makes the higher-arity terms sqrt(n_G Delta h) v^{1/2} Lambda^{3/4} and sqrt(n_G Delta h) v^{1/3} Lambda^{1/2} at most Delta h Lambda^{9/4} W^{-1/3} << Delta h Lambda^{5/4}. Since v <= 1 + 6 tau*(h) = exp(O(log h/loglog h)), there are O(ell) groups, and O(ell) dyadic classes below Lambda^3. So the configuration has O(ell) blocks, each needing a separation of 2W_h = O(h^2) of periodic sea. Plain periodic sea of length 2W_h between blocks of one profile suffices, by the 2W_h+1 locality of sec5. Total: Delta h Lambda^2 ell^{C1} + h^2 ell. The profile collars and constant tails are T1's. The exceptional labels are placed once by the positional lemma at O(h^2).

8. COROLLARY F. Repeat proof [7] of heavy_light_split.md with Theorem E at Delta = H_d(B) <= C h Lambda^{E-1} B^{-a}. The heavy region costs h^2 Lambda^{theta} ell^{C1} + h^2 ell.

9. REMARK G. Use f(n) = z^{omega_split(n)}, with sum_{p split, p <= x} 1/p = (1/2) loglog x + O(1). Lemma 3' gives sum_{T<h} z^{w(T)} << h (log h)^{(z-1)/2}. So #{T < h : w(T) >= 3 loglog h} << h (log h)^{(z-1)/2 - 3 ln z}, which is h (log h)^{-2.875} at z = 6. Under the hypothesis these are the only B-heavy diagonals. Lemma P then costs 816 H_d h (1 + ln h)^2 = o(h^2), the light region costs O(B h^2), and Theorem E gives O(h^2 ell^{C1}).

## External results used

- Henriot, Nair-Tenenbaum bounds uniform with respect to the discriminant, Corollary 2, with the 2014 erratum. Used only as quoted in T2 (7) and in sharper_polylogarithmic_threshold.md (2), with uniformity in the constant terms.
- Lovasz local lemma (product form), as used in T2 Section 7.
- Wigert's bound log tau*(h) << log h/loglog h, which bounds the number of weight classes.
- Rankin's trick, plus Mertens for split primes (density 1/2 by Dirichlet), for Remark G.
- Paper locality 2W_h+1 (sec5_threshold.tex), Lemma mixedeq, and the criterion (V1)-(V5) of block_sea_classification.md.

## Checks

All scripts are in the matching scripts_ folder of this directory. Each ran with py, one at a time, in under 60 s (one first attempt timed out and was rerun smaller). The repository was not touched.
- lemma1_check2.py: 48 geometric one-sea supports (12 for each pattern) all have exactly 2 solutions (X, xi) on a grid with |X|, |xi| <= 300.
- thmB_check.py: rigid h = 160 and 200. Stride 4 shows only intra-class Y = (y_A - s)/2 triangles; stride 8 shows none.
- thmB_random.py: shuffled block order and random columns = 0 mod 4 or 0 mod 8 give exactly the predicted survivor types. A misaligned-H control shows the killed types (mixed-parity triangles and sea-vertex triangles).
- r13_check.py and r13_control.py: R1 and R3 are absent with aligned rows (6 horizontal R3 events) and present when misaligned (18 R1 and 2 R3).
- dichotomy_check.py and dichotomy_np.py: no cross-class integral distances at h = 200 and 640 for strides 4, 8 and 12. This is vacuous for stride 8 at these heights.
These runs are sanity checks only, not proofs.

## Gaps

- (S) remains open. These families are not killed on AR regions: (i) R2 two-sea supports (side = label point + sea point, diagonal = label point + sea point), which I did not analyze; (ii) the one-sea supports of Lemma 1, which are O(1) per pair but deterministic in a rigid layout and so must be zero; (iii) the label-only mixed quadruples I.2 and II of mixed_quadruples_blocks.md; (iv) events with three or more labels and a sea point; (v) V3 collisions among parked cross-EH triangles when sigma = 2 mod 4, or horizontal R3 with F fillers when 4 | sigma (Proposition D(d)); (vi) intra-class mixed supports with sea points.
- Lemma AP modifies an audited construction. I checked its proof by reading Sections 3 to 6, not by an independent audit.
- Theorem E step (E3), the per-diagonal re-indexing of the squared estimate (5) and of the six-cell bound, was checked by inspection only. The coarse-group step (E5) is new and has not been audited.
- Theorem B and Proposition D rely on Proposition R of heavy_light_split.md and on the rigid-note reductions, which are unaudited. The proofs here are elementary and were re-read only by me.
- Proposition D(c) shows only that the 2-adic and mod-p arguments used here do not apply. It is not a proof that horizontal R3 with F fillers occurs in an actual AR layout. Numerics at feasible h cannot test stride 8, because 2 sigma p is close to h^2.
- Theorem A is an accounting of T1's upper bounds. It does not prove that the label-sea first moment is of order Lambda^2 per label under random placement, except for rivals (T11).
- Corollary F and Remark G are conditional on (S), on the unaudited heavy_light inputs (Proposition R, Lemma P, Theorems 1 and 3), and for Remark G on the orbit chromatic hypothesis.

## Missing estimate

To finish (S) on aligned rigid regions, one needs deterministic kills, or O(1) repairs per class, for these families: R2 two-sea supports, the one-sea supports of Lemma 1, the label-only I.2 and II types, and events with three labels and a sea point. One also needs to handle one of two residual families. At stride 8, that is horizontal R3 with F fillers: even-even cross-class integral distances |P1P2| = xi in 56Z, with F fillers at columns (x1 + x2 +- xi)/2. At stride 12 (with mod-3 alignment), that is V3 collisions among parked cross-EH triangles, governed by sigma Dn Y = Dj (sigma Y + H - y_A) with Y odd. By Proposition C, T1's probabilistic step cannot pay for any of them.

## Next steps

- Audit Lemma 1 and Theorem B. Both are short and elementary.
- Audit Theorem E, especially (E3) and the coarse-group step (E5). If they pass, add a ledger row: 'T1 for unions of Delta diagonals: width C(Delta h log^2 h (loglog h)^C + h^2 loglog h)'. This makes heavy_light Theorem 4 conditional on (S) only.
- Carry the 2-adic analysis of Theorem B and Proposition D over to R2. Unknowns alpha = x_S1 - x_P1 and beta = x_S2 - x_P2, with alpha^2 - beta^2 = r2^2 - r1^2 and alpha(X - alpha + beta) = -r1(r2 - r1 + 2Dy). Then do the six one-sea roles of Lemma 1, using the closed forms for X^2.
- At stride 8, test whether the rigid rule plus a choice of the empty-slot rows (fillers at slot columns = 0 mod 112) can remove horizontal R3 with F fillers. This first needs a check that T1's one-label proofs allow H fillers at some zero columns. At stride 12, count V3 collisions among cross-EH triangles exactly.
- Check the mixed quadruples I.2 and II against AR conditions; the mod-16 column and row congruences may give new 2-adic kills.
- Lemma AP needs a short audit and a re-run of verify_filled_mod7_profiles.py with the mod-16 conditions added.

