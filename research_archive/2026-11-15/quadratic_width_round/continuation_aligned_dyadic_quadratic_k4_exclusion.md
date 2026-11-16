# Aligned Hilbert tiles exclude the dyadic common-factor K4 family

15 November 2026. This is a uniform exclusion for a concrete possible
obstruction to the original S=32,M=3 private-choice systems. It covers
all four-vertex orientations and every 2-adic valuation of the rank
step. The proof combines the norm congruence with a finite carry
certificate; it is not a scan through finitely many heights.

The result is restricted to a power-of-two quadratic scale. Arbitrary
odd factors in that scale, other combinations of norm representations,
and unsatisfiability without a clique remain open.

## 1. Statement and the aligned congruence

Suppose four canonical Hilbert labels have ranks R,R+d,R+2d,R+3d,
where d>0. Write t=v2(d). Choose one cross-parity role for each of
the six pairs. Assume all six selected norm vectors have the common
quadratic form

\[
 X=96dm,\qquad Y=B_0-2cm^2>0,\qquad L=B_0+2cm^2,
 \quad m\in\{1,2,3\},
 \tag{1}
\]

where c is a power of two and B0 is odd. Their norm identities force

\[
 c=2^{7+2t},\qquad B_0=9(d/2^t)^2.
 \tag{2}
\]

For raw coordinates (i_u,j_u), a selected role u->v consequently has

\[
                       j_v-i_u=C-c(v-u)^2,
 \tag{3}
\]

where the common C satisfies B0=2T+1+2C and T is the physical row-index
offset. In a canonical aligned type, T is divisible by the tile side.
Since every relevant tile has side at least 4, (2) gives the necessary
condition

\[
                              C\equiv0\pmod4.
 \tag{4}
\]

**Theorem.** No such four labels exist in an aligned canonical Hilbert
tile. More strongly, the geometric potential equations (3), the exact
rank AP, (2)'s value of c, and the congruence (4) are already inconsistent.

This explains why the
[integer-offset counterexample](continuation_unaligned_hilbert_k4_certificate.md)
does not transfer to an aligned type: it has C=2561, which violates(4).
The theorem is uniform in t, rather than checking a bounded list of
rank-step valuations.

## 2. The easy orientations

Orient each of the six pairs by its selected odd-to-even role. A
transitive tournament contains two sources pointing to the same two
targets. Subtracting those four equations in(3) gives

\[
                    2c(r_i-r_j)(r_u-r_v)=0,
 \tag{5}
\]

which is impossible for distinct AP multipliers.

If there is a source or sink and a directed triangle on the other
three vertices, those three label coordinates are congruent modulo
2^(7+2t). Their rank differences include both d and 2d. One of the
valuations t,t+1 is even and below 2(7+2t). This contradicts the
[Hilbert orbit lemma](continuation_hilbert_quadratic_clique_exclusions.md):
coordinate-congruent points have rank difference either divisible by
the square of the coordinate modulus or of odd 2-adic valuation.

The remaining orientations have score sequence (1,1,2,2). There are 24
of these. The finite proof below treats all 24.

## 3. The two potential components

For a strong orientation, make a bipartite graph whose vertices are
four odd-coordinate variables and four even-coordinate variables.
Each edge u->v has the equation(3). After the common C is removed,
the graph has two tree components, with six and two vertices.

Assign integer potentials p to these graph vertices so an edge u->v
has p_v-p_u=-(v-u)^2. Shift each component's potentials so its minimum
is zero. This determines eight nonnegative integer coefficients.

Write the bases of the large component as A for odd coordinates and
B for even coordinates. Write the bases of the small component as Z
and W. They satisfy

\[
                            A+W=B+Z,\qquad C=B-A.
 \tag{6}
\]

Every actual coordinate is its appropriate base plus p c. Thus the
four coordinate pairs have the pattern(A,B), except that one odd
coordinate uses Z and one even coordinate uses W. The two exceptional
positions are the source and target of the isolated bipartite edge.

We may assume all four bases are nonnegative. Any finite canonical
Hilbert square can be embedded, with unchanged relative ranks, into
a far diagonal identity child of a larger square by repeated
quadrant-two descents. The resulting common coordinate translation
makes the bases nonnegative and preserves(3), (4), and the rank AP.
All coordinates are then represented by ordinary binary expansions.

## 4. A finite prefix calculation that covers every t

