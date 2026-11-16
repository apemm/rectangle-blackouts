# The 2-adic distribution of the distance sets (Eq)

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: Theorem A. For Q = 2^a, the sum over T of |D_T in QZ| is of order (h/Q) ln(sqrt(h)/Q), uniformly in Q, by an elementary count with no Hecke input. This proves the first moment of (Eq), and its tail with phi(x) weakened to x - 1, and it explains the h = 6000 data. The higher moments of (Eq) are false as stated for b > 1 and large Q (Proposition C). Route L needs only what is proved: under (Pc) and (Bal) its exponent is 5/4 with Bad_split and 1 without. Not audited yet.

# Result

## Status

partial

## Summary

Part (i) of (Eq), the first moment, is proved with an elementary argument that works for every power of 2 below sqrt(h)/2, with no Hecke or Siegel-Walfisz input. Part (ii), the Q^(-b) moment bound, is false for every b > 1 once Q >= Lambda^((3^b-3)/(2(b-1))+eps). Part (iii) is proved only with phi(x) weakened to x - 1, which follows from Markov's inequality. That is enough for Route L: assuming (Pc) and (Bal), the exponent is 5/4 with Bad_split and 1 without it, against 1.24932 / 1 under the full (Eq). So (Eq) can be dropped from Route L's hypotheses. The h = 6000 data come from a finite-h truncation factor ln(sqrt(h)/Q)/ln(sqrt h), not from a different 2-adic law.

## Statements

NOTATION. Stride 4, as in heavy_diagonals_sharp.md: D_T = {|d| : 16d^2 + (2d+T)^2 = L^2, 0 < L < h, d != 0, |d| < n_T} for odd T. Here w_T(Q) = |D_T ∩ QZ| with Q = 2^a, Lambda = ln h, E(b) = (1+3^b)/2, and phi(x) = max_a [a x - E(a) + 1], which is the phi of the note (y = x/ln3, phi = 1/2 - y + y ln 2y). g(n) = product of (2e+1) over p^e || n with p = +-1 mod 5.

THEOREM A (the 2-adic first moment; PROVED, elementary, uniform in Q). For h >= 2 and every Q = 2^a >= 1:
(a) If 2Q >= sqrt(h), then D_T ∩ QZ is empty for every T.
(b) If 2Q < sqrt(h), then sum_T w_T(Q) <= (2 pi h/Q)(1 + ln(sqrt(h)/(2Q))).
    Hence Q sum_T |D_T ∩ QZ| <= pi h (ln h + 2) for every Q. This is (Eq)(i), with C = pi(1 + 2/ln h), and it needs no restriction Q <= Lambda^C.
(c) Lower bound: if Q <= sqrt(h/60), put K = floor(sqrt(h/(60 Q^2))). Then sum_T w_T(Q) >= (h/(60Q)) sum_{k<=K} phi_E(k)/k^2 >= (h/(10 pi^2 Q))(ln K - C0), where phi_E is Euler's function and C0 is absolute.
So the true 2-adic law is sum_T |D_T ∩ QZ| ≍ (h/Q) ln(sqrt(h)/(cQ)), uniformly in Q. The fraction of distances divisible by Q is Q^(-1) times a factor of order ln(sqrt(h)/Q)/ln(sqrt h). This factor tends to 1 for Q <= Lambda^C. It explains the data: 0.416, 0.164, 0.060, 0.020, 0.005 at h = 6000.

COROLLARY B (tail; PROVED). For all Q = 2^a and M > 0, #{T : |D_T ∩ QZ| >= M} <= (2 pi h/(QM))(1 + ln(sqrt(h)/(2Q))) <= pi h (ln h + 2)/(QM).
- In exponents, with QM = Lambda^x, the count is <= h Lambda^(-(x-1)+o(1)).
- Since phi(x) >= x - E(1) + 1 = x - 1, this is (Eq)(iii) with phi(x) replaced by x - 1.
- The loss phi(x) - (x - 1) is 0 at x = (3/2) ln 3 = 1.648, and 0.0028 at x = 1.75, which is where Route L uses it.

