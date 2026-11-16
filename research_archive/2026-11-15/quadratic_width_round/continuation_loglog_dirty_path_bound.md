# Dirty nonanchor paths of logarithmically growing length

15 November 2026. The fixed-length bad-witness path estimate can be made
uniform for lengths proportional to \(\log\log h\). The only loss
that becomes a fixed power of \(h\) in this range is the repeated
divisor bound for the norm legs. All sampling, coordinate-bin, and
height-volume constants are smaller.

Let \(b\) bound the deterministic number of bad physical rows in a
parity pool. In the nonanchor V-map model described below, the expected
total incidence of actual directed P paths of every length
\[
                  1\le k\le {\log\log h\over72}
                  \tag{1}
\]
carrying a permitted dirty-row witness is at most
\[
                            b h^{25/24+o(1)}.        \tag{2}
\]
For \(b=h^{5/6+o(1)}\), this is \(h^{15/8+o(1)}\).
The statement includes the logarithmic deterministic cap/corner menus.
Every sampled endpoint row must be nonanchor. This is an incidence
bound, not a singleton assignment or a safe erasure theorem.

All logarithms in the proof are natural. Floors in (1) are understood.

## 1. Uniform model and candidate menus

Use the independently sampled nonconstant V arms and parity pools of
[the V product-kernel note](continuation_nonanchor_v_product_kernel.md).
Condition on the good anchors. Under the original law, offsets are
independent uniforms on fixed intervals of length \(\Theta(h)\).
Each arm count function has derivative between fixed positive constants
and the stated independent dyadic coefficients of size
\(1/[16(j+1)^2]\). Occurrence errors, anchor insertions, and physical
row-residue scales are uniformly bounded. The two parity pools are
independent. Anchors themselves are excluded from the row forms counted
here.

There are \(O(h^2)\) possible first physical columns. At each column,
allow at most \((C\log(2h))^A\) predetermined point forms, for fixed
\(A,C\). A form specifies effective raw indices, a V arm when needed,
and bounded row/index errors. A fixed rank's dyadic cap ancestors,
endpoint corners, and bounded small-cap fallbacks satisfy this condition.
The menus are specified independently of the sampled fields and offsets;
selection and branch eligibility may be discarded in an upper bound.

For a path candidate of length \(k\), permit a witness menu of size
at most
\[
                         (Ck)^A(C\log(2h))^{Ak},     \tag{3}
\]
with a fixed \(A\). A witness gives one parity, a deterministic raw
index from the candidate's provenance, and membership in that parity's
deterministic bad-row set. The actual cap menus are smaller: choose a
path vertex, one ancestor, a dirty immediate child, and one of its
boundary coordinates. No freely selected raw witness index is allowed.

Every edge has a nonzero odd signed height \(Y\) and an actual in-strip
integral norm, so \(|Y|,|X|,L\le h\). Constants below may depend on
the fixed menu parameters and fixed geometric profile constants, but
not on \(h\) or \(k\). A bounded-density restriction of the offsets
can be applied after the original-law estimate.

## 2. An explicit divisor bound

For all sufficiently large \(h\), uniformly for positive integers
\(n\le h^2\),
\[
                 \tau(n)\le
                 D_h:=\exp\left({3\log h\over\log\log h}\right).
                 \tag{4}
\]
This weak form needs no prime-distribution estimate. Write
\(n=\prod p^{a_p}\) and split primes at \(R=\sqrt{\log h}\).
There are at most \(R\) small primes, and each exponent is
\(O(\log h)\), so their contribution to \(\log\tau(n)\) is
\(O(\sqrt{\log h}\log\log h)=o(\log h/\log\log h)\).
For \(p>R\),
\[
 \sum a_p\le {\log n\over\log R}
                 \le {4\log h\over\log\log h},
 \qquad
 \sum\log(a_p+1)\le(\log2)\sum a_p.
\]
Since \(4\log2<3\), this proves (4).

For a prescribed nonzero signed height \(Y\), factoring
\[
                            (L-X)(L+X)=Y^2
                            \tag{5}
\]
therefore leaves at most \(2D_h\) possible signed horizontal legs.
Integrality, parity, and the in-strip restriction only decrease this
number. A path of length \(k\) incurs at most \((2D_h)^k\) from
this step.

## 3. The row-kernel constants grow at most exponentially

For \(m\) prescribed nonanchor rows of one parity, the proof in
the V product-kernel note gives the uniform bound
\[
 \Pr(\hbox{all rows})
 \le { (Cm)^{Cm}\log^{2m}(2h)
          \over h\prod_{j<m}(1+d_j)},               \tag{6}
\]
where \(d_j\) are the consecutive sorted raw-index gaps. The generous
\((Cm)^{Cm}\) factor absorbs arm splits, repeated or bounded gaps,
and bounded-error choices.

For completeness, every nontrivial same-arm target gap supplies one
dyadic variable with coefficient at least its gap divided by
\(C\log^2(2h)\). These intervals are disjoint. When both arms are
used, the longer nearest-target prefix supplies the cross-arm gap
factor; the shorter prefix fixes \(O(1)\) offsets. There are at most
\(m\) splits and at most \(C^m\) bounded-error choices. This is
the entire dependence on \(m\); the proof does not invoke an
uncontrolled fixed-dimension compactness constant.

