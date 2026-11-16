# Congruence-restricted slot lists do not lower the price

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (obstruction, two independent derivations): restricting each label's slot list to the residue classes x = s1 a (mod p1), x = s2 b (mod p2), with s^2 + 1 a nonresidue, kills every same-parity integral distance whose row gap is prime to p, but the Lemma F weight stays of order Lambda^2. Two effects cancel the 1/p saving: shorter lists make each surviving event Q = p1 p2 times as likely, and given p | y, a constant fraction of the allowed offsets are p-multiples of Pythagorean triples. Theorem RL extends the floor of Theorem R to any independent label-dependent slot laws. Not audited yet.

# Derivation 1

## Status

obstruction

## Summary

The new idea fails. Restricting slot lists to residue classes keeps the Lemma F weight at c Lambda^2 per label: Theorem R carries over to every label-dependent residue rule mod Q (the nonresidue choice included), so this construction cannot give (PE) with bE < 2.

## Statements

NOTATION. Lambda = log h. A label e has an odd row a_e and an even row b_e. In a Theorem E instance the label f_{T,i} has a = 2i+1 and b = 2i+T+1. For a parity pi, rho_pi(e) is e's pi-row.

DEFINITION (class P_res(Q)). Take the amended class P of audit_relocation_price_floor.md: a block of W columns, slots in one residue class mod m, slot index j in [0, N) with N = W/m, the c'h^2 separation clause, and one fixed sea row s0 on every empty slot, where s0 is not a label row. The certificate is any criterion that uses only (P(A), the shared-label dependency graph) and is sound for every probability space with those data, or alteration with deletion budget equal to the first moment. Change one rule: each label e gets a list L_e = {j in [0, N) : j = psi(e) mod Q}, for an integer Q >= 1 and an arbitrary map psi : Z -> Z/Q. The map psi may depend on the rows, the diagonal or anything else. Each centre j_e is uniform on L_e, independently over the labels.
- The NEW IDEA is the case Q = p1 p2 with psi(e) = 7^{-1} s1 a_e mod p1 and psi(e) = 7^{-1} s2 b_e mod p2, on top of the slots x = 7j.
- Any further CRT residue that T2 needs is also covered: replace Q by Q Q'.

THEOREM RQ (PROVED). Fix a parity pi. Define:
- M0^Q = the maximum, over rows rho and residues c, of #{e : rho_pi(e) = rho, psi(e) = c}. Note M0^Q <= M0.
- R1 = W/(2h).
- R2_Q = |Z| / (m Q M0^Q Lambda^3).
Assume N >= max(40Q, 2h/m) and R1, R2_Q >= C0. Then:
(a) The average over e in Z of the sum of P(A), over the two-label Lemma F events A that contain e, is at least
 c |Z| ln(R2_Q) ln(min(R1, R2_Q^(1/3))) / W.
(b) Every certificate of class P_res(Q) needs every incident sum < 1, so
 W > c |Z| ln(R2_Q) ln(min(R1, R2_Q^(1/3))).
