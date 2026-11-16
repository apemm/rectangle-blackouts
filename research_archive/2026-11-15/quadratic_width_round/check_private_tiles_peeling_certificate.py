"""Check every side-16 offset using greedy peeling and six tiny cores.

The normal verification does not load the large assignment table or run
a constraint solver. --extract is only a one-time certificate extractor.
"""
from collections import defaultdict, deque
from hashlib import sha256
from pathlib import Path
import argparse
import json
import time
from check_all_offset_private_tiles_independent import independent_systems


def extract(folder):
    cores = json.loads((folder/'private_tile_gain_cores_side16.json').read_text())['small_final_cores']
    original = json.loads((folder/'all_offset_private_tiles_side16.json').read_text())['certificates']
    result = {}
    for core in cores:
        t = core['offset']
        assignment = original.get(str(t), {'assignment':'0'*256})['assignment']
        colors = ''.join(str(assignment[r]) for r in core['vertices'])
        if t in (-1461,-1740):
            colors = '0'*len(core['vertices'])
        if t == 3201:
            colors = '000111'
        result[str(t)] = {'vertices':core['vertices'], 'colors':colors}
    (folder/'private_tiles_peeling_certificate.json').write_text(json.dumps(result,indent=2)+'\n')


def check(folder):
    started = time.monotonic()
    certificate = json.loads((folder/'private_tiles_peeling_certificate.json').read_text())
    systems, _, _ = independent_systems(16,32,3)
    digest = sha256()
    seen_cores = set()
    constraint_count = 0
    for t, events in sorted(systems.items()):
        digest.update(json.dumps([t,sorted(events)],separators=(',',':')).encode())
        adjacency = [defaultdict(set) for _ in range(256)]
        for r,s,delta in events:
            adjacency[r][s].add(delta%3)
            adjacency[s][r].add((-delta)%3)
        degree = [sum(map(len,row.values())) for row in adjacency]
        queue = deque(r for r in range(256) if degree[r]<=2)
        removed = [False]*256
        order = []
        while queue:
            r = queue.popleft()
            if removed[r]:
                continue
            assert degree[r]<=2
            removed[r]=True
            order.append(r)
            for s,gains in adjacency[r].items():
                if not removed[s]:
                    degree[s]-=len(gains)
                    if degree[s]<=2:
                        queue.append(s)
        core = [r for r in range(256) if not removed[r]]
        colors = [None]*256
        if core:
            entry = certificate[str(t)]
            assert entry['vertices']==core
            assert len(entry['colors'])==len(core)
            for r,c in zip(core,entry['colors']):
                colors[r]=int(c)
            seen_cores.add(str(t))
        else:
            assert str(t) not in certificate
        for r in reversed(order):
            forbidden = {(colors[s]-gain)%3
                         for s,gains in adjacency[r].items() if colors[s] is not None
                         for gain in gains}
            assert len(forbidden)<=2
            colors[r]=min(set(range(3))-forbidden)
        assert all(c in (0,1,2) for c in colors)
        for r,s,delta in events:
            assert (colors[s]-colors[r]-delta)%3
            constraint_count+=1
    assert seen_cores==set(certificate)
    assert digest.hexdigest()=='ea53acccd3a47d41dbad63f8f1daf76b515404b1d2eee651aa1a51097d377566'
    result={'status':'PASS','offsets':len(systems),'explicit_cores':len(seen_cores),
            'explicit_core_colors':sum(len(e['colors']) for e in certificate.values()),
            'checked_constraints':constraint_count,'constraint_sha256':digest.hexdigest(),
            'seconds':round(time.monotonic()-started,3)}
    (folder/'check_private_tiles_peeling_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--extract',action='store_true')
    args=p.parse_args()
    folder=Path(__file__).resolve().parent
    if args.extract:
        extract(folder)
    check(folder)


if __name__=='__main__':
    main()
