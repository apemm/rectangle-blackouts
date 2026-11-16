"""Eight-bit norm certificate for the t=6 diagonal branch."""
from pathlib import Path
import json
from probe_diagonal_alignment_registers import seed
from check_hilbert_odd_valuation_alignment import step,terminal


def audit():
    template, states = seed(3,mask=13,J=8)
    assert len(states)==384
    grouped={}
    for s in states:
        C,D=s[7:]
        b=9*D*D*pow(16*C+1,-1,256)%256
        assert b%8==1
        grouped.setdefault(b,set()).add((*s[:7],*([0]*8)))
    groups=[]
    for b,current in sorted(grouped.items()):
        levels=[sorted(current)]
        for bit in range(8):
            current={n for s in current for n in step(s,template['coeff'],template['base'],(b>>bit)&1)}
            assert not any(terminal(s,template['base']) for s in current)
            levels.append(sorted(current))
        assert not current
        groups.append(dict(b_mod256=b,levels=levels))
    return dict(status='PASS: diagonal t=6, all four outer orientations',
                seed_states=sorted(states),groups=groups)


if __name__=='__main__':
    result=audit()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'])
