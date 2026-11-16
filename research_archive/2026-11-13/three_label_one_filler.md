# Three labels and one filler (Q3)

13 November 2026. Problem 001. Status labels as in the other notes of this folder: nothing here is in the paper. "Audit" means a separate line-by-line check by a second reader who derived the critical steps again.

Result: in L*** no mixed quadruple and no black rectangle has three label points and one filler, in any composition, class or block. The proof compares squared lengths modulo 32: a filler and a label never have the same norm class as two labels. It uses only the region-wide congruences of the board, no mod-p input. Not audited yet.

# Result

## Status

proved

## Summary

Q3 closed: in L*** no mixed quadruple, and no fully black rectangle, has three label points and one filler, in any composition, class or block. The proof compares squared lengths modulo 32 and uses no mod-p input.

## Statements

SETTING. One region R_tau of the board L*** (consolidated_board.md B3 to B6), with its pure SAW*-shift margins (J6: no label sees a seam) and the offset-0 holes left by relocated labels. tau = (iota mod 32, sigma mod 16). Write Y0 = 2iota+1 (mod 64) and T0 = 2sigma+1 (mod 32). Put c = 1 if T = 3 (mod 4) and c = 3 if T = 1 (mod 4). Every deep point is (4nu, y). The proof uses only the following congruences, which hold for the whole region:
 (K-a) Every label column has nu = rho (mod 16), one residue for the region. By B5, nu = i + p t_c + b_tau with p t_c = s_c - kappa (mod 16l), so nu = iota + sigma - kappa + b_tau (mod 16).
 (K-b) Odd label rows: y_o = 2i+1 = Y0 (mod 64).
 (K-c) Even label rows: y_e = y_o + T_c with T_c = 2s_c+1 = T0 (mod 32), so y_e = Y0 + T0 (mod 32).
 (K-d) A filler in column 4nu_F with offset w = (nu_F - rho0) mod 4 sits in row f = T*_tau - 24 + 8w. Since T*_tau = Y0 + 32 or Y0 + 48 (mod 64), and the shift by 64k changes neither, f = Y0 + 8(w + c) (mod 64).

THEOREM Q3 (proved here; not audited). In R_tau:
 (a) No mixed quadruple of Lemma mixedeq (side AB, diagonal CD, |AB| = |CD|) has a support of three label points and one filler. This holds for every composition ({F,o,o,o}, {F,o,o,e}, {F,o,e,e}, {F,e,e,e}), with the filler on the side or on the diagonal, inside one class, across classes and across blocks of the region. The pair p, q plays no role, and neither do n or any mod-p condition.
 (b) No rectangle, axis-aligned or tilted, has all four corners black with three label corners and one filler corner.
 So table row D20 is EMPTY (0 labels hit), D19 gets a second, shorter proof that makes Lemma 3L1F-a unnecessary, and Q3 is no longer an open item of Theorem N.

LEMMA N (norm classes; proved). For deep points P, P' of R_tau write N(P,P') = |P - P'|^2. Then:
 (N1) N(o, o') = 0 (mod 2^12) for odd label points, and N(e, e') = 0 (mod 2^10) for even label points.
 (N2) N(o, e) = T0^2 (mod 32).
 (N3) For a filler F and an odd label point o, v2(N(F, o)) is 6, 4, 7, 4 for w = 0, 1, 2, 3.
 (N4) For a filler F and an even label point e, N(F, e) = T0^2 + 16 (mod 32).
Each holds for any two classes of the region.

Row parity, which the target asks for but the theorem does not need: with filler rows odd, C + D - A - B has an even row sum only for {F,o,e,e} and {F,o,o,o}. So {F,o,o,e} and {F,e,e,e} are impossible on that count alone.

Minimal hypotheses (remark, proved by the same computation): the argument needs only nu fixed mod 4 for labels, odd label rows and T fixed mod 16, and filler rows f = y_o + 8(w + c) (mod 16) with c odd. That last condition means T* = y_P (mod 16), which SAW* gives.

## Proofs

0. REDUCTION. Lemma mixedeq gives |D - C| = |B - A|, so N(A,B) = N(C,D). The support has four points: three labels and F. One of the pairs {A,B}, {C,D} contains F and one label L. The other pair contains two labels L', L''. So it is enough to show that N(F, L) never equals N(L', L''). If L' = L'', then N = 0, and the argument below still applies. Only (K-a) to (K-d) are used, so the classes of L, L', L'' and the blocks they lie in do not matter.

