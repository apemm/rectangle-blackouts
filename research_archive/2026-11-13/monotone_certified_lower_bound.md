# Certified monotone partitions and a fractional lower bound

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Not audited yet.

# Result

## Status

partial

## Summary

No linear monotone partition was found. I prove that mixing offsets cannot help any partition whose P-freeness rests on the slot set alone (all arc and Bohr classes): such a partition needs at least F(h) = sum_T |I_T|/alpha_A(S_T) classes, the averaged fractional form of (E). I also prove a template reduction. The one known escape is the asymmetric T29 rule, and that rule appears to gain only a log log factor under monotonicity.

## Statements

Notation. A = ceil(h/2), K = floor(h/2). A label (i,T) has slot i, offset T = 2(j-i)+1 and j = i + (T-1)/2. I_T is the set of slots of diagonal T on the board. S_T = { d != 0 : 20d^2 + 4Td + T^2 = L^2, 0 < L < h } is the full set, with no restriction on |d|. A class is a set of labels with distinct slots. X_c is the slot set of class c. Monotone means that j is nondecreasing in i and that j' - j <= C(i' - i).

Fact 0 (P-freeness is a condition on the slot set). Labels (i,T) and (i',T') are in P conflict exactly when i - i' is in S_T or i' - i is in S_T'. So a class c is P-free exactly when (i - S_{T(i)}) and X_c are disjoint for every label (i, T(i)) of c. The relation is invariant under (i,T) -> (i+t,T).

Definition. A class c is certified for the offset T if no two slots of X_c differ by an element of S_T. Put alpha_A(D) = max{ |Y| : Y a subset of [0,A), (Y - Y) disjoint from D }.

Theorem 1 (lower bound for certified classes). Take any partition of the labels into classes. Monotonicity is not needed, and classes may mix offsets. Let Cert be the set of labels (i,T) whose class is certified for T. Then the number of classes is at least sum over l = (i,T) in Cert of 1/alpha_A(S_T). In particular, if every class is certified for every offset it contains, the number of classes is at least F(h) := sum_T |I_T| / alpha_A(S_T).

Corollary 1. (a) Every constant-offset partition is certified, because a constant-offset class is P-free exactly when it is independent in G_T. Every arc class of Proposition 1 (12 November note) is certified. So is every mixed class whose P-freeness follows from a property of its slot set alone, for example a Bohr arc {i : theta i mod 1 in J} with ||theta d|| >= |J| for all d in S_T and all offsets T used. (b) F(h) <= sum_T |I_T|/alpha(G_T) <= sum_T chi(G_T). (c) Hence, among certified partitions, mixed or not, an O(h) count requires the averaged fractional statement (E_f): sum_T |I_T|/alpha_A(S_T) = O(h). Mixing can win at most the per-diagonal integrality gap between chi(G_T) and |I_T|/alpha. (d) A partition with O(h) classes that beats F(h) by more than a constant factor must put most of the weight 1/alpha_A(S_T) on uncertified labels. These are labels (i,T) whose class contains two slots that differ by an element of S_T, with neither slot the label's own. The T29 eligibility rule (i in S, (i - S_T) disjoint from S) is of this asymmetric, uncertified kind.

Theorem 2 (template reduction). Let Gamma be a set of labels in Z x (odd offsets) with these properties: distinct slots, all slots in an interval of length W, monotone with slope at most C, P-free with respect to the full S_T, and at least one label of every offset T with I_T nonempty. Then the board labels split into at most A + W - 1 monotone P-free classes, each with slope at most C. So chi_mon,P(h) <= A + W(h) - 1, where W(h) is the least such span.

Lemma 3 (few swap alternatives). In any partition of the labels into M monotone classes, count the triples (c, i, j) such that c has a label at slot i, and replacing that label by (i,j) keeps c monotone. There are at most AK + 2(K-1)M such triples. So the average label is a swap alternative for at most 1 + 2M/A classes, which is O(1) when M = O(h). The bound does not cover inserting a label into a gap of a class.

## Proofs

