# A growing filler palette avoids two Pythagorean directions

15 November 2026. The actual slow interpolation gives a positive
row-choice theorem that is stronger than square-root locality alone.
For the two directions \((4,3)\) and \((12,5)\), every sufficiently
large target palette has a positive fraction of norm-safe rows.
After imposing a literal forbidden row set of size \(b\), only \(O(b)\)
palette centers can fail this availability conclusion.

The theorem changes one selected singleton when its opposite-parity
guard already exists. It does not create that guard, exclude other
P directions, or resolve the other forbidden support families.

## 1. A deterministic plateau theorem

Fine columns are \(x=4r\), \(r\in\mathbb Z\). Fix a target column,
and translate its rank to zero. The selected opposite-parity sources
form a single-valued partial row-index function \(z(r)\), with one
fixed physical row residue modulo four. Assume:

1. For every two selected source ranks,
   \[
       |z(r)-z(s)|^2\le |r-s|/16+1.                 \tag{1}
   \]
2. The partial function has a piecewise-constant extension to the
   integer rank interval containing all relevant sources. Its jump
   locations are separated by at least \(G\ge256\).

The extension need not satisfy (1) at artificial values inserted
inside parity holes. Condition (1) is used only at actual sources.
The jump amplitudes may be arbitrary.

Consider \(K\) consecutive target rows in one opposite-parity
residue class modulo four. Then at least
\[
 \left({1\over5}-{224\over5G}\right)K-40             \tag{2}
\]
choices have no integral-distance partner among the selected sources
in either primitive direction \((4,3)\) or \((12,5)\), including
both horizontal and vertical signs.

In particular, \(G\ge256\) gives at least \(K/40-40\) choices.
If \(G\ge512\), the weaker convenient bound \(K/10-40\) holds.
Actual P partners are a subset of these norm partners, so the same
choices avoid all actual P constraints in these two directions.

### Signed scales and monotone target indices

Fix one direction \((u,v)\in\{(4,3),(12,5)\}\), and one horizontal
sign \(\sigma\). A possible source has
\[
       r=\sigma u|t|/4,\qquad
       y_{\rm target}=y_{\rm source}+vt,            \tag{3}
\]
where \(t\ne0\) is a signed integer. The fixed source and target
residues imply \(t=t_0+4n\), for one odd \(t_0\in\{1,3\}\).
If target rows are indexed by \(j\), (3) reads
\[
          j(n)=z(r(n))+vn+c,\qquad
          r(n)=\sigma u|t_0+4n|/4,                  \tag{4}
\]
with a fixed integer \(c\).

For two scales \(n_1<n_2\) that give actual selected sources, put
\(d=n_2-n_1\). Their source-rank distance is at most \(ud\). Thus
\[
 j(n_2)-j(n_1)\ge vd-\sqrt{ud/16+1}>0.              \tag{5}
\]
The strict inequality holds for both displayed directions and every
integer \(d\ge1\). It includes the turn of the absolute-value map.
In particular, the hit indices are strictly ordered.

Restrict to hits in the target interval \(0\le j<K\). If they are
nonempty, their extreme scales satisfy
\[
 vd\le K-1+\sqrt{ud/16+1}
       \le K+\sqrt{ud/16}.
\]
Using
\(\sqrt{ud/16}\le vd/2+u/(32v)\), obtain
\[
                         d\le {2K\over v}
                                     +{u\over16v^2}. \tag{6}
\]

### Counting residue phases

As \(n\) traverses this scale interval, the rank \(r(n)\) moves
monotonically or turns once. Its total rank travel is at most \(ud\).
A path of this form crosses at most \(ud/G+2\) jump locations of
the extension, counting a location twice if it is traversed twice.
Hence its selected hits split into at most
\[
                             L_{u,\sigma}\le ud/G+3 \tag{7}
\]
successive constant-row pieces. If there are no hits, use one arbitrary
phase, which also meets this upper bound.

On a constant-row piece, (4) forbids only one residue class of target
indices modulo \(v\). By (5), the integer hulls of consecutive pieces
are disjoint and ordered. Extend each residue phase through any
intervening gap, as well as to the ends of the target interval.
This only adds forbidden candidates. The resulting overgraph has
at most \(L_{u,\sigma}\) consecutive residue phases.

There are four such lists: two horizontal signs for each direction.
Equations (6)--(7) give
\[
 \sum_{u,\sigma}L_{u,\sigma}
 \le {224K\over15G}+12+{212\over225G}.                \tag{8}
\]
For example, the constant term before the factor \(2/G\) is
\(1/9+9/25=106/225\).

Partition the target interval at the phase changes of all four lists.
There are at most \(1+\sum L_{u,\sigma}\) resulting intervals.
Within each interval, at most two residues modulo three and at most
two residues modulo five are forbidden. The Chinese remainder theorem
leaves at least three of every fifteen consecutive indices safe.
An interval of length \(\ell\) therefore contributes at least
\(\ell/5-3\) safe indices.

