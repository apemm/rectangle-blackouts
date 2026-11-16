# Hilbert rank congruences exclude the displayed quadratic cliques

15 November 2026. The arbitrary-order K4 and K5 obstructions do not
embed in the canonical Hilbert order, even after allowing their free
coordinate translations and 2-adic rescalings of the rank step. The K5
exclusion is an elementary rank-congruence argument. The K4 exclusion
uses the same invariant and a small exact carry calculation, specified
below as a finite transition table.

Other quadratic-potential K4 orientations remain open. In particular,
this note does not prove uniform three-choice solvability.

## 1. Odd valuations inside a local orientation orbit

Write H_k for the canonical Hilbert map on a square of side 2^k, and
R_k for its inverse rank. Let G consist of the identity, coordinate
swap, simultaneous coordinate reflection, and their product. These
are the four recursive orientation states of this Hilbert convention.

**Orbit lemma.** For any point p, two different ranks among
{R_k(gp):g in G} have an odd 2-adic valuation of their difference.

Induct on k. In the four top quadrants, the images gp have Hilbert
quadrant digits that are equal or differ by 2. Their lower coordinates
are G-images of one common lower point. If the lower rank difference
is nonzero, induction gives an odd valuation below 2k-2; adding a
multiple of 2*4^(k-1) leaves that valuation unchanged. If the lower
difference vanishes, the whole difference is zero or ±2*4^(k-1),
whose valuation is 2k-1. This proves the lemma.

Consequently, if two points of a larger canonical Hilbert square are
coordinatewise congruent modulo 2^k, then their rank difference is

\[
 \text{either divisible by }4^k,\quad
 \text{or has odd 2-adic valuation below }2k.
 \tag{1}
\]

Indeed, their local ranks modulo 4^k belong to the same orientation
orbit. This statement allows the points to lie in different dyadic
blocks with different recursive orientations.

## 2. The quadratic normalization, including even rank steps

Suppose protected ranks have the form R+d r_i, where d>0 and the r_i
are distinct integers. A common quadratic norm family has positive
integers c,B0 with B0 odd and

\[
                           8cB0=(SMd)^2.
 \tag{2}
\]

The directed cross-row heights are B0-2c(r_j-r_i)^2, and the norm
lengths are B0+2c(r_j-r_i)^2. Thus the horizontal leg SMd|r_j-r_i|
has exactly the required Pythagorean identity.

Write e=v2(SM) and t=v2(d). Then

\[
                         k:=v2(c)=2e+2t-3.
 \tag{3}
\]

This covers an odd common large factor B0 that is not a square.
It also covers the even-step repair of the initial parity objection:
increasing t increases the coordinate scale by the corresponding
factor 4^t. We do not assume d odd.

## 3. The displayed K5 family is impossible

The five-label potential family uses

\[
 r=(0,2,6,4,7),\quad
 u=(36,16,16,24,57),\quad v=(8,32,0,12,15).
 \tag{4}
\]

Allow arbitrary coordinate translations A,B, so its points are
(A+c u_i,B+c v_i). More generally, these are all solutions of its
connected bipartite potential equations, after the common cross-row
constant is absorbed into B-A.

All five points are coordinatewise congruent modulo 2^k. The rank
list has both a difference d and a difference 2d. One of their
valuations t,t+1 is even. For e>=2,

\[
                          t+1<2k.
 \tag{5}
\]

This contradicts(1). Thus the displayed K5 family cannot occupy its
prescribed ranks in a canonical Hilbert ordering, for any positive
step d, any translations, or any normalization (2) with 4|SM.

This includes the four-choice example, where4|S and M=4. The proof
uses no computational search.

## 4. The full free-potential family of the displayed K4

For rank multipliers0,1,2,3, direct the six pairs as

\[
       0\to1,\quad1\to2,\quad2\to0,\quad
       3\to0,\quad3\to1,\quad2\to3.
 \tag{6}
\]

Every solution of the corresponding quadratic potential equations
has the form

\[
 P_0=(A+6c,B),\quad P_1=(A+z,B+5c),\quad
 P_2=(A+4c,B+z-c),\quad P_3=(A+9c,B+3c),
 \tag{7}
\]

with A,B,z free integers. This includes the displayed example z=2c.
Modulo2^k, these four points have the pattern

\[
 (a,b),\quad (f,b),\quad(a,g),\quad(a,b),
                       \qquad f+b\equiv g+a\pmod {2^k}.
 \tag{8}
\]

For odd d, P_0 and P_3 already contradict checkerboard parity. To
handle even d as well, we need the following stronger local statement.

**Carry lemma.** Suppose four local coordinate residues have (8), and
their global Hilbert ranks form an arithmetic progression of step d.
If t=v2(d)<2k, then

\[
                         t\text{ is odd},\qquad t\ge2k-7.
 \tag{9}
\]

In particular, an AP can extend for at most four coordinate-bit levels
after the first nonzero base-four digit of its step. The finite proof
of this assertion is given in Section5.

