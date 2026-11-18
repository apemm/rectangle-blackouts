"""Reconstruct and independently verify the capped-gap height-127 certificate."""
import argparse
from functools import cache
import hashlib
import json

import assemble_compact_127 as board
import check_filled_phase_bitsets as geometric

FILES=("1_122_1024","1_124_256","1_126_256","2_127_512")
SHA256="b1576b8b526428ff89b175143efcd9804c4cb3fffa0daab46f8d8853a6105bfe"


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit",action="store_true",help="replay the four full windows and all seam checks")
    parser.add_argument("--seams",action="store_true",help="replay the seam and right-tail checks")
    parser.add_argument("--sparse-index",action="store_true",help="use indexed black-pair displacement screening in the full scans")
    parser.add_argument("--column",type=int)
    parser.add_argument("--width",type=int)
    args=parser.parse_args()
    recs=[json.loads((board.HERE/f"phase_127_capped_{name}.json").read_text()) for name in FILES]
    raw,old_cuts,old_runs=board.build(recs)
    assert len(raw)//2==536684
    pad=board.R+1
    guard=4001
    trim=pad-guard
    core=bytearray()
    cuts=[]
    runs=[]
    for i,(left,right) in enumerate(zip([0]+old_cuts,old_cuts+[len(raw)//2])):
        l,r=left+(pad if i==0 else trim),right-(pad if i==3 else trim)
        piece=raw[2*l:2*r]
        runs.append((board.constant_run(piece),board.constant_run(piece,True)))
        if i==3:
            core.extend(bytes((1,0))*405)
            cuts.append(len(core)//2)
            core.extend(bytes((127,0))*599)
        elif i:
            cuts.append(len(core)//2)
        core.extend(piece)
    assert runs[1][0]==(1,4001) and runs[1][1]==(1,2298)
    assert runs[2][1]==(1,226) and runs[3][0]==(127,32)
    size=len(core)//2
    digest=hashlib.sha256(core).hexdigest()
    assert core[1] and core[-1] and sum(bool(b) for b in core[1::2])==4032
    assert size==498166 and digest==SHA256
    print("width/black/doubles/sha256",size,size+4032,4032,digest,flush=True)
    print("phase cuts",cuts,flush=True)
    print("prefix and suffix runs",runs,flush=True)
    target=size if args.width is None else args.width
    if target<size:parser.error("width is below the certificate")
    if args.column is not None:
        if not 1<=args.column<=target:parser.error("column outside requested grid")
        x=args.column-1
        joint=cuts[0]
        added=target-size
        if joint<=x<joint+added:
            entry=(1,)
        else:
            i=x if x<joint else x-added
            entry=tuple(y for y in core[2*i:2*i+2] if y)
        print(args.column,entry)
    if args.audit or args.seams:
        geometric.templates=cache(geometric.templates)
        if args.audit:
            for rec in recs:
                result=geometric.audit(rec,sparse_index=args.sparse_index)
                print("window",rec["levels"],*result,flush=True)
                assert result[0]=="pass"
        extended=core+raw[-2*pad:]+bytes((127,0))*board.R
        for cut in cuts+[size,size+pad]:
            result=board.seam_audit(extended,cut)
            print("cut",cut,*result,flush=True)
            assert result[0]=="pass"


if __name__=="__main__":
    main()
