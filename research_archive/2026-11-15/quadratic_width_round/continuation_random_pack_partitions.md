# Random pack partitions preserve occupancy and produce spacing fluctuations

15 November 2026. Independent binary words give two row-pack classes with
bounded gaps, fluctuating cumulative counts, and an exact inverse-spacing
anticoncentration bound. Applying this partition to the common-good physical
pack list preserves the fully occupied triangular scaffold.

The construction adds a proved source of randomness. It does not yet bound
the joint P constraint graph or avoid the remaining mixed supports.

## 1. An elementary bounded-gap random partition

Independently choose each length-three word to be
\[
 001\quad\text{or}\quad011
\]
with equal probability, and concatenate the words. The symbols partition
the nonnegative integer pack positions into two classes. Both symbols occur
in every word. Consecutive occurrences of either symbol have distance at
most three.

Let \(B_j\) be the indicator that word \(j\) is \(001\). Among the first
\(m\) complete words, the class counts are
\[
 C_0(3m)=m+\sum_{j=1}^m B_j,\qquad
 C_1(3m)=2m-\sum_{j=1}^m B_j.                               \tag{1}
\]
Each has mean \(3m/2\) and variance \(m/4\). Thus this partition has
unbounded count fluctuations as its length increases. It is not a permutation
of colors inside blocks with fixed color counts.

For every \(u>0\), a union bound over complete-word prefixes gives
\[
 \Pr\!\left(\max_{0\le t\le3m}|C_0(t)-t/2|>u+1\right)
 \le2m\exp(-2u^2/m).                                       \tag{2}
\]
The same bound controls both classes because \(C_1(t)=t-C_0(t)\).
To obtain (2), use
\(\mathbb E e^{z(B_j-1/2)}=\cosh(z/2)\le e^{z^2/8}\), apply
the exponential Markov inequality to each prefix, and optimize \(z\).
An incomplete word contributes at most one to the discrepancy.

Take \(u=\sqrt m\log(2m)\) and write \(E=u+1\). Except on an event of
probability at most \(2m e^{-2\log^2(2m)}\),
\[
 |C_\alpha(t)-t/2|\le E
 \quad(0\le t\le3m,\quad\alpha\in\{0,1\}).                 \tag{3}
\]

Let \(p_i^\alpha\) be the position of occurrence \(i\) of color \(\alpha\),
with zero-based indices. Since \(C_\alpha(p_i^\alpha)=i\), (3) gives
\[
 |p_i^\alpha-2i|\le2E.                                     \tag{4}
\]
The deterministic bounds, independent of (3), are
\[
 j-i\le p_j^\alpha-p_i^\alpha\le3(j-i)\quad(i<j).           \tag{5}
\]
For different classes, (4) gives the useful lower bound
\[
 p_j^\beta-p_i^\alpha\ge2(j-i)-4E.                         \tag{6}
\]

## 2. Exact local count and inverse-spacing bounds

The maximum point mass of a sum of \(m\) fair independent Bernoulli
variables is at most \(C/\sqrt{m+1}\), for an absolute \(C\).
For completeness, the central mass at even size \(2n\) is
\[
 4^{-n}\binom{2n}{n}
 =\prod_{j=1}^n\left(1-\frac1{2j}\right)
 \le\exp\left(-\frac12\sum_{j=1}^n\frac1j\right)
 \le(n+1)^{-1/2}.
\]
The neighboring odd-size central mass is no larger. Hence the count of
either color in any fixed interval of \(m\) complete words has maximum
point mass \(O((m+1)^{-1/2})\), even after conditioning on all word choices
outside that interval.

There is also an inverse statement. Extend the construction to an infinite
word sequence. Fix a color, an occurrence index \(i\), and \(t\ge1\).
Reveal all word choices through the word containing \(p_i\). Conditional
on this revealed history,
\[
 \sup_z\Pr(p_{i+t}-p_i=z\mid\text{revealed history})
 \le\frac{C}{\sqrt t}.                                     \tag{7}
\]

Indeed, (5) restricts a possible distance to \(t\le z\le3t\). For a
fixed such \(z\), the event fixes the number of occurrences in
\((p_i,p_i+z]\). After the revealed initial partial word and at most one
final partial word are removed, this count is a deterministic integer plus
a binomial sum over at least \(z/3-O(1)\) fresh complete words. Split into
the at most two choices of the final partial word. The preceding maximum
point-mass bound proves (7) for \(t\) above a fixed constant, and enlargement
of \(C\) covers the remaining values. Fresh word choices are independent
after this stopping word: conditioning on any possible stopping-word index
and its revealed prefix gives the same product distribution for the suffix.