1. PROOF OF LEMMA N. Write P' - P = (4 Dnu, Dy).
 (N1) By (K-a), Dnu = 0 (mod 16), so (4Dnu)^2 = 0 (mod 2^12). For two odd points, Dy = 0 (mod 64) by (K-b), so Dy^2 = 0 (mod 2^12). For two even points, Dy = 0 (mod 32) by (K-c), so Dy^2 = 0 (mod 2^10).
 (N2) Here 16 Dnu^2 = 0 (mod 4096), and Dy = y_e - y_o = T0 (mod 32), so Dy^2 = T0^2 (mod 64).
 (N3) Put a = nu_F - nu_o and b = f - y_o. By (K-a) and (K-d), a = w (mod 4) and b = 8(w + c) (mod 64), with c odd.
  - w odd: a is odd, so 16a^2 = 16 (mod 128). w + c is even, so 16 | b and b^2 = 0 (mod 256). Hence N = 16 (mod 128) and v2 = 4.
  - w = 2: a = 2a' with a' odd, so 16a^2 = 64a'^2 = 64 (mod 512). b = 8b' with b' = 2 + c odd, so b^2 = 64 (mod 512). Hence N = 128 (mod 512) and v2 = 7.
  - w = 0: 4 | a, so 16a^2 = 0 (mod 256). b = 8b' with b' odd, so b^2 = 64 (mod 512). Hence N = 64 (mod 256) and v2 = 6.
 (N4) Put a = nu_F - nu_e, so a = w (mod 4), and 16a^2 = 16w (mod 32). Put b = f - y_e = 8m - T0 (mod 32) with m = w + c. Then b^2 = T0^2 - 16mT0 + 64m^2 = T0^2 + 16m (mod 32), because T0 is odd. So N = T0^2 + 16(2w + c) = T0^2 + 16 (mod 32), because c is odd.

