# A repeated-row ladder has no extra sampling equations

15 November 2026. In the usual private palette, a parallel-path Hall
witness can impose exactly the same row equations as one ordinary
directed path. The number of visible copies must not be used as a count
of independent sampled row constraints.

## 1. Exact replication at a common private offset

Let label \(r\) have rows \(a_r,b_r\), and let its \(M\) private slots be
\[
                         x_{r,t}=S(Mr+t),\quad 0\le t<M.         \tag{1}
\]
At unused slots one chooses a nonempty subset of these same two rows.
The label must appear as a double at least once.

Suppose a directed zero-offset P path has label sequence
\[
                         r_0\longrightarrow r_1
                              \longrightarrow\cdots\longrightarrow r_M.
\]
Its norm equations are
\[
 [SM(r_{i+1}-r_i)]^2+(b_{r_{i+1}}-a_{r_i})^2=L_i^2.             \tag{2}
\]
For every private offset \(t\), exactly these equations describe the
edges \((r_i,t)\to(r_{i+1},t)\): both coordinate differences are
independent of \(t\). The vertical alternative rows are also independent
of \(t\). Thus their in-strip conditions repeat identically.

If these copies are genuine P exclusions, a double at one path vertex
forces every later path vertex to be odd-only at that offset. Hence at
most one of the \(M+1\) labels can be double on each of the \(M\)
parallel paths. Compulsory double placement is impossible.

This recovers the path-height obstruction in
[the private-stub note](continuation_private_parity_stub_obstruction.md)
and the matching formulation in
[the one-direction note](continuation_single_direction_p_matching.md).
It is not a new claim that an arbitrary prescribed path embeds into the
actual Hilbert scaffold.

## 2. What random row sampling can and cannot charge

Under any random construction of the row pairs, the intersection of
the norm events (2) over all \(M\) offsets equals the event (2) at one
offset. Its probability is not the \(M\)-th power of that probability.
Every repeated row is the same random variable in all copies.

Actual rectangle exclusions additionally require their midpoint and
owner conditions. Those checks can depend on the private offset and
the final placement of the owner. They must be proved separately for
an actual Hall obstruction. They do not introduce independent row
variables into the repeated norm equations.

Consequently an additional sampling saving for parallel paths requires
some additional structure: nonzero offset differences that change the
norm equations, genuinely different row options, or a geometric theorem
excluding the common-offset path itself. Counting the rectangular array
of repeated copies alone supplies none of these.

## 3. Distinction from a permutation block

A full-occupancy permutation block contains distinct labels and assigns
them bijectively to its slots. It does not place one label's repeated
pair at all private offsets. Its matching constraints therefore require
a separate analysis; this replication lemma neither proves nor disproves
their solvability.

Independent review: the full note passed a separate check of the
offset cancellation, repeated-variable probability statement, path
propagation, and the retained owner and actual-embedding qualifications.