Use the four Hilbert orientation states and the three carries from
the [earlier carry proof](continuation_hilbert_quadratic_clique_exclusions.md).
The initial set has 256 states: arbitrary orientations and zero carries.
Call the unrestricted one-bit transition U. Call the transition with
q1=q0 Z0, where q_i are the next base-four rank digits. The first
nonzero rank-step digit is odd when t is even and equals 2 when t is odd.

While the first 7+2t coordinate bits are read, c has zero bits. The
coordinate coefficients p c therefore have no effect on these bits.
Condition (4) is exactly equality of the first two bits of A and B.

For t=0,1,2,3, apply these restrictions directly for 7+2t levels. This
is a fixed finite prefix calculation, not the whole argument.
For t>=4, put t=2j+epsilon with j>=2 and epsilon in{0,1}.
The first two levels have zero rank-step digits and equal A/B bits.
Their reachable set L has 32 states and is invariant under Z0:

\[
                              Z_0(L)=L.
 \tag{7}
\]

Therefore the next j-2 zero-step levels do not change the set.
Apply the first nonzero digit transition D_epsilon. The remaining
number of zero-c coordinate levels is

\[
 (7+2t)-(j+1)=6+3j+2\epsilon.
 \tag{8}
\]

The possible end-of-prefix states for all j>=2 are consequently the
union of the two sequences

\[
 U^{12+2\epsilon+3l}D_\epsilon(L),
                         \qquad l=0,1,2,\ldots.
 \tag{9}
\]

These are orbits of the single finite set map U^3. Exact iteration
shows periods of one or two, with no preperiod. The full state sets,
not just their counts, are included in the certificate. Together with
the four small t cases, they give prefix seed sets of size 0,30,40, or 174,
depending on the positions of the isolated edge.

This reduction is the reason the certificate is uniform in t. It does
not infer an infinite conclusion from a run over t=0,...,5.

## 5. Retaining the exact offsets above the prefix

After 7+2t levels, each coordinate's unprocessed offset is exactly its
integer coefficient p. Append these eight coefficients as carries to
each prefix state. A full state now has four orientations, three
relation/AP carries, and eight coordinate-addition carries.

For each next choice of the four base bits, coordinate i has next bit

\[
          (\text{base bit}+\text{its carry})\pmod2,
 \tag{10}
\]

and new carry equal to the integer quotient by 2. Feed those actual
coordinate bits into the Hilbert transition table, and enforce the
base relation (6) and the two AP equations using their existing carries.
All coordinate carries stay between zero and their initial coefficient.
The reachable state graph is therefore finite.

An actual finite-square solution would end at the all-zero state:
canonical outer orientations, zero AP and base-relation carries, and
zero coordinate-addition carries. The exact breadth-first certificate
shows that this state is unreachable for each of the 24 strong
orientations. The largest reachable graph has 852 states.

The graph is explored to closure, so arbitrary additional binary
levels are covered. Combining this with Section4 proves the theorem
for every t and every tile side.

## 6. Reproducibility and limits

The checker generates all 64 four-vertex tournaments. It separates
the 24 transitive, eight source-cycle, eight sink-cycle, and 24 strong
orientations. For every strong orientation it derives the potential
coefficients from the equations, rather than using a fitted template.
It then regenerates the prefix invariants, the complete U^3 orbit
certificates, and the entire exact-offset reachable graph.

The output stores all prefix sets and all reachable states. Its run
passes all 24 strong orientations, with seed sizes {0,30,40,174} and
maximum reachable size 852. The written reduction and this finite exact
calculation are both parts of the proof.

If c has an arbitrary odd factor b, norm integrality only implies
C=(b-1)/2 modulo4. The later bits of c then become additional inputs
in the offset automaton. The present certificate does not cover them.
Allowing those inputs in a relaxed mod8 system leaves accepting states;
there is no general aligned exclusion from that relaxation alone.

Nor does the theorem exclude cliques using different large half-factors
on different edges, opposite signed norm heights, or three-choice
unsatisfiability without a clique. It removes one structured infinite
family from the aligned problem.

Files: [checker](check_aligned_dyadic_quadratic_k4.py) and
[complete finite certificate](check_aligned_dyadic_quadratic_k4.json).

The full written proof and finite certificate passed an independent review.
The independent reader regenerated the orientation table directly from
transformed unit quadrants, substituted it into the checker, and matched
every saved state: all 24 orientations, seed sizes 0,30,40,174, maximum
reachable size 852, and the two period-one/two U^3 orbits. The review also
checked the uniform-t reduction and the nonnegative-base embedding.
