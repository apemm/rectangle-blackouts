"""Bounded exact-history probes for correlated monotone P queues."""
from __future__ import annotations

import argparse
import json
import math
import random
import time
from pathlib import Path


def blockers(h):
    a, k = (h + 1) // 2, h // 2
    result = [[0] * k for _ in range(a)]
    for i in range(a):
        for j in range(k):
            bits = 0
            for ip in range(a):
                if ip == i:
                    continue
                norm = 16 * (i - ip) ** 2 + (2 * (j - ip) + 1) ** 2
                hyp = math.isqrt(norm)
                if hyp < h and hyp * hyp == norm:
                    assert hyp % 2
                    bits |= 1 << ip
            result[i][j] = bits
    return result


def legal(token, i, b):
    occupied, forbidden, history = token
    return not ((forbidden >> i) & 1) and not (b & occupied)


def served(token, i, j, b):
    occupied, forbidden, history = token
    return occupied | (1 << i), forbidden | b, history + [(i, j)]


def run(h, capacity, seed, b, policy, start=None, stop_after=None):
    rng = random.Random(seed)
    a, k = (h + 1) // 2, h // 2
    queues = ([[ (0, 0, []) for _ in range(capacity)] for _ in range(k)]
              if start is None else start["queues"])
    finished = [] if start is None else start["finished"].copy()
    first_column = 0 if start is None else start["next_column"]
    forced_rows = 0
    for i in range(first_column, a):
        options = [
            [t for t in range(capacity) if legal(q[t], i, b[i][j])]
            for j, q in enumerate(queues)
        ]
        if any(not op for op in options):
            return dict(success=False, column=i, reason="no_legal_token",
                        row=next(j for j, op in enumerate(options) if not op))
        forced_rows += sum(len(op) == 1 for op in options)
        updated = [[served(q[t], i, j, b[i][j]) for t in options[j]]
                   for j, q in enumerate(queues)]

        # A choice at row j and its predecessor at j-1 determine the entire
        # next queue j. This DP preserves one-step viability in every row.
        scores, predecessors = [], []
        for j, op in enumerate(options):
            row_scores, row_prev = [], []
            for t in op:
                history = queues[j][t][2]
                age = i - history[-1][0] if history else i + 1
                if policy == "oldest":
                    weight = age + rng.random()
                elif policy == "youngest":
                    weight = -age + rng.random()
                elif policy == "reserve":
                    weight = 0.01 * age + rng.random()
                else:
                    weight = rng.random()
                if j == 0:
                    row_scores.append(weight)
                    row_prev.append(-1)
                    continue
                left_options = []
                remaining_count = (capacity if i + 1 == a else
                    sum(u != t and legal(queues[j][u], i + 1, b[i + 1][j])
                        for u in range(capacity)))
                for u, old_score in enumerate(scores[j - 1]):
                    if old_score is None:
                        continue
                    incoming_good = (i + 1 == a or
                        legal(updated[j - 1][u], i + 1, b[i + 1][j]))
                    if remaining_count or incoming_good:
                        reserve = remaining_count + incoming_good
                        reward = (10 * math.log(reserve) if policy == "reserve"
                                  else 0)
                        left_options.append((old_score + reward, u))
                if left_options:
                    old_score, u = max(left_options)
                    row_scores.append(old_score + weight)
                    row_prev.append(u)
                else:
                    row_scores.append(None)
                    row_prev.append(-1)
            scores.append(row_scores)
            predecessors.append(row_prev)
        candidates = [(score, t) for t, score in enumerate(scores[-1])
                      if score is not None]
        if not candidates:
            dead = next(j for j, row in enumerate(scores)
                        if all(score is None for score in row))
            return dict(success=False, column=i, reason="no_viable_service",
                        row=dead, histories=[q[2] for q in queues[dead]],
                        incoming_histories=(
                            [q[2] for q in queues[dead-1]] if dead else []))
        _, chosen = max(candidates)
        indices = [0] * k
        for j in range(k - 1, -1, -1):
            indices[j] = chosen
            chosen = predecessors[j][chosen]
        selected = [updated[j][indices[j]] for j in range(k)]
        finished.append(selected[-1][2])
        queues = [
            [token for u, token in enumerate(q) if u != options[j][indices[j]]]
            + ([(0, 0, [])] if j == 0 else [selected[j - 1]])
            for j, q in enumerate(queues)
        ]
        if stop_after == i + 1 and i + 1 < a:
            return dict(success=True, partial=True, queues=queues,
                        finished=finished, next_column=i+1)
    finished.extend(token[2] for q in queues for token in q)
    classes = [chain for chain in finished if chain]
    verify(h, classes)
    assert len(classes) <= capacity * k + a - 1
    return dict(success=True, colors=len(classes),
                longest=max(map(len, classes)), forced_rows=forced_rows,
                classes=classes)


