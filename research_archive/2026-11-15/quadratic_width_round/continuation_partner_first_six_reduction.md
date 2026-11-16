# Partner-first reduction for same-parity parked six supports

15 November 2026. Fixing the two distant partners, rather than a hub and
an increment, gives an exact divisor test. It also gives a bounded number
of increments for raw Hilbert coordinates. On the reviewed spacing-four
mesh, at most one increment is possible.

These statements do not prove a subquadratic expected count. In
particular, uniqueness for one realized offset does not supply a second
independent offset probability.

## 1. Exact arithmetic

Use the notation of
[the raw same-parity reduction](continuation_same_parity_raw_6pt_reduction.md).
The hubs have ranks \(r,r+t\), the partners have ranks \(p_1,p_2\), and
the common sea row is \(s\). Physical columns are \(S\) times rank.
Write physical rows as
\[
 y(p)=\rho+D(f(p)-U).
\]
The nonzero sea offsets satisfy
\[
 \xi_1-\xi_2=St,\qquad t\ne0.
 \tag{1}
\]
Put
\[
 \ell=f(r)-f(p_1)=f(r+t)-f(p_2)\ne0,\qquad
 v=f(p_2)-f(p_1)=f(r+t)-f(r),
 \qquad \Delta=p_1-p_2+t.
 \tag{2}
\]
Subtracting the two parked-triangle equations gives
\[
 S^2t(r-p_1)=S\xi_2\Delta-D^2\ell v.
 \tag{3}
\]
Thus fixed partners, offsets, and increment determine the first hub:
\[
 r(\ell)=p_1+\frac{\xi_2\Delta}{St}
                   -\frac{D^2v}{S^2t}\ell.
 \tag{4}
\]
Reject nonintegral or out-of-range ranks.

The first triangle equation implies
\(D\ell\mid S\xi_1(r-p_1)\). Multiplication by \(St\), followed by (3),
therefore gives the necessary test
\[
 D\ell\mid S\xi_1\xi_2\Delta.
 \tag{5}
\]
In particular, \(\ell\mid S\xi_1\xi_2\Delta\). This is a necessary
condition, not a replacement for the original triangle equation.

For a long support of span greater than \(h^2/K\), the local-anchor
reduction supplies
\[
 |\xi_i|,|t|\le CK,\qquad
 |\ell|\ge ch/K,\qquad |v|\le C_0\sqrt{|t|}.
 \tag{6}
\]
Here \(K\) is at most a fixed power of \(\log h\), and all geometry
constants are fixed. The long-support geometry also forces a partner
leg to have rank length at least \(ch^2/K^2\).
If \(\Delta=0\), equation (4) instead gives
\[
 |r-p_1|
 \le \frac{D^2|\ell||v|}{S^2|t|}
 \le C h.
 \tag{7}
\]
Since \(\Delta=0\) also gives \(p_2=p_1+t\), the second leg has the same
length. Both legs are \(O(h)\), contrary to long span for sufficiently
large \(h\). Consequently the integer on the right of (5) is nonzero.

## 2. A bounded number of raw increments

Assume \(f\) is one raw Hilbert coordinate and
\[
 |f(a)-f(b)|\le C_0\sqrt{|a-b|}.
 \tag{8}
\]
Fix \(p_1,p_2,\xi_1,\xi_2\). Suppose two increments \(\ell_1,\ell_2\)
pass both hub row tests in (2). If \(v=0\), (4) makes the hub independent
of the increment, so the first row test determines \(\ell\) uniquely.
Otherwise, writing \(e=|\ell_1-\ell_2|>0\), equations (4) and (8) give
\[
 e\le C_0
       \sqrt{\frac{D^2|v|}{S^2|t|}\,e},
 \qquad
 e\le \frac{C_0^2D^2|v|}{S^2|t|}
       \le\frac{C_0^3D^2}{S^2\sqrt{|t|}}.
 \tag{9}
\]
The last inequality uses the second hub row test for either candidate.
Every accepted increment therefore lies in an interval of fixed length.
There are at most
\[
 1+\left\lfloor C_0^3D^2/S^2\right\rfloor
 \tag{10}
\]
such integer increments. This bound precedes the divisor test (5).

