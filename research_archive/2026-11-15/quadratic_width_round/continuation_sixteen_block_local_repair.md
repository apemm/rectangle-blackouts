# Every aligned sixteen-label block has an internal P-free permutation

15 November 2026. The four-label obstruction does not extend to one
sixteen-label block. Every aligned four-square admits a permutation
that removes all cross-parity integral distances between its columns.
This holds for the usual full-grid rows and for the H7 residue block
with bases 1 and 28, at the constant strides specified below.

This is a local theorem. The choices made in different blocks can
create P-rivals between blocks. No simultaneous solution of those
constraints, or exclusion of the other support families, is claimed.

Independent review checked the classifications, the 7-adic cases,
alignment, and the explicit words. A separate exact run regenerated
all 1468 nonempty offset systems at the four saved strides and verified
their witnesses. The all-stride claims use the proof, not this sample.

## 1. Statement and notation

The block labels are
\[
 (I+i,J+j),\qquad 0\le i,j\le3,
\]
where \(I,J\) are divisible by four. Their black rows are
\(1+D(I+i)\) and \(D+D(J+j)\). The sixteen physical columns
are consecutive slots \(S(R+r)\), \(0\le r<16\).

An internal P candidate is a cross-parity pair at distinct slots
whose Euclidean distance is integral. There is a permutation with no
internal P candidate in either of these cases:

1. \(D=2\) and \(S\ge32\) is a power of two.
2. \(D=28\) and \(S=6272\sigma\), where \(\sigma\ge16\) is
   a power of two.

For simultaneous use with the earlier same-parity locality exclusion,
take \(S\ge1024\) in the first case and \(\sigma\ge32\) in the
second. Those larger choices meet the displacement cost for blocks
of size sixteen.

Put \(T=J-I\). The signed even-minus-odd row difference is
\[
 W=D(T+\delta)+D-1,
 \qquad \delta=j'-i\in[-3,3].
\tag{1}
\]
A candidate at slot gap \(q\), \(1\le q\le15\), forbids both
cross-incidences \(j'-i=\delta\) and \(j-i'=\delta\) between
the labels placed at distance \(q\). Write such a condition as
\((q,\delta)\).

## 2. The full-grid classification

Let \(A=S^2/4\). If \((Sq)^2+Y^2=L^2\) with \(Y\) odd,
the two integers \((L-Y)/2,(L+Y)/2\) have opposite parity and
product \(Aq^2\). Their odd member is a divisor \(a\mid q^2\).
Since \(a\le225<A\), the even member is larger. Consequently
\[
 Y=Av-a,\qquad av=q^2,\quad a\text{ odd},\quad v\ge1.
\tag{2}
\]
All these heights exceed 12. Thus candidates in the row window (1)
have the same sign. Their absolute heights differ by at most 12.
Different values of \(v\) differ in height by at least
\(A-224>12\). Hence all candidates in one block have one value
of \(v\).

Write \(v=ct^2\) with \(c\) squarefree. The condition that
\(a=q^2/v\) is an odd integer gives
\[
 c\text{ odd},\qquad q=ctk,\qquad a=ck^2,
 \qquad k\text{ odd}.
\tag{3}
\]
Distinct positive odd squares differ by at least eight. After the
first pair \(1,9\), their consecutive gaps are at least sixteen.
Since the allowed range of \(a\) has width 12, two distinct gaps
can occur only with
\[
 c=1,\qquad (q,a)=(t,1),(3t,9),\qquad 1\le t\le5.
\tag{4}
\]
There cannot be a third gap.

Alignment reduces (4) to a single pattern. For positive signed
heights, the offset at gap \(t\) satisfies
\[
 T+\delta=S^2t^2/8-1\equiv-1\pmod4.
\]
The other offset is \(\delta-4\). Since both lie in \([-3,3]\)
and \(T\equiv0\pmod4\), they must be 3 and \(-1\).
For negative signed heights, the first offset is zero modulo four
and the second is larger by four, so both cannot fit in the window.
Therefore every aligned full-grid block has no condition, one
condition, or exactly
\[
 (t,3),\qquad(3t,-1).
\tag{5}
\]

## 3. The H7 classification, including the odd factor of the stride

Write \(S=2^s7^2\), so \(s\ge11\), and put
\(A=2^{2s-2}\), \(C=7^4=2401\). The same factorization gives
\[
 Y=Av-a,\qquad av=Cq^2,
\tag{6}
\]
where \(a\) is odd. Here
\[
 a\le225C=540225,
 \qquad A\ge1048576.
\]
The even factor exceeds the odd one. Every height exceeds 168,
and different \(v\)'s differ in height by more than 168. Thus
the row window (1), now of width 168, again has one sign and one
value of \(v\).

