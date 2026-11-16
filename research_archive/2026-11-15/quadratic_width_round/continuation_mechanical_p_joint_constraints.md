# Joint P constraints under independent mechanical row stretches

15 November 2026. Independent odd/even mechanical stretches provide a
joint constraint estimate, without treating edges as independent. For
central branches, one edge costs \(O(h^{-1})\); further edges are
controlled by the rank of their two-coordinate coefficient differences.
This gives an \(h^{3/2+o(1)}\) exceptional genuine-endpoint bound for
all bidirectional P templates, including unequal hypotenuses.

The conclusion removes a small set of compulsory doubles from that
obstruction. It does not assign all remaining singleton parities or
control longer paths and cycles automatically.

## 1. Sampling and the uniform approximation

Use the two complementary mechanical lists and fixed-anchor insertion in
[continuation_mechanical_anchor_insertion.md](continuation_mechanical_anchor_insertion.md).
For either chosen class in one parity, its modified occurrence list obeys
\[
 p_i(\theta)=\alpha i+O(1),\qquad 3/2\le\alpha\le3.       \tag{1}
\]
The error is absolute and uniform. Uniform \(\theta\in[1/3,2/3]\)
gives a bounded density for \(\alpha\). The two parity parameters
\(\alpha_0,\alpha_1\) are independent. The two complementary classes
within one parity need not be independent: apply each estimate to a fixed
class pair, then take the finite union.

The index offsets \(U_0,U_1\) are independent uniforms on fixed integer
intervals of length \(\Theta(h)\), independent of the stretch variables.
The padded side and genuine list lengths are \(\Theta(h)\). Eligibility
and good-row conditions can be omitted in upper bounds. Physical rows
have the fixed step \(D\) multiplying (1).

Bounded anchor insertions and fixed-size interpolation perturb (1) by
only \(O(1)\). For the cap application below, require each fine virtual
pair to be within a fixed physical error of one coarse virtual pair at a
bounded originating-rank distance. The base coarse pair has at most one
selected cap coordinate. This is an explicit representation hypothesis;
the proof does not allow two unrelated cap coordinates at one point.

## 2. A joint rank bound for fixed central-branch events

Fix finitely many vertical requirements whose central-branch forms are
\[
 D\{\alpha_1(B_e-U_1)-\alpha_0(A_e-U_0)\}+c_e
   =Y_e+O(1).                                             \tag{2}
\]
The coordinate integers \(A_e,B_e\), heights \(Y_e\), and fixed bases
\(c_e\) are specified. The bounded errors may depend arbitrarily on
the shared parameters; no independence of those errors is assumed.

Fix one event \(e_0\). Given \(\alpha_0,\alpha_1,U_1\), (2) for
\(e_0\) allows only \(O(1)\) integer values of \(U_0\). Thus it
costs \(O(h^{-1})\). Subtracting it from each other event leaves
linear strips of bounded width in the independent stretch variables:
\[
 -\alpha_0(A_e-A_{e_0})+\alpha_1(B_e-B_{e_0})
   =\text{specified constant}+O(1).                      \tag{3}
\]
Let \(R\) be the largest sup-norm coordinate difference between any two
points \((A_e,B_e)\). Let \(\Delta\) be the largest absolute determinant
of two differences from one such point. A single strip has area
\(O(1/\max(1,R))\) in the fixed stretch box. Two independent strips
have area \(O(1/|\Delta|)\), by their linear change of variables.
Consequently the joint probability is at most
\[
 \frac C h\min\left\{1,\frac1{\max(1,R)},
                    \frac1{|\Delta|}\right\},             \tag{4}
\]
where the last term is omitted when \(\Delta=0\).

This identifies the degeneracies precisely. If all coefficient points
coincide, the extra events need not add any stretch condition. If they
lie on one affine line, the affine approximation supplies only one
independent stretch condition. Noncollinear triples supply two. Additional
events can be inconsistent or constrain rounding further, but multiplying
their marginal probabilities is not justified by (1).

For a fixed primitive direction, \(Y_e\) is its prescribed rational
slope times the fixed horizontal displacement; nonintegral choices are
discarded. Thus (4) applies directly to fixed short paths or cycles in
central branches. It is a joint estimate, not a path-count theorem.

## 3. Apply two conditions to a bidirectional template

Let \(r\) be a retained genuine source object with raw cell
\((i_r,j_r)\). Its exact rows have the form
\[
 a_r=\rho_0+D p_{i_r-U_0}(\theta_0),\qquad
 b_r=\rho_1+D p_{j_r-U_1}(\theta_1).
\]
Assume its own gap is at least \(B_h\), where
\(B_h/\sqrt h\to\infty\). This condition will only exclude bounded
same-object copies below; equality of the two hypotenuses is not needed.

