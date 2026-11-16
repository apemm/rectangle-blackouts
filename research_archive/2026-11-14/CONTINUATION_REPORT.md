# Quadratic-width continuation

14 November 2026. These are research results and independently checked
arguments, not refereed results. No change to the paper is proposed here.

## Main result and current status

There is a new deterministic placement of all labels in width \(O(h^2)\)
that excludes the entire same-parity integral-distance family responsible
for the independent-relocation price floor. It preserves a constant
number of private column choices per label. Within this placement, two
choices eliminate every opposite-parity rival whose smaller Pythagorean
half-factor is one. More generally, any \(R\) prescribed half-factors can
be eliminated with \(4R+1\) choices and width \(O(Rh^2)\).

These are placement theorems, not a complete blackout construction.
All opposite-parity factors at constant cost, mixed supports, and
all-label right angles are still unresolved. The current full-board
bound therefore remains the 13 November stride-menu bound

\[
m_h\le C_\varepsilon h^2(\log h)^{1.3108172+\varepsilon}.
\]

No improvement to that exponent, no proof of \(m_h=O(h^2)\), and no
new counting formula are claimed in this continuation.

## 1. A deterministic way around the relocation price floor

Index a label by its two black rows \(2i+1,2j+2\). Pad the label grid
to a power-of-two square of side \(Q=O(h)\), and let \(r(i,j)\) be its
discrete Hilbert rank. Keep these original ranks when taking subsets.
The recursion gives

\[
\max\{|i-i'|^2,|j-j'|^2\}<16|r-r'|.                 \tag{1}
\]

Place label \(e\) at

\[
x_e=S(Mr_e+\xi_e),\qquad 0\le\xi_e<M,\quad S=32.   \tag{2}
\]

Any choices retain \( |x_e-x_f|\ge32|r_e-r_f| \).
For a nonhorizontal pair of black points of the same parity, write
\(X=|x_e-x_f|\) and \(Y\) for its row difference. Then

\[
0<Y^2<64|r_e-r_f|\le2X,
\]

so \(X^2+Y^2\) lies strictly between consecutive squares \(X^2\) and
\((X+1)^2\). No such pair has integral distance. The span is below
\(32MQ^2\), which is \(O(h^2)\) for fixed \(M\).

In particular this excludes every configuration in Lemma F of the
[relocation price-floor note](../2026-11-13/relocation_price_floor.md),
regardless of the sea row.
It also excludes a tilted right angle whose three black points have
one physical row parity. The remaining cross-parity cases require
separate arguments.

This does not contradict the independent-slot lower bound. Each label
now has only \(M\) private nearby choices, rather than a positive
fraction of all slots. Consequently the previous broad-list collision
estimates cannot be imported for the other support families.

The same construction works in a period-seven profile. For endpoint
progressions of step \(d=14\), use \(S=8d^2=1568\). All chosen columns
are multiples of seven, the same-parity exclusion survives, and the
existing one-label filler argument applies. Remaining multi-label
supports and the hypotheses needed for gluing still have to be checked.

Proof: [Hilbert placement](continuation_hilbert_placement.md).
Independent review: [placement audit](continuation_hilbert_independent_audit.md).

## 2. Two choices solve one full arithmetic family

For an opposite-parity pair with integral length, write

\[
Y=|y|,\qquad a=(L-Y)/2,\quad b=(L+Y)/2,\quad ab=X^2/4.
\]

Here \(a\) is the smaller half-factor. The case \(a=1\) has

\[
Y=X^2/4-1.
\]

Consider the candidate graph formed using **all** allowed choices in
(2), before making an assignment. A candidate absolute slot gap is

\[
q=M|r_e-r_f|+\delta>0,\qquad X=S q.
\]

For a focal label, set \(T=j-i\). Each cross-parity role gives

\[
T=\epsilon\frac{S^2q^2}{8}
  -\frac{\epsilon+1}{2}-z,
\qquad |z|<4\sqrt q.                              \tag{3}
\]

For \(S\ge8\), the difference between two distinct quadratic values
in (3) exceeds the total Hilbert-coordinate error. Opposite signs
cannot occur either. Thus every candidate edge at a label has the
same \(q\), and every nontrivial candidate component has a common \(q\).

Set \(M=2\). On an odd-\(q\) component, choose every \(\xi=0\); all
actual slot differences are then even. On an even-\(q\) component,
put \(d_0=q/2\) and choose

\[
\xi_e=\lfloor r_e/d_0\rfloor\pmod2.
\]

Candidate edges have rank difference \(d_0\), so their endpoints
receive opposite choices and their actual gap differs from \(q\).
This eliminates every factor-one pair, including candidates whose
vertical completion is outside the strip. The theorem retains all
labels and works for arbitrary subsets.

