# One-label collisions in a two-row sea, and what they force on holes

Research note, 10 November 2026. Hand proofs only. The bound m_0(h) = O(h^2) is not proved.

This note follows the audit
`../2026-11-09/full_problem_push/threshold_hand_proofs_audit_summary.md` of
`threshold_blocks_and_fillers.md`. I accept its four corrections:

* Theorem 3(a) excludes three-filler right angles only when the fourth corner is in the strip.
* The runs of a Theorem R layout are full only if 2^J = k_e, so occupancy matters and
  Corollary 2.1 is wrong as stated for h = 3 (mod 4).
* The Pell count gives an upper bound chi(G_T) <= C r(T) log(2 r(T)) and no lower bound.
* Section 5 of that note was wrong to list vertical rivals as the single open point. Mixed
  collisions with one label and repeated completions are separate conditions.

Section 1 classifies every collision that uses the cells of one label and fillers in rows 1
and h. Section 2 applies it to full occupation, section 3 to holes, section 4 to the
junction of two uniform regions, and section 5 lists the triangles that survive in a uniform
region. Section 6 states what is open.

Notation. h is odd, K = (h-1)/2. A label at column 0 has the odd cell O = (0, 2a+1) and an
even cell E. Put a* = K - a. Every other column considered holds exactly one black cell, in
row 1 or row h (a filler). v is the 2-adic valuation. A collision is a pair of distinct
rectangles with the same set of white corners.

## 1. Classification

**Theorem 4.** Let 0 < a < K. Consider collisions in which the black corners of the two
rectangles are fillers and cells of one label, with at least one label cell. They are
exactly the following.

(I-1) Positive integers u != v with u v = a^2, fillers at (v-u, 1), and fillers in one
common row r' in the columns -u and v. The white pair is W = (-u, a+1), Z = (v, a+1). The
rectangles are {O, (v-u,1), W, Z} and the axis rectangle {(-u,r'), (v,r'), W, Z}.

(I-h) The reflection: u v = a*^2, a filler at (v-u, h), fillers in one common row in the
columns -u and v, white pair in row K + a + 1.

(II-1) Integers g != 0 and D > 0 of the same parity with

    g^2 - D^2 = 4 a* (K + a),      g divides 2 a a*,      q = 2 a a* / g,

a filler at (g, 1), and fillers in the columns q + (g-D)/2 and q + (g+D)/2, one in row 1
and the other in row h. The white pair is W = (q, 2a+1+a*), Z = (g+q, 1+a*). The first
rectangle has the side from O to (g,1); the second has W Z as a diagonal.

(II-h) The reflection of (II-1), with a and a* exchanged.

(III) Singleton presentations: the triangle with vertex O and fillers (X_1, 1), (X_2, h),
X_1 X_2 = 4 a a*, completing at (X_1 + X_2, h + 1 - (2a+1)); and the triangle with vertex E
in row y and fillers (X_1, 1), (X_2, h), X_1 X_2 = (y-1)(h-y), both X_i odd.

No collision of two-white presentations uses the even cell E, and none uses both cells of
the label.

**Proof.** Three corners determine a rectangle, so the two rectangles share exactly their
white corners, and the white set has one or two cells. Two whites W, Z are either a diagonal
or a side of each rectangle. The black pairs available are (O, E), (label cell, filler),
(filler, filler). Write Q = (0, y) for a label cell and F = (g, r) for a filler, r in {1, h}.

*The pair (O, E).* It is vertical of odd length. As a side, the second rectangle would need
another column with two black cells, or a black pair whose rows sum to the odd number
y + y'; filler rows sum to 2, h+1 or 2h, all even. As a diagonal, a second antipodal black
pair again has odd row sum, and a black side parallel to W Z has odd vertical part, so its
fillers would be in rows differing by an odd number. None exists.

*Q and F a diagonal, the second black pair also a diagonal.* The second pair is antipodal
about the midpoint of Q F, so its rows sum to y + r. Two fillers give y + r in
{2, h+1, 2h}, which forces y in {1, h}. A label cell with a filler would put two fillers in
the column g.

*Q and F a diagonal, the second pair B, B' a side opposite W Z.* If B and B' are fillers in
one row, W Z is horizontal in row (y + r)/2, so y is odd, and with r = 1 the half-diagonal
l satisfies l^2 = (g/2)^2 + a^2. Put u = l - g/2, v = l + g/2. This is (I-1); r = h gives
(I-h). If B and B' are fillers in rows 1 and h, the vector Z - W has vertical part h - 1,
so the rows of W and Z are (y+r)/2 -+ K, which fit only if y + r = h + 1. If B is the other
label cell Q' = (0, y') and B' = (g', r') a filler, then
W = (Q + F - (B' - Q'))/2 has row (y + y' + r - r')/2, and y + y' is odd while r - r' is
even. So W is not a lattice point.

