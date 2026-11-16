# A long P-rival survives every Hilbert orientation choice

15 November 2026. A protected square can force a long P-rival using
only its first and last labels. The argument is independent of every
recursive orientation inside or outside that square. It applies to
continuous Hilbert-type traversals that retain aligned squares as
contiguous rank intervals with adjacent-corner endpoints.

The witness has slot gap, own-row gap, and smaller half-factor all
proportional to the ambient height. It is not confined to the short P
family. Section 6 protects its endpoints from sparse row filters and
boundary-clean caps in the affine folded specialization. Survival under
the actual sampled row maps or other cleanup events remains separate.

## 1. The endpoint incidence fact

Let a square have local label coordinates (i,j), with
0<=i,j<n. Its four corners are

    (0,0), (n-1,0), (n-1,n-1), (0,n-1).

For any two adjacent corners u,v, at least one of

    u_first = v_second,    v_first = u_second             (1)

holds. The equal value is either zero or n-1. This follows by checking
the bottom, right, top, and left sides. Reversing the order of the
corners does not change the assertion.

Suppose label (i,j) has odd row A+4i and even row B+4j. If the first
and last labels of its traversal are adjacent corners, (1) supplies
an odd point at one endpoint and an even point at the other whose row
difference is exactly B-A. Their common local coordinate is
c in {0,n-1}.

## 2. A height-linear Pythagorean witness

Fix a power-of-two stride S>=128. Let n>=2 be a power of two and put

    q=n^2-1,
    Y0=S^2/4-1,    L0=S^2/4+1,
    h=8L0q,
    A=5L0q,        B=(5L0+Y0)q.                           (2)

Use the full label square with rows A+4i and B+4j. All its odd rows
are 3 modulo four and lie above h/2. All its even rows are 0 modulo
four and lie strictly inside the strip.

Let its consecutive lattice columns be S(R+r), 0<=r<n^2.
Regardless of the adjacent-corner endpoint choice, Section 1 gives
a black diagonal with displacement, up to its horizontal sign,

    (Sq,Y0q).

Since S^2+Y0^2=L0^2, its length is L0q. Its alternative vertical
diagonal has midpoint column S(R+q/2), and endpoint rows

    A-q+4c,    B+q+4c,    c in {0,n-1}.                    (3)

Both rows lie in [1,h]. They are respectively even 0 modulo four
and odd 3 modulo four, and the latter is above h/2. The midpoint
column is integral, since S is even, but is not a lattice column:
q is odd.

The required row-pair owner belongs to the same odd/even profile.
In local row indices it is displaced from the protected square by

    K=S^2 q/16:
    (i_owner,j_owner)=(K+c,-K+c).                         (4)

Its odd row is B+q+4c and its even row is A-q+4c. In a full profile
these two black points give the axis rectangle with the common
vertical pair (3). Its column differs from that pair's midpoint,
because every owner column lies on the S-lattice.

The tilted and axis rectangles are distinct, and their symmetric
difference consists of the two endpoint black points and the two
owner black points. Hence their presentations are identical regardless
of the colors assigned to the common corners. Filling one or both
common corners cannot repair this collision.

For fixed S and n tending to infinity,

    q=h/(8L0),    (L0q-Y0q)/2=q,    |B-A|=Y0q.            (5)

Thus the event's slot gap and smaller half-factor are both Theta(h).
Every protected label also has own-row gap Y0q+O(n)=Theta(h).
A cutoff that removes a witness only because one of these quantities
is h^(1-o(1)) but o(h) does not remove this particular witness.

That last statement concerns the witness's own parameters. A protected
label might still be removed because it participates in some other
small-factor event. No claim about that union of erasures is made.

## 3. Exact embedding into a padded genuine rectangle

The translated square is an actual aligned raw Hilbert square. It does
not require an arbitrary assignment of labels to unrelated ranks.

Take a padded side

    N=64 S^2 n^2,    I=J=3N/8.                            (6)

The global odd pool is h/2+3,h/2+7,... below h,
and the even pool is 4,8,...,h. Their respective sizes are

    n0=h/8=L0q,    n1=h/4=2L0q.

Define independent raw coordinate offsets by

    U0=I-(A-(h/2+3))/4,
    U1=J-(B-4)/4.                                       (7)

These are integers. Both lie in [2n1,N-3n1]. The square
[I,I+n-1] times [J,J+n-1] lies inside the genuine rectangle
[U0,U0+n0-1] times [U1,U1+n1-1]. Its physical rows are exactly
those in Section 2.

