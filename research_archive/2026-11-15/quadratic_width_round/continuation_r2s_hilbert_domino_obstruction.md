# An R2s support survives every aligned-domino permutation

15 November 2026. Retaining bad-row labels and permuting them within
fixed aligned pairs does not universally replace the R2s row deletion.
An infinite family of actual Hilbert placements has two aligned dominos
whose odd rows are fixed. Every swap preserves a same-sea-row mixed
collision between those rows.

The support uses two genuine doubles and two automatic sea points.
It uses no singleton hole or repeated filler row. Larger permutation
blocks and moving labels across block boundaries remain open.

## 1. An exact bad row and partner placement

For an even integer q>=2, put

\[
 y=q^3+q^2-1,\qquad U=q^2+2q+2.
\]

Use black points

\[
 A=(0,y),\quad B=(U,1),\quad
 C=(4q,y+4),\quad D=(U-4,1)
 \tag{1}
\]

and common points

\[
 P=(2q-2,y+2),\qquad Q=(q^2+4q,3).
 \tag{2}
\]

The identity `(q-1)U=y-1` makes `(2q-2,2)` perpendicular to `B-A`.
Thus `A,B,Q,P` is a rectangle. Also `C+D=P+Q` and
`|C-D|^2=|P-Q|^2`, so `C,P,D,Q` is a second rectangle.
In the usual R2s equations the parameters are

\[
 X=4q,\quad\delta=4,\quad T=4(q-1),\quad m=1-y,
 \quad V=U-4q-4.
\]

They satisfy `TU=-m delta` and `V^2-U^2=delta(2m-delta)`.
In particular, `delta^2=16<=2X`: the support respects the strong
same-parity norm gap.

For even q, both B and D have columns 2 modulo four. They are automatic
row-one sea points. P also has column 2 modulo four and is white. Q has
an arithmetic column but row three. If all selected odd core rows exceed
three, it too is white. The two rectangles therefore have identical
presentation `{P,Q}`, regardless of the other even points in the doubles.

## 2. Two rigid rows in the actual Hilbert recursion

Let `n=2^(2t+1)>=8` and `R=n^2/4+6`. In the ordinary identity-oriented
side-n Hilbert order,

\[
\begin{split}
 H_n(0)&=(0,0),&H_n(1)&=(0,1),\\
 H_n(R)&=(1,n/2+3),&H_n(R+1)&=(1,n/2+2).
\end{split}
 \tag{3}
\]

For the first pair, the initial descent applies an even number of swaps
before its side-two traversal. The second pair is in quadrant one. Its
even-depth local traversal starts with an identity-oriented side-four
block, whose ranks six and seven are `(1,3),(1,2)`.

Fix a stride S divisible by four and set `q=SR/4`. This q is even.
Give the local square odd rows `y+4i` and even rows `B_0+4j`, where
y is from Section 1, and put rank r at column Sr.

Both pairs in (3) are aligned dominos. Swapping rank zero with rank one
does not change the odd row at rank zero. Swapping R with R+1 does not
change the odd row at rank R. These two fixed points are precisely A
and C in (1). Every permutation within all aligned dominos therefore
retains the mixed support. No choice of the other even rows repairs it.

## 3. Full profile coverage and a global embedding

Set `h=2y-8`. The odd upper-half pool in residue three begins at y,
and the even pool in residue two is `2,6,...,h`. Take `B_0=y-1`.
For large n, every label of the protected side-n square belongs to the
Cartesian product of these two pools.

Choose `N=4n4^m` at least a sufficiently large fixed multiple of h.
The global Hilbert address `1,2,0,...,0`, with 2m zero digits, gives an
identity-oriented side-n block at

\[
                  (I,J)=(N/4,3N/4)
\]

with starting rank `3N^2/8`. The physical row offsets are

\[
                  U_0=I,\qquad U_1=J-(y-3)/4.
\]

The protected square lies in the genuine row rectangle. Every pair of
the complete Cartesian profile has exactly one double at its Hilbert
rank. At padding ranks, use a singleton from the coordinatewise clipped
row functions. Clipping supplies both virtual parity coordinates without
enlarging their displacement. The coarse arithmetic lattice is full.
The geometric progression of possible N permits `N=Theta(h)`, so its
width is `O_S(h^2)`.

All displayed sea and common columns fit inside this core for large
parameters. Their relative span is `O(q^2)=O(h^(2/3))`, whereas the
protected block starts a fixed fraction into the quadratic core.
Every displayed row is between one and h.

## 4. Geometry and occupancy are compatible with the obstruction

The Hilbert coordinate estimate is
`|Delta coordinate|^2<16|Delta rank|`. Clipping does not enlarge it.
Aligned-domino permutations change old rank separation by at most two,
hence by a factor at most three between distinct new ranks. With row
step four this gives

\[
                   |\Delta row|^2<768|\Delta rank|.
\]

For a fixed sufficiently large S, the usual coarse same-parity
nonintegral-distance bound is preserved. If full spacing-four occupancy
is wanted, choose S beforehand large enough for the existing
[bounded-permutation interpolation](continuation_permuted_step_four_interpolation.md).
For example, its row-index constants `C_0=4`, `k=2`, `D=7` give
`G=56`, `M=1568`, and the coarse physical stride `S=4M=6272`.
Any fixed positive integer multiple of this M also works with the same G.
In this experiment no row is declared unavailable: both interpolated
parity values are allowed. Its geometric mesh then supplies an occupied
fine core without changing the genuine doubles. The number of doubles
and the complete Cartesian label list remain unchanged.

The interpolation cannot change A or C, and row-one sea outside `4Z`
cannot change B or D. P remains white at an ordinary sea column. Q
remains white because its row is three and every odd virtual row is at
least y. Thus filling intermediate columns cannot repair this support.

This is not a proof that every bad-row label must collide. The collision
uses a particular partner row and placement. It shows that fixed aligned
domino permutations need not alter that placement, even in the genuine
Hilbert order. Moving the protected labels between larger blocks is not
covered by this result.

Independent written review passed the R2s algebra, sparse Hilbert
identities, complete profile counts, global address and offsets,
interior strip and column margins, clipping, and interpolation scope.
The reviewer also independently imported the checker without rewriting
its output and verified all 15 cases, 60 swaps, and 240 colorings.

The standalone [exact checker](check_r2s_hilbert_domino_obstruction.py)
and its [saved results](check_r2s_hilbert_domino_obstruction.json) verify
15 combinations of `n=8,32,128,512,2048` and
`S=6272,12544,25088`. All 60 protected pair-swap choices and 240
common-corner colorings pass. It checks the global rank/point identities,
complete profile bounds, both rectangles, and the strip and sea conditions.
It does not enumerate the full board or certify that other supports are absent.
