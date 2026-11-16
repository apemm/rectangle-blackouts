# Unit-step walks in an all-double N-window

14 November 2026. This settles the unit-step two-walk subclass of the
N-window problem. It does not settle the one-sided two-walk problem or
the general window conjecture.

Let \(h\ge4\). Suppose an N-window of width \(w\) contains the graph
of an integer walk \(f:\{1,\ldots,w\}\to\{1,\ldots,h\}\) with
\[
 |f(x+1)-f(x)|=1.
 \tag{1}
\]
If \(w\ge4\), then \(f\) is strictly monotone. In particular,
\[
 w\le h.
 \tag{2}
\]
If the two points of every column are given by two walks satisfying
(1), and the column pairs are distinct, then
\[
 \boxed{w\le h-1.}
 \tag{3}
\]
The bound is attained by the columns
\(\{1,2\},\{2,3\},\ldots,\{h-1,h\}\), with the parity bipartition.

## A unit-step walk cannot turn in width at least four

At a local maximum in column \(x\), the three walk points are
\[
 (x-1,r-1),\quad(x,r),\quad(x+1,r-1).
\]
They form three corners of a unit tilted square. Its fourth corner is
\((x,r-2)\). Since the horizontal coordinate is already in the window,
the N-condition requires \(r-2<1\). A genuine maximum has \(r\ge2\),
so \(r=2\), and its two neighbours both have row one.

If \(x\ge3\), the preceding walk point must have row two. The point
\((x-1,1)\) is then a local minimum with fourth corner \((x-1,3)\),
inside the board, a contradiction. Thus \(x=2\).
The same argument to the right gives \(x=w-1\).
Therefore a local maximum can occur only when \(w=3\).

Reflection in the horizontal midline gives the same conclusion for a
local minimum: it must have row \(h-1\), column two, and column \(w-1\).
Every change of direction is one of these two turns. At \(w\ge4\)
there are no turns, proving monotonicity and (2).

The width-three exception is real: the walk \(1,2,1\) has its only
tilted completion in row zero. It must not be excluded by the proof.

## Two walks and distinct pairs

For \(w\le3\), (3) follows from \(h\ge4\). Otherwise both walks are
monotone.

If their directions agree, write their starting rows as \(a<b\).
For increasing walks, the second one ends at \(b+w-1\le h\), and
\(b\ge2\), so \(w\le h-1\). The decreasing case is its reflection.

Suppose their directions differ. Before crossing, let their separation
be \(D\). At each step toward each other it decreases by two.
If \(D\) is even, the walks would meet in one column, contrary to having
two distinct points. If \(D\) is odd, crossing would exchange an
adjacent row pair between consecutive columns, contrary to the
distinct-pairs condition. Thus the walks cannot cross.

If they move toward each other throughout the window, then
\(2(w-1)<D\le h-1\); if they move apart, the final separation is at least
\(2(w-1)+1\) and at most \(h-1\). Either case is stronger than (3).

Finally, the proposed lower construction lies in the two adjacent
diagonal lines \(y=x\) and \(y=x+1\), which contain no tilted right-angle
triple. Its \(h-1\) column pairs are distinct parity edges, so it is an
N-window and proves sharpness.

## Consequences and limits

In a parity N-window, the two checkerboard classes each contain one
point per column. If either class has only unit row steps, then the
whole window has width at most \(h\). Consequently every hypothetical
counterexample to \(W_N(h)\le h\) has a nonunit step in each class.
More locally, every block of \(h+1\) consecutive columns contains a
nonunit step in each class.

The proof uses rectangles with their vertex between the other two black
columns. Those are precisely the angles omitted by the one-sided
OSRAF condition. Therefore this theorem gives no corresponding
monotonicity assertion for OSRAF walks.
