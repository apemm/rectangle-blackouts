"""Interval check of the exponents in Table 1 of the upper-bound draft.

For k = 1..10 the exponent is x_k = min over a > 0 of (beta_k(a) + 2)/(1 + a), with
beta_k(a) = ((1 + 3^(a/k))/2)^k - 1. For k = infinity it is x_inf = min over a > 0 of
(1 + 3^(a/2))/(1 + a). Each minimum is at most the value at any point a, so it is enough
to evaluate the function at the tabulated point in outward-rounded interval arithmetic
and check that the whole interval lies below the tabulated bound.
"""
from mpmath import iv

iv.dps = 50

ROWS = [
    (1, '0.9124153', '1.4967430'),
    (2, '1.1056653', '1.4295235'),
    (3, '1.2096718', '1.3986921'),
    (4, '1.2756813', '1.3807492'),
    (5, '1.3215661', '1.3689531'),
    (6, '1.3554037', '1.3605886'),
    (7, '1.3814256', '1.3543412'),
    (8, '1.4020770', '1.3494942'),
    (9, '1.4188737', '1.3456226'),
    (10, '1.4328078', '1.3424580'),
]
INF_ROW = ('1.5833613', '1.3108172')


def e_k(k, a):
    beta = ((1 + iv.mpf(3) ** (a / k)) / 2) ** k - 1
    return (beta + 2) / (1 + a)


def e_inf(a):
    return (1 + iv.mpf(3) ** (a / 2)) / (1 + a)


margins = []
for k, a, bound in ROWS:
    val = e_k(k, iv.mpf(a))
    margin = iv.mpf(bound).a - val.b
    assert margin > 0, (k, a, bound)
    margins.append(margin)
    print(f'k = {k:2d}: value at a = {a} is below {bound}, margin {float(margin):.3e}')

a, bound = INF_ROW
val = e_inf(iv.mpf(a))
margin = iv.mpf(bound).a - val.b
assert margin > 0
margins.append(margin)
print(f'k = inf: value at a = {a} is below {bound}, margin {float(margin):.3e}')
print(f'least margin {float(min(margins)):.3e}')
