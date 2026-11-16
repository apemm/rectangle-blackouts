# Exact reachability of offset types

15 November 2026. This proves the reachability statement proposed in
`p_two_block_selfsimilar.md`. It does not prove that the four per-scale
systems are solvable. It shows exactly how a finite obstruction in any
fixed offset type would persist at larger scales.

The interval induction and persistence statement have been checked by
an independent reader.

Use the type \((s,k,o)\), where the block side is \(s\), its coordinate
offset is \(ks\), and \(o\) is either `id` or `swap`. Write \(\bar o\)
for the other class. The proved child rule in the source has a simple
unordered form:
\[
 (2s,k,o)\longmapsto
 (s,2k-1,o),\ (s,2k,o),\ (s,2k+1,o),\ (s,2k,\bar o).
\tag{1}
\]
The rank order of the middle children depends on the class, but their
set of types does not.

## Exact descendant sets

Fix a starting offset \(k_0\) and class \(o\). At depth \(\ell\), the
offsets occurring with class \(o\) are exactly
\[
 2^\ell k_0+[-(2^\ell-1),\ 2^\ell-1]\cap\mathbb Z.
\tag{2}
\]
For \(\ell\ge1\), the offsets with class \(\bar o\) are exactly
\[
 2^\ell k_0+[-(2^\ell-2),\ 2^\ell-2]\cap\mathbb Z.
\tag{3}
\]

At depth one these are the three offsets \(2k_0-1,2k_0,2k_0+1\)
and the single opposite-class offset \(2k_0\), so the claim holds.
For the induction, subtract the center \(2^\ell k_0\) and write
\(n=2^\ell\). The existing same-class offsets are
\([-n+1,n-1]\), and opposite-class offsets are \([-n+2,n-2]\).

The class-preserving children of the first interval cover every integer
in \([-2n+1,2n-1]\). Class-changing children of the other interval add
only points already there. For the opposite class, class-preserving
children cover \([-2n+3,2n-3]\), while the class-changing children of
the first interval supply the even offsets in \([-2n+2,2n-2]\).
Their union is exactly \([-2n+2,2n-2]\). This proves (2)--(3).

In particular, from \((-1,o)\), the depth-\(\ell\) same-class offsets
are every integer in
\[
 [-(2^{\ell+1}-1),-1],
\]
and the opposite-class offsets are every integer in
\[
 [-(2^{\ell+1}-2),-2].
\]
The positive-offset statement follows by changing signs.

## Persistence of an obstruction

Fix a block type \((s,k,o)\), with \(s\) a power of two and \(k\ne0\).
Choose \(\ell\ge0\) so that
\[
 |k|\le2^{\ell+1}-1.
\]
Then \((s,k,o)\) occurs as a descendant of
\[
 (2^\ell s,\operatorname{sign}(k),o).
\tag{4}
\]
Thus a first-off-diagonal block of sufficiently large side and the same
class contains the fixed type. All four combinations of sign and class
occur among the source's O2 and O4 blocks.

The descendant occupies a contiguous rank interval. Its internal rank
differences, coordinates up to diagonal translation, and type class
agree with the target system. Consequently its candidate constraints
are exactly those of the target type. A fixed integer or certified
unsatisfiable subsystem therefore obstructs the corresponding larger
first-off-diagonal block. The corner-cut decomposition then places an
unsatisfiable connected component inside one of the four per-scale
pieces.

This gives persistence at every larger ancestor depth, since the offset
ranges in (2) grow and retain \(k\). It does not turn candidate
unsatisfiability into a genuine in-strip rival obstruction: completion
rows and owner columns still require their own checks for that claim.

The consequence for the search is precise. The four per-scale systems
contain arbitrarily large realizations of every fixed signed offset
type. Their uniform solvability is not confined to the geometry of
offset \(\pm1\) blocks. A proof by induction must also accommodate the
interior types described by (2)--(3).
