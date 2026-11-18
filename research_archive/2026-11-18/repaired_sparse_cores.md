# Translating the fibers of the ternary placement

Move a single residue fiber at scale \(K=3^{v_3(b-a)}\) by \(4Kt\), with \(0\le t\le h\). The [translation lemma](triangles_after_interleaving.md) preserves every integral-distance exclusion and the quadratic width estimate for any given normalized coloring. The translations change the right angles between fibers. I reconstructed the following five placements from their colorings and shifts. In each one, no tilted rectangle inside the strip has three black label corners.

| Height | Doubled columns | Width from first double to last | Initial corner count | Rounds to zero |
|---:|---:|---:|---:|---:|
| 127 | 4,032 | 894,425 | 27 | 1 |
| 383 | 36,672 | 12,375,917 | 852 | 4 |
| 511 | 65,280 | 14,332,241 | 1,828 | 3 |
| 769 | 147,840 | 49,933,709 | 4,819 | 6 |
| 1,025 | 262,656 | 60,073,677 | 9,567 | 28 |

The [search](fiber_translation_search.py) uses stride 96 and seed 186. It orders the legs by horizontal extent. For any contained tilted rectangle the product of their horizontal extents equals that of their vertical extents, and the latter have sum at most \(h-1\). This bounds the shorter horizontal extent by \((h-1)/2\). From either endpoint of each candidate short leg the search checks lattice multiples of the primitive perpendicular vector. The fourth row must fit in the strip. A separate [reconstruction and triangle check](check_fiber_translations.py) works from the list of row pairs, verifies the coordinate digest, and checks rectangles in the finite board using the earlier Python checker. The JSON file for each height gives the individual translations. The construction does not yet supply a uniform choice of shifts.

## All four-cell tests at height 127

In the board between the outermost doubles, color just the 8,064 label points black. This is a valid blackout. The two assertions needed beyond the triangle check are the absence of mixed presentations and the distinction of the axis rectangles.

For a mixed presentation write \(A,B\) for the two black corners forming a side, and \(C,D\) for the pair forming a diagonal in the competing rectangle. The common corners are
\[
 A+n,\ B+n,\qquad 2n=C+D-A-B,\qquad (B-A)\cdot n=0,\qquad |B-A|=|D-C|.
\]
The [mixed checker](core_mixed_witness.py) groups pairs by squared length. For a fixed side vector it finds every diagonal with the required midpoint projection, then checks integrality and both common corners against the grid. Distinct rectangles have different unoriented side and diagonal vectors in this case. Indeed, if the vectors agree up to sign, their common pair as reconstructed from the diagonal coincides with \(C,D\).

A length cutoff of 4,200 covers every possible side at height 127. A vertical side has length at most 126. For an oblique side with horizontal extent \(u\), the other side has nonzero integral horizontal extent \(v\), so \(u\le uv\le126^2/4\). For a horizontal side of length \(u\) and a diagonal of horizontal extent \(v<u\), all black columns are multiples of four. Thus \(u-v\ge4\) and \(u+v\le126^2/4\) by equality of lengths. In all three cases the side length is below 4,200. The checker returned no witness at that cutoff. At height 383 the scans stopped at 1,024, which gives only a partial check there.

The incidence graph of black rows against columns has girth at least eight. A four-cycle would repeat a row pair. A six-cycle would give a triangle of opposite-parity row pairs. The paper's comparison of two corner sets now applies even with empty columns. Two axis rectangles have distinct presentations by girth. A competing tilted rectangle with zero or one common corner needs three or more black tilted corners. With two common corners, the symmetric difference is a full rectangle if the roles of the common segment agree. Otherwise it gives one of the tested mixed pairs. This proves the finite assertion.

## Why the boundary rows alone cannot complete this core

At the empty column 853212, either boundary choice destroys validity. With a black cell in row 1, the true points \((853196,107),(853256,41)\) and that cell are corners of a rectangle with sole visible point \((853152,67)\). The axis rectangle with columns 853152 and 81888 and rows 67 and 96 has the same presentation. With a black cell in row 127, the true points \((853148,95),(853184,23)\) and that cell leave only \((853248,55)\) visible. The axis rectangle on columns 853248 and 84580 and rows 55 and 120 has that presentation. The owners in both comparisons are fixed doubles, so adding cells in other singleton columns cannot repair either choice. Allowing interior rows or moving these labels still leaves a possible completion.

Thus the verified 127-row configuration supplies all the doubles and distinguishes all rectangles with its remaining columns empty. Reaching \(m+q_h\) requires filling each remaining column and an extension to every larger width.
