# Fixed dyadic-period column clocks still admit long endpoint rivals

15 November 2026. Allowing unequal positive column increments does not
by itself remove the hierarchical endpoint obstruction. Every fixed
dyadic-period increment pattern has arbitrarily large affine profiles
on which all adjacent-corner hierarchical traversals force a long P
rival. Fillers at the unused columns cannot distinguish the two
rectangle presentations.

The profile depends on the fixed clock pattern. This is not a theorem
against adaptive aperiodic clocks, or against choosing a pattern from
an unrestricted height-dependent family.

## 1. Endpoint distance under a periodic clock

Let P be a power of two. Fix positive increments

    delta_0,...,delta_(P-1) in 4Z,

and put C=sum delta_j. Define the monotone clock by x_0=0 and
x_(r+1)-x_r=delta_(r mod P). Its mean increment C/P is fixed.

Take a power-of-two n with P dividing n^2. Every aligned side-n
Hilbert node starts at a rank R divisible by n^2, hence by P.
Its first and last ranks differ by n^2-1, so their horizontal
distance is

    X=(n^2/P)C-delta_(P-1).                               (1)

This is independent of R and of every spatial orientation choice.

Put v=v_2(delta_(P-1)). For all sufficiently large dyadic n,

    v_2((n^2/P)C)>v,
    v_2(X)=v.

Thus X=2^v g for an odd positive integer g, and v>=2 is fixed.
Set

    X0=2^v,    Y0=2^(2v-2)-1,    L0=2^(2v-2)+1.

Then X0^2+Y0^2=L0^2, so (X,Y0g,L0g) is an integral
Pythagorean triple. Both g and X are Theta_pattern(n^2).

## 2. A protected profile for this clock

Set h=8L0g. Choose A in {5L0g,5L0g+2} so A=3 modulo four,
and put B=A+Y0g. Use labels with rows

    a_i=A+4i,    b_j=B+4j,    0<=i,j<n.                    (2)

For large n, all odd rows lie above h/2 and all rows lie in [1,h].
The even rows have one fixed residue modulo four, either zero or two.

Any adjacent-corner entry/exit pair of this square has an odd endpoint
and an even endpoint with equal local row index c in {0,n-1}.
Their displacement has horizontal magnitude X and vertical magnitude
Y0g. The common vertical alternative rows are

    A-g+4c,    B+g+4c.                                    (3)

Both are strictly inside the strip. They have opposite parity and
belong to the same odd/even row-profile residues as the original labels.
Their owner is displaced in the local Cartesian row coordinates by

    K=(Y0+1)g/4:
    (i_owner,j_owner)=(K+c,-K+c).                         (4)

Since K is Theta(n^2), this owner is outside the protected square
and can be retained elsewhere in the complete profile.

If the owner's column differs from the common midpoint, its axis
rectangle and the endpoint tilted rectangle have black symmetric
difference and therefore equal presentations. If the owner happens
to occupy the midpoint, the tilted rectangle is hidden. Either case
is forbidden. Arbitrary additional filler points cannot repair it.

The smaller half-factor is g=Theta(h). The physical span X and
the protected labels' own gaps are also Theta(h). This is not a
small-factor or short-distance witness.

## 3. Genuine embedding and locality

The square can be embedded into the same padded genuine rectangle
as in the endpoint note. Let N be a power of two at least 64h,
take I=J=3N/8, and match the odd pool starting at h/2+3 and
the even pool of B's residue by integer raw offsets. Their sizes
are h/8 and h/4. For sufficiently large n the protected square
and both owners lie strictly inside those pools. The offsets lie
in the previously used interior range.

All aligned n-squares have starts divisible by n^2, so varying
the global hierarchical order still leaves (1) unchanged. The
padded width is O_pattern(N^2)=O_pattern(h^2).

If min delta_j>=128, the usual same-parity distance exclusion
also holds. A continuous hierarchical traversal satisfies
coordinate displacement squared less than 16 times rank distance.
Physical row step four then gives

    |Delta y|^2 <256|r-s| <=2|x_r-x_s|.

The protected P obstruction is therefore compatible with that
geometric invariant.

The constant minimum-increment assumption is needed only for this
last locality comparison. The endpoint norm obstruction itself uses
positive increments divisible by four.

## 4. Scope and exact checks

For each fixed dyadic-period clock, the construction gives infinitely
many heights and affine profiles with an unavoidable endpoint rival.
It does not put a single fixed profile against all possible patterns.
A height-dependent adaptive clock, a nonperiodic clock, or a traversal
without the protected adjacent-corner interval can escape this theorem.

The arithmetic row-filter and clean-cap translation argument from
the earlier endpoint note can be applied separately when its affine
row-map hypotheses hold. Survival through other small-factor erasures
remains unproved.

The checker uses the actual clock at both protected and owner ranks,
verifies all eight directed adjacent-corner patterns, and permits every
coloring of the common corners. Its saved run passes fifteen parameter
cases and 120 endpoint patterns.

Files:
[checker](check_periodic_column_clock_obstruction.py) and
[certificate](check_periodic_column_clock_obstruction.json).

Independent written review passed on 15 November 2026. A separate
import-based rerun, without rewriting the certificate, passed all fifteen
parameter cases and 120 endpoint patterns.

