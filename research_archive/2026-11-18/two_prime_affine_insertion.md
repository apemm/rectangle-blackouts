# Quadratic placement in one unbroken affine sea

For every sufficiently large height \(h\), there is a filled interval of \(h^2\) columns carrying
\[
 \Omega\bigl(h^2/(\log h)^6\bigr)
\]
distinct pairs of an odd and an even row as doubles. Outside this interval the board continues indefinitely in the same affine sea. The resulting infinite board has no in-strip tilted corner triple, black mixed quadruple with nonvertical side, or rival to any vertical parity owner. Every finite restriction is a valid blackout. The conclusion concerns a construction in a single affine one-parity sea. It does not cover every edge.

Choose a prime \(h/13<p<h/6\), for instance by applying Bertrand's postulate to \(\lfloor h/12\rfloor\) at large heights. Let \(J\) be the top \(p\) even rows in the strip. Put
\[
 A=\lfloor c_1 h/(\log h)^4\rfloor,\qquad
 B=\lfloor c_2 h/(\log h)^2\rfloor,
\]
where \(c_2>0\) is a sufficiently small absolute constant and then \(c_1/c_2\) is sufficiently small. Let \(I\) be the odd rows in \(1,\ldots,A\), and choose a second prime \(A<q<2A\). For large \(h\) the primes are distinct. The physical odd rows in \(I\) are distinct modulo \(q\). Independently choose \(v\bmod p\) and \(w\bmod q\), each uniformly from the nonzero slopes whose \(1+\text{slope}^2\) is a quadratic nonresidue. There are order \(p\) and order \(q\) choices respectively, by the elementary character count in [the separated-row construction](separated_row_tiles.md).

At every column \(x\) put the unique even row \(b(x)\in J\) satisfying \(b(x)\equiv vx\bmod p\). Only add an odd row \(a\in I\) at a column satisfying \(x\equiv wa\bmod q\). Thus a label \((a,b_0)\) has a single permissible column class modulo \(pq\). Distinct actual labels have disjoint classes. All points of a single parity obey a nonisotropic affine line congruence and each actual row is determined by its residue. Consequently the one-role proof in the separated-row construction excludes all tilted and nonvertical mixed supports entirely in that parity. It applies to arbitrary subsets of the odd track.

## Single insertions

For \(a\in I\) and \(b\) among the top \(B\) members of \(J\), retain as targets the labels \((a,b_0)\) determined by
\[
 b_0\equiv(1+v^2)b-v^2a\bmod p .
\]
Exclude \(b\equiv a\bmod p\), losing \(O(A)\) targets. All remaining targets are distinct. The [single-insertion criterion](affine_sea_double_obstruction.md) excludes an in-strip corner triple at the inserted point since \(2\min J-A>h\). At its uniquely possible sea pivot of row \(b\), any dangerous nonzero vertical step \(y\) has \(|y|\le A+2B\). Each signed divisor of \(y(a-b)\) excludes at most one even slope. Summing \(\tau(|y|)\tau(|a-b|)\), the average over \(a,b\) of the number of bad slopes is
\[
 O\bigl((A+B)(\log h)^2\bigr).
\]
Indeed \(\sum_{1\le y\le A+2B}\tau(y)=O((A+B)\log h)\), and \(\tau(|a-b|)\) has mean \(O(\log h)\) on this box by summing over one interval of length greater than \(\sqrt h\). The usual small-divisor bound is uniform in the translated interval, including intervals in a fixed parity progression.

For each \(a,b\) outside the discarded congruence, the same single-insertion proof gives \(O(\sqrt{hA}\log h)\) slopes permitting a vertical rival. A mixed quadruple with this single odd point has odd total row sum. Dividing by the order-\(p\) choice of slopes, the expected proportion of targets lost to individual obstructions is \(O(c_2)+o(1)\).

## Pair constraints averaged over two slopes

Count the signed differences of columns of two inserted points arising from a tilted black triple with one even sea point, or a nondegenerate mixed support with two even sea points. Count over all \(I\times J\) labels before restricting to targets. A count with multiplicity is sufficient. For each normalized geometry and fixed slopes compatible with its same-role displacements, one even sea point fixes the horizontal translation modulo \(p\), so the geometry prescribes the actual labels of both inserted points. One odd point also fixes the translation modulo \(q\). Thus the expected total number of forbidden pair differences is at most the expected number of such geometries up to translation.

