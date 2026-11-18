# Modular blocks for a fixed row gap

I place all opposite-parity row pairs in width \(O(h^2)\), fill every column, and exclude every vertical rival pair in the height-\(h\) strip. All double columns can be multiples of 4. For a signed prime gap \(T=\pm p\) with \(p>C\sqrt h\), I can put its labels in one fully filled block of width \(O(h)\) and exclude all rectangle obstructions inside that block. The construction across different gaps still needs a proof for tilted triples and mixed supports.

## The congruence for one gap

Rows are numbered from 1 to \(h\). The signed gap \(T\) is the even row minus the odd row of a label. Put \(q=|T|\). For each odd prime \(p\mid q\), choose a unit \(\lambda\bmod p\) with \(1+\lambda^2\) a quadratic nonresidue. There are \((p-\left(\frac{-1}{p}\right))/2\) such choices. This follows by counting the \(p-1\) solutions of \((z-t)(z+t)=1\) and the \(1+\left(\frac{-1}{p}\right)\) roots of \(1+t^2=0\). Lift the choices to \(\lambda\bmod q\) by the Chinese remainder theorem. When \(q=1\) the congruence is empty.

In one block every black point satisfies \(x\equiv\lambda y\bmod q\). For a displacement \((X,Y)\) with integral norm \(L\), I claim that \(q\) divides \(X,Y,L\). If \(p^e\Vert q\) and \(v_p(Y)=j<e\), then \(p^j\mid X\). After dividing the squared norm by \(p^{2j}\), its residue modulo \(p\) is
\[
 (1+\lambda^2)(Y/p^j)^2 .
\]
This is a nonresidue. Hence \(q\mid Y\), and the congruence gives \(q\mid X\). The norm equation now gives \(q\mid L\).

Write \(w\in\{1,\ldots,q\}\) for a row residue and \(y=w+qz\). The allowed normalized rows are \(0\le z\le H_w=\lfloor(h-w)/q\rfloor\). Put \(H=\lfloor h/q\rfloor\), so \(H-1\le H_w\le H\). In this fiber the labels with signed gap \(T\) are disjoint adjacent pairs. Their lower row has one fixed parity in \(z\), since \(q\) is odd. Reversing the sign of \(T\) selects the other matching.

A strip rival of opposite-parity endpoints in this fiber descends to a strip rival on the normalized rows. The two rows of the vertical diagonal are the midpoint row plus or minus \(L/2\). In normalized coordinates they are \((z_1+z_2\pm L/q)/2\). These are integers because \(z_1,z_2\) have different parities and \(L/q\) is odd. The strip bounds put both rows in \([0,H_w]\). Each lies strictly beyond one endpoint row for a nonvertical displacement. Thus neither endpoint of a rival can be in normalized row 0 or \(H_w\). [Strip rival lemma](../../papers/extremal/sections/sec5_threshold.tex)

## A filled chain for the adjacent pairs

Use this bi-infinite sequence of normalized columns.

| Column \(n\) | Rows |
| --- | --- |
| \(3k\) | \(4k+1,\ 4k+2\) |
| \(3k+1\) | \(4k+2\) |
| \(3k+2\) | \(4k+3,\ 4k+4\) |

Translate the rows by \(\delta_w\in\{0,1\}\) to select the desired matching. Every point is comparable to every other point in the coordinatewise order. The chain lemma therefore excludes every tilted corner triple and mixed quadruple. [Chain lemma](../../papers/extremal/sections/sec5_threshold.tex)

For a point \((n,z)\) in this sequence before truncation the quantity \(4n-3(z-\delta_w)\) lies between \(-6\) and \(-1\). A displacement \((X,Y)\) between different columns, oriented to the right, has \(Y\ge0\) and \(|4X-3Y|\le5\). If \(Y\) is odd and \(X^2+Y^2=L^2\), reduction modulo 8 gives \(4\mid X\). Hence \(L\ge5\). Also \(4X-3Y\ne0\), since equality would give \(4\mid Y\). It follows that
\[
 0<(5L-3X-4Y)(5L+3X+4Y)=(4X-3Y)^2\le25 .
\]
The first factor is a positive integer and the second exceeds 25. This excludes integral distances of opposite-parity endpoints in distinct columns of the chain.

Clamp the rows to \([0,H_w]\), merging coincident points. The sequence is still a chain. A newly clamped point lies in an extremal row of its fiber, so it cannot participate in a normalized strip rival. The doubles left by this operation are the desired adjacent pairs.

## Quadratic width for the strip rival condition

