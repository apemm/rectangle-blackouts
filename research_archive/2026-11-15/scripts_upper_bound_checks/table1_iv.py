from mpmath import iv, mpf
iv.dps = 50
rows = {1:('0.9124153','1.4967430'),2:('1.1056653','1.4295235'),3:('1.2096718','1.3986921'),
 4:('1.2756813','1.3807492'),5:('1.3215661','1.3689531'),6:('1.3554037','1.3605886'),
 7:('1.3814256','1.3543412'),8:('1.4020770','1.3494942'),9:('1.4188737','1.3456226'),
 10:('1.4328078','1.3424580')}
three = iv.mpf(3)
ok = True
for k,(a,bound) in rows.items():
    A = iv.mpf(a)
    beta = ((1 + three**(A/k))/2)**k - 1
    e = (beta + 2)/(1 + A)
    good = e.b < iv.mpf(bound).a
    ok &= good
    print(k, a, 'upper end', iv.nstr(e.b, 12), '<', bound, good)
A = iv.mpf('1.5833613')
einf = (1 + three**(A/2))/(1 + A)
print('inf', iv.nstr(einf.b, 14), '< 1.3108172', einf.b < iv.mpf('1.3108172').a)
print('all', ok)
