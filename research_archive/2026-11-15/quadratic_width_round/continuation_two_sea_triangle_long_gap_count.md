# Long gaps in the two-sea triangle collision family

15 November 2026. For raw refined Hilbert coordinates with a uniformly
sampled row offset, the type-1/type-1 collisions in
[the low-profile classification](continuation_four_profile_residual_classification.md)
have expected count
\[
 O\left(\frac{h^2\tau_*(Ch)\log(2h)}{\sqrt Q}\right)
 \tag{1}
\]
when their inserted-point rank gap is at least \(Q\). Here the stride,
refinement factor, and low sea rows are fixed, and
\(\tau_*(X)=\max_{n\le X}\tau(n)\).
Thus gaps at least \(h^\varepsilon\) contribute
\(h^{2-\varepsilon/2+o(1)}\) witnesses in expectation.

The short-gap family is not covered by this saving. Repeated even-row
plateaus can create genuine collisions at a fixed gap. Constant cap
coordinates are also outside the raw-coordinate counting hypothesis.

## 1. An averaged divisor-difference bound

For positive integers \(B,d\), let \(W_B(d)\) count triples
\((C,u,v)\) with
\[
 1\le C\le B,\qquad u,v\in\mathbb Z\setminus\{0\},
 \qquad v-u=d,qquad u\mid C,\quad v\mid C.
\]
Then
\[
 W_B(d)\le\frac{4B\tau(d)H_d}{d},
 \qquad H_d=\sum_{j=1}^d\frac1j.
 \tag{2}
\]

Write \(g=\gcd(|u|,d)\), \(d=gk\), and \(u=ga\).
Then \(\gcd(a,k)=1\), and
\[
 \operatorname{lcm}(|u|,|u+d|)=g|a(a+k)|.
\]
The number of eligible \(C\)'s is at most
\(B/(g|a(a+k)|)\). Dropping the gcd condition only enlarges the sum.
The positive, negative, and straddling ranges give
\[
 \sum_{a\in\mathbb Z\setminus\{0,-k\}}
 \frac1{|a(a+k)|}
 =\frac{2H_k+2H_{k-1}}{k}\le\frac{4H_k}{k}.
\]
Summing over \(g\mid d\) proves (2). This bounds the number of
witnesses, not only the number of integers \(C\) supporting a witness.

## 2. A common raw row offset costs one factor of h

Fix a low sea profile \((L,F)\), and put \(k=F-L>0\). A type-1
triangle using an even inserted point at row \(b\) has divisor parameters
\[
 uv=k(b-F)=C,
 \qquad u\equiv1\pmod4,\qquad v\equiv2\pmod4.
 \tag{3}
\]
Its completion is \(u\) columns to the right of the inserted point,
at row \(b+L-F\). Therefore two such triangles sharing a completion
use inserted points at the same row \(b\), and their two \(u\)-values
differ by their inserted-column gap.

Let the total raw even function be
\[
 b(t)=\rho+4\left(f(\lfloor t/M\rfloor)-U\right),
 \tag{4}
\]
where \(f\) is one coordinate of an \(N\times N\) Hilbert traversal,
\(N=\Theta(h)\), \(M\) is fixed, and \(U\) is uniform on an interval
of at least \(c h\) integers. Fine rank \(t\) occupies column \(4t\).
Discard all candidates whose physical rows are outside the strip or
outside the chosen bulk profile.

For fixed ranks \(t,t+q\), a collision requires
\(f(\lfloor t/M\rfloor)=f(\lfloor(t+q)/M\rfloor)\).
As \(U\) varies, every admissible \(C=k(b-F)\) occurs at most once,
and \(1\le C\le C_0h\). Equation (2), with \(d=4q\), shows that
the expected number of shared-completion witnesses for this pair is at most
\[
 C_1\frac{\tau(q)\log(2h)}q.
 \tag{5}
\]
The exact divisor residues in (3), in-strip completions, distinctness,
and actual sea occupancy only remove witnesses. There is one common
offset here, so this argument does not claim an \(h^{-2}\) factor.

## 3. Pack equal-coordinate visits in short rank intervals

Hilbert injectivity and its coordinate Hölder bound imply that, for every
fine rank \(t\) and every \(D\ge1\),
\[
 \#\{u:|u-t|\le2D,\ b(u)=b(t)\}\le C_M\sqrt D.
 \tag{6}
\]
The equality in (6) is independent of \(U\). To prove it, project to
coarse ranks. All the corresponding Hilbert points lie within a rank
interval of length \(O_M(D+1)\). Their first coordinate is fixed, while
the other coordinate lies in an interval of length \(O_M(\sqrt D)\)
by locality. Injectivity gives that many coarse points, and each has
at most \(M\) fine copies.

There are \(O(h^2)\) fine ranks. Hence the number of equal-coordinate
pairs with \(D\le q<2D\) is at most \(C_M h^2\sqrt D\).
Multiplying by (5) bounds their expected witness count by
\[
 C\frac{h^2\tau_*(Ch)\log(2h)}{\sqrt D}.
 \tag{7}
\]
All actual type-1/type-1 gaps satisfy \(4q\le2C\le C'h\), since
each nonzero signed divisor of \(C\) has magnitude at most \(C\).
The dyadic sum of (7) from \(Q\) to \(C'h\) is dominated by its
first scale, proving (1).

## 4. Exact scope and the remaining local problem

The estimate concerns two raw-coordinate endpoints, including their
fixed number of fine copies. It remains an upper bound if later tests
retain only a subset of those raw candidates. It does not apply to a
pair containing a cap-constant even value: such a plateau need not have
the row-visit packing property (6).

Selecting offsets jointly with other nonnegative objectives is possible
by the same weighted averaging and Markov argument used in the cap
incidence proofs. Conditioning on a previously selected exceptional
configuration is not part of the estimate.

The short-gap problem is real. For example, in the profile \((L,F)=(3,8)\),
every eligible \(b\equiv2\pmod4\), \(b>16\), satisfies
\(C=5(b-8)\equiv10\pmod{20}\). The two divisor choices \(u=1,5\)
produce a collision between two even points at that row in adjacent
spacing-four columns, provided the associated sea columns lie inside
the core interval. A sufficiently long interior plateau therefore fails.

Thus a subquadratic long-gap count does not justify the refined core by
itself. A local rule must still control the bounded-gap repeated-row
constraints, and cap-constant endpoints need a separate treatment.
No new row filter, relocation theorem, or complete board is claimed.

Independent review: pending the written counting audit.
