"""Dump the weighted M-core constraints of G_B^o to core_B_M.json (for runs that must stay under 60 s).
Usage: py -B dump_core.py B S M orient"""
import sys, json, os
from core_cert import build, core
B, S, M, orient = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
trip = build(B, S, M, orient)
K, comps = core(trip, M)
cons = [[r, u, dl, q] for (r, u, dl), q in trip.items() if r in K and u in K]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"core_{B}_{M}_{orient}.json")
json.dump(cons, open(out, "w"))
print("wrote", out, len(cons), "constraints", len(K), "labels")
