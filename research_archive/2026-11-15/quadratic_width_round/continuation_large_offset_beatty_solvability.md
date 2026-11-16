# Three private choices solve sufficiently thin large-offset blocks

15 November 2026. This is a positive result for the original candidate P
system with S=32 and M=3. It allows more than two distinct slot gaps.
Its input is a large row offset compared with the fourth power of the
block side. The proof turns bounded Pythagorean half-factors into exact
odd-multiple gap classes, then chooses one certified Beatty rule for all
of them.

The theorem concerns the private-slot constraints only. It does not
supply occupied fillers, boundary-list extensions, or a solution of all
four per-scale Gamma/Omega systems.

## 1. Statement

Consider the side-s Cartesian tile with raw coordinates
(I+i,J+j), 0<=i,j<s, in any ordering on s^2 consecutive ranks. Its rows
are2(I+i)+1 and2(J+j)+2. A contiguous Hilbert block in either orientation
is one instance; no Hilbert property is needed for this theorem.
Put

\[
 T=J-I,\quad V=|2T+1|,\quad Q=3s^2-1,
 \quad Y_{\min}=V-2(s-1).
 \tag{1}
\]

Keep uncompressed ranks and the candidate constraints

\[
 q=3d+\delta>0,\quad|\delta|\le2,
 \qquad (32q)^2+Y^2=L^2,
 \tag{2}
\]

for either cross-parity role of two labels at rank difference d>=1.
There is no strip or owner restriction in this candidate system.

**Theorem.** There is an absolute s0 such that, whenever s>=s0 and

\[
                         Y_{\min}\ge Q^2/4,
 \tag{3}
\]

the whole candidate system has a certified three-choice solution of
the form

\[
                         \xi(r)=\lfloor3\tau r+c\rfloor\pmod3
 \tag{4}
\]

for one real tau and every real phase c. The values are represented in
{0,1,2}. The same rule satisfies every subset of these constraints.

Condition (3) is asymptotically |T|>=(9/8+o(1))s^4. In particular, for
each fixed positive epsilon, |T|>=(9/8+epsilon)s^4 implies the theorem
for all sufficiently large s.

The proof is effective in principle: it uses finitely many simultaneous
approximation targets for a fixed finite set of square roots. No useful
numerical bound for s0 is asserted.

## 2. Only bounded half-factors occur

Every internal rank difference is at most s^2-1, hence q<=Q. Let Y be
the absolute cross-row difference. It satisfies|Y-V|<=2(s-1). Let

\[
                         a=(L-Y)/2,
 \qquad                    b=(L+Y)/2=Y+a.
 \tag{5}
\]

The letters a,b in this section are half-factors, not row indices.
They are positive integers of opposite parity and

\[
                ab=256q^2,
 \qquad a={256q^2\over Y+a}<{256Q^2\over Y_{\min}}\le1024.
 \tag{6}
\]

Thus every smaller half-factor belongs to{1,...,1023}. If a is even,
b is odd, so

\[
                         v_2(a)=8+2v_2(q).
 \tag{7}
\]

Since a<1024, this forces q odd and a equal to256 or768. All other
possible half-factors are odd.

## 3. Approximate square-root gaps become exact proportional classes

Define

\[
                            \lambda={\sqrt V\over16}.
 \tag{8}
\]

Equation (6) gives

\[
 q={\sqrt{a(Y+a)}\over16}
             =\lambda\sqrt a+e,
 \qquad |e|\le E_s:={4(2s+1023)\over3s^2-1}.
 \tag{9}
\]

To check the bound, rationalize the two square roots. Their difference
is at most sqrt(a)(2(s-1)+a)/(16sqrt V). Use sqrt(a)<32 and
sqrt V>=Q/2. These give (9) with room to spare.

For s>=512, 62E_s<1. First, a fixed half-factor has at most one candidate
integer gap q, since two such integers differ by at most2E_s<1.

Now fix a squarefree class d. Write every observed half-factor in that
class as a_i=d m_i^2, with m_i<=31. If its gap is q_i, then

\[
                    |m_jq_i-m_iq_j|
                       \le(m_i+m_j)E_s<1.
 \tag{10}
\]

The expression is an integer. Therefore q_i/m_i is exactly constant
within the observed class.

Let g_d=gcd_i m_i and write n_i=m_i/g_d. There is an integer Q_d such
that

\[
               q_i=n_iQ_d,
 \qquad Q_d=\lambda g_d\sqrt d+O(E_s).
 \tag{11}
\]

