# Ternary interleaving for all opposite-parity labels

Place each unordered pair of opposite-parity rows of \([1,h]\) in a distinct column. Call the two black cells of such a label its endpoints. A P collision between two distinct labels means that two endpoints of opposite parity have integral Euclidean distance. This stronger test allows the hypotenuse to exceed the strip height. The construction below concerns these collisions. The other rectangle tests and the singleton sea still require proofs.

## One graph for the normalized pieces

Let \(s\) be dyadic and let \((i_r,j_r)\), \(0\le r<s^2\), enumerate the integer square \([0,s-1]^2\) in the canonical Hilbert order. For a fixed positive multiple \(Q\) of 12, join \(r\ne t\) if either
\[
 Q^2(r-t)^2+(6(j_t-i_r)+1)^2,\qquad
 Q^2(r-t)^2+(6(j_r-i_t)+1)^2
\]
is a square. Write \(G_s(Q)\) for this undirected graph. Every three-coloring \(c\) places the normalized labels in columns
\[
 x'_r=Qr+4c(r),\qquad c(r)\in\{0,1,2\}.
\]
The two possible cross-row differences have the form \(6(j-i)+1\), up to sign. They are units modulo three. For different colors the column difference is also a unit, and two nonzero squares modulo three sum to two. For equal colors the graph rules out the collision. The columns are distinct since \(Q\ge12\).

**Proposition.** If a fixed \(Q\) gives a three-colorable \(G_s(Q)\) at every dyadic side, then all \(\lfloor h^2/4\rfloor\) opposite-parity labels admit distinct columns in \(4\mathbb Z\), in width \(O_Q(h^2)\), with no P collision. It suffices to have the colorings at dyadic sides at most the first power of two at or above \(\lfloor h/6\rfloor+2\).

**Proof.** For an unordered pair of rows take \(K=3^{v_3(b-a)}\) and \(w\) their common representative in \([0,K-1]\). Write their rows as \(w+Kz\). The two values of \(z\) have opposite parity and differ modulo three. Orient the pair so its normalized row residues \((\alpha,\beta)\) in \(\{0,\ldots,5\}\) satisfy \(\beta-\alpha\equiv1\bmod 6\). There is a unique orientation. There are six possible ordered residue profiles. For fixed \(K,w,\alpha,\beta\), write the normalized rows as \(6i+\alpha\) and \(6j+\beta\). Across any two labels in this piece, the normalized second row minus the normalized first row is
\[
 6(j-i)+\beta-\alpha=6(j+k-i)+1,\qquad k=(\beta-\alpha-1)/6\in\{-1,0\}.
\]
Use coordinates \((i+1,j+k+1)\) in the Hilbert square. They are nonnegative and at most \(\lfloor h/(6K)\rfloor+1\). Use the least power of two \(s_K\ge\lfloor h/(6K)\rfloor+2\) for every fiber at this scale. Keep the ranks of the occupied cells in the full square. Removing the unused cells preserves a coloring.

Use one run for each \(K,\alpha,\beta\), shared by every \(w\). A label of rank \(r\) goes at
\[
 x=A+Kx'_r+4w
\]
where \(4K\mid A\). All label columns are multiples of four. Distinct fibers \(w\) give distinct residues modulo \(K\). Within a fiber, ranks are distinct and the normalized columns are strictly increasing. The span of this run is at most \(KQ s_K^2+4K\).

Now take an endpoint in each of two fibers in the same run. The endpoint rows and columns satisfy \(y\equiv w\bmod K\) and \(x\equiv4w\bmod K\). For different \(w\), write \(j=v_3(w_2-w_1)<v_3(K)\). Both legs of the displacement have valuation \(j\), and their reductions after division by \(3^j\) are units modulo three. Their squared sum cannot be a square. For equal \(w\), the legs are \(K\) times the normalized legs, already treated. If the original parity of a given oriented row flips from one \(w\) to another, the different-fiber argument still applies to every pair of endpoints.

Order the runs by nondecreasing \(K\). After each run at scale \(K\), leave a gap exceeding \(h^2/(2K)\) before the next run, whose origin is rounded up to a multiple of its own \(4K'\). For labels in different runs, \(K\) from the earlier run divides \(K'\) from the later one, so both satisfy \(x\equiv4y\bmod K\). When their rows differ modulo \(K\), the same valuation argument applies. Otherwise \(K\) divides both displacements \(X,Y\). An integral distance would give \(X/K,Y/K,L/K\) integral. Since the endpoint rows have opposite parity, \(Y\ne0\) and \(L/K\ge |X|/K+1\). Thus
\[
 2|X|/K+1\le (Y/K)^2,\qquad |X|<h^2/(2K),
\]
contrary to the gap. This covers all distinct runs, including nonconsecutive ones.

There are at most six runs per \(K\). Since \(K<h\), \(s_K=O(h/K)\). The runs and gaps together cost \(O_Q(\sum_K h^2/K)=O_Q(h^2)\). Rounding all starts costs \(O(\sum_K K)=O(h)\). This proves the proposition.

## The direct right-angle consequence

Inside a run, consider a right-angle candidate at one endpoint. If each of its two other endpoints has fiber residue different from that of the pivot, divide each leg by the power of three in its row difference. Its reduction is of the form \(u(4,1)\bmod 3\) for a unit \(u\). The dot product of the two reductions is \(17uv\ne0\bmod 3\). Such a right angle is impossible. Cases with one leg staying in the pivot's fiber require further analysis.

## Finite tests

The script [ternary_graph.py](ternary_graph.py) enumerates \(G_s(96)\) from odd divisors and the archived Hilbert rank-lag automaton. It repeatedly removes vertices of current degree at most two and greedily colors in reverse order. A separate enumerator generates primitive Euclidean triples and their odd multiples, decodes Hilbert coordinates independently, then scans every rank at every candidate lag. It checks both the total edge count and the absence of monochromatic edges.

At every dyadic side \(1,2,\ldots,4096\) the 3-core is empty. The graphs at sides 512, 1024, 2048, and 4096 have 157,282, 736,321, 3,516,060, and 16,117,764 edges respectively. This verifies the coloring hypothesis needed by the proposition for every height \(h\le 24{,}569\), since \(\lfloor h/6\rfloor+2\le 4096\). The argument for larger heights remains conditional. The experiments do not test full blackouts.