(c) Suppose every class Z_c = psi^{-1}(c) has |Z_c| <= N/(5Q). Then in the random placement, E[# fatal Lemma F pairs, with all labels present] >= (c/2) |Z|^2 ln(R2_Q) ln(min(R1, R2_Q^(1/3))) / W.
The constants c, C0 are absolute. The bound is Theorem R with R2 replaced by R2_Q, and it needs no hypothesis on Q (coprimality included) beyond N >= 40Q.

COROLLARY RQ1 (PROVED, using the Theorem E / T1 block facts that audit_relocation_price_floor.md already checked against T2 Section 7). Take a Theorem E instance on Delta >= h^(c1) diagonals, built in T1-type class blocks under any residue rule with Q <= h^(1/2). This covers the NEW IDEA with p1 p2 <= h^(1/2), in particular p_i about Lambda^2. Then every class block with |Z_w| >= |S| Lambda^(-10) has
 W_w >= c min(c1, 1) Lambda^2 |Z_w|.
So the relocation price of the construction is at least c Lambda^2 per label: bE = 2 for every choice of p1, p2, s1, s2. Hypothesis (PE) with bE < 2 cannot be proved this way, and the Theorem P exponent stays theta* = 1.4967429 for this route.

REMARK (where the idea's estimate went wrong). The idea estimates the surviving Lemma F weight as about 3 Lambda^2/p. That estimate keeps the per-offset probability at about 1/N. But each label is uniform on N/Q slots, so a permitted offset has probability Q/N. The surviving pairs are exactly the pairs in matching residue classes: on average a 1/Q fraction, which is what Cauchy-Schwarz guarantees. They carry Q times the probability. The nonresidue condition only decides which pairs match (for the NEW IDEA, those with p1 | Delta a), not how many. The loss is a factor ln(R2_Q)/ln(R2) = 1 - O(log Q/Lambda).

REMARK (the only residue-rule escape). The bound becomes trivial only when Q M0^Q >= |Z| h^(-o(1)) for both parities.
- For the NEW IDEA, the labels that share an odd row share their residue mod p1, so M0^Q >= M0/p2. Escaping therefore needs p1 >= h^(1-o(1)), and p2 >= h^(1-o(1)) for the even parity.
- That means Q >= h^(2-o(1)), which pins every label's column modulo about h^2. This is the rigid layout of rigid_layout_cross_block, which the floor note already set aside.

## Proofs

0. THE IDEA'S CONGRUENCE CLAIM IS CORRECT; THE CONCLUSION DRAWN FROM IT IS NOT. Take labels e, f with p1 not dividing y = a_f - a_e. The lists force X = x_f - x_e = s1 y mod p1, so X^2 + y^2 = (s1^2 + 1) y^2 mod p1. That is a nonresidue times a nonzero square, so X^2 + y^2 is not a square and the odd points are never at integral distance. The even points work the same way with p2. What fails is the weight estimate. The proof below shows that the Lemma F family is invariant, up to the logarithm ln R2_Q, under every residue rule.

1. THE KEY REPARAMETRISATION (the only new step against Theorem R). Fix coprime (r, s) with 1 <= s < r and r != s mod 2. Put q = 2mrs. For each label e write rho_pi(e) = q t_e + beta_e with 0 <= beta_e < q, and define the key
 K_{r,s}(e) = (beta_e, psi(e) - (r^2 - s^2) t_e mod Q).
The key takes at most qQ values. Suppose K(e) = K(f) with e != f, and put k = t_f - t_e. Then:
- y := rho_pi(f) - rho_pi(e) = q k;
- psi(f) - psi(e) = (r^2 - s^2) k mod Q.
Put d = k(r^2 - s^2) (signed), X = m d and L = m|k|(r^2 + s^2). Then X^2 + y^2 = m^2 k^2 ((r^2 - s^2)^2 + 4 r^2 s^2) = L^2. Also X +- L lies in 2mZ:
- for k > 0, X - L = -2mks^2 and X + L = 2mkr^2;
- for k < 0, the roles of r^2 and s^2 swap.
So u-+ = x_e + (X -+ L)/2 are slot columns. In slot indices they are j_e - |k|s^2 and j_e + |k|r^2 for k > 0, and j_e - |k|r^2 and j_e + |k|s^2 for k < 0. Both differ from j_e and from j_f = j_e + d.
Let A(e, f, r, s) be the event {j_f - j_e = d}. When all other slots are empty, u-+ hold s0. By Lemma F (with the audit's weakening: only s0 != (a+c)/2 and X != 0 are needed), A is an event of E. The ratio X/y = (r^2 - s^2)/(2rs) is strictly increasing in r/s, so distinct (r, s) give disjoint events for each ordered pair.

2. PROBABILITY. Since psi(f) = psi(e) + d mod Q, every j_e in L_e with 0 <= j_e + d < N has j_e + d in L_f. Restrict to j_e in [N/4, N/2).
- The range of d: |k| < h/q, so |d| <= |k| r^2 < hr/(2ms) <= hR1/(2m) = N/4 whenever r <= s R1.
- The range of u-+: |k| s^2 < h/(2m) <= N/4 when N >= 2h/m, so u-+ lie in [0, 3N/4].
- The bound: P(A) >= |L_e intersect [N/4, N/2)| / (|L_e| |L_f|) >= (n/4 - 1)/(n+1)^2 with n = N/Q. This is at least 1/(5n) = Q/(5N) for n >= 29, so N >= 40Q suffices.

3. COUNT (Cauchy-Schwarz over keys). Let A_kappa count the labels with key kappa. Then sum over kappa of A_kappa^2 >= |Z|^2/(qQ). Subtract:
- |Z| for e = f;
- the pairs with the same key and y = 0. These have t_e = t_f, so psi(e) = psi(f), and there are at most |Z|(M0^Q - 1) of them;
- the pairs whose midpoint row is s0. Then f's pi-row is 2s0 - rho_pi(e), and the key fixes psi(f). There are at most |Z| M0^Q of them.
So the number N'_{q,Q} of admissible ordered pairs is at least |Z|^2/(qQ) - 2|Z| M0^Q.

4. SUM. Let Acal be the set of (r, s) with s <= R2_Q^(1/3) and s < r <= min(s R1, R2_Q^(2/3)). The average incident sum is at least
 (1/|Z|) sum over Acal of N'_{q,Q} Q/(5N) >= (|Z|/(10W)) sum over Acal of 1/(rs) - |Acal| 2 M0^Q Q/(5N),
using mN = W. The Q in the probability cancels the Q in the key count exactly.
- The error. |Acal| <= R2_Q(1 + ln R2_Q). Also |Z| <= (h/2 + 1) Q M0^Q, so ln R2_Q <= Lambda. Hence the error is at most 2|Z|(1 + ln R2_Q)/(5 W Lambda^3) <= |Z|/(W Lambda^2).
- The main sum. It is Theorem R's harmonic sum over coprime opposite-parity pairs, at least ((1/pi^2) ln R2_Q - C)(ln min(R1, R2_Q^(1/3)) - ln 3). The audit re-derived it: at least phi(s) classes mod 2s, each contributing (1/(2s)) ln(U/(3s)), and sum of phi(s)/s^2 = (6/pi^2) ln S + O(1). No coprimality to Q is used, because the key replaces inverting 2rs mod Q.
This proves (a).

5. CERTIFICATES, part (b). All events containing e contain the variable j_e, so they form a clique. If their probabilities sum to at least 1, events with the same (P, G) data can cover a product space, so every sound (P, G)-only criterion fails. This is the clique case of Shearer, given directly in the floor note and its audit. Some e has an incident sum at least the average, and (a) then gives (b). The first-moment deletion budget fails by the same sum.

6. PART (c). Given (j_e, j_f), the other labels are independent. A slot u lies in L_g only for g in Z_{c(u)}, so
 P(u- or u+ occupied) <= 2 max_c |Z_c| / (N/Q - 1) <= 2(N/(5Q))/(N/Q - 1) < 1/2.
The configuration is fatal whatever else is black, by Lemma diff, since extra black points do not restore validity. Ordered pairs give at most twice the unordered ones, which gives (c).

7. COROLLARY RQ1. The Theorem E / T1 facts are the ones audit_relocation_price_floor.md checked against T2 Section 7 and filled_mod7:
- m = 7, centres i.i.d. on period-zero slots, empty slots hold the O(1) filler row F, labels in [5000, h - 5000];
- labels f_{T,i} with rows 2i+1 and 2i+T+1, so M0 <= Delta for both parities;
- O(ell) separated class blocks.
The new lists are subsets of the period-zero slots, so these facts are unchanged and the blocks are in P_res(Q).
- M0^Q <= M0 <= Delta.
- The classes with |Z_w| >= |S| Lambda^(-10) hold all but O(ell Lambda^(-10))|S| labels. For them R2_Q >= |Z_w|/(7 Q Delta Lambda^3) >= h Lambda^(-13)/(C Q) >= h^(1/2) Lambda^(-14).
- The coincidence events of one label have average incident sum at least (Q/(N+Q))(|Z_w|/Q - 1), so any certificate forces N >= |Z_w| - 2Q. Together with (E4), N_w >= C0 n_w, this gives R1 >= c Delta Lambda^(-10) >= h^(c1/2).
Theorem RQ(b) then gives W_w >= c |Z_w| (Lambda/2 - O(ln Lambda))(min(c1 Lambda/2, Lambda/6) - O(ln Lambda)) >= c' min(c1, 1) Lambda^2 |Z_w|. Summing over these classes, the heavy relocation costs at least c Lambda^2 per label, so bE = 2.
- For Q = Lambda^(O(1)), as in p_i about Lambda^2, the logarithms are Lambda(1 - o(1)), so even the constant is essentially that of class P.

8. THE ESCAPE REMARK. R2_Q <= h^(o(1)) requires Q M0^Q >= |Z| h^(-o(1)).
- For the NEW IDEA, the labels sharing the odd row a are the f_{T,i} with distinct T. They all have psi = 7^{-1} s1 a mod p1, so M0^{Q,odd} >= M0/p2, and R2_Q <= |Z|/(7 p1 M0 Lambda^3), which is about h/(p1 Lambda^3).
- By the symmetric argument, the even parity gives R2_Q about h/(p2 Lambda^3).
- So both parities escape only with p1, p2 >= h^(1-o(1)).
- Conversely, if the T in D are equidistributed mod p2 (M0^{Q,odd} <= 2 Delta/p2), the odd-parity bound holds with Q replaced by p1. Then Corollary RQ1 extends to p1, p2 <= h^(1/2) each.

9. SANITY CHECK (not part of the proof). lemmaF_weight.py computes the exact expected Lemma F weight per label (both parities, i.i.d. uniform on the lists, m = 7, T in {2, 6, 10}, 12 sampled labels, u-+ occupancy ignored), with N = 3h. Results for class P / (p1, p2) = (3, 5) / (11, 13), with s1 = s2 = 1 (2 is a nonresidue mod 3, 5, 11 and 13):
- h = 1000: 3.55 / 2.20 / 0.90;
- h = 3000: 4.59 / 3.19 / 1.68;
- h = 6000: 5.24 / 3.84 / 2.27.
The class-P weight grows like ln h. The deficit stays bounded: 1.35, 1.40, 1.40 for Q = 15, and 2.65, 2.91, 2.97 for Q = 143. The ratio tends to 1 (0.62 -> 0.73, and 0.25 -> 0.43). This is the predicted ln(R2/Q) versus ln R2 behaviour, not a reduction by a factor p.

## External results used

- Lemma diff, papers/extremal/sections/sec2_prelim.tex: two rectangles have the same presentation iff the symmetric difference of their corner sets is black. Used through Lemma F.
- Lemma F and Theorem R, research_archive/2026-11-13/relocation_price_floor.md, with the corrections in audit_relocation_price_floor.md: the amended class P, the separation clause, the weakened Lemma F hypothesis, the harmonic-sum lower bound, '< 1' in the certificate clause, and ln R2 <= Lambda in the error term. Theorem RQ repeats that proof with the key of Section 1 in place of the residue classes of the row.
- Clique case of Shearer's theorem (J. B. Shearer, Combinatorica 5 (1985) 241-245). Hypothesis: a family of events whose dependency graph is a clique, with probabilities summing to at least 1. Conclusion: some probability space with these probabilities and this graph has the events covering the space, so no (P, G)-only criterion certifies avoidance. The direct proof is given in the floor note and its audit.
- Classical: Pythagorean triples are parametrised by coprime (r, s) of opposite parity, and sum over s <= S of phi(s)/s^2 = (6/pi^2) ln S + O(1). The web was not used.

## Checks

Analytic first.
- Checked by hand: the nonresidue claim of the idea; the key identity psi(f) - psi(e) = (r^2 - s^2)k mod Q for equal keys; that X +- L lies in 2mZ for both signs of k, so u-+ are slots distinct from j_e and j_f; the range bounds |d| < N/4 and u-+ in [0, 3N/4]; the probability bound (n/4 - 1)/(n+1)^2 >= 1/(5n) for n = N/Q >= 29; the three subtractions in the Cauchy-Schwarz count with M0^Q; the error bound using |Z| <= (h/2+1) Q M0^Q; part (c)'s union bound 2(N/(5Q))/(N/Q - 1) < 1/2; the coincidence floor N >= |Z| - 2Q; and the R1, R2_Q bounds of Corollary RQ1 for Q <= h^(1/2).
- Read: relocation_price_exponent.md and relocation_price_floor.md in full, and audit_relocation_price_floor.md lines 1-135.
- One sanity script, scripts_congruence/lemmaF_weight.py, run with py -I three times (h = 1000, 3000, 6000), each well under 60 s. The output is in proof Section 9.
- The repository was only read. I ran no git command and used no web sources.

## Gaps

- Theorem RQ is a method bound for class P_res(Q): i.i.d. uniform centres on residue lists, one fixed sea row on empty slots, and (P, G)-only certificates or first-moment deletion. It does not bound m_h. It also does not cover combining the congruence lists with a sequential, greedy or conditional placement. That loophole stays open exactly as in the audit of Theorem R. The lists do not change the conflict density a greedy placement faces, but I did not prove anything about greedy placement.
- Corollary RQ1 relies on the Theorem E / T1 block facts (m = 7, the period-zero filler F, label rows, (E4) N_w >= C0 n_w, separated O(ell) blocks) as audit_relocation_price_floor.md checked them against T2 Section 7 and filled_mod7. I did not re-read T2, filled_mod7, block_layout_n1, t1_cost_decomposition, higher_arity_true_counts, pair_families_dp_colouring or line_aware_greedy in this session. The obstruction comes from the Lemma F family alone, so the requested recomputation of the other families' weights (coincidences, vertical rivals, label-sea pairs, R1/R2 two-sea supports, triangles, three- and four-label events), the choice of p1 and p2, and the compatibility with N1 (a)-(f) and the collars are moot and were not done. One point I did not check: a family that is not Pythagorean, with offsets biased toward the allowed residue difference, could have its weight raised by up to a factor Q.
- The extension of Corollary RQ1 to Q > h^(1/2) (Section 8) needs either equidistribution of the diagonal set D mod p2 (and mod p1), or the refined M0^Q bound. For an arbitrary heavy-diagonal set D that is not proved. Large Q does not help the idea in any case: escaping the bound needs Q >= h^(2-o(1)), which is the rigid layout.
- Constants c, C0 are absolute but not computed. They are those of Theorem R, with N >= 40Q replacing N >= 20.
- Nothing here has been audited by a second reader. The sanity script ignores u+- occupancy and block membership of u+-, and it covers only h <= 6000 and three diagonals.

## Missing estimate

(PE) with bE < 2 still needs a block outside class P_res(Q), not just outside class P. Every residue rule for the lists, at any modulus Q <= h^(1/2) (and up to h^(2-o(1)) for the NEW IDEA when D is equidistributed), leaves the Lemma F incident sum at c Lambda^2 |Z|/W under i.i.d. placement with a (P, G)-only certificate. The remaining options are:
- a sequential or conditional placement that beats both the Lemma F family and T2's sqrt(nQA(w)) term;
- slot seas with many rows;
- the rigid layout, with Q about h^2.

## Next steps

- Have a second reader audit Theorem RQ. The only new step against the audited Theorem R is the key K_{r,s}(e) = (rho mod 2mrs, psi(e) - (r^2 - s^2) floor(rho/2mrs) mod Q) and the cancellation of Q between the key count and the probability Q/(5N).
- Record in the ledger and the floor note that the congruence or mod-p list loophole is closed for i.i.d. placement. This includes the 'mod-p-rule class' gap listed in relocation_price_floor.md, as far as the lists are residue classes in the slot index and placement is i.i.d. Their even-even equidistribution question is no longer needed for that class, because the key argument needs no equidistribution.
- If congruence lists are still wanted, use them only inside a sequential or greedy placement. First check whether the residue structure helps a greedy at all: the conflict density per list slot is unchanged, by the same key computation, so I expect no gain.
- Do not choose p1, p2 to optimise this route. By Corollary RQ1 every choice with p1 p2 <= h^(1/2) gives bE = 2.

# Derivation 2 (Theorem RL)

## Status

obstruction

## Summary

The congruence-restricted slot lists fail. The idea claims the surviving Lemma F weight is about 3 Lambda^2/p, but it is still of order Lambda^2. Two effects cancel the 1/p fraction of surviving pairs: (i) a list of N/Q slots (Q = p1 p2) makes each event Q times as likely; (ii) given p | y, every Lemma F offset the lists allow is a p-multiple of a Pythagorean triple, and a constant fraction of all triples have that form, not 1/p of them. I proved a general floor for any independent label-dependent slot laws, Theorem RL. It gives price >= c Lambda^2 whenever N/N' <= n/(M0 h^c). The new idea has N/N' = Lambda^4.

## Statements

SETTING (class P_list; the same as class P, amended in audit_relocation_price_floor.md, except for the slot law). A block has W = mN columns. Its slots are the columns mj for j in [0, N), and it is flanked by the usual sea separations. Every empty slot holds one fixed sea row s0, and s0 is not a label row. Each label e of Z (n = |Z|) has its centre slot drawn independently from an arbitrary, label-dependent law mu_e on [0, N). The law satisfies:
 (L1) ||mu_e||_inf <= 1/N';
 (L2) mu_e([N/8, 7N/8)) >= 1/2.
The events E are T1/T2's events: configurations that contain a forbidden support when all other slots are empty. A certificate is any criterion that uses only (P(A), the shared-label dependency graph) and is sound for every probability space with these data. This includes every form of the local lemma and Shearer's criterion. Fix a parity pi with label rows rho(e). Let M0 be the largest number of labels sharing a pi-row, Lambda = log h, R1 = W/(4h) and R2 = n N'/(m M0 N Lambda^3).

THEOREM RL (PROVED). There are absolute constants c, C0 > 0 such that, if R1, R2 >= C0 and h >= h0:
 (a) the average over e of the sum of P(A), over the two-label Lemma F events A of E that contain e, is at least c n ln R2 ln min(R1, R2^(1/3)) / W;
 (b) every certificate in the class needs W > c n ln R2 ln min(R1, R2^(1/3));
 (c) suppose every slot u has occupancy sum_g mu_g(u) <= 1/4. Then the expected number of unordered fatal Lemma F pairs, with all labels present, is at least (c/4) n^2 ln R2 ln min(R1, R2^(1/3)) / W. So alteration by the first moment fails as well.
With N' = N (uniform laws on all slots) this is Theorem R. The only change is the factor N'/N inside R2, which enters only through a logarithm.

COROLLARY 1 (the NEW IDEA; PROVED). Take p1, p2 primes coprime to 14 with s_i^2 + 1 a quadratic nonresidue mod p_i, and Q = p1 p2. Take the T1-block lists L(e) = {j : 7j = s1 a_e (mod p1), 7j = s2 b_e (mod p2)} with mu_e uniform on L(e) and N/Q >= 10. Then (L1) holds with N' >= N/(2Q), (L2) holds, and R2 >= n/(14 M0 Q Lambda^3). In the main Theorem E classes (M0 <= Delta, n = |Z_w| >= |S| Lambda^(-10), |S| >= Delta h/C, R1 >= h^(c1/2)), and for any Q <= h^(1/2), in particular Q of order Lambda^4, the block still costs at least c c1 Lambda^2 per label. This holds for both parities, so the idea does not lower the relocation price below Lambda^2 and does not lower theta* = 1.4967.

PROPOSITION 2 (which Lemma F events survive; PROVED). Under the lists of Corollary 1, an odd-odd Lemma F event for (e, f) needs p1 | y, p1 | X and p1 | L, where y = a_f - a_e and (X, y, L) is the Pythagorean triple. So the triple is p1 times a triple for y/p1, and the event also needs one congruence mod p2 on X. The even-even case is the same with p2 and b. Every surviving family has offsets X = lambda y with lambda = (r^2 - s^2)/(2rs). The class conditions are then equivalence relations on labels with at most 2m rs Q classes, and Cauchy-Schwarz shows that the surviving weight is at least a constant times the unrestricted weight. The note's estimate of about 3 Lambda^2/p leaves out the factor Q in each event's probability.

COROLLARY 3 (where the floor ends; PROVED as a consequence of RL). A scheme in class P_list can price the Lemma F family at o(Lambda^2) only if ln R2 = o(Lambda), that is, N/N' >= (n/M0) h^(-o(1)). In the Theorem E classes this means N/N' >= h^(1-o(1)): each label's column must be fixed modulo about h^(1-o(1)). That is the near-rigid regime, which the board prices by its class counts and not by relocation.

HEURISTIC 4 (not proved). For the specific rule, the odd-odd survivor weight behaves like ln(h/p1) ln R1 and the even-even weight like ln(h/p2) ln R1. Only p1, p2 >= h^(1-o(1)), so Q >= h^(2-o(1)), kills both families, and then the lists have h^(o(1)) slots.

REMARK 5 (the upper-bound side; a gap in the idea, not a theorem). T2's budgets (10) and (14) count geometries G_J and use P <= N^(-(k-1)). Under restricted lists P <= (Q/N)^(k-1), and the restricted geometry counts are smaller only if the offsets are equidistributed mod Q against the label class forms. That is unproved. Without it, the T2 certificate for the restricted block loses a factor Q in the pair term and Q^(k-1) in the k-label terms.

## Proofs

0. NOTATION AND REDUCTION. Write lambda = lambda(r, s) = (r^2 - s^2)/(2rs) for coprime r > s >= 1 of opposite parity. Lemma F (relocation_price_floor.md, audited) needs:
- labels e != f with same-parity points C = (x_e, rho_e) and D = (x_e + X, rho_f);
- y = rho_f - rho_e != 0 and X^2 + y^2 = L^2;
- black points in row s0 at u- = x_e + (X - L)/2 and u+ = x_e + (X + L)/2;
- s0 != (rho_e + rho_f)/2.
Then the configuration is fatal. The audit notes that s0 not in {rho_e, rho_f} is not needed.

1. PARAMETRIZATION (as in Theorem R, but with signed k).
- Let q = 2mrs and suppose y = qk with k != 0. Put X = lambda y = m k (r^2 - s^2) and L = m|k|(r^2 + s^2). Then X^2 + y^2 = m^2 k^2 (r^2 + s^2)^2 = L^2.
- For k > 0: u- = x_e - mks^2 and u+ = x_e + mkr^2. For k < 0: u- = x_e - m|k|r^2 and u+ = x_e + m|k|s^2.
- So u+- are multiples of m, that is, slot columns. When empty they hold s0.
- Take r <= s R1. Then |X| <= |y| r/(2s) <= h R1/2 = W/8, and |u+- - x_e| <= m|k| r^2 = |y| r/(2s) <= W/8.
- So x_e in [W/8, 7W/8) puts x_f and u+- inside the block. The event A(e, f; r, s) = {x_f - x_e = X} is then an event of E: Lemma F applies with all other slots empty.
- For fixed (e, f), distinct (r, s) give distinct values of X/y = lambda, so these events are pairwise disjoint and distinct.

2. CAUCHY-SCHWARZ FOR ARBITRARY LAWS (the new step). Fix (r, s) and split Z into classes c by rho mod q. Let nu_e be mu_e restricted to [N/8, 7N/8).
- For e in class c, define nu~_e(z) = nu_e(z + lambda rho_e/m). For e, f in the same class, lambda rho_f/m - lambda rho_e/m = (r^2 - s^2) k is an integer, so all nu~_e with e in c live on one coset of Z.
- For e, f in c:
 sum_z nu~_e(z) nu~_f(z) = sum_j nu_e(j) nu_f(j + X/m) <= P(A(e, f; r, s)).
- The supports of the nu~_e, e in c, lie in an interval of length at most 3N/4 + lambda h/m <= 3N/4 + N/8, because lambda <= r/(2s) <= R1/2 = W/(8h). So they cover at most N + 1 <= 2N points of the coset.
- Cauchy-Schwarz and (L2) give:
 sum over (e, f) in c x c of sum_z nu~_e nu~_f = sum_z (sum over e in c of nu~_e(z))^2 >= (sum over e in c of |nu_e|)^2/(2N) >= n_c^2/(8N).
- Summing over at most q classes gives at least n^2/(8qN) = n^2/(16 m rs N).
- Subtract the ordered pairs that do not give a Lemma F event: e = f; rho_e = rho_f (y = 0, a coincidence counted separately in E); and (rho_e + rho_f)/2 = s0. There are at most 2 n M0 such pairs, and by (L1) each term is at most ||mu_f||_inf <= 1/N'.
- So the Lemma F events for (r, s) have total probability over ordered pairs of at least n^2/(16 m rs N) - 2 n M0/N'.
Note that Q never appears. If the lists are residue classes, as in Corollary 1, a pair whose classes do not fit the offset X has disjoint supports for nu~_e and nu~_f and contributes 0. The concentration of the surviving pairs is exactly what Cauchy-Schwarz records.

3. SUMMATION. Let Acal be the set of (r, s) with s <= R2^(1/3) and s < r <= min(s R1, R2^(2/3)), coprime and of opposite parity.
- The audited harmonic sum of Theorem R(iv): sum over Acal of 1/(rs) >= ((1/pi^2) ln R2 - C)(ln min(R1, R2^(1/3)) - ln 3).
- |Acal| <= R2(1 + ln R2).
- The error term: sum over Acal of 2 n M0/N' <= 2 n M0 R2 (1 + ln R2)/N' = 2 n^2 (1 + ln R2)/(m N Lambda^3). This is at most 4 n^2/(m N Lambda^2), using ln R2 <= Lambda. That bound holds because n <= (h/2 + 1) M0 and N' <= N, so R2 <= h.
- Divide by n. The average incident Lemma F sum is at least (n/(16 m N)) (sum over Acal of 1/(rs) - 64/Lambda^2) >= c n ln R2 ln min(R1, R2^(1/3))/W for R1, R2 >= C0. This is (a).

4. PARTS (b) AND (c).
- (b) The events containing e all contain x_e, so they form a clique of the dependency graph. If their probabilities sum to at least 1, disjoint events with the same data can cover the space. This is the clique case of Shearer, checked in the audit, and it does not depend on the slot law. So a certificate needs every incident sum below 1, and some e has an incident sum at least the average.
- (c) The other labels are independent of (x_e, x_f). With occupancy at most 1/4 at u- and u+, both are free with probability at least 1/2. The events for the two orientations of a pair are disjoint, which gives the factor 1/2 for unordered pairs.

5. COROLLARY 1.
- L(e) is an arithmetic progression of difference Q in j. The residue is fixed by the CRT, since p_i is coprime to 7.
- |L(e)| is between N/Q - 1 and N/Q + 1. So ||mu_e||_inf <= 1/(N/Q - 1) <= 2Q/N, and the central mass is at least (3N/(4Q) - 1)/(N/Q + 1) >= 1/2 for N/Q >= 10.
- So N' = N/(2Q) and R2 >= n/(14 M0 Q Lambda^3).
- With the Theorem E bounds from Corollary R1 (audited): R2 >= h Lambda^(-14)/(14 Q) >= h^(1/2 - o(1)) for Q <= h^(1/2), and R1 >= h^(c1/2). Theorem RL(b) then gives W >= c c1 Lambda^2 n.
- The same argument works for the even points with rows b_e. Crowding does not help: on one diagonal T, the map a -> class (a mod p1, a + T mod p2) is a CRT bijection mod Q, so the classes are balanced to within Delta.

6. PROPOSITION 2 (survivor structure).
- x_f - x_e = s1 y (mod p1) is forced. If p1 does not divide y, then X^2 + y^2 = (s1^2 + 1) y^2 (mod p1), a nonresidue, so the points are never at integral distance. This part of the idea is correct.
- If p1 | y, then X = s1 y = 0 (mod p1), so p1^2 | L^2 and the triple is p1 times a triple for y/p1. In the parametrization, 7k(r^2 - s^2) = 14 s1 rs k (mod p1) with p1 not dividing k would need (r/s - s1)^2 = s1^2 + 1 (mod p1), which is impossible. So p1 | k.
- The p2 condition is m k (r^2 - s^2) = s2 (b_f - b_e) (mod p2). With k = y (2mrs)^(-1) mod p2 (for p2 not dividing rs), it reads psi(f) = psi(e) for the linear form psi(e) = (r^2 - s^2)(2rs)^(-1) a_e - s2 b_e (mod p2).
- These are equivalence relations with at most 2m rs Q classes, which is the structure Step 2 uses. Dropping the (r, s) with p2 | rs costs O(Lambda^2/p2), which is negligible.
- Why the estimate of about 3 Lambda^2/p fails: about 1/p1 of the pairs survive, the p2 class keeps about 1/p2 of the offsets, and each event's probability rises by Q because the lists have N/Q slots. The product is 1, up to the shift of ln h to ln(h/p) in the logarithms. The extra factor 3 is the gain tau(p^2 y'^2) = 3 tau(y'^2): given p | y, about 1/3 of the triples are p-imprimitive, not 1/p of them. That is the concentration the target asked about.

7. COROLLARY 3. Here R1 >= h^c, so (b) gives o(Lambda^2) only if ln R2 = o(Lambda). That requires N/N' >= (n/M0) h^(-o(1)) >= h^(1-o(1)) in Theorem E.

8. MIXED PARITY. An odd point and an even point have y odd. Then X^2 + y^2 = L^2 forces X even and L odd, so (X +- L)/2 is not an integer and no mixed-parity Lemma F support exists. The column condition depends on a_f - a_e and b_f - b_e, not on the mixed gap b_f - a_e. So the nonresidue mechanism neither kills nor reduces T2's mixed families (vertical rivals and mixed four-cell supports). Their average weight is preserved under equidistribution (Remark 5), but no upper bound for them under restricted lists is proved. For the same-parity families, the structure inherited from T2 changes nothing:
- the rows of a T1 block agree mod 14, so 14 | y is automatic and gcd(Q, 14) = 1;
- u+- are period-zero columns holding F;
- the midpoint is a bulk row.

NUMERICAL SANITY CHECK. The script is scripts_adversary/lemmaF_restricted.py. Each run took under 25 s.
- Setup: m = 7, labels (a, a + T) with a = 1 mod 14, Delta = 2 diagonals, N = 6n. I computed exact average Lemma F incident sums with exact AP overlap counts and u+- inside the block, for full lists and for the restricted lists of Corollary 1.
- With (p1, s1, p2, s2) = (3, 1, 5, 1) and h = 1000, 2000, 4000, 8000:

| h | odd: restricted / full | ratio | even: restricted / full | ratio |
| --- | --- | --- | --- | --- |
| 1000 | 0.41 / 0.89 | 0.46 | 0.36 / 0.89 | 0.40 |
| 2000 | 0.59 / 1.09 | 0.54 | 0.54 / 1.09 | 0.50 |
| 4000 | 0.79 / 1.30 | 0.61 | 0.74 / 1.30 | 0.57 |
| 8000 | 1.00 / 1.51 | 0.66 | 0.95 / 1.51 | 0.63 |

- All of the restricted weight comes from p | y, as Proposition 2 says.
- Per doubling of h, the restricted sum grows by 0.18 to 0.205 and the full sum by 0.21. Their difference stays at about 0.5. This matches a shift of ln h to ln(h/p) at fixed R1, not a factor 1/p.
- At (5, 1, 11, 1) and h = 1500, the ratios were 0.38 and 0.28: smaller at small h, as the ln(h/p) shift predicts.
These are toy sizes with R1 of about 6. They are a sanity check only; the result rests on the proof.

## External results used

- Lemma F, Theorem R (a)-(c), the harmonic sum over coprime pairs, and the clique case of Shearer's criterion: relocation_price_floor.md and audit_relocation_price_floor.md (audited; corrected statement of class P and the separation clause).
- Corollary R1 class bounds for Theorem E (M0 <= Delta, R1 >= h^(c1/2), R2 >= h Lambda^(-14)/7): same audit.
- T2 (safe_triangle_pair_first_moment.md) Sections 4 to 7: the pair budget (10), the higher-arity bound (14), and the product-form local lemma placement (17) with P <= N^(-(k-1)).
- Standard facts: the parametrization of Pythagorean triples by coprime (r, s) of opposite parity; the CRT; tau(p^2 y'^2) = 3 tau(y'^2) for p not dividing y'.

## Checks

I checked by hand: the nonresidue kill for p not dividing y; that a survivor needs p | k, so the triple is p times a triple; the reduction of the p2 condition to a linear form psi mod p2; the shifted-law Cauchy-Schwarz with support at most 2N and the range bounds |X|, |u+- - x_e| <= W/8 for r <= s R1 with R1 = W/(4h); the subtraction of the e = f, y = 0 and midpoint pairs (at most 2 n M0 pairs, each term at most 1/N'); the error term using ln R2 <= Lambda; and the AP bounds |L(e)| between N/Q - 1 and N/Q + 1 with central mass at least 1/2. I ran one exact-count script at a time with py, each under 25 s and well under 1 GB; the table is in the proof. The repository was only read. No git command was run, and no report file was written.

## Gaps

- Theorem RL bounds a method class: independent slot laws (arbitrary and label-dependent), one fixed sea row s0 on empty slots, and certificates that use only (P(A), the dependency graph), plus first-moment alteration. Sequential, greedy or conditioned placements are not covered, and neither is the many-slot-rows loophole (empty-slot rows that depend on the slot class). With rows varying by class mod Q, the odd survivors already have p1 | k, so only p2 can help them. This is the existing open loophole of Theorem R(d) and is not analysed here.
- Corollary 1 imports the Theorem E class bounds (M0 <= Delta, |Z_w| >= |S| Lambda^(-10), R1 >= h^(c1/2)) from Corollary R1 and its audit, and the separation clause for narrow blocks from the audit. I did not re-derive them. For blocks narrower than h^(1+c), the separation-floor lemma should carry over: the coincidence bound becomes N' > max class size - 1, so N >= n - Q. I did not write this out.
- Heuristic 4 is not proved: that for the specific rule the odd weight is about ln(h/p1) ln R1 regardless of p2, so that only p1, p2 >= h^(1-o(1)) kill both families. Theorem RL is rigorous only while Q <= (n/M0) h^(-c).
- Remark 5 is an observation, not a theorem. No upper bound for T2's pair or higher-arity budgets under restricted lists is proved. The transfer needs the geometry offsets to be equidistributed mod Q against the label class forms. A family with a fixed slope lambda = s1 (mod p1) and lambda = s2 (mod p2) would gain the full factor Q; the choice of s_i must avoid the slopes of live families, and I did not classify them.
- I read in full: relocation_price_floor.md, the verdict and corrected statement of its audit, pair_families_dp_colouring.md, and T2 Sections 4 to 7. I only searched t1_cost_decomposition.md, conflict_free_matchings.md, line_aware_greedy.md, stride_menu.md and rigid_layout_cross_block.md for the mod-p material. I did not read higher_arity_true_counts.md, the t1 audit, or Section 3 of compatible_profile_threshold.md in full. The obstruction uses only Lemma F and the audited parts of Theorem R, so it does not depend on them.
- The numerics are toy sizes (h <= 8000, R1 about 6, small p). They show the trend; they do not test p of order Lambda^2, where the lists would be too short at feasible h.
- Nothing here has been audited.

## Missing estimate

To beat Lambda^2 in any independent-slot scheme with a single row s0 on empty slots, Theorem RL leaves one option for the Lemma F family: near-rigid laws, with ||mu_e||_inf >= (n/(M0 N)) h^(-o(1)), that is, each column fixed modulo about h^(1-o(1)) in the Theorem E classes. Congruence lists with p of order Lambda^2 are far from this. Outside the class, the remaining routes are the ones already open on file: a greedy or nibble placement (line_aware_greedy.md, Hypothesis W plus IT-w), slot seas with many rows, and rigid absorption of heavy diagonals. For the restricted-list idea itself, any use (for example combined with greedy) would also need an equidistribution estimate. For each T2 role, the number of geometries between e and f whose offset lies in the class g(f) - g(e) mod Q would have to be at most (1 + o(1)) G_ef/Q on average over the pairs. That is needed so the other families keep their budgets; it is not proved.

## Next steps

- Audit Theorem RL. The only new step is Step 2: Cauchy-Schwarz over z for the shifted laws nu~_e(z) = nu_e(z + lambda rho_e/m) inside each class mod 2m rs, with support size at most 2N. Everything else is the audited Theorem R. If it passes, record in the ledger that Theorem R extends to arbitrary label-dependent independent slot laws, with R2 multiplied by N'/N. That closes the congruence-list and mod-p-rule variants with p <= h^(1-c), and corrects the gap remark in relocation_price_floor.md that the mod-p rule kills odd-odd pairs (true only for p > h).
- Mark the NEW IDEA as refuted for its stated parameters (p of order Lambda^2, or any p1 p2 <= h^(1/2)), and note that the 3 Lambda^2/p estimate leaves out the factor Q in each event's probability.
- Optional: prove Heuristic 4 for Theorem E label sets (cross-diagonal pairs with the T's equidistributed mod p2). It would show that the per-parity survivor weight is about ln(h/p) ln R1 independently of the other prime, and so pin the escape at p >= h^(1-o(1)).
- Spend relocation effort only outside class P_list: the line-aware greedy (Hypothesis W and IT-w), or seas with many slot rows. Residue restrictions of the lists cannot change the Lemma F price by more than a constant inside class P_list.

