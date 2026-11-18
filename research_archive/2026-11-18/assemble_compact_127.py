"""Reconstruct the compressed height-127 board and audit its seams."""
import argparse
import base64
from functools import cache
import hashlib
import json
from pathlib import Path
import zlib

import check_filled_phase_bitsets as geometric
from core_mixed_witness import from_record

HERE = Path(__file__).resolve().parent
H = 127
R = 2*(1+(H-1)**2//4)
PALETTES = ((1,122),(1,124),(1,126),(2,127))


def windows():
    return [json.loads((HERE/f"phase_127_merged_{a}_{b}.json").read_text()) for a,b in PALETTES]


def word(rec, old):
    width = rec["width"]
    lo,hi = rec["levels"]
    bits = zlib.decompress(base64.b64decode(rec["high_zlib_base64"]))
    assert len(bits) == (width+7)//8
    assert hashlib.sha256(bits).hexdigest() == rec["high_sha256"]
    doubles = geometric.assigned_doubles(rec,old)
    assert len(doubles) == rec["doubles"]
    assert min(x for x,_,_ in doubles) >= R+1
    assert max(x for x,_,_ in doubles) <= width-R-2
    data = bytearray(2*width)
    for x in range(width):
        data[2*x] = hi if (bits[x//8]>>(x%8)) & 1 else lo
    for x,a,b in doubles:
        assert not (bits[x//8]>>(x%8)) & 1
        data[2*x],data[2*x+1] = sorted((a,b))
    return data,{tuple(sorted((a,b))) for _,a,b in doubles}


def constant_run(data, reverse=False):
    size = len(data)//2
    start,step = (size-1,-1) if reverse else (0,1)
    y = data[2*start]
    for n in range(size):
        x = start+n*step
        if data[2*x] != y or data[2*x+1]:
            return y,n
    return y,size


def shorten(piece):
    # Each cut leaves G singleton columns on both sides in its own palette.
    guard = R//2+H//2
    locations = [x for x,b in enumerate(piece[1::2]) if b]
    drops = [(a+guard+1,b-guard) for a,b in zip(locations,locations[1:])
             if b-a > 2*guard+1]
    result = bytearray()
    last = 0
    joints = []
    for first,after in drops:
        assert not any(piece[2*first+1:2*after:2])
        result.extend(piece[2*last:2*first])
        joints.append(len(result)//2)
        last = after
    result.extend(piece[2*last:])
    return result,joints


def build(records, shorten_gaps=False):
    data = bytearray()
    records_seen = set()
    cuts,runs = [],[]
    shortcuts = []
    old = from_record(H,96,186)
    for rec,palette in zip(records,PALETTES,strict=True):
        assert tuple(rec["levels"]) == palette
        piece,pairs = word(rec,old)
        if shorten_gaps:
            piece,internal = shorten(piece)
            shortcuts.extend(len(data)//2+x for x in internal)
        assert pairs.isdisjoint(records_seen)
        records_seen.update(pairs)
        if data:
            cuts.append(len(data)//2)
        runs.append((constant_run(piece),constant_run(piece,True)))
        data.extend(piece)
    expected = {tuple(sorted((a,b))) for a in range(1,H+1,2) for b in range(2,H+1,2)}
    assert records_seen == expected
    # The first two cuts have common-anchor locality 5*2*(h-1).
    assert runs[0][1][0] == runs[1][1][0] == 1
    assert min(runs[0][1][1],runs[1][1][1]) > 10*(H-1)
    # The last cut has the ordered parity-flip locality 5*(h-1).
    assert runs[2][1][0] == 1 and runs[3][0][0] == H
    assert min(runs[2][1][1],runs[3][0][1]) > 5*(H-1)
    return (data,cuts,runs,shortcuts) if shorten_gaps else (data,cuts,runs)


def seam_audit(data, cut):
    left,right = max(0,cut-R),min(len(data)//2,cut+R)
    width = right-left
    owners = {}
    row_bytes = [bytearray((width+7)//8) for _ in range(H+1)]
    for x in range(width):
        offset = 2*(x+left)
        a,b = data[offset:offset+2]
        row_bytes[a][x//8] |= 1 << (x%8)
        if b:
            assert (a,b) not in owners
            owners[(a,b)] = x
            row_bytes[b][x//8] |= 1 << (x%8)
    rows = [int.from_bytes(row,"little") for row in row_bytes]
    return geometric.audit_rows(rows,owners,width,left)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit",action="store_true",help="replay all four full-window checks and all seam checks")
    parser.add_argument("--seams",action="store_true",help="replay just the seam and tail checks")
    parser.add_argument("--shortcuts",action="store_true",help="independently audit all sixteen internal cuts")
    parser.add_argument("--column",type=int,help="print one column of the trimmed board")
    parser.add_argument("--width",type=int,help="extend the trimmed board at its first common-anchor join")
    args = parser.parse_args()
    records = windows()
    data,cuts,runs,shortcuts = build(records,shorten_gaps=True)
    width = len(data)//2
    black = width+sum(bool(v) for v in data[1::2])
    digest = hashlib.sha256(data).hexdigest()
    print("width/black/doubles/sha256",width,black,black-width,digest,flush=True)
    print("prefix and suffix runs",runs,flush=True)
    assert (width,black,black-width) == (742624,746656,4032)
    assert len(shortcuts) == 16
    trim = R+1
    assert not any(data[1:2*trim:2]) and not any(data[-2*trim+1::2])
    core = data[2*trim:-2*trim]
    assert core[1] and core[-1]
    size = len(core)//2
    digest = hashlib.sha256(core).hexdigest()
    assert size == 726742
    assert digest == "33942fef1691ba1ef46668a4573934827a7a2c78362558c53304d156dbd32761"
    print("trimmed width/black/doubles/sha256",size,size+4032,4032,digest,flush=True)
    target = size if args.width is None else args.width
    if target < size:
        parser.error(f"the certificate begins at width {size}")
    if args.column is not None:
        if not 1 <= args.column <= target:
            parser.error("column outside requested board")
        x = args.column-1
        first = cuts[0]-trim
        added = target-size
        if first <= x < first+added:
            entry = (1,)
        else:
            j = x if x < first else x-added
            entry = tuple(y for y in core[2*j:2*j+2] if y)
        print(args.column,entry)
    if args.audit or args.seams or args.shortcuts:
        geometric.templates = cache(geometric.templates)
        if args.audit:
            for rec in records:
                result = geometric.audit(rec)
                print("window",rec["levels"],*result,flush=True)
                assert result[0] == "pass"
        extended = data+bytes((H,0))*R
        extra = shortcuts if args.audit or args.shortcuts else []
        borders = cuts+[width] if args.audit or args.seams else []
        for cut in borders+extra:
            result = seam_audit(extended,cut)
            print("cut",cut,*result,flush=True)
            assert result[0] == "pass"


if __name__ == "__main__":
    main()

