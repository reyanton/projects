import numpy as np
import pandas as pd
import xlrd

df_can = pd.read_excel('Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can['Total'] = df_can.sum(axis=1)

condition = df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]
print(df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')])