PROPOSITION C ((Eq)(ii) is false as stated; PROVED). Fix b > 1, and let Q = Lambda^q <= h^(1/6).
- Then sum_T w_T(Q)^b >= sum_T w_T(Q) >= c h Lambda/Q.
- So the bound sum_T w_T^b << Q^(-b) h Lambda^(E(b)-1+o(1)) fails whenever q > (3^b - 3)/(2(b-1)).
- The thresholds are 1.657 (b = 1.01), 1.694 (b = 1.05), 1.843 (b = 1.2), 2.196 (b = 1.5) and 3 (b = 2).
- As b -> 1+, the threshold tends to (3/2) ln 3 = 1.648. So for any C > 1.648, (ii) fails in the range Q <= Lambda^C for every b in (1, b_C), where b_C > 1.
- CONJECTURED corrected form (ii*), NOT PROVED: for fixed b >= 1, sum_T w_T^b = h (Q^(-b) Lambda^(E(b)-1) + Q^(-1) Lambda) Lambda^(o(1)).

LEMMA D (pointwise structure; PROVED, using the audited dictionary of Lemma 1 and the Pisano period of 2^k).
- For Q = 2^a >= 2 and an ideal J of norm T^2 (T odd) with admissible generators beta_j = phi^(2j) beta_+, the j with Q | d(beta_j) lie in at most 2 residue classes mod 3Q/2.
- Hence |D_T ∩ QZ| <= 2 g(|T|)(1 + 2 ln(sqrt5 h/|T|)/(3Q ln phi)), and the left side is 0 when |T| >= sqrt5 h/2.

THEOREM E (Route L exponent; CONDITIONAL on (Pc), (Bal) and the inputs of Theorem N, with (Eq) replaced by Theorem A and Corollary B).
- With Bad_split, m_h <= C h^2 (log h)^(5/4) (loglog h)^C. The parameters are Q = Lambda^(1/2), B0 = Lambda^(3/4) and heavy threshold B1 = Lambda^(5/4); there are at most 4 pi h(ln h+2)/(Q B1) = O(h Lambda^(-3/4)) heavy diagonals.
- Without Bad_split, the exponent is 1 (q = b1 = 1, b0 = 0).
- The full (iii) would give 1.24932 and 1. So (Eq) costs at most 0.0007 in this exponent and is no longer needed as a hypothesis of Route L.

## Proofs

0. SETUP: Pythagorean parametrization (no Z[phi] needed).
- Let (T, d) be a pair with T odd, d != 0 and L^2 = 16d^2 + (2d+T)^2, 0 < L < h. Put A = 4|d| and B = |2d+T|.
- B is odd (T is odd), so B >= 1, and (A, B, L) is a Pythagorean triple with even leg A.
- Its gcd G is odd, because B is odd. By Euclid's parametrization, A = 2Gmn, B = G(m^2 - n^2) and L = G(m^2 + n^2), with m > n >= 1 coprime and of opposite parity. These are unique.
- Conversely, (T, d) is recovered from (G, m, n) and the two signs e1 = sgn d and e2 = sgn(2d+T): d = e1 Gmn/2 and T = e2 G(m^2 - n^2) - 2d.
- So (T, d) -> (G, m, n, e1, e2) is injective.
- 2-adic condition: Q | d iff 4Q | 2Gmn iff 2Q | Gmn iff 2Q | mn, because G is odd and Q is a power of 2. Since m and n have opposite parity, this means the even one of m, n is divisible by 2Q.

