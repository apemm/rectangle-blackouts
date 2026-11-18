# A filled quadratic-width core valid on every window of width \(h^{1-\epsilon}\)

For any \(1\le H\le h\) there is a fully filled board of width \(O(h^2)\) with one double for every ordinary parity edge except at most \(hHh^{o(1)}\) omitted edges. Every consecutive window of horizontal span at most \(H\) is free of tilted black corner triples, nonvertical mixed quadruples and vertical rivals. In fact the short nonvertical chords between opposite-parity points have nonintegral length, so the rival test allows an owner anywhere in the strip. The estimates are asymptotic in \(h\), uniformly in \(H\).

In particular at \(H=\lfloor h^{1-\epsilon}\rfloor\), \(0<\epsilon<1\) fixed, the omitted set has size \(h^{2-\epsilon+o(1)}\), within the quadratic width budget of the [positional block lemma](../../papers/extremal/drafts/upper_bound/part8_assembly.tex). This theorem certifies the windows of the main core. A collision whose black points span more than \(H\) can still invalidate the complete board.

### The star placement

For the odd row \(o=2i+1\) use columns \(16hi,\ldots,16h(i+1)-1\), filled throughout in row \(o\). For each retained even leaf \(e\) add its cell in column \(16hi+4h+4e\). All these columns are distinct. Each even point has distance at least \(2h\) from either end of its star. Any black set of span at most \(H\) meeting an even point therefore lies in a single star. Write \(g=e-o\), a signed odd integer.

Delete labels with \(|g|\le H\). Also delete labels for which any integer \(1\le X\le H\) gives \(X^2+g^2=L^2\) with \(L\) integral. The latter test gives at most \(2\sum_{X\le H}\tau(X^2)=Hh^{o(1)}\) signed gap values by factoring \((L-g)(L+g)=X^2\). A third deletion, described below, costs only \(O(H)\) signed gap values. Each signed gap corresponds to at most \(h\) labels.

The odd trace is an increasing chain on the entire board. Inside a star the even points form a line of direction \((4,1)\). Thus there are no single-role tilted triples or nonvertical mixed quadruples in a short window. For a tilted triple with one even and two odd points the right angle has to be at the even point. Its two vertical legs have absolute value \(|g|>H\), whose product exceeds the maximum horizontal product. For two even and one odd point, an odd pivot is excluded by the same product argument with the two retained gaps. At an even pivot, perpendicularity with an even-even leg \((4d,d)\) would require \(4X=\pm g\) with \(g\) odd. This accounts for every tilted triple. The integral-length deletion excludes every local vertical rival.

### The two-role mixed calculation

The sum of the four black rows in a mixed support is even by the midpoint equation. With both parities present, each therefore occurs twice. If the two odd points form one principal chord, that chord is horizontal. The other chord, between even points, has length \(\sqrt{17}\,|d|\), \(d\ne0\), and cannot have equal length.

It remains to consider two crossing chords. Orient each from odd to even. Write \(u,v\) for their signed horizontal components, respectively for the black side and black diagonal. The side is nonvertical, so \(u\ne0\). Write \(g,g+\Delta\) for their signed vertical components. Different even points in this star have different rows, so \(\Delta\ne0\). The vector between the two even endpoints is \((4\Delta,\Delta)\). The vector from the sum of the side endpoints to the sum of the diagonal endpoints is \((8\Delta+u-v,\Delta)\). Perpendicularity to the side and equality of norms give
\[
 u(8\Delta+u-v)=-g\Delta,\qquad
 u^2-v^2=\Delta(2g+\Delta).
\]
Put \((v-u)/\Delta=a/b\) in lowest terms with \(b>0\). The first equation gives \(u(a-8b)=bg\), so \(u=bk\) and \(g=k(a-8b)\), where \(k\ne0\). Substitution in the second gives
\[
 \Delta(a^2+b^2)=4kb^2(4b-a).
\]
Since \((a,b)=1\), \(a^2+b^2\) is coprime to \(b\). Its common divisor with \(4b-a\) divides 17, by substituting \(a=4b\bmod(4b-a)\). The common divisor with \(4b^2(4b-a)\) is therefore at most 68, including the case \(a=4b\), which yields no admissible \(\Delta\). Thus the nonzero \(k\)'s with \(|u|\le H\) number at most
\[
 \frac{136H}{b(a^2+b^2)}.
\]
For each \(b\ge1\), the sum of \(1/(a^2+b^2)\) over integral \(a\) is \(O(1/b)\), by comparison with its integral. Summing over \(b\) gives \(O(H)\) parameter triples and therefore \(O(H)\) signed gaps \(g\) over *all heights*. Delete these side gaps. This rules out every crossed mixed support with \(|u|\le H\) inside a single star. There is no restriction on the diagonal's horizontal component in this calculation.

The [blackout reduction lemma](../../papers/extremal/sections/sec5_threshold.tex) now applies on each stated window, since the doubles have distinct opposite-parity row pairs. More precisely, the proof excludes each of its three local geometric obstructions even if the rest of the final row-pair graph is supplied as remote owners. It does not exclude long configurations made from several stars, or long configurations inside one star. The distinction matters because the paper's unconditional locality bound is quadratic in \(h\).

