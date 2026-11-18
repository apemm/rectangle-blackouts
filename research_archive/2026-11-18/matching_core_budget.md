# Why a common column permutation eventually has large matching cores

On the XOR matching blocks, one fixed dyadic tree permutation gave 3 colors at height \(16{,}384\). Every one of the \(8{,}192\) graphs at that height had degeneracy two. The degeneracy must eventually grow even if one chooses the common permutation separately at every height.

## Edge count

Let \(N\) be a power of two and \(h=2N\). Let \(\{\pi_t:0\le t<N\}\) be any family of permutations of \([0,N-1]\) such that \(\{\pi_t(j):0\le t<N\}=[0,N-1]\) for every \(j\). The XOR matchings have this property. Choose any permutation \(\sigma\) of the same interval, and use this one column permutation in all matchings. Give index \(i\) physical column \(8\sigma(i)\), odd row \(2i+1\), and even row \(2\pi_t(i)+2\).

Let \(G_t\) contain the true opposite-role vertical rivals whose vertical alternative has integral endpoints in the strip. It can also contain the additional edges of the stronger hypotenuse test in [the matching construction](dyadic_matching_blocks.md). For the two specified choices of edge set,
\[
 \sum_t |E(G_t)|=\Theta(N^2\log N).
\]
In particular, the mean degeneracy is \(\Omega(\log N)\), independently of \(\sigma\). The column permutations may fail the dyadic isometry condition and this counting assertion still holds.

For the lower bound, take a positive integral right triangle with legs \(8r,d\), with \(d\) odd and hypotenuse \(z\le N/4\). For each \(N/4\le i<3N/4\), at least one of \(\sigma(i)\pm r\) is in \([0,N-1]\), since \(r<N/2\). Choose one by a fixed rule and let \(j\) be its inverse image. Set \(k=i+(d-1)/2\), which lies in the index range. Take the unique \(t\) for which \(\pi_t(j)=k\).

The odd point of label \(i\) and the even point of label \(j\) differ by \(8r\) horizontally in absolute value and by \(d\) vertically. The alternative column is the midpoint of two multiples of eight. Its two rows are \(2i+1+(d\pm z)/2\). They are integral, have opposite parities, and lie in \([1,2N]\). The chosen directed event determines \(i,r,d\). Passing to an undirected graph loses a factor of at most two.

There are \(\Omega(N\log N)\) eligible triangles. Here is an elementary count. In each dyadic box \(M\le m<2M,\ M/4\le n<M/2\), take \(m\) odd, \(4\mid n\), and \((m,n)=1\). These conditions leave \(\gg M^2\) pairs for all sufficiently large \(M\). To see the density assertion, write \(n=4b\). The sum over odd primes of the proportions of pairs with a common divisor is at most \(\sum_{p\ {\rm odd}}p^{-2}+o(1)<1\). Rounding contributes \(O(M\log M)\) pairs over all primes up to \(2M\), by the harmonic sum bound. Each pair gives a distinct primitive Euclidean triple with even leg \(2mn\) divisible by eight, odd leg \(m^2-n^2\), and hypotenuse \(m^2+n^2<5M^2\). For \(M^2<N/40\), at least a constant times \(N/M^2\) odd dilates meet the length cutoff. The primitive triples and their scales determine disjoint triples across the boxes. There are order \(\log N\) boxes, giving the claimed count and the lower bound on edges.

For the upper bound, every integral right triangle of hypotenuse at most \(2N\) has a unique primitive triple and dilation. The Euclidean parameters with \(M\le m<2M\) give \(O(M^2)\) primitive triples, each with \(O(N/M^2)\) possible dilations. Summing over the dyadic boxes gives \(O(N\log N)\). For each such pair of legs, at most \(4N\) directed events occur over the whole matching cover. Choose the odd index \(i\), the sign of the vertical leg, and the sign of the horizontal leg. These fix the mate index \(k\), the index \(j\) in the common column permutation, and the matching \(t\). This proves the upper bound.

