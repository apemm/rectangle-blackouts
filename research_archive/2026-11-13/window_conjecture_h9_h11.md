# Windows at heights 9 to 11 and a limit of the window method

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: W_N(h) >= h for every h >= 4, so the window method gives at most q_h + floor((q_h - 1)/h). Computation gives W_N(9) = 9, W_N(10) = 10, W_N(11) = 11. Not audited yet.

# Result

## Status

partial

## Summary

Window conjecture still open. Computed W_N(9)=9 and W_N(10)=10 (two independent programs, all bipartitions) and W_N(11)=11 (one program, all bipartitions), so m_9>=22, m_10>=27, m_11>=32 with computer assistance. Proved W_N(h)>=h for all h>=4, so the window method can never beat q_h+floor((q_h-1)/h). W_N(h)<q_h is false at h=4.

## Statements

Notation is as in lower_bound_windows.md. Point (x,y) means column x, row y. A TILTED TRIPLE in P is three distinct points V, X, Y of P with (X-V).(Y-V) = 0 and X-V not axis-parallel. Its fourth corner is X+Y-V. A set P with two points per column, whose row pairs are distinct edges of K_{A,B}, is an N-window of the h x k grid iff no tilted triple of P has its fourth corner in [1,k] x [1,h]. (Any three corners of a rectangle contain a vertex and its two neighbours.)

PROVED (by hand, proofs below):
(L1) Corner lemma. No tilted triple of a grid has its vertex at a corner of the grid.
(L2) Two-line lemma. A point set contained in two adjacent 45-degree lattice lines ({x-y = c} union {x-y = c+1}, or {x+y = c} union {x+y = c+1}) contains no tilted triple. The analogue for adjacent lines of any non-axis direction (c,d) also holds. The analogue for adjacent rows or columns is false: (x,y), (x+2,y), (x+1,y+1) is a tilted triple.
(P3) W_N(h) >= h for every h >= 4. For even h, take the parity bipartition and the columns {1,2}, {2,3}, ..., {h-1,h}, {1,h}. For odd h >= 5, take A = {1,3,...,h-2}, B = {2,4,...,h-1} union {h} and the columns {1,h-1}, {h-2,h-1}, {h-3,h-2}, ..., {1,2}, {1,h}. The odd case is new: the note had only W_N(h) >= h-1. The even case is the archive's cyclic staircase, now with a self-contained proof.
(C) Consequences. (P3) of lower_bound_windows.md can never give more than m_h >= q_h + floor((q_h-1)/h). Since W_N(4) = 4 = q_4, the weaker target W_N(h) < q_h is FALSE at h = 4. It can only hold for h >= 5.

COMPUTED (exhaustive Python searches, no proof log):
(K1) W_N(9) = 9 over all 126 balanced edge sets, and W_N(10) = 10 over all 126 edge sets (71 orbits under the row reflection). No window of width h+1 exists. Two programs agree: the audit's wn.py and my wk2.py. They give identical counts of width-h windows for every edge set (h = 9: 40 windows in total; h = 10: 88 over the orbit representatives, 140 over all edge sets). A third program, wk3.py, agrees on all width-h counts at h = 8, 9, 10.
(K2) W_N(11) = 11. wk3.py finds no window of width 12 for any of the 236 reflection orbits, which covers all 462 edge sets. wk2.py independently confirms zero for 4 of them: A = {2,4,6,8,10}, {1,3,5,7,9}, {1,2,6,7,11}, {3,4,5,9,10}. The lower bound 11 comes from (P3).
(K3) Parity bipartition, h = 12: no N-window of width 13. This used wk3 split by the column-1 pair, all 36 subtrees, one program.
(K4) Hence, with (P3) of lower_bound_windows.md: m_9 >= 22 = q_9 + 2, m_10 >= 27 = q_10 + 2, m_11 >= 32 = q_11 + 2. These are computer-assisted. Earlier notes have no lower bound above q_h for h >= 9: the ledger has only T10, m_h >= q_h.
(K5) The note's statement that maximal windows are staircase runs with at most two extra columns fails at h = 9 and h = 10. I covered each width-h window by the best pair of adjacent lattice lines (any direction (c,d) with 1 <= c <= 3, |d| <= 3). The cover holds 8 to 16 of 18 points at h = 9 and 5 to 19 of 20 at h = 10. Example of a width-10 window at h = 10, A = {1,3,4,7,9}: 1-10 1-8 5-7 1-2 2-7 3-8 8-9 3-5 2-9 9-10. Its best two-line cover holds 5 points. Width-h windows are boundary-heavy: over the 88 windows at h = 10, rows 1 and 10 hold 288 and 286 points, rows 4 and 5 hold 114 and 90.

