"""Count single-defect and two-defect neighborhoods for the 127-row insertion word."""
from fractions import Fraction


def main():
    divisors=[1,2,11,22,121,242]
    signed=divisors+[-d for d in divisors]
    implications=[(-d,242//d-d) for d in signed]
    exclusions=[(-1,4),(-2,2),(-4,1)]
    offsets=sorted({0,*[x for pair in implications+exclusions for x in pair]})
    assert len(offsets)==19

    positions={v:i for i,v in enumerate(offsets)}
    implications=[(1<<positions[u],1<<positions[v]) for u,v in implications]
    exclusions=[(1<<positions[u]) | (1<<positions[v]) for u,v in exclusions]
    center=1<<positions[0]
    accepted=[]
    for mask in range(1<<len(offsets)):
        if not mask&center:
            continue
        if any(mask&u and not mask&v for u,v in implications):
            continue
        if any(mask&uv==uv for uv in exclusions):
            continue
        accepted.append(mask)
    assert len(accepted)==6720
    margin=Fraction(len(accepted),2**len(offsets))
    print("single-site probability",margin)

    for step,expected in [(4,Fraction(3758400,2**35)),(5,Fraction(14288400,2**36))]:
        common=[x for x in offsets if x-step in positions]
        counts=[]
        for start in (0,step):
            histogram=[0]*(1<<len(common))
            for mask in accepted:
                key=sum((1<<k) for k,x in enumerate(common) if mask & (1<<positions[x-start]))
                histogram[key]+=1
            counts.append(histogram)
        numerator=sum(x*y for x,y in zip(*counts))
        probability=Fraction(numerator,2**(2*len(offsets)-len(common)))
        assert probability==expected
        margin-=probability
        print("spacing",step,"overlap",common,"histograms",counts,"joint",probability)
    assert margin>Fraction(1,80)
    print("retained density",margin,float(margin))


if __name__=="__main__":
    main()
