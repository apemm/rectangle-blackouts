# Approximate gap menus and a quantitative thin-block regime

15 November 2026. The private-slot Beatty construction tolerates small
errors in proportional gaps only when their residues leave a common
open phase interval. The first theorem states that condition exactly.
A second, quantitative theorem allows a slowly growing half-factor menu
under the odd-normalized-multiplier hypothesis. Neither theorem settles
the unrestricted three-choice problem or supplies occupied fillers.

The starting point is the certified criterion from
[the thin-block theorem](continuation_large_offset_beatty_solvability.md):
for q=Md+delta, |delta|<=M-1, the choice

\[
 \xi(r)=\lfloor M\tau r+c\rfloor\pmod M
 \tag{1}
\]

avoids the constraint for every phase c when

\[
                    \|\tau d-q/M\|>1/M.
 \tag{2}
\]

## 1. Errors modulo M survive the limit

Fix M>=3. Suppose a fixed finite menu is described by

\[
 q_{j,l}=n_{j,l}Q_j+e_{j,l},\quad
 1\le n_{j,l}\le B,\quad
 Q_j/\lambda\longrightarrow\alpha_j>0,
 \quad\max|e_{j,l}|=o(\lambda),
 \tag{3}
\]

where Q_j and e_(j,l) are integers and the alpha_j are rationally
independent. The integer multipliers
and error residues modulo M may vary over a fixed finite collection.
Assume that for every occurring residue pattern there are phases
beta_j and one common gamma>0 such that

\[
 \left\|n_{j,l}\beta_j-e_{j,l}/M\right\|
                       \ge 1/M+\gamma
 \quad\hbox{for every }j,l.
 \tag{4}
\]

Then all constraints in this gap menu have a common certified solution
(1) for sufficiently large lambda, uniformly when the convergence in
(3) is uniform over the finite collection.

To prove this, use the continuous irrational flow to choose a bounded
positive time t so that

\[
              t\alpha_j/M\approx Q_j/M+\beta_j\pmod1.
 \tag{5}
\]

Only finitely many target patterns occur. Set tau=t/lambda. Write
q=nQ+e and use the exact identity

\[
 \tau d-q/M
   =n(\tau Q/M-Q/M)-e/M+\tau e/M+\tau(d-q/M).
 \tag{6}
\]

The first term approaches n beta, the third tends uniformly to zero,
and the last has absolute value less than tau. Choose the fixed flow
accuracy below gamma/(4B), then take lambda large. Equations(4) and(6)
give (2). This also proves the assertion for negative errors.

Errors divisible by M are therefore harmless when all n are odd:
choose beta=1/2. More generally, (4) is a finite open-interval
feasibility test on each circle. Its interval endpoints are rational,
so no numerical approximation is needed to test a fixed pattern.

Arbitrary bounded errors do not suffice. For M=3, take a common base
Q=3d and the three gaps Q-1,Q,Q+1. Their constraints at the same rank
difference d forbid all three residues of xi(r+d)-xi(r). Thus no
certified coloring exists. Equivalently, the three residues
-1,0,1 with n=1 leave no phase satisfying(4). This is a statement
about certified modular constraints. It does not assert that the
corresponding finite actual-integer system is unsatisfiable, or that
this whole abstract pattern is realized by one geometric tile.

## 2. A uniform elementary time bound for radical phases

Here is the quantitative form of the flow argument. Let A>=2 be an
integer, and let

\[
 \alpha_j=g_j\sqrt{d_j},\qquad
 d_j\text{ distinct squarefree},\quad
 g_j\in\mathbb Z_{>0},\quad g_j^2d_j\le A.
 \tag{7}
\]

For fixed M>=3, any prescribed targets in the r-dimensional torus,
and eta=c_M/sqrt(A) with a fixed c_M>0 sufficiently small, a time
0<t<=T reaches every target within eta, where

\[
                   \log T\le C_M\,2^A A\log(A+2).
 \tag{8}
\]

All constants are independent of the selected radical list and the
targets. The bound is deliberately crude.

For a direct proof, put a periodic triangular bump of support radius eta about
each target and multiply the r bumps. Each bump has mean eta, Fourier
coefficient magnitude

\[
            \eta\,\left({\sin(\pi k\eta)\over\pi k\eta}\right)^2,
 \tag{9}
\]

and total absolute Fourier mass1. Its tail at |k|>K is at most
C/(eta K). The product has mean eta^r, absolute Fourier mass1, and
box-truncation tail at most Cr/(eta K). Take

\[
                     K=\left\lceil C r\eta^{-(r+1)}\right\rceil
 \tag{10}
\]

with a sufficiently large absolute C, so the tail is below eta^r/8.

For any nonzero integer vector k with |k_j|<=K, the number
z=sum_j k_j g_j sqrt(d_j) is a nonzero algebraic integer. It lies in
a multiquadratic field of degree D<=2^A. Every conjugate has magnitude
at most rK sqrt(A). Its nonzero integer norm therefore gives

