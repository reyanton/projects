import pandas as pd
import xlrd
import mysql.connector as mysql

db = mysql.connect(
    host = "10.2.0.49",
    user = "contabilidad",#root",
    passwd = "*Ecomm.2020",#"*Mysql2019*",
    database = 'contabilidadbd'
)

archivo = 'Distribucione_ 2021_Base.xlsx'
anio_dist =2021
  
wb = xlrd.open_workbook(archivo) 
hoja = wb.sheet_by_index(0) 

num_hojas = wb.nsheets
nom_hoja = wb._sheet_names[0]

def guardardatos(idemp,codigo,cedula, marca, anio, porc, estatus):
    cursor = db.cursor()
    query = """INSERT INTO distribuciones2021(empleado_id, empleado_cod, documento, marca_id, anio, porcentaje, status) VALUES(%s, %s, %s, %s, %s, %s, %s)"""
    valores = (idemp, codigo, cedula, marca, anio, porc, estatus)
    cursor.execute(query, valores)
    db.commit()
    #print(cursor.rowcount, "record inserted")
    #print(codigo + ' ' + str(marca) + ' ' + str(anio) + ' ' + str(porc) + ' ' + str(estatus) )
    #query2 = """SELECT  * FROM distribuciones where anio = 2000 order by id desc limit 5""" #WHERE empleado_id = '%s' """ 
    #cursor.execute(query2)
    #record = cursor.fetchall()
    #print(record)
    cursor.close()

def procesarexcel():
    filas = []
    for fila in range(1,hoja.nrows):
        columnas = []

        cedula = hoja.cell_value(fila,1)
        id_empleado = hoja.cell_value(fila,2) 
        codigo_emp = hoja.cell_value(fila,3)
        

        for columna in range(4,hoja.ncols):
            columnas = []
            
            if (hoja.cell_value(0,columna) is not None or hoja.cell_value(0,columna) != ''):
                porc = hoja.cell_value(fila,columna)
                Marca = int(hoja.cell_value(0,columna))
                
                #print(cedula, Marca, porc)
                if porc is None or porc == '': 
                    porc = 0

                float(int(porc))
                if (porc > 0.0):    
                    Valor = porc * 100
                    columnas.append(id_empleado)
                    columnas.append(codigo_emp)
                    columnas.append(cedula)
                    columnas.append(Marca)
                    columnas.append(anio_dist)
                    columnas.append(str(Valor))
                    columnas.append('1')

                    guardardatos(id_empleado,codigo_emp, cedula, Marca, anio_dist, Valor, 0)
                    print(columnas)
                    filas.append(columnas)
                
            #Marca = Marca + 1
    if filas:
        df = pd.DataFrame(filas,columns=['ID','CODIGO','CEDULA','MARCA','ANIO','PORC','ESTATUS'])
        df.to_excel(writer, sheet_name=nom_hoja)
    #print(df)
        #df.to_excel('Distribuciones2021.xlsx', sheet_name='ULTRA', index = False)


writer = pd.ExcelWriter('2021Dist.xlsx', engine='xlsxwriter')

#Procesar archivo
for item in range(num_hojas-2):
    hoja = wb.sheet_by_index(item) 
    nom_hoja = wb._sheet_names[item]
    
    procesarexcel()

writer.save()