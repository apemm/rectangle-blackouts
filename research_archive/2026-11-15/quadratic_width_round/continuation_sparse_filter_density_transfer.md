# Logarithmic potential-type density survives sparse common pack filters

15 November 2026. The dense translated patch survives a common physical
pack filter deleting at most \(C\sqrt h\) pack indices. A sufficiently
large fixed stride allows a clean patch interval and clean owners to be
chosen together. The patch then embeds in the compressed triangular order.

The result gives bad examples among nearby choices of band width and tail
crop. It disproves a bounded weighted-degeneracy claim uniform over that
whole scaffold family. It does not prove that every choice is bad, or that
the permutation constraints are unsatisfiable. Positive-density pack
partitions are outside the hypotheses.

Independent review checked the averaging bound, the dyadic crop,
affine compression, protected owners, and the potential-type
interpretation. The proof passed without corrections.

## 1. Precise model and conclusion

Fix an even physical pack step \(D_0\), opposite-parity residue bases
\(1\le a_0,b_0\le D_0\), and a stride \(S_0\) divisible by four.
For packed \(k\times k\) tiles these parameters are
\(D_0=kD\) and \(S_0=k^2S\); internal slot zero is used to define
the potential edges.

Among the physical pack indices
\[
 0,1,\ldots,M-1,\qquad M=\lfloor h/D_0\rfloor,
\]
let \(B_h\) be a common bad set with
\[
 |B_h|\le C\sqrt h.
\tag{1}
\]
Write the remaining list as \(g_0<\cdots<g_{m-1}\). Fix any integer
baseline band width \(c_*\) with
\[
 \sqrt h=o(c_*),\qquad c_*=o(h).
\tag{2}
\]
There is a constant lower bound on \(S_0\), depending only on
\(C,D_0\), such that the following holds for all sufficiently large
\(h\). For example,
\[
 S_0\ge10^{12}(C+1)^2D_0^2
\tag{3}
\]
is more than sufficient.

One can choose
\[
 c=c_*+O(\sqrt h)
\]
and discard only \(O(\sqrt h)\) additional indices from the end of
the good list so that the resulting upper and lower compressed
triangular orders have a genuine potential-P subgraph with
\(\Theta(h)\) vertices and \(\Omega(h\log h)\) edges. All its
slot gaps are \(\Theta(h)\), and all required owners remain in the
lower triangle.

The constants in the asymptotic notation may depend on the fixed
parameters. The potential-type graph therefore has unbounded
degeneracy. For \(k=4\), no uniform two-type peeling theorem holds
over this entire sparsely filtered family.

## 2. Choose a dyadic parent without a large crop

Let \(K\) be the largest power of two not exceeding
\(\sqrt{hS_0}/D_0\), and put
\[
 n=\left\lfloor\frac{m-c_*}{K}\right\rfloor-1,
 \qquad N=Kn.
\tag{4}
\]
For large \(h\),
\[
 n\asymp\sqrt{h/S_0},\qquad
 |T_n|\asymp h/S_0,
 \qquad K\asymp\sqrt{hS_0}/D_0.
\]
More precisely, the lower limit of \(n/\sqrt{h/S_0}\) is at least
one, and its upper limit is at most two. Thus the translated density
proof applies unchanged: \(|T_n|\) exceeds \(h/(7S_0)\) for large
\(h\), while each counted gap is below \(h/(14S_0)\).

Equation (4) reserves at least \(K\) good indices beyond \(N+c_*\).
Condition (3) ensures \(K>16n\) for large \(h\). Therefore every
choice \(|c-c_*|<8n\) satisfies
\[
 N+c\le m,
 \qquad m-(N+c)=O(K+n)=O(\sqrt h).
\tag{5}
\]
The parent order can be \(G_N\), because \(N\) is a dyadic
multiple of \(n\), without discarding a linear fraction of the rows.

## 3. Shift a dense patch away from the bad packs

Apply the translated-patch density proof with step \(D_0\), stride
\(S_0\), and the fixed order \(G_n\). It gives one translation
\[
 h/(4D_0)\le T\le h/(2D_0)
\]
and a set \(E\) of \(\Omega(|T_n|\log h)\) genuine potential
edges. The set of edges and their Pythagorean vectors do not depend
on a common horizontal index origin \(I\).

