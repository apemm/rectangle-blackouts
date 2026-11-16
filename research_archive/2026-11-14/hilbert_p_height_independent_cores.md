# Height-independent P cores

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: main-diagonal Hilbert blocks carry fixed finite P systems that recur unchanged at every large height. With a computer check this gives weighted degeneracy at least 3 for M = 3, S = 32 at every h >= 528385, so degeneracy certificates for three choices cannot extend to large heights. No bounded-M rule and no bounded-M obstruction at fixed S was found. Heuristically, a greedy or degeneracy proof on this route needs S M of order (log h)^2. Not audited yet.

# Result

## Status

partial

## Summary

I found neither a bounded-M rule nor a bounded-M obstruction at fixed S. I proved a height-independent reduction: main-diagonal Hilbert blocks carry fixed finite P systems that occur unchanged at every large height. With a computer check, that gives weighted degeneracy at least 3 for M=3, S=32 at every h >= 528385, so degeneracy certificates for M=3 cannot extend to large heights. Heuristically, any greedy or degeneracy proof on this route needs SM of order (log h)^2.

## Statements

Setting: x_e = S(M r_e + xi_e), 0 <= xi_e < M, with the Hilbert order H_Q from continuation_hilbert_placement.md and all labels kept. "Candidate constraint" (r, s, delta) with s = r + d means: if xi_s - xi_r = delta, then X = S(Md + delta) and some cross-parity black pair have X^2 + Y^2 = L^2 with both completion rows in [1, h].

THEOREM A (diagonal-block lemma; proved). Let B = 2^b <= Q = 2^k. Take any aligned block D_I = [IB, IB+B)^2 on the main diagonal of the Q-square. It occupies one contiguous rank interval [rho_I, rho_I + B^2). It is traversed either as H_B (orientation "id") or as H_B with coordinates swapped ("swap"). The two diagonal children of any diagonal 2B-block have opposite orientations.

COROLLARY A1 (height-independent block systems; proved). Fix S (even), M and B. Let G_B^o, for o in {id, swap}, be the system on local ranks [0, B^2) formed from all triples (r, r+d, delta) with |delta| <= M-1. Each triple must make a local cross-parity pair (odd row 2x+1, even row 2y+2, taken from H_B or its transpose) satisfy X^2 + Y^2 = L^2 with X = S(Md + delta). The owner of the two completion rows must lie outside the block. Then for every height h >= h0(B) := 2B^2 + 8B + 1, both G_B^id and G_B^swap occur, shifted by a rank offset, as sets of genuine P rivals of the placement at height h, with identical (d, delta) data. Hence:
(i) if some G_B^o has no assignment with M choices, M choices fail at every h >= h0(B);
(ii) the weighted degeneracy of the full candidate multigraph at height h is at least that of G_B^o.

THEOREM B (computer-assisted, single unaudited implementation). For S = 32 and M = 3, G_512^id has a nonempty weighted 3-core (3134 labels, 6197 constraints). Hence at every h >= 528385:
- the Hilbert P system has weighted degeneracy >= 3, so the reverse-peeling certificate used at h = 2048 and 4096 (degeneracy < M) cannot exist for M = 3;
- criterion (8) of continuation_hilbert_local_factor_budget.md fails for M = 3, since B(3) >= 3/8.
This core is 3-choice satisfiable (SAT, verified), and so are the 3-cores of G_1024^id and G_1024^swap. Theorem B is not an obstruction to M = 3.

LEMMA C (mod-3 structure; proved). If 3 does not divide S and 3 divides M, every candidate constraint whose vertical gap Y is prime to 3 has delta ≡ 0 (mod 3). For M = 3 that means delta = 0 (it forbids xi_e = xi_f). Equivalently, every constraint with delta not ≡ 0 (mod 3) comes from a pair with 3 | Y.

CONDITIONAL STATEMENT D (heuristic, not proved). Assume an explicit equidistribution hypothesis (H-EQ) for Hilbert partner row offsets. Then, at fixed S, the labels with |2T+1| in [h^0.6, h^0.7] induce a candidate subgraph of average degree >= c (log h)^2 / S. In that case every degeneracy or greedy argument on this placement needs M >= c' (log h)^2 / S, so S*M >= c'(log h)^2 and the width is at least h^2 (log h)^2. That is worse than the current 1.3108 exponent.