This is a general proof for every height. It is separate from the
finite three-choice evidence below.

## 3. Any finite set of factors has linear cost

The stronger comparison fixes a factor, a cross-parity role, and one
horizontal side of the focal label. If two candidate gaps are
\(q_1>q_2\), let \(\Delta=q_1-q_2\). Their hypothetical assignments
may use different choices even at the focal label. Nevertheless the
integer rank calculation gives

\[
|d_1-d_2|\le\Delta.
\]

The two partner coordinate errors therefore differ by at most
\(4\sqrt\Delta\). The smaller-factor condition \(Sq_i>2a\) makes
the difference of the two parabolic values strictly greater than
\((S/2)\Delta\ge4\Delta\). This is impossible. There is one candidate
gap for each fixed factor, role, and side, however large the factor is.

Each such gap permits at most two earlier ranks. With two roles,
each factor can forbid at most four choices at a greedy step.
Consequently \(M=4R+1\) eliminates any prescribed set of \(R\) factors.
The width at \(S=32\) is \(O(Rh^2)\).

Both the two-choice theorem and this finite-factor theorem extend to
the period-seven profiles. The general theorem there needs \(S\ge4d\),
which holds for \(d=14,S=1568\).

Proofs: [factor-choice theorems](continuation_hilbert_factor_one_choices.md).
Independent review: [factor-choice audit](continuation_hilbert_factor_choices_audit.md).

The restriction to a finite set is real. An explicit five-label
configuration using only factors \(1\) and \(245\) has no assignment
with two choices. This does not obstruct three or more choices.

## 4. What would turn this into an all-factor theorem

For a proposed fixed \(M\), build the full candidate constraint
multigraph. Let \(F^-_U(e;M)\) be the number of distinct smaller factors
witnessed by constraints from \(e\) to earlier vertices in an induced
subset \(U\). The new lemma proves

\[
b^-_U(e;M)\le4F^-_U(e;M).
\]

Either of the following is sufficient for an all-factor repair:

\[
M>4\max_eF^-_V(e;M),
\]

or

\[
M>8\max_{\varnothing\ne U\subseteq V}
  \frac1{|U|}\sum_{e\in U}F^-_U(e;M).              \tag{4}
\]

The second condition allows high-degree vertices provided no dense
constraint core survives. A bound on the global average alone is
insufficient. Both criteria retain their dependence on \(M\); neither
has been proved with a constant \(M\) uniformly in height.

A conservative unconditional estimate uses the \(O(\sqrt{h/M})\)
possible partner rows in a Hilbert neighborhood and divisor bounds
for each row. It gives \(M=h^{1/3+o(1)}\), hence a scaffold excluding
F and P at width \(h^{7/3+o(1)}\). This is a benchmark for the new
method, not a competitive full-board bound. It does not remove mixed
supports.

Details: [local factor budgets](continuation_hilbert_local_factor_budget.md).

## 5. Exact evidence and failed shortcuts

Three choices exclude all in-strip P candidates in the full label
family at \(h=2048\) and \(4096\). At \(4096\), the certificate has
695871 constraints on 877697 incident labels. An independent verifier
uses a different Hilbert algorithm and Euclid's parametrization;
it checks 360708252 opposite-parity pairs and passes.

All 58579 nonempty translated-offset groups for an identity-oriented
Hilbert patch of side 32 also admit three choices. Three groups have
weighted degeneracy three, so a universal degeneracy-below-three
argument already fails for the enlarged candidate system. Their
remaining cores are nevertheless exactly satisfiable.

These are P certificates only. They neither assemble a sea nor test
every other support. See [choice evidence](continuation_hilbert_choice_evidence.md).

Several simpler completion rules are now ruled out:

- The full binary local-choice problem has an exact obstruction:
  [two-choice certificate](continuation_hilbert_two_choice_obstruction.md).
- The unmodified Hilbert P graph has an actual triangle at \(h=4096\),
  which embeds at infinitely many heights. Its small-height
  bipartiteness was misleading.
- The unmodified order has an explicit recursive mixed collision
  and a black right angle at \(h=2S^4\):
  [recursive obstruction](continuation_hilbert_recursive_obstruction.md).
- Every rule using only fixed dyadic residues of the rank and label
  coordinates leaves a monochromatic black angle at some height:
  [dyadic obstruction](continuation_hilbert_dyadic_residue_obstruction.md).
  Fixed low-bit rules also fail for P:
  [P residue obstruction](continuation_hilbert_residue_obstruction.md).
