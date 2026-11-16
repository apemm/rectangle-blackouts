# Deep reflection centers have subquadratic expected cost

15 November 2026. In the equal-hub-row, opposite-offset six-point
family, centers with a large power-of-two divisibility can be counted
directly. The estimate includes partners in different aligned Hilbert
blocks. It therefore extends beyond the exact aligned-block reversals
counted in
[the earlier reflection note](continuation_dyadic_reflection_six_count.md).

## 1. Reflection identity

Use the final spacing-four rank coordinate. Let the hubs have ranks
\(r,r+t\), and let the nonzero sea offsets obey
\(\xi_1=-\xi_2=\xi\). A common completion gives
\[
 2\xi=4t,\qquad \xi=2t.
 \tag{1}
\]
The completion is a sea-column residue, so \(\xi\not\equiv0\pmod4\).
Consequently \(t\) is odd. If the hub rows are equal, the exact
triangle subtraction gives
\[
 p_1+p_2=2r+t=:c.
 \tag{2}
\]
Thus \(c\) is odd. The first partner fixes the second partner exactly.
The long-support theorem bounds \(|t|\le CK\), where the support span
exceeds \(h^2/K\).

## 2. Counting centers with a deep dyadic valuation

The core has \(n\le C_0h^2\) ranks. Fix a power of two \(B\ge2\),
and retain only witnesses for which
\[
 B\mid c+1=2r+t+1.
 \tag{3}
\]
For fixed odd \(t\), this places \(r\) in one residue class modulo
\(B/2\). There are at most \(2n/B+1\) such hubs. For each hub,
there are at most \(n\) choices of \(p_1\), and (2) fixes \(p_2\).
Invalid endpoints are discarded.

Hence the positional candidate count, over all permitted offsets, is
\[
 O\!\left(K(h^4/B+h^2)\right).
 \tag{4}
\]
This estimate uses neither the row-visit bound nor independence between
the two triangles.

## 3. The one-offset probability

The following candidate-union hypotheses are those of the reviewed
folded-cap construction and its fixed-size interpolation:

* One row offset \(U\) is uniform on an interval of \(\Theta(h)\)
  integers.
* At each rank, the row of the selected parity belongs to \(O(\log h)\)
  predetermined candidates. Each is affine in \(U\), with slope
  \(D\) or \(-D\), or is a fixed anchor row plus a bounded integer.
* All fixed candidates of this parity differ by \(O(1)\). The possible
  within-block permutations and interpolation shifts have fixed size.
* Long supports require their nonzero core row increment to have
  magnitude at least \(ch/K\).

The candidates are enumerated before conditioning on which caps or
permutations are selected. External collar points with unrelated fixed
rows are not included in this statement.

For a positional candidate, use only its first triangle equation:
\[
 X\xi=(C(U)-A(U))(A(U)-s),
 \tag{5}
\]
where \(X=4(r-p_1)\ne0\), \(A\) is the partner row, and \(C\) the
hub row. For each pair of candidate formulas, the right side is a
polynomial of degree at most two.

If the formulas have opposite nonzero slopes, the quadratic coefficient
is nonzero. If only \(A\) is affine, the same is true. If both formulas
have the same nonzero slope, the right side is either nonconstant
linear or identically zero. The latter cannot equal \(X\xi\ne0\).
If only \(C\) is affine, the right side is nonconstant linear unless
\(A=s\), which again makes (5) impossible.

If both formulas are fixed, their difference is \(O(1)\), contrary to
the long-increment condition for polylogarithmic \(K\) and large \(h\).
Thus each eligible formula pair allows at most two offsets.
The probability of a candidate is at most
\[
 C\log^2 h/h.
 \tag{6}
\]
The second triangle and the equal-hub-row condition can only reduce it.
This is an unconditional candidate-union estimate. It does not condition
on a selected cap configuration.

Combining (4) and (6) proves
\[
 \mathbb E\,N_{\mathrm{deep}}(B)
 \le CK\log^2h\,(h^3/B+h).
 \tag{7}
\]
For any fixed \(\varepsilon>0\), choose a dyadic
\(B\asymp h^{1+\varepsilon}\). With polylogarithmic \(K\), this is
\[
 h^{2-\varepsilon+o(1)}+h^{1+o(1)}=o(h^2).
 \tag{8}
\]
As with the other incidence estimates, realizing a relocation budget
also requires a valid support erasure and the cited relocation input.

## 4. What remains after this count

Equation (7) disposes of all sufficiently deep centers, regardless of
whether their partners form an exact aligned-block reversal. The
unresolved reflection family can therefore be restricted to
\[
 v_2(2r+t+1)<(1+\varepsilon)\log_2 h+O(1).
 \tag{9}
\]
This restriction alone is not a power saving for the remaining centers.
It supplies a precise complement to a future carry or row-section
argument. No bound for arbitrary reflection centers, unequal hub rows,
or the full same-parity six-point family follows from (7).

Independent review: the full written center count and the stated
affine-candidate probability argument passed a separate review.
