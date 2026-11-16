# What finite strides and local permutations can do for R2s

15 November 2026. A constant row-one sea admits R2s supports at every
fixed stride, within every fixed compatible row-residue class. An
explicit family also obstructs a local permutation theorem with
arbitrary fixed outside labels. Neither statement forces the support
to occur in a prescribed Hilbert order. The final section gives an
exact forbidden-row formulation and a sufficient matching condition
for the external constraints of one permutation block.

## 1. An R2s family at every fixed stride

Fix positive integers \(a,w\), and define
\[
\begin{split}
 U&=(2aw+1)^2+4a^2,& n&=wU,\\
 \delta&=4a,& T&=4aw,\\
 V&=1-4a^2(w^2+1),&
 X&=4a\{a(w^2+1)+w\}.
\end{split}                                                    \tag{1}
\]
The exact identities are
\[
 TU=n\delta,\qquad
 V^2=U^2-2n\delta-\delta^2,\qquad
 2X=U+T-V,\qquad X+V=4aw+1.                         \tag{2}
\]
Thus the four black points
\[
 A=(0,n+1),\quad B=(U,1),\quad
 C=(X,n+1+\delta),\quad D=(X+V,1)                   \tag{3}
\]
give the crossed same-sea mixed support from
[the spacing-four R2s formula](continuation_step_four_r2s_transfer.md).
Indeed, \(AB\) is the black side of one rectangle and \(CD\) is the
black diagonal of another. Their common corners are
\[
 P=(T/2,n+1+\delta/2),\qquad
 Q=(U+T/2,1+\delta/2).                              \tag{4}
\]
The translation \((T,\delta)/2\) is perpendicular to \(B-A=(U,-n)\),
by \(UT=n\delta\); the two squared diagonal/side lengths agree by
(2). All points are integral. The translation is nonzero, and the
second rectangle is nondegenerate because its diagonal has nonzero
horizontal and vertical components and its common corners are
distinct from (3).

Both sea columns \(U\) and \(X+V\) are \(1\bmod4\), while \(X\) is
divisible by four. The common rows in (4) lie between one and
\(n+1+\delta\). All six points are distinct. Adding other black
points cannot repair the equality of the two rectangle
presentations: their symmetric difference already consists of
the four black points (3).

The same-parity core-point bound holds:
\[
 \delta^2=16a^2\le 2X
 =8a^2(w^2+1)+8aw.                                \tag{5}
\]
For fixed \(a\) and \(w\longrightarrow\infty\),
\[
 n\asymp_a w^3,\qquad X\asymp_a w^2,\qquad
 \delta=4a.
\]
Consequently, the support fits a strip of height
\(h=n+1+\delta\), has horizontal span \(O_a(h^{2/3})\), and satisfies
any stronger fixed inequality \(\delta^2\le\varepsilon X\) once
\(w\) is large.

Now fix finitely many strides \(S_j\in4\mathbb Z_{>0}\) and a row
modulus \(R\). Choose \(a\) divisible by \(R\) and every \(S_j/4\).
Then every \(S_j\) divides \(X\), and
\[
 U\equiv1\pmod R,\qquad
 n+1\equiv w+1\pmod R,\qquad \delta\equiv0\pmod R.
\]
Choosing \(w\) in a compatible residue class puts both core rows in
any prescribed class, including a required odd or even profile.

This rules out a universal arithmetic exclusion based only on a
finite constant stride menu and a finite row-residue subdivision.
It does not rule out choosing positions that avoid these specific
horizontal distances, or using sea patterns other than the stated
constant row-one sea.

## 2. An arbitrary-boundary obstruction for a whole permutation block

Fix \(k\ge2\), put \(N=k^2\), and give a central block the slots
\(x_j=Sj\), \(0\le j<N\), for a sufficiently large fixed
\(S\in4\mathbb Z\). The labels in that block are the complete
Cartesian product of \(k\) odd rows and \(k\) even rows.

Use (1) with \(a>k\), \(S/4\mid a\), and \(w\equiv2\pmod4\).
Then \(y=n+1\equiv3\pmod4\). Take the central odd rows
\[
 y,y+4,\ldots,y+4(k-1).
\]
Choose any \(k\) even rows in a fixed-width interval near \(y\).
At every outside slot
\[
                         x_j+X
\]
fix a double containing odd row \(y+\delta\). Give those \(N\)
outside labels distinct even rows in a fixed-width interval near
\(y\). The outside labels are all distinct and none equals a central
label, because \(a>k\).