\[
 |z|\ge(rK\sqrt A)^{-(D-1)},\qquad
 \left|\sum_j k_j\alpha_j/M\right|
 \ge {1\over M}(rK\sqrt A)^{-(D-1)}=:\kappa.
 \tag{11}
\]

Average the truncated Fourier polynomial along t alpha/M over [0,T].
Its nonconstant terms have total average magnitude at most2/(T kappa).
Taking T>=16/(kappa eta^r) makes this below eta^r/8. The original
product bump then has positive time average, so the orbit enters its
support. Since r<=A, (10)--(11) give (8). This proof uses only the
Fourier series of a triangular bump and the integer algebraic norm.

## 3. A slowly growing factor menu

Fix a power-of-two S>=4 and M>=3. Consider any ordering of a side-s
Cartesian label tile with odd/even rows2(I+i)+1 and2(J+j)+2. Use the
candidate norm constraints

\[
 q=Md+\delta>0,\quad |\delta|\le M-1,\quad
 (Sq)^2+Y^2=L^2,
 \quad Q=Ms^2-1,
 \tag{12}
\]

where Y is the absolute cross-row difference. As before, put
V=|2(J-I)+1| and Y_min=V-2(s-1).

Let A=A(s) be an integer with

\[
 2\le A\le\log\log s,\qquad
                    Y_{\min}\ge {S^2Q^2\over4A}.
 \tag{13}
\]

All logarithms in this note are natural. The smaller half-factor
satisfies a=(L-Y)/2<A. Partition the observed factors by their
squarefree parts: a_i=d m_i^2. In each observed class, divide the
multipliers by their gcd. Assume that all the resulting multipliers
are odd.

**Theorem.** Under these hypotheses, for all sufficiently large s,
one M-choice Beatty rule solves the entire candidate system, in every
ordering of the tile. The threshold is uniform for A in(13).

First, put lambda=2sqrt(V)/S. Rationalizing the two square roots gives

\[
 \left|q-\lambda\sqrt a\right|
 \le {4A(2s+A)\over S^2Q}=:E_s,
 \qquad \lambda\ge Q/\sqrt A.
 \tag{14}
\]

Thus E_s=O_{S,M}(A/s), and2sqrt(A) E_s tends to zero. The integer
comparison

\[
                 |m_jq_i-m_iq_j|\le2\sqrt A\,E_s<1
 \tag{15}
\]

makes each squarefree class exactly proportional. Gcd normalization
therefore gives integers Q_d and odd n_i<=sqrt(A) with

\[
 q_i=n_iQ_d,\qquad
                 |Q_d-\lambda g_d\sqrt d|\le E_s.
 \tag{16}
\]

The argument does not require the smallest factor in the class to be
observed. It is the same integer/Bézout argument used in the fixed-menu
proof.

Let mu=1/2-1/M>0 and take eta=mu/(16sqrt(A)). Apply Section2 to
frequencies g_d sqrt(d)/M and targets Q_d/M+1/2, with accuracy eta.
Condition A<=loglog s makes its time bound satisfy

\[
 \log T\le C_M(\log s)^{\log2}\log\log s\log\log\log s
                         =o(\log s),
 \qquad T=s^{o(1)}.
 \tag{17}
\]

Set tau=t/lambda. The error in replacing t g_d sqrt(d)/M by
 tau Q_d/M is at most T E_s/(M lambda)=s^{-3+o(1)}, and
 tau=s^{-2+o(1)}. Both estimates are uniform in (13). Multiplying
the phase error by n_i<=sqrt(A) still leaves a fixed open margin:

\[
             \|\tau q_i/M-q_i/M\|\ge1/2-\mu/4
 \tag{18}
\]

for all sufficiently large s. Finally |d-q/M|<1, so replacing q/M
by d changes the phase by less than tau. Equations(18) and(2) finish
the proof.

A simple sufficient condition for the multiplier hypothesis is that
all candidate gaps q have the same2-adic valuation. Exact
proportionality makes their reduced multipliers have the same2-adic
valuation; because those multipliers have gcd1, that valuation is zero.
This is sufficient, not necessary.

## 4. What this extends, and what remains

Taking A comparable to loglog s reaches row offsets of order
s^4/loglog s, under the stated odd-multiplier condition. The fixed-menu
theorem supplies that condition automatically below a<S^2; it need
not hold for a growing menu. There is no conclusion here for arbitrary
mixed even/odd multiplier classes, no advance to the critical
|T| of order s^2, and no occupied-filler construction.

The first theorem identifies the exact obstruction to simply absorbing
bounded proportionality errors: their residues modulo M persist even
when their sizes are negligible compared with the main gaps. A future
extension needs either a proof of the finite phase condition(4), or a
coloring construction that does not use one global Beatty slope.

## Review status

The complete note passed two independent written reviews. The reviews
checked the residue terms, Fourier tail and absolute mass, algebraic norm
bound, and uniform slowly growing-menu estimates.