If \(w_0<w_1<\cdots\) is any deterministic strictly increasing physical
pack list, then conditional on the same history, each specified value of
\(w_{p_{i+t}}-w_{p_i}\) determines at most one value of \(p_{i+t}\).
Consequently
\[
 \sup_z\Pr(w_{p_{i+t}}-w_{p_i}=z\mid\text{revealed history})
 \le\frac{C}{\sqrt t}.                                     \tag{8}
\]
These bounds concern one spacing or one count. They do not assert
independence of several overlapping P tests.

## 3. Apply the partition to physical four-packs

Start with the deterministic common-good physical packs in
[`continuation_packed_triangles_and_hall.md`](continuation_packed_triangles_and_hall.md).
Their origins satisfy
\[
 4(j-i)\le w_j-w_i\le4G(j-i),\qquad
 n_0=h/(4D)-O(\sqrt h)-O(1),                                \tag{9}
\]
where \(D=28\) and \(G\) is an absolute constant. Pack \(w_j\) consists
of the four original physical indices \(w_j,w_j+1,w_j+2,w_j+3\).
All eight corresponding odd/even rows passed the profile filters.

Partition the first \(3m\) packs, where \(m=\lfloor n_0/3\rfloor\),
by the random words. Discard at most two remaining packs. Use the deterministic
common prefix length
\[
 n=\left\lfloor3m/2-E-2\right\rfloor.                       \tag{9a}
\]
For sufficiently large \(h\), this is positive. On event (3), both color
lists contain at least \(n\) packs. Retain their first \(n\) members.
This discards only \(O(E)=O(\sqrt h\log h)\) further packs.
The corresponding discarded labels number \(O(h^{3/2}\log h)\).
The deterministic length is important for probabilistic applications:
triangle ranks and slot differences then do not depend on the random words.

Each color list retains whole physical packs. Within either color, (5) and
(9) give
\[
 4(j-i)\le w_{p_j^\alpha}-w_{p_i^\alpha}
 \le12G(j-i).                                              \tag{10}
\]
The microtiles are therefore still genuine \(4\times4\) arithmetic squares.
All square-filter, residue, and one-label properties are unchanged.
The packed locality proof applies with \(G\) replaced by \(3G\), so a
larger fixed stride handles every permutation of the sixteen labels in
each tile. The cone-type and role-sensitive Hall statements retain their
original hypotheses on each physical tile.

## 4. Cross-color triangles and the enlarged short-P band

For each ordered color pair \((\alpha,\beta)\), order the macrotiles in
the two index triangles \(j-i\ge c\) and \(i-j\ge c\), as before.
Every tile receives sixteen consecutive slots. No padded labels or missing
slots occur.

