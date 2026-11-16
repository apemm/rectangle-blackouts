# Full occupancy and bounded Hilbert permutations remove FW

15 November 2026. This is a conditional improvement to the H7 placement
model. A full arithmetic interval of label columns removes FW. Bounded
permutations preserve the same-parity geometric exclusions at constant
stride cost. The other residual families, including 6PT, remain to be
solved. No full-board or quadratic-threshold theorem is claimed.

Independent review: the displacement bound, FW exclusion, and the
arithmetic 6PT example were checked separately and passed.

## 1. The placement model

Take a contiguous interval of \(N\) original Hilbert ranks, containing
only genuine labels of one H7 residue block. Subtract its initial rank
and call the resulting ranks \(r=0,\ldots,N-1\). The physical rows of
label \((i,j)\) are \(a_0+Di,b_0+Dj\), where \(D=28\). They satisfy
the H7 bulk and row-alignment hypotheses.

Partition these ranks into consecutive blocks of size at most \(b\).
Within each block choose any permutation \(\pi\), and put label \(r\)
in column

\[
 x_r=x_0+S\pi(r),\qquad S=8D^2\sigma,
 \quad \sigma\text{ a power of two},\quad \sigma\ge2b-1. \tag{1}
\]

Every column \(x_0+Sk\), \(0\le k<N\), contains exactly one label.
Every other core column retains the H7 period-seven sea. In particular,
the row-\(F\) point is removed at every occupied column.

## 2. The same-parity inequalities survive