def beam(h, capacity, b, width=64, branches=8, seconds=30):
    begun = time.monotonic()
    rng = random.Random(1729)
    states = [None]
    a = (h + 1) // 2
    for i in range(a):
        candidates = {}
        for state in states:
            for attempt in range(branches):
                if time.monotonic() - begun > seconds:
                    return dict(success=False, reason="time_cap", column=i)
                policy = ("random", "reserve", "oldest")[attempt % 3]
                nxt = run(h, capacity, rng.randrange(1 << 60), b, policy,
                          start=state, stop_after=i+1)
                if not nxt["success"]:
                    continue
                if not nxt.get("partial"):
                    return nxt
                key = tuple(tuple(sorted((t[0], t[1]) for t in row))
                            for row in nxt["queues"])
                if key in candidates:
                    continue
                score = rng.random() * 2
                for j, row in enumerate(nxt["queues"]):
                    for ahead in range(1, min(4, a-i)):
                        count = sum(legal(t, i+ahead, b[i+ahead][j]) for t in row)
                        score += math.log(0.25 + count) / ahead
                candidates[key] = (score, nxt)
        if not candidates:
            return dict(success=False, reason="beam_exhausted", column=i)
        states = [v[1] for v in sorted(candidates.values(),
                  key=lambda item: item[0], reverse=True)[:width]]
        print(json.dumps(dict(beam_column=i, candidates=len(candidates),
                              retained=len(states))), flush=True)


def verify(h, classes):
    a, k = (h + 1) // 2, h // 2
    cells = set()
    for chain in classes:
        for v in chain:
            assert v not in cells
            cells.add(v)
        for t, (i, j) in enumerate(chain):
            for ip, jp in chain[t + 1:]:
                assert 0 < jp - j <= ip - i
                for even_j, odd_i in [(j, ip), (jp, i)]:
                    n = 16 * (i - ip) ** 2 + (2 * (even_j - odd_i) + 1) ** 2
                    length = math.isqrt(n)
                    assert not (length < h and length * length == n)
    assert cells == {(i, j) for i in range(a) for j in range(k)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--heights", default="32,64,96,128,192,256")
    parser.add_argument("--capacities", default="2,3,4")
    parser.add_argument("--trials", type=int, default=12)
    parser.add_argument("--seconds", type=float, default=90)
    parser.add_argument("--policies", default="oldest,youngest,random")
    parser.add_argument("--output", default="continuation_monotone_queue_probe.json")
    args = parser.parse_args()
    started = time.monotonic()
    records, witnesses = [], []
    for h in map(int, args.heights.split(",")):
        b = blockers(h)
        for capacity in map(int, args.capacities.split(",")):
            successes, best_fail, policy_counts = 0, -1, {}
            witness = None
            trials = 0
            for seed in range(args.trials):
                if time.monotonic() - started > args.seconds:
                    break
                policies = args.policies.split(",")
                policy = policies[seed % len(policies)]
                trial = run(h, capacity, seed, b, policy)
                trials += 1
                if trial["success"]:
                    successes += 1
                    policy_counts[policy] = policy_counts.get(policy, 0) + 1
                    if witness is None or trial["colors"] < witness["colors"]:
                        witness = dict(h=h, capacity=capacity, seed=seed,
                                       policy=policy, **trial)
                else:
                    best_fail = max(best_fail, trial["column"])
            record = dict(h=h, capacity=capacity, trials=trials,
                          successes=successes, best_failed_column=best_fail,
                          policy_successes=policy_counts)
            records.append(record)
            print(json.dumps(record), flush=True)
            if witness is not None:
                witnesses.append(witness)
            if time.monotonic() - started > args.seconds:
                break
        if time.monotonic() - started > args.seconds:
            break
    result = dict(scope="exact-history queue experiments, no asymptotic theorem",
                  elapsed_seconds=time.monotonic()-started,
                  records=records, witnesses=witnesses)
    Path(args.output).write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
