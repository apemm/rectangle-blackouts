# An additive boundary loss for all-double windows

14 November 2026. This note improves the reduction in the archived
window_one_sided.md. It does not prove a bound on the one-sided
window width.

Let \(W_N(h)\) be the maximum width of an all-double window whose column
pairs are distinct edges of one balanced row bipartition and which has
at most two black corners in every in-board tilted rectangle.
Let \(W_O(h)\) be the corresponding maximum when no three black points
form a right angle whose two legs point to the same horizontal side.
The latter definition does not restrict the fourth corner.

Then
\[
 \boxed{W_N(h)\le W_O(h)+2\left\lfloor\frac{h-1}{2}\right\rfloor.}
 \tag{1}
\]
The older multiplicative reduction \(W_N(h)\le3W_O(h)\) remains valid;
one may take the minimum of the two bounds.

## The overshoot lemma

Consider a one-sided right angle with black vertex \(V=(x,y)\).
Reflect horizontally if necessary so both legs point right. After
interchanging them, write
\[
 X-V=(p,u),\qquad Y-V=(q,-v),\qquad p,q,u,v>0.
\]
All quantities are integers. Orthogonality and the row bounds give
\[
 pq=uv,\qquad u+v\le h-1.
\]
Consequently
\[
 \min(p,q)^2\le pq=uv\le (h-1)^2/4,\qquad
 \min(p,q)\le r_h:=\left\lfloor\frac{h-1}{2}\right\rfloor.
 \tag{2}
\]
The fourth corner \(F=X+Y-V\) has row \(y+u-v\), which lies between
the rows of \(X\) and \(Y\), so its row is automatically in the strip.
Its column is beyond the farther black endpoint by exactly
\[
 x_F-\max(x_X,x_Y)=p+q-\max(p,q)=\min(p,q)\le r_h.
 \tag{3}
\]
The reflected statement holds for a left-pointing angle.

This overshoot constant is sharp for unrestricted integer right-angle
triples. For \(h=2n+1\), use
\[
 V=(1,n+1),\quad X=(n+1,2n+1),\quad Y=(n+1,1).
\]
The overshoot is \(n=r_h\). For \(h=2n\), use
\[
 V=(1,n),\quad X=(n+1,2n),\quad Y=(n,1);
\]
the leg vectors \((n,n)\) and \((n-1,-(n-1))\) are perpendicular,
and the overshoot is \(n-1=r_h\).
This sharpness concerns the local geometric lemma, not equality in (1).

## Trimming the boundary

Let an N-window have width \(w>2r_h\), and retain columns
\[
 r_h+1,\ldots,w-r_h.
\]
If three retained points made a right-pointing right angle, (3) would put
its fourth column at most \(w-r_h+r_h=w\). Its column is positive and
its row is in the strip. Thus the original window would contain an
in-board tilted rectangle with three black corners, a contradiction.
The left-pointing case is identical.

The retained columns form an OSRAF window of width \(w-2r_h\); distinct
pairs and the bipartition are inherited. This proves (1). If
\(w\le2r_h\), the inequality is immediate.

Equivalently, every one-sided right angle in an N-window has a black
endpoint among the first or last \(r_h\) columns. Right-escaping angles
meet the last \(r_h\) columns and left-escaping angles meet the first
\(r_h\) columns.

## Consequence for equality thresholds

With \(q_h=\lfloor h^2/4\rfloor\), the archived window principle gives
\[
 m_h\ge q_h+
 \left\lfloor
 \frac{q_h-1}
 {\min\{3W_O(h),\,W_O(h)+2r_h\}}
 \right\rfloor.
 \tag{4}
\]
In particular, a proof \(W_O(h)\le Ch\) would now yield
\(W_N(h)\le(C+1)h+O(1)\), improving the former factor \(3C\).
More generally \(W_O(h)<q_h-2r_h\) suffices for
\(W_N(h)<q_h\) and hence \(m_h\ge q_h+1\).

No estimate of either form for arbitrary height is proved here.
