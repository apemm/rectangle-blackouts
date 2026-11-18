# A local SAT obstruction to saturation in thirteen rows

A saturated blackout has \(m=q_h=\lfloor h^2/4\rfloor\) columns and size \(2q_h\). The equality theorem assigns one distinct edge of a complete balanced bipartite graph on the rows to each column. In particular, every column is a double.

At \(h=13\), the twelve columns 16 through 27 of a proposed \(13\times42\) saturated board already give an unsatisfiable formula. The solver leaves the balanced partition free. This gives the finite lower bound \(m_{13}\ge43\). The first computation used 781 variables and 77,464 clauses. CaDiCaL 1.9.5 in PySAT returned UNSAT in 548 seconds. Its DIMACS digest is 13f5b4e9bb4ba1386dc24826e215e414b40186c67a552591d2ec3c133647dbad. This free-partition computation has a replayable generator. The smaller LRAT proofs below cover the parity partition.

## The necessary conditions

Write \(P_A\) for the black indicator of a tested cell and \(S_r\) for the side of the row partition. The two black points of each tested column lie on opposite sides, and the columns have distinct row pairs. The three geometric tests use the full physical grid even when some shared corners lie outside the tested slice.

1. **Tilted triples.** A tilted rectangle in an equality board has no four black corners. If three are black, its fourth corner cannot lie in a double column. In a saturated board this excludes every such triple. For tested points \(A,B,C\), take \(A\) as the pivot and require both coordinates of each leg to be nonzero. When \((B-A)\cdot(C-A)=0\) and \(B+C-A\) lies in the grid, include \(\neg P_A\vee\neg P_B\vee\neg P_C\).
2. **Two shared corners.** If distinct rectangles have the same two shared corners and their four other corners lie in the slice, those four cannot all be black. In the first generator the mixed cases use a black side \(A,B\) and a black diagonal \(C,D\). Their lengths agree, \(n=(C+D-A-B)/2\) is integral and perpendicular to \(B-A\), and \(A+n,B+n\) are the shared corners. Each actual pair gives a four-cell clause. The independent generator enumerates rectangle pairs directly.
3. **Vertical diagonals and the row partition.** Suppose two tested cells \(C,D\) in different columns form one diagonal of a rectangle whose other diagonal \(p,q\) is vertical. All four corners must lie in the grid. If \(C,D\) are black, the rows of \(p,q\) must lie in the same part. Otherwise the row pair \(\{p_y,q_y\}\) is a required double somewhere in the saturated board. If its owner stands in the column of \(p,q\), the tilted rectangle is fully black. At any other owner column, the axis rectangle using the owner and \(p,q\) has the same presentation as the tilted rectangle. This proves the two conditional clauses linking \(P_C,P_D\) and \(S_{p_y},S_{q_y}\).

The exclusion of a fully black tilted rectangle at these grid dimensions is proved in [the window note](windows.md). Each SAT exclusion uses a necessary condition. Unsatisfiability therefore excludes the proposed equality board.

## Replay and independently checked parity cases

From the root of the rectangle-blackouts repository, run

~~~text
py -B research_archive/2026-11-18/saturated_slice.py 13 12
~~~

The [first generator](saturated_slice.py) constructs perpendicular legs directly and uses the earlier window generator for the partition clauses. [The independent generator](saturated_slice_diagonals.py) pairs full-grid diagonals by midpoint and squared length. For each common pair of corners it compares all candidate complements. It encodes a specified balanced partition with exactly one point from each part per column. With the default odd-row partition it gave the following formulas.

| Height | Tested width | Variables | Clauses | SHA-256 of the DIMACS formula |
|---:|---:|---:|---:|---|
| 13 | 12 | 156 | 62,616 | 15a3ea522f6f51e839e72984fc16ab3b8798d204fce7cfe67adc1582b530d917 |
| 14 | 12 | 168 | 75,074 | 95b484b4f84abef631f335eebf8a91c08e4abfdb65688da7b0c6a30463ca55ce |
| 15 | 13 | 195 | 108,197 | 8f3f89c227ae16989b5cf3752dfcee0d0462b38c52b119cd8d3895ca8f268318 |

The stored [height-13 proof](saturation_parity_h13_k12.lrat.gz), [height-14 proof](saturation_parity_h14_k12.lrat.gz) and [height-15 proof](saturation_parity_h15_k13.lrat.gz) are gzip-compressed text LRAT. For a fixed row partition, pass its zero-based bit mask with --mask. To write a DIMACS file, add --dimacs followed by a new filename to the independent generator. CaDiCaL 2.1.2 produced these proofs. For each one the [Lean checker](../../jis/unsat/lean/Main.lean) accepted the proof and wrote back a byte-identical DIMACS formula.