Every central permutation places at least one label containing row
\(y\) at some \(x_j\). Its odd point and the fixed odd point at
\(x_j+X\) then give exactly the translated support (3). The two sea
points are at nonarithmetic columns and therefore remain present.
No outside label is moved.

For completeness, these finite label sets can obey the same-parity
norm-gap geometry for every central permutation. Their row
differences are bounded in terms of \(a,k\). First choose \(S\)
large enough for all within-block comparisons, then choose \(a\)
as its required multiple and larger than \(k\). The odd row
difference across the two blocks is at most \(4a+4k\), whereas
\(X\longrightarrow\infty\) with \(w\). The even row differences
remain \(O(k^2)\). For large \(w\), all cross-block inequalities also
hold, and the blocks are disjoint. Increasing the strip height by
a fixed \(O(a+k^2)\) amount contains every selected row and every
common corner.

Thus no universal theorem can repair R2s by permuting one bounded
Cartesian block against arbitrary fixed outside doubles, even when
there is only one obstructed odd row and the imposed geometry holds.
This is not an actual Hilbert-block embedding. It also does not
obstruct simultaneous rearrangement of the outside block.

## 3. Exact external forbidden-row sets

There is nevertheless an exact finite test for the external R2s
constraints of a proposed block. Suppose a candidate row \(y\) at
slot \(x\) and a fixed outside row \(z>y\) at slot \(x'\) have the
same profile residue. Put
\[
                  n=y-1,\quad \delta=z-y,\quad X=x'-x.
\]
The pair supports a crossed R2s collision precisely when a signed divisor
\(U\mid n\delta\) passes
\[
 T=n\delta/U\in2\mathbb Z,\qquad
 V=U+T-2X,\qquad
 V^2=U^2-2n\delta-\delta^2,                         \tag{6}
\]
together with the actual sea-column, strip and nondegeneracy tests.
For the constant sea these include \(U,X+V\notin4\mathbb Z\).
When \(z<y\), apply the test with the lower row as the side owner
and reverse \(X\). Equal rows give no nondegenerate support.

For each central slot \(s\), let \(F_0(s)\) and \(F_1(s)\) be the
odd and even row choices that fail at least one such test against
a fixed outside point. An assignment of the label \((i,j)\) to
slot \(s\) is externally R2s-safe exactly when
\[
                    i\notin F_0(s),\qquad j\notin F_1(s).
\]
No other coordinate of the outside double appears in this test.

Here is a simple sufficient condition for a full permutation:
\[
\begin{array}{ll}
 |F_0(s)|\le a_0,\quad |F_1(s)|\le a_1
      &\text{for every slot }s,\\
 \#\{s:i\in F_\alpha(s)\}\le k a_\alpha
      &\text{for every row }i\text{ of role }\alpha,\\
 a_0+a_1\le k/2.&
\end{array}                                                    \tag{7}
\]
In the slot-label bipartite graph, every slot has at least
\((k-a_0)(k-a_1)\ge k^2/2\) neighbors. Every label loses at most
\(k(a_0+a_1)\le k^2/2\) slots, so its degree is also at least
\(k^2/2\). A balanced bipartite graph on \(N+N\) vertices with both
minimum degrees at least \(N/2\) has a perfect matching: sets of
size at most \(N/2\) have enough neighbors immediately; if a larger
set had too few neighbors, a vertex outside its neighborhood would
have fewer than \(N/2\) possible neighbors. This proves (7).

The sharper role-sensitive conditions in
[the matching lemma](continuation_role_sensitive_hall_extension.md)
can be used when its row-resource hypotheses are available. Neither
criterion controls internal pairs of newly assigned labels, P, or
the other rectangle families.

The obstruction in Section 2 explains why both lines of (7) matter.
Every slot can forbid only one odd row, but that same row can be
forbidden at all \(k^2\) slots. A small number of forbidden rows per
slot does not imply a feasible permutation.

## 4. Research consequence

The remaining full-occupancy question is genuinely about placement
or simultaneous exchange. A finite residue filter cannot dispose of
all R2s rows, and arbitrary fixed boundary labels can defeat a local
permutation. A useful positive theorem would need to prove row-resource
bounds such as (7) for the actual sampled order, or allow a coordinated
move that changes both ends of an obstructing support.

Independent written review: all sections passed a separate derivation,
including the arithmetic family, the order of the fixed constants in
the block construction, the divisor reconstruction, and both matching
degree bounds. A separate exact integer check verified 30 instances of
(1), including perpendicularity, equal diagonal midpoints and lengths,
six distinct points, and (5).

