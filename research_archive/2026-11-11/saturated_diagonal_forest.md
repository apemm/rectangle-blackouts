# A boundary-safe diagonal forest identity

Research note, 11 November 2026. This audits Section 7 of
[quadratic_threshold_reattack.md](quadratic_threshold_reattack.md).
The source file is unchanged.

The global list of diagonal junction types needs an end qualification. The counting identity has a different proof that works at both ends. It counts tree components, which need not be zigzag paths.

## 1. Saturation forbids every three-black tilted rectangle

Let \(h\ge4\), let \(m=q_h=\lfloor h^2/4\rfloor\), and suppose an equality board has no singleton columns. Its double labels are the distinct edges of a balanced complete bipartite graph \(K_{A,B}\).

Every white point \(W=(x,r)\) completes an axis rectangle with three black corners. Indeed, the double in column \(x\) has a unique row \(s\) in the part opposite \(r\). The edge \(\{r,s\}\) occurs in a different column \(z\). Its column cannot be \(x\), because \(W\) is white. The axis rectangle with columns \(x,z\) and rows \(r,s\) has presentation \(\{W\}\).

Consequently, a tilted rectangle with exactly three black corners is invalid. A hidden rectangle is also invalid when both board dimensions are at least four, by the established hidden-rectangle theorem. Thus every tilted rectangle has at most two black corners.

This implication uses saturation. An arbitrary all-double board need not have every opposite-class row pair available as an axis owner.

## 2. The global junction list fails at finite ends

Consider the \(7\times4\) board with columns
\[
 \{1,7\},\quad \{3,7\},\quad \{1,5\},\quad \{4,6\}.
\]
It is valid: direct enumeration of all rectangles gives distinct presentations. Every tilted rectangle has at most two black corners.

At \(V=(3,5)\), the following three points are black:
\[
 (4,6)\quad\hbox{(NE)},\qquad
 (1,7)\quad\hbox{(NW)},\qquad
 (4,4)\quad\hbox{(SE)}.
\]
The NE/NW completion is \((2,8)\), above the board. The NE/SE completion is \((5,5)\), beyond the right end. The point therefore has chain type \((1,2)\), excluded by the source's proposed global list.

This board is not saturated: it has four doubles, while \(q_7=12\). Its labels are a subset of \(K_{\{1,3,4\},\{2,5,6,7\}}\). It disproves the global junction claim, not the proposed strict threshold lower bound. It is also narrower than its height.

## 3. The forest lemma

Let \(S\) be a set of lattice points in a rectangular board. Suppose every rectangle with sides of slopes \(+1,-1\) has at most two points in \(S\).

Construct a bipartite graph \(G\). Its vertices are the occupied lines of slopes \(+1\) and \(-1\). Each point of \(S\) is an edge joining its two lines.

**Lemma.** The graph \(G\) is a forest.

**Proof.** Assume a simple cycle exists. Among its slope-\(+1\) lines choose one with minimum line index \(u_0\). Its two neighboring slope-\(-1\) lines in the cycle are \(v_1,v_2\). Let their other cycle neighbors be \(u_1,u_2\).

If \(u_1=u_2\), the cycle has length four. Its four intersections are black corners of an in-board rectangle, a contradiction.

Otherwise relabel so that \(u_0<u_1<u_2\). The three intersections
\[
 (u_1,v_1),\qquad (u_0,v_1),\qquad (u_0,v_2)
\]
are black. The fourth intersection \((u_1,v_2)\) lies between \((u_0,v_2)\) and \((u_2,v_2)\) on their physical line. Both endpoints lie in the board, so the fourth point also lies in the board. All four intersections are lattice points: the two diagonal indices in one connected component have fixed parity. They form a rectangle with at least three black corners. This is again a contradiction. \(\square\)

The proof uses the full no-three-corner hypothesis. Excluding only fully black rectangles would merely exclude four-cycles and would not justify this argument.

## 4. The exact finite-board identity

Let \(C(S)\) be the number of nonempty tree components of \(G\). Let \(E(S)\) be the number of empty physical diagonal lines, counting both slope families. There are exactly \(2(m+h-1)\) physical lines.

A forest has one more vertex than edge in each component. Since the edge set is \(S\),
\[
 C(S)+E(S)=2(m+h-1)-|S|.                         \tag{1}
\]
For an all-double board,
\[
 \boxed{C(S)+E(S)=2h-2.}                         \tag{2}
\]
An isolated edge is a point alone on both its lines. When all remaining components do have the source's zigzag form, their component count reproduces the stated identity. In general the nontrivial components can branch, including at the example in Section 2.

More generally, if each column is a singleton or a double and there are \(t\) singleton columns, then the same no-three-corner hypothesis gives
\[
 C(S)+E(S)=t+2h-2.                               \tag{3}
\]
A valid board with singletons can contain three-black tilted rectangles. Equation (3) therefore needs its explicit extra hypothesis; it is not asserted for every valid equality board.

## 5. Every primitive perpendicular slope pair

