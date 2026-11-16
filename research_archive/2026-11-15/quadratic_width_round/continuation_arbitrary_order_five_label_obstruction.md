# Five prescribed tile ranks can defeat four private choices

15 November 2026. The actual-order obstruction is not limited to a
three-choice palette. Five labels can force pairwise different choices
with four private positions per rank, while every alternative owner
remains inside the same Cartesian tile. As in the
[four-label example](continuation_arbitrary_order_four_label_obstruction.md),
this does not give a Hilbert-order embedding or a uniform locality claim.

Fix S divisible by four, M=4, and put

\[
 A=(SM/2)^2=4S^2,\quad c=A/2=2S^2,\qquad
 r=(0,2,6,4,7),
 \tag{1}
\]

\[
 u=(36,16,16,24,57),\qquad v=(8,32,0,12,15).
 \tag{2}
\]

Take s>57c and an odd d with7d<=s^2-1 and d>7SM/2. Set
T=(d^2-1)/2. The complete side-s tile has rows

\[
 a_i=2i+1,\qquad b_j=2(T+j)+2,
 \qquad0\le i,j<s,
 \tag{3}
\]

inside height h=d^2-1+2s. Put the five labels (c u_i,c v_i) at ranks
d r_i, and put all remaining labels at unused ranks in any order.
A choice xi in{0,1,2,3} puts a rank R at column S(4R+xi).

Orient the complete graph on the five indices by i->i+1 and i->i+2,
with indices modulo5. For every one of its ten edges i->j, direct
substitution gives

\[
                       v_j-u_i=-(r_j-r_i)^2.
 \tag{4}
\]

One way to find (2) is to note that both cyclic square sums are82:

\[
 \sum_i(r_{i+1}-r_i)^2
                  =\sum_i(r_{i+2}-r_i)^2=82.
 \tag{5}
\]

The bipartite graph of these ten equations is a ten-cycle; (5) is its
compatibility condition. Formula(2) is an explicit solution, so this
existence explanation is not needed for the verification.

If labels i,j have equal choices, their selected odd/even points have
horizontal magnitude X=SMd|r_j-r_i| and vertical difference

\[
 Y=d^2-A(r_j-r_i)^2>0,
 \qquad L=d^2+A(r_j-r_i)^2,
 \qquad X^2+Y^2=L^2.
 \tag{6}
\]

The smaller half-factor is A(r_j-r_i)^2. Its alternative pair is
owned by the label

\[
 (c u_i-c(r_j-r_i)^2,\ c v_j+c(r_j-r_i)^2)
                              =(c v_j,c u_i).
 \tag{7}
\]

Both coordinates are in[0,57c], so every owner lies in the tile.
The sets of u- and v-values in(2) are disjoint. Thus no owner equals
one of the five protected labels. Two edges share one owner, which
causes no difficulty because that label is retained in full.

Every equal-choice pair therefore gives an actual in-strip P collision:
the alternative rows are present in the strip, their midpoint column
is integral, and their complete owner is black. If the owner sits at
the midpoint the tilted rectangle is hidden; otherwise it has the same
presentation as the owner's axis rectangle. Arbitrary added fillers
cannot change this black symmetric difference.

Five labels cannot have pairwise different values from four choices.
Hence no private-choice assignment makes this prescribed order valid.
Choosing d to be the largest admissible odd integer gives

\[
                         T=(1/98+o(1))s^4.
 \tag{8}
\]

This is an obstruction to unrestricted all-order extension, not to
choosing another order or to the canonical four per-scale systems.
For power-of-two S, it also does not contradict the positive thin-block
theorem, whose original sufficient offset for M=4 is asymptotically2s^4.
The later palette-dependent improvement gives8s^4/9, still above(8).
The obstruction itself needs only4|S, as stated.

## Exact check and review

The checker verifies every one of the4^5 assignments, all four choices
of the owner of the first equal-choice edge, and all four colorings
of the common pair. It checks the ten coordinate identities, all owner
rows, exact norm identities, and the two presentations.

Files: [checker](check_arbitrary_order_five_label_obstruction.py) and
[results](check_arbitrary_order_five_label_obstruction.json).

The full note passed an independent written review. The review checked all
ten potential identities, the shared-owner case, positivity of every norm
height, and the asymptotic offset.
