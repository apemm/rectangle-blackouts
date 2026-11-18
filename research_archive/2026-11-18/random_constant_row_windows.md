# Random constant rows on affine diagonals

For every fixed \(\eta>0\) and all sufficiently large \(h\), there is a filled board of width \(O_\eta(h^2)\) with every one of the \(\lfloor h^2/4\rfloor\) parity labels as a double and with every window of horizontal span at most
\[
 H=\lfloor h/(\log h)^{1+\eta}\rfloor
\]
valid. The local tests include a hypothetical owner anywhere in the full parity graph. This improves the [previous all-label radius](all_label_local_radius.md). It leaves collisions of larger span uncontrolled.

## One trial

Write the two true rows of a label as \(a=2i+1,\ b=a+T\) with \(T\) odd. Work on a single signed diagonal \(T\) and split by \(i\bmod14\), so both rows are fixed modulo 28. In one band place the selected doubles at \(x=x_0+28i\). Fill every other column in one odd row \(s\). Take \(x_0=0\bmod 28\) in local coordinates. Impose
\[
 s\equiv a+2\pmod 4,\qquad
 s\equiv (a+b)/2\pmod 7\quad(a\not\equiv b\bmod7).
\]
For \(a\equiv b\bmod7\), choose \(s\equiv a+1\bmod7\). In either case \(s\) is different modulo seven from both true rows. Choose \(s\) uniformly among the members of this residue class modulo 28 in \([1,h]\).

Define \(D_T\) to consist of the positive \(d\) with \(28d\le H\) for which at least one of \((28d)^2+(T\pm2d)^2\) is a square with positive root below \(h\). Properly color the index graph with distances \(D_T\) using at most \(1+2|D_T|\) colors. Give each color its own band. Across all \(T\),
\[
 \sum_T |D_T|=O\big(H\log(2h)(1+\log(2h/H))\big).
\]
Indeed, each positive even horizontal leg \(X\le H\), odd vertical leg magnitude \(Y\), and integral hypotenuse below \(h\) can supply at most four signed diagonals \(T\), since \(d=X/28\) is fixed. The Euclidean parametrization and harmonic sum in the [previous window proof](all_label_local_radius.md) give the bound.

In a trial discard a label if one of the following tests fails.

1. Both \(|s-a|\) and \(|s-b|\) exceed \(H\).
2. There is no \(1\le X\le H\) with \(X^2+(b-s)^2\) square.
3. Neither \(a-s\) nor \(b-s\) is a possible side gap of a short crossed mixed support for physical slope \(14\), as defined below.

Here and below a band means the full constant-row word with its chosen doubles, extended on either side in the same row. Any subset of the passing labels of one independent color may be used. The following checks also apply if a would-be sea cell in a true column is included in a calculation. The actual band uses that column only for the double.

## Geometry inside a band

All nonvertical true chords satisfy \(v_2(X)>v_2(Y)\). Same-role chords have \(X=14Y\) and \(v_2(X)=1+v_2(Y)\). Cross-role chords have odd \(Y\) and \(4\mid X\). A same-role true chord has nonintegral length \(\sqrt{197}|Y|\). These are precisely the true-point hypotheses of the [four-column mixed-support proof](four_column_matching_sea.md). Consequently there is no true tilted corner triple or all-true mixed support with two nonvertical principal chords. In a mixed support with a vertical true diagonal the true side would have the same odd integral length below \(h\), excluded by its color. No opposite-role pair in distinct true columns can be a local vertical rival, by the same color test. An opposite-parity sea-to-true rival is excluded by test 2.

Consider a tilted corner triple with a sea point. A true pivot with two sea neighbors would require the product of their horizontal offsets to have magnitude \((s-y)^2>H^2\). If both true neighbors of a sea pivot are present, the absolute product of their vertical offsets also exceeds \(H^2\). A sea pivot with one sea neighbor has a horizontal leg and cannot be a tilted corner. At a true pivot with one true neighbor and one sea neighbor, a same-role neighbor would require \(14\xi=-(s-y)\) for a horizontal offset \(\xi\), contrary to the residue modulo seven. For an opposite-role neighbor the true displacement has horizontal part divisible by four and odd vertical part, while \(4\nmid s-y\). These cases also exclude a black tilted rectangle.

A mixed support with one true and three sea points compares a horizontal chord of length at most \(H\) with a chord of vertical magnitude greater than \(H\). For one sea and three true points, let \(t\) be the horizontal component modulo seven of the chord containing the sea point. The other chord is all true. Norm equality requires
\[
 t^2\equiv (y_2-y_1)^2-(s-y_3)^2\pmod7 .
\]
All \(y_j\) are one of the two row residues. If \(y_2=y_1\bmod7\) the right side is a nonzero negative square. Otherwise it is \(3(b-a)^2/4\). Both are nonsquares modulo seven. Thus even placements with \(t=0\) are excluded.

