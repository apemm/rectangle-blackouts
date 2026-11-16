"""Average of F^-_U over U = weighted 2-core (a lower bound for B(M))."""
import sys, numpy as np
from analyze import core_peel
z=np.load(sys.argv[1]); h,S,M,q,labels=map(int,z['meta']); w=z['witness']
C,inv=np.unique(w[:,:3],axis=0,return_inverse=True); inv=inv.ravel()
verts,cu=np.unique(np.concatenate([C[:,0],C[:,1]]),return_inverse=True); nv=len(verts); m=len(C)
u,v=cu[:m],cu[m:]
for name,(alive,ae) in {"all":(np.ones(nv,bool),np.ones(m,bool)),"2core":core_peel(u,v,nv,2)[:2]}.items():
    wa=ae[inv]
    pairs=np.unique(np.stack([v[inv][wa],w[wa,3]],1),axis=0)
    Fm=np.bincount(pairs[:,0],minlength=nv)
    print(h,S,M,name,"|U|",int(alive.sum()),"avg F^-_U",round(float(Fm[alive].sum()/alive.sum()),4),
          "avg b^-_U",round(float(ae.sum()/alive.sum()),4),"=> criterion M>8B needs M >",round(8*float(Fm[alive].sum()/alive.sum()),2))
