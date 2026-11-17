# Quadratic-width round, 15 November 2026

Problem 001. This folder holds my notes, scripts and certificates from one
round of work toward `m_h = O(h^2)`. I did not prove that bound. Nothing
here is in the paper.

## Where to start

- [STOPPING_POINT.md](STOPPING_POINT.md): what I proved, what I checked by
  computation, and what still blocks a quadratic-width board.
- [NONSTOP_PROGRESS.md](NONSTOP_PROGRESS.md): the longer record, with a link
  to every note.
- [continuation_p_event_arithmetic_and_counting_load.md](continuation_p_event_arithmetic_and_counting_load.md):
  a divisibility lemma for the P events and a counting estimate for fixed
  palettes.
- [continuation_p_degree_growth_law.md](continuation_p_degree_growth_law.md):
  the measured growth of the P degree, about `(21.5/S) log2(side)`.
- continuation_diagonal_t6_alignment_independent_audit.md:
  my second check of the valuation-six diagonal certificate.

In these notes, "independent review" and "independent check" mean that I
checked a statement a second time, by a separate derivation or a separate
program. They do not mean refereeing.

## My assessment after this round

I do not think the private-choice route reaches `O(h^2)` with a fixed
palette.

- Each label meets a roughly constant number of P events per scale, and
  there are about `log h` scales. In the counting estimate, a fixed palette
  runs out of room near side `2^16`, and a larger palette does not help.
  This is a heuristic, not a theorem.
- The full odd P graph has no bounded colouring, an unaligned Hilbert K4
  defeats three choices, and the energy bound and the local limit are both
  false.
- A proof with a fixed palette would have to use correlation between
  events. The excursion decomposition is the only structure of that kind I
  have, and its constraints are new at every scale.
- P is one of several blockers. The caps, the mixed and six-cell families,
  and the relocation audit remain even if P is solved.

None of this shows that `m_h = O(h^2)` is false. I have no lower bound that
rules it out.

Directions that still look open to me:

1. A stride of order `log h`. The mean P degree scales like
   `(1/S) log h` in the stride `S`, so the degree would stay bounded and a
   fixed palette might then work. The width would be `h^2 log h`. I have
   not checked the other families or the fillers at a growing stride.
2. A lower bound showing that `m_h / h^2` is unbounded.

The best bound I have proved is `m_h <= C h^2 (log h)^(1.3108172 + eps)`;
see `../../2026-11-13/consolidated_board_menu.md`.

## The side-2048 solver test

I generated the aligned system of side 2048 at offset -4096 (10,187,303
events, 2.43 per label) and tried to solve its modular three-core. Glucose
and CaDiCaL both ran out of memory, at 4 GB and at 9 GB. The test is
undecided. Details are in Section 7 of the counting note.

## Files not stored here

Three data files are larger than 20 MB and are left out. Each can be
regenerated.

| File | Size | How to regenerate |
|---|---:|---|
| `aligned_private_side1024_minus2048_events.npy` | 26 MB | `python probe_hilbert_rank_difference_automaton.py --side 1024 --offset -2048 --array --events aligned_private_side1024_minus2048_events.npy` |
| `aligned_private_side2048_minus4096_events.npy` | 122 MB | the same command with `--side 2048 --offset -4096` (about 70 seconds, 2 GB) |
| `all_offset_private_tiles_side16.json` | 44 MB | `python check_all_offset_private_tiles.py --side 16 --out all_offset_private_tiles_side16.json` |

The hashes of the two event files are in the small JSON files with the same
stems. The solver scripts `probe_aligned_private_sat.py` and
`probe_aligned_private_sat_cadical.py` need the PySAT package in a folder
`local_sat_dependencies` beside them. That folder is not stored here.
