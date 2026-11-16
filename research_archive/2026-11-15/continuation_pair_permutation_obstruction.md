# Consecutive pair permutations leave an immutable P-rival

15 November 2026. Permuting labels inside consecutive rank blocks keeps
every arithmetic slot occupied. For blocks of two labels, however, an
actual P-rival survives every choice of permutations. In particular,
the full-grid proposal fails at stride \(S=128\), despite retaining the
same-parity distance exclusion.

The primary construction uses a power-of-two stride and explicit ranks.
Section 3 gives a small-block version for every stride divisible by
eight. Section 4 embeds the same obstruction in a bulk residue block
of the H7 profile. No earlier excursion or four-system decomposition
is assumed to survive this change of layout.

An independent reader checked the primary construction and the extension
to every \(8\mid S\), including the owner and filler claims. They also
ran the sparse checker at eleven strides, verifying all 88 relevant
swap assignments, and checked the four primary ranks at \(S=128\)
separately.

The H7 extension received a separate final review of both orientations,
the same-block owners, and both bulk margins. The generalized checker
was independently rerun on its nine ordinary cases and two H7 cases;
all 88 swap assignments passed.

## 1. Constraint formulation and retained locality

Divide the original Hilbert ranks into blocks of \(b\) consecutive
ranks. Independently permute the \(b\) labels inside each block. Physical
slots remain all integers \(n\), with column \(Sn\). Each slot receives
one label and both of its black points.

If slots \(n,m\) receive original ranks \(r,s\), then
\[
 |r-s|\le|n-m|+2(b-1)\le(2b-1)|n-m|.
\]
Hilbert locality therefore bounds the squared same-parity row difference
by \(64(2b-1)|n-m|\). Consequently
\[
 S\ge32(2b-1)
\tag{1}
\]
retains the nonhorizontal same-parity integral-distance exclusion.
For \(b=2\), stride 96 suffices, and 128 is a convenient power of two.

For candidate P exclusion, each block is a variable with \(b!\) states.
A pair of physical slots and a choice of opposite-parity points gives
a forbidden pair of block states when their squared distance is an
integer square. This is a binary finite-domain constraint system;
constraints within one block are unary. With \(b=2\), the variables
are bits and this candidate system is exactly a 2-SAT instance.
Adding the condition that the vertical completion stays in the strip
preserves this formulation. Tests involving the owner label can depend
on another block, so they are not silently included in this 2-SAT claim.

## 2. Explicit obstruction at every power-of-two stride

Let \(S=2^e\), \(e\ge2\), and put
\[
 q=S^2,\qquad h=2q,\qquad R=q^2/4.
\]
Use the complete \(q\)-square of parity labels. The four Hilbert values
\[
\begin{array}{c|c}
R+2&(1,q/2+1)\\
R+3&(1,q/2)\\
R+4&(2,q/2)\\
R+5&(3,q/2)
\end{array}
\tag{2}
\]
follow directly from the recursion. The second quadrant is an unrotated
\(q/2\)-square translated by \((0,q/2)\). Since \(q/2\) has an odd
binary exponent, its first eight points agree with the first eight
points of \(H_8\), giving (2).

The first two rows of (2) form one permitted permutation block. Their
first coordinate is the same, so both physical columns always contain
the odd black row 3. The last two form another permitted block. Their
second coordinate is the same, so both physical columns always contain
the even black row \(q+2\).

Thus the points
\[
 C=(S(R+2),3),\qquad D=(S(R+4),q+2)
\]
are black under every collection of pair swaps. Their distance is
\(q+1\), since
\[
 (2S)^2+(q-1)^2=(q+1)^2.
\]
The vertical diagonal with the same midpoint has endpoints
\[
 P=(S(R+3),2),\qquad Q=(S(R+3),q+3).
\tag{3}
\]
These points lie in the strip. They are both white in the label-only
layout under either swap of the first permutation block: its odd row
is 3 and its possible even rows are \(q+2,q+4\).

The owner of the row pair in (3) is label
\[
 (i,j)=(q/2+1,0).
\]
It belongs to neither displayed permutation block. Its two possible
columns therefore both differ from the midpoint column in (3).
At whichever column the owner occupies, its two black points and
\(P,Q\) form a nondegenerate axis rectangle. The points \(C,P,D,Q\)
form a tilted rectangle with the same presentation \(\{P,Q\}\).

This collision is independent of every pair swap, including the swap
of the owner's block. Adding black filler cells also cannot distinguish
the two rectangles: their symmetric difference consists entirely of
the four fixed black points \(C,D\) and the owner's two points.

For \(S=128\), this gives height \(h=32768\). Equation (1) holds, so
the counterexample does not arise from losing the same-parity exclusion.
Unrotated third-quadrant embeddings preserve the permutation blocks and
give the same obstruction at every height \(32768\cdot2^k\).

## 3. The same obstruction for every \(8\mid S\)

Let \(8\mid S\), put \(D_0=S^2/16\), and choose a power of two
\(Q_0>D_0+1\). In the macro Hilbert square of side \(Q_0\), the cells
\((0,D_0)\) and \((1,D_0+1)\) are opposite diagonal corners of one
aligned square of side two, since \(D_0\) is even. Their terminal
orientation classes are opposite: one is in \(\{1,\alpha\}\), and
the other is in \(\{\tau,\rho\}\). This follows because the two
local corner orientations differ by the coordinate swap \(\tau\).

