# Census of the actual H7 block systems

14 November 2026. Problem 001. Continues CONTINUATION_REPORT.md of this folder. Nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result (computational): the first census of real H7 blocks (S = 6272, row step 28, sigma = 1). P is exact up to h = 2 x 10^6 in a mixed block and 10^6 in a zero-residue block, R2s exact up to 4 x 10^5 and sampled at 10^6. Every nonempty system with M = 2 or 3 has weighted degeneracy exactly 2 and an empty 3-core; M = 2 always works (exact certificate), M = 1 always fails. Mean incidence is at most 0.03 and R2s is 10 to 100 times sparser than P. The data cannot test the growth term of (G) at reachable heights.

# Result

## Status

partial

## Summary

I ran the first census of the actual H7 block systems (S = 6272, row step 28, sigma = 1) for P and R2s. P was exact up to h = 2*10^6 in a mixed block and 10^6 in a zero-residue block; R2s was exact up to h = 4*10^5 and sampled at 10^6. In every nonempty system with M = 2 or 3, P and P u R2s have weighted degeneracy exactly 2 and an empty 3-core. M = 3 always works by peeling. M = 2 always works (exact certificate). M = 1 always fails, because P is nonempty. The systems are very sparse: mean incidence is at most 0.03 and maximum incidence at most 7. R2s is 10 to 100 times sparser than P. The data are consistent with (G) with c0 = 2, but they cannot test the c1 term, because (k+1) log h / S_k <= 0.0023 at every reachable height.

## Statements

Proved short claims (proofs in the proof field). These use the H7 block conventions: odd label rows a = 17 + 28 i, even label rows b = BRES + 28 j, S = 6272, x_e = S(M r_e + xi_e), and labels with both rows in the bulk [lo, h - lo].

