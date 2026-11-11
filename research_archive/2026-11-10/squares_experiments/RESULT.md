# Algebraic layouts on square grids: result

10 November 2026.

## Verdict

No ordering of a girth-8 incidence graph at q = 2, 3, 4 beats the random collision rate by more than
a constant factor near 2, and the factor shrinks as N grows. No ordering reaches zero collisions.
After deletion, the valid sets are no larger than what random insertion on the whole grid gives, and
they stay near 2N. The growth exponent of f(n,n) stays an open problem. I stopped here, as planned.

## Setup

- d_q: points (p1,p2,p3) and lines [l1,l2,l3] over GF(q), incident when p2 + l2 = p1 l1 and
  p3 + l3 = p1 l2. N = q^3, q^4 black cells.
- gq_q: points and lines of the symplectic quadrangle W(q). N = (q+1)(q^2+1), (q+1)N black cells.
- All six graphs have girth 8 (computed), so no layout has a collision among axis rectangles alone.
- Rate = (M4 + M6) / (black cells). M4 counts pairs of rectangles that share two corners and have the
  other four black. M6 counts pairs of right angles with three black corners and the same fourth
  corner. Tilted rectangles are included. A set is valid exactly when M4 = M6 = 0 and at most one
  rectangle is fully black.
- Baselines: a uniformly random set of the same size, and a random ordering of the same graph (20
  samples each, 6 at N = 125).
- Natural orderings: lexicographic in the coordinates, 36 coordinate orders for d_q and 24 for gq_q.
- Search: swaps of two rows or two columns with annealing, 150 s from the best natural ordering and
  150 s from a random one (210 s each at N = 125).

## Collision rates

| q | graph | N | cells | random set | random ordering | best natural | best found (search) | best / random ordering | zero reached |
|---|---|---|---|---|---|---|---|---|---|
| 2 | d2 | 8 | 16 | 4.2 | 1.8 | 1.2 | 0.25 | 0.14 | no (4 collisions left) |
| 2 | gq2 | 15 | 45 | 38.1 | 16.7 | 17.2 | 8.4 | 0.50 | no |
| 3 | d3 | 27 | 81 | 38.5 | 19.1 | 13.3 | 8.6 | 0.45 | no |
| 3 | gq3 | 40 | 160 | 124.4 | 65.9 | 59.9 | 39.5 | 0.60 | no |
| 4 | d4 | 64 | 256 | 108.2 | 59.5 | 59.0 | 34.3 | 0.58 | no |
| 5 | d5 | 125 | 625 | 230.9 | 135.1 | 133.2 | 92.1 | 0.68 | no |

Readings:

- A random ordering has about half the rate of a random set. That is the girth: the collisions made
  of axis rectangles only are gone, the tilted ones are not.
- The best natural ordering is within 30% of a random ordering. The mean natural ordering is worse
  than random at q = 4 and 5.
- The search gains a factor 1.5 to 2.2 over a random ordering for N >= 15. The gain falls with N
  (0.50, 0.45, 0.60, 0.58, 0.68). The six-cell count M6 barely moves (for d4, 10,378 to 7,108), and
  the number of black right angles drops by about 10% only.
- The searched orderings show no block or modular structure. Neighbouring rows and columns share a
  coordinate value about as often as in a random order (d4: 12 to 23 against 15 expected).

## Valid subsets after deletion

Lazy greedy hitting set on the collisions, then re-insertion, and also insertion in random order.
Every board was rechecked by an independent enumeration of rectangles as pairs of equal diagonals
with a common midpoint.

| graph | N | cells | deletions (searched) | valid size: searched | best natural | random ordering | random set | random insertion on the whole grid | 2N-1 | N^(6/5) | N^(4/3) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| d2 | 8 | 16 | 2 | 14 | 12 | 13 | 12 | 15 | 15 | 12 | 16 |
| gq2 | 15 | 45 | 18 | 28 | 26 | 26 | 24 | 28 | 29 | 26 | 37 |
| d3 | 27 | 81 | 32 | 49 | 45 | 46 | 42 | 51 | 53 | 52 | 81 |
| gq3 | 40 | 160 | 84 | 76 | 75 | 71 | 70 | 77 | 79 | 84 | 137 |
| d4 | 64 | 256 | 131 | 127 | 121 | 121 | 117 | 131 | 127 | 147 | 256 |
| d5 | 125 | 625 | 372 | 256 | 261 | 252 | 249 | 274 | 249 | 328 | 625 |

More than half of the incidences must go. What is left is at or below random insertion with no
structure at all, and below N^(6/5) from N = 27 on. For comparison f(8,8) >= 17.

## Small squares (side result)

| n | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| f(n,n) | 4 | 5 | 7 | 10 | 12 | 14 | >= 17 | >= 19 | >= 21 |

- n <= 7 are the recorded values. The encoder here reproduces them (n = 3 to 7, SAT at f and UNSAT
  at f + 1).
- n = 8 at 18 cells: 7 of 32 cases closed (all UNSAT), the rest were stopped. Not decided.
- New boards: 9 x 9 with 19 cells and 10 x 10 with 21 cells (`data/boards_n9_k19.json`,
  `data/boards_n10_k21.json`), all rechecked.
- All optima: 53, 316, 8, 160 boards for n = 3, 4, 5, 6 (complete). For n = 7, 3,509 boards in 843
  orbits (enumeration stopped at 15 minutes).
- Shape of the optima (`data/square_structure.json`): the row-column graph is a spanning tree for
  n = 3, 4 and has one cycle for n = 5, 6, 7 (girth 8, sometimes 10 or 12). The boundary holds
  about its uniform share of the black cells (0.58 against 0.56 at n = 6, 0.51 against 0.49 at
  n = 7), with 2 or 3 corners black. Row counts are uneven, typically (4,3,2,2,1,1,1). So the optima
  are a few long boundary rows and columns plus a sparse interior, not a regular incidence
  structure.

## Not run

- W(4) (N = 85): the quadrangle code handles prime q only.
- q = 4 has the single graph d4. Nothing beyond q = 5 was tried.
- The remaining 25 cases of 8 x 8 at 18 cells, 8 x 8 at 19 to 21 cells (unresolved at 18 minutes),
  9 x 9 at 20 cells (unresolved), and the structure tables for the 8 x 8, 9 x 9 and 10 x 10 boards.
- Annealing at 8 x 8 with 18, 9 x 9 with 20 and 21, and 10 x 10 with 22 was stopped before it wrote
  a result.

## Files

- `rectcore.py`: rectangle enumeration, the independent verifier, the collision counters.
  `test_rectcore.py` checks them against each other on 400 random sets.
- `algebraic_layouts.py NAME SECONDS`: one graph. Output `data/layout_NAME.json`.
- `baseline_insertion.py`: random insertion and the frame. Output `data/baseline_insertion.json`.
- `square_sat.py`, `anneal_square.py`, `analyze_squares.py`: the small squares.
- `make_tables.py`: prints the tables above from the data files.