Integrality does not require the squarefree factor d itself to occur.
Choose integer coefficients with sum_i z_i m_i=g_d. Then
Q_d=sum_i z_i q_i; equivalently Q_d=g_d q_i/m_i. The approximation
error in this latter formula is at most E_s.

Every n_i in (11) is odd. If all a_i are odd, all m_i and their gcd
are odd. The only even possibilities are256=16^2 and768=3*16^2.
Such a factor cannot share its observed class with an odd factor:
q_even/16 has2-adic valuation-4 by (7), whereas q_odd/m_odd has
nonnegative2-adic valuation. This contradicts the exact equality just
proved. Hence a class containing an even factor consists of that one
factor, and its reduced multiplier is1.

This parity fact is the key distinction from an arbitrary bounded gap
set. Arbitrary three-gap systems can already be unsatisfiable with
three choices.

## 4. A simultaneous phase for all classes

Use the elementary continuous Kronecker fact: if alpha_1,...,alpha_r
are linearly independent over the rationals, the positive-time orbit

\[
              (t\alpha_1,...,t\alpha_r)\pmod1
 \tag{12}
\]

meets every nonempty open box in the r-torus.

For completeness, average a continuous nonnegative bump supported in
that box along the orbit. Approximate it uniformly by trigonometric
polynomials. Every nonconstant Fourier term has time average zero
because its frequency is a nonzero integer combination of the alpha_i.
The limiting average is the positive integral of the bump. This proves
the assertion. Distinct squarefree radicals sqrt(d) are rationally
independent: in their multiquadratic field, the sign automorphisms and
their characters isolate each coefficient of a proposed relation.

Let B=31 and eta=1/(24B). Apply (12) to the frequencies
g_d sqrt(d)/3, one per observed squarefree class, and the target phases

\[
                            Q_d/3+1/2\pmod1.
 \tag{13}
\]

There are only finitely many possible collections of d,g_d and residues
Q_d modulo3, because all half-factors are below1024. For each collection
choose one positive time t whose coordinate errors are below eta/2.
Taking the maximum over this finite list gives a finite universal T_*.

Set tau=t/lambda. Equation (11) implies, for sufficiently large s,

\[
            \left\|{\tau Q_d\over3}-{Q_d\over3}-{1\over2}
                    \right\|<\eta,
 \qquad                 0<\tau\le1/24.
 \tag{14}
\]

Indeed, the new phase error is at most T_*E_s/(3lambda), which tends
to zero uniformly. Also lambda>=Q/32 grows quadratically in s.
The choice of s0 can incorporate both requirements and s0>=512.

Since q_i=n_iQ_d with n_i odd and n_i<=31, (14) gives

\[
                   \left\|{\tau q_i\over3}-{q_i\over3}\right\|
                                >1/2-31\eta=11/24.
 \tag{15}
\]

This is an open-margin construction. It is not an appeal to a generic
irrationality assertion about the large integer gaps themselves.

## 5. Verification of the private-slot constraints

For a constraint with gap q and rank difference d_r, the relation
q=3d_r+delta gives|d_r-q/3|<=2/3. Therefore (14)--(15) imply

\[
 \left\|\tau d_r-{q\over3}\right\|
 \ge {11\over24}-{2\tau\over3}
 \ge {11\over24}-{1\over36}={31\over72}>{1\over3}.
 \tag{16}
\]

This is exactly the certified Beatty criterion. To see it directly,
the integer increment

\[
 \lfloor3\tau(r+d_r)+c\rfloor-\lfloor3\tau r+c\rfloor
 \tag{17}
\]

is either floor(3tau d_r) or ceil(3tau d_r). If it were congruent to q
modulo3, the distance from3tau d_r to q+3Z would be less than1.
That contradicts (16). Thus xi(r+d_r)-xi(r) is not congruent to q,
and in particular is not the forbidden integer delta.

The argument works for every rank and every phase c. It proves the
theorem for the whole candidate graph, independently of which labels
realize each allowed gap.

The same Beatty criterion appears in the archived
[two-gap proof](../../2026-11-14/gap_mixing_two_gap_beatty.md).
The new input here is the square-root rigidity and its odd-multiple
class structure, which permits a bounded menu containing many gaps.

## 6. Scope for the per-scale problem

This result handles an actual infinite large-offset regime of block
types. It does not solve all fixed per-scale Gamma/Omega systems:
their large pieces also contain regions with |T| of order s, rather
than s^4. Nor can independently chosen formulas for arbitrary adjacent
blocks be combined unless their crossing constraints are controlled.