NOT PROVED: the window conjecture W_N(h) <= h for any h >= 12; W_N(h) < q_h for all h >= 5, for all large h, or for the parity bipartition; m_h >= q_h + 1 for any h >= 12.

## Proofs

COORDINATES. For a vector u = (u1,u2) put s_u = u1+u2 and d_u = u1-u2.
(F1) 2 u.v = s_u s_v + d_u d_v.
(F2) u is axis-parallel iff |s_u| = |d_u| (u2 = 0 iff s = d; u1 = 0 iff s = -d).
(F3) For a lattice point, s ≡ d (mod 2).
(F4) A point is in the h x h grid iff |d| <= s-2 and |d| <= 2h-s. This holds because x = (s+d)/2 and y = (s-d)/2 both lie in [1,h].

(L1) PROOF. Let V = (1,1) be the vertex, u = X-V and v = Y-V. All four coordinates are >= 0, so u.v = u1 v1 + u2 v2 = 0 forces u1 v1 = 0 and u2 v2 = 0. The triple is tilted, so u1 and u2 are nonzero. Then v1 = v2 = 0, so Y = V, a contradiction. The other three corners follow by reflecting the grid.

(L2) PROOF (45-degree case). The map (x,y) -> (x,-y) swaps s and d and preserves right angles and axis-parallelism, so take the lines d = c and d = c+1. Three points on one line are collinear, and collinear points form no right angle. Otherwise two of the points, Z1 and Z2, lie on one line, with (s,d) = (a1,c') and (a2,c'), a1 != a2. The third point W has d = c' +- 1.
- Right angle at Z1. By (F1), 2(Z2-Z1).(W-Z1) = (a2-a1)(s_W-a1) = 0, so s_W = a1. Then W-Z1 = (0, +-1) in (s,d) coordinates, which is axis-parallel by (F2).
- Right angle at W. 2(Z1-W).(Z2-W) = (a1-s_W)(a2-s_W) + 1 = 0, so a1-s_W = +-1 and Z1-W = (+-1, -+1) in (s,d) coordinates, which is axis-parallel.
(General direction.) Let e = (c,d) be primitive with cd != 0, and let f satisfy det(e,f) = 1. Write Z1 = Q + a1 e, Z2 = Q + a2 e, W = Q + w e + f. Lagrange's identity gives |e|^2 |f|^2 - (e.f)^2 = 1. Set al = a1-w and be = a2-w. Then |e|^2 (Z1-W).(Z2-W) = (al|e|^2 - e.f)(be|e|^2 - e.f) + 1. A right angle at W therefore makes the two integer factors 1 and -1, so (al-be)|e|^2 = +-2 and |e|^2 = 2. For e = (1,1) and f = (t,t+1), the legs are (1,0) and (0,-1), both axis-parallel. A right angle at Z1 makes W-Z1 perpendicular to e with det(e, W-Z1) = 1. That forces W-Z1 = (-d,c)/|e|^2, which is not a lattice vector because |e|^2 >= 2.

(P3) EVEN h >= 4. The bipartition is A = odd rows. The pairs {i,i+1} and {1,h} join an odd row to an even row, and they are distinct. P = D0 ∪ D1 ∪ {C} with D0 = {(i,i): 1 <= i <= h} (d = 0), D1 = {(i,i+1): 1 <= i <= h-1} (d = -1), and C = (h,1). Column i < h holds (i,i) and (i,i+1); column h holds (h,h) and (h,1).
A tilted triple avoiding C contradicts (L2). C is a corner of the grid, so it is not the vertex (L1). That leaves vertex V in D0 ∪ D1 with legs to C and to Z in D0 ∪ D1, and fourth corner F = C + Z - V. Write Z - V = (Ds, Dd) in (s,d) coordinates, with Dd in {-1,0,1}, and C = (h+1, h-1). Then F = (h+1+Ds, h-1+Dd). Adding the two inequalities of (F4) gives |d_F| <= h-1, so Dd is 0 or -1.
- If Dd = 0, (F4) gives h-1 <= h-1+Ds and h-1 <= h-1-Ds. So Ds = 0 and Z = V, a contradiction.
- If Dd = -1, (F4) gives |Ds| <= 1. By (F3), Ds is odd, so |Ds| = |Dd| = 1 and Z-V is axis-parallel (F2). That contradicts tiltedness.
So no tilted triple has its fourth corner in the h x h grid.