1. PROOF OF THEOREM A.
(a) If Q | d, the even one of m, n is at least 2Q, so L >= m^2 + n^2 > 4Q^2. Since L < h, this forces 2Q < sqrt(h).
(b) Every element x of D_T ∩ QZ equals |d| for an admissible d with Q | d (the condition |d| < n_T is dropped).
- So sum_T w_T(Q) <= #{(T,d)} <= 4 #{(G,m,n) : G odd, G(m^2+n^2) < h, 2Q | mn}.
- For fixed (m, n) with m^2 + n^2 < h, the number of odd G < y = h/(m^2+n^2) is <= (y+1)/2 <= y, since y > 1. Hence the count is <= h S, where S = sum 1/(m^2+n^2) over m, n >= 1 with m^2 + n^2 < h and 2Q | m or 2Q | n.
- In S, write the multiple of 2Q as 2Qk with 2Qk < sqrt(h), let the other coordinate j >= 1 be free, and use sum_{j>=1} 1/(j^2 + c^2) <= int_0^inf dx/(x^2+c^2) = pi/(2c).
- This gives S <= 2 sum_{k <= sqrt(h)/(2Q)} pi/(4Qk) <= (pi/(2Q))(1 + ln(sqrt(h)/(2Q))).
- Therefore sum_T w_T(Q) <= 4 h S <= (2 pi h/Q)(1 + ln(sqrt(h)/(2Q))) <= (pi h/Q)(ln h + 2).
(c) Family. Take n = 2Qk with k >= 1, m in (n, 2n) with gcd(m, n) = 1 (so m is odd), G odd with G n^2 < h/5. Put d = Gmn/2 = GmQk > 0 and T = G(m^2 - n^2 - mn).
- T is odd. 2d + T = G(m^2 - n^2) > 0, and L = G(m^2 + n^2) < 5Gn^2 < h.
- On (n, 2n), m^2 - mn - n^2 increases from -n^2 to n^2, so |T| <= Gn^2 < h/5. Also d < Gn^2 < h/5.
- From the label set, n_T = K_h - (T-1)/2 for T > 0 and n_T = A_h - (|T|+1)/2 for T < 0. So n_T >= (h - |T| - 1)/2 > 0.4h - 1/2 > h/5 > d.
- Hence d is in D_T ∩ QZ. The signs are fixed (d > 0, 2d+T > 0), so distinct (G, m, n) give distinct pairs (T, x = d).
- Count:
  - #{m} = phi_E(n), and phi_E(2Qk) >= phi_E(2Q) phi_E(k) = Q phi_E(k).
  - #{odd G < y} >= (y-1)/2 >= y/3 when y = h/(20Q^2k^2) >= 3, which holds for k <= K = floor(sqrt(h/(60Q^2))).
  - So the count is >= sum_{k<=K} (h/(60Q^2k^2)) Q phi_E(k) = (h/(60Q)) sum_{k<=K} phi_E(k)/k^2.
- The standard estimate sum_{k<=K} phi_E(k)/k^2 = (6/pi^2) ln K + O(1) (partial summation from sum_{n<=x} phi_E(n) = 3x^2/pi^2 + O(x log x)) finishes the proof. []

2. PROOF OF COROLLARY B. Markov's inequality applied to Theorem A(b): #{T : w_T >= M} <= M^(-1) sum_T w_T. For the comparison with (iii), take a = 1 in the Legendre form of phi, which gives phi(x) >= x - 1. []

3. PROOF OF PROPOSITION C. Each w_T is a non-negative integer, so w_T^b >= w_T for b >= 1.
- By Theorem A(c), with Q <= h^(1/6), we have ln K >= (1/3 - o(1)) Lambda, so sum_T w_T^b >= c h Lambda/Q.
- If (ii) held with an o(1) uniform in Q <= Lambda^C, then Lambda^(1-q) <= Lambda^(-bq + (3^b-1)/2 + o(1)), that is, q(b-1) <= (3^b-3)/2 + o(1).
- The function (3^b-3)/(2(b-1)) is increasing on b > 1, with limit (3/2) ln 3 at b = 1+.
- Heuristic behind (ii*): the g(T) ideals of one T each give 0 or 1 good generator in a short window, with probability about (window)/Q. So the moment has a main part (kappa_T/Q)^b on rich diagonals plus a first-moment part. []

