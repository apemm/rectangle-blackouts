# A global lower bound on the optimum below threshold

For sufficiently large \(h\) there is a globally valid filled board of width \(O(h^2)\) containing
\[
 \gg h^2/(\log h)^{1/3}
\]
doubles. Hence for every \(m\ge1\),
\[
 f(h,m)\ \ge\ m+c\,\frac{\min(m,h^2)}{(\log h)^{1/3}}
 \tag{1}
\]
with an absolute \(c>0\). One may round the right-hand side up. The argument uses the deterministic obstruction table of the [stride-four chain](../../papers/extremal/drafts/upper_bound/part6_table.tex). All rectangle comparisons are global. The number of retained labels is smaller than \(q_h=\lfloor h^2/4\rfloor\).

## A large class in the first period

Use the menu \(\{1\}\) and the full color budget \(B=\lceil(\log h)^{x_1}\rceil\) in the stride draft. Its one-stride exponent \(x_1>1\). For an odd positive \(T\in[h/4,h/2]\) let
\[
 g(T)=\prod_{\substack{p^e\Vert T\\p\ {\rm split\ in}\ \mathbb Q(\sqrt5)}}(2e+1).
\]
The [ideal count](../../papers/extremal/drafts/upper_bound/part7_heavy.tex) gives \(\kappa_T\le C_0 g(T)\) throughout this interval. Restrict attention to \(g(T)\le B/(8C_0)\). These are light diagonals; their index graphs of forbidden distances have degree at most \(2\kappa_T\le B/4\).

Each such \(T\) supplies 32 nonempty index classes \(i\bmod32\) (the diagonal fixes the other coordinate of the region type). Each class has \(\gg h\) indices even after removing labels with an endpoint among the fixed number of rows in (R-a), (R-b) or (R-c). Indeed the available interval of odd rows has length at least \(h/2-O(1)\). We may discard just these boundary labels at this stage.

On the remaining indices of a class form a graph. Include its forbidden-distance edges, its short-distance edges \(R_{\rm FF}^+\), and every edge in the bounded-shape part of the three same-class mixed families of [structure proposition for the in-class families](../../papers/extremal/drafts/upper_bound/part5_classes.tex) (the proposition labeled prop:inclass). Here the shape cutoffs are \(\max(p_\lambda,q_\lambda)\le h^{1/2}/32\) and \(|U'|\le h^{1/2}/32\) as in the definition of the relocation sets. The same-class graphs depend only on the two indices, before any coloring.

There are \(O(h(1+g(T)))\) edges. Forbidden distances contribute \(O(hg(T))\), and short-distance edges have degree at most 12. In \(R_{\rm IV}\) a given shape has at most \(O(h/q_\lambda+1)=O(h/q_\lambda)\) designated ends; the designated end and the shape determine the other end. The series \(\sum_\lambda 1/q_\lambda\) converges. For the two other mixed families a shape and a fixed role and filler row also determine the other end. The admissible designated indices have count \(O(h/|U'|+1)=O(h/|U'|)\) by the residue-class estimate in the proposition, and \(\sum 1/|U'|\) converges. All role and row multiplicities are bounded constants.

A graph with \(n\) vertices and \(E\) edges has an independent set of size at least \(n^2/(n+2E)\): in a random vertex order select the vertices earlier than all their neighbors and apply Cauchy's inequality to \(\sum_v1/(1+\deg v)\). We obtain \(\gg h/g(T)\) indices. Put precisely this set in color zero on its diagonal and type. Extend to a proper forbidden-distance coloring of the remaining indices using colors \(1,\ldots,B-1\), possible by the degree bound. On unselected light diagonals use any proper coloring. Colors on different diagonal-type pairs may be prescribed independently.

Take the admissible primes minimizing the cross-class counts as in [the assembly proof](../../papers/extremal/drafts/upper_bound/part8_assembly.tex). The uniform bound in its Theorem U holds for any class datum. The sets (R-a) through (R-f), apart from the bounded-shape designated ends treated separately, remove \(O(h^{11/6}\log h+h^{9/5+1/100}+h^{3/2})\) labels in all. The bounded-shape designated ends in \(\mathrm{Bad}_{\rm split}\) remove none of our chosen vertices: the only other vertices of color zero in that diagonal and type are in the chosen independent set. The exceptional set (R-g) concerns vertices already offered for relocation from \(\mathrm{Bad}_{\rm split}\). The proof of the obstruction table therefore gives a clean chain for these choices of the colorings. Its geometric statement holds pointwise in the colorings; a positive-probability relocation of the deleted labels is unnecessary for a partial board.

## Weight of the selected diagonals

The reciprocal sum over all odd \(T\) in this interval obeys
\[
 \sum_{h/4\le T\le h/2,\ T\ {\rm odd}}\frac1{g(T)}
 \gg h(\log h)^{-1/3}.
\]
Here is a lower bound using only prime estimates in fixed residue classes. Set \(y=h^\delta\) for a sufficiently small fixed \(\delta>0\). Consider odd squarefree \(d\) supported on primes at most \(y\), with weights \(w_d=1/(d g(d))\). Their total is
\[
 \prod_{2<p\le y}\left(1+\frac1{p g(p)}\right)
 \asymp(\log h)^{2/3},
\]
because the split primes have density one half and \(g(p)=3\) there, while \(g(p)=1\) at the other primes. In the normalized product distribution,
\(\mathbb E\log d\le\sum_{p\le y}\log(p)/p=O(\log y)\).
Choose \(\delta\) so this is at most \((\log h)/8\). At least half the weight then has \(d\le h^{1/4}\). For each retained \(d\) use primes \(\ell\in[h/(4d),h/(2d)]\); there are \(\gg h/(d\log h)\) by the prime number theorem, uniformly in this range of \(d\). Such a prime exceeds \(\sqrt h\) for large \(h\), so \(\ell\) is distinguished in \(T=d\ell\), and all the resulting \(T\)'s are distinct. Also \(g(T)\le3g(d)\). Summation proves the lower bound. The fixed-modulus reciprocal-prime input follows, for example, from [Williams' Mertens theorem](https://people.math.carleton.ca/~williams/papers/pdf/057.pdf).

Discarding \(g(T)>B/(8C_0)\) costs only \(O(h/B)\) in this reciprocal sum. Summing the independent-set bound over the retained diagonals, and then subtracting the power-saving number of deleted labels, leaves \(\gg h^2/(\log h)^{1/3}\) surviving color-zero doubles. At least a fixed fraction lies in one of the 512 regions. All its color-zero columns have \(t=\rho_s<16\ell\) and \(n=i+pt+b_\tau\), so they fit within \(4(16\ell p+h)+O(1)=O(h^2)\) consecutive physical columns regardless of the other colors. Take this interval in the actual clean chain, retaining all its original cells. A restriction of a valid blackout identifies the rectangles that remain in its grid.

Finally let \(D\) be the number of doubles obtained in this interval of width \(W\). For \(m<W\) subdivide it into \(\lceil W/m\rceil\) consecutive pieces of length at most \(m\). Some piece contains at least \(\lceil D/\lceil W/m\rceil\rceil\) doubles. Extend that piece to \(m\) columns in the same infinite clean chain. For \(m\ge W\) extend the full interval. Every column is nonempty. This proves (1).