Choose \(a_w\in[0,4q)\) with \(a_w\equiv\lambda w\bmod q\) and \(a_w\equiv0\bmod4\). For each \(c\in\{0,1,2,3\}\) make one copy of the block. Map normalized column \(n\) of fiber \(w\) to
\[
 x=a_w+q(n-c).
\]
In copy \(c\), retain both rows of a double only when \(n\equiv c\bmod4\). Keep its lower row otherwise. Each physical column determines a unique \(w\) and \(n\), because the \(a_w\) are a permutation modulo \(q\). Every column therefore has at least one point, and every retained double is in \(4\mathbb Z\).

Keep the integer columns in
\[
 [-6q,\ (\lceil 3H/4\rceil+5)q].
\]
All target doubles occur in this interval. For either row of an original target double, \(4n=3(z-\delta_w)+e\) with \(-6\le e\le-1\) and \(0\le z\le H_w\). This bounds the target \(n\) between \(-3\) and \(3H/4\). The interval has width \(O(h)\).

The congruence forces a rival into one fiber, where the clamped chain excludes it. Use a multiple-of-4 translation for each copy and leave at least \(h\) singleton columns in row 1 between successive copies. A rival has horizontal separation less than \(h\), and no rival meets row 1. The same row supplies an infinite tail if needed. There are \(O(h)\) signed gaps and at most 4 copies per gap. This gives the claimed \(O(h^2)\) board for the strip rival condition. The separator argument uses the strip bound on the hypotenuse.

## One clean block for \(p>C\sqrt h\)

Fix a signed gap \(T=\pm p\). Use one copy of the clamped \((3,4)\) chain with \(c=0\) and retain all target doubles. Choose \(a_w\in[0,p)\) representing \(\lambda w\bmod p\). This statement places no congruence modulo 4 on the double columns. Use the same interval as above with \(q=p\).

There is an absolute constant \(K\) such that every normalized displacement \((r,s)\) within one fiber satisfies
\[
 |4r-3s|\le K,\qquad |r|+|s|\le K(H+1).
\]
For the endpoint check, the chosen physical interval and \(0\le a_w<p\) imply \(-7\le n\le\lceil 3H/4\rceil+5\). Before clamping, every row is then within 12 of \([0,H_w]\), by \(4n=3(z-\delta_w)+e\) and \(H_w\ge H-1\). Clamping changes \(4n-3z\) by at most 36. Thus \(K=200\) suffices for both bounds. These estimates are independent of \(\lambda\).

Choose \(\lambda\) to avoid \(\lambda r+s=0\bmod p\) for every primitive nonzero \((r,s)\) in the twice-widened ranges above. There are \(O(H+1)\) candidate vectors since each \(r\) allows only \(O(1)\) values of \(s\). A primitive vector excludes at most one slope. For \(p>C\sqrt h\) with \(C\) absolute and large enough, the number excluded is smaller than the number of nonsquare-norm slopes.

Write \(\mathcal L\) for the homogeneous congruence lattice \(X\equiv\lambda Y\bmod p\). The nonzero residues of two vectors in \(\mathcal L\) have nonzero dot product modulo \(p\), since \(1+\lambda^2\ne0\bmod p\). Hence if two such vectors are perpendicular, at least one lies in \(p\mathbb Z^2\). Call a vector whose residue is nonzero a crossing vector.

In a tilted black corner triple, take the two legs meeting at its right angle. If both belong to \(p\mathbb Z^2\), the triple lies in one fiber and the chain lemma applies. Otherwise the divisible leg joins two points of one fiber. Divide it by \(p\) and by the gcd of its coordinates. The resulting primitive direction obeys the displayed bounds. A crossing leg perpendicular to it would force \(\lambda r+s=0\bmod p\).

For a mixed support, write \(u=B-A\), \(v=D-C\) for the black side and black diagonal, respectively. The common side is translated by
\[
 n=(C+D-A-B)/2,\qquad u\cdot n=0,\qquad |u|=|v|,\qquad v\ne\pm u .
\]
Here \(n\ne0\) is integral and belongs to \(\mathcal L\), since \(p\) is odd. If \(u\in p\mathbb Z^2\) and \(n\) crosses, use the primitive direction of \(u/p\) as above. If \(u\) crosses, \(n\) is divisible by \(p\). Reducing the norm equation on the modular line gives \(v\equiv\pm u\bmod p\). Exchange \(C,D\) if needed. The midpoint equation now puts \(C,A\) in the same fiber and \(D,B\) in the same fiber. Hence \(2n/p\) is a sum of two normalized black displacements. Its primitive direction obeys the twice-widened bounds, and its perpendicular crossing vector \(u\) gives the excluded slope. Finally, if \(u,n\) are divisible by \(p\), the norm equation puts \(v\) in \(p\mathbb Z^2\) and the midpoint puts all four points in one fiber. The mixed equations descend there, where the chain lemma applies for a nonvertical side. Vertical-side collisions are already covered by the strip rival argument. [Mixed-support equations](../../papers/extremal/sections/sec2_prelim.tex)