If two slots have distance at most \(Q\), their macro-rank distance is
at most \(T_Q=\lceil Q/16\rceil\). The triangular locality gives
\(j-i'\ge c-7\sqrt{T_Q}\) in the upper triangle, and the corresponding
bound for the other cross role. By (6), the difference of the original
pack positions is at least
\[
 2c-14\sqrt{T_Q}-4E.
\]
Choose \(c\) so this is positive. Equation (9) then gives a physical
row-gap lower bound of
\[
 8Dc-56D\sqrt{T_Q}-16DE-3D-|b_0-a_0|.
\]
Thus all P slot gaps \(q\le Q\) are excluded if
\[
 8Dc>|b_0-a_0|+D(56\sqrt{T_Q}+16E+3)+S^2Q^2/4-1.            \tag{11}
\]
The lower triangle is identical after reversing the sign. The exact
Pythagorean bound used here is \(|Y|\le S^2q^2/4-1\).

The least band width satisfying (11) has
\[
 c=O(Q^2+E+\sqrt Q+1).
\]
Across the four color products, the band costs \(O(hc)\) labels. Combining
all discarded families gives
\[
 n_E=O(h^{3/2}\log h+hQ^2+h).                               \tag{12}
\]
Use the same positional-relocation factor \(T(h)=h^{o(1)}\) as in the
conditional scaffold, with \(T(h)\ge1\), and take
\[
 Q=\left\lfloor\frac{\eta\sqrt h}{T(h)\log(2h)}\right\rfloor.
\]
Then \(Q=h^{1/2-o(1)}\), \(c=o(h)\), and
\[
 n_E T(h)^2
 =O\bigl(h^{3/2}T(h)^2\log h+h^2/\log^2 h+hT(h)^2\bigr)
 =o(h^2).                                                   \tag{13}
\]
There are at most \(196\cdot4\cdot2=1568\) ordinary occupied runs.
Their total width and the cited constant number of collars remain \(O(h^2)\).
Full occupancy still removes FW within each run.

## 5. What this changes, and what remains open

The physical row lists vary over unbounded distances. Formula (1) has
variance proportional to the number of words, while (7)–(8) give a direct
point-mass bound for long occurrence spacings. This differs from permuting
the order within fixed-count blocks, whose cumulative color discrepancy
would remain bounded.

The randomness therefore changes actual cross-row differences and the P
arithmetic. It preserves constant locality, one-label safety, physical
microtiles, full occupancy, and the conditional quadratic relocation budget.

The open step is a joint constraint estimate. A P event compares several
row occurrences, and many events share the same word choices. The one-spacing
bound does not imply a local-lemma condition, bounded typed degeneracy, or
solvability of the new permutation system. Conditioning on all other P
events, on arbitrary exterior labels, or on the final cropping endpoints
is not covered by (7)–(8).

Cropping does give the safe unconditional inequality
\(\Pr(\text{spacing event and both endpoints retained})
\le\Pr(\text{spacing event})\). Conditioning only on the high-probability
event (3) increases an unconditional event bound by at most its reciprocal
probability. Neither observation supplies arbitrary conditional independence.

The full-board conclusion remains conditional on the stated relocation and
collar inputs and on avoiding long P, \(\Lambda_3,\Lambda_4\), R2s, and 6PT
for this new random scaffold. No previous four-system decomposition is
transferred to these row lists.

Independent review: the complete written proof, including the stopping-word
conditioning, inverse physical-spacing bound, cross-color band, and
relocation accounting, passed a separate audit.

## 6. A fixed P test has small probability

Write \(\mathcal G\) for concentration event (3). Fix two colors and fixed
occurrence indices with \(j-i\ge\Delta>2E+4\). For every prescribed
physical pack difference \(z\),
\[
 \Pr\!\left(w_{p_j^\beta}-w_{p_i^\alpha}=z\ \text{and}\ \mathcal G\right)
 \le\frac{C}{\sqrt{\Delta-2E}}.                             \tag{14}
\]
For the same color this follows directly from (8). For different colors,
reveal through the word containing \(p_i^\alpha\). At that position,
\[
 C_\beta(p_i^\alpha)=p_i^\alpha-i\le i+2E
\]
on the past portion of \(\mathcal G\). The target occurrence of color
\(\beta\) therefore requires at least \(\Delta-2E\) further occurrences,
up to a fixed endpoint adjustment. Absorb the at most two already revealed
symbols after the starting position. The proof of (7) applies to the fresh
suffix. Integrate over the allowed revealed histories and discard the
remaining future concentration conditions to obtain (14).

Now prescribe a positive horizontal length \(X\). There are at most
\(\tau(X^2)\) positive integers \(Y\) for which \(X^2+Y^2\) is a square:
each such \(Y\) gives a factor pair \((L-Y)(L+Y)=X^2\). Thus one fixed
cross-parity P test between occurrence indices separated by \(\Delta\)
satisfies
\[
 \Pr(\mathrm P_X\text{ and }\mathcal G)
 \le\frac{C\tau(X^2)}{\sqrt{\Delta-2E}}.                    \tag{15}
\]
Fixed residue offsets, within-pack row offsets, and the factor \(D\)
only select a subset of possible pack differences.

For actual in-strip P, \(X\le h-1\). Hence the two macrotiles have rank
distance \(O(h/S)\), and their coordinate indices differ by \(O(\sqrt h)\).
The band chosen in (11) has \(c\asymp Q^2=h^{1-o(1)}\), so for all
sufficiently large \(h\), both cross-role occurrence-index differences
are at least \(c/2\), and \(c\gg E\).

The deterministic crop (9a) makes the macrotriangle order and each possible
horizontal slot gap fixed before the random words are exposed. A fixed
pair of physical \(4\times4\) tiles has only 256 label pairs and at most
31 relative slot offsets. A union bound therefore gives
\[
 \Pr(\text{this tile pair has an actual P candidate and }\mathcal G)
 \le \frac{C}{\sqrt c}\max_{1\le X\le h}\tau(X^2).          \tag{16}
\]
Constants absorb both cross-parity roles. Conditioning only on
\(\mathcal G\) divides these bounds by \(\Pr(\mathcal G)\).

The word “actual” in (16) matters: it supplies \(X\le h-1\).
The estimate does not cover arbitrary candidate diagonals with out-of-strip
alternative vertices through the same argument. Nor does summing (16)
over all nearby tile pairs give a bounded degree or a joint avoidance theorem.

Independent review: all of Section 6 passed a separate check. The deterministic
prefix in (9a) incorporates the reviewer's dependence correction for the
tile-pair application (16). The final review checked both this correction
and the actual in-strip hypothesis that makes (16) applicable.