PROOF OF FACT 0. The odd point of slot i' is (4i', 2i'+1). The even point of label (i,j) is (4i, 2j+2). Their squared distance is 16(i-i')^2 + (2(j-i')+1)^2. Since 2(j-i')+1 = T + 2(i-i'), this equals 20d^2 + 4Td + T^2 with d = i - i'. So the odd point of i' and the even point of (i,T) are at an odd integer distance L < h exactly when d is in S_T. The other orientation gives i' - i in S_T'. Neither condition depends on j', and both depend only on (i - i', T, T'), so the relation is translation invariant. []

PROOF OF THEOREM 1. Give each label l in class c the weight w(l) = 1/|X_c|. Slots in a class are distinct, so |c| = |X_c|. The weights in each nonempty class sum to 1, so the total weight equals the number of classes. Let l = (i,T) be in Cert, with class c. No two elements of X_c differ by an element of S_T, and X_c is a subset of [0,A), so |X_c| <= alpha_A(S_T) and w(l) >= 1/alpha_A(S_T). Drop the labels outside Cert, which have nonnegative weight, and sum over Cert. If every class is certified for every offset it contains, then Cert holds every label and the sum is sum_T |I_T|/alpha_A(S_T). []

PROOF OF COROLLARY 1. (a) A constant-offset class X lies in I_T, so its differences satisfy |x| < |I_T|. It is P-free exactly when no difference lies in S_T, that is, when it is independent in G_T, and that is certification. For an arc class, two slots differ by x with ||theta x|| < 1/M, while ||theta d|| >= 1/M for every d in S_T, so x is not in S_T. The general Bohr arc case is the same argument. (b) An independent set of G_T is a subset of [0,A) with no difference in S_T, so alpha(G_T) <= alpha_A(S_T). Also chi(G_T) >= |I_T|/alpha(G_T). (c) This follows from Theorem 1, (a) and (b). (d) Theorem 1 bounds the weight on certified labels by the number of classes. The rest of (d) is Fact 0: P-freeness only requires (i - S_T) and X_c to be disjoint. []

PROOF OF THEOREM 2. For each odd offset T with I_T nonempty, fix a label (x_T, T) of Gamma. For each integer t in (-W, A), let class t be the set of board labels in Gamma + t, where (x,T) + t = (x+t, T). In (i,j) coordinates this shift is (i,j) -> (i+t, j+t). It preserves all differences, so each class is monotone with slope at most C. By Fact 0 each class is P-free, because the conflict relation is invariant under the shift and Gamma is P-free for the full S_T. A board label (i,T) lies in class t = i - x_T. Since 0 <= i < A and x_T lies in the span of Gamma (normalize the span to [0,W)), t lies in (-W, A). So at most A + W - 1 classes cover everything. Keep each label in one class only. A subset of a P-free monotone class is still P-free and still monotone: the slope bound survives deleting middle labels, because j3 - j1 = (j3 - j2) + (j2 - j1) <= C(i3 - i1). []

PROOF OF LEMMA 3. Let class c have labels (i_1, j_1), ..., (i_m, j_m) with i increasing. Then j is nondecreasing. Put j_0 = 0 and j_{m+1} = K - 1. Replacing the label at slot i_r by (i_r, j) keeps c monotone only if j_{r-1} <= j <= j_{r+1}. So there are at most j_{r+1} - j_{r-1} + 1 choices of j. The sum over r telescopes to at most j_{m+1} + j_m - j_1 - j_0 + m <= 2(K-1) + m. Summing over classes, and using that the class sizes sum to AK, gives the bound AK + 2(K-1)M. Divide by the AK labels to get the average. []

HEURISTIC: WHY UNCERTIFIED MONOTONE MIXING GAINS ONLY ABOUT log log h. This part is not proved. A class of slot density p has gaps of about 1/p. In such a gap its offset can move only within a window of about 2C/p offsets: down at most 2 per slot, up at most 2(C-1) per slot. Take a label with k_T about K, at an offset in a band of relative density nu_K. Under an asymmetric random rule it is eligible for a present class with probability (1-p)^K. It has about (C/p) nu_K window candidates. The heuristic in the setting puts the mass at nu_K about log h / K. Requiring (C/p) nu_K e^{-pK} >= 1 gives pK <= log log h + O(1). The cost of the band is then about sum k_T / log log h. Over all bands that totals O(h log h / log log h), the same bound as the local sparsity bound (local sparsity). T29 avoids this loss because a label may join any present class, which gives polynomially many candidates. Lemma 3 and the window bound remove that freedom. Inserting labels into long gaps could restore the freedom. But a gap can then take only one monotone chain through its eligible points. Section 4 of the 11 November note shows that independent eligibility of density q allows chains of length only about sqrt(q) times the area, so this needs correlated, structured eligibility. That puts the problem back on Bohr-type structure, which Theorem 1 covers.

COMPUTATIONS (sanity checks only).
(i) Online left-to-right greedy that mixes offsets. At each slot, for each j in increasing order, it picks the monotone-feasible class with the largest last j that is P-feasible: its slots avoid i - S_T for d > 0, and i is not killed by an earlier label. Otherwise it opens a new class. C = 70. Classes per h:
- h = 128: 1.45
- h = 256: 1.55
- h = 512: 1.71
- h = 1024: 1.78
- h = 2048: 1.88
- h = 4096: 1.98

That is about +0.1 per doubling. The arc classes of 12 November give 1.87, 1.91, 1.98, 2.03, 2.09, 2.13 at the same heights, about +0.05 per doubling. A separate script rebuilt every class from the norm 16(i-i')^2 + (2(j-i')+1)^2 for h = 33, 64, 97, 128. It found full coverage, monotonicity with slope at most 70, and 0 conflicts. The slope bound matters. At h = 2048 the greedy gives 2.33h for C = 1, 2.13h for C = 2, 1.97h for C = 4 and 1.88h for C = 70. Growth per doubling is about 0.2 for C = 1 and 0.1 for C = 70. This matches the window heuristic.
(ii) Template greedy, rerun of an earlier chain_greedy.py: an increasing transversal x_T with step at least 1. The span R/h is 1.83, 2.25, 2.37, 2.69, 2.80, 2.96, 3.16, 3.49, 3.61 for h = 64 to 16384, in doublings. So Theorem 2 with greedy templates gives 2.3h to 4.1h, still growing, and is worse than arcs. Reason: a template has one label per offset, so the hardest offsets (largest k_T) all have to fit in one chain of density Theta(1). With random phases that costs about e^{k_T / lambda} per offset, where lambda is the chain's mean step.

## External results used

- Ledger T29 (global_P_linear_coloring.md): random slot sets plus Hall give chi = O(h) for the vertical-rival graph without monotonicity. Its eligibility rule is asymmetric, so it is not certified in the sense of Theorem 1.
- 11 November monotone_p_palette_progress.md, Section 4: under independent private coins of probability theta, every eligible monotone class has length O(h sqrt(theta)). Section 2 there: a clique of size 2h/3 - O(1).
- 12 November arc_classes_monotone_partition.md: Proposition 1 (arc classes are monotone, P-free and free of right angles) and the arc-class counts per h.

## Checks

I re-read the proofs of Fact 0, Theorem 1, Corollary 1, Theorem 2 and Lemma 3 line by line. In Fact 0 I checked the identity 16d^2 + (T+2d)^2 = 20d^2 + 4Td + T^2, with 2(j-i')+1 = T + 2(i-i'). Computation: kill_sets matches a brute-force S_T for every odd T in (-40, 40) at h = 40. A separate script rebuilt the classes of the online mixed greedy from the original norm formula for h = 33, 64, 97 and 128. Every label was covered exactly once, every class was monotone with slope at most 70, and there were 0 P conflicts. Each run stayed under 60 seconds.

## Gaps

- No O(h) monotone P-free partition was constructed, and no omega(h) lower bound was proved for any family. Theorem 1 gives a lower bound F(h), but F(h) is only known to be at least linear. Heuristically F(h) = O(h).
- The claim that uncertified (asymmetric) monotone mixing gains at most a log log h factor is a heuristic. A rigorous version would need the distribution of k_T across offsets (a Sathe-Selberg type count of prime factors that are 1 or 4 mod 5), plus a first-moment bound on monotone chains in correlated eligible sets. I did neither.
- Lemma 3 bounds only swap alternatives. Inserting labels into long gaps can give a label many candidate classes, so Lemma 3 alone does not exclude a T29-style Hall argument with monotone gap filling. It only shows that such an argument must use long gaps and structured eligibility.
- Theorems 1 and 2 and Lemma 3 are short complete arguments that I re-read. They have not been independently audited.
- The computations are sanity checks at moderate h. The online greedy was independently verified only for h <= 128. The template-greedy numbers come from an earlier script, rerun but not independently checked.

## Missing estimate

Through Theorem 1, every certified approach, mixed or constant-offset, needs (E_f): sum_T |I_T| / alpha_A(S_T) = O(h). Here alpha_A(S_T) is the largest subset of [0,A) with no difference in S_T. It would suffice to have alpha_A(S_T) >= c A / (1 + k_T / log h) for all T outside a set of total weight O(h). This is the fractional, slot-set form of (E) in the missing estimate. For constant-offset classes the integrality step chi(G_T) <= O(|I_T| / alpha) would also be needed, unless the large independent sets are Bohr arcs, which tile exactly. To beat (E_f), a construction must be uncertified, and under monotonicity it must also produce monotone chains of eligible labels with correlated, structured eligibility. I know no candidate for that.

## Next steps

- Attack (E_f) instead of (E). It asks only for one large S_T-free subset of [0,A) per offset, and Lemma 2 of the 12 November note or a Bohr set at one scale per Pell orbit might give it. Translates and arc tiling would then give the integer count when the set is a Bohr arc.
- Turn Corollary 1(c) into a computed check: at h <= 2048, compute alpha_A(S_T), or a lower bound from the best arc, together with F(h). That shows how much the integrality gap between sum chi(G_T) and F(h) leaves for mixing.
- Prove the log log barrier rigorously for one natural model: unthinned random slot sets of density p, with eligibility i in S and (i - S_T) disjoint from S, and monotone selection. That needs a first-moment chain count with correlated eligibility and a lower bound on the number of offsets with k_T >= (log h)^{1+delta}.
- Drop the template route (Theorem 2) for linear bounds unless a structured per-offset phase is found. With a global Beatty phase, the template's P-freeness reduces to a single global Bohr condition on the union of all S_T, and that union contains every odd d < h/5. This reduction is a computation I did not write up.

