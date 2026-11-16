import sys, numpy as np
parts=[np.load(p) for p in sys.argv[2:]]
meta=parts[0]['meta']; assert all((p['meta']==meta).all() for p in parts)
w=np.unique(np.concatenate([p['witness'] for p in parts]),axis=0)
np.savez_compressed(sys.argv[1], witness=w, meta=meta); print(len(w))
