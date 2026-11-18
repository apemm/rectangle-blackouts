"""Replay or search shorter singleton gaps on the four filled height-127 windows."""
import argparse
from functools import cache
import hashlib
import json
from pathlib import Path

import assemble_compact_127 as board
import check_filled_phase_bitsets as geometric


def cut(piece, left_double, right_double, target):
    keep_left=(target-1)//2
    keep_right=target-1-keep_left
    left=left_double+keep_left+1
    right=right_double-keep_right
    assert left<right and not any(piece[2*left+1:2*right:2])
    return piece[:2*left]+piece[2*right:],left


def run(plan=None, search=False):
    old=board.from_record(127,96,186)
    data=bytearray()
    plan_out=[]
    borders=[]
    changes=[]
    geometric.templates=cache(geometric.templates)
    for phase,rec in enumerate(board.windows()):
        piece,_=board.word(rec,old)
        piece,_=board.shorten(piece)
        sites=[x for x,b in enumerate(piece[1::2]) if b]
        working=piece
        offset=0
        entries={}
        if plan is not None:
            entries=dict(plan["phases"][phase])
        result=[]
        for index,(c,d) in enumerate(zip(sites,sites[1:])):
            gap=d-c
            if search:
                if gap<1024:continue
                candidates=[t for t in (256,1024,2048,4096,6144) if t<gap]
            elif index in entries:
                candidates=[entries[index]]
            else:
                continue
            for target in candidates:
                test,pos=cut(working,c-offset,d-offset,target)
                evidence=board.seam_audit(test,pos) if search else None
                if evidence is not None and evidence[0]!="pass":continue
                working=test
                result.append([index,target])
                changes.append(len(data)//2+pos)
                offset+=gap-target
                if search:print("accepted",phase,index,gap,target,offset,flush=True)
                break
        if data:borders.append(len(data)//2)
        data.extend(working)
        plan_out.append(result)
    core=data[2*(board.R+1):-2*(board.R+1)]
    size=len(core)//2
    checksum=hashlib.sha256(core).hexdigest()
    assert sum(bool(x) for x in core[1::2])==4032
    assert core[1] and core[-1]
    doc={"height":127,"width":size,"doubles":4032,"sha256":checksum,"phases":plan_out}
    if plan is not None:assert doc==plan
    return doc,data,borders,changes


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    arg=parser.add_mutually_exclusive_group(required=True)
    arg.add_argument("--search",type=Path,help="write a new plan after checking every accepted edit")
    arg.add_argument("--replay",type=Path,help="rebuild the supplied cut plan")
    parser.add_argument("--audit",action="store_true",help="scan all final cut neighborhoods, phase borders and right tail")
    parser.add_argument("--column",type=int)
    parser.add_argument("--width",type=int)
    args=parser.parse_args()
    if args.search:
        if args.search.exists():parser.error("the search output already exists")
        doc,raw,borders,changes=run(search=True)
        with args.search.open("x") as out:json.dump(doc,out,indent=2)
    else:
        doc,raw,borders,changes=run(json.loads(args.replay.read_text()))
    core=raw[2*(board.R+1):-2*(board.R+1)]
    n=doc["width"]
    print("width/black/doubles/sha256",n,n+4032,4032,doc["sha256"],flush=True)
    if args.width is not None and args.width<n:parser.error("requested width is below certificate")
    if args.column is not None:
        width=n if args.width is None else args.width
        if not 1<=args.column<=width:parser.error("column outside board")
        z=args.column-1
        extra=width-n
        start=borders[0]-(board.R+1)
        if start<=z<start+extra:
            ys=(1,)
        else:
            i=z if z<start else z-extra
            ys=tuple(y for y in core[2*i:2*i+2] if y)
        print(args.column,ys)
    if args.audit:
        geometric.templates=cache(geometric.templates)
        w=len(raw)//2
        raw.extend(bytes((127,0))*board.R)
        for pos in changes+borders+[w]:
            result=board.seam_audit(raw,pos)
            print("cut",pos,*result,flush=True)
            assert result[0]=="pass"


if __name__ == "__main__":
    main()