2. PROOF OF (a). Take L, L', L'' as in step 0.
 - L odd. N(F, L) has 2-adic valuation 4, 6 or 7 by (N3), so it is even and nonzero. N(L', L'') must therefore be even, so L' and L'' have the same parity (mixed parity gives an odd norm by (N2)). By (N1), v2(N(L', L'')) >= 10 > 7. Contradiction.
 - L even. N(F, L) is odd, so L' and L'' have different parities (equal parity gives an even norm by (N1)). Then N(L', L'') = T0^2 (mod 32) by (N2), while N(F, L) = T0^2 + 16 (mod 32) by (N4). Contradiction.
 Both cases fail, whichever point is F, on the side or on the diagonal. QED (a).

3. PROOF OF (b). The diagonals of any rectangle have equal length, so N(A,C) = N(B,D) for the corners in cyclic order. One diagonal contains F and a label, and the other has two labels. Step 2 applies word for word. A second proof: three label corners already form an LLL right angle, which is empty by table row A1 (rigid Theorem C, audited). An axis-aligned rectangle with a filler corner is impossible in any case, because a filler column holds only one black point. QED (b).

4. CORNER TRIPLES AND V3. Theorem Q3 leaves no three-label one-filler configuration, so these quadruples create no V3 collision. The corner triples with at most one filler and no sea point are LLL, Fee, Feo and Foo. All four are empty: LLL by rigid Theorem C (audited), and the rest by v3_and_cross_block.md Theorem B (not audited). The only parked triples with labels and one filler have a shallow corner (intra-class SLL-Pc and SLF-Pc), and Theorem C of v3 classifies their V3 pairs as family (d). Q3 adds nothing new there. The norm trick alone does not settle right angles: for example, Fee with an even vertex is consistent mod 32. So Theorem B is still needed, and still owes its audit (U2).

5. WHY THE OLDER ROUTE WAS LONGER. Lemma 3L1F-a solved the in-class {F,o,o,o} equations and read off row(F) mod 64. The norm comparison makes that solving unnecessary. In every split of the support, F pairs with a label, and the other pair is two labels. (N1) to (N4) show that these two kinds of pair never share a norm class modulo 32. The congruences are region-wide, so the cross-class case needs no rigid input (M_c in pZ, p > 40h, (5/p) = -1). The same reason explains the earlier census results: the 2448 + 340 geometric {F,o,o,o} solutions had row(F) = y_P (mod 64), and in that case F behaves like an odd label point under N.

CHECKS (scripts in scripts_three_label_filler/; py -I, each run under 60 s; the repository was only read).
 - residues.py enumerates residues and confirms (N1) to (N4). The F-o valuations are [6], [4], [7], [4] for w = 0..3 with both c = 1 and c = 3. F-e minus T0^2 is 16 mod 32 for all 16 odd T0 and every w. o-e minus T0^2 is {0} mod 32. The minimum valuations are 12 for o-o and 10 for e-e.
 - q3_solver.py builds synthetic L*** regions with true primes: l in (1.04h, 2.08h] with l = +-2 (mod 5), p in (40h, 80h] with p = 3 or 7 (mod 20), the 16l rule, t_c = rho_s + 16lk, i = iota (mod 32), s = sigma (mod 16), and the SAW*-shift rows. For every label triple and all 6 role assignments, it solves Lemma mixedeq exactly for F (a quadratic in t when F is on the diagonal, and a line-circle intersection when F is on the side). Each solution is re-checked from the definition: n integral and nonzero, n.(B-A) = 0, |CD| = |AB|, D-C != +-(B-A), and p, q, F inside rows 1..h.
  - h = 800 (iota 5, sigma 3): 181 geometric solutions, 70 with F deep, odd row and a non-label column, 0 on the SAW* rule. The control rule with c even gives 11.
  - h = 1500 (iota 6, sigma 4, T = 1 mod 4): 2908 solutions, 911 deep odd, 0 on the rule.
  - h = 1201 (iota 17, sigma 10): 778 solutions, 86 deep odd, 0 on the rule.
  - h = 1003 (iota 30, row-3 type, sigma 15): 1899 solutions, 550 deep odd, 0 on the rule. The c-even control gives 2.
  - These windows are small. They test the algebra, not the full board.

## External results used

- None. The proof uses only paper Lemma mixedeq (sec2_prelim.tex, read: |D-C| = |B-A|), the locality of 2W_h+1 columns (sec5_threshold.tex, read), and the L*** definitions in consolidated_board.md B3, B5 and B6.

## Checks

Residue enumeration (residues.py) confirmed all four norm classes. The exact mixedeq solver (q3_solver.py) ran on 4 synthetic L*** regions (h = 800, 1003, 1201, 1500; row-1 and row-3 types; T = 1 and 3 mod 4) with true primes l and p. It found 5766 geometric solutions in total and 1617 with F at a deep non-label odd row. None had F on the SAW*-shift rule, while the c-even control rule had 13 hits. Every solution was re-checked against Lemma mixedeq from the definition. One batch exceeded the time limit; I stopped it and reran each case on its own at a smaller size.

## Gaps

- Not audited. The proof is about one page. It rests on (K-a) to (K-d), which come from the board's definitions: (K-a) from B5 (p t_c = s_c - kappa mod 16l, and b_tau fixed per type), (K-b) and (K-c) from B3 and the class restriction to types, (K-d) from B6 with T0_tau as defined there. An auditor should check against consolidated_board.md that every label of R_tau really has nu fixed mod 16 (at least mod 4 is needed), with b_tau constant per type and the classes of all diagonals s = sigma (mod 16) included.
- Scope: the four points lie in one region R_tau together with its pure SAW*-shift margins and holes. This uses the locality of 2W_h+1 columns (sec5_threshold.tex) and the margins and buffers of J5 and J6 (full_layout_junctions, audited), which keep a label of R_tau from seeing another region, a seam, a Theorem D or E block, or a Proposition partial block. If a margin used a different type's filler rule, (K-d) would fail there. J6 says the margins are pure SAW of the region, which is what the proof needs.
- Corner triples (3 black corners) with labels and one filler are not re-proved here. That rests on v3_and_cross_block Theorem B (not audited, U2). The norm trick does not kill every right angle; for example, Fee with an even vertex is consistent mod 32.
- The synthetic checks have small windows (h <= 1500, at most 138 labels, 2 classes per diagonal). Cross-class geometric solutions are rare at these sizes, so the cross-class case is backed by the proof, not by the census.

## Missing estimate

None for Q3. Theorem Q3 hits 0 labels, so it adds nothing to n_rel and nothing to the relocation width. The open items left for the near goal are Q1 (now only the df = 0 even-even and N_h parts, according to two_filler_row_lemma.md), Q2 (empty according to two_filler_row_lemma.md Corollary 2, not audited), Q4, Q5 (AP), and the audits U1 to U8.

## Next steps

- Audit Theorem Q3 together with Lemma N: about one page of residue arithmetic and a lookup of (K-a) to (K-d) in the board definition. Once it passes, mark D20 EMPTY (H, 0 labels) in the table of consolidated_board.md, and keep Lemma 3L1F-a only as a second proof of D19.
- Try the same norm-class comparison on the other quadruple families where one pair holds a filler and the other does not. These are the two-label two-filler shapes with side {F,F'} and diagonal {L,L'} (ll/FF and FF/ll, D14) and the cross-block F1 and F2 shapes. It might shorten their proofs or remove their dependence on R1. It does not help when both pairs are {F,L} (F3, D15 to D17).
- Q4 (row-3 types, deep-only quadruples with a corner p or q in rows 1 to 2) is the next open item on the Q list.