NOT PROVED: bounded M at fixed S for all P factors; any obstruction to bounded M at fixed S; any full-board statement.

## Proofs

1. PROOF OF THEOREM A.
H_{2q} lists four quadrants:
- Q1 = (y, x), the lower-left square, transposed;
- Q2 = (x, y+q);
- Q3 = (x+q, y+q), a pure translation into the upper-right square;
- Q4 = reflected.
Every aligned block of side B is the image of one rank interval of length B^2 (placement note, Section 1). This gives contiguity.

Induct downward from the top square, whose orientation is id. Suppose a diagonal block of side 2B has orientation g in {id, swap}. Both id and swap fix the lower-left and upper-right corners of the 2x2 child grid. So its two diagonal children are:
- the local Q1 child, with orientation g∘swap;
- the local Q3 child, with orientation g.
Both lie on the global main diagonal, and both orientations stay in {id, swap}. The off-diagonal children (Q2, Q4) are not main-diagonal blocks. The two diagonal children of one parent have orientations g∘swap and g, which are opposite.

Numerical check (validate_embed.py, Q = 2048, B = 2..128): every main-diagonal block is id or swap, and both kinds occur.

2. PROOF OF COROLLARY A1.
Place D_I with origin (IB, IB). Global rows are local rows plus 2IB, so every row difference is local. Global rank difference equals local rank difference by contiguity. So X, Y, L and delta are the same as in G_B^o.

Local odd rows lie in [1, 2B-1] and even rows in [2, 2B]. So Y <= 2B-1 and L = (u+w)/2 with uw = Y^2, which gives L <= (Y^2+1)/2 < 2B^2. Global completion rows are 2IB + (s ± L)/2 with 3 <= s <= 4B-1. They lie in [1, h] whenever
  B^2/2 <= IB <= (h - B^2 - 2B - 1)/2.
For h >= 2B^2 + 8B + 1 this interval has length >= 3B. It therefore contains IB and (I+1)B for a sibling pair {I, I+1} with I even. By Theorem A that pair has both orientations. The block is inside the real label grid, and L <= h-1.

Genuine rival: the owner of the completion rows exists because every label is kept. It is outside D_I, so its rank is outside the block's rank interval. Columns increase strictly with rank, so the owner's column is outside the block's column hull. The midpoint column (x_e + x_f)/2 lies strictly inside that hull and is an integer because S is even. Both completion rows are integers because s and L are odd. By the argument of the two-choice and residue notes, the tilted and axis rectangles then have the same presentation whatever the fillers.

(i) follows because a subsystem of genuine rivals with no solution leaves no valid assignment at all. (ii) follows because degeneracy is monotone under taking subgraphs.

Code check: at h = 4096, M = 3, S = 32, I brute-forced the global in-strip P constraints inside a mid-strip diagonal block of side 32 for each orientation, with the owner outside the block. They match G_32^o exactly: 229 constraints (id, I = 24) and 216 (swap, I = 25).

3. THEOREM B (computation: diag_fast.py, core_sat.py, numba plus pysat CaDiCaL).
G_B^id at S = 32, M = 3:

| B | constraints | average weighted degree | weighted degeneracy |
|---:|---:|---:|---:|
| 64 | 1726 | 0.843 | 2 |
| 128 | 10130 | 1.237 | 2 |
| 256 | 48419 | 1.478 | 2 |
| 512 | 250953 | 1.915 | 3 (3-core: 3134 vertices, 6197 constraints) |
| 1024 | 1205405 | 2.299 | 3 (3-core: 40136 vertices, 81898 constraints) |

G_1024^swap has 1202041 constraints, average 2.293, and a 3-core of 42125 vertices. No 4-core appears at B <= 1024.

The 3-cores at B = 512 and B = 1024 (both orientations) are SAT with three choices. Each SAT model was checked against every core constraint. Peeled vertices extend by reverse greedy.

h0(512) = 2*512^2 + 8*512 + 1 = 528385. A 3-core has minimum weighted degree >= 3, which gives b^-_U summed over U at least 3|U|/2. By (4) of the budget note, the sum of F^-_U over U is at least 3|U|/8, so B(3) >= 3/8 and M = 3 > 8B(3) fails.