(P3) ODD h >= 5. A = {1,3,...,h-2} has size (h-1)/2. The pair {1,h-1} is an edge because h-1 is even. For 2 <= j <= h-1 the pair {h-j, h-j+1} is an edge: its odd row is <= h-2, so in A, and its even row is in B. {1,h} is an edge. The pairs are distinct, since their differences are h-2, 1 and h-1 and the difference-1 pairs differ from each other.
P = E0 ∪ E1 ∪ {C1, C2} with E0 = {(j,h-j): 1 <= j <= h-1} (s = h), E1 = {(j,h+1-j): 2 <= j <= h} (s = h+1), C1 = (1,1) and C2 = (h,h). Column 1 holds (1,h-1) and (1,1). Column j holds (j,h-j) and (j,h-j+1). Column h holds (h,1) and (h,h).
Triples with no corner point contradict (L2), and a corner vertex contradicts (L1). The remaining cases have vertex V in E0 ∪ E1, with Z - V = (Ds, Dd) and Ds in {-1,0,1}.
(a) Legs to C1 = (2,0) and to Z in E. Here F = C1 + Z - V has s_F = 2+Ds and d_F = Dd. (F4) needs |Dd| <= Ds. If Ds = -1 this is impossible. If Ds = 0 then Z = V. If Ds = 1 then |Dd| = 1 by (F3), so Z-V is axis-parallel.
(b) Legs to C2 = (2h,0) and to Z. (F4) needs |Dd| <= -Ds. The same three cases give a contradiction.
(c) Legs to C1 and C2. By (F1), the right angle means d_V^2 = (s_V-2)(2h-s_V). For V in E0 this gives d^2 = h^2-2h, which lies strictly between (h-2)^2 and (h-1)^2 for h >= 3, so it is not a square. For V in E1 it gives d = +-(h-1), and the only such point of E1 is (h,1). There C1 - V = (1-h, 0) is horizontal, so the triple is not tilted.
Hence P is an N-window of width h. A definition-level check of all point triples (constr_check.py) confirms both families for 4 <= h <= 40.

(C). Theorem (P2)/(P3) of the note gives m_h >= q_h + floor((q_h-1)/W_N(h)), and W_N(h) >= h, so the method cannot exceed q_h + floor((q_h-1)/h). W_N(4) >= 4 = q_4 by the even construction, so W_N(4) < q_4 fails.

COMPUTATIONS. Every script ran with py in under 60 s (chunked) and used well under 1 GB. All scripts are in the matching scripts_ folder of this directory
- wn.py is the audit's program, copied with a patch that lets it take a list of indices. It runs a prefix DFS over all widths up to h+1 and counts windows by width. wn_sym.py restricts it to one edge set per orbit of the row reflection y -> h+1-y. That map preserves the grid, the tilted rectangles and balancedness, so it maps windows to windows.
- wk.py, and its bitmask version wk2.py, are my own and were written from the definition. Width K is fixed, and the DFS prunes as soon as a tilted triple of placed points has its fourth corner anywhere in the h x K grid, a condition that is monotone in P. The triple scan treats N or O as the vertex and walks along the perpendicular. On 5 edge sets at h = 9 (width 10), wk.py and wk2.py agree, and at h = 8 their width-8 counts agree with wn.py.
- wk3.py is a third formulation. M[a][b] holds the cells c that make {a,b,c} a tilted triple (any vertex) with its fourth corner in the grid. The search does forward checking and picks the most constrained column first.
Agreement:
- h = 8: all three programs give the same width-8 counts on all 35 edge sets (8 edge sets have windows: six have 2 and two have 4).
- h = 9: wn and wk2 give identical width-9 counts on all 126 edge sets (14 edge sets nonzero, 40 windows), and both give zero at width 10. wk3 matches the width-9 counts.
- h = 10: wn and wk2 give identical width-10 counts on all 71 orbits, and zero at width 11 for every orbit (wk3 also gives zero on 3 orbits). wk3 matches the width-10 counts.
- h = 11: wk3 gives zero at width 12 for all 236 orbits. I checked that the result lines cover the whole orbit list. wk2 gives zero on 4 edge sets.
- h = 12, parity: wk3_root.py gives zero at width 13, summed over all 36 choices of column 1, with no subtree timing out.
classify.py lists all width-h windows (h = 9: 20 windows on orbit representatives; h = 10: 88). verify_list.py rechecks every listed window from the definition by enumerating all tilted rectangles of the h x h grid (748 at h = 9, 1280 at h = 10): 0 bad. Trend of window counts over all edge sets: width h-1 / width h / width h+1 is 2320 / 20 / 0 at h = 8, 14100 / 40 / 0 at h = 9 and 24072 / 140 / 0 at h = 10. The number of edge sets that reach width h is 8 of 35, 14 of 126 and 39 of 126.