4. PROOF OF LEMMA D. Use the dictionary of Lemma 1 (audited): every d in D_T comes from a unique beta = (X + L sqrt5)/2 in O = Z[phi], with N(beta) = -T^2, beta > 0, X = 10d + T and L < h, and beta is one of the beta_j = phi^(2j) beta_+ of the ideal J = (beta). The proof has four steps.
- Step 1: Q | d iff X = T (mod 2^k) with k = a+1, because 10 | X - T already.
- Step 2: the good generators.
  - beta satisfies beta^2 - X beta - T^2 = 0. So y = beta/T (T is odd, hence invertible mod 2^k) satisfies y^2 - y - 1 = (y - phi)(y - phi') = 0 in O/2^k O whenever X = T (mod 2^k).
  - O/2^k O is a local ring with maximal ideal 2O, because 2 is inert. The difference (y - phi') - (y - phi) = sqrt5 is a unit, so one factor is a unit and the other is 0 mod 2^k.
  - So y = phi or y = phi' (mod 2^k). Conversely, either congruence gives Tr beta = T (mod 2^k).
- Step 3: the residue classes.
  - With u = beta_+/T, the condition reads phi^(2j) u = phi or phi^(2j) u = phi' (mod 2^k).
  - The order of phi in (O/2^k)^* is the Pisano period 3 * 2^(k-1), because phi^n = F_n phi + F_(n-1) (Wall 1960; checked by script for k <= 11).
  - So each congruence holds for j in at most one class mod ord(phi^2) = 3 * 2^(k-2) = 3Q/2.
- Step 4: the window.
  - The admissible j satisfy |t_0 + 2j log phi| < arccosh R with R = sqrt5 h/(2|T|), so N_J <= 1 + arccosh(R)/log phi.
  - A residue class mod P = 3Q/2 meets at most 1 + (N_J - 1)/P of them, and arccosh R <= ln(sqrt5 h/|T|).
  - Summing over the g(|T|) ideals of norm T^2 (T odd: split p^e gives 2e+1 ideals, inert primes and 5 give 1 each) gives the bound. []
Remark (route to the exact (iii), NOT used):
- J/T = product over split p | T of (pi_p/pi_p')^(c_p), with |c_p| <= e_p. The good class of J is therefore fixed by theta_J = sum_p c_p theta_p, where theta_p is a point on a circle of length 3Q log phi (residue mod 2^(a+1) together with angle, modulo units).
- So w_T is a sum, over a product set, of a window function evaluated at sum_p c_p theta_p.
- Expanding the window function in characters of that circle turns w_T into a combination of multiplicative functions lambda_chi(T) = product over p of S_e(chi(theta_p)) (Hecke Grössencharacters of Q(sqrt5) of 2-power conductor), as the target suggested.
- Integer moments would follow from mean values of the products lambda_chi1 ... lambda_chib. The real moment of order about 1.05 that the exact phi needs does not follow this way. I did not carry this out.

5. PROOF OF THEOREM E (substitution into heavy_diagonals_sharp.md section 7, whose arithmetic I took as written).
- Heavy pieces: w_T >= B1/4. By Corollary B there are at most 4 pi h(ln h+2)/(Q B1) = h Lambda^(1-q-b1) of them, at h Lambda^2 ell^C each (Theorem E blocks), so the heavy term is h^2 Lambda^(3-q-b1).
- The width term's first moment Q sum_T 4 w_T <= 4 pi h(ln h + 2) is Theorem A(b).
- The exponent is max(q+b0, b1, 1, 3-q-b1, 2-b0). From b0 >= 2-E, q <= 2E-2 and b1 <= E, we get 3 - (2E-2) - E <= E, so E >= 5/4. Equality holds at q = 1/2, b0 = 3/4, b1 = 5/4. A grid search (expo.py) agrees: 1.25 at (0.5, 0.75, 1.25).
- Without Bad_split, b0 = 0 and the exponent is max(q, b1, 1, 3-q-b1) = 1 at q = b1 = 1.
- With the exact phi: 2 - phi(3E-2) = E gives 1.249322, and 2 - phi(2E) = E gives 0.9904, which is below the floor of 1. []

CHECKS (scripts in scripts_eq/; each ran with py in under 12 s).
- dyadic.py builds D_T from (G, m, n). It matches a brute-force construction exactly at h = 60, 201 and 500. It reproduces the note's fractions at h = 6000: 0.4157, 0.1640, 0.0597, 0.0197, 0.0046, 0.
- Fraction of distances divisible by Q, against the fit Q^(-1) ln(sqrt h/Q)/ln sqrt h. The fit is in brackets; the line also gives max_T w_T:

  | h | Q = 2 | Q = 4 | Q = 8 | Q = 16 | Q = 32 | Q = 64 | max_T w_T for Q = 1, 2, 4, 8, 16 |
  |---|---|---|---|---|---|---|---|
  | 20000 | 0.4266 [0.4300] | 0.1751 [0.1800] | 0.0683 [0.0725] | 0.0247 [0.0275] | 0.0073 [0.0094] | 0.0015 [0.0025] | not recorded |
  | 200000 | 0.4413 [0.4432] | 0.1904 [0.1932] | 0.0800 [0.0824] | 0.0323 [0.0341] | 0.0122 [0.0135] | not recorded | not recorded |
  | 10^6 | 0.4486 [0.4498] | 0.1978 [0.1998] | 0.0856 [0.0874] | 0.0361 [0.0374] | 0.0147 [0.0156] | 0.0057 [0.0062] | 161, 80, 42, 20, 10 |

  The approach to 2^(-a) as h grows, and the about kappa/Q scaling of the maximum, both match Theorem A and the heuristic for (ii*).
- Theorem A(b): Q sum/(pi h(ln h+2)) stays between 0.006 and 0.074 for all Q tested. A(a): the sets are empty exactly when 2Q >= sqrt h (Q = 64 at h = 6000; Q = 128 at h = 20000).
- pointwise.py: the Lemma D bound had 0 violations at h = 6000 and 200000 for Q = 2..128, with largest ratio 0.413. The Pisano period 3 * 2^(k-1) holds for k <= 11, and phi^n is never -1 mod 4. The Markov tail held with a large margin, for example 7654 <= 557871 at h = 200000, Q = 2, M = 8.
- expo.py: 1.249322 and 0.99042 under the exact (iii); 1.25 under Markov; the thresholds of Proposition C.

## External results used

- Euclid's parametrization of Pythagorean triples: (2mn, m^2-n^2, m^2+n^2) times a common factor, with m > n coprime and of opposite parity, unique for a given triple.
- sum_{n<=x} phi_E(n) = 3x^2/pi^2 + O(x log x) (Apostol, Introduction to Analytic Number Theory, Ch. 3; theorem number not checked), giving sum_{k<=K} phi_E(k)/k^2 = (6/pi^2) ln K + O(1) by partial summation.
- Pisano period: the period of the Fibonacci numbers mod 2^k is 3*2^(k-1) (D. D. Wall, Fibonacci series modulo m, Amer. Math. Monthly 67 (1960)); checked by script for k <= 11. Used only in Lemma D.
- Arithmetic of Z[phi] and the generator dictionary of heavy_diagonals_sharp.md Lemma 1 (audited): 2 inert, units +-phi^n, admissible generators phi^(2j) beta_+, window cosh t < sqrt5 h/(2T). Used only in Lemma D.
- Route L arithmetic of heavy_diagonals_sharp.md section 7 (unaudited, conditional), used as written apart from the substituted heavy-count and first-moment inputs.

## Gaps

- Nothing here has been audited. Theorem A, Corollary B and Proposition C are short and elementary and should be audited first. Lemma D is needed only for the structural remark.
- (Eq)(iii) in its exact form (phi(x) rather than x - 1) is NOT proved. It needs a real moment of order about 1.05 of w_T, which needs equidistribution of the ideal angles theta_p on the circle of length 3Q log phi with control of concentrated diagonals. It is worth only 1.25 -> 1.24932 in Route L. Heuristically it is true, because diagonals whose split primes all have theta_p near 0 are super-polynomially rare in Lambda.
- (Eq)(ii) is disproved only for b > 1 and Q >= Lambda^((3^b-3)/(2(b-1))+eps). For Q below that threshold (Route L uses q = 1/2), and for b < 1, (ii) is open. The corrected form (ii*) is a conjecture.
- Theorem E is conditional on (Pc), (Bal) and every input of Theorem N, all untouched here. I took the width and Bad_split arithmetic of Route L (heavy_diagonals_sharp.md section 7, which its audit did not cover) as written, and changed only the heavy-count term and the first-moment input.
- Theorem A(c) uses the standard estimate sum_{k<=K} phi_E(k)/k^2 = (6/pi^2) ln K + O(1) (partial summation from sum_{n<=x} phi_E(n) = 3x^2/pi^2 + O(x log x), Apostol's textbook; theorem number not checked). Lemma D cites Wall (1960) for the Pisano period of 2^k, checked by script for k <= 11.
- No Siegel-Walfisz-type theorem for Hecke characters is used or cited. Theorem A is uniform in Q by elementary counting, so the target's request to cite one exactly does not apply. I did not verify any such statement in a source.
- Theorem A's constant (2 pi) is about 14 times the truth. Only the shape (h/Q) ln(sqrt h/(cQ)) matters for the exponents.

## Missing estimate

(Eq) is no longer a hypothesis of Route L. The first moment is proved, and the tail it needs follows from Markov's inequality. That gives exponent 5/4 with Bad_split and 1 without it, assuming (Pc) and (Bal). The only arithmetic left on this route is the exact tail #{T : |D_T ∩ QZ| >= M} <= h Lambda^(-phi(log_Lambda(QM)) + o(1)). It is worth 0.0007 (5/4 -> 1.24932) and needs a moment of order about 1.05 of w_T, through equidistribution of ideal angles mod 2^(a+1) in Q(sqrt5). The real bottlenecks of Route L are now (Bal) and (Pc).

## Next steps

- Audit Theorem A(a)-(c), Corollary B and Proposition C. Each is under a page and uses only Euclid's parametrization.
- If they pass, restate Route L in heavy_diagonals_sharp.md as exponent 5/4 (with Bad_split) and 1 (without it), conditional on (Pc) and (Bal) only, and drop (Eq) from its hypotheses. Replace the moment form (ii) by (ii*), and record that (ii) is false for b > 1 when Q >= Lambda^((3^b-3)/(2(b-1))+eps).
- Record the 2-adic law: the fraction of distances divisible by Q is Q^(-1) times a factor of order ln(sqrt h/Q)/ln sqrt h. The faster-than-2^(-a) decay at h = 6000 is this truncation factor; the data at h = 10^6 are within 3 percent of the fit.
- Attack (Bal). Theorem A gives the exact average load (Q B0 + 4 pi (ln h + 2)/... per diagonal). Look for a deterministic or derandomised choice of the layer constants kappa_rho, so that the maximum load is within a constant factor of the average and the Chernoff factor Lambda/ell disappears.
- Attack (Pc) family by family: Lemma L-adic (i)(ii), Proposition 1(c),(d), J4, and the A4/B7 first moments, for class pairs in different i-residues mod Q.
- Optional and low value: prove the exact tail (iii) by real-exponent moments of sum_J nu(theta_J), using the circle structure of Lemma D's remark. This gains only 0.0007.

