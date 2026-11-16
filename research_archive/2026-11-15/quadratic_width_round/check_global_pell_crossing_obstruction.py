"""Sparse exact bisection checks of the global Pell crossing obstruction."""
from pathlib import Path
import json
from check_hilbert_endpoint_p_obstruction import point, rank, rectangle


def pell_seed(S):
    z,w = 1,0
    while True:
        z,w = 2*z+3*w,z+2*w
        if z % 4 == 1 and w % S == 0:
            return z,w


def check(S,z,w):
    assert z*z-3*w*w == 1 and z % 4 == 1 and w % S == 0
    q = 3*w//S
    n = 1 << (z.bit_length()-1)
    assert n >= 4 and n*n//16 > q
    assert n*n > 1600*q
    total = n*n
    A,B,h = 8*z+3,7*z+1,16*z
    def gap(r):
        i,_ = point(n,r)
        _,j = point(n,r+q)
        return j-i
    rn = rank(n,3*n//4,n//4-1)
    rp = rank(n,n//4-1,3*n//4)
    assert rn+q < total and rp+q < total
    assert gap(rn) < 0 and gap(rp) >= 2
    l,u = sorted((rn,rp))
    gl,gu = gap(l),gap(u)
    evaluations = 2
    found = None
    while u-l > 1:
        m = (l+u)//2
        gm = gap(m)
        evaluations += 1
        if gm in (0,1):
            found = m
            break
        if (gm < 0) == (gl < 0):
            l,gl = m,gm
        else:
            u,gu = m,gm
    if found is None:
        for r in (l,u):
            if gap(r) in (0,1):
                found = r
                break
    assert found is not None
    r = found
    i,j = point(n,r)
    ip,jp = point(n,r+q)
    gg = jp-i
    assert gg in (0,1)
    odd,even = A+4*i,B+4*jp
    X = S*q
    hyp = 2*z+1 if gg == 0 else 2*z-1
    Y = z+2 if gg == 0 else z-2
    assert even-odd == -Y and X*X+Y*Y == hyp*hyp
    lo,hi = (odd+even-hyp)//2,(odd+even+hyp)//2
    assert 1 < lo < hi < h and (hi-lo) % 2 == 1
    assert (odd+even-hyp) % 2 == 0
    own0 = B+4*j-(A+4*i)
    own1 = B+4*jp-(A+4*ip)
    assert abs(own0) >= z//2 and abs(own1) >= z//2
    middle = S*r+X//2
    C,D = (S*r,odd),(S*(r+q),even)
    P,Q = (middle,lo),(middle,hi)
    owner_column = S*(total+1)
    E,F = (owner_column,lo),(owner_column,hi)
    tilted,axis = (C,P,D,Q),(E,P,Q,F)
    assert rectangle(tilted) and rectangle(axis)
    for mask in range(4):
        black = {C,D,E,F} | ({P} if mask&1 else set()) | ({Q} if mask&2 else set())
        assert set(tilted)-black == set(axis)-black
    return {"S":S,"Z":z,"w":w,"h":h,"side":n,"q":q,
            "found_rank":r,"endpoint_cells":[[i,j],[ip,jp]],
            "g":gg,"norm":[X,Y,hyp],"half_factor":(hyp-Y)//2,
            "common_rows":[lo,hi],"own_gaps":[own0,own1],
            "bisection_evaluations":evaluations}


def main():
    cases=[]
    for S in (128,256):
        z,w = pell_seed(S)
        for _ in range(2):
            cases.append(check(S,z,w))
            z,w = z*z+3*w*w,2*z*w
    result={"status":"PASS","cases":cases,
            "scope":"Sparse canonical witnesses for the universal continuous-order proof."}
    Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":"PASS","cases":len(cases),
                      "evaluations":sum(c["bisection_evaluations"] for c in cases)}))


if __name__ == "__main__":
    main()