Comparison runs at B = 1024:
- S = 64: average degree 0.968, no 3-core (density roughly halves as S doubles);
- M = 4: average degree 2.933, no 4-core.

4. PROOF OF LEMMA C.
Squares mod 3 are 0 and 1. If 3 divides neither X nor Y, then X^2 + Y^2 ≡ 2 (mod 3), which is not a square. So 3 | Y or 3 | X. If 3 does not divide Y, then 3 | X = Sq, and 3 does not divide S, so 3 | q = Md + delta. With 3 | M this gives 3 | delta.

Data agree: setting every choice to zero violates 48.8% of the G_1024^id constraints, which is exactly the delta = 0 share.

S = 32 and the profile stride S = 1568 = 2^5 * 7^2 are both prime to 3.

5. TESTS OF EXPLICIT RULES (rule_test.py, G_1024^id, M = 3).
Each rule violates 25% to 27% of the 1205405 constraints:
- r mod 3;
- floor(r/2) mod 3;
- base-4 digit sum mod 3;
- popcount(r) mod 3;
- (i+j) mod 3, (i-j) mod 3, i mod 3.
A uniformly random assignment violates 24.8%. Fixed low-digit and coordinate-residue rules therefore behave like random rules on this canonical h-independent test family, consistent with the residue obstructions on file.

6. DERIVATION OF STATEMENT D (heuristic).
For a label with Y0 = |2T+1|, the expected number of candidates is about 8 times the mean number of legs X ≡ 0 (mod S) with L <= h, taken over odd Y near Y0. The factor 8 counts 2 roles, 2 sides, and the 2 ranks d per gap q. This step uses H-EQ: partner rows are spread over the O(sqrt d) window like random odd numbers, on average over labels in T-windows of length >= h^(1/2).

Count the legs. Take u = g a^2 and w = g b^2 with uw = Y^2, so Y = gab. Then:
- S | X costs a factor of about 4/S (the condition is u ≡ ±Y mod 2^e);
- L <= h means g a^2 >= Y^2/(2h).
In log coordinates (l = log Y, H = log 2h, l > H/2), the admissible region has area (H - l)(3l - H)/4. For Y <= sqrt(2h) it is l^2/4.

So, in log h units, the degree is about C*(H-l)(3l-H)/S. It peaks near Y ~ h^(2/3) at about C H^2/(12 S). For Y ~ h it is only of order (log h)/S, which matches the census growth 0.17, 0.20, 0.30.

Partners shift T by at most 8 sqrt(h/(SM)), which is much smaller than h^0.6. So the band {h^0.6 <= Y <= h^0.7} contains, up to its edges, all candidate edges of its labels. That gives average degree >= c(log h)^2/S on an induced set. Then the degeneracy is >= c(log h)^2/(2S), and every peeling argument needs M above it.

Numerical check of the band shape (band_degree.py, S = 32, M = 3, mean degree):

| |T| range | h = 2048 | h = 4096 |
|---|---:|---:|
| [16, 128) | 0.43 to 0.53 | 0.73 to 0.77 |
| all labels | 0.277 | 0.342 |

The near-diagonal band is denser and grows faster than the global mean. At these sizes, pre-asymptotic effects (L >= S^2/4 + 1, q <= h/S) are strong, and the range cannot separate (log)^2 growth from log growth.

7. SCOPE.
- The suggestion of induced subgraphs with growing average factor count would refute criterion (8) only. It would not refute bounded M. An obstruction to bounded M needs, for each M, a finite subsystem with no solution in M choices. Corollary A1 reduces this to the h-independent finite family G_B^o.
- SAT of a G_B core does not certify the block, because G_B omits constraints whose owner lies inside the block. UNSAT would certify an obstruction.
- Theorem B relies on one implementation, checked against brute force only at B = 32.

## External results used

- pysat (CaDiCaL 1.5.3 backend) as a SAT solver for finite cores. Only SAT results with checked models are claimed.
- Heuristic inputs only, not used in any proof: the asymptotic sum over n <= x of tau(n^2) ~ (3/pi^2) x (log x)^2, and Shiu's short-interval bound for multiplicative functions. Neither was used as a hypothesis of a proved statement.

