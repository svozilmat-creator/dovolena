import json, pathlib
root=pathlib.Path(__file__).parent
data=json.loads((root/'destinations.json').read_text())
assert len(data)==100
assert len({d['id'] for d in data})==100
for d in data:
 assert set(map(str,range(1,13)))==set(d['seasonality'])
 assert all(0<=v<=10 for v in d['scores'].values())
 assert d['costs']['accommodationPerNight']['min']<=d['costs']['accommodationPerNight']['max']
 assert d['transport']['recommended'] in {'AUTO','LETADLO','AUTO I LETADLO'}
 assert (root/d['image']).exists()
print('OK: 100 destinací, unikátní ID, 12 měsíců, rozsahy, doprava a obrázky.')