Vary that origin over the integer interval
\[
 \mathcal I=
 [\lceil h/(5D_0)\rceil,\lfloor h/(4D_0)\rfloor].
\tag{6}
\]
Its length is at least \(h/(25D_0)\) for large \(h\). All the
strip and owner margins in the density proof remain linear in \(h\)
throughout this interval.

Call the whole patch clean when both integer intervals of radius
\(20n\) about \(I\) and \(I+T\) contain no bad pack. For an
edge \(e\in E\), its two owner indices have the form
\[
 I+\alpha_e,\qquad I+\beta_e,
\tag{7}
\]
where the offsets are fixed integers. Call the edge protected when
the radius-\(20n\) intervals around these two indices also avoid
\(B_h\).

For any one of these four intervals, a fixed bad pack excludes at
most \(40n+1\) choices of \(I\). Hence, for each edge, the number
of origins where the patch is not clean or the edge is not protected
is at most
\[
 4(40n+1)C\sqrt h.
\tag{8}
\]
By (3), (4), and (6), this is less than one quarter of
\(|\mathcal I|\) for large \(h\). Averaging the number of
protected edges over \(I\) shows that some origin has a clean
patch and at least \(3|E|/4\) protected edges. No independence
assumption is used.

## 4. Compression is affine on the protected intervals

For that origin let \(g_\alpha=I\), \(g_\beta=I+T\). Cleanliness
gives exact identities
\[
 g_{\alpha+t}=I+t,\qquad
 g_{\beta+t}=I+T+t
 \qquad(|t|\le20n).
\tag{9}
\]
Also \(\beta-\alpha=T+O(\sqrt h)\), by (1).

In the parent triangle \(T_N\), consider the point
\[
 P=(\alpha,\beta-\alpha-c_*).
\]
It lies inside the triangle, a linear distance from the boundary:
\(\alpha\) is near \(h/(5D_0)\) to \(h/(4D_0)\),
\(\beta-\alpha\) is near \(T\), and \(N\sim h/D_0\).
The identity-child lemma from
[the recursive embedding note](continuation_dense_patch_recursive_embedding.md)
gives a side-\(n\) child with origin \((U,V)\) and
\[
 |U-\alpha|<8n,\qquad
 |V-(\beta-\alpha-c_*)|<8n.
\]
Set
\[
 c=\beta-\alpha-V.
\tag{10}
\]
Then \(|c-c_*|<8n\), so the crop in (5) is valid.

The physical pack indices of this child's labels are
\[
 g_{U+u_r},\qquad g_{U+c+V+u_r+v_r}.
\]
Using (9), these equal
\[
 I+\Delta+u_r,\qquad
 I+T+\Delta+u_r+v_r,
 \qquad \Delta=U-\alpha,
\tag{11}
\]
because \(|\Delta|<8n\) and \(u_r+v_r<n\). Thus the entire
dense patch is preserved exactly, up to one common physical
translation by \(\Delta\) pack indices. Its order is \(G_n\),
and its columns are consecutive in the parent run.

For every protected edge, both owner indices in (7), shifted by
\(\Delta\), remain good. They also survive the tail crop: the
density proof places their physical rows a linear distance from
both boundaries, whereas the crop has only \(O(\sqrt h)\)
indices. Their compressed index difference is \(\Theta(h)\),
even after subtracting the at most \(C\sqrt h\) missing indices.
Since \(c=o(h)\), they belong to the lower compressed triangle.
The common corners remain white inside the patch and remain in the
strip, with linear margins. All protected potential edges are genuine.

## 5. Interpretation

The theorem transfers the logarithmic density through the common
square filters, because their bad-pack count is only \(O(\sqrt h)\).
The extra band adjustment and tail crop cost \(O(h^{3/2})\) labels.
This is a counting statement, not a separate relocation theorem.

It establishes bad examples among allowed nearby choices. A specially
selected band might behave better. The conclusion also concerns the
graph of all potential types, not unsatisfiability of the permutation
system. Finally, positive-density random pack partitions do not satisfy
(1), so their proposed smoothing mechanism is not addressed here.
