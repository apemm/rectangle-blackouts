# Three integer choices on three labels

15 November 2026. This is an elementary restriction on small obstructions
to the integer P system. The certified system, which forbids differences
modulo three, is stronger and does not satisfy this lemma.

The proof below has been checked independently. The supplementary
exhaustive check also passes all 4096 systems.

**Lemma.** Let three variables take values in \(\{0,1,2\}\). For each
pair, forbid at most two of the integer differences
\(\{-2,-1,0,1,2\}\). Then the resulting system is satisfiable.

Missing pair constraints are allowed. Orient the three pairs arbitrarily
when specifying their forbidden differences. Reversing an orientation
replaces its forbidden set by its negative and does not change the problem.

Suppose first that one pair, say \(a,b\), permits difference zero. Assign
\(x_a=x_b=u\) and orient the other two pairs toward \(c\). If they both
also permit zero, assigning all variables zero works. Otherwise at least
one of their forbidden sets contains zero. Their union therefore contains
at most three of the four nonzero differences. Choose a nonzero
\(\delta\) outside that union, and choose \(u\) so that
\(u,u+\delta\in\{0,1,2\}\). Then \(x_c=u+\delta\) solves the system.

It remains that every pair forbids zero. Each pair has at most one
additional forbidden difference. Consider the six assignments that are
permutations of \((0,1,2)\). A forbidden difference \(1\) or \(-1\)
eliminates two such permutations. A forbidden difference \(2\) or
\(-2\) eliminates one. Thus, unless all three additional differences
exist and are units, at most five permutations are excluded.

In the remaining case, orient each pair \(u\to v\) so that its additional
exclusion is \(x_v-x_u=1\). This is a tournament on three vertices and
has a directed Hamiltonian path \(u\to v\to w\). Assign
\[
 x_u=2,\qquad x_v=1,\qquad x_w=0.
\]
The two path edges have difference \(-1\), and the third edge has
absolute difference two. None of the exclusions applies. This proves
the lemma.

## Consequence for P obstructions

An integer three-choice P system on three labels can be unsatisfiable
only if some pair forbids at least three distinct integer differences.
There are only two cross-parity roles for a pair of labels. Hence one
role must provide at least two distinct slot values \(q\) for the same
odd vertical gap \(Y\), with
\[
 |q-q'|\le4.
\]
Thus every three-label integer obstruction contains a common-leg
exception from the fixed-gap Pell families in Lemma Q of
`hilbert_energy_bound_false.md` or Theorem 3(c) of
`p_two_block_selfsimilar.md`.

Together with [the three-leg bound](continuation_three_leg_spacing.md),
the possibilities are narrower: no two-label integer obstruction exists
at any height, and a three-label obstruction must meet one of these
common-leg families. This is not a classification of such obstructions
and does not exclude larger ones.

The short checker
[check_three_label_integer_lemma.py](check_three_label_integer_lemma.py)
also checks all \(16^3=4096\) triples of forbidden sets of size at most
two. This finite check is supplementary to the proof.
