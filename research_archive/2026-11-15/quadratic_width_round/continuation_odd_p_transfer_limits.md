# Narrow-ratio odd P obstructions and their exact construction scope

15 November 2026. This strengthens the independently reviewed
[localized partition-regularity argument](continuation_odd_p_localized_partition_regularity.md)
and rechecks the earlier one-prime embedding. It does not embed the odd
graph into the Hilbert choice systems. The narrow-ratio, annulus, and
deletion arguments below received an independent written review.

Let \(G_\downarrow\) have the positive odd integers as vertices, with an
edge \(u<v\) when
\[
 u^2+4(v-u)^2=L^2.                                      \tag{1}
\]
The larger symmetric odd graph allows either endpoint in the first
square term. Every lower bound below already holds for \(G_\downarrow\).

## 1. Arbitrarily small relative gaps

**Proposition 1.** For every finite coloring of the positive odd integers
and every \(\epsilon>0\), there is a monochromatic edge of (1) with
\(1<v/u<1+\epsilon\).

Use the notation \(R,T,Q,a,b\) of the localized proof. Fix
\(\delta<\tfrac12\log(1+\epsilon)\). On its unshifted weight support,
\[
 z=n/m\in(0,z_\delta],\qquad
 T(m,n)/R(m,n)\le e^\delta<1+\epsilon,
\]
where \(z_\delta<1\). The function
\[
 \psi(z)=\frac{1+z-z^2}{1-z^2}
\]
is continuous and increasing on this compact range. Since
\(1\le a,b\le Q\), the shifted parameters satisfy
\[
 \frac{Qn+b}{Qm+a}\le z+\frac1m.                          \tag{2}
\]
There is an integer \(M_\epsilon\), independent of \(Q,a,b\), such
that \(m\ge M_\epsilon\) on the weight support implies
\[
 1<\frac{T(Qm+a,Qn+b)}{R(Qm+a,Qn+b)}<1+\epsilon.           \tag{3}
\]
The denominator is positive by the original localized proof.

Insert the indicator of (3) into every localized average. For each fixed
\(\delta\), the removed normalized weight has mean \(o_N(1)\): on
the original support \(n<m\), so only finitely many pairs have
\(m<M_\epsilon\). This is uniform in the CRT choices. All aperiodic
limits, concentration formulas, multiplicative averages, and successive
Fatou steps are unchanged. Extract the positive spectral kernel only
after this indicator has been inserted. The final common odd multiplier
preserves the ratio. This avoids assuming that a shifted pair
automatically inherits the original weight condition.

## 2. Every sufficiently large fixed-shape annulus is highly chromatic

**Proposition 2.** Fix \(c>1\) and an integer \(K\). For all sufficiently
large real \(H\),
\[
 \chi\bigl(G_\downarrow[H,cH]\bigr)>K.                   \tag{4}
\]
The height threshold is not quantitative.

