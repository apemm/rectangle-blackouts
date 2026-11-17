# Odd scale factors: exact alignment prefixes for quadratic K4 patterns

This note extends the quadratic-potential exclusion beyond a pure power of
two scale. It concerns the common-factor quadratic family only. It does
not classify all four-label private-choice obstructions.

The finite prefix certificate proves the following statement for the
Hilbert ordering at stride 32 with three private choices, in any of its
four recursive orientations.

**Proposition.** Suppose four labels have ranks

\[
 R, R+d, R+2d, R+3d
\]

in a square of side \(2^N\) with a common outer orientation, and the selected role on each pair
satisfies

\[
 j_v-i_u=C-c(v-u)^2.
\tag{1}
\]

Write

\[
 d=2^tD,\qquad c=2^{7+2t}b,\qquad b,D\text{ odd},\quad b>0.
\tag{2}
\]

If \(t\in\{0,1,2,3\}\), these equations cannot give an aligned
common-factor Pythagorean K4. The conclusion holds for every odd factor
\(b\), rather than a finite list of tested factors.

The certificate is
`check_hilbert_rational_alignment_prefix.py`, with its saved JSON. The
proof combines exact arithmetic reductions with a finite state
enumeration. No upper bound on \(N\) or \(b\) is imposed. Independent
review of this new certificate is complete: the independent reader
regenerated the Hilbert transition table from transformed unit quadrants
and reproduced all 96 cases, including the signed terminal tests. The
modulus-512 witness was also checked independently by separate forward
and inverse Hilbert routines.

## 1. The full alignment condition

For a pair with rank-index difference \(m\), the intended norm identity
is

\[
 (96dm)^2+(B_0-2cm^2)^2=(B_0+2cm^2)^2,
 \qquad B_0=\frac{9D^2}{b}.
\tag{3}
\]

If the raw tile offset is \(T\), then

\[
 B_0=2T+1+2C.
\]

Consequently an aligned tile, for which \(2^N\mid T\), necessarily
satisfies

\[
 b(2C+1)\equiv9D^2\pmod{2^{N+1}}.
\tag{4}
\]

There is a separate odd divisibility condition \(b\mid9D^2\). The
prefix exclusion below does not need this divisibility condition:
there are no finite geometric terminal states on the surviving prefix
paths.

The previous dyadic-factor theorem used only \(C\equiv0\pmod4\).
Condition (4) retains the actual odd rank-step digits and is stronger
than merely checking whether an expression is an odd square modulo 8.

## 2. A finite geometry witness survives modulus 512

Small fixed moduli do not suffice. In the square of side \(2^{22}\),
consider

| Label | Coordinates | Hilbert rank |
|---|---:|---:|
| 0 | \((536906,668149)\) | 612580740983 |
| 1 | \((953259,506485)\) | 829719411574 |
| 2 | \((791595,90132)\) | 1046858082165 |
| 3 | \((1384363,506485)\) | 1263996752756 |

The common rank difference and potential parameters are

\[
 D=217138670591,\qquad c=53888=128\cdot421,
 \qquad C=-231222.
\]

Equation (1) holds for the roles

\[
 1\to0,  0\to2,  3\to0,  2\to1,  1\to3,  2\to3.
\]

Direct calculation gives

\[
 v_2\bigl(421(2C+1)-9D^2\bigr)=9,
 \qquad 9D^2\equiv335\pmod{421}.
\tag{5}
\]

Thus this actual Hilbert geometry passes the required congruence modulo
512. It fails both the full modulus \(2^{23}\) and the odd divisibility
condition. It is **not** an aligned Pythagorean K4.

The search-independent checker
`check_hilbert_alignment_residue_witness.py` verifies the ranks by a
recursive coordinate-to-rank routine and an iterative rank-to-coordinate
routine, all six potential identities, and both failures in (5).

## 3. Why the next odd-factor bit is already determined

Put \(k=7+2t\). At coordinate depth \(\ell\), the lower \(\ell\)
bits of each base coordinate have been read, and the lower \(2\ell\)
bits of each Hilbert rank have been read. In particular,

\[
 C\pmod{2^\ell},\qquad D\pmod{2^{2\ell-t}}
\tag{6}
\]

are determined once the rank-step valuation has been selected.

