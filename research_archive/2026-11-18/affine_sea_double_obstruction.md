# Interior doubles in an affine one-parity sea

The tilted-triple obstruction for row step two in [the initial proof](step_two_sea_obstruction.md) applies to every invertible affine slope \(v\bmod p\) such that \(1+v^2\ne0\bmod p\). This includes each nonsquare norm slope used by the modular sea construction.

Let \(p\ge3\) be prime and \(J\) a set of \(p\) consecutive even rows, in steps of two, within rows \(1,\ldots,h\). Put the unique even row \(b(x)\in J\) congruent to \(vx+c\bmod p\) in each integer column \(x\) of the sea. Write \(n_o=\lceil h/2\rceil\). Let \(D\) be the nonzero even representative of \(v\bmod p\) with \(|D|\le p-1\), and put \(m=|D|/2\).

Suppose an odd cell \((t,a)\) is added to the sea, with residue \(b_0=b(t)\). Let \(b\) be the unique row in \(J\) satisfying
\[
 (1+D^2)b\equiv b_0+D^2a\pmod p .
\]
If some \(\eta\in\{-1,1\}\) has \(b+\eta D\in J\) and \(1\le a+\eta D\le h\), then the new configuration cannot occur on a valid board having every ordinary parity edge as a double. The assertion uses only sea columns within \(|D|(h-1)+1\) of \(t\), together with the owner of one parity edge. It tolerates arbitrary extra black cells.

Indeed set \(s=t+D(a-b)\). Then \(b(s)\equiv b_0+D^2(a-b)\equiv b\), so \((s,b)\) and \((s+\eta,b+\eta D)\) are both black. The legs from \((s,b)\) to the added point and its sea neighbor have vectors \((-D(a-b),a-b)\) and \((\eta,\eta D)\). They are nonaxial and perpendicular. Their fourth corner is \(W=(t+\eta,a+\eta D)\). If it is white, its column contains the even sea point. The owner of that even row and the odd row of \(W\) supplies an axial rectangle with the same white presentation. If \(W\) is black, the entire tilted rectangle is black, which violates the hidden-rectangle condition in the [window proof](windows.md) in dimensions at least four.

There are precisely \(2m^2\) labels \((a,b_0)\) for which this sign test is silent, out of \(n_op\) candidates. For each \(a\), the map \(b_0\mapsto b\) permutes \(J\). Every \(b\) admits at least one sign because \(2m\le p-1\). Every \(a\) except the lowest \(m\) and highest \(m\) odd rows admits both signs. The two boundary sets are disjoint because \(n_o\ge p\). For each low or high \(a\), precisely \(m\) values of \(b\) lack the one allowed sign, those closest to the opposite boundary of \(J\). This proves the count. In particular \(2m^2<n_op/2\), so the test forbids more than half the prospective labels for every such slope, even when the maximal allowed step is used. At row step two only two labels escape this test. Interchanging the row parities gives the corresponding statement on an odd sea, with the boundary count using the number of even rows and requiring it to be at least \(2m\); this holds whenever the strip contains \(p\) consecutive odd rows.

## All tilted triples with their pivot in the sea

There is a divisor test for the other possible sea legs at the same pivot. Let \(b\) be the row determined above. For a nonzero signed integer \(y\) with \(b+y\in J\) and \(a+y\) in the strip, look for a signed divisor \(n\) of \(y(a-b)\) such that \(vn\equiv y\bmod p\). If it exists, put
\[
 s=t+y(a-b)/n .
\]
The sea points \((s,b)\) and \((s+n,b+y)\) and the extra point form a tilted right angle at \((s,b)\). Its completion is \((t+n,a+y)\). To check the first sea congruence, use \(y/n\equiv v\bmod p\), valid since \(y\ne0\bmod p\) (the rows of \(J\) are distinct modulo \(p\)). The second follows by \(vn\equiv y\).

Conversely every such tilted triple has one sea leg \((n,y)\), with \(n,y\ne0\), \(vn\equiv y\), and every sea row difference \(y\ne0\) is a unit modulo \(p\). Perpendicularity forces \(s=t+y(a-b)/n\) for the pivot \((s,b)\). Modulo \(p\) this gives \((1+v^2)b\equiv b_0+v^2a\), so the pivot row is unique even when other slopes of sea chords are permitted. Thus on the infinite sea the divisor test classifies all in-strip completions whose pivot lies in the sea. For row step two the two exceptional boundary labels have no admissible \(y\) at all. Their pivot could still be the extra point itself, or they could belong to a mixed support.

