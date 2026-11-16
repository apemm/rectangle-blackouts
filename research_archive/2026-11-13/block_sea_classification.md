# Obstructions with a row-1 sea in the block scaffold

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Not audited yet.

# Result

## Status

partial

## Summary

Sea for the stride-4 block scaffold: I proved a complete list of the obstructions that contain a row-1 sea point. Three facts follow. A row-1 sea is not free inside constant-offset blocks. X2, the main intra-class family, disappears when each class is split by v2(i) mod 3. Every single-row deep sea fails against a parabolic forbidden-offset rule.

## Statements

Setting. Strip Z x {1..h}. The parity bipartition. Doubles have distinct parity edges, and every other column is a singleton. SHALLOW points: Sh = {(x,1) : x != 0 mod 4}, all black. DEEP points: every other black point, which by assumption lies in a column = 0 mod 4. These are the label points (column 4n, n = i + Pc) and the fillers (singletons in columns = 0 mod 4). Deep points may lie in row 1, as the odd point of a label with i = 0 does.

(0) CRITERION. Assume all parity edges occur as doubles and h, m >= 4. Then S is valid iff all five of the following hold.
 (V1) No tilted rectangle is fully black.
 (V2) Let a tilted rectangle have exactly 3 black corners. Then its white corner W lies in a column whose black points all have the parity of row(W) ("parked").
 (V3) No two tilted rectangles parked at the same W.
 (V4) No mixed quadruple is black.
 (V5) No rival pair is black.

