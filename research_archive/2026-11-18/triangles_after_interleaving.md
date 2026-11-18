# Three-label obstructions after ternary interleaving

In the ternary placement, all P tests can pass even when a triple of black label cells already makes a full blackout impossible. Here are concrete examples, an all-height exclusion for one family, and the translations that remain available.

## A failure at height 127

Take \(Q=96\) and the greedy three-coloring used by [the generator](ternary_graph.py). The following doubled columns are produced by [the placement code](check_ternary_placement.py).

| Column | Odd black row | Even black row |
|---:|---:|---:|
| 775120 | 1 | 118 |
| 775124 | 119 | 2 |
| 775984 | 1 | 64 |
| 775988 | 65 | 2 |

At \((775988,65)\) the two tilted legs to \((775984,1)\) and \((775124,119)\) are \((-4,-64)\) and \((-864,54)\). Their dot product is zero. The fourth corner \((775120,55)\) is white in a double. It already appears as the sole white corner of an axis-aligned rectangle. In this case its other row can be taken as 118, and the owner of \(\{55,118\}\) supplies the second column. Thus adding singletons cannot repair these four fixed columns.

In this example the scale is \(K=9\). The short leg crosses fibers 1 and 2. The long leg lies within fiber 2, joins endpoints of the same normalized row type, and has normalized displacement \((-96,6)\), a single Hilbert step.

## A uniform exclusion for close ranks

Keep one ternary residue profile and write \(t=v_3(Q)\ge1\). Suppose a tilted right angle has one leg crossing fibers within this run and the other lying in the pivot's fiber, joining two endpoints of the **same normalized row type**. All the claims here are independent of the choice of a proper coloring of \(G_s(Q)\).

In the normalized coordinates of the second leg its row displacement is \(6b\), where \(b\ne0\) is the difference of the corresponding Hilbert cell coordinates. The cross-fiber leg, after division by the common power of three of its coordinates, has direction \((4,1)\) times a nonzero scalar modulo three. Therefore both components of the normalized same-fiber leg must have the same 3-adic valuation. If the two colors differ, its horizontal component is a unit modulo three and its row component is zero modulo three, which rules out perpendicularity. If the colors agree, the horizontal component is \(Qd\) for the signed rank gap \(d\), so a necessary condition is
\[
 v_3(b)=t-1+v_3(d).
\]
Two Hilbert cells at rank distance \(|d|\) differ by at most \(|d|\) in either coordinate, since every step moves one lattice unit. In particular \(0<|d|<3^{t-1}\) is impossible. For any prescribed constant rank cutoff, a fixed \(Q\) divisible by a sufficiently high power of three excludes the entire family up to that cutoff. This argument uses only same-type endpoints on the same-fiber leg. It leaves opposite-type legs and long rank gaps.

Choosing \(Q=288\) gives \(t=2\), which rules out the height-127 mechanism at every height. An explicit surviving example at height 383 has pivot \((26636568,54)\) and legs \((4,256)\) and \((-3456,54)\). The fourth corner \((26633116,364)\) lies in the double \(\{109,328\}\) and is white. The other double rows at the three black corners are respectively \(\{309,54\},\{55,310\},\{327,108\}\). Here \(K=3\), the normalized same-fiber leg is \((-1152,18)\), \(|d|=4\), and \(b=3\). Thus the divisibility condition holds. This gives a direct counterexample to this particular placement with the changed stride.

## Translations that preserve all P exclusions

One can add \(4Kt_w\) to every column of a single fiber \(w\) of a run. All same-fiber displacements are unchanged. Different fibers still have \(x\equiv4w\bmod K\), so the P proof continues to hold. Recompute each run's bounding interval and gaps when assembling the board. Even allowing **each fiber independently** to choose \(0\le t_w\le h\) costs only \(O(h^2)\) in total width: one run at scale \(K\) needs at most \(4Kh\) extra columns and \(\sum_{3^e<h}3^e=O(h)\). The rank exclusion above is unchanged as well.

The simple shear \(t_w=w\) removes all three-label tilted rectangles with fourth corner in the strip and between the outermost label columns in the placements tested at heights 127, 191 and 257 with \(Q=96\). At height 383 it fails. The legs \((16,256)\) and \((-288,18)\) at \((9162472,1)\) complete at \((9162200,275)\) in a double. The freedom to choose translations separately for different fibers has no uniform selection proof. A repair within one fiber would require changing its normalized placement.

[The triangle checker](check_label_triangles.py) visits every possible shorter horizontal leg of a tilted right angle. For a rectangle in a strip of height \(h\), perpendicularity gives \(|X_1X_2|=|Y_1Y_2|\le(h-1)^2/4\), so this leg has horizontal extent at most \((h-1)/2\). The checker visits both pivots and all lattice multiples of the perpendicular primitive direction, checks the fourth point against both boundaries, and reports its first fatal double or the first incompatible parity demands on a singleton column. These tests concern black label cells before a sea is inserted.
