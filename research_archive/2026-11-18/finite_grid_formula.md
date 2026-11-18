# A finite formula for size and multiplicity at any dimensions

Let \(N=hm\). Enumerate the grid rectangles by pairing distinct segments with equal squared length and equal doubled midpoint. Each resulting pair gives the two diagonals of one rectangle. Let \(\mathcal E\) be the inclusion-minimal distinct symmetric differences of two rectangle corner sets. When there are fewer than two rectangles this family is empty.

Put \(B=2^{N+1}\) and compute the positive integer
\[
 Z=\sum_{\mathcal J\subseteq\mathcal E}(-1)^{|\mathcal J|}
        B^{|U_{\mathcal J}|}(1+B)^{N-|U_{\mathcal J}|},
 \qquad U_{\mathcal J}=\bigcup_{E\in\mathcal J}E.
\]
Then for every \(h,m\ge1\) the two requested finite quantities are
\[
 f(h,m)=\left\lfloor{\lfloor\log_2 Z\rfloor\over N+1}\right\rfloor,
 \qquad a_h(m)=\left\lfloor Z/B^{f(h,m)}\right\rfloor .
\]

Indeed two rectangles have identical visible corners precisely when their symmetric difference is entirely black. A valid blackout contains none of the members of \(\mathcal E\). For a fixed union \(U\), the total weight of all sets containing it, with weight \(z\) for each black point, is \(z^{|U|}(1+z)^{N-|U|}\). Inclusion-exclusion gives the entire size enumerator \(F(z)\) and \(Z=F(B)\). Each coefficient of \(F\) is less than \(B\), so the base-\(B\) digits of \(Z\) are the counts by size. Its highest occupied digit gives the maximum size and the digit itself gives its multiplicity.

[The checker](finite_grid_formula.py) groups terms with the same union and discards zero coefficients. It also exhausts all black subsets and compares their visible presentations directly. The two methods agreed on the following labeled grids.

| Grid | Maximum size | Number attaining it |
|---|---:|---:|
| \(1\times5\) | 5 | 1 |
| \(2\times2\) | 4 | 1 |
| \(2\times3\) | 4 | 12 |
| \(2\times4\) | 5 | 32 |
| \(2\times5\) | 6 | 80 |
| \(3\times3\) | 5 | 53 |
| \(3\times4\) | 6 | 224 |
| \(3\times5\) | 7 | 892 |
| \(4\times4\) | 7 | 316 |

The sum can involve exponentially many distinct unions. It gives a direct, finite alternative to optimizing over candidate blackouts and a small-grid audit of the coefficients. Its present form does not simplify \(f(h,m)\) below the threshold or identify a dominant sea for the large-width asymptotic. For the existing fixed-height transfer method see [the enumeration paper](../../papers/enumeration/sections/sec7_height.tex).
