# Quadratic columns on additive dyadic matchings

Let \(h=2N\), where \(N\) is a power of two. In [the dyadic matching construction](dyadic_matching_blocks.md) use
\[
 \pi_t(j)=[j+t]_N,\qquad
 \sigma_t(j)=[j+2u_t j^2]_N,
\]
where \([z]_N\) is the representative in \([0,N-1]\) and \(u_t\) is any odd integer. The matchings cover all row pairs. Since
\[
 (i+2u_t i^2)-(j+2u_t j^2)=(i-j)(1+2u_t(i+j)),
\]
the column map preserves the valuation of every nonzero difference modulo \(N\), so it is a dyadic isometry. Each block keeps the tilted-triple and nonvertical mixed exclusions.

## Copies of a Pythagorean vector

Consider a fixed signed displacement from the even point of label \(j\) to the odd point of label \(i\). Its actual horizontal component is \(8r\), with \(r=\sigma_t(i)-\sigma_t(j)\), and its signed vertical component is \(d=2i-2\pi_t(j)-1\). The vertical value determines
\[
 s=i-j\equiv t+(d+1)/2\pmod N .
\]
The horizontal equation now gives a linear congruence in the starting index,
\[
 r\equiv s(1+2u_t s+4u_t j)\pmod N .
\]
Take \(q=v_2(r)\). If a nonzero horizontal displacement occurs, \(v_2(s)=q\). All possible \(j\) belong to one residue class modulo
\[
 N/\gcd(N,4s).
\]
There are at most \(4\cdot 2^q\) of them.

If the vector has integral norm \(z\le h-1\), the integer \(d\) is odd and
\[
 ((z-|d|)/2)((z+|d|)/2)=16r^2.
\]
The two factors have opposite parities, so \(16\cdot2^{2q}+1\le z\). In particular \(\gcd(N,4s)\le4\cdot 2^q<\sqrt h\). Distinct occurrences of the same signed Pythagorean vector in this matching therefore have their even starting indices at distance greater than \(N/\sqrt h\). Their physical starting columns are separated by more than \(8N/\sqrt h\), since \(\sigma_t\) preserves the valuation of nonzero differences. This excludes repeated signed vectors in windows below that length. It makes no assertion about repeated vectors in different matchings or about the Hilbert constraint graph.

## A uniform edge bound for each matching

Each matching has \(O(N\log N)\) edges for the test \(z\le h-1\), uniformly in \(t\) and \(u_t\). Count oriented events. A primitive triangle whose positive even leg is \(8r_0\), positive odd leg is \(d_0\), and hypotenuse is \(z_0\) has odd dilations \(k\le h/z_0\). Other primitive triangles cannot occur because the vertical leg is odd and the horizontal leg is divisible by eight. Put \(q=v_2(r_0)\), and fix both signs. The necessary condition \(v_2(t+(\pm k d_0+1)/2)=q\) fixes the odd integer \(k\) to one class modulo \(2^{q+2}\). Indeed \(2t\pm k d_0+1\equiv2^{q+1}\pmod{2^{q+2}}\) and \(d_0\) is odd. Contributions with no possible \(s\) can be omitted.

There are at most \(h/(2^{q+2}z_0)+1\) such dilations. Each permits at most \(4\cdot2^q\) starting indices, as proved above. Thus it suffices to sum \(O(h/z_0+2^q)\) over primitive triangles with \(z_0\le h\).

Write the primitive even leg as \(2mn\), with \(0<n<m\), opposite parity, and \(m^2+n^2=z_0\). The box \(M\le m<2M\) contains \(O(M^2)\) choices. Hence the sum of \(h/z_0\) is \(O(h\log h)\). Also \(2^q\le2^{v_2(m)}+2^{v_2(n)}\), since one of the two parameters is odd. The elementary bound \(\sum_{b\le 2M}2^{v_2(b)}=O(M\log(2M))\) gives \(O(M^2\log(2M))\) in the box. Summing the dyadic boxes up to \(M\le\sqrt h\) gives \(O(h\log h)\) for this term as well.

If all \(u_t\) agree, the common-column lower bound in [the matching core budget](matching_core_budget.md) gives \(\sum_t |E(G_t)|\gg N^2\log N\), even for the true in-strip test. Combined with the per-matching upper bound, this implies that a positive proportion of the matchings have \(\gg N\log N\) edges and hence degeneracy \(\gg\log N\). The column law supplies a separation bound for repeated events, while a direct chromatic bound for these graphs remains open.

## A logarithmic lower bound for every matching

