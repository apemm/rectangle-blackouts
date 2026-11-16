# Power savings for the two M2c point counts

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: |E(Q)| << Q^(4/5+eps) for every Q and N_h << h^(9/5+eps). So cross-class M2c and label-filler M2c hit O(h^(9/5+eps)) labels. Not audited yet.

# Result

## Status

proved

## Summary

Both counts have a power saving. For every Q, |E(Q)| << Q^(4/5+eps), even without the (ii-a) congruences, and N_h << h^(9/5+eps). The proof is elementary: a new identity (kappa^2+mu^2) m'^2 = Q^2 + W^2, a p-adic lemma, a Pell-equation count and a Rankin sieve. Not audited yet.

## Statements

Notation. For an integer Q >= 3, let E0(Q) be the set of e with 1 <= e < Q/2 for which there are integers n1, X, Y >= 1 with XY = e^2 + n1^2 and n1(X + Y + 2n1) = e(Q - 2e). This is E(Q) of saw_residual_families.md (ii-b) without the congruences of (ii-a) or the slot condition, so E(Q) is a subset of E0(Q). N_h is the count of threshold_families_random_prime.md, Proposition 5. Its tuples (n1, w, e, u2) are M2c data, so Delta = e u2/n1 - w is an integer (a column difference; block_sea M2c also requires z = -e u2/n1 in Z).

THEOREM A (per-Q bound; proved, not audited). For every eps > 0 and every Q >= 3, |E0(Q)| <<_eps Q^(4/5+eps). The implied constant depends only on eps.

COROLLARY B (N_h; proved, not audited). N_h <<_eps h^(9/5+eps). This holds without the threshold |Delta| >= 78h and without the shallowness conditions: every M2c 4-tuple with e + u2 < h is counted.

COROLLARY C (consequences; conditional only on the upstream reductions, which are unaudited).
(1) Cross-class M2c, through Proposition 5 (in L* and in L*_l, every parity combination): the expected number of labels hit is O(N_h log h) = O(h^(9/5+eps)).
(2) Label-filler M2c, through (ii-b): the labels hit are at most (h/2) times the sum over the O(1) filler rows of |E(Q)|, which is O(h^(9/5+eps)).
Both families therefore hit O(h^(2-delta)) labels with delta = 1/5 - eps. The relocation rule moves them in width O(h^(9/5+eps) tau*(h)^2) = o(h^2 / Lambda^A) for every A. The strong form of the target holds, with no averaging over the filler row and no use of the congruences of (ii-a).

THEOREM D (secondary, independent cross-check; rests on Heath-Brown's theorem as stated in the journal abstract). N_h <<_eps h^(52/27+eps), by the determinant method on the projective cubic surface S: e w u2 = n1(e^2 + (n1+w)^2). The exponent is weaker than in Corollary B. Its value is that it confirms Corollary B by a completely different route.

## Proofs

0. SETUP AND WITNESS IDENTITIES

Fix Q and e in E0(Q), and fix one witness (n1, X, Y). Put:
- L = X + Y + 2n1;
- W = X - Y;
- m = Q - 2e >= 1.

LEMMA 1.
(a) n1 L = e m.
(b) W^2 = L^2 - 4e(Q - e).
(c) 4 n1^2 <= eQ.
(d) Write n1/e = mu/kappa in lowest terms (mu, kappa >= 1). Then mu | m, and with m' = m/mu,
 (kappa^2 + mu^2) m'^2 = Q^2 + W^2.

Proof.
(a) This is the second defining equation.
(b) L^2 - W^2 = 4XY + 4n1(X+Y) + 4n1^2 = 4(e^2+n1^2) + 4n1(L-2n1) + 4n1^2 = 4e^2 + 4n1 L. By (a) this equals 4e^2 + 4em = 4e(Q-e).
(c) From (b), L >= 2 sqrt(e(Q-e)). Then n1 = em/L <= sqrt(e) (Q-2e) / (2 sqrt(Q-e)) <= sqrt(eQ)/2.
(d) Multiply (b) by n1^2 and use 4e(Q-e) = Q^2 - m^2 (since e = (Q-m)/2). This gives (n1 W)^2 = e^2 m^2 - n1^2(Q^2 - m^2), that is m^2(e^2 + n1^2) = n1^2(Q^2 + W^2). Multiply by kappa^2/e^2 and use kappa n1/e = mu: m^2(kappa^2 + mu^2) = mu^2(Q^2 + W^2). Since gcd(mu, kappa^2 + mu^2) = gcd(mu, kappa^2) = 1, mu^2 | m^2, so mu | m. Dividing by mu^2 gives the identity.
From (c): mu = kappa n1/e <= (kappa/2) sqrt(Q/e). (*)
Conversely, e = (Q - mu m')/2 is determined by (mu, m').

1. THE p-ADIC LEMMA AND THE BOUND ON kappa

Write e = G e', where G is the part of e supported on the primes dividing 2Q and gcd(e', 2Q) = 1. Write e' = a b^2 with a squarefree.

