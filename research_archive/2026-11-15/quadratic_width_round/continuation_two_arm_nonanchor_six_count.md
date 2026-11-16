# Independent fold arms count all nonanchor long six supports

15 November 2026. This note proves a counting theorem for a two-arm
mechanical row map. The arm slopes are independent, and both arms start
at one fixed base. Under the stated cap and sampling hypotheses, long
same-parity six supports with no fixed-anchor endpoint have expected
count \(h^{31/16+o(1)}\).

The theorem does not establish a complete board assembly. In particular,
it does not count fixed-anchor endpoints or specify a safe support
repair.

## 1. Sampling assumptions

Fix a base row \(B_0\), a row step \(D\), and two independent random
parameters with slopes
\[
 \alpha_-,\alpha_+\in[a,b],\qquad 0<a<b<\infty.
 \]
Each slope has a bounded density. Independently choose an integer
offset \(U\) uniformly from a fixed interval of \(\Theta(h)\) integers.
On the two nonconstant arms, require the uniform formulas
\[
 Y_-(k)=B_0+D\alpha_-(U-k)+O(1),\quad k<U,
 \qquad
 Y_+(k)=B_0+D\alpha_+(k-U)+O(1),\quad k\ge U.
 \tag{1}
\]
The errors are bounded by a fixed constant. They may depend on the
parameters and need not be independent. A fixed list of bounded row
shifts is also allowed.

Assume each arm is a bounded-gap monotone occurrence list, both arms
agree at their common base up to the fixed listed adjustments, and the
realized total row map is uniformly Lipschitz in the raw index.
Consequently the total cap functions retain the established
square-root locality in rank.

Every nonanchor cap candidate is evaluated at the boundary coordinate
\(c_Q\) of a prescribed dyadic node. The node and coordinate are
enumerated before sampling. The candidate may lie on either arm;
its branch membership is an additional event condition.
Fixed physical anchor plateaus are excluded.

## 2. Two prescribed rows, including different arms

Suppose two fixed candidate indices must take two fixed target rows
\(A_1,A_2\), and put \(d=|A_1-A_2|\ge1\).

If both candidates use the same arm, multiplying their row equations
by its common sign and subtracting eliminates \(U\). The slope is
restricted to an interval of length \(O(1/|k_1-k_2|)\).
For each slope, either row equation permits \(O(1)\) offsets.
The actual same-arm Lipschitz bound gives
\(|k_1-k_2|\ge cd\) for large \(d\). Thus the probability is
\[
 O(1/(hd)).
 \tag{2}
\]

For different arms, write the target heights above the common base
as \(a_i=A_i-B_0\), and set \(A_i^*=1+\max(0,a_i)\).
Targets below the base by more than the fixed error are impossible.
For a fixed offset, let \(x_i=|k_i-U|\).
The row event implies
\[
 1+x_i\asymp A_i^*.
 \tag{3}
\]
The bounded slope density bounds its probability, for that offset,
by \(C/(1+x_i)\). The slopes of the two arms are independent,
so the joint conditional probability is at most
\[
 C/((1+x_1)(1+x_2)).
 \tag{4}
\]
The offsets compatible with the first target occupy \(O(A_1^*)\)
integers, and those compatible with the second occupy \(O(A_2^*)\).
Their intersection therefore has at most \(C\min(A_1^*,A_2^*)\)
integers. Summing (4) over offsets and using (3) gives
\[
 \Pr(Y(k_i)=A_i,\ i=1,2)
 \le \frac{C}{h\max(A_1^*,A_2^*)}
 \le \frac{C}{hd}.
 \tag{5}
\]
This argument does not subtract formulas with different slopes.
All branch conditions and bounded errors are retained as event
conditions or enlarged by fixed constants.

Therefore a prescribed parked triangle with an already enumerated
physical increment \(|\delta|\ge ch/K\) has probability at most
\[
 CK/h^2
 \tag{6}
\]
for every choice of two nonconstant arms. Its target rows are fixed by
\[
 A=s+X\xi/\delta,\qquad A+\delta.
 \tag{7}
\]

## 3. Three prescribed rows with a far partner

