# Full affine embeddings of reversed Hilbert sections

15 November 2026. The exact finite invariant below proves a classification
at every depth. It is a computer-assisted induction with independently
checked finite certificates. It is not an inference from bounded-depth
enumeration.

## 1. The classification

Let `R_sigma(w)` be the reversed Hilbert section defined by the transition
table in
[the carry-automaton note](continuation_hilbert_affine_carry_automaton.md).
The state `sigma` is one of `X+,X-,Y+,Y-`. The binary word `w` has length
`q` and is read from low to high. The section consists of `2^q` residues
modulo `4^q`.

For `q>=2`, suppose an odd multiplier `u` and a translation `c` satisfy

`u R_sigma(w)+c = R_tau(w) mod 4^q`.

Then

`u belongs to {1,-1,5,-5,5^(-1),-5^(-1)} mod 4^q`.

More precisely, the union of allowed multipliers over all states and
translations is exactly this six-element set if the first `q-1` bits
of `w` are constant. Otherwise it is exactly `{1,-1}`.

The words and states are part of the theorem. Arbitrary unrelated
nonstationary digit sets are not covered.

## 2. Two elementary structural facts

Each section has two adjacent residues modulo four. Above every permitted
lower-rank prefix, its next digit also has two adjacent choices modulo
four. Such a pair has trivial translation stabilizer in `Z/4Z`.

Consequently an affine embedding with its multiplier and translation
fixed modulo `4^q` has at most one lift modulo `4^(q+1)` for a prescribed
next row bit. To see this, compose two supposed lifts. Their quotient acts
as

`x -> (1+t 4^q)x+s 4^q mod 4^(q+1)`.

On the fiber above lower prefix `x`, this translates the two top digits
by `tx+s mod4`. Trivial fiber stabilizers force `tx+s=0 mod4` for every
allowed lower prefix. Two such prefixes differ by an odd number, so
`t=s=0 mod4`.

There is also an exact negation involution. Put

`J(X+)=X-`, `J(X-)=X+`, `J(Y+)=Y+`, `J(Y-)=Y-`.

The transition table gives

`R_(J sigma)(w) = -R_sigma(w)-1 mod 4^q`.

Indeed, replacing every rank digit `d` by `3-d` and every state by `J`
preserves the reversed transitions with the same row bit. Thus negative
multiplier cases reduce to their positive counterparts.

## 3. A finite invariant that identifies the lift

The uniqueness observation alone does not identify which lift exists.
For that step, use the three positive rational representatives

`a/b = 1, 5, 1/5`.

At depth two, direct enumeration modulo 16 gives exactly

`{1,3,5,11,13,15} = {+/-1,+/-5,+/-5^(-1)} mod16`.

Fix one positive representative and write the embedding in the form

`a p-b r = C mod4^q`.

Use the reverse carry state `(sigma,tau,z)` and additionally retain the
least source-rank digit `d0`. The initial carry is zero. Every source
word has exactly one candidate target digit because `b` is odd. Full
embedding means that both source branches survive at every reached state.
Merging paths with the same tagged state loses no information about this
full-branch condition.

For a next common row bit and translation digit `e`, the canonical
transition has

`a d1-b d2-e+z = 4 z'`.

If the next multiplier were instead

`a/b + lambda 4^q`, with `lambda in {1,2,3}`,

then its last-digit congruence would be

`a d1-b d2-e+z+b lambda d0 = 0 mod4`.

This is why the lowest source digit is retained. The noncanonical step
is only a final-digit existence test. Its carry is not propagated.

The certificate contains a finite family of tagged-state subsets for
each positive representative. It has these three properties:

1. It contains every full two-digit initial state subset.
2. Every canonical full-branch successor belongs to the same family.
3. For every member, every next row bit, every translation digit, and
   every nonzero `lambda`, at least one source branch is rejected.

The exact certificate sizes and checks are:

| Representative | Initial subsets | Invariant subsets | Canonical edges | Rejected lift tests |
|---|---:|---:|---:|---:|
| `1` | 39 | 131 | 166 | 3144 |
| `5` | 12 | 22 | 16 | 528 |
| `1/5` | 12 | 30 | 24 | 720 |

These properties prove the multiplier classification by induction. A full
embedding at depth `q+1` projects to one at depth `q`. By induction its
multiplier is one of the six representatives. Apply the negation
involution if necessary. Its full prefix gives a member of the relevant
invariant family. Property 3 excludes every noncanonical next multiplier
digit, while property 2 retains every possible canonical extension.

All invariant subsets are saved in
[hilbert_affine_lifting_certificate.json](hilbert_affine_lifting_certificate.json).
The generating checker is
[check_hilbert_affine_lifting.py](check_hilbert_affine_lifting.py), and its
compact result is
[check_hilbert_affine_lifting.json](check_hilbert_affine_lifting.json).

The separate
[check_hilbert_lifting_independent.py](check_hilbert_lifting_independent.py)
initializes the two-digit states from complete word-pair congruences,
rather than the generating search. It tests all digit pairs directly,
without modular inversion. It independently reproduced every count in
the table and verified the three invariant properties.

## 4. Which row words admit the exceptional slopes

The slope-five three-digit certificate gives at most six paths when
the first two row bits differ, regardless of the third bit, translation,
or starting states. A full three-digit section has eight words. Thus an
embedding at slope 5 cannot have a row-bit change before the final bit
of the complete word. Swapping the sections handles slope `1/5`, and
the involution `J` handles their negatives.

Conversely, if the first `q-1` bits are 1, the three states

`(Y+,X+,0)`, `(Y+,X-,2)`, `(Y+,Y-,1)`

have full two-branch transitions under row bit 1 and translation digit 3.
The same subset has a full final step under either row bit with translation
digit 3. Starting at `(Y+,X+,0)` therefore gives a full modular slope-five
embedding. Complementing every row bit and exchanging `X+` with `X-`
and `Y+` with `Y-` gives the analogous construction when the first bits
are 0. Inversion and negation supply the other three exceptional slopes.
The multipliers `1,-1` always occur by identity and `J`. This proves the
more precise row-word assertion in Section 1.

## 5. A uniform block loss for every other odd rational slope

Let `a,b` be nonzero odd integers, reduced if desired, and suppose

`a/b is not in {1,-1,5,-5,1/5,-1/5}`.

Choose the least integer `q>=2` such that

`4^q > 5(|a|+|b|)`.

The residue `a b^(-1) mod4^q` cannot be one of the six exceptional
residues. Each such congruence would make one of the nonzero integers
`a+/-b`, `a+/-5b`, or `5a+/-b` divisible by `4^q`, although its absolute
value is smaller than that modulus.

Therefore every common-row block of length `q`, every pair of initial
section states, and every translation permit at most `2^q-1` paths.
For ordinary sections of a Hilbert square of side `N=2^k`, this gives

`I_N(y;a,b;c) <= 16 * 2^(k mod q) * (2^q-1)^floor(k/q)`.

In particular,

`I_N(y;a,b;c) <= C N^(1-eta)`,

where

`eta = -log_2(1-2^(-q))/q > 0`.

The bound is uniform in the row, translation, and global section states.
Writing `K=|a|+|b|`, the choice of `q` gives

`eta >= c/(sqrt(K) log(2K))`.

For fixed nonexceptional slope this is a power saving. For a growing
slope palette its exponent decreases as displayed. The exceptional
slope-five average and its linear-sized special row are treated in the
earlier carry-automaton note.

## 6. Construction scope

This theorem resolves the full-branch multiplier classification for raw
Hilbert row sections. It does not establish the needed joint saving
after the six-point increment divisibility and hub constraints are
imposed. Those restrictions cannot be treated as independent of the
section intersection. Cap constants and crossings of folded branches
also retain their separate hypotheses.

The finite-state proof and the lifting invariant passed an independent
implementation and a separate written induction review. No full
quadratic-width construction is claimed.
