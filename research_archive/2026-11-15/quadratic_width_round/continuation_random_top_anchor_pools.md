# Independent anchor pools near the strip edge

15 November 2026. The required random anchors exist in a window of length
\(E=h^{23/24}\), with atom bounds \(h^{-23/24+o(1)}\). The even anchor
can retain the prime-gap collar condition. Both anchors can be sampled
independently of the mechanical row partitions and then inserted into
their classes. This is a sampling lemma; it does not establish the remaining
six-point estimates or the global residual choice.

## 1. The prime input

For fixed odd \(a\bmod4\), uniformly for \(x\asymp h\) and
\(H\asymp h^{23/24}\),
\[
 \#\{p\text{ prime}:x-H<p\le x,\ p\equiv a\pmod4\}
   =(1+o(1))\frac{H}{2\log h}.                         \tag{1}
\]
This follows from Theorem 1.1 of Thorner and Zaman,
[*Refinements to the prime number theorem for arithmetic progressions*](https://arxiv.org/pdf/2108.10878),
with fixed modulus 4. Its worst threshold exponent is \(32/37<23/24\).
Any exceptional zero is fixed below 1, so the theorem's factor
\(\lambda\) tends to 1; its relative error tends to zero. Dividing the
log-weighted asymptotic by \(\log h+o(1)\) gives (1). Section 1.2 of the
same paper also explicitly gives the fixed-small-modulus short-interval
asymptotic with threshold \(7/12+\varepsilon\).

No assertion about primes in a mechanical or Beatty class is used.

## 2. Good pools in the upper window

Fix a low odd sea row \(s=O(1)\). Let \(\beta\) be the required even
residue modulo 4 and \(\gamma\) the required odd residue. Put
\[
 E=\lfloor h^{23/24}\rfloor,
 \qquad I_h=\{h-E,\ldots,h-2\}.
\]
The exclusion of the top two rows leaves room for the adjacent-row collar.
Let \(B_0,B_1\) be fixed excluded physical-row sets, independent of the
subsequent anchor and mechanical sampling, with
\[
 |B_0|+|B_1|\le h^{5/6+o(1)}.                         \tag{2}
\]
Fixed-radius enlargements of the original bad sets are allowed in (2).
Assume that the original row pools contain their indicated residue classes
throughout \(I_h\). This holds for the low-sea upper-half odd pool and the
full even pool once \(h\) is sufficiently large.

Define
\[
 \mathcal A_0=\{b\in I_h\setminus B_0:
       b\equiv\beta\pmod4,\ b-s\text{ is prime}\},
\]
\[
 \mathcal A_1=\{a\in I_h\setminus B_1:
       a\equiv\gamma\pmod4\}.
\]
Then
\[
 |\mathcal A_0|=(1+o(1))\frac{E}{2\log h},
 \qquad |\mathcal A_1|=(1+o(1))\frac E4.              \tag{3}
\]
Indeed \(b-s\equiv\beta-s\pmod4\) is a reduced odd residue, so (1)
counts the unexcluded even candidates. The excluded number is at most
\(|B_0|\), and
\[
 h^{5/6+o(1)}=o(E/\log h)
\]
because \(23/24-5/6=1/8\). The odd count is elementary.

Every even candidate satisfies, for sufficiently large \(h\),
\[
 p=b-s\text{ odd prime},\qquad p^2>2h,
 \qquad b>(h+s)/2.                                  \tag{4}
\]
Thus the two-level \(s,b\) connector in
[the collar note](continuation_lipschitz_collar_graphs.md) retains its
in-strip triangle and P exclusions. The whole prime pool lies in the same
fixed even residue; a random collar anchor does not change that profile.

## 3. Independence and insertion

Sample \(A_0,A_1\) independently and uniformly from these two pools.
Independently sample both mechanical parameters and both raw-coordinate
offsets. Then
\[
 \sup_b\Pr(A_0=b)=O(\log h/E),\qquad
 \sup_a\Pr(A_1=a)=O(1/E).                           \tag{5}
\]
The same bounds hold conditionally on all mechanical parameters and raw
offsets, and the two anchor values remain independent under that
conditioning. Conditioning on an event that itself depends on an anchor
does not preserve these statements automatically.

After this sampling, insert each prescribed physical anchor into each
class of its own parity as in
[the anchor-insertion lemma](continuation_mechanical_anchor_insertion.md).
The inserted occurrence is nongenuine if it was absent from that class.
This creates only \(O(h)\) virtual objects. Each occurrence index changes
by at most one, the largest physical gap does not increase, and
\(p_i=\alpha i+O(1)\) remains uniform over the random anchor. The original
genuine labels are still covered exactly once. Choose padded sizes and
offset intervals from the maximum possible modified class sizes, so those
intervals remain independent of the sampled anchors and parameters.

The anchor index in a realized class is allowed to depend on all these
values. Consequently an estimate involving a constant fold branch must
be proved using its actual anchor value; it cannot be replaced by an
independent raw class index. Formula (5) supplies the appropriate atom
bound without making that replacement.

All conditional cap-area and bad-preimage bounds in the insertion lemma
are uniform in the chosen good anchors. They can therefore be averaged
jointly with new nonnegative costs, with no resampling or selection of
anchors after observing those costs.

## 4. Long partners and the numerical margin

Suppose the low-sea long-PT parametrization has a positive row increment
\(\delta\), with partner row \(y\) and hub row \(y+\delta\). If the
partner equals either anchor, then
\[
 0<\delta\le h-y\le E.                             \tag{6}
\]
For any fixed or polylogarithmic \(K\), every long event with
\(\delta\ge c h/K\), \(c>0\) fixed, therefore has no anchor partner
once \(h\) is sufficiently large. Anchors can still be hubs.

Here is the precise probability consequence available for such hub
events. Condition on parameters independent of one anchor \(A\) and one
uniform offset \(U\) whose range has size \(\Theta(h)\). If a fixed
event has at most \(C\) admissible pairs \((A,U)\), then (5) gives
\[
 \Pr(\text{event}\mid\text{conditioned parameters})
       =O(\log h/(hE)).                            \tag{7}
\]
It is enough that one equation gives \(O(1)\) possible physical anchor
values and, for each, a nonconstant partner equation gives \(O(1)\)
offsets. A single equation coupling \(A\) and \(U\) is insufficient.
Adaptive cap selection can be handled by enumerating candidate cap forms
before applying (7), provided their number and the two-equation fiber
bound are proved separately.

Thus an independently established count \(h^{3+o(1)}L\) of forms,
with \(L=h^{15/16}\) and fibers satisfying (7), would contribute at most
\[
 h^{3+o(1)}L/(hE)=h^{95/48+o(1)}=o(h^2).            \tag{8}
\]
Likewise the previously proposed stub-P expression
\(h^{3/2+o(1)}\sqrt E\), if applicable to the sampled model, is
\(h^{95/48+o(1)}\). These exponent identities do not replace the
separate event-count and fiber proofs.

The same statements hold for a high-sea core after reflecting physical
rows. Reflection can interchange absolute parities; the reflected pool
is defined using the reflected residue and the prime difference to the
high sea, rather than by retaining the names ``even'' and ``odd''.

## Review status

The short-interval input was checked directly in the cited primary
paper and independently checked there again by a second reader. The
pool count, removal of the bad rows, independent sampling and insertion,
and the joint-fiber qualification passed that reader's written review.