For a triple with fixed rows, choose its tilted pivot. The horizontal legs \(u,u'\) have product equal to the negative of the product of the two vertical legs. Both vertical components are nonzero, hence the number of horizontal placements up to translation is bounded by a constant times \(\tau(|L_1L_2|)\), where the \(L_i\) are its two vertical leg differences.

For a mixed support fix its four rows and designate the side and diagonal, with displacement vectors \((u,y),(u',z)\) and \(u\ne0\). If \(z^2\ne y^2\), factor \((u-u')(u+u')=(z-y)(z+y)\). For each choice, perpendicularity to the doubled midpoint difference fixes the remaining horizontal translation between the two chords. If \(z^2=y^2\), orient both chords with the same positive horizontal component \(u\). The only nondegenerate orientation has \(z=-y\ne0\). If the horizontal displacement of the first endpoints is \(t\), and the vertical doubled midpoint difference is \(M_y\), then \(2ut=-yM_y\). Its right side cannot vanish, since \(y\ne0\) and \(M_y=0\) would force zero midpoint difference. We again have a constant times \(\tau(|L_1L_2|)\) choices, with \(L_1,L_2\) bounded-coefficient homogeneous linear forms in the prescribed rows.

On every box of rows used here these bounds average to \(O((\log h)^2)\), even after specifying which two rows of a role coincide. Identify the repeated variables first. In the case of unequal rows one may extend to the whole box for this nonnegative upper bound, setting the summand to zero where either form vanishes. If the two nonzero forms are linearly independent, choose two row variables giving a nonzero two-by-two determinant, and fix the others. Partition the two index intervals into squares of side equal to the shorter length, padding the longer final slice if necessary. Each side has length \(T\gg h^{3/4}\). The map from a square to \((L_1,L_2)\) is injective and its image lies in two intervals of length \(O(T)\). On either interval the sum of \(\tau(|n|)\) over nonzero \(n\) is \(O(T\log h)\), by summing divisors at most \(O(\sqrt h)\). Therefore \(\tau(|L_1L_2|)\le\tau(|L_1|)\tau(|L_2|)\) gives the asserted mean. If the forms are proportional, they are bounded integer multiples of a single primitive linear form, and \(\tau(|L_1L_2|)\ll\tau(n^2)\le d_3(n)\). On any interval of length \(T\gg h^{3/4}\) with \(|n|=O(h)\), this last function sums to \(O(T(\log h)^2)\). Indeed the product of the two smallest factors in an ordered triple factorization is at most \(O(h^{2/3})\). Summing \(O(T/k+1)\) with weight \(O(\tau(k))\) over such products \(k\) proves the bound. Summing over any variable with nonzero coefficient gives the same estimate on a box, since its integer values occur with bounded multiplicity in a length-\(O(T)\) interval. An identically zero factor contributes to none of the cases in which its product is required to be nonzero.

If two odd rows are distinct, they are distinct modulo \(q\); their displacement then fixes at most one compatible \(w\), at probability \(O(1/q)\). If two even rows are distinct, they are distinct modulo \(p\); their displacement fixes at most one compatible \(v\), at probability \(O(1/p)\). The restrictions are independent. Write \(n=|I|\asymp A\). For a mixed support, the contributions from equal and distinct rows of each role therefore give an expected total at most
\[
 C(\log h)^2(n+n^2/q)(p+p^2/p)=O(Ap(\log h)^2).
\]
For a triple there is one even row and the same two odd-row possibilities, giving the same bound.

## Selecting columns

For fixed slopes, assign each label its degree, counting all its forbidden differences with other labels in \(I\times J\), with multiplicity. The sum of degrees is at most twice the preceding pair count. The interval of \(h^2\) columns contains at least \(S=\lfloor h^2/(pq)\rfloor\gg h/A\) possible columns per label. Discard every target of degree at least \(S\). The expected number discarded is \(O(A^2(\log h)^2)\), a proportion \(O(c_1/c_2)\) of the original target set of order \(AB\). Together with the individual losses this is less than one half for suitable constants and large \(h\). Some choice of slopes retains order \(AB\) labels.

Place each surviving label in any order. Each forbidden signed difference with a previously placed label removes at most one candidate. The degree is below \(S\), so a permissible column remains. By the Chinese remainder theorem the chosen column supplies the required actual even row. Every column already contains its even point. Individual and pair tests eliminate every tilted triple except one concentrated in a single role, already ruled out by the modular construction. The same holds for a mixed support, since its total black row sum is even. All opposite-parity vertical rivals involve just one actual odd insertion and were checked individually. This proves the assertion, including extension in the infinite affine sea.
