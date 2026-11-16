# Larger finite offset windows for private Hilbert choices

15 November 2026. The stride-32, three-choice candidate systems pass
two larger finite tests. Every system in the stated intervals has a
certified modular solution. A separate generator and search-free checker
verify the saved core assignments and extend them by weighted peeling.

These tests concern internal P constraints only. They do not provide
occupied fillers or a complete blackout. Moreover, the subsequent
[unaligned four-label certificate](continuation_unaligned_hilbert_k4_certificate.md)
disproves three-choice solvability at every integer offset and every
Hilbert tile size. The canonical aligned systems remain open.

| Tile side | Integer offsets checked | Constraints | Nonempty weighted cores | Largest core |
|---:|---:|---:|---:|---:|
| 32 | -10,000 through 10,000 | 10,101,475 | 80 | 204 vertices |
| 64 | 1,600 through 1,800 | 886,096 | 27 | 733 vertices |

The model has rows `2i+1`, `2(T+j)+2` at Hilbert cell `(i,j)`,
and private columns `32(3r+xi_r)`, with `xi_r` in `{0,1,2}`.
Every candidate event at ranks `r<s` and integer delta in `[-2,2]`
forbids the stronger modular equality

`xi_s-xi_r = delta (mod 3)`.

The producer generates every event in each stated offset interval.
For each possible horizontal leg, opposite-parity factor pairs of its
half-square give every odd vertical leg. Both signs and both cross-row
roles are included. Weighted peeling removes a vertex with at most two
remaining forbidden-color incidences. The remaining cores are solved
by exact finite-domain search, then their colors are saved.

The independent checker uses primitive Euclid triples and a separate
Hilbert rank decoder. It regenerates the complete event set in each
interval, matches its digest, independently peels the graph, reads only
the core colors, and greedily restores every removed vertex. It directly
checks all original modular constraints. It invokes no search solver.

Files:

- [Producer](probe_private_tiles_offset_window.py)
- [Side-32 certificates](private_tiles_offset_window_side32.json)
- [Side-64 certificates](private_tiles_offset_window_side64.json)
- [Independent checker](check_private_tile_offset_windows.py)
- [Independent verification results](private_tile_offset_windows_independent.json)

The all-offset theorem for sides 4, 8, and 16 remains valid separately.
This note extends only the finite evidence at the listed larger sizes.
