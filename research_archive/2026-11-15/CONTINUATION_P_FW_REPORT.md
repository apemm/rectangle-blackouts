# P solvability and FW across cuts

15 November 2026. This round follows `p_dec_all_scales.md`,
`p_two_block_selfsimilar.md`, and `h7_excursion_transfer.md`.
The target remains a construction of width O(h^2).

The two requested steps remain open. The progress is a sparse deletion
theorem for P, a precise obstruction to local H7 seas, and an alternative
way to remove FW by keeping the slot lattice fully occupied. All results
below distinguish the original private-choice problem from that alternative.
Nothing here establishes a new full-board threshold bound.

## 1. The four-system reduction passes its audit

[The cut audit](continuation_dec_cut_audit.md) confirms the isolated
corner cuts and the reduction to the four canonical systems at each scale:
Gamma with either orientation, and Omega with either orientation.
This is the original full-grid private-choice system at S=32, M>=3,
with uncompressed Hilbert ranks.
There are no P constraints between distinct pieces. The remaining task
is uniform solvability inside those pieces, not compatibility between them.

The same audit supplies two structural refinements.

- The corner-cut comparison works with the weaker rank-length estimate
  d < |U|(|U|+1)/27 + 1, provided the three other separation hypotheses
  are retained. This is not an automatic transfer to a new layout.
- Every candidate edge joins equal or adjacent bands of
  floor(log_4(|T|+2)). Thus a band-by-band extension can retain only the
  current band as its frontier. The frontier has no proved bounded size.

For certified constraints, two-terminal modules have an exact finite
message: their attainable terminal differences in Z/MZ. Series composition
takes a sumset and parallel composition an intersection. At M=3, the sum
of two sets of size at least two is all of Z/3Z. This would support an
induction if the actual pieces had a suitable small-separator decomposition.
No such decomposition is proved here. These modular shift rules do not
automatically apply to integer-difference constraints.

[Offset reachability](continuation_p_type_reachability.md) is also proved.
Every fixed nonzero offset type occurs in sufficiently large canonical
blocks. A finite candidate obstruction in such a type would therefore
persist at larger scales. Candidate failure still needs completion-row
and owner checks before it becomes a full-board obstruction.

## 2. Nearby Pythagorean legs can be isolated cheaply

The main arithmetic result is
[the sparse multiple-leg theorem](continuation_p_sparse_multiple_legs.md).
Fix an even S and M>=3, keep the original Hilbert ranks, and use

\[
 x_r=S(Mr+\xi_r),\qquad 0\le\xi_r<M.
\]

There is a deterministic set of O_{S,M}(h^{3/2}) labels whose deletion
leaves at most one forbidden slot value per cross-parity role of a pair.
Every remaining pair consequently forbids at most two integer differences.

The saving comes from a weighted Pell count. If the same odd vertical
leg Y has two horizontal legs X and X+g with g at most 2S(M-1), let f
be their hypotenuse difference. Subtracting the norm identities gives

\[
 0<f<g,\qquad (g-f)X<fY.
\]

If both legs belong to the same rank-pair choice interval, its rank
distance is less than 2Y+1. Hilbert locality then places both labels
within O(sqrt(Y)) diagonals of T=Y/2 or T=-Y/2.

For fixed g and f, the possible Y belong to finitely many Pell orbits.
Their positive terms grow geometrically. In particular,

\[
 \sum_{\substack{Y<h\\Y\text{ exceptional}}}\sqrt Y
 =O_{S,M}(\sqrt h).
\]

Deleting those diagonal bands costs O(h) labels per diagonal, proving
the h^{3/2} bound without a logarithm. The proof, including the weighted
orbit sum, passed independent review.