For \(k\) fixed norm equations, form the two sorted-index paths,
their gap products \(Q_0,Q_1\), the minimum tree product \(\tau\),
and \(K=Q_0Q_1/\tau\). Insert one prescribed bad-row witness as in
[the dirty-witness kernel](continuation_dirty_witness_path_kernel.md).
The target-tuple enumeration on a spanning tree costs at most a fixed
constant per edge, times the tree product. The extra witness gap cancels
between the augmented row denominator and the attached tree edge.
Applying (6) in both parity pools consequently gives
\[
 \Pr(\hbox{norm equations and this witness})
       \le {b (Ck)^{Ck}\log^{Ck}(2h)\over h^2 K}.   \tag{7}
\]
Here and below a larger fixed \(C\) may be used in successive lines.
The probability is computed for deterministic rank, height, form, and
witness candidates. No sampled field is conditioned on a target chosen
adaptively from that same field.

## 4. Uniform full height volume

Fix the two coordinate orders and dyadic bins of the \(2k-2\) gap
weights, using lower dyadic representatives. They are at most \(Ch\),
including cap-projected forms. There are at most
\[
                    (k!)^2(C\log(2h))^{2k}          \tag{8}
\]
such choices.

The full, nondeleted version of
[the cycle-space height-volume lemma](continuation_cycle_height_cycle_space_volume.md)
has \(k-1\) independent circulation constraints. One can choose them
successively from simple cycles at their birth scales. Each coefficient
is \(0,1\), or \(-1\). If a circulation is born at scale \(t\),
its alternating height sum has absolute value at most \(Ck^2t\):
each coordinate cluster spans at most \(k\) consecutive raw gaps,
and at most \(k\) row differences occur in the cycle.

Together with one height coordinate, these \(k-1\) circulation
forms give an injective integer linear map on \(\mathbb Z^k\).
Indeed, at the final threshold their span is the subspace of vectors
with coordinate sum zero, and the extra height coordinate completes
the rank. Counting integer images in the bounding box is enough; no
inverse-matrix estimate or unspecified determinant constant is needed.
The product of the \(k-1\) circulation birth scales is \(K\), up
to a factor \(2^{O(k)}\) from dyadic representatives. Thus the number
of possible signed-height tuples is at most
\[
                              h(Ck)^{Ck}K.          \tag{9}
\]
The proof requires only the global bounded variation of each V-map in
its raw index. It does not require all forms to lie on one arm, nor an
\(O(\sqrt h)\) effective-coordinate diameter.

Choose the first physical column in \(O(h^2)\) ways and factor each
of the \(k\) heights by (5), recovering subsequent columns in path
order. At each recovered column choose a permitted form. Reject those
whose actual orders and bins do not match the selected ones. This gives
at most
\[
       h^3 K(Ck)^{Ck}(C\log(2h))^{Ak}(2D_h)^k       \tag{10}
\]
candidates in a bin. All heights were enumerated before the horizontal
legs. There is no additional endpoint-coordinate or cap-area factor.

## 5. Sum the candidates and choose the growing length

Multiply (10) by (7), and sum the orders, bins, forms, and witness menu.
The factors of \(K\) cancel. A uniform upper bound for length \(k\)
is
\[
 \mathbb E N_k
 \le b h\,(Ck)^{Ck^2}(C\log(2h))^{Ck}D_h^k.        \tag{11}
\]
This deliberately allows more dependence on \(k\) than the preceding
estimates need. If \(k\le c\log\log h\), for a fixed \(c>0\),
then
\[
 (Ck)^{Ck^2}(C\log(2h))^{Ck}=h^{o(1)},
 \qquad D_h^k\le h^{3c}.                            \tag{12}
\]
The first assertion follows by taking logarithms: its exponent is
\(O((\log\log h)^2\log\log\log h)=o(\log h)\).
Summing all lengths up to this cutoff introduces only a factor
\(O(\log\log h)=h^{o(1)}\). Therefore
\[
 \mathbb E\sum_{1\le k\le c\log\log h}N_k
                          \le b h^{1+3c+o(1)}.      \tag{13}
\]
Taking \(c=1/72\) proves (2). Multiplying by \(k+1\) to count
all path-vertex incidences changes only \(h^{o(1)}\). The same
estimate holds under the reviewed bounded joint density restriction of
the offsets.

## 6. What the estimate does and does not permit

The bound controls a slowly growing exploration radius, rather than
each fixed radius separately. It applies to the compiled potential
nonanchor point union before selecting caps or singleton states. A
selected cap supplies a permitted dirty-child witness through the
deterministic ancestor menu.

Constant-anchor endpoints require a different kernel and are not counted.
Paths can contain singleton objects, so marking their genuine vertices
does not automatically destroy every counted path. Erasing a genuine
pair may also leave a singleton with the same relevant point. A safe
occupancy-preserving repair must handle these issues separately.
The theorem therefore does not establish a bounded reachability
closure, a consistent global parity choice, or an \(O(h^2)\) board.

## Review status

The fixed-length V product kernel, dirty-witness kernel, and full
height-volume argument have separate written reviews. The complete
growing-length proof also passed an independent written review: the
divisor constant three, uniform row strips, injective integer height
map, order/bin/form factors, and final exponent arithmetic were checked
again. A second independent written review checked the same uniform
constants, including the \(Ck^2\) circulation widths and witness menus,
and also passed without correction.
