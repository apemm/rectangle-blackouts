import sys,json
for line in sys.stdin:
    line=line.strip()
    if not line.startswith('{'): print(line); continue
    r=json.loads(line)
    if 'row_cands_O' in r: print(r); continue
    print('M',r['M'],'R2s',{k:r['R2s'][k] for k in ['constraints','mean_inc','max_inc','degeneracy']},'P',r.get('P'),'PuR2s',{k:r['PuR2s'][k] for k in ['constraints','mean_inc','max_inc','degeneracy','core_sizes','greedy_stuck','M_suffices','method','exact_Mcore']} if 'PuR2s' in r else None)
