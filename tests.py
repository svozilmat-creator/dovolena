import json,pathlib
r=pathlib.Path(__file__).parent;d=json.load(open(r/'destinations.json'))
assert len(d)==100 and len({x['id'] for x in d})==100
for x in d:
 assert len(x['seasonality'])==12
 assert (r/x['image']).exists()
 assert all(0<=v<=10 for v in x['scores'].values())
print('OK',len(d),'destinací')
