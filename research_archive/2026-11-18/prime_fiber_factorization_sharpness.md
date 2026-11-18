# The product scale in prime-fiber factorization is necessary

Use the zero-based coordinates and residue rule \(y\equiv\lambda x\bmod p\) of the [factorization theorem](prime_fiber_counting_lift.md). Suppose \(H,M\ge4\), the prime \(p\) exceeds \(\max(H,M)\), and
\[
 (H-1)(M-1)>p.
\]
For every nonzero slope \(\lambda\bmod p\) there is a blackout on the \(pH\)-by-\(pM\) grid supported on that residue rule whose induced blackouts on the fibers are all valid and whose global blackout is invalid. Four black cells suffice.

Consider the residues \(i+\lambda j\bmod p\) for \(0\le i\le M-2,\ 0\le j\le H-2\). A repeated residue yields an integer vector \((r,s)\ne(0,0)\) such that
\[
 r+\lambda s=0\bmod p,\qquad |r|\le M-2,\quad |s|\le H-2.
\]
Both coordinates are nonzero. If \(s=0\), then \(p\mid r\) and \(|r|<p\). If \(r=0\), use \(\lambda\ne0\) and \(|s|<p\).

Put \(U=p(r,s)\) and \(V=(s,-r)\). The two vectors are nonzero and perpendicular. The residue of \(U\) is zero, while \(V\equiv s(1,\lambda)\bmod p\) crosses between fibers. The vertex set \(\{0,U,V,U+V\}\) has horizontal span \(p|r|+|s|\) and vertical span \(p|s|+|r|\). The available horizontal translations form an integer interval with
\[
 pM-p|r|-|s|\ \ge\ 2p-(H-2)\ >p
\]
members, and the available vertical translations form an interval with
\[
 pH-p|s|-|r|\ \ge\ 2p-(M-2)\ >p
\]
members. Fix any allowed horizontal translation and choose a vertical translation agreeing with \(\lambda\) times it modulo \(p\). All four translated vertices now satisfy the residue rule and lie in the grid.

Color only those four cells black. Each of two fibers receives a pair of cells separated by \(U\); every other fiber is empty. Two distinct rectangles have at most two common vertices because three corners determine a rectangle. Their vertex sets therefore have symmetric difference of size at least four. Equal white presentations require the symmetric difference to be all black, which a fiber with at most two black cells cannot do. Every induced blackout is consequently valid. The large grid contains the fully hidden rectangle with sides \(U,V\), forbidden by the [hidden-rectangle lemma](windows.md) in dimensions at least four.

The same construction also gives failure at arbitrary long widths without the hypothesis \(p>\max(H,M)\). For any odd prime \(p\), let \(s=1\) and choose the least absolute representative \(r\) of \(-\lambda\), so \(1\le |r|\le(p-1)/2\). If \(H\ge3\) and \(M\ge(p+3)/2\), the horizontal translation interval has at least \(2p-1\) members, and the vertical translation interval has at least \(2p-(p-1)/2>p\) members. The previous argument applies.

Thus the order-\(HM\) sufficient bound is sharp up to an absolute factor for arbitrary inputs when \(p>\max(H,M)\). If complete \(H\)-row templates have \(M\ge cH^2\) and \(h=pH\), a uniform arbitrary-input factorization in this range requires \(p=\Omega(h^{3/4})\). The obstruction uses sparse inputs and does not rule out a smaller prime for specially chosen complete templates.