Thus the filled finite block excludes tilted triples, mixed quadruples and strip rivals among its own points. Distinct double row pairs are parity edges, so the blackout criterion applies. The other sign of the prime gap has its own block. [Blackout criterion](../../papers/extremal/sections/sec5_threshold.tex)

## A bounded number of clean blocks for any sufficiently large prime gap

I can also cover each signed prime gap \(T=\pm p\) by an absolute number of independently clean, fully filled finite blocks of total width \(O(h)\). This holds for all sufficiently large \(p\), uniformly in \(h\). Take \((a,b,c)=(31,480,481)\), so \(a^2+b^2=c^2\), and write \(E(x,y)=bx-ay\).

In each normalized fiber take all the points with \(0\le bx'-a(z-t_w)\le a\). Every column has one point or two adjacent points, and the points form a chain since \(b>a\). A double at \(x'=ak\) has rows \(bk+t_w-1,bk+t_w\). Across \(b/2\) phase choices, let \(t_w\) run through the representatives in \([0,b)\) of the parity needed for the upper row. The phases cover the prescribed matching.

Lift \(z\) to \(y=w+pz\) and \(x'\) to \(x=A_w+px'\), with \(A_w\equiv\lambda w\bmod p\). Choose the representative \(A_w\) so that \(0\le bA_w-aw-pa t_w<bp\). Consecutive representatives change this quantity by \(bp\), so the choice always exists. Now every lifted point in every fiber satisfies \(0\le E(x,y)\le Bp\), where \(B=a+b\). Within a single fiber every normalized black displacement has \(|E|\le a\).

I choose \(\lambda\) once for the prime. For a primitive vector \((r,s)\), put
\[
 e=br-as,\qquad z_0=ar+bs .
\]
Since \(bz_0-ae=c^2s\) and \(\gcd(b,c)=1\), fixing \(e\) fixes \(z_0\bmod c^2\). For each positive \(e\le 2a\) there are at most \(2Bp/c^2+1\) possible \(z_0\) with \(|z_0|\le Bp\). Each pair determines at most one primitive vector and excludes at most one slope by \(\lambda r+s=0\bmod p\). Signs cover the negative values of \(e\). When \(e=0\) the primitive direction is \(\pm(a,b)\), which excludes at most one further slope. The total exclusion is at most
\[
 (4aB/c^2)p+2a+1,\qquad 4aB/c^2<0.275.
\]
For all sufficiently large \(p\), a nonsquare-norm slope survives.

The preceding prime-block proof now applies with a different bound on the primitive direction. For a tilted triple the divisible leg supplies a primitive \((r,s)\) with \(|e|\le a\). In a mixed support the divisible vector \(u\) or \(2n\) supplies one with \(|e|\le 2a\), using the matched fibers when \(u\) crosses. The perpendicular crossing vector is an integer multiple of \((-s,r)\). Its \(E\) has magnitude at least \(|ar+bs|\). On the other hand its \(E\) has magnitude at most \(Bp\). This holds for a black displacement and also for \(n\), since \(E(n)\) is half a difference of two sums of black \(E\)-coordinates. These are the directions excluded in choosing \(\lambda\). When all points lie in one fiber the chain lemma again excludes the tilted and mixed obstructions.

The normalized chain excludes every integral norm between opposite-parity points in different columns. For a displacement with \(X>0\), \(Y\ge0\) and \(Y\) odd, \(bX-aY\ne0\) since \(\gcd(a,b)=1\) and \(b\) is even. Any integral norm here has \(L\ge5\). The identity
\[
 (cL-aX-bY)(cL+aX+bY)=(bX-aY)^2\le a^2<5c
\]
would have a positive integer first factor and a second factor at least \(5c\).

For each phase keep the physical interval
\[
 \lceil(a+Bp)/b\rceil\le x\le\lfloor ah/b\rfloor .
\]
All its chain points lie in the strip because \(0\le bx-ay\le Bp\). Every column of this interval is filled. A target label lost at the left lies within \((Bp+b)/a+1\) rows of the bottom, and a label lost at the right lies within the same distance of the top. The same bounds cover the labels when the interval is empty. Thus each fiber has only \(O(1)\) omitted labels across all phases.

Place these remaining labels in separate blocks of \(p\) consecutive columns. Each such block has one column for each residue \(w\). Put at most one omitted double in that column and otherwise choose any singleton in the fiber. In a black tilted triple some leg is divisible by \(p\), yet its nonzero horizontal component has magnitude less than \(p\). In a mixed support, \(|u_x|\) and \(|n_x|\) are also less than \(p\). A divisible \(u\) would be vertical. A divisible \(n\) would be vertical and force a horizontal \(u\). Two black points on the same row would then occupy columns congruent modulo \(p\), which is impossible in this interval. Rivals would have to be in the same fiber, which has only one column. Hence each of the \(O(1)\) end blocks is clean. Its width is \(p\le h\).