For a partner's two central coordinate forms \((c_0,c_1)\), specify
any two signed P heights \(Y_1,Y_2\) at their common horizontal gap:
\[
 b_s-a_r=Y_1,\qquad b_r-a_s=Y_2.                          \tag{5}
\]
Subtracting (5), and using (1), gives
\[
 D\{\alpha_0(c_0-i_r)+\alpha_1(c_1-j_r)\}
       =Y_1-Y_2+O(1).                                    \tag{6}
\]
Set \(R_{r,s}=\max(|c_0-i_r|,|c_1-j_r|)\). If this is nonzero,
the joint probability of (5) is
\[
 O\!\left(\frac1{hR_{r,s}}\right).                       \tag{7}
\]
The signs and the two hypotenuses may differ. This is the gain absent
from the fixed-step equal-height argument.

For an uncapped partner, \(R_{r,s}=0\) means the same coarse object.
Its bounded-copy horizontal displacement is \(O(1)\), while its
cross-row height is \(B_h-O(1)\). Such an integral norm is impossible
for large \(h\), since \(X^2\ge2|Y|+1\) for a nonzero integer
horizontal leg and an odd vertical leg. For a capped partner, its
coordinate projection lies inside its cap square. A genuine source
cannot lie in that selected cap. Thus \(R_{r,s}\ne0\) in every
actual capped case. Retain that necessary exclusion when taking the
cap-coordinate union.

## 4. Weighted cap projection bound

An actual P has horizontal span at most \(h-1\), so the partner raw
ranks lie in an interval of length \(O(h)\) about \(r\). Their cells
lie in a square of side \(R_0=O(\sqrt h)\). For uncapped partners,
integer grid packing gives
\[
 \sum_s\frac1{\max(|i_s-i_r|,|j_s-j_r|)}=O(R_0),         \tag{8}
\]
with the coincident cell omitted.

At a fixed cap depth, project each candidate partner to
\(\pi_Q(s)=(c_Q,H_N(s)_\beta)\), or its coordinate reversal,
and exclude squares \(Q\) containing \(r\). Then
\[
 \sum_s\frac1{\|\pi_Q(s)-H_N(r)\|_\infty}
       =O(R_0\log(2R_0)).                                \tag{9}
\]
Here multiplicities of a projected coordinate are retained.

For detail, let the dyadic side be \(\ell\le R_0\). Squares at
distance comparable to \(j\ell\), \(j\ge1\), number \(O(j)\),
each contribute at most \(\ell^2/(j\ell)\), and summing their shells
gives \(O(R_0)\). There are only \(O(1)\) squares within distance
\(O(\ell)\) of the source. In each, projection collapses at most
\(\ell\) cells to each coordinate row; the remaining reciprocal
distance sum is harmonic, at most \(O(\log(2\ell))\). Their
contribution is \(O(\ell\log(2\ell))\).

If \(\ell>R_0\), the rank interval meets only \(O(1)\) depth nodes.
Each projected coordinate has multiplicity at most \(O(R_0)\) inside
the raw box, and the same harmonic bound gives
\(O(R_0\log(2R_0))\). The exclusion \(r\notin Q\) ensures that
no denominator vanishes. Summing over depths costs one further logarithm.

## 5. Other fold branches

Condition on the stretches and on a target branch choice. Its row options
have offset coefficients \(D\sigma_0\alpha_0U_0\) and
\(D\sigma_1\alpha_1U_1\), where \(\sigma_\alpha\in\{-1,0,1\}\).
Constant anchors have coefficient zero. All bounded approximation and
interpolation errors are retained as bounded-width inequalities.

For the two equations (5), the offset determinant is, up to sign,
\[
 D^2\alpha_0\alpha_1(1-\sigma_0\sigma_1).
\]
If \(\sigma_0\sigma_1\ne1\), at most \(O(1)\) integer offset
pairs satisfy them, giving probability \(O(h^{-2})\). The upper-fold
branch's intercept may depend on the realized class length; after
conditioning on the stretches this is fixed and does not change the bound.

The two negative coefficients are exactly the central case treated above.
If both are positive, at least one target coordinate is uncapped and
lies on a reflected branch. Its raw value is outside the corresponding
genuine interval. A genuine source at raw rank distance \(O(h)\) must
therefore lie in an \(O(\sqrt h)\) boundary strip of its genuine
rectangle. Uniformly in all stretches and offsets, only \(O(h^{3/2})\)
genuine labels are in that strip. Charge all of them as exceptional.