The row residues make \(7\nmid Y\). Hence the full 7-adic
valuation of \(av=Cq^2\) belongs to exactly one of \(a,v\).
If \(v\) is coprime to seven, every candidate \(a\) is divisible
by 2401. Two such values cannot differ by at most 168 unless they
are equal, which also makes \(q\) equal.

Otherwise \(a\) is coprime to seven. If \(7\mid q\), the only
possibilities are \(q=7,14\); they cannot have the same \(v\),
because their 2-adic valuations differ and \(a\) is odd. These
values also cannot share \(v\) with a gap coprime to seven.
Therefore a block with two distinct candidate gaps has
\(7\nmid q\), \(a\mid q^2\), and
\[
 Y=(S^2/4)(q^2/a)-a.
\tag{7}
\]

For positive signed heights, (1) and (7) require
\(a\equiv1\pmod{28}\). Among odd divisors of \(q^2\),
\(1\le q\le15\), these values are exactly
\[
 a=1,169,225.
\tag{8}
\]
For negative signed heights the required residue is \(-1\),
whose only such divisor is \(a=27\), occurring at \(q=9\).
These short divisor lists follow by checking the residue classes
between 1 and 225; every excluded number has a prime factor greater
than 15 or requires \(q>15\).

Two distinct values in (8) can share \(q^2/a\) only in the
family \((q,a)=(1,1),(13,169),(15,225)\). The first and last
heights differ by 224, so the window cannot contain all three.
The remaining pairs have height gaps 168 and 56.

Before imposing alignment their conditions are
\[
 \{(1,3),(13,-3)\},
 \quad\text{or}\quad
 \{(13,u),(15,u-2)\},\qquad -1\le u\le3.
\]
For the second pair,
\[
 T+u=S^2/112-7\equiv1\pmod4,
\]
so alignment forces \(u=1\). Every aligned H7 block therefore
has at most one condition, or one of the two patterns
\[
 \{(1,3),(13,-3)\},\qquad
 \{(13,1),(15,-1)\}.
\tag{9}
\]

## 4. Explicit permutations

Encode label \((i,j)\) by \(4i+j\). The cyclic word
\[
 0,6,7,2,3,11,1,9,13,14,4,8,12,5,10,15
\tag{10}
\]
has both cross-differences nonzero modulo four across every adjacent
pair, including its last and first entries. Replacing every second
coordinate \(j\) by \(j+\delta\pmod4\) makes both
cross-differences different from \(\delta\pmod4\).

For one condition \((q,\delta)\), the graph of physical slot
pairs at distance \(q\) is a disjoint union of paths. List those
paths consecutively and place consecutive segments of the shifted
word (10) along them. Every constrained pair is then safe. This
gives one uniform rule for all single-gap cases.

The remaining patterns have these explicit words:

| Pattern | Word |
|---|---|
| \((1,3),(3,-1)\) | 0, 1, 2, 8, 3, 4, 10, 5, 9, 6, 7, 12, 11, 13, 15, 14 |
| \((1,3),(13,-3)\) | 0, 1, 2, 4, 3, 5, 6, 7, 8, 9, 10, 12, 13, 11, 14, 15 |
| \((13,1),(15,-1)\) | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12, 14, 15 |

For the first word, the sets of cross-differences at gaps 1 and 3
are respectively
\[
 \{-2,-1,0,1,2\},\qquad\{-3,-2,0,1,2,3\}.
\]
For the second word, the sets at gaps 1 and 13 are
\[
 \{-3,-2,-1,0,1,2\},\qquad\{-2,-1,2,3\}.
\]
For the third word, the sets at gaps 13 and 15 are
\[
 \{-3,-2,-1,0,2,3\},\qquad\{-3,3\}.
\]
Each set omits its forbidden value. To handle (5), divide the
physical slots into their gap-\(t\) paths and fill them with
consecutive segments of the first word. Gap \(3t\) pairs lie
three steps apart within one such path, so both constraints remain
satisfied. This proves the theorem.

## 5. Verification and the remaining global problem

The companion checker verifies the explicit permutation witnesses and
enumerates all odd factorizations for every gap \(q\le15\).
At full-grid strides 1024 and 2048 it checks all 600 nonempty offset
systems, including nonaligned origins. At H7 strides 100352 and
200704 it checks all 134 nonempty offset systems. Every system has
at most two conditions and has a verified witness. The proof above
establishes the classifications for all stated strides.

An internal P-free choice can now be made in every full sixteen-label
block. The unresolved problem is to coordinate those choices across
blocks while excluding interblock P and the other residual families.
Incomplete blocks created by deletion or interval cuts also require
separate handling. This note proves no global quadratic-width bound.