The preceding upper bound has the correct order for each \(t\), even if one chooses the column law separately for every matching. Take
\[
 F(j)=a j+2b j^2+8P(j)+c,\qquad \sigma_t(j)=[F(j)]_N,
\]
where \(a,b\) are odd, \(P\in\mathbb Z[x]\), and all coefficients may depend on \(N,t\). Write \(G_t\) for the graph of genuine in-strip P rivals in this block with columns \(8\sigma_t(j)\), before it is colored. Its vertices correspond to labels. Two labels are adjacent if one of the two cross-parity chords has the same midpoint and length as a vertical segment whose endpoints lie in the strip. For absolute constants \(C_1,C_2>0\) and all sufficiently large dyadic \(N\),
\[
 C_1N\log N\le |E(G_t)|\le C_2N\log N
\]
for every \(t\). In particular the degeneracy is at least \(C_1\log N\) for every matching.

To see this, let \(Q_s(j)=(P(j+s)-P(j))/s\), an integer polynomial for each nonzero integer \(s\). Then
\[
 F(j+s)-F(j)=s\{a+2bs+4[bj+2Q_s(j)]\}.
\]
For integers \(y,x\), the difference of the two values of \(bj+2Q_s(j)\) equals \((y-x)\) times an odd integer. This map and \(F\) therefore permute each dyadic quotient and preserve the valuations of differences. For fixed \(s,r\), with \(q=v_2(s)=v_2(r)\), first cancel \(2^q\) and the remaining odd part of \(s\) in the horizontal congruence. After the constant congruence modulo 4 is met, the bracket fixes \(j\) to one residue modulo \(N/2^{q+2}\). The preceding estimates for the upper bound and for separation of equal signed vectors now hold for the whole polynomial family. For the vectors in question \(2^{q+2}<\sqrt{h}\le N\).

For the lower bound fix a Pythagorean triangle with legs \(8r,d\) and hypotenuse \(z\), where \(r,d\) are positive odd integers, \(z\le N/4\), and
\[
 s=t+(d+1)/2\quad\hbox{is odd}.
\]
Since \(s,a\) are odd, one of the two signs for \(r\) satisfies \(\pm r\equiv s(a+2bs)\pmod4\). With that sign the equation \(F(j+s)-F(j)\equiv\pm r\pmod N\) has four solutions, all in one residue class modulo \(N/4\). The four odd indices \(i=[j+s]_N\) also form one such class. Two lie in \([N/4,3N/4)\). For either of those, \(\pi_t(j)=i-(d+1)/2\) as integers because the latter index lies in \([0,N)\). The actual vertical difference from the even point of \(j\) to the odd point of \(i\) is then \(d\). The endpoints of the rival vertical segment have rows
\[
  2i+1-(d+z)/2,\qquad 2i+1+(z-d)/2.
\]
Both lie in \([1,2N]\). Its column is the chord midpoint, which is integral since the two endpoint columns are multiples of eight.

The four values \(\sigma_t(j)\) again form one residue class modulo \(N/4\), since \(F\) preserves residues and permutes this quotient and the full group. The signed horizontal difference wraps around \([0,N)\) only if \(\sigma_t(j)\) lies in an interval of length \(r<N/4\) at one end. This discards at most one of the four roots. At least one central \(i\) therefore yields an actual in-strip chord. Each ordered pair of labels realizes just one positive shape of this orientation. Forgetting the orientation costs a factor of at most two.

It remains to count eligible triangles uniformly in \(t\). In each dyadic box \(M\le m<2M,\ M/4<n<M/2\), there are \(\gg M^2\) choices with \(m\) odd, \(n\equiv4\pmod8\) and \(\gcd(m,n)=1\). For example, apply Möbius inversion over odd divisors of \(m\) and \(n\). The main term is a positive constant times \(M^2\prod_{p>2}(1-1/p^2)\), with an \(O(M\log M)\) boundary error. Euclid's parametrization gives distinct primitive shapes with \(r_0=mn/4\) odd, \(d_0=m^2-n^2\) odd, and \(z_0=m^2+n^2<5M^2\). For an odd dilation \(k\), the parity requirement on \(t+(k d_0+1)/2\) fixes just one of the two odd residue classes of \(k\pmod4\). Provided \(5M^2\le N/64\), there are \(\gg N/z_0\) such dilations with \(kz_0\le N/4\), independently of \(t\). Each box thus contributes \(\gg N\) distinct shapes. Summing the \(\gg\log N\) disjoint boxes gives the claimed lower bound. A graph of degeneracy \(D\) on \(N\) vertices has at most \(DN\) edges, which gives the stated consequence. A bounded chromatic number is still possible.

