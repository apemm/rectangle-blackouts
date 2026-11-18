# A quadratic-width board carrying every label and valid in nearly linear windows

Let \(\eta>0\) be fixed. At every sufficiently large height \(h\), one can fill \(O_\eta(h^2)\) columns with one singleton or double per column, use each of the \(q_h=\lfloor h^2/4\rfloor\) parity labels once as a double, and have **every subwindow of horizontal span at most**
\[
 H=\left\lfloor\frac{h}{(\log h)^{3+\eta}}\right\rfloor
\]
**distinguish all rectangles contained in it.** The local collision tests also take account of remote axis owners in the full parity graph. Constants here use the repository's [Theorem E](../../papers/extremal/drafts/upper_bound/part3_t1chain.tex) and [positional window lemma](../../papers/extremal/drafts/upper_bound/part2_validity.tex).

This gives the target size \(m+q_h\) and the target width order on one candidate board, with validity certified only at the indicated scale. The paper's general locality span for full-board validity is \(2W_h\), of order \(h^2\). In particular, certificate windows of span \(H\) cannot by themselves prove \(m_h=O(h^2)\).

### Counting the exceptional diagonals

Use [the constant-star window theorem](all_obstructions_short_windows.md). Its deleted set comprises entire signed-gap diagonals. Small absolute gaps and the binary cubic mixed-support condition remove \(O(H)\) such diagonals. To count the short integral chords, write the even leg of a triple as \(X=2kmn\), its odd leg as \(Y=k(m^2-n^2)\), and its hypotenuse as \(k(m^2+n^2)\), with \(m>n\ge1\). Dropping the coprimality and parity restrictions bounds the count from above. Since \(X\le H,\ |Y|\le h\), the hypotenuse is at most \(2h\). The number of admissible scales is at most \(\min(H/(mn),2h/m^2)\). For fixed \(m\le\sqrt{2h}\), sum first over \(n\le Hm/(2h)\) and then over the remaining \(n<m\). The first sum is at most \(H/m\). The second is \(O((H/m)(1+\log(2h/H)))\), including when the first range is empty. Summing in \(m\), and allowing both signs for \(Y\), gives
\[
 \Delta=O\bigl(H\log(2h)(1+\log(2h/H))\bigr)
\]
exceptional diagonals in total. Retain every label outside them in the constant-star main core.

### Shortening the periodic separations in Theorem E

The proof of Theorem E applies to *any prescribed set of diagonals*. It puts their ordinary labels into finitely many types, with \(O(\log\log h)\) classes per type. Its slot-count calculation, before the inter-core separations are charged, gives total physical core length
\[
 O\bigl(\Delta h(\log h)^2(\log\log h)^{C_1}+h^{1+o(1)}\bigr)
\]
for an absolute \(C_1\). There are 49 types, with a bounded number of collar stages for each. The collars and inter-type separations cost \(O(h^2)\) in total. The remaining \(O(h^2\log\log h)\) term in the full-width theorem pays for a separation of \(2W_h+1+O(1)\) period-seven sea columns between consecutive classes of a type. These facts follow from (BL1)–(BL4), the width count for the layout, and the dyadic-class and coarse-group estimates in [the proof of Theorem E](../../papers/extremal/drafts/upper_bound/part3_t1chain.tex).

Use the unique multiple of seven in \([2H+2,2H+8]\) as the length of every inter-core separation, and put the first core of each type at a multiple of seven. Each core length is \(7N_c\), so every core starts at the required phase. Fill intervening columns with the original period-seven rule. This phase choice is explicit because the literal layout (BL3) in the draft prescribes a gap \(D=2W_h+1\) and starts divisible by seven, which can conflict when \(7\nmid D\). Rounding that gap upward to a multiple of seven in the full layout costs at most six columns and preserves its locality proof. Equivalently, place the local cores directly from their infinite, clean class configurations. A subword of at most \(H+1\) columns meeting a core sees only that core and its own periodic extension. One meeting no core is contained in the pure periodic stages or in the already validated collar and background. The ends can be aligned at bounded cost inside the constant row-\(h\) separations. No double is lost. The virtual owner tests use the same full parity graph. Parked tilted triples allowed by Theorem E remain subject to the same white-completion and virtual-owner checks. This argument asserts local validity for the retained spans and does not assert global cleanliness of the compressed component.

The shortened part has length
\[
 O\bigl(\Delta h(\log h)^2(\log\log h)^{C_1}
          +h^{1+o(1)}+h^2+H\log\log h\bigr)=O_\eta(h^2).
\]
Indeed \(1+\log(2h/H)=O_\eta(\log\log h)\), and the factor \((\log h)^\eta\) absorbs any fixed power of \(\log\log h\).

Theorem E excludes a set of nonordinary labels from its input. The profile proposition bounds the total number of such labels on the entire grid by \(O(h^{3/2})\). Place just the nonordinary labels on the exceptional diagonals in the positional block WP. The bound in the [WP lemma](../../papers/extremal/drafts/upper_bound/part2_validity.tex) is \(O(h^2+(h^{3/2}+4)\tau_{\max}(h)^2)=O(h^2)\), since \(\tau_{\max}(h)=h^{o(1)}\).

### Joining the three pieces

Reflect the main core horizontally so its last star uses row 1. Append a constant row-1 stretch. Its length may be taken to be \(2W_h+2\). Continue with WP, whose left exterior is row 1. For odd heights its right exterior is row \(h\). For even heights it can end in row 1; place a row-1 stretch, a switch to row \(h\), and a row-\(h\) stretch before the last component. Use the same switch if WP is empty. Take length \(2W_h+2\) on each side of a switch. End with the shortened Theorem E board, whose exterior is row \(h\). Empty components may be omitted.

The constant boundary step is a monotone chain, and neither boundary row participates in a vertical rival. In the main core the last even points are farther than \(H\) from the end. Thus any short window at a join either sees just the step, extends the existing exterior of a clean component, or meets only the row-1 end of the main core. Its geometric and virtual-owner tests hold. The added length is \(O(h^2)\). The three label lists partition all parity pairs, and every column is occupied.

The loss of long constraints is real for the main-core rule. For any fixed \(c>0\) take an even integer \(s\) so large that \(2s/(s^2-1)<c\). For every central odd row \(o\in[h/4,h/2]\) and odd \(k\) with \(h/8\le k(s^2-1)\le h/4\), the star label of row \(e=o+k(s^2-1)\) has a genuine integral diagonal to its constant row \(o\) at distance \(2sk<ch\). The alternative vertical endpoints are \(o-k,e+k\), both in the strip. The opposite-parity owner, wherever placed, gives a collision, or a hidden tilted rectangle if it is at the midpoint. There are \(\Omega_c(h^2)\) such labels. Thus this constant-row core cannot reach a fixed linear test radius with only a subquadratic exceptional set. A different filler or a different bulk placement is needed at longer scales.

