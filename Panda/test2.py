
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


print ('Matplotlib version: ', mpl.__version__)
print(plt.style.available)

df_can = pd.read_excel('Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can['Total'] = df_can.sum(axis=1)
df_can.set_index('Country', inplace=True)

years = list(map(str, range(1980, 2014)))
#print(df_can.loc['Haiti'], years)
haiti = df_can.loc['Haiti', years] # ejecución en los años 1980 a 2013 para excluir la columna 'total'

haiti.plot()