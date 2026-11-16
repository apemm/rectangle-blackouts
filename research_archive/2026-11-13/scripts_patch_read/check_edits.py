import json,sys
E=json.load(open(sys.argv[1],encoding='utf-8'))
F=open(sys.argv[2],encoding='utf-8').read()
P=open(sys.argv[3],encoding='utf-8').read()
for k,e in enumerate(E,1):
    o,n=e['old_str'],e['new_str']
    print(k,'new_in_filed',F.count(n),'new_in_patched',P.count(n),'old_in_filed',F.count(o))
