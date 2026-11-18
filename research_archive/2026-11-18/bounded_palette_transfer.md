# Any fixed palette suffices for the vertical-rival construction

Use \(G_s(Q)\) from [ternary interleaving](ternary_interleaving.md). Its vertical test is \(6(j_v-i_u)+1\) in either direction, with horizontal distance \(Q|r_v-r_u|\). The order is the canonical Hilbert order. The following reduction keeps one fixed family of ordinary graphs at all palette sizes.

**Theorem.** Fix \(Q=96\), or any positive multiple of four. Suppose \(\chi(G_s(Q))\le C\) for some finite \(C\) and every dyadic \(s\). Then the \(\lfloor h^2/4\rfloor\) opposite-parity pairs of rows can be placed in distinct columns of \(4\mathbb Z\), in width \(O_{C,Q}(h^2)\), with no integral distance between opposite-parity endpoints from distinct labels. This theorem addresses the vertical-rival obstruction. It does not supply the sea or the other conditions for a blackout.

**Local choice of a prime.** For every odd prime \(p\) choose \(\lambda_p\) divisible by four so that \(1+\lambda_p^2\) is a quadratic nonresidue modulo \(p\). Indeed, \(z^2-t^2=1\) has \(p-1\) solutions, by \((z-t)(z+t)=1\). If every \(1+t^2\) were a square or zero, there would be at least \(2p-2\) solutions, since at most two of these values vanish. Thus a suitable \(t\) exists. It is nonzero. Choose a positive representative \(\lambda_p\equiv t\bmod p\) divisible by four.

Choose a fixed set of \(l\) distinct odd primes, including three, with \(2^l\ge C\). Write \(P\) for their product. All constants in the proof may depend on these primes.

**Unpacking one prime.** Consider any subfamily of opposite-parity labels with rows in \([0,H]\). For each label choose \(K=p^{v_p(b-a)}\), and let \(w\in[0,K-1]\) be the common residue of its rows. Replace row \(y\) by \((y-w)/K\) in this fiber. The normalized pair still has opposite parity and its two rows differ modulo \(p\). If they already differed modulo other processed primes, they still do so, since \(K\) is a unit at those primes. The normalized rows lie in \([0,\lfloor H/K\rfloor]\).

Suppose all the child fibers have placements \(x'\) in \(4\mathbb Z\), with the required P exclusion and \(0\le x'\le D\lfloor H/K\rfloor^2\). Reserve one run for each \(K\), with different fibers interleaved by
\[
 x=A+Kx'+\lambda_p w,\qquad 4K\mid A.
\]
Different fibers give distinct column residues modulo \(K\). Within one fiber the displacement scales by \(K\). Across fibers, \(X\equiv\lambda_p Y\bmod K\), where \(X,Y\) are the column and row displacements. If \(p^j\Vert Y\) with \(j<v_p(K)\), then
\[
 (X/p^j)^2+(Y/p^j)^2\equiv (1+\lambda_p^2)(Y/p^j)^2\bmod p
\]
is a nonresidue. This rules out an integer distance.

Order runs by increasing \(K\). Start the next run beyond the preceding one by more than \(H^2/(2K)\), rounding its origin up to a multiple of its own \(4K'\). Both displacements across any such cut satisfy \(X\equiv\lambda_p Y\bmod K\) for the smaller \(K\), because \(K\mid K'\). If \(K\nmid Y\), the nonresidue argument applies. If \(K\mid Y\), then \(K\mid X\); an integral distance forces \(L/K\) integral and gives \(2|X|/K+1\le(Y/K)^2\). This contradicts the gap, since \(0<|Y|\le H\) for opposite-parity endpoints. The interleaved child runs, their gaps and rounding cost at most
\[
 O_{p,\lambda_p}\left((D+1)\sum_{K=p^e\le H} H^2/K+
                       \sum_{K=p^e\le H} K\right)
 =O_{p,\lambda_p,D}(H^2).
\]
Empty subfamilies need no placement. Apply this step recursively, using each prime once in a fixed order. The number of recursion levels is independent of \(h\).

**Terminal pieces.** At the bottom every label has a row difference coprime to \(P\). Orient it so the second row minus the first is \(1\bmod 6\). Partition labels by the residues of the ordered pair modulo \(2P\). In one piece, all cross-row differences from the first type to the second are congruent to a fixed unit \(\delta_p\bmod p\) for each chosen \(p\). Take the representatives \(\alpha,\beta\in[0,5]\) of the two row types modulo six and write the rows as \(6i+\alpha,6j+\beta\). Shift both indices and correct the second by \((\beta-\alpha-1)/6\) as in the ternary construction. This realizes every cross-row difference as \(6(j'-i')+1\). Embed the labels in the full dyadic square of side \(O(H+1)\), keeping their original full-square ranks.

Split this piece once more by Hilbert rank modulo \(4P\). For each ordinary graph color assign a distinct binary word \((b_p)_p\). By the Chinese remainder theorem take the offset \(z\in[0,4P)\) satisfying
\[
 z\equiv0\bmod4,\qquad z\equiv\delta_p\lambda_p b_p\bmod p
 \quad(p\mid P).
\]
Place the label at \(Qr+z\). Distinct ranks in the piece differ by at least \(4P\), so these columns are distinct. Two different colors disagree at some \(p\). Since the ranks coincide modulo \(p\), their horizontal difference is \(\pm\delta_p\lambda_p\bmod p\). Their vertical difference in either cross role is \(\pm\delta_p\bmod p\). The squared distance is the nonresidue \(\delta_p^2(1+\lambda_p^2)\bmod p\). For equal colors the offsets agree as integers, so the defining test in \(G_s(Q)\) excludes any collision.

The terminal pieces occupy \(O_{P,Q}(H^2)\) width in total. There are at most \((2P)^2(4P)\) pieces. Separate consecutive ones by more than \(H^2/2\) and translate each by a multiple of four. No integral distance with \(0<|Y|\le H\) crosses such a gap. Translating the entire output of a recursive call to start at a nonnegative multiple of four preserves all its internal tests. The one-prime step now gives \(O_{C,Q}(h^2)\) at the root.

The proof does not require the zero graph to be sparse or to have bounded degeneracy. A uniform chromatic bound alone suffices. A coloring certified up to a finite side only applies at those heights whose recursion uses the certified sides. The smaller three-color construction has substantially better constants for the finite checks.
