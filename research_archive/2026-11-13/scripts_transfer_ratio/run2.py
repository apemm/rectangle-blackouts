import sys,os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from riv_u import pred_edges, brute
for (u,h,iota,mod,k) in [(3,3000,1165%32,32,5),(3,3000,1,32,5),(3,3000,13,32,5),(1,8000,1237%32,32,5),(5,2400,1,8,3),(9,2400,5,8,3),(3,2600,5,8,3)]:
    P={e for e in pred_edges(u,k,(h-1)//2) if e[0]%mod==iota%mod}
    Bf=brute(u,h,iota,mod)
    print("u",u,"h",h,"iota",iota,"mod",mod,"pred",sorted(P),"brute",sorted(Bf),"equal",P==Bf)
for u in (1,3,5,7,9):
    for k in (3,5):
        P=pred_edges(u,k,10**6)
        print("u",u,"k",k,"edges<=1e6:",len(P),"smallest:",sorted(P,key=lambda e:e[1])[:3])
