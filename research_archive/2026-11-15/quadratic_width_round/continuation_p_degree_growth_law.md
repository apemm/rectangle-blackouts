# The growth law of the P degree in the aligned Hilbert tile

15 November 2026. Problem 001. This note measures how the number of P
constraints per label grows with the side. It is a measurement, not a
theorem.

## Result

The mean P degree grows like `(log h)/S`. It does not level off. In the
aligned tile of side `s`, offset `-2s`, with three choices:

    mean degree = about (21.5 / S) * log2(s) + constant.

So no argument through bounded degree, degeneracy or the local lemma can
give a fixed stride and a fixed number of choices.

## Setup

The tile has side `s = 2^k` and offset `T = -2s`. A label has slot
`3r + xi`. The degree of a label is its number of distinct pairs (partner,
choice difference) that give an integral cross-parity distance. Every such
event is `Y = g e f`, `q = g (f^2 - e^2)/(2S)` with `g, e, f` odd, `e < f`
coprime and `f = +-e (mod S)`. The script `sample_p_degree_growth.py` lists
these triples once and then finds the partners of each sampled label by
decoding the candidate Hilbert ranks. Each row below uses 2000 random
labels, except sides 512 and 1024 at stride 32, which use 3000.

Check: the complete event sets at sides 512 and 1024 give mean degrees
3.564 and 4.138 (twice the events per label). The sampler gives
3.556 +- 0.040 and 4.114 +- 0.044.

## Data

Stride 32:

| Side | Mean degree | Standard error | Share of labels with degree >= 3 |
|---:|---:|---:|---:|
| 512 | 3.556 | 0.040 | 0.649 |
| 1024 | 4.114 | 0.044 | 0.725 |
| 2048 | 4.859 | 0.057 | 0.836 |
| 4096 | 5.432 | 0.059 | 0.876 |
| 8192 | 6.137 | 0.063 | 0.919 |
| 16384 | 6.748 | 0.065 | 0.948 |
| 32768 | 7.638 | 0.070 | 0.970 |
| 65536 | 8.251 | 0.074 | 0.977 |

Stride 64:

| Side | Mean degree | Standard error | Share of labels with degree >= 3 |
|---:|---:|---:|---:|
| 1024 | 1.931 | 0.037 | 0.304 |
| 2048 | 1.998 | 0.036 | 0.329 |
| 4096 | 2.536 | 0.041 | 0.446 |
| 8192 | 2.679 | 0.042 | 0.484 |
| 16384 | 3.292 | 0.046 | 0.595 |
| 32768 | 3.597 | 0.048 | 0.661 |

## Fit

- Stride 32: the degree rises by 0.671 per doubling of the side on
  average. The seven increments are 0.56, 0.75, 0.57, 0.71, 0.61, 0.89,
  0.61, with no trend. So the growth is linear in `log h`, not constant
  and not `log^2 h`, over this range.
- Stride 64: the degree rises by 0.333 per doubling on average.
- The products `0.671 * 32 = 21.5` and `0.333 * 64 = 21.3` agree. So the
  slope is inversely proportional to the stride.

I did not sample sides `2^18` and `2^20`. The cost doubles with each step
(six minutes at `2^16`), and eight sides already separate the three laws.

## Consequences

1. With a fixed stride and a fixed palette, the degree is unbounded. The
   share of labels with at least three constraints is already 0.98 at side
   65536 and stride 32, so peeling removes almost nothing there.
2. To keep the mean degree below a fixed level, the stride must grow like
   `log h`. The P family alone then costs a factor `log h` in width. So the
   honest target of this route is `h^2 log h`, not `h^2`.
3. A fixed stride and palette could still work only for a structural
   reason that handles all factors together. I have no such argument.

## Scope

One family of tiles (aligned, offset `-2s`), the P family only, three
choices. The global board has other offsets, and its counts per label
differ by constant factors because of the strip and owner restrictions.