WHY THE CONJECTURE DID NOT CLOSE.
(i) A classification of width-h windows is not small or staircase-like (K5). Many are boundary-heavy mixtures that no pair of adjacent lines covers well, so a classification proof needs an invariant other than staircase structure.
(ii) For perpendicular directions other than 45 degrees, the ray and line counts are slack by (P5) of the note. The 45-degree identity is exactly tight and cannot be violated. 45-degree rectangles alone allow saturated parity windows at h = 9 (the note's C2).
(iii) A heuristic two-band test does not produce long windows. Put rows 1..t and h-t+1..h in one column each. Cross-band right angles need |a Dx| = |b| (h-2t) with |a|, |Dx| < k, so the bands decouple only when k^2 < h-2t. Distinct pairs give k <= t^2. So decoupled two-band windows stay short. This is a remark, not a bound.

## External results used

- lower_bound_windows.md (P2)/(P3), audited: m_h >= q_h + floor((q_h-1)/W_N(h)). Used for the consequences m_9 >= 22, m_10 >= 27, m_11 >= 32.
- The paper's equality-structure theorem and Lemma diff are used only through the reduction above. No published external theorem is needed.

## Checks

Script folder the matching scripts_ folder of this directory
- Programs: wn.py and wn_sym.py (the audit's program with orbit restriction); wk.py, wk2.py, wk2_list.py, wk3.py, wk3_list.py, wk3_root.py (mine); classify.py; verify_list.py; constr_check.py.
- Raw outputs: h9_[abcd].txt and h10_*.txt (wn); x9_9.txt, x9_10.txt, x10_10_*.txt, x10_11_*.txt (wk2); y9_9.txt and y10_10[ab].txt (wk3 cross-checks); x11_12_*.txt, x11_m_*.txt, all11.txt (h = 11); r12_*.txt (h = 12 parity); cl9.txt and cl10[ab].txt (classification).
- constr_check.py: 0 bad triples for both (P3) families, 4 <= h <= 40.
- verify_list.py: 0 bad among 20 (h = 9) and 88 (h = 10) listed windows.
- Repository untouched. No git commands.

## Gaps

- The window conjecture W_N(h) <= h is not proved for any h >= 12. For h = 9, 10, 11 it is exhaustive computation without a proof log or certificate.
- The weaker target W_N(h) < q_h (that is, m_h >= q_h + 1) is not proved for all h >= 5, for large h, or for the parity bipartition. As stated for h >= 4 it is false, since W_N(4) = 4 = q_4.
- h = 11 rests on one program (wk3.py) over all 236 reflection orbits. The second program (wk2.py) checked only 4 edge sets. wk3 matches wn and wk2 on every width-h count at h = 8, 9, 10.
- h = 12 was checked only for the parity bipartition, by one program, and gives no bound on m_12.
- The searches are Python DFS programs. Agreement between independently written programs is the only safeguard. I did not read wn.py's internals beyond the docstring and the main loop: I copied it and added an index-list patch.
- I took the reduction m_h >= q_h + floor((q_h-1)/W_N(h)) from lower_bound_windows.md (audited there) and did not re-derive it.
- I could not find a classification invariant for width-h windows: they are not near-staircases (two-line cover as low as 5 of 20 points at h = 10).

## Missing estimate

Still missing: for every h >= 12 (or at least every large h) and every balanced bipartition, a proof that no N-window of width h+1 exists. Failing that, a proof of no N-window of width q_h for h >= 5, which would give m_h >= q_h + 1. A proof must use slopes other than 45 degrees together with the distinct-pairs condition: 45 degrees alone allows saturation at h = 9, and constant columns {1,h} give arbitrarily long windows once pairs may repeat.

## Next steps

- Encode 'N-window of width h+1' as SAT, one clause per tilted triple with fourth corner in the grid, plus exactly-two-per-column and at-most-once-per-edge constraints. Get DRAT proofs for h = 9..13 so that m_h >= q_h + 2 is citable for h <= 13. Python wk3 with root splitting takes about 4 minutes per bipartition at h = 12, which is too slow for all 236 orbits.
- Look for an invariant that separates boundary-heavy windows from deep ones. Width-h windows put about 3.3 points in rows 1 and h and about 1 in middle rows (h = 10). A charge argument would have to show that a deep point costs a boundary column.
- For the parity bipartition, combine the class-function rigidity (P4, P7 of lower_bound_windows.md) with the slope (1,2) and (2,1) families, which cross the parity classes. Test with wk3 whether 45-degree rectangles plus one such family already bound the window width by h at h <= 12.
- Fix lower_bound_windows.md: W_N(h) >= h now holds for all h >= 4 (proved here, so the cyclic-staircase citation is no longer needed). The staircase description of maximal windows is wrong at h = 9, 10. The weaker target must read h >= 5.

