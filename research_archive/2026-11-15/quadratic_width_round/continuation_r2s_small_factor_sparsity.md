# Effective sparsity for growing small R2s factors

15 November 2026. The positive-offset R2s supports with
\(\min(a,b)\le B\) have the effective bound
\[
 \#\{\text{support parameter tuples}\}
 \le C\sqrt h\,B^{5/4}\mathcal D_h,\qquad
 \mathcal D_h=\max_{1\le q\le32h^3}\tau(q)=h^{o(1)},
 \quad 1\le B\le h.                                  \tag{1}
\]
This covers arbitrary row increments, unlike the bounded-increment
Siegel theorem. In particular \(B=h^{2/5-\varepsilon}\) gives a
sublinear exceptional row set and a subquadratic exceptional label
set for every fixed \(0<\varepsilon<2/5\).

The result counts potential supports and labels. It does not give
a full-occupancy repair of their columns.

The full row family already has the bound
\(h^{5/6+o(1)}\) from
[the small-variable argument](continuation_r2s_small_u_refinement.md).
Thus (1) is additional parameter information, not a better bound for
all R2s rows or a new method of eliminating every support. When both
estimates apply, their minimum is available. Ignoring subpower factors,
the new bound is smaller only when \(B<h^{4/15}\).

## 1. Keep the smaller factor but retain the full norm gap

Use the positive-offset constant-sea equations
\[
 \begin{gathered}
 4ab=T^2+\delta^2,\quad U=T+a+b,\quad
 n={TU\over\delta},\\
 T,\delta,a,b>0,\qquad n\le h,\qquad
 \delta^2\le2X,\qquad 0<X<U.
 \end{gathered}                                                   \tag{2}
\]
All parameters are integers. Set \(b_0=\min(a,b)\). The symmetric
formula for \(U\) gives
\[
 U={ (T+2b_0)^2+\delta^2\over4b_0},\qquad
 n={T\{(T+2b_0)^2+\delta^2\}\over4b_0\delta}.          \tag{3}
\]
This interchange does not assert that locality holds with the
smaller candidate core displacement \(T+b_0\). Instead use the
weaker symmetric consequence
\[
                \delta^2\le2U.
\]
Since \(n=TU/\delta\),
\[
                         \delta T\le2n\le2h.        \tag{4}
\]
On the other hand, (3) gives
\[
                         n\ge{T^3\over4b_0\delta}.
\]
Combine this with (4):
\[
                       T^4\le8b_0h^2,\qquad
                       T\le8^{1/4}b_0^{1/4}\sqrt h. \tag{5}
\]
No assumption that \(T\) is larger than \(b_0\) is needed.

## 2. Count increments by divisors

Clearing denominators in (3) gives
\[
       4b_0n\delta=T(T+2b_0)^2+T\delta^2.
\]
Thus every possible increment is a positive divisor:
\[
                         \delta\mid T(T+2b_0)^2.    \tag{6}
\]
For fixed \(b_0,T,\delta\), formula (3) determines \(n,U\)
and the other factor. There are at most two choices for which
factor is \(a\) in the original orientation, and a fixed number
of horizontal reflections. The actual parity, congruence,
strip, and integrality tests can only discard these candidates.

When \(b_0\le B\le h\), (5) gives \(T\le2h^{3/4}\le2h\).
Therefore
\[
                         T(T+2b_0)^2\le32h^3.
\]
Summing (6) over (5) proves
\[
 \begin{aligned}
 \#\{\text{tuples}\}
 &\le C\mathcal D_h\sum_{b_0\le B}b_0^{1/4}\sqrt h\\
 &\le C\mathcal D_h\sqrt h\,B^{5/4}.
 \end{aligned}
\]
These are support parameter tuples up to horizontal translation.
Each tuple determines its two row endpoints, so the number of
incident row vertices is bounded by twice the same expression.

The complete row graph with any one fixed factor \(b_0\) therefore
has \(h^{1/2+o(1)}\) edges through height \(h\). In the special
unit-factor parametrization,
[the exact formula](continuation_r2s_unit_factor_structure.md)
also gives \(m\le\sqrt{h/8}\) directly.

## 3. Growing cutoffs and exact label cost

For fixed \(0<\varepsilon<2/5\), take
\(B=\lfloor h^{2/5-\varepsilon}\rfloor\). Equation (1) gives
\[
 \begin{split}
 \#\{\text{incident rows}\}
    &\le h^{1-5\varepsilon/4+o(1)},\\
 \#\{\text{complete row-pair labels incident to them}\}
    &\le h^{2-5\varepsilon/4+o(1)}.                 \tag{7}
 \end{split}
\]
The second bound uses at most \(h\) original labels per row.
It also applies after any partition into row-color products:
each original label belongs to exactly one product, so the
partition does not multiply the exceptional label count.

For an explicit conditional relocation budget, let
\(\mathcal T(h)\ge1\) be a separately justified relocation factor,
with internal cost \(O(n_E\mathcal T(h)^2)\) for \(n_E\) labels.
Set
\[
 B=\left\lfloor
 \frac{\eta h^{2/5}}
 {\mathcal T(h)^{8/5}\mathcal D_h^{4/5}
                      \log(2h)^{8/5}}
 \right\rfloor,                                      \tag{8}
\]
where \(\eta>0\) is fixed. Whenever \(1\le B\le h\), (1) yields
\[
                  n_E\mathcal T(h)^2
                    \le C\eta^{5/4}\frac{h^2}{\log^2(2h)}.       \tag{9}
\]
If \(\mathcal T(h)=h^{o(1)}\), then
\(B=h^{2/5-o(1)}\).

The cutoff and count are effective. They are independent of the
nonquantitative threshold in
[the bounded-parameter bipartite theorem](continuation_r2s_bounded_parameter_bipartite.md).

## 4. What this permits and what it leaves open

Deleting the implicated point options destroys every targeted R2s
support, because the collision condition is monotone in the black
support. The numerical relocation budget in (9) is available
whenever its separate placement and interface hypotheses hold.

Neither assertion chooses a legal replacement singleton at an
erased double column. Endpoint row-color filling, odd-stub repair,
or another occupied repair must still verify its P and higher
collision conditions. In particular, the support count does not
justify reusing an arbitrary replacement row at the original
column.

Conversely, a source-only row bound or an edge count of order
\(h^{1/2+o(1)}\) does not imply a bounded chromatic number. The
remaining large-factor family is not shown to be sparse enough
for a constant coloring, and the full R2s row-coloring problem
remains open.

The complete saved proof passed independent written review, including
the symmetric use of U, the divisor argument, the growing cutoff,
the relocation exponents, and the occupancy limitation.

