# Opposite-parity long six supports with all cap types

15 November 2026. The independent-arm scaffold and its random near-edge
anchors give an \(h^{13/12+o(1)}\) expected count for long six-point
supports whose two triangles use opposite parities. This includes all
cap sizes and fixed anchor hubs.

The count uses only a divisibility progression and independence between
the two parity parameter families. It does not use Hilbert row-section
energy. Safe support erasure and external relocation remain separate.

## 1. Sampling inputs

Use the reviewed
[independent-arm V-map](continuation_independent_arm_v_map.md)
for each parity. Its anchor \(A_\alpha\) is sampled independently of
its arm parameters and index offset, with
\[
 E=h^{23/24},\qquad
 \sup_a\Pr(A_\alpha=a)\le h^{o(1)}/E.
 \tag{1}
\]
The complete parameter families of the two parities are independent.
The number of profiles and central class products is fixed.

The available bound for two prescribed nonconstant candidate values
with physical difference at least \(ch/K\) is
\[
 CK/h^2.
 \tag{2}
\]
This is uniform conditional on the anchor, and includes same-arm
or opposite-arm formulas at fixed raw or cap boundary indices.
For one prescribed nonconstant value, the corresponding uniform bound
is \(C/h\), since for every arm parameter it admits \(O(1)\) offsets.

Take polylogarithmic \(K\). For a long support of span greater than
\(h^2/K\), its common physical increment is positive and obeys
\[
 \delta\ge ch/K.
 \tag{3}
\]
Positivity follows because the completion row is \(s+\delta\), where
the low sea row \(s\) is bounded. A negative increment is bounded and
cannot satisfy the long-increment estimate.

An anchor cannot be a partner: its hub would have row at least
\(h-E+\delta>h\) for large \(h\). The same conclusion holds for
the fixed bounded perturbations in the interpolation candidate union.

## 2. Prescribed-increment probability for one triangle

Fix its two core ranks \(r,p\), a nonzero sea offset \(\xi\), the sea
row \(s\), and a physical increment \(\delta\ne0\).
The triangle equation prescribes the partner and hub rows as
\[
 y_p=s+\frac{S\xi(r-p)}{\delta},\qquad
 y_r=y_p+\delta.
 \tag{4}
\]
Noninteger or out-of-strip target rows are rejected.

If both endpoint candidates are nonconstant, (2) applies.
If the hub is an anchor, (4) fixes that physical anchor value.
Its atom bound is \(h^{o(1)}/E\). Conditional on that anchor,
the nonconstant partner takes its prescribed row with probability
at most \(C/h\). Thus the triangle has probability at most
\[
 h^{o(1)}/(hE).
 \tag{5}
\]
No anchor-partner case remains. Since \(E<h\), equations (2) and
(5) give the uniform bound
\[
 \Pr(\hbox{one prescribed triangle and increment})
 \le h^{o(1)}/(hE).
 \tag{6}
\]
All cap-node, branch, and bounded local refinement candidates precede
sampling. Conditioning on the selected caps is not used.

## 3. A short candidate list

Fix the two sea offsets \(\xi_0,\xi_1\), each of magnitude at most
\(CK\). A common completion fixes the hub relation
\[
 r_1=r_0+(\xi_0-\xi_1)/S.
 \tag{7}
\]
Unlike the same-parity case, the shift may be zero, since one core
column can contain both parities. Noninteger or out-of-range hubs
are rejected.

There are \(O(h^4)\) choices of the first hub \(r_0\) and partner
\(p_0\) in a core of \(O(h^2)\) columns. Their triangle requires
\[
 \delta\mid S\xi_0(r_0-p_0).
 \tag{8}
\]
The integer on the right is nonzero and has size \(O(Kh^2)\).
Enumerate its signed divisors satisfying (3) and \(|\delta|<h\).
For polylogarithmic \(K\), their number is \(h^{o(1)}\).

The second triangle requires
\[
 p_1\equiv r_1\pmod{d},\qquad
 d=\frac{|\delta|}{\gcd(|\delta|,|S\xi_1|)}
      \ge ch/K^2.
 \tag{9}
\]
Its rank interval has length \(O(h^2)\), so it has at most
\(O(hK^2+1)\) possible partners.

Each of the four positions has \(O(\log h)\) possible cap ancestors,
a fixed number of arm or anchor forms, and a fixed-size local
refinement union. Including these choices and the \(O(K^2)\) offset
pairs, the total number of fixed candidates is
\[
 h^{5+o(1)}.
 \tag{10}
\]
No upper bound on cap side length is used.

## 4. Independence and expectation

For each candidate, the first triangle's prescribed-row event depends
only on the first parity's parameters. The second depends only on the
other parity's parameters. Their probabilities therefore multiply
before imposing cap-selection or shared good-row conditions.
Discarding those additional conditions is an upper bound, even though
the selected cap configuration itself depends on both parities.

Equation (6) bounds the joint event by
\[
 h^{o(1)}/(h^2E^2).
 \tag{11}
\]
Summing over (10) gives
\[
 \mathbb E N_{\mathrm{opposite}}
 \le h^{3+o(1)}/E^2
 =h^{13/12+o(1)}.
 \tag{12}
\]
This is a witness count. It covers raw points, either nonconstant arm,
arbitrary cap depths, and fixed anchor hubs. Reflection supplies the
high-sea version.

The independence argument concerns the original product sampling law.
One can combine (12) with cap-area and other incidence objectives by
joint averaging. It would be invalid to condition on a chosen cap
configuration and then assume the two triangles remain independent.

The result controls this long opposite-parity family in the enlarged
scaffold. It does not itself choose an occupancy-preserving erasure,
resolve shorter supports, or prove the complete quadratic-width result.

Independent review: the complete written proof passed a separate review
of the progression count, zero hub shift, cap-candidate enumeration,
anchor cases, and unconditional parity independence.