- The four terminal Hilbert orientations alone also leave an exact
  black angle:
  [orientation obstruction](continuation_hilbert_orientation_obstruction.md).

These statements do not rule out arbitrary bounded colorings,
combined orientation-and-residue rules, or a constant-choice repair.

There is a positive but nonquadratic mixed-support theorem:
\(S^4\ge1024h\) excludes every genuine nonvertical mixed four-support.
At constant \(S\), mixed supports whose four black points all have
the same parity are excluded. The other parity cases remain. See
[mixed-support proof](continuation_hilbert_mixed_supports.md).
An [explicit abstract counterexample](continuation_holder_mixed_counterexample.md)
shows that the Hilbert distance estimate alone cannot resolve them.

## 6. The older Cayley route still has an assembly obligation

No polynomial saving in \(\chi(\operatorname{Cay}(\mathbb Z,D_T))\)
is proved here. A chromatic bound cannot simply replace a degree bound
in the existing random-coloring marginal estimate. The correct
alternatives are a suitable coloring distribution or a refinement
that also handles the auxiliary edges.

At stride four, the audited degree-capped refinement supplies such an
interface. If \(\chi\ll\kappa^\delta\), its conditional optimized
exponent is

\[
E_1(\delta)=\min_{a>0}
 \frac{\delta(3+3^a)}{2(\delta+a)}.
\]

For example \(E_1(1/2)=0.990421407\ldots\); any
\(\delta<0.776216335\ldots\) would beat the present menu exponent.
The premise is unproved. A corresponding menu consequence additionally
needs a transfer of the degree-capped argument to the new strides;
the existing menu audit does not cover that transfer.

See [coloring assembly](continuation_chi_assembly_requirements.md) and
[conditional payoffs](continuation_cayley_coloring_payoff.md).
A [generic graph obstruction](continuation_cayley_window_barrier.md)
shows that dyadic-window capacity \(M(D)\) and exclusion of all
relations up to a prescribed fixed length do not imply
\(\chi\le C M(D)^\alpha\) with \(\alpha<1\).
Its total number of distances can be much larger than \(M(D)\).
It gives no obstruction to a bound in \(\kappa^\delta\), and it is
not a lower bound for the Pell graph.

## 7. Window progress

The boundary reduction improves to

\[
W_N(h)\le W_O(h)+2\lfloor(h-1)/2\rfloor.
\]

For a one-sided right angle, write the leg displacements as
\((p,u),(q,-v)\), with \(pq=uv\) and \(u+v\le h-1\).
Its fourth corner overshoots the farther endpoint by
\(\min(p,q)\le\lfloor(h-1)/2\rfloor\). Trimming that many columns
at each end gives the reduction.

Separately, for \(h\ge4\), an N-window containing a unit-step black walk
across all its columns has width at most \(h\). If both points in every column
are supplied by unit-step walks, distinct labels improve this to
\(h-1\), sharply. The unrestricted \(W_N(h)\le h\) conjecture and
a general linear bound on \(W_O(h)\) remain open.

Proofs: [boundary overshoot](continuation_window_boundary_overshoot.md)
and [unit walks](continuation_window_unit_walks.md).
Thus the threshold reduction

\[
m_h\ge q_h+\left\lfloor\frac{q_h-1}{W_N(h)}\right\rfloor
\]

has not yet gained a new unconditional asymptotic lower bound.

## 8. The next construction task

The most concrete positive direction is to keep the private Hilbert
choices and prove a bounded-cost simultaneous repair. It has three
remaining obligations:

1. Control the interaction of unbounded Pythagorean factors, using
   a condition such as (4), a direct choice rule, or another argument.
2. Exclude cross-parity all-label right angles and mixed supports
   with the same choices or a bounded refinement.
3. Recheck all profile supports and the collar/gluing hypotheses for
   the resulting placement. Compatibility with the one-label filler
   theorem alone does not discharge these obligations.

The new factor-one theorem settles a whole arithmetic family at
constant cost. The finite-factor theorem shows that large factors
are not individually difficult. What is missing is uniform control
of their simultaneous constraints and their interaction with the
remaining geometry.

## Verification and archive scope

The main placement, factor-budget, and window theorems have separate
written audits. Computational claims have saved integer certificates
and reproducible Python scripts. The large graph searches and independent
choice verifier use NumPy; the sparse obstruction checkers use the
standard library. A side-64 translated-patch census was stopped at its memory
cap and has no claimed result. Earlier exploratory candidate files
are not the certificates used for the final claims.
The [synthesis audit](continuation_synthesis_audit.md) records the
window checks and the scope corrections made during final review.

Only new files were prepared for this continuation. Existing archive
notes and the paper were left unchanged; nothing was committed.
