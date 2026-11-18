# Two-row singleton completions of the 127-row ternary core

Fix the translated height-127 assignment in [the certificate](fiber_search_127_96_186.json). Keep the 3,886 doubles whose row gap is not divisible by 27. The scale \(K=3^{v_3(b-a)}\) then belongs to \(\{1,3,9\}\). In the horizontal interval from the first retained double to the last, fill each remaining column with a singleton. Assume the eventual board contains each opposite-parity row pair as a double, with the missing labels outside this interval.

**Finite result.** Any valid completion must use at least three distinct singleton rows within the retained interval.

## Geometric tests

If a tilted rectangle has three black corners and a white fourth corner \((z,q)\) in a double column, select its black row \(s\) of opposite parity to \(q\). The double owning the pair \(\{s,q\}\) gives an axis rectangle whose sole white corner is \((z,q)\). The same proof applies to a singleton column \(z\) if its black row has opposite parity to \(q\). Thus three corners can force the parity of a second singleton.

For a mixed support take a black side \(A,B\) and a black diagonal \(C,D\). Write \(U=B-A,\ V=D-C,\ T=C+D-A-B\). Their two rectangles have the common corners \(A+T/2,B+T/2\) when
\[
 |U|^2=|V|^2,\qquad U\mathbin{\cdot}T=0.
\]
The tests require integral, in-grid common corners, four distinct vertices in each rectangle, and distinct rectangles. When a vertical side is a parity pair placed outside this block, its location need not be specified. For a diagonal from \((x,y)\) to a singleton in row \(s\) of the other parity, set \(d=|y-s|\). The possible alternatives have vertical length \(d+2j\) and horizontal displacement \(2\sqrt{j(d+j)}\). Both common vertical endpoints must lie in the strip. The axis owner must differ from the column of the common vertical side. An owner outside the block always differs.

Only local true pairs need to be enumerated, apart from these vertical owners. If the two legs of a tilted rectangle have absolute horizontal components \(u,v\ge1\), their product equals the product of their absolute vertical components. The latter components sum to at most \(h-1\), so \(u+v\le uv+1\le (h-1)^2/4+1\). If a mixed support has a horizontal black side of length \(l\) and oblique black diagonal with horizontal magnitude \(d<l\), integral common corners give \(l-d\ge2\). Then \((l-d)(l+d)\le(h-1)^2\), which gives \(l\le(h-1)^2/4+1\). Indeed \(l-d\le h-1\), and the upper bound \(((h-1)^2/k+k)/2\) decreases over \(2\le k\le h-1\). Parallel side and diagonal directions give degenerate rectangles.

The first pass processes every candidate single point and tests these triangles in double columns and all mixed supports with three previously present black points. The second pass imposes the parity condition at a second singleton for each triangle containing two previous black points and one proposed filler. With a palette of two rows these conditions are clauses of at most two literals. Each pass supplies necessary conditions for full validity.

| Test applied | Two-row palettes still possible |
|---|---:|
| All unordered pairs of distinct rows | 8,001 |
| Single-point tests, including virtual vertical sides | 22 |
| Parity implications between two singleton columns | 1 |
| Three-diameter obstruction | 0 |

The last surviving pair is \(\{2,127\}\). For a hand witness take the black diagonal from \((424628,107)\) to \((424720,22)\). Pairing columns \(424670\) and \(424678\) with rows \(2\) and \(127\) in either order gives two more diagonals with the same midpoint and squared length \(15689\). If the two singleton columns choose opposite levels, two of the three diagonals are completely black. The two rectangles formed by pairing either black diagonal with the third diagonal have identical presentations. If both singleton columns choose the same level, pairing the original diagonal with a cross diagonal leaves one white corner in the other level. Its opposite parity gives the axis competitor above. The same three-diameter test works for any two levels of opposite parity whenever such a circle occurs.

On the entire 4,032-double assignment, each of the empty columns \(853212,853232,853236\) separately excludes rows 1 and 127 using triangles whose fourth corners are in true doubles. At \(853212\), choosing row 1 gives the three black corners \((853196,107),(853256,41),(853212,1)\) with white corner \((853152,67)\). The axis rival uses columns \(853152,81888\) and rows \(67,96\). Choosing row 127 instead gives black \((853148,95),(853184,23),(853212,127)\) with white \((853248,55)\). Its axis rival uses columns \(853248,84580\) and rows \(55,120\). Over all singleton sites on this full assignment the single-point tests remove at least one row at 78,491 sites. At most 110 rows are removed at any site. These figures leave the question of a simultaneous completion with three or more levels open.

## A fixed-mesh obstruction at every height

Suppose \(h\ge9\), the eventual owner of every opposite-parity pair lies in \(4\mathbb Z\), and the singleton alphabet consists of two interior levels \(s,t\) of opposite parity. Choose \(a=s\pm3\) and \(b=t\pm3\) in \([2,h-1]\), which is possible because the interior interval has at least seven integers. Let \(x\) be the column of their unique double. Every in-board column \(x\pm4\) must also be a double. Indeed, if it is filled at \(s\), the diagonal to \((x,a)\) has length 5. Its common vertical side in column \(x\pm2\) has rows \(\min(a,s)-1,\max(a,s)+1\). Their owner lies in \(4\mathbb Z\) and differs from \(x\pm2\). The same argument excludes \(t\) using the black point \((x,b)\). In particular a board of width at least nine with doubles restricted to \(8\mathbb Z\) cannot use this single interior two-row alphabet throughout. In a construction with several blocks the argument requires the neighboring column and the proposed singleton assignment to lie in the same block.

Run [the single-point checker](one_filler_check.py) without arguments for the complete assignment. Run [the two-row checker](two_level_filler_check.py) for the reduced core and all row pairs. The computations establish obstructions for these placements. They give no lower bound on the threshold for unrestricted blackouts.

