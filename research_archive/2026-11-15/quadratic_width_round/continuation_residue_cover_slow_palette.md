# Slow row palettes and a finite residue-cover criterion

15 November 2026. A finite direction palette has an elementary
sufficient condition for safe growing row choices under the actual
slow-plateau geometry. The condition is automatic for pairwise coprime
odd vertical legs. When the finite residue system covers everything,
there is a fully occupied slow-background obstruction. This converse
is not a sampled-Hilbert embedding.

## 1. The finite residue parameter

Let \(\mathcal D=\{(u_i,v_i):1\le i\le d\}\) be distinct primitive
Pythagorean direction magnitudes, with \(u_i>0\) even and \(v_i>0\)
odd. Then \(u_i\) is divisible by four and \(v_i\ge3\). Both horizontal
and vertical signs are allowed.

Put \(L=\operatorname{lcm}(v_1,\ldots,v_d)\). For each direction
choose two residues \(e_i^-,e_i^+\) modulo \(v_i\), allowing equality.
Define
\[
 \gamma(\mathcal D)=
 \min_{\{e_i^\pm\}}
 {1\over L}\left|
 \left\{j\bmod L:
       j\not\equiv e_i^-,e_i^+\pmod{v_i}\quad\hbox{for all }i
 \right\}\right|.                                      \tag{1}
\]
This is a finite arithmetic test, independent of any placement graph.
If the \(v_i\)'s are pairwise coprime, the Chinese remainder theorem gives
\[
                      \gamma(\mathcal D)
                            =\prod_i(1-2/v_i)>0.       \tag{2}
\]
Repeated or noncoprime vertical legs need the actual test (1).

## 2. Availability when the residue parameter is positive

Assume the selected opposite-parity source function and its auxiliary
plateau extension satisfy the two hypotheses of
[the two-direction theorem](continuation_two_direction_slow_palette.md):
\[
 |\Delta z|^2\le q/16+1,\qquad
          \text{extension jump spacing at least }G\ge256.
                                                               \tag{3}
\]
The extension may fill parity holes only for counting.

For a fixed direction and horizontal sign, use signed scale
\(t=t_0+4n\). The target index is
\[
                    j(n)=z(\sigma u_i|t|/4)+v_i n+c.
\]
For two selected scales at difference \(m\ge1\), this increases
strictly. Indeed,
\[
 |\Delta z|\le\sqrt{u_i m/16+1}<v_i m.
\]
The last inequality holds for every primitive direction in the list:
\[
      u_i\le(v_i^2-1)/2
\]
follows from
\((\sqrt{u_i^2+v_i^2}-u_i)
 (\sqrt{u_i^2+v_i^2}+u_i)=v_i^2\), whose first factor is a positive
integer.

The signed-scale and plateau count from the cited proof therefore
applies unchanged. In a \(K\)-row target window, the sum of the
numbers of residue phases over both horizontal signs and every
direction is at most
\[
 {4K\over G}\sum_i{u_i\over v_i}
          +6d+{1\over8G}\sum_i{u_i^2\over v_i^2}.       \tag{4}
\]
On each common phase interval, at least a fraction \(\gamma\) of
every complete period \(L\) is safe. The incomplete period costs
at most \(L\) choices. Consequently
\[
 \#\{\text{norm-safe choices}\}\ge
 \left(\gamma-{4L\over G}\sum_i{u_i\over v_i}\right)K-C,
 \quad
 C=L\left(1+6d+{1\over8G}\sum_i{u_i^2\over v_i^2}\right).
                                                               \tag{5}
\]
If \(\gamma>0\), choose a sufficiently large fixed mesh,
\[
          G\ge\max\left\{256,\,
                {8L\over\gamma}\sum_i{u_i\over v_i}\right\}.       \tag{6}
\]
Then (5) is at least \(\gamma K/2-C\).

The fine multi-anchor construction permits this fixed slowdown:
increase its integer parameter \(D\), then use
\(G_0=256D\), \(M=4096D^2\). Its bound (3) is unchanged, and the
width multiplier remains constant in \(h\). The auxiliary cap
extension has the required jump spacing by the audited proof in the
two-direction note.

If a literal forbidden row set has \(b\) indices, at most
\(4b/\gamma\) window starts have more than \(\gamma K/4\) forbidden
choices. Outside these starts, (5)--(6) leave at least
\(\gamma K/4-C\) actual-good safe choices. Profile boundary windows
cost an additional \(O(K)\) starts. An already selected opposite-parity
guard of radius \(6(K^2+1)\) permits the same one-column retuning
as before.

All directions in the finite list are handled simultaneously.
Directions outside it, guard creation, and the other support families
remain separate.

## 3. A slow occupied obstruction when the residue system covers

Suppose \(\gamma(\mathcal D)=0\), and choose residues \(e_i^\pm\)
that cover every integer. Take their representatives in
\(\{0,\ldots,v_i-1\}\), and let \(R=\max_{i,\sigma}e_i^\sigma\).
Fix any desired constant jump spacing \(G\), and any \(K=o(h)\).

