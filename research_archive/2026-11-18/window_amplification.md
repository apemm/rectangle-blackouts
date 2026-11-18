# A counterexample to the window bound would persist at every large height

Let \(W(h)\) be the largest width of a balanced window. All columns contain two black points, the row pairs are distinct edges of a single bipartite graph, and every tilted rectangle in the grid contains at most two black points. A balanced window also requires the two parts to differ in size by at most one, counting unused rows.

**Theorem.** Suppose some bipartite window on \(H\ge4\) rows has at least \(H+1\) columns. Its partition may be unbalanced. Then
\[
 \liminf_{h\to\infty}\frac{W(h)}h\ \ge\ \frac{H+1}{H}.
\]
Consequently, if \(W(h_j)/h_j\to1\) on even one sequence \(h_j\to\infty\), the upper bound \(W(H)\le H\) holds at every height \(H\ge4\), even for unbalanced partitions. Conversely the [square windows](windows.md) give \(W(h)\ge h\) for every \(h\ge4\), so the universal bound implies this subsequence statement.

Start with the first \(H+1\) columns of the given window. The other two templates are balanced square windows of sides \(H\) and \(H+1\). Use coordinates starting at zero. For the three fixed templates, list all nonzero displacements \((u,v)\) between black cells within the same template. At every sufficiently large prime \(p\), choose a nonzero \(a\bmod p\) satisfying
\[
 1+a^2\ne0,\qquad u+av\ne0\pmod p
\]
for all listed displacements. For \(p\) larger than the coordinate differences, each displacement with \(v\ne0\) excludes just one residue and the other displacements exclude none. There are only finitely many exclusions independently of \(p\).

Take \(p\) to be the largest prime at most \(h/H\). The prime number theorem gives \(p\sim h/H\), by applying it to each interval \([(1-\epsilon)h/H,h/H]\) with fixed \(\epsilon>0\). Thus \(h=pH+r\) with \(0\le r<p\) for every sufficiently large \(h\). [Proof of the prime number theorem](https://terrytao.wordpress.com/2021/02/12/246b-notes-4-the-riemann-zeta-function-and-the-prime-number-theorem/)

For each column residue \(w\in[0,p-1]\) put \(z_w=[aw+b]_p\) in that same range. A copy of a local template in this fiber sends
\[
 (x,y)\longmapsto (px+w,py+z_w).
\]
Exactly \(r\) fibers have \(H+1\) available rows. Each gets the square of side \(H+1\). The remaining fibers have \(H\) rows. If their count \(p-r\) is even, give all of them the given template, with ambient width \(p(H+1)\). If their count is odd, choose \(b\) so that \(z_{p-1}\ge r\). Give fiber \(w=p-1\) the balanced square of side \(H\), give the other short fibers the given template, and use ambient width \(p(H+1)-1\). In this case only the last column residue loses a column. In particular the local row and column ranges in every fiber are precisely its template ranges.

Each physical column has two black points, and its row pair belongs to its unique row residue. This preserves distinctness of the pairs. Reverse the row parts in alternate copies of the given template to cancel their imbalances. In the first case, \(r\) is odd, so the tall squares leave at most one balanced square unpaired. In the second case \(r\) is even, and the balanced square of side \(H\) is left over. Both global partitions are balanced.

A vector between different fibers reduces to a nonzero multiple of \((1,a)\) modulo \(p\). Two such vectors cannot be perpendicular. If one leg stays in a fiber it equals \(p(u,v)\), and after division the other leg has nonzero dot product with it modulo \(p\). Thus a tilted triple must lie entirely in one fiber. The fourth corner is in that fiber's coordinate residues as well. If it fits the large grid, it fits the local template, which excludes the triple. This proves \(W(h)\ge p(H+1)-1\) and the theorem.

The same argument with \(p\) identical copies of any fixed balanced \(H\)-row window of width \(k\) gives \(W(pH)\ge pk\) for all sufficiently large primes. In the all-height theorem the square templates handle the remainder \(r\); simply adding unused rows could allow a fourth corner that previously lay outside the grid.

The theorem concerns runs of double columns. The unique row-pair owners and filled singleton columns required for a full threshold construction are additional conditions.
