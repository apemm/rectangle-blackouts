# Divisibility improves the factor cleanup and the remaining P gap

15 November 2026. Using the divisibility in the Pythagorean equation improves
the exceptional-label count to
\[
 |E_A|\le C h^{7/4}A^{3/4}\log(2A).                         \tag{1}
\]
The previous elementary bound had \(A^{7/4}\). With the audited odd-stub
implementation, a half-factor cutoff \(A=h^{1/3-o(1)}\) fits the quadratic
budget while preserving occupied cores. Combined with the growing triangular
band, every remaining genuine in-strip P event has slot gap
\(q\ge h^{2/3-o(1)}\).

This is a stronger conditional construction reduction. It does not assign
the remaining permutations or avoid long P, \(\Lambda_3,\Lambda_4\), R2s,
and 6PT simultaneously.

## 1. A uniform physical-locality formulation

Consider one of the fully occupied ordinary cores, with fixed even stride
\(S\). Suppose every allowed choice of its bounded tile permutations obeys
\[
 |a_e-a_f|, |b_e-b_f|\le C_0\sqrt q                       \tag{2}
\]
when the two occupied slots have distance \(q\). The two physical rows of
label \(e\) are the odd row \(a_e\) and the even row \(b_e\).
The packed triangular cores, including their random physical-pack variants,
have such a height-independent constant \(C_0\).

For a P candidate with vertical magnitude \(Y<h\) and hypotenuse \(L\),
put
\[
 a=(L-Y)/2\in\mathbb Z_{>0}.
\]
The horizontal leg is \(Sq\), so
\[
 a(Y+a)=(Sq/2)^2,\qquad
 Y=\frac{(Sq/2)^2}{a}-a.                                   \tag{3}
\]
For every integer \(a\le A\le h\) and every positive integer
\[
 q\le\frac{2\sqrt{a(h+a)}}{S},
\]
retain only the values for which (3) gives an odd integer \(0<Y<h\).
Put in \(E_A\) every label whose own signed row gap \(b_e-a_e\) is within
\(C_0\sqrt q+1\) of \(Y\) or \(-Y\), for one retained pair \((a,q)\).

Equation (2) shows that both source labels of every P candidate with
half-factor at most \(A\) belong to \(E_A\). This construction of \(E_A\)
is uniform over the allowed tile permutations. A band for one \((a,q)\)
contains \(O(\sqrt q+1)\) integer row gaps, each supporting at most \(h\)
distinct parity labels.

## 2. Keep the square-divisibility restriction

Write uniquely
\[
 a=u v^2,\qquad u\text{ squarefree}.
\]
Put \(K=S/2\), a fixed positive integer. Then
\[
 a\mid(Kq)^2
 \quad\Longleftrightarrow\quad uv\mid Kq
 \quad\Longleftrightarrow\quad
 d_a:=\frac{uv}{\gcd(uv,K)}\mid q.                          \tag{4}
\]
The first equivalence follows prime by prime: if the exponent of a prime
in \(a\) is \(e\), its required exponent in \(Kq\) is \(\lceil e/2\rceil\).
In particular \(d_a\ge uv/K\).

For any \(Q\ge1\),
\[
 \sum_{\substack{1\le q\le Q\\d_a\mid q}}(\sqrt q+1)
 \le C\frac{Q^{3/2}}{d_a}.                                 \tag{5}
\]
If \(Q<d_a\) the sum is zero. Otherwise write \(q=d_a j\), use
\(\sqrt q+1\le2\sqrt q\), and sum \(\sqrt j\) up to \(Q/d_a\).

Since \(A\le h\), the bound on \(q\) in Section 1 is
\(Q=O_S(\sqrt{ah})\). The band count and (5) therefore give
\[
 |E_A|\le C_{S,C_0}h^{7/4}
          \sum_{a\le A}\frac{a^{3/4}}{uv}.                  \tag{6}
\]
Finally,
\[
 \begin{aligned}
 \sum_{a\le A}\frac{a^{3/4}}{uv}
 &=\sum_{v\le\sqrt A}v^{1/2}
       \sum_{\substack{u\le A/v^2\\u\text{ squarefree}}}u^{-1/4}\\
 &\le C\sum_{v\le\sqrt A}v^{1/2}(A/v^2)^{3/4}\\
 &\le C A^{3/4}\log(2A).
 \end{aligned}                                             \tag{7}
\]
This proves (1). No average divisor theorem is used.

