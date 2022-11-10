import pandas as pd
import numpy as np
import xlrd

data = pd.read_csv(r'C:\Proyectos\ExcelContab\Distrib_2020.csv')
print(data)

#print(data)
#sheets = pd.pivot_table(data, index= ['empleado_id','marca_id'], values = ['porcentaje'], aggfunc = np.sum)
sheets = pd.pivot_table(data, 'porcentaje', ['empleado'], 'marca')

print(sheets)

writer = pd.ExcelWriter('Distrib_2020.xlsx', engine='xlsxwriter')
df = pd.DataFrame(sheets) #columns=['MARCA1','MARCA2','MARCA3','MARCA4','MARCA5', 'MARCA6','MARCA7','MARCA8','MARCA9'])
#df.to_excel('Dist_2020.xlsx', sheet_name='DATA', index = False)
df.to_excel(writer, sheet_name="nom_hoja")

writer.save()