The two possible owner cells are

    (I+K+c,J-K+c),    c in {0,n-1}.                       (8)

They also lie in the genuine rectangle and outside the protected
square. In particular, the owner is present elsewhere in the same
complete profile for every global traversal order.

Every aligned side-n square is a contiguous n^2-rank interval in
the stated hierarchical traversal family. Adaptive choices above
that square can change R; adaptive choices inside it can change
the two adjacent endpoint corners. Neither change affects the proof.

The offsets in (7) are a deterministic affine-row example. They are
not asserted to be a surviving realization of the sampled multiscale
fields after all filters and cap replacements.

## 4. Uniform locality is compatible with the obstruction

The example does not rely on a failure of the same-parity distance
exclusion. Consider any nearest-neighbor hierarchical traversal that
visits every aligned dyadic square contiguously. For two ranks at
distance d>=1, choose the smallest dyadic L with L^2>d.
The rank interval meets at most two consecutive side-L blocks.
If it meets two, those squares share an edge, because the traversal
is continuous. Their coordinate diameter is less than 2L.
Since L^2<=4d,

    max_coordinate_difference^2 <16d.                   (9)

The same conclusion is immediate if the entire curve is one such
block. A physical row map with step four, or its 1-Lipschitz
clipped/folded extension, therefore satisfies

    |Delta y|^2 <256d <=2Sd =2|Delta x|.                 (10)

For S>=128, every nonhorizontal same-parity pair has nonintegral
Euclidean length. Equation (10) is uniform over all the hierarchical
orientation choices in the theorem.

A more general locality-preserving traversal that does not have
adjacent-corner endpoints in every aligned square is outside the
statement. Likewise a layout that splits the protected square,
restarts its ranks, reorders its labels by arbitrary permutations,
or replaces one of its endpoint labels can escape this argument.

## 5. Exact checks and scope

The sparse checker verifies the integer embedding, genuine-pool
membership, owner rows and ranks, the norm identity, both rectangles,
and all eight directed adjacent-corner patterns. For each pattern it
checks all four colorings of the two common corners. No large board
is enumerated.

Files:
[checker](check_hilbert_endpoint_p_obstruction.py) and
[certificate](check_hilbert_endpoint_p_obstruction.json).
The saved run passed 96 corner patterns and 384 common-corner colorings
over twelve parameter pairs.

This rules out an unconditional all-P repair theorem based only on
choosing continuous hierarchical orientations while retaining this
full affine label square and its owners. It does not rule out the
filtered mechanical scaffold, variable domain cuts, safe endpoint
relocation, or arbitrary variable-size permutations. Those additional
operations require their own analysis.

Independent review: the complete saved statement passed a separate
written review. The reviewer independently reran all twelve sparse
cases, checking 96 endpoint patterns and 384 common-corner colorings.
The genuine raw embedding and the sampling/cleanup limitations remain
as stated.

## 6. Protect the endpoints from sparse row filters and clean caps

There is a stronger existence statement for the affine folded-row
specialization. It still does not address the union of small-factor
source erasures.

Fix the height and q from (2). Translate the protected row bases by
A -> A+4t and B -> B+4t, with integer |t|<=floor(h/256).
The norm, slot gap, and half-factor remain unchanged. The protected
corners and the two owner raw cells in (8) remain fixed. The two raw
offsets in (7) both change by -t. All six cells remain in their genuine
pools, with a fixed positive height margin.

Assume each scalar folded/V extension is fixed before t is chosen,
has good constant plateaus, and has at most two nonconstant raw
preimages for each forbidden physical row. Let each parity's
deterministic forbidden set have size at most b, where
b log h=o(h).

For each of the four protected corner cells and two owner cells,
collect the boundary coordinate indices of EVERY CHILD of EVERY
dyadic ancestor containing that cell. There are O(log h) such indices.
For one fixed index c, being bad at offset U_alpha-t requires

    c-U_alpha+t in Z_alpha,

where Z_alpha is the bad raw-preimage set and |Z_alpha|<=2b.
Thus at most 2b translations fail that condition. In total only
O(b log h)=o(h) translations make any collected boundary value bad.

If all those values are good, no selected first-boundary-clean cap
can cover any protected or owner cell. Indeed a selected clean cap
must have a dirty immediate child: otherwise a smaller clean ancestor
would have been encountered first. Any cap containing the protected
cell is one of its ancestors, and every child of that ancestor was
tested. Maximality among first-clean caps does not change this
necessary dirty-child condition. Testing only the ancestors' own
boundaries would not suffice.

