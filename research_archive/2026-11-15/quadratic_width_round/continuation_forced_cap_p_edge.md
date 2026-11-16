# Two bad rows can force an actual P edge after the cap repair

15 November 2026. The total virtual cap palettes can contain a direct edge
from an intrinsically forced odd singleton to an intrinsically forced even
singleton. Two bad rows suffice. The unique first-good cap in the example
does not cover either endpoint.

Thus sparse intrinsic force sets and the cap geometry do not, by themselves,
prove the directed-path condition in
[`continuation_virtual_cap_palettes.md`](continuation_virtual_cap_palettes.md).
The example uses arbitrary bad rows and specified admissible offsets. It
does not show failure for the actual R2s row sets, for every choice of
offsets, or after local block permutations.

## 1. The padded square and the two bad rows

Take height \(h=65536\), with row classes
\(2i+1,2j+2\) for \(0\le i,j<32768\). Use the padded Hilbert
square of side \(N=131072\), and offsets
\[
 (U_0,U_1)=(15840,17120).
\]
These satisfy the cap construction's offset condition
\(1\le U_\alpha\le N-32768-1\). Remove only odd-row index
\(16976\) and even-row index \(15695\). Their physical rows are
\(33953\) and \(31392\). All boundary rows are good.

Clipping therefore has exactly one doubly bad rank: the raw coordinate
\[
 (32816,32815),\qquad r_{\rm bad}=2147486549.
\]
The leaf is bad-cap. Its four-rank parent is
\[
 [2147486548,2147486551].                                 \tag{1}
\]
Its Hilbert entry and exit are \((32817,32815)\) and
\((32817,32814)\). Their common odd index after translation is
\(16977\), which is good. Hence (1) is the first good ancestor,
and it is the entire selected cap family. Its area is four.

## 2. The two forced endpoints remain outside the cap

An identity-oriented side-32 block has start
\(r_0=2147485696\) and origin \((32800,32800)\). The following
data use its local ranks 192 and 597.

| Object | Global rank | Raw cell | Original physical rows | Good palette |
|---|---:|---|---|---|
| Source | 2147485888 | (32807, 32815) | (33935, 31392) | odd 33935 only |
| Target | 2147486293 | (32816, 32831) | (33953, 31424) | even 31424 only |

Both ranks lie outside (1), so the virtual cap functions do not change
their values. The source is intrinsically forced to choose odd, and the
target is intrinsically forced to choose even. This conclusion does not
depend on the choices at any other singleton.

## 3. The P edge has a retained in-strip owner

Put every arithmetic slot at horizontal coordinate \(96r\). The two
forced points have
\[
 X=96(597-192)=38880,\qquad Y=2511,\qquad L=38961,
\]
and
\[
 38880^2+2511^2=38961^2.                                  \tag{2}
\]
Their alternate vertical corners have rows
\[
 \frac{33935+31424-38961}{2}=13199,
 \qquad
 \frac{33935+31424+38961}{2}=52160.                         \tag{3}
\]
Both are strictly inside the strip. The corresponding row-pair owner has
indices \((6599,26079)\), raw coordinates \((22439,43199)\), and
rank \(3721733056\). It is a genuine good label outside the selected
cap, so the cap construction retains its double.

Let \(A,B\) be the two forced black points, \(P,Q\) the common
vertical corners in (3), and \(U,V\) the two owner points. Then
\(APBQ\) is a tilted rectangle and \(UPQV\) is an axis-aligned
rectangle. Their entire symmetric difference \(\{A,B,U,V\}\)
is black. Therefore they have the same white part, irrespective of the
occupancy of \(P,Q\). In particular, row-1 sea fillers leave both
common corners white, since the midpoint column is halfway between two
arithmetic slots.

The singleton implication is a direct forced-one to forced-zero edge.
Moving or removing the owner double is outside the fixed-owner test. If
the same owner pair is relocated to another column, it still supplies an
axis rival unless that column is the common midpoint.

## 4. Verification and scope

[`check_forced_cap_p_edge.py`](check_forced_cap_p_edge.py) uses sparse exact
Hilbert rank and coordinate queries. It checks the unique doubly bad rank,
first-good ancestor, both forced palettes, the norm identity, in-strip
corners, retained owner, and both rectangle equations. It also checks all
four possible common-corner occupancy patterns. Its saved result is
[`check_forced_cap_p_edge.json`](check_forced_cap_p_edge.json).

No large state enumeration is used. The arbitrary two-row bad set is the
essential limitation. This example rules out a universal cap-palette
solvability claim based only on the number of bad rows. It does not rule
out an offset-selection theorem using the arithmetic of the actual row
filters, an augmented palette, or a simultaneous permutation repair.

Independent review checked the complete written argument and reran the
sparse certificate. The unique cap, forced endpoints, norm identity,
retained owner, and all four common-corner occupancy cases passed.
