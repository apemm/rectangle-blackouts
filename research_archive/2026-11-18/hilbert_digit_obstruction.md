# How much digit memory a Hilbert coloring needs

Let \(s\) be a power of two. The vertex of Hilbert rank \(r\) has coordinates \((i_r,j_r)\) in \([0,s-1]^2\). In the normalized graph \(G_s(Q)\) of [the interleaving construction](ternary_interleaving.md), two ranks \(r,t\) are adjacent if either cross role gives a square
\[
 (Q(r-t))^2+(6(j_t-i_r)+1)^2.
\]
Here \(4\mid Q>0\). I give an obstruction to constructing bounded colorings by reading digits with bounded memory.

## Local color words

For a proper coloring with \(C\) colors, record the colors of every aligned dyadic \(L\)-square in traversal order. Write \(H\) for the number of different words among these squares.

**Theorem.** Let \(N\ge2\) be dyadic, \(B=N\), \(L=N^2\), and \(s\ge Q^2N^8/24+L\). Then
\[
 12 C^H\ \ge\ \log_2 N .
\]

**Proof.** Use the shift graph on ordered pairs \(0\le a<b<N\), joining \((a,b)\) to \((b,c)\) when \(a<b<c\). In a proper coloring, let \(S_a\) be the set of colors of pairs that start with \(a\). For \(a<b\), the color of \((a,b)\) is in \(S_a\) and is absent from \(S_b\). Thus the \(N\) sets are distinct. The shift graph needs at least \(\log_2 N\) colors.

In a canonical side-\(L\) square use the cell \((aB,bB)\) for \((a,b)\). Record the orientation of its \(B\)-square, the rank of that square modulo three, and the colors at this cell's local Hilbert rank in each of the \(H\) words. This gives at most \(12C^H\) types, since the Hilbert orientations are the identity, the swap of coordinates, the simultaneous complement of coordinates, and their composition.

If \(12C^H<\log_2 N\), two consecutive shift-graph pairs have the same type. Their chosen cells are \((aB,bB)\) and \((bB,cB)\). In their respective \(B\)-squares both occupy the local corner \((0,0)\). The common orientation gives that corner the same rank within both smaller squares. The positive rank difference \(d\) of the chosen cells is therefore a multiple of \(3B^2\), with \(d<L^2\).

Put \(T=Q^2d^2/24\). Writing \(Q=4q\) and \(d=3B^2v\) gives \(T=6q^2 B^4v^2\), a multiple of \(L\). Place the side-\(L\) tile with lower coordinate \((T,0)\) in the large square. The side assumption ensures it fits. Within it the same two ranks have equal colors by the type agreement, whichever local color word occurs. Their local cells shared a cross coordinate \(bB\). Every allowed tile orientation preserves some cross-coordinate equality, possibly exchanging the two roles. After translation one role therefore has \(j_t-i_r=-T\). Its squared distance is
\[
 (Qd)^2+(1-6T)^2
   =\left(1+(Qd/2)^2\right)^2 .
\]
This contradicts properness.

## Consequence for algorithms reading digits

A machine reads one base-four rank digit and the corresponding binary digit of each coordinate at each level, from most significant to least significant. The terminal state gives the color. If it has at most \(k\) states at the boundary of each aligned \(L\)-square, its prefix state and one of four orientations determine the entire remaining color word. Hence \(H\le4k\) and
\[
 12 C^{4k}\ge \log_2 N .
\]
This applies even if the transition functions vary by side and digit position, provided they agree across tiles at the same level and incoming state. In particular neither a fixed finite-state rule nor a coloring by fixed residues of coordinates and rank works at every side. The theorem leaves unrestricted bounded-color constructions open.

For \(Q=96,s=32\), ranks 291 and 375 give \((5,20)\) and \((5,26)\). Their ranks and coordinates agree componentwise modulo six. One cross role gives \(8064^2+127^2=8065^2\).

## The original bounded-choice question

In [Problem 1](../2026-11-15/two_problems/two_problems.tex) the horizontal scale of equal offsets is \(Q=SM\), and the vertical test is \(2(j_t-i_r)-4s+1\). Fix positive \(S,M\). No single deterministic bounded-state digit machine with the same transitions at all levels and sides can supply collision-free offsets at every side.

Use the shift graph again, but record the local transition function on *every* possible incoming state for each of the four outer tile orientations. Also record the orientation of the \(B\)-square. The number of types is bounded independently of \(N\), so a matched pair exists for sufficiently large dyadic \(N\). The rank gap \(d\) is a positive multiple of \(B^2\). Take \(B=N\ge8\). Then \(T=Q^2d^2/8\) is a multiple of \(L=N^2\), and \(T\ge8L\) for sufficiently large \(N\).

Choose the largest dyadic \(s\le T-L\). It satisfies \(s+L\le T\le3s-L\) and \(L\mid s\). There is an aligned \(L\)-tile inside the side-\(s\) board whose origin \((x_0,y_0)\) has \(x_0-y_0=T-2s\), since this multiple of \(L\) has absolute value at most \(s-L\). The two chosen local ranks read the same high input and induce the same state map on the low input in this tile. Their offsets agree. A preserved local cross equality gives vertical leg \(1-2T=1-(Qd/2)^2\), and the same square identity gives a collision.

This second argument uses level-independent transitions because it chooses the ambient side after finding the local pair. Arbitrary offsets remain an open case.