The only standard existence input is a positive norm-one Pell unit for
a positive nonsquare discriminant. This was checked against
[the Pell existence theorem in the mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Pell.html#Pell.exists_of_not_isSquare).
The reduction to finitely many orbits and the weighted estimate are
derived in the note. The new results have not been formally verified.

The theorem extends to each fixed H7 profile by replacing the band centres
with (plus or minus Y minus c)/28, where c is the profile's fixed row
offset. [The relocation audit](continuation_adjacent_sea_and_p_relocation_audit.md)
records this extension. Under the archive's existing hypothesis (Rel),
moving these labels costs

\[
 h^{3/2+o(1)}+O(h^2)=O(h^2).
\]

This is a conditional accounting statement. A complete use still needs
the H7 relocation/gluing hypothesis and avoidance of every other family
in the final occupancy. Deleting a label creates an F point, so filler
constraints must be checked after deletion or through a proved envelope
covering all occupancy states. The original ranks must not be compressed.

### What this says about small obstructions

[The three-label lemma](continuation_three_label_integer_lemma.md)
proves that three variables in {0,1,2}, with at most two forbidden integer
differences per pair, are always satisfiable. Therefore the retained
P system has no obstruction on at most three labels.

A separate [three-leg spacing theorem](continuation_three_leg_spacing.md)
states that if three horizontal legs, all divisible by a stride S with 4|S, share an odd
vertical leg Y and have total span H, then

\[
 Y<\frac{H^3}{16S\gcd(Y,S)}.
\]

At S=32 and M=3 this reduces the possible three-leg exception to Y<4096.
Two independent exact enumerations agree on all 1285 vectors in that
range and find no two slot values within distance four. Combining the
finite check with the theorem proves that no two-label integer
obstruction exists at any height, even before deletion.

These conclusions concern the integer system. They do not exclude
two-label obstructions in the stronger certified modular system.

Multiplicity control does not settle larger systems.
[Explicit abstract examples](continuation_p_simple_constraint_obstructions.md)
show that a four-variable obstruction can have only one forbidden
difference per pair. A five-variable example is both bipartite and
ordinary two-degenerate, with two forbidden differences per pair.
Neither example is asserted to occur in P geometry. They show why the
next argument must use that geometry, rather than ordinary degree alone.

## 3. Local H7 seas do not repair the cuts

[The FW and local-module note](continuation_fw_local_module_barrier.md)
proves the useful geometric part of the proposed repair. If a support's
black rows span R, its horizontal extent is O(R^2), with explicit bounds
for tilted triangles, mixed four-supports, and pairs of tilted rectangles.
For dyadic excursion sizes B_x=2^{v_2(x)},

\[
 \sum_{x=1}^{Q-1}B_x^2=\frac{Q(Q-1)}2.
\]

Thus separating genuinely local modules has a quadratic total budget.
This calculation alone does not provide filled connectors or a safe sea.

The obstruction to using H7 locally is stronger than an external
Pythagorean rival. Write p=H-L, q=H-F, and choose epsilon in {1,-1}
so that epsilon p is a square modulo seven. The three sea cells

\[
 (\epsilon p,H),\quad (0,F),\quad
 (\epsilon(p+q),L)
\]

form a right angle and complete to

\[
 (\epsilon q,L+F-H).
\]

The completion column is low, but its row has the opposite parity.
It is a fatal, unparked triangle whenever L+F-H is at least one. The
configuration fits in a run of length p+q+14 and can avoid every column
eligible for label substitution. No labels are needed to create it.

Consequently a reusable H7 profile in the full ambient strip must satisfy

\[
 L+F-H<1.
\]

A profile confined to rows t+O(B), with t much larger than B, fails this
condition. Removing excursions smaller than sqrt(h) does not repair the
remaining local profiles. Keeping L and F near the global boundary avoids
this particular obstruction, but loses the local row span needed by the
quadratic separator calculation. The triangle and its scope passed an
independent check.

A second tested background also has a limitation.
[The adjacent-row checkerboard note](continuation_adjacent_sea_repair_obstruction.md)
exhibits one inserted label requiring at least
tau(d(d-1)/2) changes to other columns. Along d=3^{2k+1}, this is
Omega(log h). This rules out a bounded number of patches per label in
that background. It is not a lower bound on width and does not exclude
shared repairs or a different sea.

## 4. Full occupancy removes FW, but changes the P problem

There is a positive alternative to local seas. Keep the occupied label
columns equal to a full arithmetic interval. For an FW triangle, write

\[
 X\xi=-\delta(F-y),\qquad
 x_g=x_e+X+\xi.
\]

In H7, y>F and the divisibility conditions force any in-strip FW event
to have delta>0. Hence X and xi have the same sign. The would-be F source
at x_e+xi lies strictly between the occupied endpoints x_e and x_g.
Arithmetic closure makes that source occupied too, so its F point is
absent. FW is impossible.

This motivates bounded permutations within consecutive Hilbert-rank
blocks, instead of independent private choices. Such permutations retain
every slot. If a block has at most b labels, an old rank distance is at
most (2b-1) times the new distance. A constant increase in stride therefore
preserves the same-parity distance estimate. The exact statement and
remaining family list are in
[the full-occupancy note](continuation_full_occupancy_permutations.md).

This is a different P constraint system. Existing certificates and the
four-system reduction cannot be transferred without a new proof.
Nor may deleted labels or padding holes be inserted into the argument:
they destroy the required full occupancy. Six-cell parked collisions
remain among the constraints.

The simplest permutation rule already fails in the ordinary-row full
grid, whose label rows are 2i+1 and 2j+2.
[The pair-swap obstruction](continuation_pair_permutation_obstruction.md)
constructs a vertical rival that survives every independent swap of
consecutive pairs. For a power-of-two stride S>=4, take q=S^2 and a Hilbert
square of side q. Two nearby dominoes keep an odd row and an even row
fixed in both of their slots. The resulting pair has horizontal leg 2S,
vertical leg S^2-1, and hypotenuse S^2+1. Its common corners remain white
under all swaps, and the axis owner lies elsewhere. Thus this is a genuine
rival, not just failure of a stronger candidate test.

The same local pattern extends to the H7 residue block with row bases
1 and 28. Choose a small Hilbert block with coordinate offset S^2/28,
and translate it far enough into the bulk. The two dominoes' fixed rows again
differ by S^2-1. This defeats pair swaps that retain those original
arithmetic rank positions. It does not defeat a construction that splits
the intervals, changes those positions, or uses larger permutation blocks.
Uniform solvability for the latter models, arbitrary-height full
occupancy, and the other support families still need proofs.

## 5. What to attack next

The most focused continuation of the original route is an extendability
invariant for the integer P systems after the sparse exceptional bands
are removed. The proved band locality and terminal-difference rules
identify possible induction interfaces, but neither gives a nonempty
set of extensions yet. Any successful invariant must rule out the actual
geometric realizations of the larger abstract obstructions.

For FW, full occupancy is the more concrete alternative left by this
round. A block of four labels is a useful next test: its 2-by-2 Hilbert
block lacks the fixed-row property used by the pair-swap obstruction.
That does not itself prove solvability. A positive result would still
require a fresh P reduction and a way to keep every slot occupied at
arbitrary heights.

The local H7 proposal should not be reused without changing its sea:
the explicit zero-label triangle is an obstruction to that premise.
The O(h^2) theorem, uniform solvability of the four original systems,
and a complete FW-compatible board are all still open.

## Checks and file scope

- The three-label lemma was checked by proof and all 4096 finite systems.
- The three-leg cutoff was checked by independent divisor and Euclid
  enumerations, with identical full vector sets.
- The abstract larger obstructions have small exhaustive checkers.
- The pair-swap obstruction has a sparse exact-coordinate checker.
- Independent readers checked the sparse Pell count, general-stride
  spacing bound, offset reachability, cut reduction, and sea obstructions.

This round creates continuation notes and small checkers only. It does
not change the paper, claim ledger, pre-existing archive notes, or
pre-existing manifests. Nothing is committed.
