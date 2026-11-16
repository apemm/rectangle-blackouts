# Dirty-cap path bounds through a slowly growing length

15 November 2026. The dirty-witness path proof is uniform through

`k(h)=floor(sqrt(log log h))`                          (1)

for sufficiently large h. Summing every length from one to k(h) still
gives

`b h^(1+o(1)) (h/E)^2`.                               (2)

The anchor-free subfamily has the stronger bound b h^(1+o(1)). This
goes beyond a separate statement for each fixed length, but still does
not control an arbitrarily long reachability closure.

## 1. A uniform bookkeeping bound

Use the deterministic cap/corner menus, two-arm product kernel and
artificial-anchor extension from
[the dirty-witness path theorem](continuation_dirty_witness_path_kernel.md).
Let

`D_h=max_(1<=n<=h) tau(n^2)`.

For a k-edge path in one core, a safe explicit upper form for the proof
is

`E N_k <= b h (h/E)^a
          exp[C k^2 log(k+2)]
          [C log(2h)]^(C k^2) [C D_h]^k`,             (3)

where a in {0,1,2} is the number of parity anchors used. The constant C
depends on the fixed profile and provenance parameters, but not on k
or h. The same bound with a=2 covers the full menu when E<=h.

Here are the uniform sources of these factors.

* The k-row strip proof uses independent variables in disjoint target
  intervals. It costs a factor at most C^k log^(O(k))(2h), including
  arm splits and bounded target errors.
* The coordinate orders, dyadic bins, potential ancestor/corner forms,
  and dirty-witness menus cost at most
  exp[O(k log(k+2))] log^(O(k))(2h).
* A coordinate threshold block has row diameter at most Ckt. A simple
  circulation has at most k terms, so its height error is at most
  Ck^2t. There are at most k-1 independent circulation constraints.
* The integer linear map formed from those circulation rows and one
  distinguished height has nonzero integer determinant, of absolute
  value at least one. Map disjoint unit cubes around integer height
  tuples into its target box. Each row changes by at most k on a unit
  cube. Enlarging the target sides therefore costs at most
  `(Ck^2)^k`, giving height volume at most `(Ck^2)^k hK`.
* The physical tuple tree has k vertices and one dirty witness; its
  bounded-gap interval choices contribute at most C^(k+1). Its extra
  witness width cancels the extra gap-product denominator exactly.
* Factoring each fixed height to recover its signed horizontal leg
  costs at most C D_h. There are k such legs. The first physical
  column has O(h^2) choices, independent of k.

The coordinate-birth product K cancels the mixed probability denominator
as in the fixed-length proof. Dyadic rounding changes at most k-1 birth
scales by a fixed factor. The displayed, deliberately generous factor
in (3) dominates all these costs.

The artificial-anchor loss is at most (h/E)^2, not a factor per vertex.
Repeated anchor occurrences use the same sampled anchor and the same
artificial index in that parity.

## 2. An elementary uniform divisor bound

Write H=log h and split prime factors of n<=h at x=sqrt(H). For each
prime exponent e, its contribution to tau(n^2) is 2e+1.

There are at most x small primes, and each exponent is at most H/log2.
Their total logarithmic contribution is at most

`O(sqrt(H) log(H+2))`.

For p>x, the sum of their exponents is at most
`H/log x=2H/log H`. Since 2e+1<=3^e for e>=1, their contribution to
log tau(n^2) is at most `2(log3) H/log H`. Thus uniformly in n<=h,

`log D_h <= C log h/log log h`.                       (4)

No prime-counting theorem is needed for this upper bound.

## 3. Substitute the growing length

For k<=k(h), equations (1) and (4) give

`k log D_h = O(log h/sqrt(log log h)) = o(log h)`.

The logarithms of the other factors in (3) are at most
O((log log h)^2), also o(log h). There are only k(h) lengths to sum.
Therefore (2) holds uniformly and simultaneously for every path length
at most k(h). Restricting to paths without anchor rows removes the
factor (h/E)^2.

For b=h^(5/6+o(1)) and E=h^(17/18), (2) is

`h^(35/18+o(1))`.                                    (5)

The initial top-window relocation has the same exponent. The
anchor-free path incidence is h^(11/6+o(1)).

If a path contains a retained genuine double, both of that object's
rows are at least 2E-O(1) below the top strip boundary. An anchor is
within E+O(1) of that boundary. A k-edge actual P path has rank span
O(kh). Same-parity locality would require

`E-O(1) <= C sqrt(kh)`

if it contained an anchor of either parity. Thus every such path of
length k=o(E^2/h) is anchor-free. In particular this applies throughout
(1), and also at the compatible E=h^(11/12) choice. The reflected
lower-anchor case is identical.

## 4. What growing length does not prove

A path longer than k(h) can leave the cap neighborhood after its initial
segment. The present bound does not charge that entire tail to the
finite prefix. Nor does it show that erasing one of the counted points
is compatible with keeping its column occupied.

Consequently this theorem provides a growing finite reachability test
and a simultaneous incidence budget. It is not a bound for every
reachable vertex, a solution of the singleton implication system, or
an occupancy-preserving repair. Paths crossing distinct core profiles
also require their stated interface analysis.

Independent review: the complete written proof passed an independent
review of the uniform factor accounting, integer lattice-volume bound,
elementary divisor estimate, once-per-parity anchor losses, simultaneous
length sum, and retained-genuine anchor exclusion. The distinction from
full reachability closure remains explicit.
