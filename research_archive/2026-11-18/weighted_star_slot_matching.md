# Matching labels with different blocked-distance lists

Consider \(n\) labels. Label \(e\) has a finite set \(D_e\) of positive integers. The goal is to choose distinct integer slots \(t_e\) so that \( |t_e-t_f|\notin D_e\cup D_f\) for all \(e\ne f\). Put \(d=\max |D_e|\), and let \(\Delta\) be the maximum number of lists containing any one distance.

**Lemma.** For a sequence of instances with \(d,\Delta=n^{o(1)}\), all labels fit in an interval of length
\[
 O\!\left(n\max\{1,d/\log n\}\right).
\]
The sets \(D_e\) need not be distinct. Their numerical entries can exceed the length of the interval.

Choose \(p=\min\{1/4,\log(n)/(64\max(1,d))\}\) and \(N=\lceil8n/p\rceil\). Select each integer in the candidate interval \([1,N]\), and each integer at a listed distance to either side of it, independently with probability \(p\). Write \(S\) for the selected set. A slot \(t\in[1,N]\) is available to \(e\) if \(t\in S\) and none of \(t\pm D_e\) lies in \(S\). Any matching of the labels to their available slots has the stated distance property. Sampling the extra sites gives each slot the same availability probability, including near the ends.

Give every availability edge incident with \(e\) weight \(w_e=(1-p)^{-2|D_e|}\). Thus \(1\le w_e\le L=n^{1/16}\) for large \(n\), using \(-\log(1-p)\le2p\). I claim that with positive probability every label has total incident weight at least \(Np/2\), and every slot has total incident weight at most \(2n\). Once this holds, the incident weight of any \(j\) labels is at least \(4nj\), so their neighborhood contains at least \(2j\) slots. Hall's theorem gives the matching.

Here are the two concentration estimates. For a fixed label \(e\) and candidate slot \(t\), its availability indicator depends on the bits at \(t\) and \(t\pm D_e\). The indicators as \(t\) varies have a dependency graph of maximum degree at most \((2d+1)^2\), by subtracting two offsets in the same list. The mean number of available slots is \(\mu_e=Np/w_e\ge8n/L\). The probability of obtaining fewer than \(\mu_e/2\) is at most \(\exp(-c\mu_e/(1+(2d+1)^2))\).

For a fixed slot \(t\) condition on \(t\in S\). The remaining availability indicators, indexed by \(e\), are independent whenever their lists do not intersect. The dependency graph has maximum degree at most \(d\Delta\). Each weighted indicator has mean 1 and size at most \(L\). The probability of total weight above \(2n\) is at most \(\exp(-c n/(L(1+d\Delta)))\). When \(t\notin S\) this total is zero. The two exponents are at least \(n^{15/16-o(1)}\), and the union bound applies to the \(n+N\) tests.

For completeness, both bounds follow by greedily coloring the dependency graph in \(q\) colors and applying Hölder's inequality to the \(q\) independent-within-color products. For variables \(0\le X_i\le1\), convexity gives \(\mathbb E e^{uX_i}\le\exp((e^u-1)\mathbb E X_i)\). Consequently \(\mathbb E e^{t\sum X_i}\le\exp((e^{qt}-1)\sum\mathbb E X_i/q)\). Optimizing at \(e^{qt}=1/2\) or \(2\) gives the stated bounds. For the slot test, divide the weights by \(L\) first.

## Odd-row stars

Fix an odd row \(o\). Give every even row \(e\) a label with endpoints \(o,e\), and measure the horizontal slot coordinates in units of eight. The blocked set for an in-strip vertical rival is contained in
\[
 D_e=\{d\ge1:(8d)^2+(e-o)^2=L^2\text{ for some integer }L<h\}.
\]
Any two labels placed by the lemma in the same interval avoid all such rivals within that interval.

The divisor identity \((L-8d)(L+8d)=(e-o)^2\) gives \(d_{\max}=h^{o(1)}\), where \(d_{\max}\) denotes the maximum list size. Conversely \((L-|e-o|)(L+|e-o|)=(8d)^2\) gives \(\Delta=h^{o(1)}\), since at most two rows have any given positive distance to \(o\). Also
\[
 \sum_e |D_e|=O(h\log h).
\]
Indeed the odd leg of each triple fixes at most two labels. A primitive triple of hypotenuse \(u^2+v^2\) admits at most \(h/(u^2+v^2)\) scales. Summing over \(1\le v<u\le\sqrt h\) gives \(O(h\sum_{u\le\sqrt h}1/u)\).

Group the labels of this star by dyadic list size, with empty lists in a separate group, and apply the lemma separately to every group with \(n_j\ge h^{1/3}\) members. The sum of the internal lengths is
\[
 O\!\left(\sum_j n_j+\frac{\sum_e |D_e|}{\log h}\right)=O(h).
\]
All smaller groups together have at most \(h^{1/3+o(1)}\) labels per star. Across the entire board their count is \(h^{4/3+o(1)}\), within the archive's \(O(h^{3/2})\) exceptional-label allowance.

The calculation treats each size group as a separate interval. It does not pay for keeping different intervals free of mutual P collisions. In particular inserting a length-\(h\) guard for each group would lose the linear per-star estimate. It also imposes no constraints for tilted right angles, mixed supports or fillers. The [pooled star packing argument](pooled_star_packing.md) handles the physical gaps across groups in total width \(O(h^2)\), with contiguous intervals for each star at each tier.