These three proof files exclude saturation for the parity partition. The free-partition result excludes saturation at height 13. They do not settle the conjectured window width at height 13. Mixed quadruples and required owners impose additional conditions on an equality board.

## Runs of twenty doubles

The same argument excludes twenty consecutive doubles in every height-13 equality board, even when the whole board is wider. Test the twelve middle columns of the twenty-column run and allow only common corners and tilted completions inside the run. The white corner of every tested tilted triple would be in a double. The owner of a required row pair can lie anywhere on the board. These facts justify all three necessary conditions at the new boundaries.

The shorter formula keeps the 34,426 mixed supports and the 438 conditional rival pairs. It drops 34 of the 18,638 tilted triples. Its 77,430 clauses have SHA-256 fc5883e86e48f72856424ec7704d3480c6abdf3983af39619eb5f13c763d9c86. The free-partition solve returned UNSAT in 399 seconds. A second run tested the 34 omitted clauses one at a time by imposing their three black corners on the shorter formula. Every one of these assignments was unsatisfiable.

There are 42 doubles. Since a run contains at most 19, there must be at least three runs and two singleton separators. Thus
\[
 m_{13}\ge 44.
\]
The command to replay the shorter formula is

~~~text
py -B research_archive/2026-11-18/saturated_slice.py 13 12 --run-width 20
~~~

For the original 42-column formula, a separate replay fixed one balanced partition at a time. Row reflection gives 868 representatives of the 1,716 choices of the seven-row part. All 868 cases returned UNSAT. This replay used the same first geometric generator.


## Proof checks and the stronger fourteen-column test

For the twenty-column result, fix the three row-part indicators of rows 1, 2, and 3 in all eight possible ways. Each branch of the same formula has a text LRAT proof from CaDiCaL 2.1.2. The standalone lrat-check verifier accepted every branch. The [certificate record](saturation_h13_run20_parts.json) gives the individual formula and proof digests. The proofs occupied 15,921,092,009 bytes in total and were checked in temporary files. [The replay script](certify_saturation_parts.py) takes the solver and checker paths as arguments. Running it with height 13, tested width 12, run width 20, and parts 0 through 7 covers the free partition.

A separate run takes all fourteen columns of a fourteen-column run as its tested slice. It has 895 variables, 105,612 clauses, and DIMACS digest 33dec2ca75045ed83515c68632efc9c2a754f1fe7140b9c55f6df309306f5099. The free-partition solve returned UNSAT in 1,052 seconds. Thus a run has at most thirteen doubles, 42 doubles require four runs, and
\[
 m_{13}\ge45.
\]
The shorter proof produces the stronger inequality because more separators are required. The independently checked LRAT branches above concern \(m_{13}\ge44\). The fourteen-column result can be replayed with

~~~text
py -B research_archive/2026-11-18/saturated_slice.py 13 14 --run-width 14
~~~

Using only the central twelve columns of a fourteen-column run leaves satisfiable local configurations. Including all fourteen columns matters for this check.


## Height fourteen

At height 14 a run of 24 double columns is impossible on an equality board. Test the 13 central columns, starting at zero-based index 5 of the run. The free balanced-partition formula has 918 variables and 112,446 clauses, including 27,056 tilted triples, 51,054 mixed supports and 582 candidate rival pairs. Its DIMACS SHA-256 is 81eb1c5307d5dba410f4dadb75ccec72d513a2852f468f8090826ee0925515e6. The free solve returned UNSAT in 5,457 seconds.

A second run generated rectangles directly by pairing equal-length diagonals at a common midpoint in the entire \(14\times24\) grid. In each tested column it imposed two points in opposite parts with a sequential cardinality constraint. It tested all balanced row partitions, identifying only vertical reflections and exchanges of the two parts. All 890 representatives returned UNSAT. The [six-shard record](saturation_h14_run24_replay.json) identifies the enumerated masks by digest. These are two SAT encodings, without an independently checked LRAT trace at height 14. Their commands are

~~~text
py -B research_archive/2026-11-18/saturated_slice.py 14 13 --run-width 24
py -B research_archive/2026-11-18/replay_saturated_run_diagonals.py 14 13 24
~~~

Every height-14 equality board has 49 doubles. At most 23 of them lie in each run, so at least two singleton columns separate at least three runs. Hence \(m_{14}\ge51\).