(L1) Band completeness in an H7 block. For a candidate pair (r, r + d) in cross-parity role 1, the row difference equals c + 28(T_e + z), where c = BRES - 17, T_e = j_e - i_e and z^2 < 16d. Role 2 gives -c + 28(-T_e + z'). So for each Pythagorean row gap Y, the earlier labels that can be hit lie on the diagonals T_e in [(+-Y -+ c)/28 - isqrt(16d - 1), (+-Y -+ c)/28 + isqrt(16d - 1)].

(L2) P length floors at sigma = 1, for every choice vector.
- In a mixed block (7 does not divide c), every P witness has L >= 2^12 + 7^4 = 6497.
- In a zero-residue block (7 | c), every P witness has L >= 2^12*7 + 7 = 28679.
- If M >= 2 and xi_e = M r_e (mod 2) for every e, the floors become 2^14 + 7^4 = 18785 (mixed) and 2^14*7 + 7 = 114695 (zero).
- So P is empty when h - 1 is below the floor. The smallest L actually attained per class mod 28 up to 2*10^6: class 13: 6497; class 11: 18785; class 7 (zero): 29015; class 9: 32485; class 5: 39265; class 3: 71467; class 1: 84461.

(L3) Exact R2s parametrization. Take A = (0, y), B = (u, s), C = (X, y + delta), D = (X + v, s), with m = s - y, delta = 28*Delta and N = delta(2m - delta). Under the bulk hypothesis (lo > max(783, 2F)), these four points are the support of a mixed pair with side AB and diagonal CD (Lemma mixedeq) if and only if all of the following hold:
- delta is not 0 and N is not 0;
- there is a signed divisor p of N, with q = N/p and u = (q - p)/2 a nonzero integer dividing m*delta;
- t = -m*delta/u is even, and X = (t - p)/2, v = u + p;
- the common-corner rows y + delta/2 and s + delta/2 lie in [1, h].
Each solution arises from exactly one p. Sea blackness adds type(u mod 7) = type((X + v) mod 7) = s.

(L4) 7-adic restriction on R2s. Assume 49 | X (true at every stride 6272 * 2^a). If 7 does not divide m, then 7 | Delta. In H7 blocks 7 does not divide m for every role except (odd label, s = L), and also (even label, s = L) in zero blocks. In particular every R2s support with sea row F has 7 | Delta.

(L5) Hilbert precondition. If the partner f of e has coordinate offset Delta and |q'| = |X|/S, then |q'| >= 1 + M*floor(Delta^2/16) >= 1 + floor(Delta^2/16), so |X| > delta^2/2.

(L6) Exactness of the choice tests.
- The system is solvable with M values if and only if every component of its weighted M-core is solvable.
- For M = 2, each constraint forbids one or two value pairs, so solvability is exactly 2-SAT.
- M = 1 suffices if and only if the M = 1 system is empty.

Finite census results (exact integer arithmetic; P and R2s only). For M in {2, 3}, every nonempty P system and P u R2s system measured has weighted degeneracy exactly 2. M = 3 is certified by peeling, M = 2 by an explicit verified assignment, and M = 1 fails in every block at every h >= 2.5*10^5. The ranges are:
- P: blocks (17, 8) (class 9), (17, 4) (class 13) and the zero block (17, 24), for h in {2.5*10^5, 5*10^5, 10^6}, plus h = 2*10^6 for class 9. The zero block at h = 10^6 with M = 2 was not completed.
- R2s and P u R2s: h <= 4*10^5 in the class-9 and zero blocks.
- P on 6 tiles of the multilevel tiling at h = 10^6.

Nothing here is a statement for all h, and nothing about (G) is proved.

## Proofs

SETUP AND DEFINITIONS (stated so that the counts can be reproduced)

Blocks. Odd label rows a = 17 + 28i and even label rows b = BRES + 28j, with i, j >= 0 and rows in [1, h].
- BRES = 8 gives the mixed block of the toy and pt_census, with c = -9 (class 9).
- BRES = 4 gives a mixed block with c = -13 (class 13), one of the classes richest in P.
- BRES = 24 gives the zero-residue block, with c = 7.
- Bottom indexing: the Hilbert square side Q is the least power of two >= the number of class rows in [1, h], and r is the Hilbert rank of (i, j). I used the standard low-bit-rotation curve of pgraph.py and checked xy2d(d2xy) and the locality bound exhaustively for Q = 64, 128.
- Labels are the (i, j) with both rows in the bulk [lo, h - lo]. This is a subset with the original ranks, as H7 prescribes. lo = 10^5 = C1 unless stated otherwise.

Sea (for R2s). L = 3, F = 2015, H = the largest row <= h with H = 18 mod 28. These satisfy the mod-28 conditions of H7 (L = F = a + 2, H = b + 2 mod 4, normalized rows 0, 3, 1) for BRES = 8 and 24. The column type is F if 7 | x, L if x mod 7 is in {3,5,6} and H if x mod 7 is in {1,2,4}, relative to the label columns (all 0 mod 7).
- The reflected rule (L on {1,2,4}) gives identical R2s counts at h = 2.5*10^5 and 4*10^5.
- The specific F and H that AP4's filters would pick are unknown to me. I did not run R2s for BRES = 4, because its sea normalization needs lambda = 5 and the reflection choice is ambiguous.

P is defined exactly as in scripts_hb1_census/pgraph.py. Take an odd point of one label and an even point of the other with X = S q', X^2 + Y^2 = L^2, L <= h - 1 and completion rows (y1 + y2 -+ L)/2 in [1, h]. The constraint (r, r + d, delta) with q' = Md + delta forbids xi_{r+d} - xi_r = delta.

R2s is defined by Lemma S5 and Lemma mixedeq. A sea point of type s counts as black even when its column is a slot column. This is a superset, and no witness found has such a column. Being in-window is not required, which is also a superset.

PROOFS

L1. In role 1 the row difference is (BRES + 28 j_f) - (17 + 28 i_e) = c + 28(j_f - i_e) = c + 28(T_e + z), with z = j_f - j_e. The audited Hilbert locality bound gives z^2 < 16d. Role 2 is the same computation with z' = i_f - i_e. QED.

L2. We have (X/2)^2 = 2^{2v2(X)-2} * 7^{2v7(X)} * (rest) = ab, with a + b = L odd and b - a = Y.
- Exactly one of a, b is even, and it carries the whole 2-part, which is at least 2^12 because v2(6272) = 7.
- Mixed block: 7 does not divide Y = b - a, so 7 does not divide both a and b. Since 7^4 | ab, the whole 7^4 sits in one factor. If it sits in the even factor, L > 2^12 * 7^4. Otherwise L >= 2^12 + 7^4.
- Zero block: 7 | Y and 7 | ab, so 7 | a and 7 | b. Then the even factor is at least 2^12 * 7, the odd factor is at least 7, and L >= 28679.
- Parity choice: if every slot position M r + xi is even, then 2S | X, so v2(X) >= 8 and the 2-part is at least 2^14. The same argument gives the floors 18785 and 114695.
- The per-class minima come from trip_scan.py. QED.

L3. Put B - A = (u, m), D - C = (v, m - delta) and C - A = (X, delta). Lemma mixedeq asks for an integral n with:
- n.(B - A) = 0, where 2n = C + D - A - B = (t, delta) and t = 2X + v - u;
- |D - C| = |B - A|;
- D - C != +-(B - A).
These conditions are equivalent to:
- (a) u t + m delta = 0;
- (b) v^2 - u^2 = N;
- (c) t and delta even;
- (d) non-degeneracy.
Put p = v - u and q = v + u. Then pq = N, u = (q - p)/2, t = 2X + p, so X = (t - p)/2.

The excluded cases:
- u = 0 puts B in A's label column, so B is not a sea point.
- delta = 0 forces v = +-u and t = 0. Then v = u gives X = 0 (C = A), and v = -u puts D in A's column. So delta is not 0.
- delta = 2m puts C at row 2s - y. For s in {L, F} this row is < 0, and for s = H it is > h - lo, whenever lo > max(783, 2F). This is (Bulk).
- So N is not 0, p ranges over the signed divisors of N, u | m*delta, and each solution comes from one p.
- (d) holds automatically, because m - delta = +-m would force delta = 0 or 2m. QED.

L4. All label columns are 0 mod 7 and 7 | delta.
- s = F: the sea types force u = v = 0 (mod 7). So 49 | (v - u)(v + u) = N. Since 7 does not divide 2m - delta, this forces v7(delta) >= 2.
- s in {L, H}: u is not 0 mod 7. Mod 7, (b) gives v = +-u, and (a) gives u(v - u) = 0 (mod 7), so v = u. Suppose v7(delta) = 1, and write delta = 7 delta'. Then v7(t) = 1, and P = u - v = -N/(u + v) has v7(P) = 1. Mod 7, t/7 = -m delta'/u and P/7 = -delta'(2m)/(2u) = t/7. So (P + t)/7 = 2t/7, which is not 0 mod 7. But 49 | 2X = P + t, a contradiction.
- So v7(delta) >= 2, that is, 7 | Delta.
- The m residues come from the normalized rows: L, F, H are rows 0, 3, 1, and the label rows are 0 and 5 (mixed) or 0 (zero).
- check_prune7.py found no violation in 8,502 unpruned solutions. QED.

L5. Locality gives Delta^2 < 16d. And |q' - Md| <= M - 1 gives |q'| >= M(d - 1) + 1. QED.

L6. This is the peeling argument T5 of hilbert_p_census.md, applied with the M-core taken first. For M = 2, each constraint xi_b - xi_a != delta forbids the pairs (x, x + delta) inside {0,1}^2, which are 2-clauses. QED.

VERIFICATION OF THE CODE
- P band method against an all-pairs brute force: identical constraint sets at 8 settings. These include S = 6272 at h = 9*10^4 and 10^5 (22,524; 30,487; 13,963 constraints) and smaller strides 784, 1568, 3136 in both block types.
- R2s divisor enumeration against an independent loop over every u with |u| <= (|N|+1)/2: identical at 10 settings.
- Every R2s witness at h = 2.5*10^5 (M = 3, 808 witnesses) and h = 2*10^5 (M = 2, 4,069 witnesses) was rebuilt from the ranks and checked against mixedeq, the types, the strip and Hilbert locality. Zero failed.
- The exact solvers agree with brute force on 300 random small systems. Every final assignment was checked against all constraints.
- The tile code, run on the whole block square, reproduces the block census exactly (37,209 P, 809 R2s, 38,018 union).
- The parallel and serial R2s kernels agree.

MEASUREMENTS
Notation: E = number of constraints, mi = mean incidence 2E/labels, mx = maximum weighted incidence, deg = weighted degeneracy. A system is "solved" when M values suffice.

P, lo = 10^5, labels 3.19e6 / 1.15e8 / 8.16e8 / 4.1e9 at h = 2.5e5 / 5e5 / 1e6 / 2e6.

Class 9 (BRES = 8):
- h = 2.5e5: M=1 E=3553, mi 0.0022; M=2 E=7356, mi 0.0046, mx 4, deg 2, solved; M=3 E=6416, mi 0.0040, mx 4, deg 2, solved.
- h = 5e5: M=1 94,576 (0.0016); M=2 203,162 (0.0035); M=3 141,778 (0.0025).
- h = 1e6: M=1 656,449 (0.0016); M=2 1,340,109 (0.0033); M=3 957,674 (0.0023).
- h = 2e6: M=1 3,897,205 (0.0019); M=2 6,919,013 (0.0033), 2-core 418,607; M=3 5,428,260 (0.0026), 2-core 299,647, mx 4.

Class 13 (BRES = 4):
- h = 2.5e5: M=1 6068 (0.0038); M=2 8653; M=3 6265 (2-core 24).
- h = 5e5: M=1 293,469 (0.0051); M=2 459,178 (0.0080); M=3 378,135 (0.0066).
- h = 1e6: M=1 1,773,063 (0.0043); M=2 2,656,389 (0.0065; greedy stuck on 124 labels, peeling solved it); M=3 2,437,048 (0.0060).

Zero block (BRES = 24):
- h = 2.5e5: M=1 21,497 (0.0135); M=2 43,282 (0.0271); M=3 37,209 (0.0233).
- h = 5e5: M=1 1,029,554 (0.0179); M=2 1,831,348 (0.0319); M=3 1,692,009 (0.0295).
- h = 1e6: M=1 7,797,149 (0.0191, mx 4, deg 1); M=3 11,935,618 (0.0292, mx 5, deg 2, 2-core 1,130,987).

Every M = 1 system has degeneracy 1 (a forest). Every M = 2, 3 system has degeneracy 2 and an empty 3-core.

R2s, lo = 10^5.
- Class 9: row candidates 12, 20, 22, 35 at h = 2.5e5, 3e5, 3.5e5, 4e5. All are (odd, F) except one (odd, L) at 4e5. R2s constraints for M = 1/2/3:
  - h = 2.5e5: 587 / 276 / 808;
  - h = 3.5e5: 1795 / 2395 / 3155;
  - h = 4e5: 2818 / 7723 / 6126.
  mi is between 1.1e-4 and 5.1e-4, mx <= 4, and deg is 1 except M = 2 at 4e5 (deg 2).
- Zero block: 14 candidates at 2.5e5 and 39 at 4e5 (34 OF, 1 OL, 4 EF). At 4e5, M = 2, P u R2s has 736,087 constraints, mx 7, deg 2, a 2-core of 76,114, and the exact 2-SAT on the 2-core is satisfiable.
- In every P u R2s system: deg 2 for M = 2, 3, and M = 2, 3 solved.
- lo = 10^4 series (class 9): candidates 8, 20, 30, 44 and mi(M=1) 1.5e-4, 1.4e-4, 2.1e-4, 1.7e-4 at h = 5e4, 1e5, 1.5e5, 2e5.
- Sampled at h = 10^6: 0.0033 candidates per odd row (8 in 2,400 rows), none in even rows. Per-row density is about 0.003 throughout, nearly flat in the distance |m| to the F row.
- All candidates have |Delta| <= 126, small |u| (7 to 203, plus one L case with 6625), and no slot-column sea point.

Tiles (h = 10^6, zero block, P only, M = 3 unless noted).
- Level 1, square [0, 32768)^2 with |j - i| in [16384, 32768), S_1 = 12544, 1.49e8 labels:
  - M=1: 227,974 (mi 0.0031);
  - M=2: 455,452 (0.0061), deg 2, solved;
  - M=3: 357,610 (0.0048), deg 2, 2-core 46,293, solved;
  - class 9 at M=3: 54,804 (0.0007), deg 2.
- Level 2, next to the diagonal, [0,16384) x [16384,32768), S = 25088: empty.
- Level 3, [8192,16384)^2: empty. Level 3, [16384,24576)^2: 25,209 (0.0030), deg 2, solved.
- Level 4, [8192,12288) x [12288,16384), S = 50176: empty.

Band profile of P (zero block, h = 10^6, M = 3). Mean incidence by |T| = |j - i|:
- [16, 64): 0.032;
- [64, 256): 0.038;
- [256, 1024): 0.050;
- [1024, 4096): 0.042;
- [4096, 8192): 0.037;
- [8192, 16384): 0.019;
- [16384, 32768): 0.017.
The peak sits near |b - a| ~ h^(2/3) and is about 2.8 times the far-band value. Class 9 at 2*10^6 shows the same shape (0.0048 against 0.0017).

First-moment model (heuristic). Each triple, choice gap, and matching role and sign contributes its number of admissible earlier-label rows. Measured/predicted ratios at 8 checked points are 0.83 to 1.01, for example 1.006 for the zero block at 10^6, M = 3. Predictions for the zero block at M = 3:
- mean 0.029, 0.048, 0.059, 0.072 at h = 1e6, 1e7, 4e7, 1.6e8 (rho = h/S^2 = 0.025 to 4.07), a slope of about 0.009 per unit ln h;
- the |T| in [1024, 4096] band: 0.045, 0.106, 0.159, 0.215, about 3 times the mean and growing faster.

WHAT THE NUMBERS SUGGEST FOR (G)

Here is what I read from the data. None of it is proved.
- At sigma = 1, the base block (k = 0) has c0 = 2: degeneracy is 2 whenever M >= 2. The c1 term is invisible, because (k+1) log h / S_k <= 0.0023 at h <= 2*10^6, and the model keeps the mean and peak-band first moments below 0.25 up to h = 1.6*10^8. So the reachable data cannot distinguish (G) from the band-excess alternative (degree ~ (log h)^2/S). The model's band peak grows faster than its mean, which is consistent with that excess.
- With mean degree << 1, what decides M is the cycle structure of the 2-core, not counting. Increasing-rank greedy fails at M = 2 in a few cases, while peeling and 2-SAT succeed.
- R2s does not bind here. It is a single structured subfamily (O-F, small u, 7 | Delta), whose per-row density stays flat at about 0.003 from h = 5*10^4 to 10^6, with no growth with h visible.
- On the multilevel tiles the larger strides make P even sparser, and the per-tile degeneracy is <= 2.

script folder (all scripts; under 7 MB): scripts_hb2_census_h7/
- Builders: h7common.py, p_h7.py, r2s_h7.py, r2s_par.py, tile_h7.py.
- Analysis: analyze_h7.py.
- Run drivers: run_p.py, run_r2s.py, r2s_sample.py, r2s_density.py.
- Checks: p_brute.py, r2s_brute.py, check_prune7.py, check_r2s_sound.py, test_analyze.py.
- Profiles and model: p_profile.py, p_first_moment.py, p_fm_large.py, trip_scan.py.
- Small outputs: out/.

## External results used

- Hilbert locality max(Delta i^2, Delta j^2) < 16 |Delta r| on a 2^k x 2^k Hilbert square (Placement Theorem 1, continuation_hilbert_placement.md, audited). I used it for band completeness and the R2s Hilbert precondition, and checked it numerically for Q = 64, 128.
- Lemma mixedeq (papers/extremal/sections/sec2_prelim.tex). A mixed pair with side AB and diagonal CD has an integral n perpendicular to B - A with C + D = A + B + 2n, |D - C| = |B - A| and D - C != +-(B - A). The common corners are A + n and B + n.
- The peeling lemma T5 and the P conventions of scripts_hb1_census/pgraph.py (hilbert_p_census.md). The H7 design and Lemma S5 (hilbert_sea_design_h7.md, unaudited). Hypothesis (G) and design C4 (hilbert_round1_synthesis.md, unaudited).

## Checks

I checked by hand: the L1 band derivation, the L2 2-adic and 7-adic floors with their per-class minima, the L3 equivalence (including exclusion of delta = 0 and delta = 2m under the bulk condition), the L4 7-adic argument, the L5 inequality, and the L6 reductions. By computer, each run once, one script at a time, each under 60 s and 1 GB, with py -B:
- P band against brute force: identical at 8 settings, 3 of them at S = 6272.
- R2s fast against brute force: identical at 10 settings.
- 7-adic lemma: 0 violations among 8,502 unpruned solutions.
- R2s witnesses rebuilt from coordinates: 4,877 witnesses, 0 failures.
- Exact solvers against brute force: 300 random systems, 0 mismatches.
- Tile code against the block census: exact match.
- Parallel against serial kernels: equal.
- Sampler against the full census: equal mean incidence at h = 3*10^5.
- First-moment model against measured counts: ratios 0.83 to 1.01 at 8 points.
Every final choice assignment was verified against all constraints. The repository rectangle-blackouts was only read, and no git command was run.

## Gaps

- Nothing asymptotic is proved. Degeneracy 2 and M = 2 or 3 solvability are checked only for h <= 2*10^6 (P, mixed), 10^6 (P, zero) and 4*10^5 (R2s exact). All of these lie at rho = h/S^2 <= 0.05, far below the regime where the counting term of (G) could matter.
- Families FW, 6PT, Lambda3 and Lambda4 were not counted, so this is not a test of the weighted hyper-degeneracy in (G). The occupancy dependence (slot columns holding F) was handled as a superset, and no R2s witness used a slot column.
- Sea rows: F = 2015 and H = the largest row = 18 mod 28 were chosen as in pt_census, not by AP4's filters, which are unaudited and were not rerun. R2s was run only for blocks (17,8) and (17,24). The L/H column rule has a reflection ambiguity, and the reflected rule gave identical counts at two heights.
- Only 3 of the 196 blocks were run: one per class 9, 13 and the zero class. Class 7 (zero blocks) is the richest in P (876 of the 1458 triples up to h = 2*10^6), so the zero block is the worst case found. The other mixed classes (1, 3, 5, 11) were not run.
- Bottom indexing of the Hilbert square was used. Bulk-relative indexing is also consistent with H7 and would change the ranks. Bulk margin lo = 10^5 (C1), plus lo = 10^4 for one R2s series.
- The P definition is copied from pgraph.py (in-strip vertical completion only). I did not rederive it from Lemma rival.
- Zero block, h = 10^6, M = 2 was not completed (over 60 s and a 53 MB file).
- Tiles: P only (R2s not run on tiles), 6 tiles at h = 10^6, under the C4 alignment convention as I read it.
- The first-moment model, the band-excess reading and all extrapolations are heuristic. The model is validated only to within 0.83 to 1.01 at 8 measured points.
- L3 and L4 are new and unaudited, though they were checked by independent brute force and by 8,502 unpruned solutions respectively.

## Missing estimate

To make (G) a usable hypothesis at sigma = 1 (k = 0, S = 6272), the missing statement is structural, not a degree count. The census data imply nothing for larger h. In every H7 block, the weighted 2-core of the P u R2s candidate multigraph would have to have no 3-core (that gives M = 3 by peeling), or every 2-core component would have to satisfy its 2-SAT instance (that gives M = 2), uniformly in h. A proof needs a description of how cycles arise in that 2-core, for example multiple choice gaps on one pair, or triangles closed by shared half-factors. The divisor-rich triples behind the band excess near |b - a| ~ h^(2/3) would have to be controlled to that end. For R2s, the dominant (odd, F) small-u subfamily (u = 7k, v^2 = u^2 + N, 7 | Delta, |Delta| <= 126 observed) needs a per-label bound uniform in h. A heuristic suggests that per-row density stays bounded and the per-label incidence of labels near the bulk edge grows at most like (log h)/C1. That heuristic is unproved.

## Next steps

- Classify the weighted 2-core of the zero-block P system at h = 10^6, M = 3 (1.13M vertices): its cycle types, which half-factor and choice-gap patterns close the cycles, and whether every component is a cycle with pendant trees. This would explain the degeneracy 2.
- Run the 11 remaining residue classes, including the other mixed classes 1, 3, 5 and 11 and a second zero block, at h = 10^6 for P, and complete the zero block at M = 2 in split runs, saving only the 2-core.
- Prove a uniform per-label bound for the (odd, F) R2s subfamily, using L3 with small u = 7k and the square condition v^2 = 49k^2 + N. Check whether |Delta| <= 126 is forced by a 2-adic argument.
- Audit L3 and L4, and fix the AP4 sea rows (rerun verify_filled_mod7_profiles with the mod-28 conditions) before rerunning R2s with the true F and H.
- Add FW and 6PT (all occupancy states) to the same multigraph to test the full hyper-degeneracy that (G) refers to.
- Use the validated first-moment model to locate the h at which the band-peak P degree reaches 1 at S = 6272. That gives the first height at which (G)'s c1 term could be tested by computation.