Summing this bound and using (8) proves
\[
 \#\{\text{safe choices}\}
 \ge \left({1\over5}-{224\over5G}\right)K
                                      -39-{212\over75G},
\]
which implies (2). No independence of the four source lists is used.

## 2. The actual fine menu supplies the plateau hypothesis

Use the constants and geometry of
[the fine multi-anchor theorem](continuation_fine_multi_anchor_compatibility.md):
\[
             G_0=256D,\qquad M=4096D^2,\qquad D\ge1.
\]
That theorem supplies (1), since \(4\epsilon_0=1/16\).

Outside modified caps, keep its original total fine coordinate.
Its unit jumps are separated by at least \(G_0\).
Within a modified cap, the common role is constant. In the other
role, fix all bridge choices. On a bridge interval \([a,b]\) of
length \(L\ge M\), the left value is offered through \(p\), the right
value from \(p+d\), and
\[
                a+L/4\le p\le p+d\le a+3L/4.       \tag{9}
\]
Extend that coordinate through the parity hole by making one jump
between the two values at any integer time in this middle interval.
For example, use a midpoint of \([p,p+d]\). This is an auxiliary
extension for counting; no black point is added.

Jump locations in consecutive bridge intervals are separated by at
least \(M/2-1\). This exceeds \(G_0\). The same estimate holds across
different adjacent modified caps, using their end plateaus. A bridge
jump is at least \(M/4-1\) from its cap boundary. The original fine
coordinate is constant in its coarse-anchor guards, so any outside
mesh jump is also separated from that bridge jump by more than \(G_0\).

Therefore this auxiliary total coordinate has all jump locations
separated by at least \(G_0\ge256\). A zero row difference contributes
no jump. Return intervals obey the same central-quarter condition.
Unmodified caps retain the original compatible fine coordinate.

Selecting only some offered points does not change the extension or
increase its number of jumps. The conclusion is consequently uniform
over the bridge positions, parity selections, and literal-good
omissions, provided the selected source function is the one supplied
by the compatible fine-menu theorem.

This argument uses the actual interpolation and cap order. The broad
square bound \(|\Delta z|^2\le q/2\) alone does not imply the plateau
hypothesis. The five-row counterexample in
[the growing-palette note](continuation_growing_row_palette_obstruction.md)
has much more frequent oscillations.

## 3. Actual-good choices and the exceptional centers

Let \(B\) be the forbidden target row indices in this fixed profile,
with \(|B|=b\). For every integer window start \(j_0\), put
\[
              N_B(j_0)=|B\cap[j_0,j_0+K-1]|.
\]
Each bad index belongs to exactly \(K\) such windows, so
\[
                       \sum_{j_0}N_B(j_0)=Kb.       \tag{10}
\]
At most \(80b\) window starts have \(N_B(j_0)>K/80\).

For every other start, (2) at \(G\ge256\) leaves at least
\[
                         K/80-40                    \tag{11}
\]
actual-good, two-direction-safe choices. For \(K\ge6400\), this is
at least \(K/160\). Windows crossing the ends of a prescribed profile
pool can be excluded separately, at a cost \(O(K)\) starts per
interval boundary.

Thus the deterministic exceptional-center set has size
\(O(b+K)\), with no sampling assumption. This does not assert that
a given forced singleton lies outside that set. Counting how often
its physical center belongs to it still requires the relevant
sampling or provenance estimate.

## 4. A genuine guarded retuning consequence

Suppose a singleton's initial row belongs to the target window, all
of its possible P partners are in the two stated directions, and
its window start is nonexceptional in Section 3. Suppose also that
every other rank within \(6(K^2+1)\) is already occupied by a selected
point of the opposite parity.

Choose a safe actual-good row from (11), and retune this singleton
without changing its parity. Its index displacement is at most \(K\).
Every other selected same-parity point is at distance
\(q>6(K^2+1)\). The old fine bound gives
\[
 |\Delta z_{\rm new}|^2
       \le 2|\Delta z_{\rm old}|^2+2K^2
       \le q/8+2+2K^2\le q/2.                       \tag{12}
\]
All other same-parity pairs are unchanged. The move preserves
occupancy, width, and the complete double-label list. It removes
all P incidents at this singleton under the direction hypothesis.

The guard must already exist. Creating it can introduce other P
pairs. Other directions and higher support families must still be
compiled or excluded. In particular, neither (11) nor (12) is an
all-direction filler theorem or an all-length reachability argument.

Independent written review: the complete theorem passed a separate
check of the signed-scale monotonicity, the exact coefficient in (2),
the CRT phase count, actual cap-extension jump spacing, exceptional
centers, and guarded retuning. The review retained the restrictions
to an already selected guard and the stated two directions.

