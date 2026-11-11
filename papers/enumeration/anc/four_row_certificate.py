"""Check of the four-row recurrence on the automaton of Proposition "the automaton".

For each of the 3 pair sets F the script builds the automaton A_F exactly as the
proposition defines it. A state is the word of the last 6 letters read and the set of
pairs of F read so far. The proof of the recurrence is the function exact(), described
at the end. Before it, as a quick test, the script checks modulo each of two primes
below 2^31

  (1) that sum_j q_j a_4(n-j) = 0 for 445 <= n <= NMAX and not for n = 444, where the q_j
      are the coefficients of Q in four_row_gf.txt and a_4(n) = 0 for n < 6,
  (2) that Q times the series of a_4 agrees with P of four_row_gf.txt up to z^NMAX, and
  (3) for each F, the first index K >= 445 such that sum_j q_j u_F(K-j) = 0 in every
      coordinate. Here u_F(n) is the vector that gives, for each state, the number of
      words of length n that lead from this state to acceptance. Since u_F(n+1) is a fixed
      linear image of u_F(n) and a_F(n) is the coordinate of the start state, this gives
      the recurrence for a_F(n) modulo the prime for every n >= K.

Checks (1) to (3) are modular and prove nothing over the integers. The function exact()
repeats (3) at K = 445 and the comparison with P modulo 48 primes below 2^31. Their
product exceeds twice the largest possible absolute value of the integers involved, so
by the Chinese remainder theorem these two statements hold over the integers. Usage:  py four_row_certificate.py [NMAX]   (default 1000)
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
PRIMES = (2147483629, 2147483587)
PARTS = {'{1,2}|{3,4}': ((1, 2), (3, 4)),
         '{1,3}|{2,4}': ((1, 3), (2, 4)),
         '{1,4}|{2,3}': ((1, 4), (2, 3))}
TEMPLATES = ((3, 4, 1, 2), (3, 1, 4, 2), (2, 4, 1, 3), (2, 1, 4, 3))


def tilted(length):
    """Tilted rectangles in columns 1..length, as tuples of (column, row) corners."""
    out = []
    for i in range(1, length - 1):
        for j in (1, 2):
            out.append(((i, j + 1), (i + 1, j), (i + 2, j + 1), (i + 1, j + 2)))
    for i in range(1, length - 2):
        for rows in TEMPLATES:
            out.append(tuple((i + k, rows[k]) for k in range(4)))
    return out


TILTED = {n: tilted(n) for n in range(0, 8)}


def build(part, only_test=False):
    pairs = [frozenset((a, b)) for a in part[0] for b in part[1]]
    letters = [frozenset((r,)) for r in (1, 2, 3, 4)] + pairs
    fset = set(pairs)
    cache = {}

    def has_rival(pres, word):
        if len(pres) == 1:
            (x, r), = pres
            return any(frozenset((r, s)) in fset for s in letters[word[x - 1]])
        (x, r), (z, s) = pres
        if x == z:
            return frozenset((r, s)) in fset
        if r == s:
            return bool(letters[word[x - 1]] & letters[word[z - 1]])
        return s in letters[word[x - 1]] and r in letters[word[z - 1]]

    def ok(word):
        """word: tuple of letter indices, the last one is the new column."""
        res = cache.get(word)
        if res is not None:
            return res
        n = len(word)
        pres = []
        for rect in TILTED[n]:
            pres.append(frozenset(p for p in rect if p[1] not in letters[word[p[0] - 1]]))
        good = True
        for k, rect in enumerate(TILTED[n]):
            if max(p[0] for p in rect) != n:
                continue
            shown = pres[k]
            if len(shown) == 0:
                good = False
                break
            if len(shown) <= 2:
                if has_rival(tuple(shown), word):
                    good = False
                    break
                if any(pres[i] == shown for i in range(len(pres)) if i != k):
                    good = False
                    break
        cache[word] = good
        return good

    if only_test:
        return letters, ok
    start = ((), 0)
    index = {start: 0}
    order = [start]
    src, dst = [], []
    head = 0
    while head < len(order):
        u, used = order[head]
        for y in range(8):
            bit = 0
            if y >= 4:
                bit = 1 << (y - 4)
                if used & bit:
                    continue
            word = u + (y,)
            if not ok(word):
                continue
            state = (word[-6:], used | bit)
            k = index.get(state)
            if k is None:
                k = len(order)
                index[state] = k
                order.append(state)
            src.append(head)
            dst.append(k)
        head += 1
    accept = np.array([1 if used == 15 else 0 for _, used in order], dtype=np.int64)
    return len(order), np.array(src, dtype=np.int64), np.array(dst, dtype=np.int64), accept


def read_gf():
    pcoef, qcoef = {}, {}
    with open(os.path.join(HERE, 'four_row_gf.txt')) as fh:
        for line in fh:
            t = line.split()
            if len(t) == 3 and t[0] == 'P':
                pcoef[int(t[1])] = int(t[2])
            elif len(t) == 3 and t[0] == 'Q':
                qcoef[int(t[1])] = int(t[2])
    return ([pcoef.get(k, 0) for k in range(max(pcoef) + 1)],
            [qcoef.get(k, 0) for k in range(max(qcoef) + 1)])


def primes_below(top, count):
    out = []
    n = top
    while len(out) < count:
        n -= 1
        if n % 2 and all(n % d for d in range(3, int(n ** 0.5) + 1, 2)):
            out.append(n)
    return out


def exact(machines, pnum, qden, index=445):
    """Exact form of (3) and of the numerator, by the Chinese remainder theorem.

    Every entry of u_F(n) is at most 8^n, so every entry of sum_j q_j u_F(index-j) has
    absolute value at most A 8^index, where A is the sum of the |q_j|. If it vanishes
    modulo primes whose product exceeds 2 A 8^index, it vanishes. In the same way the
    coefficients of Q times the series of a_4 up to z^(index-1) are compared with P.
    """
    deg = len(qden) - 1
    bound = 2 * 3 * sum(abs(q) for q in qden) * 8 ** index
    bound = max(bound, 2 * max(abs(c) for c in pnum))
    # The numerator check needs 2 (3 A 8^(index-1) + max|P_n|), which is smaller.
    assert bound >= 2 * (3 * sum(abs(q) for q in qden) * 8 ** (index - 1)
                         + max(abs(c) for c in pnum))
    primes, prod = [], 1
    for p in primes_below(2 ** 31, 80):
        primes.append(p)
        prod *= p
        if prod > bound:
            break
    assert prod > bound
    vector_ok, numerator_ok = True, True
    for p in primes:
        qmod = [q % p for q in qden]
        total = [0] * index
        for nstates, rows, d_sorted, firsts, accept in machines:
            u = accept.copy()
            acc = np.zeros(nstates, dtype=np.int64)
            for n in range(index + 1):
                if index - n <= deg:
                    acc = (acc + qmod[index - n] * u) % p
                if 6 <= n < index:
                    total[n] = (total[n] + int(u[0])) % p
                nxt = np.zeros(nstates, dtype=np.int64)
                nxt[rows] = np.add.reduceat(u[d_sorted], firsts) % p
                u = nxt
            vector_ok = vector_ok and not acc.any()
        for n in range(index):
            lhs = sum(qmod[j] * total[n - j] for j in range(min(n, deg) + 1)) % p
            rhs = pnum[n] % p if n < len(pnum) else 0
            numerator_ok = numerator_ok and lhs == rhs
    return {'index': index, 'number_of_primes': len(primes),
            'smallest_prime': min(primes), 'largest_prime': max(primes),
            'bits_of_product': prod.bit_length(), 'bits_of_bound': bound.bit_length(),
            'vector_identity_exact': bool(vector_ok),
            'numerator_exact': bool(numerator_ok and len(pnum) == index)}


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    t0 = time.time()
    pnum, qden = read_gf()
    deg = len(qden) - 1
    report = {'nmax': nmax, 'primes': list(PRIMES), 'degree_Q': deg,
              'degree_P': len(pnum) - 1, 'pair_sets': {}}
    total = {p: np.zeros(nmax + 1, dtype=np.int64) for p in PRIMES}
    machines = []
    for name, part in PARTS.items():
        nstates, src, dst, accept = build(part)
        info = {'states': int(nstates), 'transitions': int(len(src))}
        by_src = np.argsort(src, kind='stable')
        s_sorted, d_sorted = src[by_src], dst[by_src]
        firsts = np.flatnonzero(np.r_[True, s_sorted[1:] != s_sorted[:-1]])
        rows = s_sorted[firsts]
        machines.append((nstates, rows, d_sorted, firsts, accept))
        for p in PRIMES:
            qmod = [q % p for q in qden]
            u = accept.copy()
            vecs = []
            counts = np.zeros(nmax + 1, dtype=np.int64)
            hold = None
            for n in range(nmax + 1):
                counts[n] = u[0]
                vecs.append(u)
                if len(vecs) > deg + 1:
                    vecs.pop(0)
                if hold is None and n >= 445 and n <= 470:
                    acc = np.zeros(nstates, dtype=np.int64)
                    for j in range(deg + 1):
                        acc = (acc + qmod[j] * vecs[deg - j]) % p
                    if not acc.any():
                        hold = n
                nxt = np.zeros(nstates, dtype=np.int64)
                nxt[rows] = np.add.reduceat(u[d_sorted], firsts) % p
                u = nxt
            info['vector_identity_first_index_mod_%d' % p] = hold
            counts[:6] = 0
            total[p] = (total[p] + counts) % p
            info['counts_6_to_12_mod_%d' % p] = [int(c) for c in counts[6:13]]
        report['pair_sets'][name] = info
        print(name, info, round(time.time() - t0, 1), flush=True)
    for p in PRIMES:
        a = [int(x) for x in total[p]]
        res = []
        for n in range(nmax + 1):
            res.append(sum((qden[j] % p) * a[n - j] for j in range(min(n, deg) + 1)) % p)
        nonzero = [n for n in range(nmax + 1) if res[n]]
        matches = all(res[n] == (pnum[n] % p if n < len(pnum) else 0)
                      for n in range(nmax + 1))
        report['mod_%d' % p] = {
            'recurrence_holds_445_to_nmax': all(res[n] == 0 for n in range(445, nmax + 1)),
            'last_index_where_it_fails': max(nonzero),
            'product_Q_times_series_equals_P': matches,
            'a4_6_to_12': a[6:13]}
    report['exact'] = exact(machines, pnum, qden)
    report['seconds'] = round(time.time() - t0, 1)
    with open(os.path.join(HERE, 'four_row_certificate.json'), 'w') as fh:
        json.dump(report, fh, indent=1)
    print(json.dumps(report, indent=1))


if __name__ == '__main__':
    main()