With two sea points, the two true points have the same parity by the even black row sum. If they form one principal chord, its nonintegral length excludes a horizontal sea chord. Otherwise both chords go from a sea point to a true point. Write \((u,g),(v,g+\Delta)\) for their oriented displacements, in side and diagonal order. The displacement between their true endpoints is \((14\Delta,\Delta)\), with \(\Delta\ne0\). The same calculation as in the [crossed-support proof](all_obstructions_short_windows.md), now for \(\kappa=14\), gives
\[
 u=b_0 k,\quad g=k(a_0-2\kappa b_0),\quad
 \Delta(a_0^2+b_0^2)=4 k b_0^2(\kappa b_0-a_0),\qquad
 (a_0,b_0)=1,\ b_0>0 .
\]
Indeed \((v-u)/\Delta=a_0/b_0\), and the two equations before elimination are \(u(2\kappa\Delta+u-v)=-g\Delta\) and \(u^2-v^2=\Delta(2g+\Delta)\). The common divisor of \(a_0^2+b_0^2\) and \(4b_0^2(\kappa b_0-a_0)\) is at most \(4(1+\kappa^2)\). Therefore with \(0<|u|\le H\) the number of possible nonzero \(k\) is \(O_\kappa(H/[b_0(a_0^2+b_0^2)])\). Summation over \(a_0,b_0\) gives \(O_\kappa(H)\) possible signed \(g\), independent of the height. Test 3 excludes each such support. A zero side offset would give a vertical black side and belongs to the separate axis-owner test.

## Repeated trials and relocation

For any given label, tests 1 and 3 exclude \(O(H)\) choices of \(s\). For test 2, \(b-s\) is odd. Its bad nonzero values are counted by triangles with even leg \(X\le H\) and hypotenuse at most \(2h\), since \(|b-s|<h\). Thus the same harmonic bound applies, without any in-strip restriction. As there are \(h/28+O(1)\) candidates for \(s\), the probability of failure of a trial is at most
\[
 O(H\log(2h)(1+\log(2h/H))/h)
 \le (\log h)^{-\eta/2}
\]
for sufficiently large \(h\). Choose \(K=\lceil 8/\eta\rceil\) independent trials for each diagonal and type. Assign each label to its first passing trial and its fixed color. The probability of missing all trials is at most \((\log h)^{-4}\). The missed subsets on distinct diagonals are independent. This dependence condition holds even when all labels of one type share their trial rows.

The total number of affine bands is at most \(14K\sum_T(1+2|D_T|)=O_\eta(h)\). Each needs \(O(h)\) columns, including \(H+1\) pure sea columns at either end. A short window meeting a change of sea row then sees only a step between two odd rows. Its cells form a coordinatewise chain after vertical reflection if necessary, so it has neither tilted triples nor nonvertical mixed supports, and its points have the same parity. We can append a step to constant row 1 at the end under the same rule.

Use [Theorem D](../../papers/extremal/drafts/upper_bound/part3_t1chain.tex) on missed ordinary labels with \(q=1,\ c=1,\ \rho=(\log h)^{-4}\), all signed diagonals, and its fixed \(\varepsilon=1/10\). The slot and class bounds in its proof give total core length \(O(h^2)\): the density term is \(O(h^2(\log h)^{-2}(\log\log h)^{C_1})\), and the lower-order terms in the core sum are \(o(h^2)\). The separate term \(h^2\log\log h\) charges the long gaps between the \(O(\log\log h)\) class cores per type. As in the [local relocation argument](all_label_local_radius.md), replace these gaps by multiples of seven in \([2H+2,2H+8]\). The finite types, collars and intertype gaps still cost \(O(h^2)\). Each short window meets at most one core and its original periodic exterior, or belongs to a collar or pure background. The class construction includes the virtual parity owner tests and the checks on allowed triangles. This step uses the positive-probability conclusion of Theorem D together with the deterministic band bound.

Theorem D leaves \(O(h^{2-\varepsilon}+h^{1+8\varepsilon}\log\log h)\) missed ordinary labels. There are at most \(O(h^{3/2})\) additional missed nonordinary labels. Place these with the [WP construction](../../papers/extremal/drafts/upper_bound/part8_assembly.tex) at width \(O(h^2)\), since its per-label overhead is \(h^{o(1)}\). Join the main row-1 end, WP and the compressed Theorem D component using their constant boundary rows as in the previous all-label theorem. Every local window survives, every column is occupied and every parity label occurs once.
