import pandas as pd
import xlrd

df1 = pd.DataFrame({'Data': ['a', 'b', 'c', 'd']})

df2 = pd.DataFrame({'Data': [1, 2, 3, 4]})

df3 = pd.DataFrame({'Data': [1.1, 1.2, 1.3, 1.4]})

archivo = 'DISTRIBUCION_2020.xlsx'
anio_dist =2020
  
wb = xlrd.open_workbook(archivo) 
num_hojas = wb.nsheets

for item in range(num_hojas):
    hoja = wb.sheet_by_index(item) 
    nom_hoja = wb._sheet_names[item]


writer = pd.ExcelWriter('multiple.xlsx', engine='xlsxwriter')

df1.to_excel(writer, sheet_name='Sheeta')

df2.to_excel(writer, sheet_name='Sheetb')

df3.to_excel(writer, sheet_name='Sheetc')

writer.save()