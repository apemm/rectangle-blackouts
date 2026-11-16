# The exponent as a function of the relocation price

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: Theorem P. If a heavy diagonal costs h Lambda^bE and a Theorem D label costs Lambda^bD, the exponent is max(theta_E(bE), min(bE, bD/2)), where theta_E(b) is the root of x + phi(x) = b (and b itself for b <= ln3/2). With Theorem DC it is theta_E(bE). So theta_E(2) = 1.4967429, theta_E(1) is about 0.91, and exponent 1 needs bE = 1.135. Lemma K proves the fractional moment input for every a > 0. Conditional on the price hypothesis, which is open for every b < 2. Not audited yet.

# Result

## Status

proved

## Summary

Conditional on the price hypothesis, Theorem N's exponent has a closed form. With heavy price Lambda^bE and Theorem D price Lambda^bD, theta = max(theta_E(bE), min(bE, bD/2)), where theta_E(b) solves x + phi(x) = b (and theta_E(b) = b for b <= ln3/2). With Theorem DC the exponent is theta_E(bE). The fractional moment input is proved for every a > 0.

## Statements

NOTATION. Lambda = log h, ell = loglog h, E(a) = (1+3^a)/2.
- For x >= ln3/2: phi(x) = 1/2 - y + y ln(2y), with y = x/ln 3.
- For x < ln3/2: phi_+(x) = 0, and phi_+ = phi above that. phi_+ is continuous and nondecreasing.
- kappa_T = |D_T| (stride 4), and H_d(B) = #{T : kappa_T >= B}.
- x0 := ln3/2 = 0.5493061.

DEFINITION (the heavy-limited exponent theta_E). For 0 < b <= x0, theta_E(b) = b. For b > x0:
 theta_E(b) = min over a > 0 of (E(a) - 1 + b)/(1 + a) = (ln3/2) 3^(a*(b)).
Here a*(b) > 0 is the unique root of
 b = 1/2 + 3^a((1+a) ln3 - 1)/2.
Equivalently, theta_E(b) is the unique x >= x0 with x + phi(x) = b.
Properties:
- theta_E is increasing and concave, with theta_E(b) <= b, and equality exactly for b <= x0.
- Its slope is d theta_E/db = 1/(1 + a*(b)), which lies in (0.5226, 1] for b <= 2.
- theta_E(2) = theta* = 1.4967429 (a* = 0.9124154).
- theta_E(b) = 1 exactly at b = 1 + phi(1) = 1.1350845.