Combining (3) and (9) excludes the family (7) whenever e>=3. First,
t>=2k would give3t<=6-4e, impossible. Otherwise t is odd and

\[
                      3t\le13-4e\le1,
 \tag{10}
\]

also impossible. Thus the entire free-potential K4 family (7), including
all even-step rescalings, is excluded for 8|SM. In particular this
covers the original S=32,M=3 private system.

## 5. The carry lemma as a finite exact calculation

The calculation has at most 4^4*3^3=6912 formal states, and only 120
states immediately after the first nonzero step digit. It is not a
board or height enumeration.

Label the orientation states 0,1,2,3 by identity, swap, simultaneous
reflection, and reflected swap. Given a lower orientation o and the
next physical coordinate bits(x,y), the parent orientation p and
Hilbert rank digit q are the following pairs(p,q):

| o | 00 | 01 | 10 | 11 |
|---|---|---|---|---|
| 0 | (1,0) | (0,1) | (3,3) | (0,2) |
| 1 | (0,0) | (2,3) | (1,1) | (1,2) |
| 2 | (2,2) | (1,3) | (2,1) | (3,0) |
| 3 | (3,2) | (3,1) | (0,3) | (2,0) |

This is the inverse of the standard quadrant recursion. If the parent
orientation is p, first apply p to the coordinate bits. Their quadrant
digit is 0,1,2,3 for 00,01,11,10 respectively. The lower orientation is
p composed with swap, identity, identity, or reflected swap, according
to that digit. This derives the table without an empirical Hilbert fit.

A state is (o0,o1,o2,o3,c0,c1,c2). The three carries enforce, in order,
the coordinate relation in(8) and the two AP equations
R0-2R1+R2=0, R1-2R2+R3=0. Starting from the least significant bits,
all carries are zero and the four orientations are arbitrary.

Choose bits a,b,f,g. Feed(a,b),(f,b),(a,g),(a,b) to the four orientation
rows, giving parent states p_i and rank digits q_i. The transition is
allowed exactly when

\[
 f+b-g-a+c0\equiv0\pmod2,
 \tag{11}
\]

\[
 q0-2q1+q2+c1\equiv0\pmod4,\qquad
 q1-2q2+q3+c2\equiv0\pmod4.
 \tag{12}
\]

The new state replaces each orientation by p_i and divides the three
left sides by 2,4,4 respectively. All carries stay in{-1,0,1}.
No final carry condition is imposed, because only congruences modulo
the local square size are needed. This enlarges the allowed set and
therefore is safe for exclusion.

As long as the AP step has zero digits, q1=q0. The closure of the
256 initial states under these transitions is exactly the same 256
states. At the first nonzero digit, q1-q0 modulo4 is always 2; an odd
digit never occurs. Let F_j be the states reachable after j further
bit levels, counting the first nonzero digit as level 1. Applying the
explicit transition rule gives

| j | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| number of states in F_j | 120 | 112 | 48 | 16 | 0 |

The companion certificate lists these finite state sets, rather than
only their counts, and the checker regenerates the table and all sets.
If the first nonzero step digit is at base-four place ell, then
t=2ell+1. At most four of the k bit levels can remain, so k-ell<=4,
which is exactly (9).

Thus the K4 result uses a finite exact transition calculation in
addition to the written arithmetic argument. It should not be described
as an entirely unaided hand proof.

## 6. What the argument does not exclude

For a quadratic-potential K4 with a source or sink and a directed
triangle on the other three indices, those three labels are
coordinatewise congruent modulo 2^k. Among any three AP indices from
{0,1,2,3}, differences of sizes d and2d occur. Equation (1) therefore
excludes these families by the same argument as Section3.

A transitive four-vertex orientation contains two sources pointing to
the same two targets. Its potential equations are inconsistent for
distinct rank multipliers: subtracting the four equations gives
2(r_i-r_j)(r_u-r_v)=0.

The remaining strong orientations have one isolated edge in their
bipartite potential graph. When its source and target are the two
middle AP indices, the modular pattern is(8), up to swapping the axes,
and the carry lemma applies. Other placements of that isolated edge
have surviving cycles in the analogous modular transition graph.
They are not excluded by this note. A surviving modular state is not
an actual Hilbert embedding; higher coordinate digits and the exact
quadratic offsets still have to be matched.

Accordingly, this removes the two displayed arbitrary-order templates
and several related families from the canonical Hilbert search. It
does not rule out every equal-choice clique, every other P constraint
configuration, or unsatisfiability without a clique.

## Files and review

[Finite carry checker](check_hilbert_quadratic_clique_exclusions.py)
and [complete state certificate](check_hilbert_quadratic_clique_exclusions.json).

The complete standalone note passed an independent written review. The
independent reader also reran the carry certificate and matched every saved
state and the counts 120,112,48,16,0. The orbit induction, K5 valuations,
free-potential pattern, and even-step normalization were checked separately.