The physical-divisor enumeration fixes the two partner rows as
\(A,A+v\), and the two hub rows as
\[
 A+\delta,\quad A+\delta+v,
 \qquad |v|\le C\sqrt K,\quad |\delta|\ge ch/K.
 \tag{8}
\]
Suppose the partners occupy opposite arms and each has height at least
\(R\) above \(B_0\), where \(R\ge C\sqrt K\).

One arm contains a partner and a hub whose target-row difference is
\(\delta\), \(\delta+v\), or \(\delta-v\).
Indeed, each arm already contains a partner, and at least one hub
belongs to one of those arms. For polylogarithmic \(K\), all three
possible differences have magnitude at least \(ch/(2K)\) for large
\(h\).

Choose such a pair. Its common-arm equations restrict that arm's
slope to an interval of length \(O(K/h)\), and permit only \(O(1)\)
offsets for each slope. The other partner lies on the independent
arm. Its height condition forces distance at least \(cR\) from the
turn, so its prescribed row has conditional probability at most
\(C/R\). Therefore the probability of the required three rows is
\[
 CK/(h^2R).
 \tag{9}
\]
The fourth row and the second triangle can be discarded for an upper
bound.

The chosen arm pair may involve the second hub. Both hub candidate
indices must therefore be enumerated before applying (9). For cap
candidates this costs \(O(\log^2h)\), not an independence assumption.

## 4. Physical divisibility fixes the candidate hubs

Use the exact partner-first identity
\[
 \Delta=p_1-p_2+t,\qquad
 \delta\mid S\xi_1\xi_2\Delta,\qquad
 r=p_1+\frac{S\xi_2\Delta-\delta v}{S^2t}.
 \tag{10}
\]
Here \(t=(\xi_1-\xi_2)/S\ne0\), and \(|\xi_i|,|t|=O(K)\).
For long supports, \(\Delta\ne0\), by actual hub locality.

Enumerate partner positions and their potential cap nodes, signed
divisors \(\delta\) with \(0<|\delta|<h\), and integers
\(|v|\le C\sqrt K\). Equation (10) fixes \(r\), after which both
hub ancestor candidates are listed. The first triangle equation (7)
then prescribes all four physical rows in (8).

The integer in the divisibility condition is \(O(K^2h^2)\).
For polylogarithmic \(K\), divisor choices, offset choices, arm choices,
and ancestor choices together contribute only \(h^{o(1)}\).
In particular, the near-base/far-base distinction is made from
deterministic target rows after this enumeration. It is not a
conditioning step on the sampled parameters.

## 5. Near-base and far-base counts

At any fixed cap depth, the total candidate rank mass is \(O(N^2)\).
Thus all ordered partner pairs, including their two ancestor choices,
number at most \(h^{4+o(1)}\).
For opposite-arm partners with both heights at least \(R\), equation
(9) gives
\[
 \mathbb E N_{\mathrm{far}}\le h^{2+o(1)}/R.
 \tag{11}
\]

If one partner height is below \(R\), the other is at most
\(R+C\sqrt K\), by (8). Formula (1) then puts both prescribed partner
indices within \(C(R+\sqrt K)\) of \(U\). Hence
\[
 |c_1-c_2|\le C(R+\sqrt K).
 \tag{12}
\]
This is a deterministic necessary condition on their candidate indices.

For cap sides \(L_1,L_2\le L_{\max}\), the reviewed weighted mass bound
is
\[
 \#\{(p_1,Q_1),(p_2,Q_2):|c_1-c_2|\le W\}
 \le CN^3(W+\min(L_1,L_2)).
 \tag{13}
\]
Summing the dyadic levels gives at most
\[
 h^{3+o(1)}(R+L_{\max})
 \tag{14}
\]
near-base partner candidates when \(R\ge C\sqrt K\).
The two-row estimate (6), with the physical-divisor enumeration,
therefore gives
\[
 \mathbb E N_{\mathrm{near}}
 \le h^{1+o(1)}(R+L_{\max}).
 \tag{15}
\]
Choose \(R=h^{1/2}\). The opposite-arm total is
\[
 \mathbb E N_{\mathrm{opposite}}
 \le h^{3/2+o(1)}+h^{1+o(1)}L_{\max}.
 \tag{16}
\]