## 3. Fit the stronger cutoff within the relocation budget

Let \(T(h)\ge1\), with \(T(h)=h^{o(1)}\), be the factor in the cited
exceptional-label internal width estimate \(O((n_E+1)T(h)^2)\).
Set \(\Lambda=\log(2h)\), and choose any fixed \(\eta>0\). For all
sufficiently large \(h\), take
\[
 A(h)=\left\lfloor
       \frac{\eta h^{1/3}}{T(h)^{8/3}\Lambda^4}
       \right\rfloor.                                     \tag{8}
\]
Then \(A=h^{1/3-o(1)}\), \(1\le A\le h\), and
\[
 |E_A|T(h)^2\le C\frac{h^2}{\Lambda^2}=o(h^2).              \tag{9}
\]
Indeed \(A^{3/4}\le C h^{1/4}/(T(h)^2\Lambda^3)\), and
\(\log(2A)\le C\Lambda\).

Use the audited operation from
[`continuation_odd_stub_exception_repair.md`](continuation_odd_stub_exception_repair.md):
erase the odd point of every label in \(E_A\), retain its even singleton
stub in its original arithmetic slot, and relocate the complete pair
externally. The targeted P candidates lose their odd endpoint. No row-\(F\)
point is restored, so the occupied-core FW argument survives. The final
excess is exactly restored, and every surviving even stub must still be
included in the residual P and mixed-support tests.

The count (9) concerns the internal relocation cost. The cited filled
collars, external-window validity relative to the full final row-pair graph,
and avoidance of the surviving core families remain separate inputs.

## 4. Every remaining actual P gap is at least h to the two-thirds scale

Use the growing triangular band with
\[
 Q_0(h)=\left\lfloor\frac{\eta_0\sqrt h}{T(h)\Lambda}\right\rfloor,
 \qquad c_h\asymp Q_0(h)^2
       \asymp\frac{h}{T(h)^2\Lambda^2}.                    \tag{10}
\]
The constants depend on the fixed stride and row-profile data. In the random
pack version, its additional \(O(\sqrt h\log h)\) discrepancy term is
\(o(Q_0(h)^2)\), so the same asymptotic comparison holds.

Now consider a genuine P event whose two alternative vertical corners lie
in the height-\(h\) strip. Their separation is \(L\le h-1\), hence
\(X=Sq\le h-1\). The two macrotiles consequently have rank distance
\(O(h)\). Triangular locality gives coordinate-index displacement
\(O(\sqrt h)\).

Within one retained upper or lower triangle, the cross-coordinate separation
is therefore at least \(c_h-O(\sqrt h)\). For random color lists the
additional discrepancy is \(O(\sqrt h\log h)\). Both errors are \(o(c_h)\).
The physical pack lists are strictly increasing with their fixed minimum
spacing, so for an absolute positive constant depending on the scaffold,
\[
 Y\ge c_1c_h
   \ge c_2\frac{h}{T(h)^2\Lambda^2}.                       \tag{11}
\]

After the stub erasure, the remaining event also has \(a>A(h)\). Equation
(3) gives
\[
 q=\frac{2\sqrt{a(Y+a)}}{S}
   \ge c_3\frac{h^{2/3}}{T(h)^{7/3}\Lambda^3}
   =h^{2/3-o(1)}.                                          \tag{12}
\]
There is a useful second separation from a degenerate direction:
\[
 L-X=\frac{Y^2}{L+X}
 \ge c_4\frac{h}{T(h)^4\Lambda^4}
 =h^{1-o(1)}.                                              \tag{13}
\]

Equations (11)–(13) use the actual in-strip condition. They are not claimed
for the larger candidate graph whose alternative vertical corners may lie
outside the board. The factor deletion itself, Sections 1–3, covers that
larger graph as well.

The reduction leaves a precise long-gap, large-factor P regime. It does not
bound its degree, its coloring number, or its permutation solvability.
The other four residual families remain, and no complete quadratic-width
construction is asserted.

Independent review: the complete written proof passed a separate audit,
including the primewise identity (4), the empty-sum case in (5), the
squarefree sum, all relocation exponents, and the actual-versus-candidate
scope of (11)–(13). The preceding odd-stub implementation is independently
reviewed in its own note.
