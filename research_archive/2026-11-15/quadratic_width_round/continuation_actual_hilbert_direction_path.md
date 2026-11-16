# A twelve-vertex fixed-direction path in the actual Hilbert refinement

15 November 2026. The following sparse certificate gives a twelve-vertex
directed path of slope \(3/4\) in the actual spacing-four Hilbert
refinement. It is longer than the smallest local obstructions, but does
not prove unbounded path lengths or failure of the private-size-64 Hall
condition.

Take a side-128 Hilbert block, replication size \(M=64\), and
coordinate-offset difference \(T=12669\). At a fine rank \(v\),
write \(r=\lfloor v/M\rfloor\), and \(H_{128}(r)=(i,j)\).
The physical rows are
\[
 a_v=8T+3+4i,\qquad b_v=12T+2+4j.
\]
The twelve fine ranks are
\[
\begin{split}
218304,235197,252142,269119,286092,303065,\\
320038,337063,354104,371149,388130,405139.
\end{split}
\]
At consecutive ranks \(v,w\), the exact identity is
\[
 b_w-a_v=3(w-v).
\]
Since their column difference is \(4(w-v)\), each directed edge
is an integer multiple of the 3--4--5 triangle. The gaps are odd and range
from 16893 to 17045. The half-factors equal these gaps.

Set \(h=16T=202704\). Every alternative vertical pair lies strictly
in the strip, and its column is \(2\pmod4\), so its two corners
are white in the constant sea \(L=1\). The odd endpoint rows exceed
\(h/2\) and are \(3\pmod4\); the even rows are \(2\pmod4\).
All objects have own gaps of order \(h\).

This pattern embeds into the actual padded Hilbert square, not just an
arbitrary rank assignment. Take \(N=524288\), choose the aligned
side-128 block at
\[
 I=J=196608=3N/8,
\]
and use the independent offsets
\[
 U_0=196608,\qquad U_1=158603.
\]
The block has identity orientation. For the genuine odd row pool starting
at \(h/2+3\) and the even pool starting at 10, their sizes are 25338
and 50672. The padded-side and offset inequalities of the folded-cap
construction hold. Every displayed point is inside its genuine rectangle,
so its folded coordinate agrees with the unmodified raw coordinate.

The checker evaluates both forward and inverse Hilbert routines only at
the required ranks. It verifies the global embedding, exact norms, all
alternative rows, row residues, and private offsets. This is a valid
potential path before good-row filtering. No claim is made that all its
rows survive the R2s set or subsequent source erasures. Only its first
displayed vertex is at private offset zero, and the path has fewer than
64 vertices. It therefore does not give a Hall obstruction for the
actual private palette.

Files: [check_actual_hilbert_direction_path.py](check_actual_hilbert_direction_path.py)
and [its exact certificate](check_actual_hilbert_direction_path.json).
The path was found in a small projection-matching probe over sixteen
offset differences at side 128; the saved checker reconstructs the
certificate without rerunning that search.

## Review status

The sparse certificate awaits independent review. An asymptotic bound or
an infinite family of longer actual paths remains open.
