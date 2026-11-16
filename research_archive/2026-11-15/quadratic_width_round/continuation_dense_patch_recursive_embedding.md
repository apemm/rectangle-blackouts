# Dense P patches embed after a small adjustment of the diagonal band

15 November 2026. The translated density obstruction can be embedded
in an actual full-size, unfiltered triangular recursive order.
Adjusting the removed band by \(O(\sqrt h)\) suffices. This gives
examples with unbounded genuine-P degeneracy and, for packed tiles,
unbounded degeneracy of the potential-type graph.

The conclusion concerns a family of admissible nearby band choices.
It does not say that every band choice has this property. It also
does not yet cover the nonlinear index compression caused by the
common square filters, or rule out adaptive tile permutations.

Independent review checked the four address identities, the ancestor
sizes, the band adjustment, the owner inclusion, and the packed-tile
interpretation. A sparse checker also verified 47864 point identities
for \(2\le n\le32\) and both parent sizes.

## 1. Every local orientation occurs nearby

Use the triangular recursion \(G_n\) from the hole-free ordering
note. Number its four children 0, 1, 2, 3 in their traversal order.
Their linear maps are respectively
\[
 \tau,\quad I,\quad-\tau,\quad I,
 \qquad \tau(u,v)=(v,u).
\]
All accumulated linear maps belong to
\(\mathcal G=\{I,\tau,-I,-\tau\}\).

For \(n\ge2\) and either parent size \(8n\) or \(8n-1\), the following
depth-three children have size exactly \(n\):

| Address | Linear map | Translation |
|---|---|---|
| 000 | \(\tau\) | \((0,0)\) |
| 001 | \(I\) | \((0,n)\) |
| 020 | \(-\tau\) | \((2n-1,2n-1)\) |
| 120 | \(-I\) | \((2n-1,6n-1)\) |

These identities follow by substituting the child sizes and maps.
They hold for both parent sizes because the relevant ceilings agree.
Multiplying the four maps by any parent orientation again gives
all of \(\mathcal G\). In particular every such parent contains
a side-\(n\) child with global identity orientation.

Now let \(N=2^k n\), \(k\ge3\). At depth \(k-3\), every
recursive node has size \(8n\) or \(8n-1\). Indeed a node of
size \(2m\) or \(2m-1\) has children of sizes \(m,m-1\).
For any point \(P\in T_N\), take its node at that depth and
then an identity-oriented child from the table. Its origin \((U,V)\)
satisfies
\[
 \max(|U-P_u|,|V-P_v|)<8n.
\tag{1}
\]
Both points belong to the same parent, whose triangular-norm
diameter is less than \(8n\). The child occupies a contiguous
rank interval and its local order is exactly \(G_n\).

## 2. Embedding a dense translated patch

Fix the stride \(S\), even row step \(D\), and residue bases
\(1\le a_0,b_0\le D\) of opposite parity. Let \(H\) be a
large auxiliary height. Choose \(n\) with
\(|T_n|\sim H/S\), as in
[the translated-patch theorem](continuation_translated_patch_density.md).
Choose the least dyadic multiple
\[
 N=2^k n\ge H/D,
\]
so \(N<2H/D\) for large \(H\).

Let a desired integer baseline band width \(c_*\) satisfy
\[
 \sqrt H=o(c_*),\qquad c_*=o(H).
\tag{2}
\]
The translated-patch theorem, applied to the fixed order \(G_n\),
provides a translation \(T\) with
\(\Omega_{S,D}(|T_n|\log H)\) genuine P edges. Put
\[
 P=\bigl(\lfloor H/(4D)\rfloor,\ T-c_*\bigr).
\]
For large \(H\), the bounds on \(T\) and (2) place this point
inside \(T_N\), a positive linear distance from its boundary.
Choose the identity child with origin \((U,V)\) supplied by (1),
and set
\[
 c=T-V.
\tag{3}
\]
Then
\[
 |c-c_*|<8n=O_{S,D}(\sqrt H),
\tag{4}
\]
so \(c>0\) and \(c=o(H)\).

Use the full upper label triangle
\[
 (i,j)=(u,c+u+v),\qquad (u,v)\in T_N,
\]
in order \(G_N\), at consecutive stride-\(S\) columns.
Inside the selected child, its labels are
\[
 i=U+u_r,\qquad
 j=c+U+V+u_r+v_r
   =U+T+u_r+v_r.
\]
This is exactly the dense translated patch, except for a common
row translation of size \(D(U-\lfloor H/(4D)\rfloor)=O(\sqrt H)\).
Its P vectors and edge count are unchanged. The original proof gives
linear margins from both strip boundaries, so the common corners
remain in the strip after this translation.

The full board height can be taken as
\[
 h=D(N+c)=\Theta(H),
 \qquad H\le h<2H+o(H).
\]
The counted slot gaps are \(\Theta(H)=\Theta(h)\). Every
owner belongs to the lower triangle \(i-j\ge c\): its index
difference is \((L+b_0-a_0)/D=\Theta(H)\), whereas \(c=o(H)\).
Retaining that lower run therefore makes all counted P-rivals
genuine in the full two-run label layout.

The dense patch has \(\Theta(h)\) vertices and
\(\Omega(h\log h)\) edges. Its induced graph has unbounded
degeneracy. Thus no uniform bounded-degeneracy theorem holds for
all these unfiltered triangular orders and nearby band choices.

Changing the band by (4) changes at most \(O(h^{3/2})\) labels.
This is the scale already permitted for the sparse exceptional
sets in the scaffold discussion. This observation is only a label
count; it does not independently prove a full relocation theorem.

## 3. Potential types in packed square tiles

The same construction applies to the graph of potential P types
for fixed \(k\times k\) physical packs. Replace the parameters
in Section 2 by
\[
 D'=kD,\qquad S'=k^2S.
\]
At every macrotile select the label with internal coordinates
\((0,0)\), and consider its possible placement in internal slot
zero. Its rows and columns follow exactly the translated-patch
model with parameters \(D',S'\).

The Euclidean scaling congruence from the density proof makes the
owner rows belong to these same \(D'\) residue classes. Hence
the owner is another internal-\((0,0)\) label in the lower macro
triangle. Both common corners are absent from every label of the
midpoint patch tile, because the odd and even physical row ranges
of the whole patch are separated by a linear amount.

Each counted macro edge therefore supplies a genuine potential
P type between two tiles. The potential-type graph contains a
\(\Theta(h)\)-vertex subgraph with \(\Omega(h\log h)\)
edges, so its unweighted and weighted degeneracies are unbounded.
This remains true for the type graph even if a later permutation
avoids the particular internal-slot-zero realization.

For \(k=4\), this rules out a uniform two-type peeling argument
over this entire unfiltered family. It does not refute a specially
chosen band, a simultaneous permutation rule that uses more than
peeling, or the filtered scaffold. Those are separate possibilities.