Fix coprime positive integers \(a,b\), and use directions
\[
 u=(a,b),\qquad v=(-b,a).
\]
Assume every rectangle with sides parallel to these directions contains at most two points of \(S\).

The same incidence graph is a forest. Work separately in each coset of the lattice \(\mathbb Zu+\mathbb Zv\). The permissible indices along a line form an interval within that coset. The minimum-index cycle argument therefore applies without requiring every intersection of arbitrary lattice lines to be integral.

There are exactly
\[
 L_u=mh-(m-a)_+(h-b)_+,\qquad
 L_v=mh-(m-b)_+(h-a)_+
\]
nonempty physical lattice lines of the two directions in the full board. For example, the \(u\)-lines partition the board points into paths with consecutive step \(u\), and there are \((m-a)_+(h-b)_+\) such consecutive pairs.

With \(E_{a,b}\) counting lines empty of \(S\), the exact identity is
\[
 C_{a,b}(S)+E_{a,b}(S)=L_u+L_v-|S|.              \tag{4}
\]
If \(m,h\ge\max(a,b)\) and the board is all-double, this is
\[
 C_{a,b}+E_{a,b}=(a+b-2)m+(a+b)h-2ab.           \tag{5}
\]
Only \(a=b=1\) removes the width term. Thus the special strength of the \(45^\circ\) count is real, even after correcting the boundary argument.

## 6. Cycle rank and singleton completions

For an arbitrary set \(S\), let \(\beta(S)\) be the cycle rank of the occupied diagonal-line graph. Euler's identity gives
\[
 C(S)+E(S)=2(m+h-1)-|S|+\beta(S).                \tag{6}
\]

Suppose \(h,m\ge4\) and \(S\) is valid. Let \(s_{45}(S)\) count its slope-\(\pm1\) rectangles with exactly three black corners. Then
\[
 \beta(S)\le s_{45}(S).                          \tag{7}
\]
To prove this, repeat the minimum-index cycle argument. It supplies a rectangle with at least three black corners, three of which are edges of the chosen cycle. A valid board has no hidden rectangle, so it has exactly three. Delete one of those cycle edges. This lowers the cycle rank by one. Repeating destroys \(\beta(S)\) different three-black rectangles.

Deletion cannot create a new three-black rectangle from an originally hidden rectangle, because the original valid board had none. Nor can a destroyed rectangle reappear under further deletion. Thus all selected rectangles were distinct members of the original family, proving (7). This part only needs absence of hidden rectangles. Validity also says that the white completion points of the selected rectangles are distinct.

Now assume the full equality structure, with \(t\) singleton columns and all double labels \(K_{A,B}\). A three-black tilted rectangle cannot complete in a double column, by Section 1. If it completes at row \(r\) of a singleton column whose black row is \(s\), then \(r,s\) must lie in the same part. Otherwise the double label \(\{r,s\}\) supplies its singleton axis rival. A singleton column therefore provides at most \(\max(|A|,|B|)-1\) possible completion points. Consequently
\[
 \beta(S)\le s_{45}(S)
 \le\bigl(\lceil h/2\rceil-1\bigr)t.             \tag{8}
\]
Since \(|S|=2m-t\), equations (6) and (8) give
\[
 2h-2+t
 \ \le C(S)+E(S)
 \ \le 2h-2+\lceil h/2\rceil t.                  \tag{9}
\]
For \(t=0\), this recovers the forest identity. It supplies a boundary-safe version of the source's proposed correction term when singleton columns are present.

The completion budget also works simultaneously across slopes. Let \(\beta_{a,b}\) be the cycle rank of the line-incidence graph for the primitive perpendicular pair \((a,b),(-b,a)\), where \(a,b>0\) and \(\gcd(a,b)=1\). Then
\[
 \boxed{\sum_{a,b}\beta_{a,b}
 \le \#\{\text{three-black tilted rectangles}\}
 \le\bigl(\lceil h/2\rceil-1\bigr)t.}            \tag{10}
\]
Only \(a+b\le\min(h-1,m-1)\) can contribute. For each slope pair, the deletion proof selects \(\beta_{a,b}\) different original rectangles. Rectangles from different slope pairs differ, and a valid board gives them different white completion points. Thus their counts share one budget, rather than a separate budget for each slope.

Equation (10) is a necessary condition computable from line incidences. It still needs a positive forced cycle, or another source of forced completions, before it yields \(t\ge1\).

## 7. What remains for a strict threshold bound

For a saturated board, (2) is proved. It does not contradict saturation: it supplies an exact component budget, not a lower bound exceeding that budget.

A proof that \(m_h\ge q_h+1\) would need another input. Possible inputs include the complete coverage of \(K_{A,B}\), or the two-black mixed rectangle collisions omitted by the no-three-corner condition. The present argument does not establish that every all-double board is invalid. Section 2 supplies a valid counterexample to that broader statement.

The accompanying [exact checker](check_saturated_diagonal_forest.py) and [output](check_saturated_diagonal_forest.json) verify the finite example, the branching junction, and the forest identity. The forest proof and general-slope formula do not depend on the computation. The forest and general-slope arguments received an independent review.

