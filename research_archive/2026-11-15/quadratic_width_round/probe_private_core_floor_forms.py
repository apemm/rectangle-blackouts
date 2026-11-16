"""Small exact search for transparent floor-linear core colorings."""
from pathlib import Path
import json

folder=Path(__file__).resolve().parent
items=json.loads((folder/'private_tile_gain_cores_side16.json').read_text())['small_final_cores']
results=[]
for item in items:
    if item['offset'] not in (1732,-1733,-1739):
        continue
    found=[]
    tested=0
    for denominator in range(1,17):
        for ai in range(-8,9):
            for aj in range(-8,9):
                if ai==aj==0:
                    continue
                for shift in range(denominator):
                    values=[(ai*i+aj*j+shift)//denominator%3 for i,j in item['cells']]
                    tested+=1
                    if all((values[s]-values[r])%3 not in gains for r,s,gains in item['edges']):
                        found.append({'i_coefficient':ai,'j_coefficient':aj,
                                      'shift':shift,'denominator':denominator,'colors':values})
        if found:
            break
    results.append({'offset':item['offset'],'tested':tested,'solutions':found})
(folder/'private_core_floor_forms.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