## Checks

Theorem A was proved by induction on the quadrant maps and checked numerically for every main-diagonal block, Q = 2048, B = 2..128. The embedding of G_B into the global system was checked exactly: brute-force global in-strip constraints with the owner outside the block equal the local system (229 and 216 constraints, both orientations, B = 32, h = 4096). The numba builder was checked against a slower pure-numpy builder at B = 512 (identical constraint count 250953). Every SAT model was checked against every core constraint. The band census reproduces the archive scale: 145141 constraints at h = 2048, against 139237 deduplicated triples in the certificate, because I count each role separately. Every script ran in under 60 s and 1 GB. Scripts are in scripts_hb1_p_rule/: band_degree.py, diag_block.py, diag_core.py, diag_fast.py, core_sat.py, rule_test.py, validate_embed.py.

## Gaps

- No bounded-M choice rule at fixed S is proved, even for the P family alone. The target of the route is not reached.
- No obstruction to bounded M at fixed S is proved. All block-system cores computed (B <= 1024, M = 3) are 3-choice satisfiable, and no 4-core appears for M = 3 or M = 4.
- Theorem B is computer-assisted, from one implementation (numba build plus a CaDiCaL check). It was checked against brute force only at B = 32, h = 4096, and needs an independent verifier before it goes into any note.
- Statement D (band density about (log h)^2/S, and the consequence that degeneracy proofs need SM of order (log h)^2) depends on the unproved equidistribution hypothesis H-EQ for Hilbert partner offsets. I did not prove even an unconditional lower bound on the global average degree (about (log h)/S heuristically).
- G_B^o deliberately omits constraints whose completion owner lies inside the block. SAT results for these cores therefore certify nothing about full blocks.
- Off-diagonal blocks, with offset T0 of order B^{1+theta} and theta near 1/3, are heuristically slightly denser than diagonal ones. Their systems depend on T0 and h, and I did not compute them.
- Lemma C only shows that, for 3 | M, the delta = 0 constraints are exactly a graph-coloring problem. It does not resolve that coloring problem.
- Mixed supports, cross-parity right angles, the sea, collars and gluing are untouched.

## Missing estimate

Unconditional lower or upper bounds for the average degree and degeneracy of G_B^o as B grows. The predicted order is (log B)^2/S. Equivalently, an equidistribution lemma for the rank-gap-d partner offset (j_{H(r-d)} - i_{H(r)}) over labels on short diagonal windows. That lemma would make Statement D a theorem. A sufficiently dense G_B core with no solution in M choices would give the actual obstruction to M choices.

## Next steps

- Push the exact block test to B = 2048..8192: build G_B^o in chunks across runs of under 60 s each, take the M-core, and run SAT. Any UNSAT core is, by Corollary A1, an obstruction to M choices at every h >= 2B^2 + 8B + 1, and it extends the two-choice obstruction to M = 3. Add the omitted owner-in-block constraints as conditional clauses to test full blocks.
- Prove the partner-offset equidistribution lemma using the quadrant self-similarity. Pairs between Q2 and Q3 of a 2B-block at the same local position are pure translations with y = 2T+1, and their diagonal counts have an exact tent profile |((t mod 2B)) - B|*(Q-|t|)/(2B). This would make Statement D unconditional and show that degeneracy methods at fixed S fail for every bounded M.
- Test the design suggested by Statement D. Split labels into dyadic bands by |T| (h/2^{k+1} <= Y < h/2^k) and Hilbert-order each band as its own strip, with stride S_k proportional to k log h. The heuristic cost is h^2 log h * M, compared with h^2 (log h)^2 for uniform stride. This needs a new separation argument for strip-ordered bands, an upper bound on dense cores (no divisor-rich clusters, perhaps through short-interval divisor bounds), and the mixed-support theory at S of order log h.
- Use Lemma C with residue-split sub-profiles (row steps divisible by 3, a stride prime to 3, and b0 - a0 not ≡ 0 mod 3). On two thirds of the row pairs, the P problem becomes a pure proper 3-coloring of the delta = 0 candidate graph. Compute its chromatic behavior on G_B before investing further.

