# Explicit good rows from inert prime factors

15 November 2026. This gives arithmetic subsets of the good rows for
the constant-sea scaffold. It does not give bounded good-row gaps or a
quadratic construction. The current global bad-row estimate already
proves that almost all rows are good; the point here is an explicit
description that may support a local gap estimate.

## 1. Geometry and the prime-factor criterion

Use the same-sea mixed-support equations from
[the spacing-four transfer](continuation_step_four_r2s_transfer.md).
Write the positive side-owner distance above the sea as `n=y-s`.
Then

`TU=n delta`,
`V^2=U^2-2n delta-delta^2`,
`2X=U+T-V`.                                                (1)

The two inserted rows have the same residue modulo four, so
`delta` is a nonzero multiple of four. Integral white corners require
`T` even. The side's sea displacement `U` is nonzero and is not divisible
by four. The refined same-parity geometry gives
`delta^2<=2|X|`, apart from the bounded seam `|X|=|delta|=4`.

For positive `delta=d`, the geometric proof in the transfer note,
with `n` in place of its bound `h`, gives

`d<=4 sqrt(n)`, and `|T|<=4n/d` whenever `|X|>=16`.          (2)

For completeness, in its `|U-X|<=X/2` regime the second bound follows
directly from `|U|>=X/2` and `d^2<=2X`. In the other regime,
`|U|>X/2` gives the same inequality. When `|U|<=X/2`, the sign
`m delta<0` gives `|T|<=sqrt(nd/2)` and `d<2n^(1/3)`, hence again
`|T|<=2n/d`. These are all positive-delta cases. Reflection makes
`X` positive without changing `d`. Small `|X|` and the seam have
`d=4`.

**Lemma.** Suppose `n=c p`, where `c>=1` is an integer and `p` is a
prime congruent to 3 modulo 4, with `p>32c^2`. Then no positive-delta
support satisfying (1) and the preceding geometry exists.

Indeed, (2) implies `d<p`, since `p>32c^2>=32c` and
`4 sqrt(cp)<p`. The same conclusion holds in the bounded cases.
As `p` divides `TU`, either `p` divides `U` or `p` divides `T`.
In the first case (1) gives

`V^2+d^2=0 mod p`.

The fact that minus one is a quadratic nonresidue modulo `p` forces
`p` to divide `d`, a contradiction. Thus put `T=p t`. Equation (1)
now gives `t U=c d`, so `|U|=c d/|t|`. Nonnegativity of `V^2`
implies

`c^2 d^2/t^2 >= 2c p d+d^2`,

and therefore `d>2p t^2/c`. If `|X|>=16`, (2) gives
`d|t|<=4c`. Combining these inequalities yields
`p<2c^2/|t|^3<=2c^2`, a contradiction. In the bounded cases
`d=4`, already `c^2 d^2<2cpd` under `p>32c^2`, so the norm
equation is impossible without using the second part of (2).

Consequently any row distance `n` having a prime factor

`p=3 mod4`, `p>32^(1/3) n^(2/3)`                         (3)

is excluded from the positive-delta R2s family.

This criterion concerns actual candidate supports. If an implementation
defines its bad-row superset using a looser geometry, its superset must
be tightened before treating (3) as a permitted row family.

## 2. Two complete explicit prime families

Assume `1<=s<=4`. The row of the second white corner is
`s+delta/2`, so negative delta forces `delta=-4`. Let

`p=79 mod420`

be prime, and large enough for the preceding lemma. Both distances
`n=p` and `n=2p` then give rows that admit no R2s support at all.

For negative delta, the alternative `p|U` again contradicts
`V^2+16=0 modp`. Thus `T=p t` and `t U=-4c`, for `c=1` or `2`.
Since `T` is even, `t` is even. Hence `|U|` divides `2c`.

For `c=1`, the possibilities are `|U|=1,2`:

* If `|U|=2`, then `V^2=8p-12=12 mod16`, impossible.
* If `|U|=1`, then `V^2=8p-15=2 mod3`, because `p=1 mod3`.

For `c=2`, the possibilities are `|U|=1,2,4`:

* If `|U|=4`, then `V^2=16p`, impossible for prime `p`.
  This value of `U` is also excluded by the sea-column congruence.
* If `|U|=2`, then `(V/2)^2=4p-3=3 mod5`, because `p=4 mod5`.
* If `|U|=1`, then `V^2=16p-15=3 mod7`, because `p=2 mod7`.

All are impossible. The congruence `p=79 mod420` supplies every
residue used here, including `p=3 mod4`.

For odd seas, `n=p` gives an even inserted row and `n=2p` gives
an odd inserted row in the required opposite residue modulo four.
The remaining half-strip, bulk, and physical height restrictions still
have to be imposed. Reflection gives the corresponding statement near
a high sea whose reflected height is at most four.

## 3. Limits

The proof is elementary and makes no assertion about primes in short
intervals. It produces explicit good rows, not bounded spacing between
them. The sparse prime family cannot replace every original double label.
The large-prime-factor criterion in (3) is a possible input to a future
local distribution argument. No such argument is supplied here.

Review status: the full proof passed an independent written derivation,
including the use of n in the geometric bound, the bounded-offset cases,
and every prime congruence. See
the saved audit.
The separate [multiplicative refinement](continuation_multiplicative_r2s_good_rows.md)
now supplies a larger explicit family without the large-prime condition.