The first \(k\) bits of \(c\) are zero. At depth \(k+j\), its next
bit is bit \(j-1\) of \(b\). From (4), any solution in a square whose
depth is at least \(k+j\) must have

\[
 b\equiv9D^2(2C+1)^{-1}\pmod{2^j}.
\tag{7}
\]

The denominator is odd. The right side of (7) is known **before** reading
coordinate depth \(k+j\): the preceding depth determines enough digits
in both entries of (6). Thus the next scale bit is forced, rather than
branched over. Its first value is one because \(D\) is odd.

This is a finite-prefix use of a rational 2-adic identity. It does not
assume that a finite aligned tile satisfies that identity at arbitrarily
high moduli. Terminal tests are made at every finite square size before
the search proceeds to deeper prefixes.

## 4. Exact transitions and signed potential bases

The 24 strong tournament templates are the same as in
`continuation_aligned_dyadic_quadratic_k4_exclusion.md`. Each has four
potential bases \(A,B,Z,W\), with

\[
 A+W=B+Z,
\tag{8}
\]

and eight coordinates of the form \(B_i+p_i c\), where
\(B_i\in\{A,B,Z,W\}\) and \(p_i\ge0\) is an explicitly generated
integer. The other tournament types are excluded by the earlier
potential and Hilbert orbit arguments, which apply to every odd \(b\).

The state contains four Hilbert orientations, the carry in (8), the two
arithmetic-progression carries, and eight coordinate-addition carries.
It also records the exact signed differences of the prefixes of \(B-A\)
and of the first two ranks, together with the scale prefix. The next
scale bit is supplied by (7). The coordinate and rank transitions are
otherwise exactly the previously audited transitions.

One finite-size detail matters. The potential bases need not be
nonnegative even when every label coordinate is nonnegative. A larger
identity embedding cannot remove this issue here, because it changes
the alignment modulus. The new checker therefore permits signed bases
at a finite terminal state.

