import pandas as pd
import xlrd
import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "*Mysql2019*",
    database = 'contabilidadbd'
)

#archivo = 'DISTRIBUCION MERYS.xlsx'
archivo = 'DISTRIBUCION_2020.xlsx'
anio_dist =2020
  
wb = xlrd.open_workbook(archivo) 
hoja = wb.sheet_by_index(0)

num_hojas = wb.nsheets
nom_hoja = wb._sheet_names[0]

def guardardatos(codigo, marca, anio, porc, estatus):
    cursor = db.cursor()
    query = """INSERT INTO distribuciones(empleado_id, marca_id, anio, porcentaje, status) VALUES(%s, %s, %s, %s, %s)"""
    valores = (codigo, marca, anio, porc, estatus)
    cursor.execute(query, valores)
    db.commit()
    
    cursor.close()

def procesarexcel():
    filas = []
    for fila in range(1,hoja.nrows):
        columnas = []
        codigo_emp = hoja.cell_value(fila,3)
        Marca = 1

        for columna in range(6,15): #34 todas las marcas 
            columnas = []
            porc = hoja.cell_value(fila,columna)
            #print( str(fila) + ',' + str(columna) + '-' + str(codigo_emp) + '-' + str(porc))
            
            if porc is None or porc == '': 
                porc = 0
            #print("asigne la celda - " + str(porc))
            float(int(porc))
            if (porc > 0.0):    
                Valor = porc * 100
                columnas.append(codigo_emp)
                columnas.append(Marca)
                columnas.append(anio_dist)
                columnas.append(str(Valor))
                columnas.append('0')

                #guardardatos(codigo_emp, Marca, anio_dist, Valor, 0)

                filas.append(columnas)
            
            #Marca = Marca + 1
            #print(nom_hoja + ' - ' + str(Marca) + '-' + str(fila) + '-' + str(columna) )
    

    if filas:
        df = pd.DataFrame(filas,columns=['CODIGO','MARCA','ANIO','PORC','ESTATUS'])
        
        df.to_excel(writer, sheet_name=nom_hoja)

    #df.to_excel('Distribucion2020.xlsx', sheet_name='ULTRA', index = False)


writer = pd.ExcelWriter('2020Dist.xlsx', engine='xlsxwriter')

for item in range(num_hojas):
    hoja = wb.sheet_by_index(item) 
    nom_hoja = wb._sheet_names[item]
    #Procesar archivo
    procesarexcel()

writer.save()