## A boundary double that can be inserted

Fix the extra row \(a=1\), put \(J\) wholly above \((h+1)/2\), and assume \(1+v^2\) is a quadratic nonresidue modulo \(p\). Choose the residue of the added column so that its determined pivot row is \(b=\max J\). On this otherwise unbroken affine sea, the resulting one-double block excludes every geometric obstruction, including all tests against remote parity owners.

A tilted triple with pivot at a sea point would require both \(b+y\in J\) and \(1+y\ge1\) with \(y\ne0\), impossible. A tilted triple with pivot at the extra point and two sea endpoints completes in row \(b_1+b_2-1>h\). An oblique chord from row 1 cannot have an in-strip vertical alternative. A mixed quadruple involving the sole odd point has odd total row sum, impossible by the midpoint equation. The remaining supports are excluded by the same-role nonresidue sea proof. This realizes one boundary exception from the row-step-two obstruction when the height permits the separated row interval.

## Many single insertions on the same affine sea

Suppose \(p\) is comparable to \(h\), and that the \(p\) even levels of \(J\) all exceed \((h+1)/2\). This is possible, for example, by choosing \(h=5p\) and the highest \(p\) even rows. Given fixed \(\epsilon\in(0,1)\), put \(R=\lfloor p^{1-\epsilon}\rfloor\). For some fixed slope with \(1+v^2\) a quadratic nonresidue there are \((1-o(1))R\) distinct labels involving row 1, each of which can individually be added to this same affine sea without introducing any obstruction.

Indeed consider the top \(R\) possible pivot rows \(b\). With \(a=1\), a dangerous sea-pivot triple requires \(0<y\le 2R\). For given \(b,y\), a signed divisor \(n\) of \(y(1-b)\) determines at most one possible slope \(v=y/n\bmod p\) when \(n\) is a unit modulo \(p\). There are \(h^{o(1)}\) such divisors, uniformly since \(|y(1-b)|=O(h^2)\). Summing over \(b,y\) gives at most \(R^2 h^{o(1)}\) bad incidences of pivot rows and slopes. The finite-field character count in [the separated-row construction](separated_row_tiles.md) gives order \(p\) slopes with nonresidue norm. Hence some good slope admits at most \(R^2h^{o(1)}/p=o(R)\) inadmissible pivots in this list. The others correspond to distinct \(b_0\) by invertibility of \(1+v^2\). The boundary-double argument above excludes every other obstruction to an individual insertion. A mixed support involving two different insertions still requires its own check if the new columns are to lie close together.

## Individually safe interior labels

Take \(J\) to be the highest \(p\) even rows. Let \(A,B\) be positive integers with \(A,B<p/4\) and \(2\min J-A>h\). Use odd insertion rows \(1\le a\le A\) and the top \(B\) possible projected pivot rows \(b\) of \(J\). Discard \(b\equiv a\bmod p\); at most one \(b\) is lost per \(a\). For any remaining candidate \((a,b)\), the number of bad slopes among \(v\in\mathbb F_p^\times\) with \(1+v^2\ne0\) is
\[
 O\bigl((A+B)h^{o(1)}+\sqrt{hA}(1+\log(2A))\bigr).
\]
Here bad means that inserting the odd point above the sea residue \(b_0=(1+v^2)b-v^2a\) creates an in-strip corner triple, mixed support or vertical rival, when the unperturbed sea itself is clean.

For a sea-pivot triangle, the required signed vertical step \(y\) ranges from \(-(a-1)\) to \(\max J-b\le 2B\). By the divisor test each \(y\ne0\) forbids at most \(h^{o(1)}\) slopes. A pivot at the inserted point has fourth row at least \(2\min J-A>h\).