*Q and F a side, W = Q + t, Z = F + t.* A second black side parallel to Q F is a translate
of (Q, F) by a vector tau perpendicular to F - Q. Two fillers would be in rows differing by
|r - y| < h - 1. If the translate of F is Q', then tau = (-g, g^2/(r-y)) and the translate
of Q is a filler in row r_B with y' = r + r_B - y; r_B = r puts y' outside the strip, and
r_B != r gives y' = h + 1 - y, of the parity of y. If W Z is a diagonal of the second
rectangle with black pair B, B': using Q or F as B does not give a rectangle. Using Q'
fails by the parity computation of the previous case with the roles exchanged. Two fillers
in one row rho would put the rows of W and Z at rho -+ (y-r)/2, outside the strip. Two
fillers in rows 1 and h give 2 t_y = h + 1 - y - r, so y is odd; for r = 1,
t = (2 a a*/g, a*), the centre of W Z is in row K + 1, and the black diagonal has
horizontal part D with D^2 + (2K)^2 = g^2 + 4 a^2. This is (II-1); r = h gives (II-h).

*Singletons.* A triangle with one label cell and two fillers has its completion in the
strip only when the label cell is the vertex and the fillers are in rows 1 and h (Theorem 3,
proof of (a)). Two such triangles at one label with the same completion would have the same
product and the same sum of offsets, so the same two columns with rows exchanged. QED.

Checks against the audit. (I-1) with a = 3, u = 1, v = 9 is the height-seven certificate:
columns 175, 184, 185 around the label at 176. (II-1) with h = 38t+1, a = 17t, g = 17t,
D = t, q = 4t is the collision used in `period_eight_binary_sea_impossibility.md`. A small
case of (II-1): h = 15, a = 5, g = 10, D = 2, q = 2, fillers (10,1), (6,1), (8,15), whites
(2,13) and (12,3).

## 2. Full occupation

Let label columns be the multiples of s = 2^e, all occupied, and no label cell in rows 1
or h in the columns considered.

**Corollary 4.1 (uniform sea).** Let e be 2 or 3 and let every filler be in row 1. A label
with a odd is in no collision of Theorem 4. For e = 3 a label with v(a) = 1 is in one
(u = 1, v = a^2).

Proof. Only (I-1) needs no filler in row h. If a is odd, u and v are odd and
u v = 1 (mod 8), so v = u (mod 8) and the column v - u is a multiple of 8, a label column.
If v(a) = 1, the columns -1, a^2 - 1, a^2 are odd, odd and 4 modulo 8. QED.

So the restriction to a odd in a uniform region, which Corollary 3.2 needed for triangles,
is also exactly what two-white collisions need.

**Corollary 4.2 (the word 1,1,1,h,1,1,1).** At spacing 8 with fillers in row h at offset 4
and in row 1 otherwise, no label is in a collision of type (I-1) or (I-h).

Proof. Write alpha = v(u), beta = v(v), nu = v(a), so alpha + beta = 2 nu. The columns -u
and v must be fillers in one row, so alpha and beta are both in {0, 1} or both equal to 2.
That leaves (0,0), (1,1), (2,2). In each, u/2^alpha and v/2^alpha are odd with product an
odd square, so v - u is divisible by 2^(alpha+3) >= 8 and is a label column. The same
computation with a* gives (I-h). QED.

This explains the letter h at offset 4: it separates the columns -1 and a^2 when
a = 2 (mod 4). Type (II) is not excluded by this word, and at h = 38t+1 it is fatal for
every order, which is the theorem of the note cited above. A uniform region has no type
(II) and no type (III), because both need fillers in both rows.

## 3. Holes

Let a hole be a column that is a multiple of s and holds a filler instead of a label.

**Corollary 4.3 (hole law).** In a region whose other fillers are all in row 1, with e in
{2, 3} and a odd, a label at column X forbids:

* row 1 at every hole X + (v - u) with u v = a^2, u != v;
* row h at every hole X + (v - u) with u v = a*^2, u != v and v(u) = v(v) < e;
* row h at a hole X + (v - u) with u v = a*^2 when X - u and X + v are holes in one row.

Proof. The first is (I-1): the columns X - u and X + v are odd, hence in row 1. The second
and third are (I-h), with the columns X - u and X + v in row 1 in the second case. QED.

The first set has tau(a^2) - 1 elements and reaches a^2 - 1 columns. It is the hitting-set
family of `private_blocking_set_lower_bound.md`, now without the privacy assumption but
only for uniform regions.