When both partners use the same arm, (1) makes their candidate indices
\(O(\sqrt K)\)-close. The existing central-cap argument applies
directly and has the same \(h^{1+o(1)}L_{\max}\) upper bound.

## 6. A concrete cap cutoff

Assume the reviewed bad-child bound with
\(b=h^{5/6+o(1)}\). Set
\[
 L_{\max}\asymp h^{15/16}.
 \tag{17}
\]
The probability of any larger selected cap is at most
\[
 Chb/L_{\max}^2=h^{-1/24+o(1)}=o(1).
 \tag{18}
\]
Equations (16)--(18) yield a joint selection with no larger caps and
long same-parity six incidence at most
\[
 h^{31/16+o(1)}.
 \tag{19}
\]
This includes same-arm and opposite-arm nonconstant candidates,
unequal cap depths, and raw/cap mixtures. For raw partners alone,
the opposite-arm bound is \(h^{3/2+o(1)}\).

The use of (18) does not condition the sampling estimates on cap
selection. All short-cap candidates are counted unconditionally, and
the large-cap event is handled separately in a joint selection.

Fixed physical anchors remain excluded from (1), (2), and (9).
The theorem also assumes the independent-arm map can be implemented
with the stated locality, bad-row probability, and genuine-label
coverage. Those assembly requirements and safe support repair remain
separate.

## 7. A weighted partner-distance refinement

The split at \(R=h^{1/2}\) is not needed for raw partners. Let
\[
 d_0=|c_1-c_2|,\qquad W_0=C_0\sqrt K,
 \tag{20}
\]
where \(C_0\) is a sufficiently large fixed constant.
For opposite arms, the two distances from the turn sum to \(d_0\).
Their physical heights differ by at most \(C\sqrt K\), and both arm
slopes stay between fixed positive constants. If \(d_0>W_0\),
both arm distances and both heights are therefore at least \(cd_0\).
The three-row proof from Section 3 gives
\[
 \Pr(\hbox{required target rows})
 \le CK/(h^2d_0),\qquad d_0>W_0.
 \tag{21}
\]
For \(d_0\le W_0\), retain the two-row bound \(CK/h^2\).
The distance \(d_0\) is determined by the candidate indices before
sampling.

At fixed partner cap depths, put \(L=\min(L_1,L_2)\).
The near-pair estimate (13) bounds the unweighted mass at distances
at most \(D\) by \(CN^3(D+L)\). On dyadic annuli
\(D<d_0\le2D\), weighting by \(1/d_0\) consequently gives at most
\[
 CN^3(1+L/D).
 \]
Summing over \(D\ge W_0\), and adding the unweighted near mass, gives
\[
 CN^3\bigl(W_0+L+\log(2N)\bigr).
 \tag{22}
\]
All divisor, offset, hub-ancestor, and cap-depth factors are
\(h^{o(1)}\) for polylogarithmic \(K\).

Thus the opposite-arm expected count is \(h^{1+o(1)}\) when at least
one partner is raw, even if the other has arbitrary cap side.
More generally, restricting the smaller partner side to at most \(L_0\)
gives
\[
 \mathbb E N_{\min(L_1,L_2)\le L_0}
 \le h^{1+o(1)}(1+L_0).
 \tag{23}
\]
The sum of \(\min(L_1,L_2)\) over dyadic levels up to \(L_0\), with
the other level unrestricted, is \(O(L_0\log h)\), which is sufficient
here. When both levels are at most \(L_{\max}\), the sharper sum is
\(O(L_{\max})\).

Equation (23) improves the raw opposite-arm bound stated after (19).
The all-cap exponent \(31/16+o(1)\) remains the same. Fixed physical
anchor endpoints are still excluded.

Independent review: the full written proof passed a separate review,
including the cross-arm two-row estimate, the three-row gain,
parameter-independent ancestor enumeration, weighted cap counts, and
the sharper partner-distance kernel in Section 7.