For distinct labels let \(d=|\pi(r)-\pi(r')|\ge1\). Since each label
moves by at most \(b-1\),

\[
 |r-r'|\le d+2(b-1)\le(2b-1)d. \tag{2}
\]

The audited Hilbert locality bound then gives, for either same-parity
row difference \(Y\),

\[
 Y^2<16D^2(2b-1)d
 =\frac{2(2b-1)}\sigma |x_r-x_{r'}|
 =\frac2{\sigma_{\rm eff}}|x_r-x_{r'}|,
 \quad \sigma_{\rm eff}=\frac\sigma{2b-1}\ge1. \tag{3}
\]

Consequently the H7 same-parity distance exclusion, same-parity
right-angle exclusion, and all-same-parity mixed-support exclusion
remain available. Arguments that use the quantitative locality
constant must use \(\sigma_{\rm eff}\), not the original \(\sigma\).
The archived absence-threshold constants are not asserted unchanged.

All label columns are still congruent modulo \(S\). The row residues,
mod-four alignment, and valuations of \(S\) are unchanged. Thus the
modular exclusions and the one-label profile hypotheses are preserved.
The geometric H7 reduction still leaves only

\[
 P,\quad\Lambda_3,\quad\Lambda_4,\quad R2s,\quad FW,\quad 6PT.
\]

This assertion uses the structural reduction and its audited profile
and collar hypotheses. It does not transfer any private-choice
certificate to the permutation model.

## 3. FW is empty

Suppose an FW triangle had label vertex \(A\), same-parity label end
\(C=A+(X,\delta)\), and sea end

\[
 B=A+(\xi,F-y_A),\qquad X\xi=-\delta(F-y_A).
\]

Its fourth corner is \(W=C+(\xi,F-y_A)\), in an occupied column.
The case \(\delta=0\) would force \(\xi=0\), placing the supposed
row-\(F\) sea point in \(A\)'s occupied column, and is impossible.
Since both \(C\) and \(W\) have occupied columns, \(S\mid\xi\).
Also \(S\mid X\). H7 alignment gives

\[
 v_2(F-y_A)\le1,\qquad 7\nmid(F-y_A).
\]

The only prime divisors of \(S\) are two and seven. Therefore

\[
 \frac{S^2}{2}\mid\delta. \tag{4}
\]

For the original H7 profiles, \(F\le23952\), whereas
\(S^2/2\ge6272^2/2=19668992\). The nonzero \(\delta\) cannot be
negative when \(y_W=F+\delta\ge1\). Hence \(\delta>0\). Bulk rows
satisfy \(y_A>F\), so \(X\xi>0\).

It follows that the source column \(x_A+\xi\) lies strictly between
\(x_A\) and \(x_W=x_A+X+\xi\). Both endpoints are in the full
occupied arithmetic interval. The source is on the same arithmetic
lattice, so it too is occupied. Its row-\(F\) point was removed and no
bulk label contains row \(F\), contradicting that \(B\) is black.

Thus FW is absent, including near the endpoints of the occupied
interval. No assumption about the permutation chosen inside a block
enters this argument.

## 4. What remains of 6PT-same

Two parked triangles sharing an offset \(\xi\) have a common label
hub \(f\). Their equations are

\[
 X\xi=-\delta(s-a_e),\qquad
 X'\xi=-\delta(s-b_{e'}),
\]
\[
 a_f-a_e=b_f-b_{e'}=\delta,
 \qquad W=(x_f+\xi,s+\delta). \tag{5}
\]

If \(S\mid\xi\) and the column of \(W\) lies inside the occupied
interval, then it is a label column, and Section 3 rules out either
triangle as FW. This does not cover an exterior \(W\), or offsets not
divisible by \(S\). In particular, offsets of low and high sea columns
are never divisible by \(S\).

Full occupation alone does not remove this residual possibility.
For an explicit arithmetic example put \(S=6272\), \(L=15\),
\(\delta=3S=18816\), and \(\xi=3\). Use three labels

\[
 e=(20000,10672),\quad e'=(20672,10000),\quad f=(20672,10672)
\]

with physical row bases \(a_0=1,b_0=2\), at occupied slot indices

\[
 k_e=0,\qquad k_{e'}=279999,\qquad k_f=559986. \tag{6}
\]

Their relevant rows are

\[
 a_e=560001,\quad b_{e'}=280002,\quad
 a_f=578817,\quad b_f=298818.
\]

Then

\[
 X=S\cdot559986,\quad X'=S\cdot279987,
\]

and both equations (5) hold. The two sea points have columns
\(3\) and \(S\cdot279999+3\), and row 15. The common white corner
is \((S\cdot559986+3,18831)\). All three are low-sea columns modulo
seven. The six required black cells are distinct, and both triangles
are parked at the same white corner. Filling every arithmetic slot
from zero through 559987 leaves these off-lattice sea points intact.

This pattern respects the H7 row residues and mod-four alignment with
\(g=3\), \(F=2019\), and a high row congruent to four modulo 28.
These statements concern the residue conditions, not the separate
one-label square filters. For the three displayed labels, their coordinate differences
are at most 672, whereas their slot differences are at least 279987.
Thus they satisfy even the original Hilbert pairwise locality bound.

This is an arithmetic occupancy example, not a claimed embedding of
these three prescribed coordinates at the ranks (6) in the actual
Hilbert curve. This pattern is not excluded by full occupancy or by the
pairwise locality tests on its three involved labels. It does not
construct a globally local assignment of all the other labels. An
actual Hilbert exclusion would need additional structure.

## 5. Conditional gain and outstanding obligations

The model removes FW and keeps the known structural exclusions at
constant cost. Since the smallest power of two at least \(2b-1\) is
less than \(4b\), its core width is \(O(bN)\). For fixed \(b\) and
\(N=O(h^2)\), this is quadratic.

A full construction would still have to solve the five residual
families \(P,\Lambda_3,\Lambda_4,R2s,6PT\) in the same permutation
assignment, and then verify the applicable global collars and joins.
The constraints within a permutation block are correlated and are not
the independent choices used by previous greedy certificates.
In particular, the four-system reduction for the original private-choice
candidate P graph is not asserted for this new permutation P problem.

Finally, every rank in the interval must hold a genuine label.
Padding cells, deleted exceptional labels, or compressed ranks are not
allowed without a new argument. Splitting into many full intervals
also requires accounting for their collars; a separate global-height
collar for every interval can destroy the quadratic width estimate.
