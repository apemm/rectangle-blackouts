# The optimum one column before eventual equality

Let \(M=m_h\) be the least integer such that \(f(h,m)=m+q_h\) at every width \(m\ge M\), where \(q_h=\lfloor h^2/4\rfloor\). For \(h\ge6\),
\[
 f(h,M-1)=M-1+q_h-1,\qquad a_h(M)\le a_h(M-1).
\]
In particular the last width of failure always misses one cell, and every optimum at width \(M\) has a double in each end column. These conclusions use no assumption that earlier equality widths form an interval.

Indeed \(M\ge q_h\) by the equality theorem (there must be \(q_h\) doubles), and \(M-1\) fails by minimality. An optimum at \(M\) has only singletons and doubles and has every edge of a balanced complete bipartite row graph once. Restrict it to the first \(M-1\) columns. Restriction preserves geometric validity, so removing a singleton would yield equality at a failing width. The last column is a double, and the prefix has one fewer cell than the row upper bound. It is optimal by integrality. Apply the same argument at the other end. [Equality characterization](../../papers/extremal/sections/sec3_rowbound.tex)

The double graph of the prefix is a balanced complete bipartite graph with one edge missing. Both parts have at least two vertices, so this graph is connected and determines its two parts up to interchanging them. Its missing edge is unique. Thus two distinct width-\(M\) maxima cannot have the same width-\(M-1\) prefix. More precisely, \(a_h(M)\) equals the number of width-\(M-1\) optima with no empty column and balanced double graph missing one edge for which appending that edge as the last double passes geometric validity. This is an extension test on one specified pair. The newly restored pair can supply a remote axis owner, so a test limited to the last few columns without a remote-owner check would be insufficient.

All optima at \(M-1\) have one of the following row structures. With one empty column their double graph is balanced and complete. With no empty column their double graph is balanced and missing one edge, or, when \(h=2s\), it is a complete graph \(K_{s-1,s+1}\) between the parts. To prove the list, let \(z\) count empty columns. The intrinsic deficit of the occupied columns is \(1-z\), so \(z\in\{0,1\}\). Since \(1<\lfloor h/2\rfloor-1\), the [near-bound classification](../2026-11-09/full_problem_push/square_finitewidth_progress.md) makes every occupied column a singleton or a double, and the double graph is bipartite. For part sizes \(a,h-a\) the deficit is the sum of \(q_h-a(h-a)\) and the missing cross edges. For even height the first term is an integer square, and for odd height it is \(j(j+1)\) with \(j\ge0\). This gives the list. The cropping argument guarantees a member of the balanced one-missing-edge class. Attainment of the other classes depends on geometry.

The same restriction gives a count bound at every jump of two cells sufficiently close to the row bound. Write \(\delta_j=j+q_h-f(h,j)\). If \(j\ge4\), \(f(h,j)-f(h,j-1)=2\), and \(\delta_j<\lfloor h/2\rfloor-1\), then
\[
 a_h(j)\le(\delta_j+1)a_h(j-1).
\]
Every width-\(j\) optimum has at most two cells per column, so its last column must be a double and its prefix is an optimum. Its prefix double graph has at least \(q_h-\delta_j-1>q_{h-1}\) edges, because empty columns only lower the intrinsic deficit. A disconnected triangle-free graph on \(h\) vertices has at most \(q_{h-1}\) edges: apply Mantel's bound to its components and merge their sizes to maximize the sum, leaving parts of sizes \(h-1,1\). This last inequality also follows directly from convexity of the integer sequence \(q_n\). The prefix therefore has a unique bipartition. Among its cross pairs at most \(\delta_j+1\) are missing, which bounds the number of possible last doubles.


When \(M>q_h\) the count inequality is strict, with
\[
 a_h(M)\le \frac{q_h-1}{q_h}\,a_h(M-1).
\]
Form a directed graph on width-\((M-1)\) optima, using each width-\(M\) optimum as an edge from its prefix to its suffix. The unique missing double gives both indegree and outdegree at most one. If an edge is followed by another edge, the next full word is its cyclic left rotation. Indeed, the suffix is missing precisely the first double of the old word, so this double must be appended. Every full word in the graph has minimal rotation period \(M\), because it contains a double label occurring just once. A directed cycle would therefore include all rotations. Every rotation would start with a double, contradicting \(M>q_h\). In a path with \(t\) edges the \(t\) starting columns and the column just before the first starting column must all be doubles. A singleton occurs somewhere, so \(t<M\) and these are \(t+1\) distinct columns. Thus \(t\le q_h-1\). A path with \(t\) edges has \(t+1\) vertices, which proves the bound after summing over paths, including isolated vertices.


At height seven the archive gives \(M=21\), \(q_7=12\), \(a_7(20)=3364\), and \(a_7(21)=4\). The restriction map identifies four of those 3,364 width-20 optima: each accepts its unique missing pair at the right edge. The size formula gives \(f(7,20)=31\). [Seven-row threshold and count tables](../2026-11-09/full_problem_push/REPORT.md)