At depth \(N\), let \(a,b',z,w\) denote the nonnegative base residues.
All final coordinate carries belonging to the same base must have a
common value \(q_A,q_B,q_Z,q_W\), respectively. The actual bases are

\[
 A=a-2^Nq_A,\quad B=b'-2^Nq_B,
 \quad Z=z-2^Nq_Z,\quad W=w-2^Nq_W.
\tag{9}
\]

The final carry \(q_0\) in (8) must satisfy

\[
 q_0=q_A+q_W-q_B-q_Z.
\tag{10}
\]

The four parent orientations must all equal one common orientation
\(g\); it need not be the canonical orientation zero. The two
rank-progression carries must be zero. Conditions (9)--(10), together
with these orientation and rank conditions, are necessary and
sufficient to reconstruct four coordinates in the finite oriented
square from the bit state.
Changing from the prefix difference to the signed value of \(C\)
changes \(2C\) by a multiple of \(2^{N+1}\), so the terminal test of
(4) uses the recorded prefix difference directly.

Every strong template has a coefficient spread of at least three among
coordinates sharing one base. Thus a finite realization requires
\(3c<2^N\). No terminal realization is lost by starting the terminal
tests after the first nonzero scale bit.

## 5. Exhaustion and its meaning

For each \(t=0,1,2,3\), the checker starts from all \(4^4\) lower
orientation states. It imposes the zero base-four rank-step digits and
then the first nonzero digit required by \(v_2(d)=t\). It retains every
transition allowed by (7)--(8), the coordinate equations, and the two
rank progression equations.

The maximum values over the 24 strong orientations are:

| \(t\) | Latest empty depth | Largest prefix set | Finite geometric terminal states |
|---:|---:|---:|---:|
| 0 | 52 | 9528 | 0 |
| 1 | 36 | 704 | 0 |
| 2 | 53 | 68388 | 0 |
| 3 | 15 | 96 | 0 |

Every case reaches an empty prefix set. There is no memory or depth
cutoff in these certified cases. A solution in a shallower square would
give a finite terminal state; none occurs, including the signed-base
terminals above. A solution in a deeper square would give a surviving
prefix at the empty depth; that is impossible. This proves the
proposition for all side lengths and all odd factors at these four
valuations.

The direct representation has not produced a uniform result for
\(t\ge4\). Its exact prefixes grow before the first scale bit. A
bounded-register projection is a possible next step, but neither a
uniform exclusion nor an aligned counterexample follows from the
current calculation.

## 6. Quotient normalization and a uniform residue exclusion

There is an additional geometric reduction for large \(t\). Put
\(j=\lfloor t/2\rfloor\) and \(\epsilon=t-2j\). This section assumes
\(j\ge1\).

**Common-residue lemma.** All four coordinate pairs have the same
residue modulo \(2^j\). Write this residue as \((x_0,y_0)\). Quotienting
the corresponding aligned squares gives four Hilbert labels with the
same outer orientation
whose ranks remain an arithmetic progression, now of step
\(2^\epsilon D\), and whose potential parameters are

\[
 c'=2^{7+3j+2\epsilon}b,\qquad
 C=2^jC'+y_0-x_0.
\tag{11}
\]

To prove the first step, use that an even rank difference gives equal
checkerboard parity. Since \(c\) is even, the large component of a
strong template gives three equal first-coordinate bits and three
equal second-coordinate bits. The two exceptional coordinate bits must
then agree with the corresponding common bits. If \(4\mid d\), the
four ranks also have the same lowest base-four digit. Dividing the
coordinates by two and the ranks by four therefore preserves their
exact arithmetic progression. Repeat \(j\) times.

The common residue is further restricted:

\[
 x_0=y_0
 \quad\hbox{or}\quad
 x_0+y_0=2^j-1.
\tag{12}
\]

Indeed, equality of the common low rank word means that the four
quotient orientations send \((x_0,y_0)\) to the same point. The
orientation group consists of identity, coordinate swap, simultaneous
reflection, and reflected swap. At an integer point in an even-sided
square, its stabilizer is nontrivial only on the two diagonals in
(12). Simultaneous reflection has no fixed integer point.

The stabilizer must be nontrivial here. The two labels lying in both
large coordinate groups are coordinatewise congruent modulo \(2^k\),
where \(k=7+2t\). If their quotient orientations were equal, the
Hilbert bit recurrence would give equal rank digits through level
\(k\). Their rank difference would be divisible by \(4^k\), whereas
its valuation is at most \(t+1<2k\). This is impossible.

In the diagonal case, the quotient orientations lie in one coset of
the subgroup generated by coordinate swap, and \(y_0-x_0=0\). In the
antidiagonal case they lie in a coset of the subgroup generated by
reflected swap, and

\[
 \theta:=2(y_0-x_0)+1
   =2^{j+1}-1-4x_0\equiv3\pmod4.
\tag{13}
\]

Thus the normalized alignment equation is

\[
 b\bigl(2^{j+1}C'+\theta\bigr)
 \equiv9D^2\pmod{2^{N'+j+1}},
\tag{14}
\]

where \(N'=N-j\), and either \(\theta=1\) or \(\theta\) is one of
the \(2^j\) values in (13). This reduction retains the precise
alignment modulus. It does not substitute the original stride-32
theorem into a different row spacing.

**Corollary.** No aligned quadratic K4 in this family has
\(b\equiv5\pmod8\), at any valuation \(t\).

For \(t\le3\), use the finite prefix proposition. For \(t\ge4\),
we have \(j\ge2\). In the diagonal case, reducing (14) modulo eight
gives \(b\equiv9D^2\equiv1\pmod8\). In the antidiagonal case,
reduction modulo four gives \(b\equiv3\pmod4\). Neither permits
\(b\equiv5\pmod8\).

The common-residue argument and its corollary have passed an independent
written review.

## 7. Every odd valuation is excluded

The normalization also permits a small uniform finite certificate.

**Theorem.** Under (1)--(4), the valuation \(t\) cannot be odd.

The case \(t=1\) is covered by Section 5. For \(t=2j+1\ge3\),
Section 6 gives a normalized rank step \(2D\) and

\[
 c'=2^{9+3j}b.
\tag{15}
\]

The four initial quotient orientations lie in a coset of either
\(\{1,\mathrm{swap}\}\) or
\(\{1,\mathrm{reflected\ swap}\}\). Equation (14) modulo four
forces

\[
 b\equiv1\pmod4\quad\text{in the first case},
 \qquad b\equiv3\pmod4\quad\text{in the second case}.
\tag{16}
\]

No other norm or alignment condition is needed for this certificate.

Let \(U\) be the ordinary zero-scale bit transition. The first
base-four rank difference digit is two. After reading it, the number
of remaining zero-scale coordinate levels is
\(8+3j\). Thus the possible seed sets for \(j\ge1\) form the orbit
under \(U^3\) starting from \(U^{11}\) of the first-digit state set.
The exact state-set orbits have preperiod zero and period at most two.

At the next two coordinate levels, the scale bits are respectively
\((1,0)\) or \((1,1)\), as prescribed by (16). For odd \(j\), all
states then disappear. For even \(j\), only tournament masks
\(4,12,51,59\) remain, with eight states for each coset. Allowing
**every subsequent scale bit** gives a closed finite graph with no
signed-base terminal state. The graph has 197 states for masks 4 and
59, and 369 for masks 12 and 51.

These assertions are fully enumerated in
`check_hilbert_odd_valuation_alignment.py` and its JSON. They involve 48
template/coset cases. The JSON records the entire periodic seed orbits
and the entire closed suffix graphs. Since a coordinate spread of at
least \(3c'\) requires \(N'\ge9+3j+2\), no finite tile terminates
before the two prescribed scale bits have been processed. The signed
terminal criterion from Section 4 covers all later finite sizes.
This proves the theorem.

The uniform certificate has passed an independent written and
computational review: the reader regenerated the transition table and
reproduced all 48 state-set orbits and closed suffix graphs. A subsequent
terminal extension permits every common outer orientation. The
independent reader checked all 2,264 saved uniform suffix states with
this broader terminal condition and again found none. The full 96-case
finite-prefix rerun also has no terminal; its separate independent
rerun with regenerated transitions reproduced every case and count.
Together with the preceding results, the unresolved portion of this
quadratic family is restricted to even \(t\ge4\) and
\(b\equiv1,3,7\pmod8\). This is still a restriction on one explicit
candidate obstruction family, not a proof of private-choice solvability.

## 8. The remaining even-valuation orientations

For even \(t=2j\ge4\), the same seed-set calculation is small even
though the complete rational prefixes can be large. Here
\(c'=2^{7+3j}b\). The first rank difference digit is odd, and the
remaining zero-scale length is \(6+3j\). Starting at \(j=2\) therefore
means applying \(U^{12}\), followed by the orbit under \(U^3\).

Only eight strong tournament masks survive this zero-scale stage:

\[
 \mathcal A=\{13,19,44,50\},\qquad
 \mathcal B=\{17,29,34,46\}.
\tag{17}
\]

The diagonal branch has \(b\equiv1\pmod8\). For every mask in
\(\mathcal B\), prescribing the first scale bits \((1,0,0)\) and
then allowing all subsequent bits gives a closed suffix graph without
a finite signed terminal. The graph sizes are 806 or 808. In the
antidiagonal branch, the same conclusion holds for
\(b\equiv7\pmod8\), whose first scale bits are \((1,1,1)\).
The coefficient spread for these masks is at least \(8c'\), so no
finite square terminates before these three bits have been read.

Thus only the antidiagonal branch with \(b\equiv3\pmod8\) remains
in class \(\mathcal B\). Class \(\mathcal A\) retains the three
residue possibilities \(1,3,7\pmod8\). The entire periodic seed and
closed suffix calculations are saved in
`check_hilbert_even_branch_reduction.py` and its JSON. They use the
broader common-parent terminal condition from the outset.

There are two exact symmetries within (17). Replacing each label index
\(u\) by \(3-u\) reverses the arithmetic progression and preserves
\(C,c,D^2\). Reflecting and swapping coordinates,

\[
 (i,j)\longmapsto(2^N-1-j,2^N-1-i),
\tag{18}
\]

while reversing every selected role also preserves (1), with the same
\(C\) and \(c\). Transformation (18) changes only the common outer
Hilbert orientation. It preserves the common-residue difference
\(y_0-x_0\), and hence preserves \(\theta\). These two operations
generate each of the classes in (17): it is enough to study masks 13
and 17, respectively. Negative progression steps are already allowed
in the prefix overgraph, so reversing their sign causes no loss.

This section's finite graphs and symmetry reduction have passed an
independent written and computational review. The reader regenerated
the transitions and reproduced all 48 cases, every suffix state, and
the symmetry table. The reduction does not assert that a surviving
branch contains a Pythagorean K4.

## 9. The valuation-four case

The exact quotient-prefix calculation also excludes \(t=4\) for
every odd factor \(b\). Here \(j=2\), \(\epsilon=0\), and

\[
 c'=2^{13}b,\qquad
 b(8C'+\theta)\equiv9D^2\pmod{2^{N'+3}}.
\tag{19}
\]

The diagonal branch has \(\theta=1\). The antidiagonal branch has
\(\theta\in\{7,3,-1,-5\}\). At quotient depth \(13+s\), the next
scale bit is bit \(s-1\) of

\[
 9D^2(8C'+\theta)^{-1}\pmod{2^s},
\tag{20}
\]

which is already determined by the preceding coordinate and rank
digits. This is the same delayed-bit argument as Section 3, with the
correct quotient intercept retained. The signed finite terminal test
permits every common outer orientation. Its full alignment modulus is
\(2^{N'+3}\), not \(2^{N'+1}\).

By Section 8, only the following seven cases require this calculation:

| Representative mask | \(\theta\) | Empty depth | Largest prefix set |
|---:|---:|---:|---:|
| 13 | 1 | 21 | 106864 |
| 13 | 7 | 21 | 338512 |
| 13 | 3 | 56 | 338512 |
| 13 | -1 | 80 | 491930 |
| 13 | -5 | 20 | 338512 |
| 17 | 3 | 39 | 338512 |
| 17 | -5 | 20 | 338512 |

Every case has zero finite signed terminal states and reaches an empty
prefix set. None reaches the 500,000-state or depth-120 safety cutoff.
The checker and results are
`check_hilbert_normalized_t4_alignment.py` and its JSON. As before,
terminal testing before prefix exhaustion excludes every finite square
size; this is not a search restricted to the displayed empty depths.

This extension has passed an independent written and computational
review. Regenerating the transition table reproduced all seven saved
case dictionaries, including the common-parent signed terminal tests,
the empty depths, and the maximum state count. The
remaining part of this quadratic family has even \(t\ge6\), with the
orientation and residue restrictions in Section 8. The original
private-choice solvability question remains open.

## 10. An eight-bit exclusion for the diagonal branch at valuation six

For \(t=6\), the diagonal quotient has \(j=3\),
\(c'=2^{16}b\), and

\[
 b(16C'+1)\equiv9D^2\pmod{2^{N'+4}}.
\tag{21}
\]

To determine the first eight bits of \(b\), it is enough to retain
\(C'\pmod{16}\) and \(D\pmod{256}\). Both registers have stopped
changing long before the first nonzero scale bit is read. Thus these
two finite registers can replace the exact growing prefixes for this
test.

For representative mask 13, start with the diagonal stabilizer cosets
and process all 16 zero-scale coordinate levels, requiring the first
rank difference digit to be odd. The resulting register state set has
384 elements. Group these
states by

\[
 b_8=9D^2(16C'+1)^{-1}\pmod{256}.
\tag{22}
\]

For each group, read the eight scale bits prescribed by \(b_8\).
Every group becomes empty. At each intermediate level, the broader
signed terminal test also has no accepting state. The coefficient
spread rules out any finite square before the first scale bit, and
every later finite alignment has a modulus larger than 256. Hence
the procedure excludes every finite diagonal realization at \(t=6\).

The state construction is the `seed` function in
`probe_diagonal_alignment_registers.py`; the complete certificate is
`check_hilbert_diagonal_t6_alignment.py` and its JSON. The JSON records
all 384 seed states and every subsequent grouped state set. Section 8's
symmetries cover the other masks in class \(\mathcal A\); class
\(\mathcal B\) was already excluded in the diagonal branch.

I checked this eight-bit certificate a second time with a separate
implementation; see
the review. The same
bounded-register approach does not yet extend uniformly: at larger
quotient parameters, projected suffixes can accept even after twelve
norm bits are imposed. Such acceptance is only a failure of this
overgraph exclusion, and is not an aligned Pythagorean certificate.