Choose \(1<c'<c\). If every annulus
\([(c')^j,(c')^{j+1})\), \(j\ge0\), were \(K\)-colorable, color each
separately and append the parity of \(j\). Proposition 1 with ratio less
than \(c'\) gives a monochromatic edge. Its endpoints cannot lie in
different annuli of the same parity, since then their ratio exceeds
\(c'\); they cannot lie in the same annulus by properness. Hence one
annulus contains a finite non-\(K\)-colorable set \(U\), with
\(u_{\max}/u_{\min}<c'<c\).

Every odd dilation \(\lambda U\) is another obstruction. It fits in
\([H,cH]\) whenever
\[
 H/u_{\min}\le\lambda\le cH/u_{\max}.                     \tag{5}
\]
This interval has length proportional to \(H\), so contains an odd
integer for every sufficiently large \(H\).

There is also a deletion version. Fix \(0<\alpha<\beta\), and choose
\(U\) with \(u_{\max}/u_{\min}<\beta/\alpha\). There are
\(c_Uh+O(1)\) odd dilations fitting in \([\alpha h,\beta h]\), with
\(c_U>0\). A particular integer belongs to at most \(|U|\) of these
copies, since choosing its preimage determines \(\lambda\). Therefore
\[
 \text{deletions needed to make }
 G_\downarrow[\alpha h,\beta h]\text{ \(K\)-colorable}
 \ \ge c_{K,\alpha,\beta}h                               \tag{6}
\]
for all large \(h\), with a positive nonexplicit constant.

These copies have macroscopic edges. For each edge of the fixed graph
\(U\), put
\[
 X=2(v-u),\qquad Y=u,\qquad A=(L-Y)/2>0.
\]
After an admissible dilation, all three are at least a positive constant
times \(h\). Consequently (6) still holds after discarding every edge
with \(X\le f(h)\) or \(A\le g(h)\), for arbitrary
\(f(h),g(h)=o(h)\). This is an edge-cutoff statement. A vertex removed
because of some other event is counted separately by (6).

## 3. Exact transfer to the older one-prime blocks

Section 1 of the
9 November odd-graph audit
has the correct embedding. Here is its uniform central version.

Fix \(0<\eta<1/2\), an even row
\(R\in[\eta h,(1-\eta)h]\), and put \(\alpha=\eta/10\).
In its one-prime block, the label indexed by odd \(u\) has rows
\(R+u,R\), and column \(4a+\text{constant}\), where
\(a=(R+u-1)/2\). For \(u,v\in[\alpha h,2\alpha h]\), their column
difference is \(2(v-u)\). An edge (1) gives the black diagonal
\[
 (x_u,R+u),\quad(x_v,R)
\]
and an alternate vertical diagonal at their midpoint, with rows
\[
 R+(u-L)/2,\qquad R+(u+L)/2.                             \tag{7}
\]
Since \(L<3\alpha h\), these rows and every endpoint row lie in the
height-\(h\) strip, uniformly in the central \(R\), for all large \(h\).
The midpoint column is integral. The two rows in (7) have opposite
parity because their difference \(L\) is odd.

Assume the full final parity-pair graph occurs somewhere in the board.
Its owner of (7) makes this a genuine obstruction regardless of the
midpoint filling. If both midpoint corners are white, the axis owner
gives the same two-white presentation. If one is black, the owner gives
the same one-white presentation. If both are black, the tilted rectangle
is hidden. In the first two cases the owner cannot be at the midpoint:
the required pair is not fully black there.

**Corollary 3.** For every fixed \(K\), every central one-prime block
requires more than \(K\) P-color layers for all sufficiently large
\(h\). Removing labels so the retained block is \(K\)-layerable costs
\(\Omega_{K,\eta}(h)\) labels per block. There are
\(\Theta_\eta(h)\) central even-row blocks with disjoint label sets,
so the total cost is \(\Omega_{K,\eta}(h^2)\). The same holds for the
macroscopic-edge subgraphs in Section 2.

A layer here retains the prescribed within-block column differences.
Removed labels may be relocated, but the owner hypothesis requires
their parity pairs still to occur in the final board. The result assigns
no width tariff to relocation or layering. It is not a general
\(\omega(h^2)\) width lower bound.

The same argument covers a finite shared offset palette, not just widely
separated layers. Suppose the column of label \(u\) is
\(2u+C+\eta_u\), where \(\eta_u\) belongs to a shared set of at
most \(K\) offsets. Coloring by \(\eta_u\) preserves the original
column difference on each monochromatic pair, so Corollary 3 applies
unchanged. In particular, permutations within consecutive blocks of
any fixed size \(b\) cannot repair the row-linear one-prime placement:
the displacement from column \(4a+C\) is
\(4(p(a)-a)\), one of at most \(2b-1\) values. This conclusion
allows an arbitrary permutation in each block; it does not require
the same permutation in different blocks. The shared-palette or bounded
displacement hypothesis is essential, and this is still not a statement
about Hilbert order.

## 4. Why this does not yet transfer to the Hilbert choice systems

For [p_dec_all_scales.md](../p_dec_all_scales.md), a candidate constraint
between ranks \(r_v<r_w\) has
\[
 q=M(r_w-r_v)+\delta,\quad |\delta|\le M-1,\qquad
 (32q)^2+|2(y_e-x_o)+1|^2=\square.                        \tag{8}
\]
The unknowns are private slot choices, not colors of the odd numbers
in (1). DEC reduces the problem exactly to four systems per scale,
but supplies no embedding of arbitrary finite odd graphs into a piece.

Even the zero-shift subsystem would require a new geometric statement:
one assignment of graph vertices to Hilbert labels must realize all
horizontal rank differences and cross-row differences simultaneously.
The one-prime construction has a constant even row and a linear
odd-row/column relation; the Hilbert systems have neither. Separate
occurrences of the individual Pythagorean triples do not provide a
graph embedding. Candidate unsolvability would additionally need owner
and strip checks before it obstructed the genuine system.

The refinement formulas in
[p_two_block_selfsimilar.md](../p_two_block_selfsimilar.md),
\(U'\in2U+\{-1,0,1\}\) and \(d'\in4d+[-3,3]\), do not preserve
the arithmetic test (8). Thus the odd theorem supplies no unsatisfiable
scale, no lower bound on the number of private choices, and no failure
of bounded local permutations. It does not bypass the near-linear
actual-gap cleanup.

One sufficient transfer hypothesis is precise: every finite
non-\(M\)-colorable odd graph occurs on label representatives in some
candidate system, with every graph edge forbidding \(\delta=0\).
An integer \(M\)-choice solution would then properly color that graph
by its choices. This hypothesis is not established here. A genuine
obstruction would require the same embedding in the strip with owners.

## 5. A fixed-diagonal Cayley graph is also different

For the constant-offset construction, write \(T=2s+1\). Its positive
forbidden distances come from signed solutions of
\[
 20d^2+4Td+T^2=L^2,                                     \tag{9}
\]
with the actual diagonal-length and strip cutoffs where appropriate.
The substitution \(u=T+2d,\ v=T\) turns (9) into
\(u^2+4(v-u)^2=L^2\). This extracts neighbors of the single vertex
\(T\) in the symmetric odd graph, allowing signed odd vertices if
necessary. It does not embed that graph into
\(\operatorname{Cay}(\mathbb Z,D_T)\): the Cayley graph repeats one
difference set at every translate, whereas the odd-graph relation
depends on the absolute endpoints.

No bound or lower bound for
\(\chi(\operatorname{Cay}(\mathbb Z,D_T))\), uniformly in \(T\),
therefore follows from the new partition-regularity theorem alone.
Earlier arc and odd-relation deletion obstructions concern particular
sufficient criteria and remain separate.

The constructive target left by this audit is exact: solve or obstruct
the four Hilbert slot systems using their rank arithmetic, or establish
a new graph embedding. Bounded coloring of the full odd graph can no
longer supply the older one-prime layering step.

