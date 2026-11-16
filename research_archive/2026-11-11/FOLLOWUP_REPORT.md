# Follow-up on the quadratic threshold attack

11 November 2026. The quadratic threshold and general dominance questions remain open. This pass addresses the two questions in `quadratic_threshold_reattack.md`. It finds all-double counterexamples, proves sharper bounds for the monotone P problem, and repairs the diagonal argument. No source manuscript or earlier research note was changed. Nothing was committed.

## 1. Valid all-double squares exist

A valid 7 by 7 blackout has column pairs

\[
 17,\quad67,\quad15,\quad35,\quad36,\quad23,\quad12.
\]

Every column has exactly two black cells. Three separate rectangle enumerations agree on 640 rectangles, all with different white presentations. An explicit certificate lists all 184 rectangles with at most two white corners. Presentations with at least three white corners determine their rectangle automatically.

Opposite-parity labels also allow all-double squares. A valid 8 by 8 example is

\[
 14,\quad16,\quad47,\quad27,\quad67,\quad12,\quad78,\quad18.
\]

Its row-pair graph is \(K_{2,4}\), on parts \(\{1,7\}\) and \(\{2,4,6,8\}\). All 1192 rectangle presentations are distinct.

Unused rows are not necessary either. The 8 by 8 word

\[
 38,\quad16,\quad78,\quad14,\quad67,\quad18,\quad12,\quad58
\]

is valid, uses every row, and every label joins opposite physical parities. Its independent checker also verifies all 1192 rectangles.

These examples answer the broad existence question. They do not answer the saturated question: no example here has all \(q_h=\lfloor h^2/4\rfloor\) labels of a balanced complete bipartite row graph. In a saturated all-double board every white point has an axis singleton owner. In these examples some tilted singleton presentations have no axis owner, so they are harmless.

See [the counterexample note](all_double_square_counterexample.md), [the 7 by 7 finite certificate](all_double_7x7_weak_rectangles.md), and [the independent all-rows-used check](all_double_rows_used_h8_independent_check.json).

## 2. Bounds for the monotone P partition

Let \(\chi_{\mathrm{mon},P}(h)\) be the least number of classes with distinct \(i\), nondecreasing \(j\), and no pair satisfying the square test in the question. Then

\[
 \frac{2h}{3}-O(1)
 \le \chi_{\mathrm{mon},P}(h)
 \le O(h\log h).
\]

The lower bound is an explicit clique: one full fixed-\(i\) class, together with a decreasing family connected to it by scaled 3-4-5 triangles. If the actual white-endpoint containment condition is imposed, the same construction gives \(5h/8-O(1)\).

The upper bound colors each constant-offset diagonal separately and sums its possible signed Pythagorean gaps. The total number of integer right triangles with hypotenuse below \(h\) is \(O(h\log h)\). Every resulting class has Lipschitz constant one.

Two distinctions matter for the proposed linear construction:

- Monotonicity alone costs exactly \(K=\lfloor h/2\rfloor\), not \(A+K-1\). Constant-\(j\) classes attain this.
- The archived independent private-coin thinning typically leaves no eligible monotone class longer than \(O(h^{31/32})\). Consequently its usual realizations require \(\Omega(h^{33/32})\) colors for a monotone cover. This is a barrier to that implementation, not a superlinear lower bound for the underlying graph. Correlated palettes remain possible.

See [the proofs](monotone_p_palette_progress.md). The absolute linear upper bound remains the main open combinatorial step.

## 3. The boundary-safe diagonal theorem

If every 45-degree rectangle contains at most two black points, the bipartite incidence graph of occupied slope-\(+1\) and slope-\(-1\) lines is a forest. Its edges are the black cells.

The proof chooses a minimum-index line on a hypothetical cycle. Convexity of the board puts a fourth corner inside the board, producing a rectangle with at least three black corners. This works at both horizontal ends. It does not require the components to be zigzag paths.

Writing \(C\) for the number of occupied components and \(E\) for the number of empty diagonal lines gives, for an all-double saturated board,

\[
 C+E=2h-2.
\]

For a valid equality board with \(t\) singleton columns, let \(\beta_{a,b}\) denote the cycle rank for the primitive perpendicular directions \((a,b),(-b,a)\), with \(a,b>0\). Then

\[
 \boxed{\sum_{a,b}\beta_{a,b}
 \le \bigl(\lceil h/2\rceil-1\bigr)t.}
\]

Each cycle can be removed by deleting a black edge of a three-black rectangle. Different selected rectangles require distinct white completion points. For the full balanced row family, these points must be in singleton columns, in the same part as that column's black row. This supplies one budget across all slopes.

This remains a necessary condition. Neither the repaired identity nor the cycle-rank bound forces a positive cycle rank for every saturated placement. Thus \(m_h\ge q_h+1\) is still unproved.

See [the forest and cycle-budget note](saturated_diagonal_forest.md) and [its independent audit](diagonal_forest_independent_audit.md).

## 4. The constant-offset gap formula needed correction

In the current scaffold the square test is

\[
 20d^2-4Td+T^2=L^2.
\]

The copied divisibility-by-7 formula came from a different row step. Here the 3-4-5 witnesses are \(d=-T\) and \(d=T/5\) when \(5\mid T\). For example, the minimum absolute arithmetic gap at \(T=7\) is 7, not 1. Even \(|T|/5\) is only an upper bound, not a general equality.

The architecture consisting of one separate block for every consecutive, fully occupied constant-offset run still needs \(\Omega(h\log h)\) blocks. The proof uses a central interval where all scaled 3-4-5 white endpoints fit, so it does not depend on the incorrect minimum-gap formula. It does not rule out reusing separated pieces in one block.

See [the audited gap calculation](constant_offset_gap_audit.md).

## 5. What is still needed

The most direct remaining construction task is a correlated monotone P-free partition with \(O(h)\) classes. Even that would leave cross-block even-odd-even angles, mixed collisions, and a compatible filler rule.

For a strict lower bound on the threshold, the full balanced row-pair family must enter the argument. The broad no-singleton claim, the bipartite variant, and the all-rows-used variant are false. A forced tilted completion or a forced positive cycle rank for every saturated placement would be sufficient.

No general dominance theorem or unconditional counting asymptotic was established in this pass.

## Verification status

The finite witnesses have exact, solver-free presentation checks. The 7 by 7 and first 8 by 8 examples were rerun after discovery using three rectangle parameterizations. The 7 by 4 boundary example was rerun separately and has 152 distinct presentations. The gap proof and diagonal forest proof received independent review.

Small SAT exclusion records are exploratory computation. They do not come with an independently checked UNSAT proof and are not used in the analytical results. The corresponding search files record solver outcomes and timing separately from the witness certificates.