If \(G_t\) is \(d_t\)-degenerate, then \(|E(G_t)|\le Nd_t\). Summation proves \(N^{-1}\sum_t d_t\gg\log N\). In particular a common tree permutation cannot give a fixed degeneracy bound on all heights. High degeneracy can coexist with few colors. Allowing a different column permutation in each matching also removes the counting argument's common coordinate system.

## Checked finite instances

The [verifier](dyadic_matching_check.py) generates the Pythagorean legs by Euclidean parameters and independently recovers the same complete list by factoring \(16r^2=((z-d)/2)((z+d)/2)\). It assigns every directed event to its XOR matching, removes duplicate undirected edges, computes all core numbers, and checks the reverse-elimination colors against every edge. At height 128 the optional direct check also tested every ordered pair in every matching against the original squared-distance equation.

| Height | Matchings | Simple edges | Core histogram | Color histogram |
| ---: | ---: | ---: | --- | --- |
| 128 | 64 | 2,110 | 31 of degeneracy 1, 33 of degeneracy 2 | 39 use 2, 25 use 3 |
| 1,024 | 512 | 238,118 | 2 of degeneracy 1, 510 of degeneracy 2 | 2 use 2, 510 use 3 |
| 2,048 | 1,024 | 1,092,016 | All 2 | All 3 |
| 4,096 | 2,048 | 4,987,434 | All 2 | All 3 |
| 8,192 | 4,096 | 22,354,182 | All 2 | All 3 |
| 16,384 | 8,192 | 98,790,900 | All 2 | All 3 |

At \(h=16{,}384\) the directed list had \(100{,}079{,}622\) events. The SHA-256 of the verified color arrays, in matching order, was \(\texttt{4eec51d8becb28653457bdf1c77b7486b080d0622776af44af2f9c836af4a0ab}\). These computations use the hypotenuse test \(z\le h-1\) even when the vertical alternative falls outside the strip.


## Bounded changes of the common permutation

Suppose that \(\sigma,\sigma_t\) are dyadic isometries and that, for some constant \(D\), some signs \(\epsilon_t\), and integers \(b_t\),
\[
  |\sigma_t(i)-\epsilon_t\sigma(i)-b_t|\le D
\]
at all indices. The same lower bound holds with these matching-dependent column permutations. Choose a power of two \(B>2D\). For \(i\equiv j\bmod B\), preservation of dyadic congruences implies that the two errors above are congruent modulo \(B\). They differ by at most \(2D<B\), so they are equal. Consequently
\[
   |\sigma_t(i)-\sigma_t(j)|=|\sigma(i)-\sigma(j)|.
\]

Run the edge-count proof with \(B\mid r\). There are still \(\Omega_B(N\log N)\) eligible triangles. In the parameter boxes take \(4B\mid n\) in place of \(4\mid n\), giving a positive density of coprime pairs for fixed \(B\). For the selected \(i,j\), congruence of the common columns modulo \(B\) implies \(i\equiv j\bmod B\). Hence every selected event still has the required physical gap in its chosen matching.

This argument also rules out a class of direct coloring rules. Allow each dyadic matching to choose any rule using only the bottom \(e\) binary digits of the odd index, the even index, and the column. Take \(B\ge2^e\) as well. The two selected indices agree modulo \(B\), as do their two images under \(\pi_t\) and under \(\sigma_t\). Every such rule therefore leaves \(\Omega_{D,e}(N^2\log N)\) in-strip monochromatic edges in the family. The unrestricted chromatic number can still be smaller than the degree-based bound.

## The first larger benchmark with 3-cores

At \(h=32{,}768\), the same tree permutation produced \(438{,}182{,}193\) directed events and \(433{,}880{,}536\) simple edges. Of the \(16{,}384\) matchings, \(13{,}815\) had degeneracy two and \(2{,}569\) had degeneracy three. The first nonempty 3-core, in matching \(t=2\), had \(4{,}839\) vertices and \(9{,}186\) edges. The smallest nonempty 3-core, in matching \(t=2{,}432\), had \(2{,}619\) vertices and \(4{,}766\) edges.

