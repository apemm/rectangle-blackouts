from eq_enum import spf_sieve, EQ
Qs=[30030,55440,60060,65521,99991,100800]
spf=spf_sieve(max(Qs)+5)
for Q in Qs:
    es=set(x[0] for x in EQ(Q,spf)); print(Q,len(es),'Q^0.8=',round(Q**.8))
