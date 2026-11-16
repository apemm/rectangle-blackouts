# The parked-six family survives a single good-row step

15 November 2026. Independently reviewed. A constant odd sea and an inserted sequence with one
isolated spacing-four step can have two tilted rectangles with the same
single white corner. The example persists after excluding any `o(h)`
prescribed inserted rows.

This separates the parked-six obligation from the other three residual
families in the constant-sea geometric reduction. It does not claim that
the example embeds in every folded-cap Hilbert order.

## 1. An exact family

Let `n` be a positive integer with `n=2 mod4`, and put

`y=1+5n`.

Use sea row `L=1`. Consider the four inserted points

```
A1 = (-20n,    y),       C1 = ( 0, y+4),
A2 = (-4n-4,   y),       C2 = (-4, y+4),
```

and the two sea points

```
B1 = (1-20n, 1),         B2 = (1-4n, 1).
```

Their columns have the prescribed types. The inserted columns are
divisible by four, and both sea columns are `1 mod4`. Both inserted rows
are `3 mod4`, as required for odd labels above sea row 1.

The two right-angle equations, at `A1` and `A2`, are

```
(C1-A1) dot (B1-A1) = (20n,4) dot (1,-5n) = 0,
(C2-A2) dot (B2-A2) = (4n,4)  dot (5,-5n) = 0.
```

Both fourth corners are

`W=C1+B1-A1=C2+B2-A2=(1,5)`.

The six black points are distinct. In particular, the two sea columns
differ by `16n`, and inserted points cannot coincide with a sea point.
The two rectangles are therefore distinct. Since column 1 has its sea
point at row 1, `W` is white.

Both rectangles lie inside any board containing columns from `-20n`
through `4` and rows from 1 through `y+4`. Negative columns can be
removed by translating all columns by a multiple of four.

## 2. A fully occupied inserted sequence with just one seam

Fill every arithmetic column in this interval by row `y` to the left
of one jump, and by row `y+4` to its right. Place the jump strictly after
`A2` and no later than `C2`. Fill every other column by sea row 1.
Every column is occupied exactly once.

The inserted points lie on a 1-Lipschitz graph. For a nonhorizontal pair,
the vertical difference is 4. Unless its horizontal distance is 4,

`16 <= 2 |Delta x|`.

The sole adjacent crossing pair is the isolated vector `(4,4)`. Its
length is nonintegral. There is only one such seam, so two perpendicular
seam legs cannot occur. Hence there is no inserted three-corner right
angle. The closed-cone lemma also excludes every nonvertical mixed
four-support among inserted points.

All selected rows are odd, so no opposite-parity P event exists in this
core. The two repeated presentations above are nonetheless present.

For any fixed interpolation mesh, the jump can also be placed at one
of its permitted unit-change positions when `n` is sufficiently large.
The interval between `A2` and `C2` has `n` fine steps. It eventually
contains a position in the required fixed congruence class. Thus merely
separating the unit changes by a fixed mesh does not remove this family.

## 3. Sublinear row filters cannot exclude all examples

Fix a sufficiently large height `h`. Choose

`h/8 <= n <= h/7`, with `n=2 mod4`.

There are `Theta(h)` such integers. They satisfy

`y>(h+1)/2` and `y+4<=h`.

Thus both inserted rows lie in the allowed upper-half odd pool for the
low constant sea. They also lie far from the strip and bulk boundaries.

Let `B_h` be any prescribed bad-row set of size `o(h)`. Each physical
row can equal at most one of the values `1+5n` or `5+5n`, over all these
integers `n`. Equality between the two forms for different integers
would require `5(n-n')=4`, which is impossible. Consequently at most
`|B_h|` choices of `n` are removed by demanding that both inserted rows
avoid `B_h`.

In particular, the `h^(5/6+o(1))` R2s side-owner filter still leaves
`Theta(h)` choices. Applying that filter removes the crossed same-sea
mixed supports covered by its theorem. It does not remove the repeated
parked triples exhibited here.

## 4. Scope

The example shows that full occupancy, the half-strip rule, good rows,
same-parity nonintegral distances, isolated seams, and the 1-Lipschitz
mixed-support exclusion do not imply uniqueness of parked completions.
The fourth residual system remains necessary in
[the constant-sea assembly](continuation_constant_sea_assembly.md).

The constructed inserted sequence is a geometric example. It is not a
claim about an unavoidable pattern in the actual folded-cap Hilbert
construction, nor a lower bound on the final construction width.

The independent review checked both dot products, the common white
completion, six-point distinctness, residue and strip conditions, the
one-step geometric exclusions, and robustness under a sublinear row filter.