The finite omitted values s<s0 are not certified by the proof. The
large-offset condition and bounded q do leave only finitely many
nontrivial offsets for each such s, but no computation of that finite
remainder is claimed.

Finally, private choices create unoccupied positions. All questions
about their singleton fillings, other forbidden supports, and collars
remain separate. This is a certified P-choice theorem, not a completed
blackout construction.

The current occupied scaffold already removes all bounded smaller
half-factors through its growing factor cutoff. Thus this theorem does
not remove a new family from that scaffold's residual P graph. Its
positive contribution is to the original all-offset private-slot
problem and to the reusable gap-menu lemma that follows.

## 7. The abstract odd-multiple gap-menu lemma

Fix M>=3, an integer B, and positive rationally independent real
numbers alpha_1,...,alpha_r. Suppose an integer gap menu, indexed by
lambda tending to infinity, has the form

\[
 q_{j,l}=n_{j,l}Q_j,\qquad
 1\le n_{j,l}\le B\text{ odd},\qquad
 Q_j/\lambda\longrightarrow\alpha_j.
 \tag{18}
\]

Then, for all sufficiently large lambda, one Beatty rule

\[
                      \xi(r)=\lfloor M\tau r+c\rfloor\pmod M
 \tag{19}
\]

satisfies every certified private-slot constraint with these gaps,
for every phase c. The threshold depends on the convergence modulus in (18). The assertion
is uniform over a fixed finite collection of frequency lists and
odd-multiplier patterns when the errors in (18) tend to zero uniformly.

Indeed, put mu=1/2-1/M>0 and eta=mu/(4B). The continuous flow with
frequencies alpha_j/M can approach each of the finitely many target
vectors Q_j/M+1/2 modulo1 within eta/2. Select a bounded positive
time t for each residue vector and put tau=t/lambda. For large lambda,
(18) makes each base phase lie within eta of1/2 and makes tau<mu/4.
Every odd multiple has distance at least1/2-B eta from the integers.
Replacing q/M by the actual rank difference changes its phase by less
than tau. The resulting distance exceeds1/M, which is precisely the
general certified Beatty criterion.

No conclusion is asserted when an exact gap class has both odd and
even reduced multipliers. In particular, arbitrary bounded gap menus
are not covered by this lemma.

## 8. Every fixed power-of-two stride and palette size

Fix a power of two S>=4 and an integer M>=3. For any ordering of the
same side-s tile, replace (1)--(2) by

\[
 Q=Ms^2-1,\qquad q=Md+\delta>0,\quad |\delta|\le M-1,
 \qquad (Sq)^2+Y^2=L^2.
 \tag{20}
\]

For all sufficiently large s, depending only on S and M, the condition
Y_min>=Q^2/4 again gives a certified solution with M choices.

Here the half-factor identity and cutoff become

\[
 ab={S^2q^2\over4},\qquad a<S^2.
 \tag{21}
\]

If a is even, b is odd and

\[
 v_2(a)=2v_2(S)-2+2v_2(q).
 \tag{22}
\]

Thus q is odd, and the only even possibilities are S^2/4 and3S^2/4.
Their square-root multipliers are S/2, whereas an odd half-factor has
an odd multiplier. Exact proportionality excludes coexistence of the
even and odd cases within one squarefree class: their rational ratios
q/m have respectively negative and nonnegative2-adic valuations.
Each observed class therefore again has only odd reduced multipliers,
bounded by S-1.

To justify exact proportionality, use

\[
 \lambda={2\sqrt V\over S},\qquad
 |q-\lambda\sqrt a|
 \le {4(2s+S^2)\over Ms^2-1}=O_{S,M}(s^{-1}).
 \tag{23}
\]

The products of this error by any two multipliers tend uniformly to
zero. The integer argument (10), the gcd normalization (11), and the
finite list of rationally independent square-root frequency families
apply unchanged. Section7 then proves the claimed M-choice solution.
In particular, the asymptotic sufficient regime is
|T|>=(M^2/8+epsilon)s^4 for any fixed epsilon>0. This remains a
private-slot theorem; the additional construction questions in
Section6 are unchanged.

## Review status

The full S=32,M=3 proof, its all-order scope, and the abstract lemma
passed three independent written reviews. The reviews checked the
half-factor cutoff, exact proportionality without requiring a smallest
observed factor, normalized multiplier parity, uniform finite-target
approximation, and every certified constraint. The general fixed-S,M extension in Section8 also passed an independent
written review.
