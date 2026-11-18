# Combining a modular shear with binary row alignment

The modular-shear placement on a signed diagonal \(T\) uses physical columns \(8f(i)+x_0\) for the two rows \(2i+1,\ 2i+1+T\). Its vertical-rival argument asks for
\[
 f(i)\equiv r\,i+c\pmod{|T|},\qquad
 64r^2+4\ \hbox{a quadratic nonresidue modulo every prime dividing }T .
\]
A separate way to control tilted triples or mixed supports is a common power-of-two alignment of same-role chords. The two requirements cannot both hold on all but \(o(h^2)\) labels with bounded band counts and spans.

More precisely, fix integers \(C,D\ge1\) and \(b\ge0\). Allow at most \(C\) bands per signed diagonal. Within a band suppose the \(f(i)\) span at most \(Dh\), satisfy the displayed congruence for a band-specific \(r,c\), and obey
\[
 2^{\max(0,v_2(i-j)-b)}\ \mid\ f(i)-f(j)
 \quad\text{for distinct retained indices in that band}.
\]
Then for all sufficiently large \(h\), these bands must omit \(\gg_{C,D,b} h^2\) labels. This includes the condition \(v_2(X)>v_2(Y)\) on the same-role chords of the stride-eight placement, for which one may take \(b=1\). The obstruction concerns this combination of sufficient conditions. It does not rule out an angle-free modular shear obtained by other means.

Take positive odd diagonals \(h/4\le T\le h/2\). Each has a consecutive interval of \(n\ge h/5\) legal indices for large \(h\). Choose the largest power \(2^k\le n/(C+1)\). For each of \(2^k\) different starting residues at the left of the interval, take \(C+1\) indices with step \(2^k\). These progressions are disjoint. If all of a progression are retained, two share a band. Their index difference is \(d2^k\), \(1\le d\le C\). Once \(k\ge b\), the binary hypothesis gives \(f(i)-f(j)=a2^{k-b}\) with \(|a|\le Dh2^b/2^k\le 10D2^b(C+1)\). The congruence forces
\[
 r\,(2^b d)\equiv a\pmod p
\]
at any odd prime \(p\mid T\).

Choose one odd prime \(p\) larger than all the finitely many positive integers \(64a^2+4(2^bd)^2\) in this range, with each of them a quadratic residue modulo \(p\). Such primes exist: take primes congruent to one modulo eight times the product of their odd prime divisors and use quadratic reciprocity. Also require \(p>2^b C\). The prime number theorem for a fixed progression suffices. At this prime, the last congruence makes \(64r^2+4\) a nonzero square, by multiplying it by \((2^bd)^2\). This contradicts the required nonsquare test for every band, even though different bands may choose different shears.

Each of the \(\gg_p h\) odd multiples of \(p\) in the central range must therefore omit at least one label in each of its \(2^k\gg_C h\) disjoint progressions. Summing proves the claim.
