# Odd-height windows and the threshold inequality

Coordinates are (column,row), starting at one. Write w(h) for the window
width in the two-problems draft, and q=floor(h²/4).

## A width-h window at every odd height

For odd h at least five, take
\[
 D_0=\{(x,x):1\le x\le h-1\},\qquad
 D_1=\{(x,x-1):2\le x\le h\}
\]
and add A=(1,h), B=(h,1). Each of the h columns has two points.
The distinct row pairs are the edges of the cycle on rows 1 through
h-1 in natural order, plus the edge {1,h}. The cycle has even length.
Give its vertices alternating colors and give h the color opposite 1.
The resulting partition is balanced.

Here is a direct check of the rectangle condition. A vector between
two regular points in different columns has the form (t,t+e) with
e in {-1,0,1}. If it is tilted, its coordinates have the same strict
sign. Consequently two tilted vectors between regular points at a
common vertex cannot be perpendicular. At A the vectors to all points
have signs (+,-) or an axial zero, so there is no tilted right angle
at A. The same holds at B with signs reversed.

If exactly one exceptional point is a *leg endpoint* of a right
angle whose other two vertices are regular, its fourth corner is the
exceptional point plus a regular leg (t,t+e). A tilted such leg has
strictly equal coordinate signs, so this fourth corner lies outside
the square at either A or B. Finally no tilted rectangle in the square
can contain both A and B. They cannot be endpoints of a side, since
a perpendicular translate of that side would take an endpoint outside.
If they are opposite corners, the other diagonal must have the maximum
possible length, the diameter of the square. The other diagonal can
only join (1,1) to (h,h), giving an axis-aligned rectangle.

Thus w(h) >= h for every odd h >= 5. Together with the even-height
construction in [the window draft](../../papers/extremal/drafts/window_conjecture.tex),
this shows w(h) >= h for every h >= 4. If the conjectured upper bound
holds, equality follows at every height. A window is only a necessary
local condition on a run of doubles in an optimal blackout.

## Restoring the stronger threshold inequality

The draft allows one exceptional run with a fully black tilted
rectangle. The [earlier archive proof](../2026-11-13/lower_bound_windows.md)
already excludes this case when both dimensions are at least four.
Here is the geometric argument, checked against the presentation
definition.

If a fully black tilted rectangle has an oblique diagonal AC, take
P and Q to be the other corners of the axis-aligned rectangle with
opposite corners A,C. The segments AC, BD (the original other
diagonal), and PQ have the same midpoint and length. They are distinct
unordered segments. Indeed, if BD=PQ, the original rectangle was
axis-aligned. The rectangles with diagonal pairs (AC,PQ) and (BD,PQ)
therefore have symmetric difference exactly the four black corners,
a contradiction.

If both diagonals are axial, the rectangle is an integral diamond of
radius d. For d>=2, divide it into two rectangles by a lattice cut
parallel to one side, one primitive step from the opposite side.
The two pieces have the four original corners as their symmetric
difference. For d=1 choose a diagonal translation u=(s,t), where
s,t are signs, that sends the center to another interior lattice point.
Both choices of a sign can be made inward since both grid dimensions
are at least four. With v=(s,-t), the diamond has side vectors u,v.
Its translate by u and its union with that translate (the rectangle
of sides 2u,v) are in the grid. Their corner sets have the original
four corners as their symmetric difference. This again contradicts
validity. Here a lattice cut need not pass through the midpoint.

On an equality board every white point of a double column is the
unique visible corner of an axis rectangle: pair its row with the
black row in the opposite partition part, and use the owner of that
row pair. Hence a tilted rectangle entirely inside a run of doubles
cannot have exactly three black corners. The preceding lemma excludes
four. Every run of doubles is therefore a window. The q doubles
require at least ceil(q/w(h)) runs and at least one singleton between
successive runs. Consequently
\[
 m_h\ \ge\ q_h+\left\lfloor\frac{q_h-1}{w(h)}\right\rfloor .
\]
This is the November 13 inequality, and its geometric proof supplies
the missing unit in the current draft. Using the November 16 LRAT
window values w(h)=h for h=4,...,12 gives, in order, lower bounds
4, 7, 10, 13, 17, 22, 27, 32, and 38. In particular m_7>12 and
m_8>16 already follow. The seven-row archive reports the stronger
m_7=21 using additional finite computations.

These lower bounds do not imply the conjectured upper bound on m_h.
