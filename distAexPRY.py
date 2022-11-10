import json
import pandas as pd


data = open('Apex PRY.json', 'r', encoding='UTF-8')

js = json.loads(data.read())
print(json.dumps(js, indent=4))
det = []
for item in js:
    #mun = item[0]
    det.append((item['codigo_departamento'], item['departamento_denominacion'],item['codigo_ciudad'], item['denominacion'],  item['ubicacion_geografica']))
#     for k,v in mun.items():
#       cant = k
#         #for t in v.items():
#       det.append((item, k,v))
#           #det.append((item, k.encode('UTF-8'), v))
    df = pd.DataFrame.from_records(det, columns =['CodDpto', 'Dpto', 'CodCiudad', 'Ciudad', 'Geoloc']) 
    df.to_excel ('PRY_Apex.xls', index = False, header=True)

print(df)