# Larger fixed palettes improve the all-order thin-block regime

15 November 2026. The same radical-phase argument gives a better
sufficient offset when the fixed private palette has more than three
choices. It permits even reduced multipliers in a controlled finite
range. The three-choice threshold is unchanged.

Fix a power-of-two S>=4 and M>=3. Use any ordering of the side-s
Cartesian label tile and the notation

\[
 V=|2(J-I)+1|,\quad Y_{\min}=V-2(s-1),\quad Q=Ms^2-1.
 \tag{1}
\]

Keep all candidate constraints q=Md+delta>0, |delta|<=M-1, for which
(Sq)^2+Y^2=L^2, where Y is the absolute cross-row difference.

**Theorem.** For all sufficiently large s, depending only on S,M,
the condition

\[
                         Y_{\min}\ge {Q^2\over(M-1)^2}
 \tag{2}
\]

gives a common certified Beatty solution with M private choices, in
every ordering of the tile.

To prove this, write a=(L-Y)/2, b=(L+Y)/2. Then

\[
 ab=S^2q^2/4,\qquad
                     a<{S^2(M-1)^2\over4}=:A_*.
 \tag{3}
\]

The factor menu is bounded independently of s. The square-root
approximation q=(2sqrt(V)/S)sqrt(a)+O_(S,M)(1/s) and the integer
cross-multiplication argument give exact proportionality inside every
observed squarefree class. Write a_i=d m_i^2, g=gcd(m_i), n_i=m_i/g,
and q_i=n_i Q_d, with Q_d an integer. As before, this does not require
the smallest factor in the class to occur.

If a_i is even, b_i is odd and

\[
 v_2(a_i)=2v_2(S)-2+2v_2(q_i).
 \tag{4}
\]

Its squarefree part d is therefore odd, and

\[
 v_2(m_i)\ge v_2(S)-1,\qquad
                 v_2(q_i/m_i)=1-v_2(S)<0.
 \tag{5}
\]

For an odd a_i the ratio q_i/m_i has nonnegative2-adic valuation.
Exact proportionality therefore forbids an odd factor and an even
factor from occurring in the same squarefree class. This separation
holds for every factor cutoff, not only the original a<S^2 cutoff.

An odd-factor class has all its normalized n_i odd, so phase beta=1/2
satisfies

\[
                            \|n_i\beta\|=1/2>1/M.
 \tag{6}
\]

In an even-factor class every m_i is divisible by S/2, since S is a
power of two. Their gcd is also divisible by S/2. Equation(3) gives

\[
                         1\le n_i\le {2m_i\over S}<M-1.
 \tag{7}
\]

Choose beta=1/(M-1) in this class. Then

\[
                  \|n_i\beta\|\ge1/(M-1)>1/M.
 \tag{8}
\]

There are finitely many radical frequency lists and target residues.
The continuous radical flow can therefore choose one bounded time
approaching Q_d/M+beta_d modulo1 for every class simultaneously.
Set tau equal to that time divided by2sqrt(V)/S. The approximation
errors and tau tend uniformly to zero, while (6)--(8) have a fixed
positive margin. Thus

\[
                            \|\tau d-q/M\|>1/M
 \tag{9}
\]

for every actual rank difference associated with a candidate gap.
This is the certified Beatty criterion, proving the theorem.

The necessary flow argument and the floor-increment verification are
proved in the [thin-block note](continuation_large_offset_beatty_solvability.md).
Alternatively, (6)--(8) are exactly the zero-error special case of the
[residue-aware gap-menu criterion](continuation_approximate_gap_menu_beatty.md).

The asymptotic sufficient condition is

\[
               |T|\ge\left({M^2\over2(M-1)^2}+\epsilon\right)s^4.
 \tag{10}
\]

For M=3,4,5 the leading coefficients are9/8,8/9,25/32 respectively.
Consequently, for each fixed epsilon>0, a sufficiently large fixed
palette solves every ordered tile with |T|>=(1/2+epsilon)s^4, once s
is sufficiently large. The palette depends on epsilon, not on s.

This theorem does not settle the canonical per-scale systems, whose
large pieces have much smaller offsets. It also does not supply
occupied singleton fillers or validity against the other support
families. The actual-order K4 and K5 obstructions concern smaller
offset regimes and are compatible with this statement.

## Review status

The complete note passed an independent written review. The review checked
the even-class multiplier divisibility, both open phase margins, uniform
finite-target approximation, and the stated offset coefficients.
