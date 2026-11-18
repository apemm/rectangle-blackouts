"""Reconstruct the filled 127-row extremizer from its phase certificates."""
import argparse
import base64
from functools import cache
import hashlib
import json
from pathlib import Path
import zlib

import check_filled_phase_bitsets as geometric
from core_mixed_witness import from_record
from fiber_translation_search import group_key

HERE = Path(__file__).resolve().parent
HEIGHT = 127
SPAN = 1 + (HEIGHT-1)**2//4
BUFFER = 2*SPAN + 1


def phases():
    out = []
    for name in ("phase_127_filled_windows.json","phase_127_remaining_windows.json"):
        out.extend(json.loads((HERE/name).read_text()))
    return sorted(out,key=lambda rec: anchor(rec))


def anchor(rec):
    return 1 if 1 in rec["levels"] else HEIGHT


def read_phase(rec, old):
    h, base, width = rec["height"],rec["base"],rec["width"]
    low, high = rec["levels"]
    assert h == HEIGHT and anchor(rec) in (low,high)
    assert (low-high)%2 and 2*low-high < 1 and 2*high-low > h
    data = zlib.decompress(base64.b64decode(rec["high_zlib_base64"]))
    assert len(data) == (width+7)//8
    assert hashlib.sha256(data).hexdigest() == rec["high_sha256"]
    assert int.from_bytes(data,"little").bit_length() <= width
    subset = set(rec["columns"]) if "columns" in rec else None
    rows = {x-base:tuple(sorted((a,b))) for x,a,b in old
            if group_key(a,b)[:3] == tuple(rec["group"]) and (subset is None or x in subset)}
    assert len(rows) == rec["doubles"]
    if subset is not None:
        assert {x+base for x in rows} == subset
    assert min(rows) >= BUFFER and width-1-max(rows) >= BUFFER
    for offset in rows:
        assert not data[offset//8] & (1<<(offset%8))
    return width,low,high,data,rows


def pieces(records):
    previous = None
    for rec in records:
        current = anchor(rec)
        if previous is not None:
            yield previous
            if previous != current:
                yield current
        yield rec
        previous = current


def reconstruct(records):
    old = from_record(HEIGHT,96,186)
    labels = set()
    total_width = total_black = 0
    digest = hashlib.sha256()
    for item in pieces(records):
        if isinstance(item,int):
            digest.update(bytes((item,0))*BUFFER)
            total_width += BUFFER
            total_black += BUFFER
            continue
        width,low,high,data,rows = read_phase(item,old)
        encoded = bytearray(2*width)
        for x in range(width):
            encoded[2*x] = high if (data[x//8]>>(x%8)) & 1 else low
        for x,pair in rows.items():
            assert pair not in labels
            labels.add(pair)
            encoded[2*x],encoded[2*x+1] = pair
        digest.update(encoded)
        total_width += width
        total_black += width+len(rows)
    expected = {tuple(sorted((y,z))) for y in range(1,HEIGHT+1,2)
                for z in range(2,HEIGHT+1,2)}
    assert labels == expected
    return total_width,total_black,len(labels),digest.hexdigest()


def board_column(records, ordinal):
    """The finite board starts at column 1. The constant continuation follows."""
    if ordinal < 1:
        raise ValueError("column numbers start at one")
    old = from_record(HEIGHT,96,186)
    for item in pieces(records):
        if isinstance(item,int):
            if ordinal <= BUFFER:
                return (item,)
            ordinal -= BUFFER
            continue
        if ordinal <= item["width"]:
            width,low,high,data,rows = read_phase(item,old)
            x = ordinal-1
            return rows.get(x,(high if (data[x//8]>>(x%8)) & 1 else low,))
        ordinal -= item["width"]
    return (anchor(records[-1]),)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit",action="store_true",
                        help="check every local rectangle and all virtual parity owners")
    parser.add_argument("--column",type=int)
    args = parser.parse_args()
    records = phases()
    counts = reconstruct(records)
    assert counts[:3] == (1507048,1511080,4032)
    print("phases",len(records),"buffer",BUFFER,"width/black/doubles/sha256",*counts,flush=True)
    if args.column is not None:
        print(args.column,board_column(records,args.column))
    if args.audit:
        geometric.templates = cache(geometric.templates)
        for i,rec in enumerate(records,1):
            result = geometric.audit(rec)
            print(i,rec["group"],rec["levels"],*result,flush=True)
            assert result[0] == "pass"


if __name__ == "__main__":
    main()