The residue-excluded offset rule can also be imposed. Take the common
dyadic modulus L to be the least power of two at least 16 max(1,b),
so L=O(b+1)=o(h). For each parity there are at most 4b prohibited
offset residues modulo L. Since both offsets change by -t, their
union prohibits at most 8b residues of t, at most half of the modulus.
A fixed interior t interval of length Theta(h) therefore contains
Theta(h) permitted translations. Removing the O(b log h) failures
still leaves a permitted translation.

This proves the existence of an affine folded layout in which all
endpoint witnesses and both owners avoid the literal sparse row
filters and every selected boundary-clean cap, uniformly over the
hierarchical orientation choices. The tested raw indices and the
spatial cap tree do not depend on those orientation choices.

The argument uses an affine central map at the protected cells.
Arbitrary bounded changes to occurrence lists can destroy the exact
norm identity, even though locality survives. No survival through
balanced planting or arbitrary multiscale row sampling is inferred
here. Nor does this argument show that the endpoint labels survive
deletion for OTHER small-factor P events.

This section passed a separate written review of the child-boundary
criterion, bad-preimage count, common-translation residue law, and
the affine-map qualifications.

## 7. A sparse planting extension for an affine half-word

The same obstruction can survive balanced planting when its underlying
word is the affine alternating word and the planting support is sparse.
This does not extend the obstruction to general sampled multiscale
fields.

Use row step D=8, a power-of-two S>=16384, and n>=4. Keep (2).
The protected rows are now A+8i and B+8j. Since q=7 modulo eight,
A=3 modulo eight and B=4 modulo eight. Use the class pools

    h/2+7, h/2+15, ... <h,    and    4,12,20,... <h.

These are one class of each alternating partition of the original
spacing-four pools. Their sizes are floor((h-(h/2+7))/8)+1 and h/8.
The offsets are defined by the same physical matching rule (7), now
dividing by eight. The owner displacement becomes

    K=(Y0+1)q/8=S^2q/32.

All norm and presentation calculations are unchanged. Replace 4c
by 8c in the common rows, and translate the row bases by 8t for
|t|<=floor(h/512). The genuine-pool margins remain positive.

Consider balanced planting by disjoint swaps supported on m(h)=o(h)
bounded-size intervals of the physical pool indices. Outside their
union, both the bit and its prefix count are unchanged. Therefore
the selected class's occurrence position at a fixed occurrence index
changes only at O(m(h)) indices. The same statement holds separately
for both parity classes.

Each protected corner and owner asks for only two occurrence positions.
As t varies, each requested occurrence index moves by exactly t.
Hence only O(m(h)) translations make any of these finitely many
positions differ from the affine reference word. All other translations
retain the exact norm identity and the true owner labels.

Perform the bad-preimage and child-boundary exclusions of Section 6
using the ACTUAL planted maps. They still have at most two nonconstant
preimages per bad physical row. At most O(b log h) translations fail.
The simultaneous residue law still leaves a positive proportion of t.
Thus, whenever

    m(h)=o(h),    b log h=o(h),

some translation preserves the endpoint collision through the sparse
planting, literal row filters, and selected boundary-clean caps.

A good anchor family of density zero, thinned and allocated by the
balanced planting construction, supplies m(h)=o(h). This is a sparsity
hypothesis, not an assertion about an arbitrary dense planting policy.
For the multiplicative good family, density zero also follows from
finite excluded-prime sieving and the divergent reciprocal sum of the
excluded primes.

After planting, each class gap is at most nine physical pool indices,
hence at most 36 in physical rows. The uniform raw Hilbert estimate (9)
then gives squared same-parity displacement less than 16*36^2*d.
The choice S>=16384 makes this less than 2Sd. Thus planting does not
sacrifice the same-parity distance exclusion.

A later fixed fine interpolation that retains the genuine labels at
their coarse anchor columns also retains this collision. Additional
singleton points can change only the colors of the common corners
or add unrelated black points; they cannot distinguish rectangles
whose symmetric difference already consists of black points.

The surviving limitation is substantial: this is an affine starting-word
branch with sparse planting. No positive-probability assertion for the
actual continuous field law is made. The selected endpoints may still
be erased because of other small-factor events. The statement rules
out a universal orientation-only repair for this admissible specialization,
not the full filtered probabilistic construction.

The checker additionally verifies six D=8 embeddings. Including the
earlier D=4 cases, it passes 144 endpoint patterns and 576 common-corner
colorings. The sparse-planting selection proof is analytic.