An oblique chord from the inserted cell to a sea row \(c'\) can have a contained vertical alternative only if
\[
 X^2=4j(c'-a+j),\qquad 1\le j\le a-1 .
\]
Here \(|X|>0\) is the horizontal extent. Write \(j=m n^2\), \(m\) squarefree. Integrality of \(X\) implies \(c'-a+j=m k^2\). There are \(O(\sqrt{A/m})\) possible \(n\)'s and \(O(\sqrt{h/m})\) possible \(k\)'s for each \(m\le A\). Thus there are \(O(\sqrt{hA}(1+\log(2A)))\) choices of \((j,c',|X|)\). For each choice the affine congruence at the sea endpoint requires
\[
 (b-a)v^2\pm |X|v + b-c'\equiv0\bmod p .
\]
Each of its two sign choices forbids at most two slopes, since \(b-a\ne0\bmod p\). Finally a mixed quadruple using the sole odd insertion has odd total row sum.

For instance take \(p\asymp h\) and \(p\le h/6\), and let \(A=B=\lfloor p^{1-\epsilon}\rfloor\) with fixed \(0<\epsilon<1\), for sufficiently large \(h\). The displayed bad-slope bound is \(o(p)\) for every candidate. Averaging over the order-\(p\) slopes with nonresidue norm and \(v^2\ne1\) leaves one slope for which \((1-o(1))\lceil A/2\rceil B\) labels can each be inserted alone in the same infinite sea. Their residue points are distinct, since \(a\) specifies a row from an interval of length less than \(p\) and the map \(b\mapsto b_0\) permutes the residues. They are off the modular line since \(b_0-a=(1+v^2)(b-a)\ne0\). Consequently the [general pair-interaction theorem](affine_sea_pair_rigidity.md) also applies to every pair of these prospective insertions. Its \(p\)-dependent width cost still prevents a quadratic assembly of all labels.

## A uniform central band for all modular permutation seas

There is a stronger exclusion on the rows that stays uniform in the affine slope. Write \(w=v/2\bmod p\). Among \(w,2w\) there is a least absolute representative \(d\ne0\) with \(|d|\le\lfloor p/3\rfloor\). Indeed the three distinct residues \(0,w,2w\) on a circle of circumference \(p\) have a consecutive gap at most \(\lfloor p/3\rfloor\), and their pairwise differences are \(\pm w,\pm2w\). Write \(d\equiv nw\) with \(n=1\) or \(2\), absorbing a sign by choosing the representative. Put \(y=2d\). Then \(y\equiv nv\bmod p\), and \(n\mid y(a-b)\) for every odd \(a\) and even \(b\), including \(n=2\).

Apply the sea-pivot test with this horizontal step \(n\) and vertical step \(y\) or with both signs reversed. Every \(b\in J\) permits at least one direction since \(|d|\le(p-1)/2\). For
\[
 1+2\lfloor p/3\rfloor\le a\le h-2\lfloor p/3\rfloor
\]
both directions keep the fourth row in the strip. The forced collision uses only sea columns within \(2\lfloor p/3\rfloor(h-1)+2\) of the insertion, together with a possible remote owner. Since \(p\le h/2\), this forbids every odd insertion in the central third of the physical rows, for every slope with \(1+v^2\ne0\).

The same conclusion holds if a period-\(p\) permutation of the \(p\) even row representatives is assumed to have a nonsquare squared norm for every nonhorizontal chord modulo \(p\). In fact this assumption forces an affine permutation. Here is the prime-field direction argument. Let \(f\) be the permutation on column residues and interpolate it by a polynomial of degree at most \(p-1\). Assume its degree \(d\) is at least 2. Set \(j=\lfloor(p-1)/d\rfloor,\ i=p-1-jd,\ k=i+j\). Then \(k\le(p-1)/2\). For \(d=2\) this is equality. For \(3\le d\le(p-1)/2\) one has \(j\ge2\) and \(i\le d-1\le(d-2)j\). For \(d>(p-1)/2\) use \(j=1\) and \(i=p-1-d\).

Since \(x^if(x)^j\) has degree precisely \(p-1\), its sum over the field is minus the nonzero \(j\)-th power of the leading coefficient of \(f\). Therefore the coefficient of \(c^i\) in
\[
 S_k(c)=\sum_{x\in\mathbb F_p}(f(x)-cx)^k
\]
is nonzero. Its degree is at most \(k-1\), since \(\sum_x x^k=0\). A missing finite chord slope \(c\) makes \(f(x)-cx\) a permutation and therefore a root of \(S_k\). There are at most \(k-1\) missing slopes, so the graph of a nonlinear permutation determines at least \((p+3)/2\) finite slopes. But a chord of slope \(s\) has nonsquare squared length only if \(1+s^2\) is a quadratic nonresidue. The character sum \(\sum_s\chi(1+s^2)=-1\) gives at most \((p+1)/2\) such slopes. This contradiction proves that \(f\) is affine, as claimed. This rigidity uses the modular norm certificate; integer chord avoidance alone is a weaker condition.
