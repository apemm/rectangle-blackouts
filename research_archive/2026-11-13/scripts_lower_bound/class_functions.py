"""Sanity exploration.  Parity partition, h even.  A bishop class of a saturated board has exactly one
black cell per column.  Count the functions phi:[1,w]->[1,h], phi(x) = x + par (mod 2), with each row
used at most cap times, such that no 45-degree rectangle inside [1,w]x[1,h] has >= 3 black corners.
usage: py class_functions.py h w cap par [seconds]
"""
import sys, time


def run(h, w, cap, par, tl):
    t0 = time.time()
    rows_for = {}
    for x in range(1, w + 1):
        rows_for[x] = [y for y in range(1, h + 1) if (x + y) % 2 == par]
    phi = [0] * (w + 2)
    use = [0] * (h + 2)
    count = [0]
    sols = []
    timeout = [False]
    # diag[v] = list of points on diagonal v ; anti[u] = list on antidiagonal u
    diag = {}
    anti = {}

    def ok(x, y):
        # new point N=(x,y); existing points are in columns < x
        dn = diag.get(x - y, [])
        an = anti.get(x + y, [])
        # right angle at N: P on diagonal (SW of N), Q on antidiagonal (NW of N)
        for P in dn:
            for Q in an:
                fx = P[0] + Q[0] - x
                fy = P[1] + Q[1] - y
                if 1 <= fx <= w and 1 <= fy <= h:
                    return False
        # right angle at P (on N's diagonal): Q on P's antidiagonal
        for P in dn:
            for Q in anti.get(P[0] + P[1], []):
                if Q == P:
                    continue
                fx = x + Q[0] - P[0]
                fy = y + Q[1] - P[1]
                if 1 <= fx <= w and 1 <= fy <= h:
                    return False
        for P in an:
            for Q in diag.get(P[0] - P[1], []):
                if Q == P:
                    continue
                fx = x + Q[0] - P[0]
                fy = y + Q[1] - P[1]
                if 1 <= fx <= w and 1 <= fy <= h:
                    return False
        return True

    def dfs(x):
        if timeout[0]:
            return
        if x > w:
            count[0] += 1
            if len(sols) < 1000000:
                sols.append(tuple(phi[1:w + 1]))
            if count[0] % 5000 == 0 and time.time() - t0 > tl:
                timeout[0] = True
            return
        if time.time() - t0 > tl:
            timeout[0] = True
            return
        for y in rows_for[x]:
            if use[y] >= cap:
                continue
            if not ok(x, y):
                continue
            phi[x] = y
            use[y] += 1
            diag.setdefault(x - y, []).append((x, y))
            anti.setdefault(x + y, []).append((x, y))
            dfs(x + 1)
            diag[x - y].pop()
            anti[x + y].pop()
            use[y] -= 1

    dfs(1)
    return count[0], sols, timeout[0], time.time() - t0


if __name__ == '__main__':
    h = int(sys.argv[1])
    w = int(sys.argv[2])
    cap = int(sys.argv[3])
    par = int(sys.argv[4])
    tl = float(sys.argv[5]) if len(sys.argv) > 5 else 40
    c, sols, to, el = run(h, w, cap, par, tl)
    print('h', h, 'w', w, 'cap', cap, 'par', par, 'count', c, 'timeout', to, 'sec', round(el, 1))
    for s in sols[:5]:
        print('  ', s)
