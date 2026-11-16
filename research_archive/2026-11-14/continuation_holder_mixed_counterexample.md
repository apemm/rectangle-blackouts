# The Holder invariant alone does not remove mixed collisions

14 November 2026. This is a finite counterexample to a possible shortcut
in completing the Hilbert construction. It is **not** asserted to be a
subconfiguration of the actual Hilbert order.

At stride \(S=32\), take the four labels below. Columns are zero-based;
adding one to every column embeds the example in an ordinary grid.

| Column | Odd black row | Even black row |
|---:|---:|---:|
| 0 | 32,769 | 4 |
| 32 | 32,771 | 2 |
| 1,048,544 | 33,795 | 1,026 |
| 1,048,576 | 33,793 | 1,028 |

All eight black points satisfy the Hilbert consequence
\[
 (\Delta y)^2<\frac{64}{S}|\Delta x|
\]
for distinct points of the same parity. There is no tilted right angle
among the black points. In fact, every pair in different columns has
nonintegral Euclidean distance, so neither parity's F-family nor any
cross-column integral-distance P test detects the obstruction.

Nevertheless there is a mixed collision. Put
\[
\begin{aligned}
 A&=(0,32769),& B&=(32,2),\\
 C&=(1048576,33793),&D&=(1048544,1026),\\
 P&=(1048544,33793),&Q&=(1048576,1026).
\end{aligned}
\]
The points \(P,Q\) are white. The first rectangle has black side \(AB\)
and white side \(PQ\): its side vectors are
\[
 (32,-32767),\qquad(1048544,1024),
\]
whose dot product is zero. The second rectangle is axis-aligned and
has black diagonal \(CD\) and white diagonal \(PQ\).
They therefore have the same presentation \(\{P,Q\}\).

The [exact checker](check_holder_mixed_counterexample.py) verifies all
24 pairs in distinct columns by integer square roots, all 168
triple/vertex choices by dot products, the same-parity Holder
inequalities, and the two rectangles. Its
[output](holder_mixed_counterexample_check.json) also checks the same
finite pattern at strides \(8,16,64,128,256\).

For those checks the pattern is
\[
 m=S^4/32,\qquad
 (x,a,b)\in
 \left\{
 (0,m+1,4),\
 (S,m+3,2),\
 (S(m-1),m+S^2+3,S^2+2),\
 (Sm,m+S^2+1,S^2+4)
 \right\}.
\]
Only the listed finite instances are used for the nonintegral-distance
and no-right-angle assertions here.

Thus the following three properties, even together, do not suffice:
the same-parity Holder bound, absence of tilted black right angles,
and absence of cross-column integral distances. A constant-stride
Hilbert completion would have to use more of the actual order, or
explicitly control mixed supports. The example does not contradict
the \(S^4\ge1024h\) theorem in
[the mixed-support reduction](continuation_hilbert_mixed_supports.md):
its height is above that theorem's range.
