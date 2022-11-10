import json
import pandas as pd


data = open('jsonURY.json', 'r', encoding='UTF-8')

js = json.loads(data.read())
# print(json.dumps(js, indent=4))
det = []
for item in js:
    print(item)
#     print(item['id'], item['nombre'].split('(')[0], item['nombre'].split('(')[1].replace(')',''))
#     provinicia = item['nombre'].split('(')[1].replace(')','')
#     capital = item['nombre'].split('(')[0]
#     codigo = item['id']

#     det.append((provinicia, capital, codigo))

# df = pd.DataFrame.from_records(det, columns =['Prov', 'Cap', 'Cod']) 
# df.to_excel ('serv_ecu.xls', index = False, header=True)
#     # item['nombre'].split(' ')[1].replace('(', '').replace(')', '')
#     for k,v in mun.items():
#       cant = k
#         #for t in v.items():
#       det.append((item, k,v))
#           #det.append((item, k.encode('UTF-8'), v))
#       df = pd.DataFrame.from_records(det, columns =['Dpto', 'Cap', 'Cod']) 
#       df.to_excel ('ecud.xls', index = False, header=True)

# print(df)