All \(16{,}384\) matchings nevertheless admit 3 colors. For each nonempty 3-core, the verifier requires each vertex to take at least one of three colors and forbids every edge from sharing a color. A satisfying assignment supplies colors on the core. Reverse elimination extends them to the whole matching. The verifier checks every edge after extension. The SHA-256 of the final colors, in matching order, was \(\texttt{cb7799b7c8ed702901941d568c253db45945907f3a4060ef77553045c4b1913f}\). The [script](dyadic_matching_check.py) reproduces this calculation with arguments \(\texttt{32768 --chunk 2048 --three}\). It outputs the digests of the two recorded vertex sets as well.

## Permutations chosen by matching prefix

In the XOR cover, fix a power of two \(B\) and a residue \(a\bmod B\). Suppose the column permutation is common on the single class \(t\equiv a\bmod B\) and is a dyadic isometry there. Its choice elsewhere is unrestricted. The total number of true in-strip edges in this class of matchings is still \(\Omega_B(N^2\log N)\).

Use only central indices \(i\equiv0\bmod B\), horizontal shifts \(r\equiv0\bmod B\), and signed positive vertical legs \(d\equiv2a+1\bmod 2B\). The chosen \(j\) is zero modulo \(B\) because its column residue agrees with that of \(i\). The chosen leaf index \(k=i+(d-1)/2\) is \(a\bmod B\). Hence the matching \(t=j\mathbin{\mathrm{XOR}}k\) is in the specified class. The primitive count with \(4B\mid n\) still applies. Its odd primitive leg is invertible modulo \(2B\), so one residue class of odd dilation factors produces the required \(d\). For fixed \(B\) the count retains order \(N\log N\). Thus choosing an unrelated common permutation for each of a fixed number of low-bit prefixes cannot keep mean degeneracy bounded.

There is a sharp cutoff for the restricted coloring rule itself. Continue to take \(h=2N\) with \(N\) dyadic and \(B\) a power of two. Suppose the column permutation is common on the class \(t\equiv0\bmod B\). Within each matching allow a different arbitrary coloring rule on the residues modulo \(B\) of the odd index, the even index, and the column. If \(h\ge16B^2+2\), such rules cannot produce a proper coloring for the whole family.

Indeed take \(i=8B^2\) and \(k=0\). At least one of the two values \(\sigma(i)\pm B\) belongs to \([0,N-1]\). Write it as \(\sigma(j)\). Then \(j\equiv i\equiv0\bmod B\). The matching \(t=j\mathbin{\mathrm{XOR}}k=j\) is in the designated class. Its two labels indexed by \(i,j\) agree in all three residues used by the rule. The chord from the odd point of \(i\) to the even point of \(j\) has horizontal leg \(8B\), vertical leg \(16B^2-1\) in absolute value, and hypotenuse \(16B^2+1\). Its two alternative rows are 1 and \(16B^2+2\), so this is an actual in-strip rival.

Conversely if \(h\le16B^2+1\), the coloring by \(i\bmod B\) excludes all such edges in every dyadic matching for any column isometry, even one chosen separately for each matching. A possible same-color edge has \(X=8Bm\ne0\) and \(Y\) odd. If its length \(Z\) were integral, the positive factors \((Z-|Y|)/2\) and \((Z+|Y|)/2\) would have opposite parities and product \(16B^2m^2\). Hence the even factor is divisible by \(16B^2\), giving \(Z\ge16B^2+1>h-1\). Together these two bounds determine the low-digit resolution on the stated dyadic-height sequence.

## Independent sampling from a common distribution

Suppose the matching-dependent permutations \(\sigma_t\) are sampled independently from any common law on permutations of \([0,N-1]\). They need not be dyadic for the edge count. By linearity of expectation, the expected total number of true in-strip edges is the same as if all matchings had received one shared sample. It is at least \(cN^2\log N\) by the first result.