(A) EARLIER DERIVATION: verified, with one correction. The equation u(10t1 - T0) = Ds(T0 - 2t1) - 8 t1 P Dc is correct. So are u = -Ds + 8 t1 N/(10t1 - T0) with N = Ds - P Dc, and the integrality criterion m = |10t1 - T0|/gcd(T0,t1) divides N. The correction: R = P + Q - V lies in column 4(iQ + t1 + P c'), but its row is 2(iQ + t1 + Ds) + 1, not the odd row of that slot. Consequences:
 - Slot iQ + t1 occupied: R is black iff Ds = 0, and then the rectangle is fully black (fatal). If Ds != 0, R is white in a double column (fatal).
 - Slot empty, with an odd filler in row r: fatal iff r = row(R). Otherwise the triple is parked.
 - If row(R) is outside 1..h, no rectangle exists.

(B) THEOREM 1 (corner triples with a shallow point). Let a tilted rectangle have at least 3 black corners, at least one of them shallow. Then exactly one black corner E is shallow, the other two black corners F and G are deep and not in row 1, and the fourth corner W is white. W lies in a column != 0 mod 4, whose only black point is in row 1. So no fully black tilted rectangle has a shallow corner. Exactly one of the following holds:
 (Pa) E is the vertex, x_E is odd, F and G are in even rows, and W is in an odd row: parked.
 (Pb) E is the vertex, x_E = 2 mod 4, and the rows of F and G are = 3 mod 4: parked.
 (X1) E is the vertex, x_E = 2 mod 4, F is in an even row, and G is in a row = 5 mod 8. W is in an even row: FATAL. For given F and G, this happens iff y_F + y_G - 1 <= h and |x_F - x_G|/2 = d + M/d for a divisor d of the odd number M = (y_F-1)(y_G-1)/4. There are at most 2 choices of E.
 (Pc) E is an end, V is the vertex, the other end is G, and y_G - y_V is even: parked.
 (X2) E is an end, the vertex V has y_V = 1 mod 4 and y_V >= 5, and G is in an even row with y_G > y_V: FATAL. This happens iff a = (y_V - 1)(y_G - y_V)/(x_G - x_V) is an integer with a != 0 mod 4, and then E = (x_V + a, 1).

(C) THEOREM 2 (mixed quadruples with a shallow point). Write the support as (A,B,C,D), with AB the side and CD the diagonal. Its shallow points are one of the following:
 - {A,B} (M2a);
 - one of A,B together with one of C,D (M2c);
 - exactly {C} or exactly {D} (M1C).
 The sets {C,D}, {A,B,C}, {A,B,D}, {A}, {B} and all 4 points never occur. Rival pairs never contain a shallow point.
 M2a: for deep C and D this happens iff y_C = y_D mod 2, y_C != y_D, L = |D - C| is an integer, and either L = 2 mod 4, or L = 4 mod 8 and 8 divides x_D - x_C. In particular it never happens when y_D = y_C mod 8.
 M2c (A and C shallow; B and D deep): e = (y_D - y_B)/2 is a positive integer. With Delta = x_D - x_B and u2 = y_B - 1, there is an integer n1 with n1((Delta - n1)^2 + e^2) = e u2 (Delta - 2n1). Also z = -e u2/n1 is an integer (if u2 = 0, take n1 = 0 and z = -(Delta^2 + e^2)/Delta), z != 0 mod 4, 2n1 - z != 0 mod 4, and y_B + e <= h. Conversely, any such data with D - C != ±(B - A) gives a mixed quadruple.
 M1C (only C shallow): x_C = 2 mod 4. A and B are in even rows with y_B - y_A = 2 mod 4. D is in a row = 1 mod 4.

(D) COROLLARY (fillers). If every filler lies in a row = 3 mod 4, then no X1, X2 or M1C contains a filler. In one constant-offset class:
 (D1) M2a never joins two label points.
 (D2) X2 does occur. Example: T = 1, slots 4 and 6. Every intra-class X2 pair has v2(i) - v2(i') in {1,2}. So splitting each class by v2(i) mod 3 removes all intra-class X2.
 (D3) X1 occurs (T = 1, slots 2 and 6). M2c occurs. One scaled family has y_B - 1 = 5t, D = B + (4t, 2t), t != 0 mod 4, and there are sporadic solutions.
 So the remark in stride_menu.md that a row-1 sea is free inside blocks is false.

(E) PROPOSITION 3 (pure seas). For every h >= 2 and every row r > (h+1)/2, Sea(1,r) = Sh ∪ {(x,r) : x = 0 mod 4} contains no tilted rectangle with 3 or more black corners, no mixed quadruple and no rival pair. So it is a valid gap sea, and it has no parked triples.

(F) PROPOSITION 4 (one-label family at the deep level). Let the fillers lie in one row r. A deep point D in column c and row r ± 2k, together with fillers at c - u, c + v - u, c + v (uv = k^2, u != v), is a black mixed quadruple. This needs 4 | k.
 Rule: suppose all block offsets P c are even. If every empty slot m = (r-1)/2 mod 2 takes a row other than r, this family is empty for every label odd point. The hole row rho has no such family of its own iff rho = r + 2 mod 4.

(G) PROPOSITION 5 (forbidden offsets). Let D be a black deep point and k >= 1. Then the 4 points D + (±4k(k+1), ±(4k+2)) must all be white, because otherwise M2a gives a black mixed quadruple. Consequence: a gap sea with deep points in a fixed row r kills every label odd point at row r - 2epsilon (epsilon odd, |epsilon| >= 3) whose column x_D ± (epsilon^2 - 1) falls in that gap.

NOT PROVED: m_h = O(h^2); a sea for the blocks with load O(1) per label; any bound for the cross-class loads.

## Proofs

Notation. Point (x,y) means column x, row y. "Shallow" means (x,1) with x != 0 mod 4; all of these are black. "Deep" means a black point in a column = 0 mod 4. Every black point is shallow or deep. A column != 0 mod 4 therefore has exactly one black point, in row 1: a second black point would be deep, hence in a column = 0 mod 4. I use the paper's facts (F1) (a tilted rectangle has at most one corner in row 1), (F3), Lemma diff, Lemma mixedeq, Lemma compress and Lemma rival. I also use the audited Lemma 1 (axis owner) and Lemma 2 (no fully black tilted rectangle, h, m >= 4) of research_archive/2026-11-13/lower_bound_windows.md.

0. Criterion.
"If": let R1 != R2 have the same presentation. The case analysis follows the paper's Lemma criterion.
 - Both axis-aligned: a 4-cycle or 6-cycle in G_S, impossible for distinct parity edges, as in the paper's reduction lemma.
 - No common corner: both are fully black, and one is tilted (V1).
 - One common corner W. If W is black, both are fully black (V1). If W is white, both have exactly 3 black corners. If both are tilted, (V3) applies. If R2 is axis-aligned, R2 = {(x,rho)=W, (x,s), (z,rho), (z,s)}. Column z then holds rho and s, so {rho,s} is a parity edge and (x,s) is a black point of the other parity in W's column, against (V2).
 - Two common corners p, q. Lemma compress gives a fully black R3, which (V1) or the girth condition excludes. Otherwise the pair is mixed, and the support is a mixed quadruple (V4) or, when AB is vertical, a rival pair (V5).
"Only if":
 - (V1) is Lemma 2.
 - (V2) is the axis owner lemma, which needs every parity edge present.
 - (V3): both rectangles present {W}.
 - (V4): a black support gives equal presentations.
 - (V5): the owner double of {c-j, c'+j} together with the black rival pair is a black mixed support, as in the paper's reduction lemma.

A. Earlier derivation.
V = (4(i0+P c0), 2i0+1+T0) and P = V + (4t1, 2t1 - T0). Q = (4(i0+u+P c'), 2(i0+u)+1+T'), so Q - V = (4(u + P Dc), 2c2) with c2 = u + Ds. The dot product is 16 t1(P Dc + u) + 2c2(2t1 - T0). Setting it to 0 and expanding gives u(10t1 - T0) = Ds(T0 - 2t1) - 8t1 P Dc. Next, Ds(T0 - 2t1) = -Ds(10t1 - T0) + 8 t1 Ds, which gives the stated form of u.
10t1 - T0 is odd, so it is coprime to 8. Also gcd(10t1 - T0, t1) = gcd(T0, t1). This gives the integrality criterion.
R = P + Q - V has column 4(i0 + t1 + u + P c') and row 2(i0+t1) + 1 + 2(i0+u) + 1 + T' - (2i0 + 1 + T0) = 2(iQ + t1 + Ds) + 1. The fatal and harmless cases then follow from Lemma 2 (fully black), the axis owner lemma (white in a double column) and the criterion (V2, V3).
coord.py checked 956 integral random instances against a direct dot product and a direct computation of R: 0 failures.

B. Theorem 1.
By (F1), at most one corner is in row 1, so E is the unique black corner there. F and G are black and not in row 1, hence deep.

Case E is the vertex. Put a = x_F - x_E and c = x_G - x_E. Both are = -x_E mod 4, which is nonzero. Put f = y_F - 1 >= 1 and g = y_G - 1 >= 1, so ac + fg = 0. W = F + G - E has column = -x_E != 0 mod 4 and row 1 + f + g >= 3, so W is white.
 - x_E odd: ac is odd, so f and g are odd, F and G are in even rows, and row(W) is odd (Pa).
 - x_E = 2 mod 4: a = 2a' and c = 2c' with a', c' odd, so v2(fg) = 2.
   - (v2 f, v2 g) = (1,1): both rows are = 3 mod 4 and row(W) = 1 mod 4 (Pb).
   - (0,2): F is in an even row, g = 4 mod 8, so y_G = 5 mod 8. row(W) = 1 + odd + even is even, and the axis owner lemma makes it fatal (X1).
 Explicit form of X1: a' - c' = (x_F - x_G)/2 and a'c' = -M. So {|a'|, |c'|} = {d, M/d} with opposite signs. Conversely, each divisor d gives x_E = x_F - 2a' = 2 mod 4. The rectangle fits iff 1 + f + g <= h.

Case E is an end. Let V be the vertex and G the other end. Then E = V + (a, -f) with f = y_V - 1 >= 1 and a != 0 mod 4, and G = V + (4gamma, g) with gamma != 0 and g != 0. Perpendicularity gives 4 a gamma = f g. W = E + (4gamma, g) has column = x_E mod 4, which is shallow, and row 1 + g. W is not in row 1, so g >= 1 and W is white.
 - g odd: 4 | f, so y_V = 1 mod 4 and y_V >= 5, y_G is even, and row(W) is even: fatal (X2), with a = fg/(4gamma).
 - g even: parked (Pc).

C. Theorem 2.
Let (A,B,C,D) be the support and n the vector of Lemma mixedeq: n.u = 0 with u = B - A, C + D = A + B + 2n, |D - C| = |u|, D - C != ±u and u1 != 0. The corners p = A + n and q = B + n are grid points.

(i) C and D are never both in row 1. The diagonals CD and pq of R2 share their midpoint, which is in row 1. If pq is not horizontal, one of p, q is above row 1. If pq is horizontal, then {p,q} = {C,D}, which is impossible because C and D are not common corners.

(ii) A, B and one of C, D shallow, the other deep. Say C is shallow and D is deep; D is in a column = 0 mod 4. AB is horizontal, so n1 = 0, y_D = 1 + 2n2 and x_C = x_A + x_B - x_D. Write x_D = c, x_A = c - u and x_B = c + v. Then (u - v)^2 + 4n2^2 = (u + v)^2, so uv = n2^2 != 0.
 With j = gcd(u,v), the coprime numbers u/j and v/j have the square product n2^2/j^2, so u = j a^2 and v = j b^2 with gcd(a,b) = 1, up to a common sign.
 2-adic remark (arc note, Section 7, rechecked). If a and b are both odd, v2(u) = v2(v) = v2(j) and v2(v - u) >= v2(j) + 3. If one of a, b is even, that term has valuation >= v2(j) + 2. So one of u, v, v - u is = 0 mod 4. Then one of the columns c - u, c + v, c + v - u is = 0 mod 4, and that point is not shallow: a contradiction.

(iii) Exactly one shallow point, and it is A (the case B is symmetric).
 - Column equation mod 4: alpha + 2n1 = 0, so alpha = 2 mod 4 and n1 is odd.
 - u1 = x_B - alpha = 2 mod 4, so n1 u1 = 2 mod 4 and hence n2 u2 = 2 mod 4.
 - Lengths: (x_D - x_C)^2 + (y_D - y_C)^2 = u1^2 + u2^2. Modulo 16 the left side is 0 + s with s in {0,1,4,9}, and u1^2 = 4.
 - If u2 is odd, the right side is = 5 or 13. If u2 = 2 mod 4, it is = 8. Neither value lies in {0,1,4,9}: a contradiction.
 Together, (i) to (iii) leave only {A,B}, the mixed pairs and the singletons {C} or {D}.

M2a. Here AB is horizontal, n1 = 0, x_A + x_B = x_C + x_D and n2 = (y_C + y_D)/2 - 1, so the rows have equal parity.
 - If y_C = y_D, then D - C = ±(B - A), which is excluded.
 - With D - C = (4delta, 2eps), L = 2L' and L'^2 = 4delta^2 + eps^2. The columns of A and B are 2(n_C + n_D) ∓ L'.
 - L' odd: both columns are odd, hence shallow.
 - L' = 2 mod 4: both columns are = 2(n_C + n_D + 1) mod 4, which is nonzero iff delta is even.
 - L' = 0 mod 4: this would need delta odd, but then 4delta^2 + eps^2 = 0 mod 16 forces eps^2 = 12 mod 16, which is impossible.
 - If eps = 0 mod 4, then either L' = 2 mod 4 with delta odd, or L' = 0 mod 4. So y_D = y_C mod 8 is never fatal.
 Same class: D - C = (4t, 2t) and |D - C|^2 = 20t^2, which is never a square, giving (D1).

M2c. The row equation gives n2 = e. p = A + n has row 1 + e, so e >= 0, and e = 0 forces n = 0. So e >= 1.
 - Perpendicularity: n1 z + e u2 = 0, with z = x_B - alpha.
 - Lengths: w = D - C = (2Delta + z - 2n1, u2 + 2e) and |w|^2 = z^2 + u2^2. Put tau = Delta - n1, so w1 = 2tau + z. This gives tau^2 + tau z + e u2 + e^2 = 0, and with tau z = Delta z + e u2, tau^2 + Delta z + 2e u2 + e^2 = 0.
 - Multiply by n1 and use n1 z = -e u2: n1((Delta - n1)^2 + e^2) = e u2 (Delta - 2n1). The steps reverse when n1 != 0.
 - n1 = 0 forces u2 = 0, and then Delta^2 + Delta z + e^2 = 0.
 - Shallowness of A and C reads z != 0 and 2n1 - z != 0 mod 4, because kappa = 2x_B - z + 2n1 - x_D.
 Check: for t = 1, B = (0,6) and D = (4,8), the data A = (5,1), C = (3,1), n = (1,1) give p = (6,2) and q = (1,7). Both rectangles were verified by hand.

M1C. Column equation mod 4: kappa = 2 mod 4 and n1 is odd. u1 = 0 mod 4, so n2 u2 = 0 mod 4. Lengths mod 16: 4 + (y_D - 1)^2 = u2^2, and among squares mod 16 this forces y_D = 1 mod 4 and u2 = 2 mod 4. Then n2 is even. The row equation gives y_A + y_B = 2 mod 4, and with y_B - y_A = 2 mod 4 both rows are even.
Rival pairs: by Lemma rival, neither point is in row 1.

D. Corollary.
The filler rule (rows = 3 mod 4) follows from the row conditions in B and C.
(D2): X2 inside a class has gamma = t, f = 2i, g = 2t + T odd and a = i g/(2t). The condition v2(a) in {0,1} gives v2(t) in {v2(i) - 1, v2(i) - 2}. So v2(i + t) = v2(t), and the difference of valuations is 1 or 2, never = 0 mod 3. Example: T = 1, i = 4, t = 2: a = 5, E = (21,1), V = (16,9), G = (24,14), W = (29,6). The brute force found it, and 2 is not in D_1 (89 and 73 are not squares).
(D3): X1 example: F = (8,6), G = (24,13) and E = (18,1) give W = (14,18), with h >= 18. Here 4 is not in D_1.
M2c family: n1 = t and u2 = 5t satisfy t·10t^2 = t·5t·2t.

E. Proposition 3.
Corner triples. Two black corners in one row are opposite (F3). If they lie in row r, the centre is in row r and the fourth corner is in row 2r - 1 > h. If they lie in row 1, the fourth corner is in row 2 - r < 1.
Mixed quadruples. By (i), C and D are not both in row 1. They are not both in row r either: for A,B rows (1,1), {p,q} = {C,D}; for (r,r), n = 0; for (1,r), the mod-16 contradiction of (iii) applies, for either parity of r. So exactly one of C, D is in row 1.
 - A, B in row 1: n2 = (r-1)/2, and for odd r the 2-adic remark gives a contradiction. For even r, n2 is not an integer.
 - A, B in row r: the column of the row-1 point is = 0 mod 4.
 - A, B in different rows: n2 = 0 forces n = 0.
Rival pairs: a rival pair would need both points in row r, but its two rows have different parity.
Check: brute force at h = 12 and 17, for all r, finds no obstruction when r > (h+1)/2.

F. Proposition 4.
The family is the deep analogue of (ii). The 3 points lie in columns = 0 mod 4, so 4 | u and 4 | v; write u = 4u' and v = 4v', so u'v' = (k/4)^2.
Members are the slots n - u', n + v' - u', n + v'. One of u', v', v' - u' is even, so one member has the parity of n.
A danger needs 4 | k, so i = (r-1)/2 mod 4. With all offsets P c even, n = i mod 2, so that member is a hole slot.
For a hole row rho, all 3 members are hole slots only if u' and v' are even. Then 8 | k, so n = (rho - 1)/2 mod 2, which differs from (r-1)/2 when rho = r + 2 mod 4.

G. Proposition 5.
Take D - C = (∓(eps^2 - 1), -2eps) with eps = 2k+1. Then L'^2 = (eps^2 - 1)^2/4 + eps^2 = ((eps^2 + 1)/2)^2, and L' = (eps^2 + 1)/2 = 1 mod 4 is odd. So L = 2 mod 4, and M2a applies.
For gap fillers in row r: eps odd forces delta = (eps^2 - 1)/4 to be even, so slot n ± delta has the parity of n, which is not the hole parity of F. The point there is a row-r filler unless it is a double.

COMPUTATIONS (folder block_sea, each run under 60 s, command py). These are sanity checks, not proofs.
(1) board.py is a brute force from the definitions. It enumerates all tilted rectangles with at least 3 black corners and applies the axis owner rule, all mixed supports with a non-vertical side, and all rival pairs.
 t3.py checks Theorems 1 and 2 at h = 16 (T = 1, -1, 3, 5, -5) and h = 21 (T = 1, -1, 3, -3, 7, -7, 9, -11), with full diagonals and random fillers in rows = 3 mod 4: 0 violations.
 fam.py and cmp.py give formula predicates whose label-pair lists match the brute force on every diagonal tested.
(2) loads2.py counts intra-class pair degrees over pairs not in G_T, on full diagonals. Average (maximum) degrees:
 - h = 64: X1 0.19 (5), X2 1.98 (14), M2c 0.56 (6).
 - h = 96: X1 0.21 (5), X2 2.46 (19), M2c 0.57 (9).
 - M1C is at most 0.003.
 - X2 pairs with equal v2 mod 3: 0.
(3) Fillers. Against M2a with the filler's own class line, the minimum number of admissible rows = 3 mod 4 per empty slot is 2, 4, 8 and 11, out of 6, 12, 24 and 40 rows, at h = 24, 48, 96 and 160. Against every obstruction with one filler (filler_brute.py), the minimum is 1 of 7 at h = 28, and rival pairs dominate.
(4) Two-level pure sea, hole row rho = h + 2 mod 4: V3 collisions occur (h = 13: 40; h = 17: 68 and 126; h = 21: 88 to 188).
(5) Mixed sea at h = 21 with labels and the boundary labels removed:
 - Sea(1,h): deep (3a) present, M2a filler-label 27.
 - rho = h - 2: (3a) gone, V3 470, M2a 36.
 - rho = h - 1 (even): X2 with a hole filler 25.

## External results used

- Paper sec2_prelim.tex: Lemma diff, compress, criterion and facts (F1), (F3); sec5_threshold.tex: Lemma mixedeq, rival, reduction (all in the repository).
- research_archive/2026-11-13/lower_bound_windows.md: Lemma 1 (axis owner) and Lemma 2 (no fully black tilted rectangle), audited.
- research_archive/2026-11-12/arc_classes_monotone_partition.md, Section 7 (the 2-adic remark), rederived here.

## Checks

Scripts are in the script folders of this directory.
- board.py: brute-force obstruction finder.
- t1.py: explicit X1 and X2 examples.
- t2.py and t3.py: classification check.
- fam.py and cmp.py: formula predicates matched against the brute force.
- loads.py and loads2.py: intra-class degrees and the v2 mod 3 test.
- m2c.py: M2c intra-class solutions.
- filler_count.py and filler_brute.py: admissible filler rows.
- t4.py and t5.py: Sea(1,h) and two-level deep seas with labels.
- t6.py to t9.py: pure-sea scans.
- coord.py: check of the earlier derivation formula.
All runs took under 60 s.

## Gaps

- No sea for the blocks is constructed. The deep layer (fillers in label blocks and gaps) is open. Proposition 5 rules out single-row gap fillers. Two-level fillers kill the deep one-label family but create V3 collisions (odd rho = h+2 mod 4), X2 with hole fillers (even rho), or the need for a third level (rho = h mod 4).
- X1 and M2c inside a class are not killed. Their average intra-class degree is small (at most 0.21 and 0.57 for h <= 96), but the maximum degree grows like a divisor function. I did not bound the chromatic number of G_T together with these graphs.
- Cross-class loads of X1, X2, M2a and M2c are not computed. I only show that each family needs a column difference O(h^2). Heuristically the load per label is of order rho log(h)/20, which is not O(1).
- Labels whose odd row is 1 (i = 0), or whose odd row is the filler row, act as sea points. They produce many M2a and M2c instances in the brute force. They must go to a separate region (for example the boundary star of ledger row T25), and I did not check that transition.
- V3 (two parked triples at one white corner) and the deep-only families with fillers (corner triples, mixed quadruples and rival pairs among labels and fillers) are only counted by computer for small h.
- Nothing here is independently audited. The proofs of Theorems 1 and 2 and of Propositions 3 to 5 were re-read once by me and checked by brute force at h <= 21 only.

## Missing estimate

To finish the block sea, three pieces are needed. (a) A deep-layer rule, a function from empty columns 4m to rows, that obeys the forbidden offsets D + (±4k(k+1), ±(4k+2)) for every deep black D, has no deep one-label family and no V3 collisions, and is compatible across gaps. (b) A bound on the chromatic number of G_T ∪ X1 ∪ M2c per diagonal (X2 is handled by the v2 mod 3 split). (c) Cross-class pair loads of order rho log h/20, absorbed by the block order.

## Next steps

- Audit Theorems 1 and 2 by hand, especially case (iii) (mod 16) and the M2c relation n1((Delta-n1)^2+e^2) = e u2 (Delta - 2n1).
- Design the gap deep layer from Proposition 5. Treat the gap fillers as a function f(m) with f(m + k(k+1)) - f(m) != ±(4k+2), and f avoiding y_D ± (4k+2) at m = n_D ± k(k+1) for nearby labels. A greedy choice row by row is plausible, because each gap column sees only about rho h/80 forbidden rows.
- Compute the degeneracy of G_T ∪ X1 ∪ M2c per diagonal up to h = 512, to test whether the class count grows by only a constant factor.
- Move the i = 0 labels and the labels whose odd row is the filler row to a boundary-star region, then recount the families.
- Count the cross-class X2 and M2a incidences exactly for a random block order at h = 1000 to 4000, to compare with the earlier (E;O,E) load.