Consequence for rigid layouts (heuristic count, not a theorem). In a Theorem R layout a
fraction of about 19/20 of the slots are holes. The expected number of labels that forbid
row 1 at a given hole is (label density per slot) times the mean of tau(a^2) - 1, which is
of order (log h)^2, and the same holds for row h through the second item. So for large h
almost every hole is forbidden both rows. A sparse rigid layout with holes in rows 1 and h
cannot work in a uniform sea, for the same arithmetic reason as the h^2 (log h)^2 lower
bound for private prescriptions. I do not see how a mixed sea would avoid this, because the
second sea row brings types (II) and (III).

What it selects. The blocker that costs nothing is a double: in a full run every column
X + (v - u) is a label column. So inside the reach a^2 of a label the slot lattice must be
fully occupied, or the sea must not be uniform there. The small boards are of the first
kind.

## 4. The junction of two uniform regions

Take h = 3 (mod 4), region 1 (a odd, fillers in row 1) on the left and region 2 (a even,
fillers in row h) on the right, on one slot lattice with no gap and no hole.

**Lemma 4.4.** No collision of type (I) uses a label of one region and fillers of either.

Proof. For a label at X in region 1 and type (I-1), the column X - u is left of X, so it is
in row 1 or off the board. If X + v is in region 2, it is in row h and the rows differ. If
X + v is in region 1, so is X + v - u, which is a multiple of 8 and a label column. For
type (I-h), X + v - u must be a filler in row h, so it and X + v are in region 2 and X - u
is in row 1. Region 2 is the reflection. QED.

So type (I) does not ask for a separation. Types (II) and (III) and the fatal triangles
A2, B2 of Theorem 3 do occur at the junction, for labels within about K^2 columns of it. A
separation zone filled with fillers consists of holes, and Corollary 4.3 applies to it: a
hole within reach of region 1 must avoid row 1 and, for labels with v(a*) < e, row h. I
have no junction that satisfies all of these. This is open.

## 5. Triangles that survive in a uniform region

Region 1, full occupation, a odd, fillers in row 1 at offsets not divisible by s. By
Theorem 3 no triangle with a filler is fatal. The surviving triangles with two label cells
and one filler are, with X_1 the filler offset and X_2 a multiple of s:

| Kind | Vertex | Label cells | Equation | Completion row |
|---|---|---|---|---|
| S1 | odd cell a | odd a, odd a' > a | X_1 X_2 = 4 a (a' - a) | 2(a' - a) + 1 |
| S2 | even cell b | even b, even b' > b | X_1 X_2 = 2 (2b+1)(b' - b) | 2(b' - b) + 1 |
| S3 | filler, offset 2 mod 4 | odd a_1, odd a_2 | X_1 X_2 = -4 a_1 a_2 | 2(a_1 + a_2) + 1 |
| S4 | filler, odd offset | even b_1, even b_2 | X_1 X_2 = -(2b_1+1)(2b_2+1) | 2(b_1 + b_2) + 3 |

In S3 and S4 both X_i are offsets of label cells from the filler. Every completion is in an
odd row of a filler column. The height-2051 example of the audit is two triangles of kind
S3 with the same pair (a_1, a_2) = (381, 385).

A pair of labels at slot gap G forms an S3 triangle exactly when G^2 - a_1 a_2 is a square
(for spacing 4; the filler is then determined), and an S4 triangle exactly when
(sG)^2 - 4(2b_1+1)(2b_2+1) is a square. So these triangles are a property of pairs, and the condition to meet is that their
completions are distinct. A heuristic count gives about log h of them per label in a random
order. Kinds S1 and S2 put their completions in low rows when the two indices are close; I
expect the measured sharing (0.17 to 0.29 shared cells per label at heights 23 to 47 in the
split layout) to come from there, and I have not checked it.

## 6. What is open after this note

Continued in `sea_mediated_collisions_and_junctions.md`, which treats the junction
(Theorem 6), spacing 4, and the two-label collisions through the sea.

The architecture that the one-label conditions allow for h = 3 (mod 4) is: two uniform
regions, each fully occupied on its slot lattice at spacing 4 or 8. What it still needs:

1. An order of the labels inside a fully occupied region with no tilted right angle among
   label cells and no vertical rival. Theorem R gives the first only with holes, and
   section 3 rules holes out. In a full region every three-label triangle completes in a
   label column, so every one is fatal or hidden. This is the main open point, and it is a
   pure question about one sequence of labels.
2. Distinct completions for the triangles S1 to S4.
3. A junction (section 4).
4. Two-label collisions with two white cells, which Theorem 4 does not cover.
5. Labels with a cell in row 1 or row h, excluded from Theorem 4.
6. Heights h = 1 (mod 4) and even heights.