## A prime modulus near the height

For a prime \(p<h<2p\) there is a simpler strip-wide result. Let \(a_0\) be the least absolute representative of \(\lambda^{-1}\bmod p\). The least vertical span of a tilted lattice rectangle in \(\mathcal L\) is \(p+|a_0|\). To see this, two perpendicular legs cannot both cross. Two divisible tilted legs need vertical span at least \(2p\). If one divisible leg has vertical component of magnitude at least \(2p\), the same bound holds. Otherwise reverse the leg if needed to write it as \(p(k,1)\). A perpendicular crossing leg \((c,d)\) then has \(d=-kc\) and \(d\equiv a_0c\bmod p\). Since \(p\nmid c\), this gives \(|d|\ge |a_0|\). Conversely the lattice vectors \((-pa_0,p)\) and \((1,a_0)\) realize the stated span.

Thus if \(h\le p+|a_0|\), a tilted corner triple from this affine lattice cannot fit in the strip. For a mixed support with tilted \(u\), the rectangle with legs \(u,n\) would violate the same bound since \(n\in\mathcal L\). Every nonaxial lattice displacement of integer norm must have \(p\mid Y\). As \(h<2p\), its norm would be \(p\sqrt{k^2+1}\) with \(k\ne0\), which is impossible. This also excludes rivals. If \(u\) is horizontal and \(v\) is vertical with the same length, then \(|u_x|=|v_y|=p\). The midpoint identity requires \(u\equiv v\bmod2\), whereas \(p\) is odd. Thus arbitrary singleton choices on the affine line work at every width in this range. Each gap-\(p\) row pair can be placed at its residue column within \(p\) consecutive columns since the lower rows \(1,\ldots,h-p\) are distinct modulo \(p\).

For \(p>4h/5+2\), some nonsquare-norm slope has \(|a_0|\ge h-p\). Inversion permutes the nonzero residues and preserves the nonsquare-norm condition. Fewer than \(2(h-p)\) inverse residues violate this size bound, and at least \((p-1)/2\) meet the norm condition. For \(p\equiv2,3\bmod5\) one can take \(\lambda=2\), giving \(|a_0|=(p-1)/2\).

## Why the blocks still need a gluing argument

Two individually clean modular blocks can form a fully black tilted rectangle even when their separation is quadratic. Take \(d\ge4\) with \(d\equiv4\bmod21\) and \(h=2d+1\). The first two singleton columns have points \((0,d+1),(1,2d+1)\). They lie on an affine line of slope parameter \(\lambda=1\bmod3\). The second two singleton columns have \((d^2,1),(d^2+1,d+1)\), with \(\lambda=2\bmod7\). Both parameters have nonsquare \(1+\lambda^2\). The four points form a rectangle with perpendicular legs \((1,d)\) and \((d^2,-d)\). Thus a gluing argument for a quadratic-width blackout must use more information about the placements than the individual cleanliness and an \(O(h)\) lower bound on their separation.

## An obstruction to a simultaneous 2-adic order

Suppose a whole signed-gap block uses columns \(x_i=4m_i\) for the odd rows \(2i+1\), obeys \(x_i\equiv\lambda(2i+1)+t\bmod q\), and satisfies \(v_2(m_i-m_j)\ge v_2(i-j)\) for every pair of distinct indices. If \(n_T\) is the number of labels in this diagonal, take two indices at distance \(2^j\) with \(n_T/2\le 2^j<n_T\). They exist since the indices are consecutive. Dividing the column congruence by \(2^j\) gives
\[
 (m_{i+2^j}-m_i)/2^j\equiv\lambda/2\bmod q .
\]
The block span is at least \(4\cdot 2^j\) times the least absolute representative of \(\lambda/2\bmod q\).

For any fixed \(R\), choose a multiple \(M\) of 4 and of all the integers \(1+4r^2\) with \(|r|\le R\). Each prime \(p\equiv1\bmod M\) makes all these integers quadratic residues by reciprocity. The prime number theorem in arithmetic progressions and partial summation give a divergent reciprocal sum over these primes. Sieving by finite subsets of them shows that almost every odd \(q\) has such a prime factor. For these \(q\), a slope with the required nonresidue property at every prime divisor has least absolute representative of \(\lambda/2\) greater than \(R\). On \(h/4\le T\le h/2\) we have \(n_T\gg h\). The sum of the block spans, divided by \(h^2\), therefore tends to infinity if the blocks use these two conditions and are arranged disjointly. This rules out this particular 2-adic ordering for a quadratic-width construction.
