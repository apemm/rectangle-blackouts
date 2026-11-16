# Direct forced P edges are local to a doubly bad cell

15 November 2026. The total virtual palettes give two useful necessary
conditions for a direct intrinsically forced odd-to-even P edge. Neither
condition proves that all forced paths can be excluded.

Use the padded standard Hilbert square and virtual cap functions from
[`continuation_virtual_cap_palettes.md`](continuation_virtual_cap_palettes.md).
Suppose rank \(r\) has only a good odd option, and rank \(s\) has only
a good even option. Put \(q=|r-s|>0\).

## 1. The crossing of the two bad coordinate lines is nearby in rank

The bad virtual even value at \(r\) was not changed by an even cap,
since every cap replacement is good. It is therefore an original bad
clipped value. Clamping only produces good boundary values, so the raw
even coordinate is exactly \(U_1+j_{\rm bad}\).
Likewise, the raw odd coordinate at \(s\) is
\(U_0+i_{\rm bad}\). Their coordinate lines meet at
\[
 z=(U_0+i_{\rm bad},U_1+j_{\rm bad}).
\]
This is a doubly bad raw cell. Let its Hilbert rank be \(t\).

Choose the least power of four \(B\ge q\). The ranks \(r,s\) lie
in at most two consecutive Hilbert blocks of area \(B\). Each block
is an axis-aligned square, and consecutive blocks are edge-adjacent.
Their union is consequently a rectangle. Since it contains both endpoint
cells, it also contains their coordinate crossing \(z\). Thus
\[
 |t-r|,|t-s|<2B<8q.                                      \tag{1}
\]
For \(q=1\), the last inequality holds directly with \(B=1\).
The argument is unaffected by which selected cap covers \(z\), or by
whether either good endpoint value was changed by its own-parity cap.

For an actual in-strip P event at stride \(S\),
\(q\le(h-1)/S\). Equation (1) therefore places both forced endpoints
within \(8h/S\) ranks of one doubly bad cell. The number of such cells
is at most the product of the two bad-row counts. The resulting crude
union bound is too large for the present quadratic budget.

## 2. The bad physical row gap is near the Pythagorean height

Write the two total physical virtual functions as \(A,B\), with odd
and even parity, and suppose each satisfies
\[
 |A(r)-A(s)|,|B(r)-B(s)|\le C\sqrt q.
\]
The unavailable values \(A(s)\) and \(B(r)\) are the two original
bad physical rows. The prospective P endpoints have rows \(A(r)\) and
\(B(s)\). Hence
\[
 \left||B(s)-A(r)|-|B(r)-A(s)|\right|\le2C\sqrt q.         \tag{2}
\]
If the edge is a P event, its magnitude \(Y=|B(s)-A(r)|\) satisfies
\((Sq)^2+Y^2=L^2\), with \(L\le h-1\). Thus a necessary
arithmetic condition is
\[
 \bigl|\,|b_{\rm bad}-a_{\rm bad}|-Y\,\bigr|
       \le2C\sqrt q                                     \tag{3}
\]
for some in-strip norm solution at horizontal leg \(Sq\).

This reduces exclusion of direct intrinsic forced edges to a condition
on differences between the two actual bad-row sets. Cardinality alone
does not imply that condition, as the exact example in
[`continuation_forced_cap_p_edge.md`](continuation_forced_cap_p_edge.md)
shows. Equation (3) also does not exclude a longer directed path through
singleton objects with two good options, or forces introduced by retained
genuine doubles.

Independent review checked the raw-coordinate argument, the two-block
rectangle and rank bound, and the total virtual-function comparison.
The rank statement concerns the original order before object permutations.