Choose the macro-cell of class \(\{1,\alpha\}\), where
\(\alpha(x,y)=(7-y,7-x)\) on a square of side eight, and refine it
to a Hilbert block of side eight. Its physical origin \((I,J)\)
satisfies
\[
 J-I=8D_0=S^2/2.
\]
Its rank start \(B\) is divisible by 64. Thus its local pairs
\(\{2,3\}\) and \(\{4,5\}\) are full permitted permutation blocks.

If its orientation is the identity, local ranks 2 and 3 have coordinates
\((1,1),(1,0)\), and local ranks 4 and 5 have coordinates
\((2,0),(3,0)\). The invariant points at slots \(B+2,B+4\) have rows
\(2I+3,2J+2\). Their row gap is \(S^2-1\), and the two common
corners at slot \(B+3\) have rows \(2I+2,2J+3\). Their owner is
\((J+1,I)\), outside both permutation blocks.

If the orientation is \(\alpha\), the first pair has coordinates
\((6,6),(7,6)\), and the second has coordinates
\((7,5),(7,4)\). The invariant rows at slots \(B+2,B+4\) are now
\(2J+14,2I+15\), again with absolute gap \(S^2-1\).
The common corners have rows \(2I+14,2J+15\), and their owner is
\((J+7,I+6)\), again outside both blocks.

In both cases the horizontal gap is \(2S\), the hypotenuse is
\(S^2+1\), both common corners are white under all swaps, and all
rows lie in the complete strip of height \(16Q_0\). Thus every stride
\(S=32\sigma\), including the minimal safe stride 96, has an immutable
pair-permutation P-rival.

## 4. Extension to an H7 residue block, away from the boundary

Consider the H7 residue block with row step \(D=28\) and row bases
\(a_0=1,b_0=28\). Label \((i,j)\) has black rows
\[
 1+28i,\qquad 28+28j.
\]
Use stride \(S=6272\sigma=8D^2\sigma\), where \(\sigma\ge4\) is
a power of two. This is within the stride range that retains the
same-parity exclusion under consecutive pair swaps.

Put \(D_0=S^2/(8D)=S^2/224\), which is an even integer, and choose
an even integer \(K\ge450\). The macro-cells
\[
 (K,D_0+K),\qquad (K+1,D_0+K+1)
\]
are diagonal corners of one aligned two-square. As in Section 3,
one has orientation class \(\{1,\alpha\}\). Choose that cell
\((a,D_0+a)\), refine it to a side-eight block, and write
\[
 I=8a,\quad J=8(D_0+a),\quad B=64r,
\]
where \(r\) is its macro rank. Now
\[
 J-I=S^2/D.
\tag{4}
\]
The two protected permutation blocks are again local ranks
\(\{2,3\}\) and \(\{4,5\}\).

In the identity orientation, their invariant rows at slots \(B+2\)
and \(B+4\) are
\[
 1+D(I+1),\qquad D(J+1).
\]
Equation (4) makes the absolute row gap \(S^2-1\). The common
corners at slot \(B+3\) have rows \(D(I+1)\) and
\(1+D(J+1)\); their owner is \((J+1,I)\), in the same residue
block.

In the \(\alpha\) orientation, the invariant rows are
\[
 D(J+7),\qquad 1+D(I+7).
\]
Their absolute gap is again \(S^2-1\). The common rows are
\(D(I+7)\) and \(1+D(J+7)\), with owner \((J+7,I+6)\).
Thus the same length identity
\[
 (2S)^2+(S^2-1)^2=(S^2+1)^2
\]
gives a genuine vertical P-rival under all pair swaps. The common
points are white in the label layout: the midpoint is in the first
protected domino, and neither of its two possible labels has either
common row.

This configuration can be placed entirely in the bulk. Choose a
power of two
\[
 Q_0>D_0+K+\left\lceil\frac{100000}{8D}\right\rceil+4
\]
and take Hilbert side \(n=8Q_0\) and height \(h=Dn=224Q_0\).
Every row of each of the four protected labels and of the owner is
strictly between \(100000\) and \(h-100000\). Indeed all relevant
indices lie between \(8K\) and \(8(D_0+K+1)+7\), and these two
inequalities give the claimed margins. The common rows satisfy the
same margins. Therefore a deletion based only on that boundary
margin does not remove these labels.

The precise obstruction is conditional on retaining the two protected
dominoes at their original consecutive arithmetic slots and retaining
the owner label elsewhere in the final board. The owner need not lie
in the same occupied interval. It cannot occupy the midpoint, which
already belongs to one of the protected dominoes. Additional labels
and black fillers cannot repair the collision, because the symmetric
difference of the two rectangles is already black.

This rules out pair swaps as a universal repair of a full padded H7
residue block. It does not claim that an arbitrary scheme of interval
cuts and restarted ranks preserves these protected adjacencies.

## 5. Verification and scope

[check_pair_permutation_obstruction.py](check_pair_permutation_obstruction.py)
uses sparse forward and inverse Hilbert routines. It checks the block
orientations and coordinates, then all eight choices of swaps in the
two endpoint blocks and the owner's block. For each choice it checks
both rectangles and their actual presentations. The H7 cases use
\(\sigma=4,8\), \(K=450\), and explicitly check the 100000-row
margin for every protected label and the owner.

The obstruction settles blocks of two labels in this full-grid layout.
It does not settle permutations of larger blocks. In particular a full
\(2\times2\) Hilbert block does not retain a single fixed odd or even
row at every one of its slots, so the invariant-point argument does not
transfer automatically to \(b=4\).