For a raw \(N\times N\) Hilbert square, \(N=\Theta(h)\), each coordinate
row has exactly \(N\) visits. For fixed \(t\), the number of ordered
partner pairs with \(|v|\le C_0\sqrt{|t|}\) is at most
\[
 C N^3(1+\sqrt{|t|}).
 \tag{11}
\]
There are \(O(K^2)\) offset pairs in (6). Equations (10) and (11)
bound all positional candidates by \(O(h^3K^{5/2})\).

The raw coordinate tests are independent of \(U\). Each candidate that
also passes the first triangle equation fixes \(U\) uniquely:
\[
 U=f(p_1)+\frac{\rho-s}{D}
             -\frac{S\xi_1(r-p_1)}{D^2\ell}.
 \tag{12}
\]
If \(U\) is sampled uniformly from \(\Theta(h)\) integers, the expected
number is therefore
\[
 O(h^2K^{5/2}).
 \tag{13}
\]
Additional in-strip, sea-color, and nondegeneracy tests only decrease it.
This removes the maximal-divisor loss from the earlier raw bound.
For polylogarithmic \(K\), it still has quadratic rather than
subquadratic order.

The same argument works on a prescribed common affine fold branch,
after replacing \(f\) by \(f\) or \(-f\). Different affine branches,
cap-constant points, and arbitrary candidate unions require their own
argument. They are not included in (13).

## 3. Unique increments on the spacing-four mesh

Fix a realized pair of total functions from
[the bounded-permutation interpolation](continuation_permuted_step_four_interpolation.md).
For one role, use its integer index function \(F\). Physical column and
row steps are now both four. The reviewed mesh has the following
properties:

1. \(|F(a)-F(b)|\le |a-b|\).
2. Equality for distinct ranks is possible only for an adjacent unit
   jump.
3. Two unit-jump edges of this role cannot be consecutive. In fact, the
   construction separates them by at least eight ranks.

These properties apply to the total virtual function. The corresponding
points need not all be selected black points.

Fix distinct partners \(p_1,p_2\) and offsets satisfying (1), now with
\(S=D=4\). There is at most one increment \(\ell\) satisfying both hub
row tests and (3).

To prove this, let two distinct increments be accepted. The case \(v=0\)
was already excluded in Section 2. Equation (4) becomes
\[
 r(\ell)=p_1+\frac{\xi_2\Delta}{4t}-\frac vt\ell.
 \tag{14}
\]
The first row tests and the first mesh property imply
\[
 |\ell_1-\ell_2|
 \le |r(\ell_1)-r(\ell_2)|
 =\frac{|v|}{|t|}|\ell_1-\ell_2|.
 \tag{15}
\]
The second row tests give \(|v|\le|t|\). Hence equality holds throughout.
The equality characterization forces \(|t|=|v|=1\), and it also forces
\[
 |r(\ell_1)-r(\ell_2)|=|\ell_1-\ell_2|=1.
 \tag{16}
\]
Both edges joining \(r(\ell_i)\) to \(r(\ell_i)+t\) must therefore be
unit-jump edges. Equation (16) makes them consecutive, contradicting
the third mesh property.

This proves uniqueness even in the presence of folds, caps, and the
allowed local permutations. It is a deterministic statement about the
realized total function. Since that function can depend on the sampled
offset, the uniqueness statement alone does not justify applying
the \(O(1/h)\) probability from (12).

## 4. The remaining counting target

The partner-first formulation leaves a concrete test: the bounded set
of increments selected by the hub row conditions must also satisfy
the large-divisor condition (5), the exact offset equation (12), and
the strip conditions. A power saving in this combined test would improve
(13).

A separate coarse affine-row deficit cannot be multiplied into (13)
without a joint counting argument. In particular, the increment selected
by the hub row condition is not an independent random divisor of
\(S\xi_1\xi_2\Delta\).

Independent review: the full written proof passed a separate review of
the signed arithmetic, nonzero divisor, bounded raw increment count,
offset-independent expectation, and the isolated-jump uniqueness proof.