LEMMA K (fractional moments; PROVED from audited inputs: stride_menu Lemma 2 and heavy_light Lemma 3'). For every fixed a > 0 and every h >= 4,
 sum over odd T with 0 < |T| < h of kappa_T^a <= C_a h Lambda^(E(a)-1),
with no o(1) loss. Consequence (Markov): H_d(B/4) <= C_a 4^a h Lambda^(E(a)-1) B^(-a) for every fractional a in (0,1).
Sharpness (uses the sieve lower bound of heavy_diagonals_sharp Theorem 2, audited; its sieve citation still has no theorem number): the sum is at least h Lambda^(E(a)-1-o(1)).
The statement is not separately stated in heavy_light_split.md. It is the inequality displayed in the proof of Theorem 1(b) just before Markov's inequality, and the proof holds verbatim for a in (0,1). This closes the gap that independence_density_f.md lists ("did not re-check for fractional exponents").

HYPOTHESIS (Price; bE, bD in (0, 2]).
- (PE) For every set of Delta <= h diagonals sent to the Theorem E instance (Delta = h allowed, which is T1 at the new price), the instance can be built with all of Theorem N1 (a)-(f) as patched, at cost C(Delta h Lambda^bE ell^C + h^2 ell).
- (PD) Weighted Theorem D, under its hypotheses (i), (ii), (AP) and rho >= Lambda^(-C'), has cost C(rho kappa |D| h Lambda^bD ell^C + h^2 ell). Its exceptional set stays |E_D| <= 4 h^(2-eps_D), and N1 (a)-(f) still hold.
- Both prices must cover T2's higher-arity term sqrt(n Q A(w)) as well as the pair term.
- By relocation_price_floor Theorem R (audited, with its separation clause), any b < 2 needs a block outside class P, for example a sequential or conditional placement.

THEOREM P (CONDITIONAL on (H1)-(H4) of Theorem N v3 and on (PE), (PD)).
(a) Board L***U with the (B4) law and Bad_split:
 m_h <= C h^2 Lambda^(theta_B) ell^C, with theta_B(bE, bD) = max(theta_E(bE), min(bE, bD/2)).
 Parameters:
 - if theta_E(bE) >= bD/2: B = ceil(Lambda^theta_E(bE)) and a = a*(bE);
 - if theta_E(bE) < bD/2 <= bE: B = ceil(Lambda^(bD/2)), with the same a;
 - if bD/2 > bE: send every label to Theorem E (no light region).
(b) With Theorem DC in place of (B4)/(B8). This is ADDITIONALLY CONDITIONAL on Theorem DC (unaudited) and on its transfer from the v2 board to v3. For every eta > 0 and every bD <= 2,
 m_h <= C_eta h^2 Lambda^(max(theta_E(bE), eta)) ell^(C_eta).
 So the exponent is theta_E(bE), whatever bD is.
(c) Equal prices. theta_B(b, b) = theta_E(b) for every b in (0, 2]; in fact for every b <= 7.779. So at equal prices Bad_split never binds, and Theorem DC changes no exponent. DC lowers the exponent exactly when min(bE, bD/2) > theta_E(bE). Example: bD = 2 (Theorem D unchanged) and x0 < bE < 1.1350845. At bE = 1, bD = 2 the exponent is 1.0000 with Bad_split and 0.9101 with DC.
(d) Other terms. No other term of the width becomes binding for any b in (0, 2]. This covers the light width (exponent x, which is the balancing term), the Theorem D group overheads, n_rel, the Proposition partial windows, the junctions, buffers and collars, and the census remark (P1). Their exponents are 0 (times ell^C) or h^(-delta).
(e) Within this architecture (kappa-heaviness, light width proportional to B h^2, heavy cost h Lambda^bE per diagonal), theta_E(bE) cannot be improved by better counts of heavy diagonals. This follows from the matching lower bound in Theorem 2. It is a statement about the method, not a lower bound on m_h.

TABLE 1 (one price b = bE = bD; the exponent is the same with Bad_split and without it):
 b     | theta_E(b) | a*(b)    | B = Lambda^x, x =
 2.00  | 1.4967429  | 0.912415 | 1.49674
 1.90  | 1.4440055  | 0.879765 | 1.44401
 1.80  | 1.3903180  | 0.845277 | 1.39032
 1.75  | 1.3630894  | 0.827274 | 1.36309
 1.70  | 1.3355871  | 0.808721 | 1.33559
 1.60  | 1.2797026  | 0.769814 | 1.27970
 1.50  | 1.2225327  | 0.728213 | 1.22253
 1.40  | 1.1639172  | 0.683490 | 1.16392
 1.30  | 1.1036585  | 0.635101 | 1.10366
 1.25  | 1.0728375  | 0.609320 | 1.07284
 1.20  | 1.0415072  | 0.582342 | 1.04151
 1.10  | 0.9771413  | 0.524275 | 0.97714
 1.00  | 0.9101318  | 0.459610 | 0.91013
 0.90  | 0.8398844  | 0.386495 | 0.83988
 0.80  | 0.7655328  | 0.302123 | 0.76553
 0.70  | 0.6857201  | 0.201903 | 0.68572
 0.60  | 0.5980845  | 0.077440 | 0.59808
 <= 0.5493 | b      | (a -> 0) | everything goes to Theorem E
Inverse (the price that reaches a target exponent):
- theta = 1.40 needs b = 1.817897;
- theta = 1.25 needs b = 1.547748;
- theta = 1.00 needs b = 1.135085 (= 1 + phi(1));
- theta = 0.75 needs b = 0.779919.

TABLE 2 (two prices, with Bad_split, theta_B = max(theta_E(bE), min(bE, bD/2)); last column is DC, theta_E(bE)):
 bE \ bD  | 2.00   | 1.75   | 1.50   | 1.25   | 1.00   | 0.50   | DC
 2.00     | 1.4967 | 1.4967 | 1.4967 | 1.4967 | 1.4967 | 1.4967 | 1.4967
 1.75     | 1.3631 | 1.3631 | 1.3631 | 1.3631 | 1.3631 | 1.3631 | 1.3631
 1.50     | 1.2225 | 1.2225 | 1.2225 | 1.2225 | 1.2225 | 1.2225 | 1.2225
 1.25     | 1.0728 | 1.0728 | 1.0728 | 1.0728 | 1.0728 | 1.0728 | 1.0728
 1.1351   | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000
 1.00     | 1.0000 | 0.9101 | 0.9101 | 0.9101 | 0.9101 | 0.9101 | 0.9101
 0.75     | 0.7500 | 0.7500 | 0.7500 | 0.7264 | 0.7264 | 0.7264 | 0.7264
 0.55     | 0.5500 | 0.5500 | 0.5500 | 0.5500 | 0.5500 | 0.5500 | 0.5500
 0.40     | 0.4000 | 0.4000 | 0.4000 | 0.4000 | 0.4000 | 0.4000 | 0.4000
A cheaper Theorem D (bD < 2) with Theorem E unchanged (bE = 2) gives nothing: the exponent stays theta*.

REMARK T4 (independence_density_f Theorem 4 with prices; CONDITIONAL on its H(beta', gamma) and on its own hypotheses, unaudited). Its width line is linear in the two prices, so
 theta = inf over x of max{ x, bD - x, bD - x - gamma + Psi, bE - Phi((x+gamma)/beta') }.
Without Bad_split it is inf over x of max{ x, bE - Phi((x+gamma)/beta') }.
Values at bE = bD = b (grid step 0.0025, so each value is an upper approximation within about 0.003):

| Hypothesis | b = 2 | b = 1.5 | b = 1 |
|---|---|---|---|
| H(1, 0.5) | 1.2500 | 0.9975 | 0.7226 |
| H(1, 1), with Bad_split | 1.0000 | 0.7500 | 0.5000 (the bD/2 term binds) |
| H(0.5, 0), with / without Bad_split | 1.1725 / 0.9914 | 0.9335 / 0.8349 | 0.6835 / 0.6561 |

NOT PROVED: (PE) and (PD) for any b < 2. Nothing below theta* is proved, and m_h = O(h^2) is not proved. Even b -> 0 gives only h^2 Lambda^(o(1)) ell^C.

## Proofs

All note paths are in research_archive/2026-11-13 of the rectangle-blackouts repository unless a path says otherwise.

1. PROOF OF LEMMA K (fractional moments).
Inputs:
- stride_menu Lemma 2 (audited in audits_stride_menu_and_gamma.md);
- heavy_light Lemma 3' (audited in audit_heavy_light_split.md, "Lemma 3': as stated").
At stride 4 (sigma = 2, Delta = 5, tau(sigma^2) = tau(4) = 3), D_T as in stride_menu is the board's D_T. So kappa_T = k_T^(2), and Lemma 2 gives, for odd T with 0 < |T| < h,
 kappa_T <= 6 g(|T|)(1 + 2 log(3h/|T|)/log phi_g) <= C3 (1 + log(3h/|T|)) g(|T|).
Here:
- phi_g = (1+sqrt5)/2;
- C3 = 12/log phi_g = 24.94, because 2/log phi_g > 1 gives 1 + 2u/log phi_g <= (2/log phi_g)(1+u);
- g(n) = prod (2e+1) over p^e || n with p = +-1 (mod 5).
Fix a > 0. Put F_a := g^a. It is multiplicative, with:
- F_a(p^e) = (2e+1)^a for p = +-1 (mod 5);
- F_a(p^e) = 1 otherwise (p = 2, 5, and p = +-2 mod 5).
So 0 <= F_a(p^e) <= (2e+1)^a, which is the hypothesis of Lemma 3' for every a > 0, fractional or not.

I re-checked each step of Lemma 3' for a < 1:
- Phi(y) <= 3^a theta(y) + y^(1/2)(log_2 y)(2 log_2 y + 1)^a log y = O_a(y);
- the Euler tail sum_{e>=2}(2e+1)^a p^(-e) is at most C_a p^(-2);
- nothing uses a >= 1.

Prime sum. For p not 2 or 5, F_a(p) = (1+3^a)/2 + ((3^a-1)/2)(p/5). The Legendre symbol (p/5) is a nonprincipal character mod 5, so sum (p/5)/p converges. Hence sum_{p<=x} F_a(p)/p = E(a) loglog x + O_a(1), and Lemma 3' gives S_a(x) := sum_{n<=x} F_a(n) <= C_a x (log x)^(E(a)-1) for x >= 3. For x < 3, S_a is bounded.

Partial summation. Put w(t) = (1 + log(3h/t))^a, which decreases on [1, h]. Then
 sum_{t<h} w(t) F_a(t) = S_a(h) w(h) + int_1^h S_a(u)(-w'(u)) du, with -w'(u) = a(1 + log(3h/u))^(a-1)/u.
Since E(a) >= 1, (log u)^(E-1) <= (log h)^(E-1). Substituting u = h e^(-y), the integral is at most
 C_a a (log h)^(E-1) h int_0^inf (1 + log 3 + y)^(a-1) e^(-y) dy.
The integral is finite for every a > 0; for a < 1 the integrand is at most e^(-y). The boundary term is (1 + log 3)^a S_a(h). Summing over both signs of T:
 sum_T kappa_T^a <= 2 C3^a sum_{t<h} w(t) F_a(t) <= C_a h Lambda^(E(a)-1).
Markov's inequality then gives H_d(B/4) <= (4/B)^a sum_T kappa_T^a.

Lower bound. sum_T kappa_T^a >= Lambda^(a xi) H_d(Lambda^xi) >= h Lambda^(a xi - phi(xi) - o(1)) by Theorem 2. Take xi = (ln3/2) 3^a, so y = 3^a/2 and y ln(2y) = a y ln3. Then a xi - phi(xi) = y - 1/2 = E(a) - 1. []

2. THE WIDTH LINE AT GENERAL PRICES.
I go through consolidated_board_v3 Section 4 term by term, with B = ceil(Lambda^x).
- Light regions: t < 16 l B in every type, so the width is <= 5.453e6 B h^2. Exponent x. The price does not enter.
- Theorem E: Delta = H_d(B/4) <= C_a 4^a h Lambda^(E(a)-1) B^(-a) by Lemma K, for any fixed a > 0. Under (PE) the cost is C h^2 Lambda^(E(a)-1+bE-ax) ell^C + C h^2 ell. Taking the best fixed a, the exponent is bE - phi_+(x). This uses inf_{a>0}(E(a) - 1 - ax) = -phi_+(x): for x > x0 the infimum is at 3^a = 2y (heavy_diagonals_sharp Theorem 2, audited). For x <= x0 the function is convex with nonnegative slope at 0, so the infimum is 0, which is also the trivial bound Delta <= h.
- Theorem D (one group, rho = 2/B, |D| <= h, kappa finite): C h^2 Lambda^(bD - x) ell^C + C h^2 ell under (PD). Exponent bD - x.
- Collars and separations of the N1 blocks (O(1) blocks per instance and O(ell) class separations): O(h^2 ell). Buffers, margins and sea pieces: O(h^2). The switch and tails: O(h^2). Exponent 0. None of these depends on the price, since (PE) and (PD) keep the N1 layout.
- Proposition partial: n_rel = O(h^(2-eps_D) + h^(11/6) log h + h^(9/5+2eps)) (V3-4). Every item is bounded independently of B up to powers of Lambda, or over all chi:
 - the Theorem U averages A4, D8, B7, D17 and D18 have no factor B;
 - R-e is bounded over all label pairs;
 - E_D is a single group.
 So c0 n_rel tau*(h)^2 = h^(2 - min(eps_D, 1/6) + o(1)). This is o(h^2 Lambda^(-C)) for every C, and it never binds.
- The uncovered-slot and higher-height parts appear only in the variants (DC, Theorem 4). Their exponents are bD - 3 or bD - 7/3 + eps, which are negative for bD <= 2.
Total, with the light region nonempty:
 M <= C h^2 ell^C (Lambda^x + Lambda^(bE - phi_+(x)) + Lambda^(bD - x)) + O(h^2 ell) + o(h^2).
Option 2 (no light region: every label in S goes to Theorem E with Delta = h, and the rest to WP): M <= C h^2 Lambda^bE ell^C. This is T1 at price bE and uses (PE) at Delta = h.
The validity of the truncations and the passage from M to m_h are exactly as in Theorem N, since only the costs change. So m_h <= C h^2 Lambda^theta ell^C, with
 theta = min( bE, inf_{x>=0} max(x, f(x), g(x)) ), f(x) = bE - phi_+(x), g(x) = bD - x.

3. THE OPTIMISATION.
LEMMA O1 (the heavy crossing). x - f(x) is continuous and strictly increasing, equal to -bE < 0 at 0 and tending to infinity. So x = f(x) has a unique root x_f, and inf_x max(x, f(x)) = x_f:
- for x < x_f, f(x) >= f(x_f) = x_f;
- at x_f, the max equals x_f.
For bE <= x0: f(x) = bE on [0, x0] and f(x) < x0 beyond, so x_f = bE.
For bE > x0: x_f > x0 solves x + phi(x) = bE. Parametrise by a = log_3(2y), which is increasing in x, with y = x/ln3. Then x = (ln3/2)3^a, and x + phi(x) = y ln3 + 1/2 - y + y a ln3 = 1/2 + 3^a((1+a) ln3 - 1)/2 =: b(a). Here:
- b(0) = x0;
- b'(a) = (ln3)^2 3^a (1+a)/2 > 0;
so a*(bE) is unique.
Duality. inf_x max(x, inf_a (E(a) - 1 + bE - ax)) = inf_a inf_x max(x, E(a) - 1 + bE - ax) = inf_a (E(a) - 1 + bE)/(1+a). The order of the infima can be swapped because t -> max(x, t) is monotone and continuous. The critical-point equation E'(a)(1+a) = E(a) - 1 + bE is exactly bE = b(a), and the minimum value is E'(a*) = (ln3/2)3^(a*) = x_f. So x_f = theta_E(bE).
By the envelope theorem, theta_E' = 1/(1 + a*). It is 1 at a* = 0 and decreases as a* grows, so theta_E is concave and theta_E(b) <= b. At b = 2: 1/1.9124 = 0.5229.
LEMMA O2 (two decreasing terms). If f and g are nonincreasing with crossings x_f and x_g = bD/2, then inf_x max(x, f, g) = max(x_f, x_g):
- for x below max(x_f, x_g), the corresponding f or g is at least its crossing value;
- at x = max(x_f, x_g), both f and g are at most x.
With option 2: theta_B = min(bE, max(theta_E(bE), bD/2)). Since theta_E(bE) <= bE, this equals max(theta_E(bE), min(bE, bD/2)).
Parameters. In the case bD/2 > theta_E, keep a = a*(bE). The heavy exponent at x = bD/2 is theta_E(1 + a*) - a* x <= x.
This proves (a).

4. PROOF OF (b) (DC).
Theorem DC replaces (B4)/(B8). Its light width is B' = B + 9 Lambda^eta + 16 classes per (T, tau), so the width exponent is max(x, eta). Its deterministic set Y goes to one weighted Theorem D group with rho = 1 and kappa <= C_k (log H1)^(c_k) k^k Lambda^(-2) + C Lambda^(-7/3+7eps) (DC (c), using C(D, k) >= Lambda^2/k^k with k = ceil(2/eta) and log H1 = 7 ell). Under (PD) its cost is C h^2 (Lambda^(bD-2) ell^C + Lambda^(bD-7/3+7eps)) <= C h^2 ell^C for bD <= 2. For larger bD, raise k and H1. The heavy term is unchanged, with threshold kappa_T >= B, which changes only constants. Hence the exponent is max(theta_E(bE), eta), by Lemma O1 and option 2.

5. PROOF OF (c).
Put psi(y) = y ln3 - phi(y ln3) = y(ln3 + 1) - 1/2 - y ln(2y). Then:
- psi(1/2) = ln3/2 > 0;
- psi'(y) = ln3 - ln(2y), so psi increases up to y = 3/2 and then decreases;
- its root is y1 = 3.5403, that is x1 = 3.88952.
So phi(x) < x on [x0, x1). For b in (x0, 2], theta_E(b) <= theta* < x1, so b = theta_E + phi(theta_E) < 2 theta_E. For b <= x0, theta_E = b > b/2. In both cases min(b, b/2) = b/2 <= theta_E(b), so theta_B(b, b) = theta_E(b). The same argument works up to b = 2 x1 = 7.779.
DC helps exactly when min(bE, bD/2) > theta_E(bE). For bD = 2 this means theta_E(bE) < 1, that is bE < 1 + phi(1) = 1.1350845, together with bE > x0, since below x0 theta_E = bE.

6. PROOF OF (d) (other terms) is Section 2. On the census remark (P1): it bounds the size of a light class and does not enter M. Its proof needs only that two surviving labels of one class with |Delta i| <= 210 are impossible.
- Under (B4)/(B8) such a pair is a monochromatic R_FF^+ edge, which leaves the region by rule 3 or R-g.
- Under DC, (b) states that no class contains an in-class R_FF^+ edge (height q = 1 is below the cutoff).
So (P1) holds in both variants, at every price.

7. PROOF OF (e).
By Theorem 2 (audited), H_d(Lambda^xi) >= h Lambda^(-phi(xi) - o(1)) for xi > x0. Since H_d is monotone and phi is continuous with phi(x0) = 0, also H_d(Lambda^xi) >= h Lambda^(-o(1)) for xi <= x0. So if the heavy diagonals really cost of order h Lambda^bE each, the heavy term is h^2 Lambda^(bE - phi_+(x) - o(1)), and the minimum over x is theta_E(bE). This is a statement about the method only.

8. REMARK T4. In the M-bound of independence_density_f Theorem 4, each of the following is linear in its price:
- the light Bad_split term Lambda^2/W;
- the F-treatable Bad_split term (Lambda^2/(hW)) ell sum_F 1/alpha_T;
- the uncovered term Lambda^(-1);
- the H term (Lambda^2/h)|H|.
Replacing Lambda^2 by Lambda^bD in the first three and by Lambda^bE in the H term gives the displayed formula. Its Rankin step needs (1/h) sum kappa_T^a <= C_a Lambda^(E(a)-1) for a in [0, 6], including fractional a, and that is Lemma K (at a = 0 the sum is at most 2h). The values come from expo_thm4_price.py. At price 2 it reproduces the note's 1.4967, 1.172/0.991 and 1.25.

9. ON THE HEURISTIC LEVER.
The audit of Theorem R suggests that a sequential greedy placement prices the Lemma F family at about Lambda per label. Even if that is made rigorous, it gives bE = 1 only if T2's higher-arity term sqrt(n Q A(w)) (which costs Lambda^2) is also beaten. Then:
- with Theorem D unchanged (bD = 2), the exponent is 1.0000 with Bad_split and 0.9101 with DC;
- at bE = bD = 1 it is 0.9101 either way.
Near b = 2 each unit of price saved lowers the exponent by about 0.52.

## External results used

- Mertens' theorem in arithmetic progressions mod 5 (Dirichlet): the sum of 1/p over primes p = +-1 mod 5 up to x is (1/2) loglog x + O(1). Equivalently, sum (p/5)/p converges for the nonprincipal real character mod 5. Used in Lemma K.
- Repository inputs used as audited: stride_menu Lemma 2 (audits_stride_menu_and_gamma.md); heavy_light Lemma 3' and Theorem 1(b) (audit_heavy_light_split.md); heavy_diagonals_sharp Theorem 2 and Proposition 3 (audit_heavy_diagonals_sharp.md); relocation_price_floor Theorem R, for class P only (audit_relocation_price_floor.md).
- Repository inputs used as conditional and unaudited: Theorem N v3 with (H1)-(H4) (consolidated_board_v3.md); Theorem DC and Lemma M (degree_capped_colouring.md); Theorem 4 (independence_density_f.md).

## Checks

Analytic work first, then two short sanity scripts in scripts_exponent/. I ran each with py -I, one at a time; each took under 10 s.
- expo_beta.py:
 - closed form against grid: theta_E(2) = 1.496742913 at a* = 0.9124153, and the grid gives 1.49675;
 - Table 1 against a grid over x of max(x, b - phi_+(x)): agreement within 2e-5 at every row;
 - the crossing phi(x) = x is at x = 3.88952, that is b = 7.779;
 - the inverse prices 1.817897, 1.547748, 1.135085 and 0.779919.
- expo_two_prices.py: Table 2 from max(theta_E(bE), min(bE, bD/2)) against a grid minimum that includes option 2. The largest difference is 3.3e-5. 1 + phi(1) = 1.1350845.
- expo_thm4_price.py: reproduces independence_density_f's 1.4967 (beta' = 1, gamma = 0), 1.172/0.991 (beta' = 0.5) and 1.25 (gamma = 0.5) at price 2, then evaluates the priced formula.
- My Table 1 agrees with the grid values recomputed in audit_relocation_price_floor.md: 1.4968, 1.4440, 1.3903, 1.3631, 1.2797, 1.2226, 1.1639, 1.0415 and 0.9101.
- By hand: Lemma K line by line, including Lemma 3' for a in (0,1), the prime-sum identity and the partial-summation integral; Lemmas O1 and O2; the parametrisation b(a) and its monotonicity; the envelope slope; psi(y) and its root; and the DC kappa bound at general bD.
- Read in full: consolidated_board_v3.md, heavy_light_split.md and its audit, heavy_diagonals_sharp.md and its audit, degree_capped_colouring.md, independence_density_f.md, and stride_menu.md lines 120-159 (the definitions and Lemma 2).
- Searched audit_relocation_price_floor.md for the heuristic lever and its exponent table.
The repository was only read, I ran no git command, and I used no web sources.

## Gaps

- The price hypotheses (PE) and (PD) are unproved for every b < 2. Theorem R (audited, with its separation clause) excludes them for class-P blocks, so any b < 2 needs a sequential or conditional placement. That placement must also beat T2's higher-arity term sqrt(n Q A(w)) with A(w) = Lambda^4, not only the Lemma F pair term. (PE) is also needed at Delta = h (option 2) and must keep all the N1 claims (a)-(f) and an exceptional set of size h^(2-delta).
- Theorem P inherits every open item of Theorem N v3: (H1) completeness of the K2 and K4 lists; (H2a) the N1 patches [G12]-[G16], which nobody has re-read; (H2b) the steps V3-1 to V3-5, which are not audited; the T1 chain, which no single audit reads end to end; and a non-explicit h0.
- Part (b) uses Theorem DC (degree_capped_colouring.md), which is not audited. DC was written against the v2 board, with greedy classes and psi. I did not check its transfer to v3 (Theorem U in pointwise form, N1 as a single instance, K6-v3), its threshold kappa_T >= B in place of B/4, or the step 'weighted Theorem D accepts a deterministic Y with rho = 1'. The DC note itself flags that last step.
- The lower-bound half of Lemma K and the sharpness remark (e) rest on Theorem 2's sieve lower bound. That proof is audited, but the citation of the fundamental lemma still has no theorem number. The upper bound of Lemma K, which Theorem P uses, does not depend on it.
- The tables come from exact closed forms evaluated by bisection to about 1e-9. The grid cross-checks agree within 4e-5, and they are not certified by interval arithmetic. The Remark T4 values use a grid of step 0.0025, so each is an upper approximation within about 0.003.
- Remark T4 holds only on top of independence_density_f Theorem 4, which is unaudited and conditional on H(beta', gamma). The degree-scaled routing of Bad_split to a Theorem-E-type method (which would make the effective bD equal to min(bD, bE)) is only mentioned as a heuristic. It would need (H1') of heavy_light at price bE and a bound on the row degree of Bad_split, and I did not prove either.

## Missing estimate

Two estimates are missing.

(PE) is the binding one: a relocation block outside class P, built by sequential or conditional placement, that relocates the labels of Delta whole diagonals at cost C Delta h Lambda^bE ell^C with bE < 2. It must beat both the Lemma F pair term and T2's higher-arity term sqrt(n Q A(w)), and keep N1 (a)-(f). By Theorem P the exponent is then theta_E(bE), the root of x + phi(x) = bE. Values:
- bE = 1.817897 gives 1.4;
- bE = 1.547748 gives 1.25;
- bE = 1.135085 gives 1;
- bE = 1 gives 0.9101.

(PD) matters only when bD > 2 theta_E(bE). With Theorem DC (once it is audited and transferred to v3), (PD) is not needed at all.

## Next steps

- Attack (PE) at the Lemma F family with a sequential greedy placement inside one T1-type block. First make rigorous the audit heuristic that the excluded slot fraction is about 1 - e^(-lambda) when the earlier centres are well spread. Then check whether T2's higher-arity term (A(w) = Lambda^4) can also be priced below Lambda^2 under sequential placement; if it cannot, bE stays at 2 whatever happens to the pair term.
- Audit Theorem DC and write its transfer to v3 (Theorem U in pointwise form, N1 as a single instance, threshold kappa_T >= B). It changes the exponent only in the window x0 < bE < 1.1351 with bD = 2. It is still worth having, because it removes Bad_split from the hypothesis list.
- Have a second reader check Lemma K and Lemmas O1 and O2. They are about one page together and close the fractional-a gap that independence_density_f.md records.
- If a degree-scaled version of (PE) is ever proved (cost C Delta h Lambda^bE for any label set of row degree Delta), route Bad_split to it as well. That needs a Chernoff bound on the row degree of Bad_split, which is independent across T. The effective bD then becomes min(bD, bE), and the exponent is theta_E(bE) without DC.
- Do not spend effort on a cheaper Theorem D alone. With bE = 2 the exponent stays theta* = 1.4967429 for every bD <= 2 (Table 2, first row).

