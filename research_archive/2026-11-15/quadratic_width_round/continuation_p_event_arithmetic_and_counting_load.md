# P events: a divisibility lemma and a counting estimate for fixed palettes

15 November 2026. This note concerns open item 1 of
[STOPPING_POINT.md](STOPPING_POINT.md): uniform solvability of the aligned
P systems with a fixed number of actual choices. It proves one lemma and
records one heuristic estimate. The estimate is not a theorem. I have not checked either part a second time.

## 1. Parametrization of the events

Stride 32, `M = 3`. A label of rank `r` at cell `(i, j)` has slot
`c_r = 3r + xi_r` with `xi_r` in `{0, 1, 2}`. For two labels `u, v` the
cross-row differences are

    Y_1 = 2T + 1 + 2(j_v - i_u),      Y_2 = 2T + 1 + 2(j_u - i_v),

and a P event with gap `q = |c_v - c_u|` is an integer solution of
`(32q)^2 + Y^2 = L^2` with `Y = |Y_1|` or `Y = |Y_2|`.

Put `a = (L - Y)/2`. Then `a(a + Y) = 256 q^2`. Let `g = gcd(a, Y)`. The
numbers `a/g` and `(a + Y)/g` are coprime with a square product, so
`a = g m^2`, `a + Y = g n^2`, `gcd(m, n) = 1`. With `e = n - m`,
`f = n + m`:

    Y = g e f,      q = g (f^2 - e^2)/64,                               (1)

where `g, e, f` are odd, `e < f`, `gcd(e, f) = 1`, and `64 | f^2 - e^2`,
that is `f = +-e (mod 32)`. Conversely every such triple gives an event.
So the gaps that a pair can have are read off from the factorizations of
its two odd numbers `Y_1, Y_2`.

## 2. Lemma: a gap not divisible by 3 needs 3 | Y

**Lemma.** In (1), if `3` does not divide `Y`, then `3 | q`.

*Proof.* If `3` does not divide `Y`, it divides neither `e` nor `f`, so
`e^2 = f^2 = 1 (mod 3)` and `3 | f^2 - e^2`. Since `64` is prime to 3,
`3 | q`. QED

If `3 | Y`: when `3 | g`, again `3 | q`. When `3 | e`, `q = g (mod 3)`.
When `3 | f`, `q = -g (mod 3)`.

**Consequence.** Write `q = 3d + delta` with `d` the rank difference and
`|delta| <= 2`. An event with `delta != 0` needs `3 | Y`. Since
`Y_1 = 0 (mod 3)` exactly when `j_v - i_u = kappa (mod 3)` for one fixed
residue `kappa = (1 - T) mod 3`, the events with `delta != 0` occur only
for one of the three residue classes of `j_v - i_u`. Every other event
forbids only equal choices, `xi_u = xi_v`.

Check on the saved side-1024 system (offset -2048, 2,169,330 candidate
events): all 564,864 first-role hits with `delta != 0` have `3 | Y_1`, with no
exception. The second role was not tabulated. The hits with `delta = 0` have `Y` in all three classes
(199126, 146445, 151894 for the first role).

The lemma is special to the palette size 3, because 1 is the only nonzero
square modulo 3.

## 3. Counts by delta at side 1024

Events per label, by the exact integer `delta` that gives a norm:

| `delta` | -2 | -1 | 0 | 1 | 2 |
|---|---:|---:|---:|---:|---:|
| Side 1024, offset -2048 | 0.259 | 0.292 | 0.972 | 0.258 | 0.287 |
| Side 512, offset -1024 | 0.199 | 0.260 | 0.865 | 0.210 | 0.249 |

About half of the events are equality events (`delta = 0`). Their graph at
side 1024 has 892,764 vertices and 1,019,628 edges, and it is not
bipartite.

## 4. A counting estimate (heuristic)

An event with a given `delta` forbids `3 - |delta|` of the 9 ordered pairs
of choices. If the events acted independently, the expected number of valid
assignments on `n` labels would be

    3^n * prod_events (1 - p_event) = exp( n (ln 3 - Lambda) ),

    Lambda = sum over delta of (events per label) * ( -ln(1 - (3 - |delta|)/9) ).

Call `Lambda` the load. In this model, solutions exist only while
`Lambda < ln 3 = 1.099`. For the stronger modular model every event forbids
3 of 9 pairs, so its load is `(events per label) * ln(3/2)`.

| Side | Events per label | Integer load | Modular load |
|---:|---:|---:|---:|
| 512 | 1.782 | 0.522 | 0.723 |
| 1024 | 2.069 | 0.597 | 0.839 |

The events per label grow by about 0.29 for each doubling of the side,
which agrees with the logarithmic growth of the mean P degree in the
earlier notes. Extrapolating linearly in the logarithm of the side:

- The modular load reaches `ln 3` between sides 4096 and 8192.
- The integer load reaches `ln 3` near side `2^16` to `2^17`.

**What this suggests.**

1. It explains the present data without any appeal to structure: at side
   1024 the integer system is far below the bound and was solved, and the
   modular system is close enough to the bound to be hard for a solver.
2. For a general palette `M`, an event forbids about a fraction `1/M` of
   the pairs, and the number of candidate events per label grows in
   proportion to `M`. So the load is roughly independent of `M`, while the
   entropy is `ln M`. The independent model then needs
   `ln M >= c log(side)`, a palette that grows like a power of the side.
3. So a proof of uniform solvability with a fixed palette has to use
   positive correlation between events: many events must forbid the same
   assignments. Any argument that treats events at different scales as
   independent cannot succeed. This agrees with the partition-regularity
   result for the full odd P graph, and with the failure of the energy
   bound and of the local limit.

**Limits of the estimate.** The model is not the actual system. The events
are arithmetic, the excursion decomposition shows strong structure, and
structured systems can be solvable far above a first-moment bound. The
growth rate rests on two sides only, and the two offsets scale with the
side. The estimate proves nothing about solvability at any size.

## 5. A decisive test that stays small

The estimate predicts that the stronger modular system fails first, near
side 4096 to 8192. A direct solver run at that size is too large. A
smaller test is the weighted core: the estimate predicts that the core of
the modular system at side 2048 is close to unsatisfiable. A solver result
either way on that core, or on a dense sub-tile of it, would show whether
the independent model describes these systems. This was not run.

## 6. Scope

P-only, aligned, stride 32. Nothing here concerns fillers, the other
families, or a full board.

## 7. The side-2048 run (15 November 2026)

The side-2048 system at offset -4096 was generated with the rank-lag
generator: 10,187,303 candidate events, 2.429 per label, with the hash in
`aligned_private_side2048_minus4096.json`; the 122 MB event file is not
stored and can be regenerated (see the README). Its modular load is `2.429 ln(3/2) = 0.985`. The growth from side 1024
is 0.36 events per label, more than the 0.29 used in Section 4.

The weighted three-core has 3,273,463 labels and 8,768,226 events. No
solver result was obtained under a 4 GB memory limit:

- Glucose 4 (`probe_aligned_private_sat.py`) failed while loading, with
  its allocator limit exceeded.
- CaDiCaL (`probe_aligned_private_sat_cadical.py`) reached the 3.8 GB cap
  while loading and was stopped.
- A min-conflicts local search (`probe_modular_local_search.py`) stalls at
  about 45,000 violated events already on the side-1024 modular system, so
  it gives no information.

The test of Section 5 is therefore undecided. The integer mask for side
2048 was not computed.

A later CaDiCaL run with a 9 GB cap loaded the core in 43 seconds, then
reached the cap during the solve and was stopped. The test remains
undecided.