Put \(Z_t=2|E(G_t)|/N^2\), so \(0\le Z_t\le1\), and put \(\mu=\sum_t\mathbb E Z_t\). Convexity gives \(e^{-x}\le1-(1-e^{-1})x\) on \([0,1]\). Hence independence and Markov's inequality give
\[
 \Pr\!\left(\sum_t Z_t\le\mu/2\right)
 \le e^{\mu/2}\prod_t\mathbb E e^{-Z_t}
 \le \exp\big(-(1/2-e^{-1})\mu\big).
\]
Since \(\mu\gg\log N\), except with probability \(O(N^{-c'})\) the mean degeneracy is at least \(c''\log N\) for absolute positive constants. Sampling a different isometry for each matching from the same distribution therefore preserves the obstacle to bounded degeneracy with high probability.

## Binary lifting and an adaptive permutation check

The [one-matching verifier](lift_one_matching.py) generates edges for a single XOR matching without testing every index for every Pythagorean shape. For fixed horizontal sign, vertical sign, and positive shape \((8r,d,z)\), put \(D=(\pm d-1)/2\). Starting at the odd endpoint \(i\), the candidate label at the even endpoint is \(j=(i+D)\mathbin{\rm XOR}t\) modulo \(N\). Lift the congruence
\[
 \sigma(j)-\sigma(i)=\pm r \pmod{2^k}
\]
from \(k\) to \(k+1\). The two possible children \(i\) and \(i+2^k\) flip the next bit of both \(j\) and \(i\), and hence the next bit of both permuted values. The signed difference modulo \(2^{k+1}\) is the same for both children. The search therefore takes both or neither. At full length it checks both endpoint row ranges and the actual signed horizontal difference. The graph used here keeps every shape with \(z<h\), including those whose alternative vertical would cross the strip boundary. The 3-core is thus computed on the stronger graph defined in the matching note.

For a uniformly random binary tree isometry, fix \(i\) modulo \(2^k\) and put \(v=v_2(r)<k\). If \(i,j\) do not first differ in bit \(v\), they cannot solve the congruence. Otherwise, conditional on the first \(v+1\) output bits, the two paths below their split use disjoint, independent coin flips. Their output difference is uniform among the \(2^{k-v-1}\) residues of valuation \(v\). The expected number of successful nodes at this level is at most \(2^{v+1}\). Before the split, at most \(2^{v+1}\) nodes in total are tested. The expected number of visited nodes is therefore \(O(2^v\log N)\) per signed shape. Euclid's parametrization gives \(O(N\log^2 N)\) for the sum of \(2^v\) over shapes, including odd dilations with \(z<h=2N\). Indeed in a dyadic parameter box of side \(M\) the primitive weight sum is \(O(M^2\log(2M))\), and each primitive shape has \(O(N/M^2)\) dilations. Thus one random matching costs \(O(N\log^3 N)\) expected search nodes, apart from preparing the shape table and testing or coloring emitted edges. This expectation concerns independent fair flips, not the deterministic hash used in the checks.

At \(h=32768\) the lifting check independently reproduced the two recorded 3-core vertex digests at \(t=2\) and \(t=2432\) for seed zero. At \(h=131072,t=2\), seed zero, the lift visited 3,447,656 nodes and found 125,790 simple edges. The 3-core had 38,489 vertices and 83,928 edges and admitted a 3-coloring; the full coloring was checked on every edge.

A second check lets each matching choose its first tree seed whose graph has an empty 3-core. Run [the permutation menu](matching_permutation_menu.py) at \(h=32768\) with the default chunk and last seed at least 8. Here are the counts still unresolved after each seed.

| Last seed tried | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Remaining matchings | 2569 | 633 | 171 | 64 | 22 | 6 | 1 | 1 | 0 |

All 16,384 XOR matchings at this height have a 2-degenerate realization among these nine tree permutations. The SHA-256 of the selected seed vector in matching order, little-endian signed 16-bit format, is 4fd812c3691346ec5f6a7108c940939ff5c54f80fef13e5e53a39b229ae1ec9f. This is a finite statement about sparse blocks. The logarithmic average degeneracy theorem above applies to any single fixed permutation used across all matchings.

