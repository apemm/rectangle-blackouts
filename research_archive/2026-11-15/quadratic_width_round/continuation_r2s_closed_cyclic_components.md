# Seven complete cyclic components of the R2s row graph

15 November 2026. The seven cyclic components found through `n=262144`
are complete components of the infinite positive sea-one row graph.
They cannot acquire extra vertices or chords at a larger height.
Each is unicyclic, so each is three-colorable.

This strengthens the finite cactus observation. It does not prove that
every component of the infinite graph is a cactus or has bounded
chromatic number.

## 1. A finite bound on every neighbor

Vertices are `n=y-1`, with sea row one and same-parity core columns in
`4Z`. Include a positive-offset crossed R2s support only when the sea
columns are outside `4Z` and the strong norm gap holds. Its parameters
satisfy

\[
 n\delta=TU,\qquad
 V^2=U^2-2n\delta-\delta^2,\qquad
 2X=U+T-V,\qquad \delta^2\le2X.
\]

The audited classification gives

\[
                 0<T<X<U\le n.
\]

Therefore an edge from n to `n+delta` satisfies

\[
                     \delta^2<2n.
\tag{1}
\]

Every larger neighbor of a vertex v is below
`v+sqrt(2v)`. Every smaller neighbor is positive and below v. Thus,
if a component found in the exact induced graph through H has

\[
             \max_{v\text{ in the component}}(v+\sqrt{2v})<H,
\tag{2}
\]

it is already a complete component of the infinite graph.

The ambient strip causes no later qualification. The two common rows
are `n+1+delta/2` and `1+delta/2`, both between row one and the upper
core row `n+delta+1`. Increasing the ambient height cannot add a new
support between two fixed rows that was excluded only by a white row
outside the earlier strip.

## 2. An independent neighbor enumeration

[The independent closure checker](check_r2s_closed_cyclic_components.py)
starts from the seven recorded cycles. At every reached vertex v it
tests every positive multiple-of-four increment up to `floor(sqrt(2v))`,
both as an incoming and outgoing edge. For each lower endpoint n it
enumerates every `U | n*delta`, sets `T=n*delta/U`, and tests both signed
square roots for V. It then applies the exact column residues and norm
gap. This is independent of the earlier factor-pair enumeration of
`4ab=T^2+delta^2`.

The search stops with 35 vertices and 35 edges. All seven components
are connected and have exactly one cycle. Every tested component also
satisfies (2), well inside the original height bound.

| Full component, in n-coordinates | Unique cycle | Upper bound for all neighbors |
|---|---|---:|
| 22250, 22270, 22286, 22306 | 22250, 22270, 22306 | 22517 |
| 35098, 35126, 35174, 35182 | 35098, 35126, 35182 | 35447 |
| 83910, 83950, 83990, 84010 | 83950, 83990, 84010 | 84419 |
| 106470, 106506, 106530, 106542, 106614 | 106470, 106506, 106542 | 107075 |
| 48906, 48950, 48958, 48982, 48994, 48998, 49030 | 48950, 48958, 48982, 48994 | 49343 |
| 146850, 146874, 146946, 146982, 146994, 147114 | 146850, 146874, 146946, 146982 | 147656 |
| 244750, 244790, 244834, 244910, 244970 | 244750, 244790, 244910, 244970 | 245669 |

The [saved exact result](check_r2s_closed_cyclic_components.json)
contains all 35 edge witnesses. All direct geometric and closure tests
pass. The row graph records potential pair constraints; the witnesses
need not all occur simultaneously at one choice of column positions.

## 3. What the repeated four-cycle means

The three recorded four-cycles have the same vertex pattern scaled by
1, 3, and 5. Their displayed geometric witnesses scale by those factors
as well. For a direct dilation by lambda, the norm gap becomes

\[
                  \lambda\delta^2\le2X.
\]

In the smallest four-cycle, the edge with `delta=44,X=4884` bounds an
integer dilation by five. An even dilation also blackens one required
sea-column residue. Hence the observed copies exhaust the admissible
positive integer dilations of these particular witnesses.

This does not exclude a larger scaled row pattern supported by entirely
different geometric witnesses. It only prevents treating the displayed
cycle as a freely scalable obstruction. A noncactus component elsewhere
would be disjoint from the seven complete components certified here.

The neighbor bound, global closure argument, ambient-height qualification,
and fixed-witness dilation scope have passed a separate written review.
