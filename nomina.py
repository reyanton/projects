import pandas as pd
import mysql.connector as mysql
import xlrd
import os


db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "*Mysql2019*",
    database = 'contabilidaddb'
)

ruta = "C:/Proyectos/ExcelContab/Nominas"
datalist = list()
noexist = dict()
fileslist = list()

def nominas():
    cursor = db.cursor()
    query = """select numero_empleado from empl_master"""
    cursor.execute(query)
    datadb = cursor.fetchall()
    for datos in datadb:
        datalist.append(datos[0].strip())
    

def procesarexcel(archivo):
    for fila in range(1,hoja.nrows):
        codigo_emp = (hoja.cell_value(fila,14)).strip()
        monto = hoja.cell_value(fila,54)
        if codigo_emp not in datalist and int(monto) > 0:
            noexist[codigo_emp] = archivo


def cargararchivos():
    for file in os.listdir(ruta):
        if file.endswith(".xlsx"):
           fileslist.append( file)