## 6. The exceptional-set bound and its limit

Write \(\mathcal D_h=\max_{n\le h}\tau(n^2)=h^{o(1)}\).
For a fixed horizontal displacement, there are at most
\(O(\mathcal D_h^2)\) ordered signed pairs of integral P heights.
There are \(O(h^2)\) genuine source ranks. Equations (7)--(9), summed
over all cap depths, give
\[
 \mathbb E I_{\rm central}
 \le C h^{3/2}\mathcal D_h^2\log^2(2h).                 \tag{10}
\]
The nonsingular branch cases have \(O(h^3\log h)\) rank/form
possibilities and probability \(O(\mathcal D_h^2/h^2)\), for
\(O(h\mathcal D_h^2\log h)\) expected templates. Add the
deterministic \(O(h^{3/2})\) genuine boundary set.

Consequently suitable joint stretch/offset choices have only
\(h^{3/2+o(1)}\) genuine endpoints incident to any bidirectional
P template. The normalized cost can be included in the same averaging
objective as the other established construction costs. Relocating all
such pairs has subquadratic internal cost under the existing
\(h^{o(1)}\) relocation factor.

This removes compulsory doubles from every bidirectional obstruction in
the specified virtual union, not just the equal-height subfamily. It does
not remove every P edge between the singleton points left behind, choose
their retained parity, or prove an object-to-path Hall condition. Longer
cycles can retain only one stretch condition when their coefficient
points are collinear. Those shared-parameter degeneracies are explicit
in Section 2 and remain part of the remaining choice problem.

## Review status

The full joint estimate passed an independent written review. The review
checked the conditional offset count, determinant cases, weighted cap
projection with multiplicity, and the reflected boundary charge.

The interpolation representation in Section 1 was also verified for the
cleared scheme. Each fine pair is within the fixed adjacent-jump bound of
its left coarse pair. Under a cleared fixed-size block permutation that
pair comes from a bounded-distance originating rank; a moved pair is
genuine and has no cap coordinate, while an unmoved pair has at most one
selected cap coordinate. Thus the stated one-base-pair hypothesis applies
to this scheme. It is not inferred for arbitrary coordinate substitutions.

## 7. Well-conditioned three-cycles in a fixed direction palette

Fix a finite set of nonzero Pythagorean slopes, independent of \(h\),
and let \(\varepsilon>0\). Consider three-cycles whose three objects
are genuine central-branch objects. The same statement holds for a fixed
finite union of the central nonconstant forms covered by Section 2, with
its logarithmic factors retained. Constant anchors and arbitrary fold
signs are not included without a separate determinant estimate.
Use the three coefficient points
\[
 (i_0,j_1),\quad(i_1,j_2),\quad(i_2,j_0)
\]
in Section 2. The expected number of such cycles with
\[
 |\Delta|\ge h^{1/2+\varepsilon}
\tag{11}
\]
is \(O(h^{2-\varepsilon})\), or \(h^{2-\varepsilon+o(1)}\)
for the stated form union. In particular, their genuine endpoints can be
marked at subquadratic internal relocation cost.

There are \(O(h^2)\) choices for the first fine object and \(O(h)\)
choices for the second, since an actual P edge has horizontal span below
\(h\). Write the first two signed horizontal increments as \(X_1,X_2\)
and their assigned slopes as \(\mu_1,\mu_2\). Same-parity locality
forces
\[
 |(b_2-a_1)-(b_1-a_0)|
 \le |b_2-b_1|+|a_1-a_0|=O(\sqrt h).
\]
Thus a necessary condition for the first two edges is
\[
 \mu_2X_2=\mu_1X_1+O(\sqrt h).
\]
Once the first two objects and the slopes are specified, the third column
lies in an interval of length \(O(\sqrt h)\). Consequently there are
only \(O(h^{7/2})\) potential rank triples, uniformly over the sampled
parameters. The finite direction choices only change the constant.
Apply (4) and (11): each triple has probability at most
\(C h^{-3/2-\varepsilon}\). Their product gives the asserted bound.

This leaves the small-determinant family
\(|\Delta|<h^{1/2+\varepsilon}\), including collinear coefficient
triples. It also leaves palettes whose directions change with height and
longer cycles. The rank estimate alone supplies no exponential suppression
in the number of edges. This section passed a separate independent written
review, including the deterministic interval for the third rank and the
central-form scope stated above.