Choose
\[
 Y_0\in[\eta h,\eta h+4L],\quad L\mid Y_0,\quad
 Y_0\equiv3\pmod4,\qquad
 A\in[.65h,.66h],\quad A\equiv3\pmod4,                 \tag{7}
\]
where \(\eta>0\) is sufficiently small depending only on the finite
direction list. Such \(Y_0\) exists because \(L\) is odd.
The target palette at column zero is
\[
                         b_j=A+Y_0+4j,\quad0\le j<K.
\]
For every membership \(j\equiv e_i^\sigma\pmod{v_i}\), put
\[
 g={Y_0+4(j-e_i^\sigma)\over v_i},\quad
 x=\sigma u_i g,\quad a=A+4e_i^\sigma.                \tag{8}
\]
For large \(h\), \(g>0\). This source creates the norm
\[
                  (|x|,b_j-a,\ell_i g)
                      =(u_i g,v_i g,\ell_i g),
 \qquad \ell_i=\sqrt{u_i^2+v_i^2}.                    \tag{9}
\]

Each signed direction has a constant source row on a band centered
at \(\sigma u_iY_0/v_i\), of width \(O(K)\). Distinct primitive
direction magnitudes have distinct positive slopes \(u_i/v_i\).
Their signed band centers are separated by \(\Theta(h)\).
Thus no incompatible source prescriptions share a column.

Fill the rest of each band at its prescribed odd row. Join the
bands by unit row-index changes separated by
\[
                         H\ge\max\{G,16(R+1)\}.       \tag{10}
\]
There is room because \(H,R\) are fixed and band separations have
order \(h\). All arithmetic columns except zero are now occupied
at one of the odd rows \(A,A+4,\ldots,A+4R\).
Nonarithmetic columns carry sea row one. Column zero receives one
target row.

The resulting total odd index function meets (3). A pair with index
difference \(m\ge2\) crosses at least \(m\) unit seams, so its rank
distance \(q\) is at least \(H(m-1)\). Since \(m\le R\),
\[
 m^2-1=(m-1)(m+1)\le H(m-1)/16\le q/16.
\]
Differences zero and one satisfy (3) directly. Its jump spacing is
at least \(G\), and the only adjacent seams are isolated unit seams.

Every target is blocked because the residues cover every \(j\).
Each specified horizontal leg and smaller half-factor has order \(h\).

### Actual white cells and owner residues

For a primitive even-horizontal, odd-vertical Pythagorean vector,
\[
                       a_i^*=(\ell_i-v_i)/2
\]
is a square. If \(v_i\equiv1\pmod4\), that square is divisible by
four. If \(v_i\equiv3\pmod4\), it is odd and congruent to one.
This follows immediately from the usual primitive parametrization
\(u_i=2mn\), \(v_i=m^2-n^2\), \(m>n\) of opposite parity.

The smaller half-factor in (9) is \(t=a_i^*g\).
Equation (7) gives \(g\equiv3v_i^{-1}\pmod4\).
Thus \(t\equiv0\pmod4\) in the first case and
\(t\equiv1\pmod4\) in the second. The common vertical pair lies
at column \(x/2\), in rows
\[
                              a-t,\qquad b_j+t.       \tag{11}
\]
Its odd row is \(3\pmod4\), and its even row is \(2\pmod4\).

Choose \(\eta\) small enough that these rows remain in the strip
and their odd member remains above \(h/2\), uniformly over the fixed
list. Both rows differ by \(\Theta(h)\) from the bounded collection
of odd background levels. At a midpoint arithmetic column the
background has one of those levels; at a midpoint nonarithmetic
column it has sea row one. Both cells in (11) are therefore white.
A retained full-family axis owner for this row pair makes the rival
a genuine presentation collision, exactly as in the earlier palette
obstructions.

All background rows can avoid an arbitrary literal bad set of size
\(o(h)\): excluding \(A\)'s for which one of \(A+4r\),
\(0\le r\le R\), is bad removes only \(o(h)\) possibilities.
The same averaging argument as before leaves \((1-o(1))K\)
actual-good target choices. Every such choice remains blocked.

This is a fully occupied geometric obstruction with arbitrarily slow
fixed transitions. It is not a raw Hilbert or sampled-cap realization.
The complete row-pair owner hypothesis remains explicit.

## 4. The first concrete zero-cover example

Take the four direction magnitudes
\[
                  (4,3),\quad(12,5),\quad(8,15),\quad(112,15).
\]
Use residues zero and one for the first two directions. Their uncovered
residues modulo fifteen are \(2,8,14\). The third direction covers
two and eight; one sign of the fourth covers fourteen.
Hence \(\gamma=0\).

The corresponding source rows are among
\(A,A+4,A+8,A+32,A+56\), and their smaller half-factors are
\(g,4g,g,49g\). This example explains why the positive two-direction
theorem cannot be promoted to arbitrary finite direction palettes
merely by making the interpolation slower.

Independent written review: the complete note passed a separate
check of the finite-mesh availability coefficient, signed-scale
monotonicity, separated source bands, slow-join square bound,
primitive half-factor parity, actual owner scope, literal-good
averaging, and the four-direction covering example. The distinction
between a slow geometric background and a sampled-core realization
was checked explicitly.