LEMMA 2. Let p be an odd prime with p not dividing Q, and let alpha = v_p(e) be odd. Then v_p(n1) >= (alpha+1)/2. Consequently kappa | G b^2, so kappa <= G(e) b(e)^2.

Proof. Let beta = v_p(n1).
- Since p | e and p does not divide Q, p does not divide m or Q - e. By (a), v_p(L) = alpha - beta >= 0.
- p is odd, so v_p(4e(Q-e)) = alpha.
- In (b): if 2(alpha - beta) > alpha, then v_p(W^2) = alpha is odd, which is impossible (W = 0 would give 2(alpha - beta) = alpha). Equality 2(alpha - beta) = alpha is impossible because alpha is odd. So 2(alpha - beta) < alpha, that is beta > alpha/2.
For kappa = e/gcd(e, n1):
- p | 2Q: v_p(kappa) <= v_p(G).
- p not dividing 2Q, p | a (so alpha = 1 + 2 v_p(b)): v_p(kappa) = alpha - min(alpha, beta) <= (alpha-1)/2 = v_p(b).
- p not dividing 2Q, p not dividing a: v_p(kappa) <= alpha = 2 v_p(b).
So kappa divides G b^2.

2. A PELL COUNT

LEMMA 3. For integers D >= 2 and Q >= 1,
 #{(W, m') in Z^2 : W^2 - D m'^2 = -Q^2, |m'| <= Q} <<_eps Q^eps (1 + log D).

