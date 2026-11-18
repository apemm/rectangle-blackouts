"""Recompute a phase filling after capping every consecutive true-column gap."""
import argparse
import json
from pathlib import Path

import assemble_compact_127 as board
import search_compact_127 as compact

HERE=Path(__file__).resolve().parent


def search(rec, cap, destination):
    low,high=rec["levels"]
    source=f"phase_127_merged_{low}_{high}.json"
    start=sorted(board.geometric.assigned_doubles(rec,compact.old))
    first=start[0][0]
    prev=first
    loss=0
    rows={}
    for x,y,z in start:
        loss+=max(0,x-prev-cap)
        rows[x-first-loss]=y,z
        prev=x
    result=compact.search((low,high),cap,source=(rows,[]))
    if result is None:return False
    del result["groups"]
    result.update(source_window=source,max_true_gap=cap)
    with destination.open("x") as f:json.dump(result,f,indent=2)
    return True


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase",type=int,choices=range(4))
    parser.add_argument("caps",type=int,nargs="+")
    args=parser.parse_args()
    rec=board.windows()[args.phase]
    low,high=rec["levels"]
    for cap in args.caps:
        dest=HERE/f"phase_127_capped_{low}_{high}_{cap}.json"
        if dest.exists():raise FileExistsError(dest)
        if search(rec,cap,dest):
            print("certified candidate",dest.name,flush=True)
            return
    raise SystemExit(1)


if __name__=="__main__":
    main()
