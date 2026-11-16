# Repeated even rows create a two-core four-sea collision

15 November 2026. In any of the four low profiles, two even points at the
same bulk row can give distinct one-label/two-sea triangles with the same
white completion. Every eligible bulk even row has such a pair of column
positions. A fixed finite profile menu cannot eliminate all prescribed
bounded same-row gaps.

This is a limitation on repeated-row placements and fixed local repairs.
It is not a lower bound for arbitrary blackout constructions.

## 1. Exact divisor parametrization

Fix the profile's odd row \(L\) and even row \(F\), and an even row
\[
 b>2F,\qquad b\equiv F+2\pmod4.
\]
Put
\[
 C=(F-L)(b-F)=2n,
\]
where \(n\) is positive and odd. For any signed odd divisor \(u\mid C\),
write \(v=C/u\), and choose a completion column \(w\equiv u\pmod4\).
The three black points
\[
 E_u=(w-u,b),\quad
 F_u=(w-u-v,F),\quad
 L_u=(w-v,L)                                               \tag{1}
\]
have the required column types: respectively 0, 2, and odd modulo four.
At \(F_u\), their horizontal legs are \(v,u\), and their vertical
legs are \(b-F,L-F\). Their dot product vanishes because \(uv=C\).
The common fourth corner is
\[
 W=(w,b+L-F).                                             \tag{2}
\]
It is a white point in the strip whenever \(b\le h\): its row lies
strictly between \(F\) and \(b\), and its column is odd.

Two distinct odd divisors \(u,u'\) in the same class modulo four give
a collision whenever both corresponding even points are present. Their
column difference is \(u-u'\). All six black points in (1) are distinct.
For the only nontrivial same-row coincidence, equality of the two F points
would imply \(uu'=C\), impossible because the left side is odd.

For an all-row witness, choose \(\varepsilon\in\{1,-1\}\) with
\(\varepsilon n\equiv1\pmod4\), and use
\[
 u=1,\quad v=2n;\qquad
 u'=\varepsilon n,\quad v'=2\varepsilon.
\]
The bulk assumption gives \(n>1\). At \(w=1\), the two even columns
are 0 and \(1-\varepsilon n\), and the whole support has horizontal
span \(O_{L,F}(b)\). Thus a sufficiently long constant-even-row plateau
is invalid. Finite core boundaries can exclude a particular witness and
must be checked in any application.

## 2. Degree is small, despite the obstruction

For fixed \(b\), let \(D_b\) be the signed odd divisors of \(C\).
The forbidden column differences are among
\[
 \{u-u':u,u'\in D_b,\ u\ne u',\ u\equiv u'\pmod4\}.
\]
Consequently each fixed even point has at most
\(4\tau(C)^2=h^{o(1)}\) partners in this family, uniformly over any
actual occupied column set. No randomness or Hilbert hypothesis is needed.

If \(K\) even-only stubs are prescribed, at most \(K h^{o(1)}\)
genuine doubles can be their neighbors in this family. Erasing the even
point of each such genuine double, retaining its odd point, and relocating
the full pair removes every stub-to-double edge at that internal cost.
This erasure creates no new edge in the present family, which uses only
even points. It does not repair an edge between two even-only stubs, and
does not by itself control the P or other supports of the new odd stubs.

## 3. No fixed finite menu removes all bounded repeated-row gaps

Consider any fixed finite menu of profiles \((L_i,F_i)\) compatible
with one even residue class \(b_0\pmod4\). Thus every
\(F_i\equiv b_0+2\pmod4\). For each profile, prescribe any finite
set of positive column gaps \(\mathcal D_i\subset4\mathbb Z\).
There is a positive-density arithmetic progression of bulk rows
\(b\equiv b_0\pmod4\) for which every gap in every
\(\mathcal D_i\) is forbidden by the family above.

For each pair \((i,d)\), choose a positive integer
\(u_{i,d}\equiv1\pmod4\) so that
\[
 m_{i,d}=u_{i,d}(u_{i,d}+d)
\]
are pairwise coprime. This can be done successively. For every odd prime
already used, avoid the at most two residues 0 and \(-d\). At least one
residue remains, including at the prime three. Combine those conditions
with \(u_{i,d}\equiv1\pmod4\) by the Chinese remainder theorem.

The Chinese remainder theorem then gives a progression satisfying
\[
 b\equiv F_i\pmod{m_{i,d}}\quad\text{for every }(i,d),
 \qquad b\equiv b_0\pmod4.                               \tag{3}
\]
For sufficiently large members, every bulk inequality holds. Both odd
integers \(u_{i,d}\) and \(u_{i,d}+d\) divide
\((F_i-L_i)(b-F_i)\), and they are congruent modulo four. Equation (1)
therefore realizes a collision at the prescribed gap \(d\).

All selected divisors and moduli are fixed. Their witness sea columns are
within \(O(b)\) of the two even points. Thus the assertion applies to
same-row pairs sufficiently far from the core's ends. The horizontal
margin is part of the conclusion's hypothesis.

For example, let \(\mathcal D_i\) contain all possible separations of
two slots in a fixed-width permutation block. For rows in (3), any block
containing two copies of that even row has a forbidden pair in every
permutation, provided the witnesses fit. Neither a fixed finite menu nor
fixed-width local permutations alone repair these repeated-row objects.
An adaptive global order, different singleton rows, or an unbounded menu
is outside this obstruction.

## Review status

The full written proof was independently reviewed on 15 November 2026.
The review checked the six distinct black cells, divisor-degree bound,
finite-set finite-menu Chinese remainder construction, and the necessary
horizontal margin. No correction was needed.