Proof.
(i) Removing common primes. If a prime p divides both Q and D, then p | W.
- If p^2 does not divide D, then p | m' (compare valuations), and (W/p, m'/p) solves the equation for (D, Q/p).
- If p^2 | D, then (W/p, m') solves it for (D/p^2, Q/p).
The case is decided by D alone, so this map is injective. Iterating reaches an equation W'^2 - D' m''^2 = -Q'^2 with gcd(D', Q') = 1, D' >= 1, Q' | Q and |m''| <= Q.
(ii) D' = delta^2 a square. Then (W' - delta m'')(W' + delta m'') = -Q'^2 gives at most 2 tau(Q'^2) solutions.
(iii) D' not a square. Put g = gcd(W', m''). Then g | Q', and dividing by g gives a primitive solution of norm N = -(Q'/g)^2.
- m''' is invertible mod |N|: a prime dividing both would divide W'''.
- So lambda = W''' m'''^(-1) mod |N| satisfies lambda^2 = D' (mod |N|) with gcd(D', N) = 1. There are at most 2^(omega(N)+2) such lambda.
- Two primitive solutions alpha_1, alpha_2 with the same lambda satisfy alpha_1 conj(alpha_2) = N beta, where beta is in Z[sqrt D'] with norm 1. So alpha_1 = beta alpha_2 with beta = +-eps0^j, where eps0 >= 1 + sqrt 2 is the fundamental norm-1 unit.
- In one class with |m'''| <= Q: |W'''| <= sqrt(D') Q, so |alpha| and |conj(alpha)| are at most R = 2 sqrt(D') Q, and |alpha conj(alpha)| >= 1. Hence j ranges over at most 1 + 2 log R / log(1 + sqrt 2) values.
Summing over g | Q' and over lambda gives <<_eps Q^eps log(DQ) <<_eps Q^(2 eps)(1 + log D). Rename eps.

3. A SIEVE COUNT

LEMMA 4. For 1 <= E <= Q and y >= 1: #{e <= 2E : G(e) b(e)^2 > y} <<_eps E Q^eps y^(-1/2).

Proof.
- G(e) b(e)^2 divides e, so the count is at most the sum over b and over G | (2Q)^infinity with G b^2 > y of 2E/(G b^2).
- Rankin: the sum over G > z of 1/G is at most z^(-1+eps) times the product over p | 2Q of (1 - p^(-eps))^(-1). That product is <<_eps Q^eps, because omega(Q) << log Q / log log Q.
- Terms with b^2 >= y: at most the sum over b >= sqrt(y) of (2E/b^2) times the product over p | 2Q of (1 - 1/p)^(-1), which is << E y^(-1/2) log log Q.
- Terms with b < sqrt(y): at most the sum over those b of (2E/b^2) Q^eps (b^2/y)^(1-eps), which is << E Q^eps y^(-1+eps) sqrt(y).

4. PROOF OF THEOREM A

Split (0, Q/2) into O(log Q) dyadic blocks (E, 2E]. If E < Q^(1/3), bound the block trivially by 2E. Otherwise put y = E^(3/5) Q^(-1/5) >= 1.
- B_y = the e in the block with G b^2 > y. By Lemma 4, |B_y| << E Q^eps y^(-1/2).
- A_y = the other e in E0(Q) in the block. Each has kappa <= y (Lemma 2) and mu <= y sqrt(Q/E) (by (*)). It also has a solution (W, m') of W^2 - D m'^2 = -Q^2 with D = kappa^2 + mu^2 <= 2 y^2 Q and 1 <= m' <= Q (Lemma 1(d)). The map e -> (kappa, mu, m') is injective, because e = (Q - mu m')/2. By Lemma 3, |A_y| <<_eps y^2 sqrt(Q/E) Q^(2 eps).
With this y both terms equal E^(7/10) Q^(1/10) Q^(2 eps), which is at most Q^(4/5 + 2 eps) since E <= Q/4. Summing over the blocks gives |E0(Q)| <<_eps Q^(4/5+eps).

5. PROOF OF COROLLARY B

Mirror. (n1, w) -> (-n1, -w) preserves the identity, e, u2 and |Delta|. So take n1 > 0.

The tuple gives a witness. The identity forces w > 0. Put X = Delta - 2n1 and Y = w. Then XY = (e u2/n1 - w - 2n1) w = e^2 + n1^2 (this is (I2)). So X is a positive integer, because Delta is an integer. Also n1(X + Y + 2n1) = e u2. So with Q = u2 + 2e <= 2h, (n1, X, Y) is a witness for e in E0(Q).

Recovering the tuple. The tuple is fixed by (Q, e, n1) and a choice w in {X, Y}:
- u2 = Q - 2e;
- L = e(Q-2e)/n1;
- W = +-sqrt(L^2 - 4e(Q-e)), which gives {X, Y};
- n1 | e(Q-2e), so n1 takes at most tau(e(Q-2e)) = h^(o(1)) values.

Hence N_h <= 4 h^(o(1)) times the sum over Q <= 2h of |E0(Q)|, which is <<_eps h^(9/5+eps).

6. PROOF OF COROLLARY C

Substitute Corollary B into Proposition 5 (E[labels] = O(N_h log h)). Substitute Theorem A into (ii-b) (labels hit <= (h/2) times the sum over filler rows of |E(Q)|, with E(Q) contained in E0(Q) and Q <= h). Then apply the relocation rule with tau*(h) = h^(o(1)).

7. PROOF OF THEOREM D (cross-check)

The ingredients:
- S is a cubic surface, and it is absolutely irreducible: it is linear in u2 with coprime coefficients e w and n1(e^2+s^2).
- N_h tuples have all coordinates below h. With n1 > 0 we have s t = e(e+u2) < e h and t = Delta - n1 >= 77h, so s < e/77 < h/77 and n1, w < s.
- N_h is at most the sum over lambda >= 1 of N1(S; h/lambda), where N1 counts primitive points that lie on no rational line.

Rational lines on S. I classified them by projecting from the double point (0:0:0:1). There are exactly five: {n1=e=0}, {n1=w=0}, {e=0, n1+w=0}, {n1=u2=0} and {n1+w=0, u2=-e}. Each lies in n1 w e (e+u2) = 0, so no N_h point lies on one.

Heath-Brown, Ann. of Math. 155 (2002): a projective surface in P^3 of degree d >= 3 has O(B^(52/27+eps)) rational points of height <= B off its rational lines. This gives h^(52/27+eps).

The same method applied to the cubic T: Y(s^2 + eP) = s(s^2 + e^2) gives only the average of |E(Q)| over Q <= x. Theorem A supersedes it.

8. STRUCTURE REMARK (explains the census)

The N_h identity is homogeneous of degree 3, and Delta/(e+u2) is scale invariant. So N_h is the sum over primitive shapes with Delta0/H0 > 78 of about h(1/H0 - 78/Delta0)_+ scaled copies. The h^2-like local growth of the census (N_h about 4.3e-7 h^2 for h <= 6e4) is the onset of shapes with ratio >= 78. For ratio thresholds 6 and 20 the primitive count grows with local exponent 1.45 and 1.6, and both are falling.

## External results used

- Heath-Brown, The density of rational points on curves and surfaces, Ann. of Math. 155 (2002) 553-598. A projective surface in P^3 of degree d >= 3 has O(B^(52/27+eps)) rational points of height <= B off its rational lines. Read from the journal abstract on the Oxford record https://ora.ox.ac.uk/objects/uuid:61776df1-3232-4fdc-87de-f3c01f6bce3f and arXiv math/0405392. Used only for the secondary Theorem D.
- Standard facts: the Pell unit group of Z[sqrt D] is +-eps0^Z with eps0 >= 1+sqrt 2; tau(n) and 2^omega(n) are n^(o(1)); the number of roots of lambda^2 = D mod N with gcd(D,N)=1 is at most 2^(omega(N)+2). Lemma 3 is proved from these in the text.

## Checks

All scripts are in scripts_point_counts/. They ran with py, one at a time, each under 60 s. The repository was not touched.
- eq_enum.py computes E0(Q) by brute force over divisors. It matches the note at Q = 1000, 1002 and 2002 (19, 6 and 39).
- check_identity.py checks 3015 witnesses (Q = 3001 to 3060, plus 1000, 1002, 2002, 4001, 8191, 9973, 10080, 20011 and 30030) against Lemma 1(a)-(d), 4n1^2 <= eQ, the p-adic lemma and kappa | G b^2. Result: 0 failures. The maximum of mu/(kappa sqrt(Q/e)) is 0.497, so bound (*) is tight.
- check_nh_to_eq.py takes all 168 positive-n1 N_h tuples at h = 20000 and finds each one as an E0(u2+2e) witness (0 missing).
- nh_enum.py and nh_stats.py: N_h^+ = 28, 168 and 695 at h = 1e4, 2e4 and 4e4, in line with the note's 190 at 2e4. 87% of the tuples have s | e.
- prim.py: primitive shapes by height. With ratio >= 78 there are 57, 279 and 1046 shapes up to height 1e4, 2e4 and 4e4 (onset). With ratio >= 6 the local exponent is about 1.45 and falling.
- eq_sizes.py: |E0(Q)| = 88, 123, 109, 14, 18 and 246 at Q = 30030, 55440, 60060, 65521, 99991 and 100800. Q^0.8 is between 3820 and 10064 there.

## Gaps

- Nothing here is audited. Audit these first: Lemma 1(d), the identity (kappa^2+mu^2)m'^2 = Q^2+W^2 and the step mu | m; Lemma 2, the p-adic step and kappa | G b^2; Lemma 3, the Pell count, which is standard but written out by me, including the reduction to gcd(D,Q)=1 and the class/unit argument; and the dyadic assembly in Section 4.
- Corollary C inherits every hypothesis of the upstream reductions, all unaudited: threshold_families_random_prime.md Proposition 5 (cross-class M2c reduces to N_h, with E = O(N_h log h)) and saw_residual_families.md (ii-b) (label-filler M2c reduces to E(Q), with labels hit <= (h/2) times the sum of |E(Q)|).
- Corollary B assumes that Delta (equivalently e u2/n1) is an integer for N_h tuples. That holds for M2c data (Delta is a column difference, and z = -e u2/n1 is in Z in block_sea Theorem 2), but N_h as literally written in Proposition 5 does not state it.
- Theorem D (exponent 52/27) rests on Heath-Brown's theorem as read from the journal abstract only. I did not open the paper to check the exact hypotheses or the 'not on a line' convention. Corollary B does not depend on it.
- The exponent 4/5 is not optimised. The census (|E(Q)| <= 246 for Q <= 1.01e5; prime Q give 2 to 18) suggests that the truth is Q^(o(1)) times a divisor-type factor.
- Theorem A bounds |E0(Q)| for every Q. It does not address the other (O2)/(O3) families: V3 between parked SLL triples, the R_FF ratio graphs of Fo/Fo and Fe/Fe, the colouring of R_IV, and the inhomogeneous or cross-block two-label quadruples.

## Missing estimate

None for these two counts. Both meet the strong target (power saving delta = 1/5 - eps): N_h << h^(9/5+eps), and the sum over the filler rows of |E(Q)| << h^(4/5+eps). The averaging over the filler row and the 2-adic congruences of (ii-a) are not needed.

## Next steps

- Audit Theorem A: Lemma 1(d), Lemma 2, Lemma 3 (Pell count with the gcd reduction) and the dyadic choice y = E^(3/5) Q^(-1/5). Then audit Corollary B, including the integrality of Delta and the mirror step.
- Audit the upstream reductions that Corollary C needs: Proposition 5 of threshold_families_random_prime.md and (ii-b) of saw_residual_families.md. Then record cross-class M2c and label-filler M2c as closed in the ledger, at O(h^(9/5+eps)) labels each.
- In threshold_families_random_prime.md, replace 'N_h <= h^(2-delta) OPEN' with Corollary B. In saw_residual_families.md, replace the missing estimate (1) with Theorem A; the T* averaging route is no longer needed.
- Optional: sharpen 4/5. The loss comes from counting all pairs (kappa, mu) in A_y; a bound showing that most Pell equations (kappa^2+mu^2) m'^2 - W^2 = Q^2 have no solution with m' <= Q/mu would lower it.
- Move on to the families that remain open: V3 between parked SLL triples, the colouring of R_IV, the R_FF ratio graphs, and the inhomogeneous or cross-block two-label quadruples.

