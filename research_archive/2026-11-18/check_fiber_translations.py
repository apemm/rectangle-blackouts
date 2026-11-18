"""Reconstruct the certificate from row pairs and verify with the archived Python checker."""
import hashlib
import json
import sys

import numpy as np

import check_label_triangles
from check_ternary_placement import columns
from ternary_graph import HERE


def audit(h, stride, seed):
    rec = json.loads((HERE/f'fiber_search_{h}_{stride}_{seed}.json').read_text())
    moves = {tuple(row[:4]): row[4] for row in rec['translations']}
    assert len(moves) == len(rec['translations']) and all(0 < t <= h for t in moves.values())
    runs = {}
    for x, odd, even in columns(h, stride):
        k = 1
        gap = abs(odd-even)
        while gap % 3 == 0:
            k *= 3
            gap //= 3
        w = odd % k
        u, v = (odd-w)//k % 6, (even-w)//k % 6
        key = (k,u,v) if (v-u)%6 == 1 else (k,v,u)
        runs.setdefault(key, []).append((x,w,odd,even))
    board, current = [], 0
    for key, cells in sorted(runs.items()):
        k = key[0]
        original_base = min(x for x,_,_,_ in cells)//(4*k)*4*k
        base = (current+4*k-1)//(4*k)*(4*k)
        block = [(base+x-original_base+4*k*moves.get((*key,w),0),a,b)
                 for x,w,a,b in cells]
        board.extend(block)
        current = max(x for x,_,_ in block)+h*h//(2*k)+1
    board.sort()
    assert len(board) == h*h//4 == len({col[0] for col in board})
    digest = hashlib.sha256(np.asarray(board,dtype='<i8').tobytes()).hexdigest()
    assert digest == rec['assignment_sha256']
    original = check_label_triangles.columns
    try:
        check_label_triangles.columns = lambda *args: board
        status, corners, _ = check_label_triangles.obstruction(h)
    finally:
        check_label_triangles.columns = original
    assert status.startswith('no obstruction') and corners == 0
    print(h, len(board), len(moves), rec['width'], digest, 'PASS', flush=True)


if __name__ == '__main__':
    for value in sys.argv[1:]:
        audit(int(value),96,186)
