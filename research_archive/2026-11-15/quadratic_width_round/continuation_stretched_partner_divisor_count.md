# Physical divisibility counts stretched same-parity six supports

15 November 2026. A uniform two-parameter probability for a prescribed
parked triangle gives an \(h^{1+o(1)}\) expected count for long
same-parity six supports on a raw monotone row stretch. Physical
divisibility fixes the increment before the random parameters are
chosen. No affine-section deficit is needed.

The abstract theorem states its probability hypothesis explicitly.
The reviewed
[mechanical sampling lemma](continuation_mechanical_triangle_sampling.md)
supplies that hypothesis. The count does not cover arbitrary cap
plateaus or partners on different branches of a fold.

## 1. Hypotheses

Let \(f(p)=H_N(p)_\alpha\) be one coordinate of a raw Hilbert square,
where \(N=\Theta(h)\). Its physical core columns are \(Sp\), with fixed
positive integer \(S\). Let the random physical row map be \(F\).
Assume uniformly over its parameters that
\[
 c|u-v|-C\le |F(u)-F(v)|\le C(|u-v|+1).
 \tag{1}
\]
A monotone stretch with bounded positive gaps has this property.
The constants do not depend on \(h\).

Assume also that for every prescribed first hub \(r\), partner \(p\),
nonzero sea offset \(\xi\), and sea row \(s\), the probability of
the corresponding parked triangle with the required long nonzero
physical increment is at most \(P_h\). The probability bound must be
unconditional and uniform in these positional data.

Fix a common sea row and offset bound \(|\xi_i|\le CK\).
The two hubs have ranks \(r,r+t\), with
\[
 \xi_1-\xi_2=St,\qquad t\in\mathbb Z\setminus\{0\}.
 \tag{2}
\]
The support has span greater than \(h^2/K\), and the established
local-anchor reduction applies. In particular, its common physical
increment has magnitude at least \(ch/K\).
Take \(K\) to be at most a fixed power of \(\log h\).

## 2. Eliminate the random physical row values

Let the partners have ranks \(p_1,p_2\). Write
\[
 \begin{aligned}
 \delta&=F(f(r))-F(f(p_1))
        =F(f(r+t))-F(f(p_2))\ne0,\\
 v&=F(f(p_2))-F(f(p_1))
    =F(f(r+t))-F(f(r)),\\
 \Delta&=p_1-p_2+t.
 \end{aligned}
 \tag{3}
\]
Both \(\delta\) and \(v\) are integers. Subtracting the triangle
equations gives the physical version of the partner-first identity:
\[
 S^2t(r-p_1)=S\xi_2\Delta-\delta v.
 \tag{4}
\]
The first triangle itself gives
\[
 \delta\mid S\xi_1(r-p_1).
 \tag{5}
\]
Multiplying (5) by \(St\) and substituting (4) proves
\[
 \delta\mid S\xi_1\xi_2\Delta.
 \tag{6}
\]
No raw row increment or row-step factor is needed in this divisibility.

If \(\Delta=0\), then \(p_2=p_1+t\), and both core legs have the same
rank length. Hilbert locality and (1) give
\[
 |v|\le C(\sqrt{|t|}+1),\qquad
 |r-p_1|\le C h/\sqrt{|t|}\le Ch.
 \tag{7}
\]
The sea offsets and hub separation are \(O(K)\), so the whole support
would have span \(O(h+K)\). This contradicts the long-span assumption
for large \(h\). Therefore
\[
 S\xi_1\xi_2\Delta\ne0.
 \tag{8}
\]

## 3. A parameter-independent candidate list

Equation (7) gives \(|v|\le C\sqrt K\). The lower bound in (1), applied
to the partners, then gives
\[
 |f(p_2)-f(p_1)|\le C\sqrt K.
 \tag{9}
\]
Each raw coordinate row has exactly \(N\) visits. Thus, for fixed
offsets, there are at most
\[
 C N^3\sqrt K
 \tag{10}
\]
ordered partner pairs satisfying this necessary condition.

For each pair with \(\Delta\ne0\), enumerate:

1. Every signed divisor \(\delta\) of
   \(S\xi_1\xi_2\Delta\) with \(0<|\delta|<h\).
2. Every integer \(v\) with \(|v|\le C\sqrt K\).
3. The uniquely determined candidate hub
   \[
   r=p_1+\frac{S\xi_2\Delta-\delta v}{S^2t}.
   \tag{11}
   \]

Reject nonintegral and out-of-range ranks. All quantities used to
construct this list are deterministic. In particular, enumerating
the possible physical values \(\delta,v\) does not condition on the
random stretch.

Set
\[
 \mathcal D_h(K)=
 \max_{1\le n\le C K^2h^2}\tau(n).
 \tag{12}
\]
The constant can absorb the fixed stride. Equations (10)--(11) give
at most
\[
 C h^3K\,\mathcal D_h(K)
 \tag{13}
\]
candidates for fixed offsets. There are \(O(K^2)\) offset pairs,
and a fixed number of sea rows, so the total is at most
\[
 C h^3K^3\,\mathcal D_h(K).
 \tag{14}
\]

## 4. Expected count

For each candidate in (14), require its first prescribed triangle to
occur, together with its enumerated increment \(\delta\). This event
has probability at most \(P_h\). The remaining row conditions, the
second triangle, and the in-strip conditions can only reduce it.
The union bound therefore gives
\[
 \mathbb E N_{\mathrm{same}}
 \le C P_h h^3K^3\,\mathcal D_h(K).
 \tag{15}
\]
This is a witness count, so it also bounds the number of implicated
first triangles and genuine labels.

For polylogarithmic \(K\), the elementary divisor bound gives
\(\mathcal D_h(K)=h^{o(1)}\). If the independent random-stretch
argument supplies
\[
 P_h\le h^{-2+o(1)},
 \tag{16}
\]
then
\[
 \mathbb E N_{\mathrm{same}}\le h^{1+o(1)}.
 \tag{17}
\]
All signs and slopes are included. In particular, opposite-offset
reflection cases and the slope-five row-section resonances need no
separate treatment for this raw monotone-stretch count.

## 5. Scope and finite candidate extensions

The partner-row bound (9) is essential. It follows for raw monotone
stretching, and for a prescribed common injective branch with the same
bounds. It need not hold for cap-constant points or for points on
different branches of a fold. Those cases remain separate.

A fixed-size union over local rank displacements and bounded row shifts
changes the count only by a constant if (1), the hub locality bound,
and the uniform first-triangle probability hold for every listed
candidate pattern. One must enumerate the patterns before the random
parameters. This is a conditional extension, not an automatic statement
about every interpolated or capped construction.

The first-triangle probability is the only probabilistic input to
(15). There is no independence assumption between the two triangles
and no multiplication of unrelated energy estimates. Applying a
relocation budget still requires an admissible erasure and the stated
external relocation theorem.

Independent review: the complete written count passed a separate review
of the physical divisor identity, zero-difference exclusion,
parameter-independent candidate list, and expectation. The sampling
lemma has also received a separate written review.
