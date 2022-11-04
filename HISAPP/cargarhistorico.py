import dbconnection as dbc
import pandas as pd
from pandas import json_normalize
import json
import os
import sys
from datetime import datetime, timedelta, timezone
import sqlalchemy as sa


def cargardatos(source:str, dbdata:str,destination:str, dbdestination:str, dia, pathfile):
    
    
    try:
        #conexión externa
        conn = dbc.db_connect(source, dbdata,'novelty_reportes','novelty2020')

        #conexion local
        connstring = 'mssql+pyodbc://nwduser:nwduser@'  + destination + '/' + dbdestination + '?driver=SQL+Server+Native+Client+11.0'
        engine = sa.create_engine(connstring, connect_args={'connect_timeout': 10}, echo=False)
        
        #limpiar tablas de historia
        print("Limpiando fecha....")
        Connection = engine.raw_connection()
        cursor = Connection.cursor()
        res = cursor.execute("Exec spLimpiarDia '" + dia +"'")
        cursor.commit()
        cursor.close()

        #cargar datos historicos desde ICG
        print("Cargando datos desde ICG....")
        dfventas = dbc.db_ventasdia(conn,dia)
        dfcompras = dbc.db_comprasdia(conn, dia)
        dfstock = dbc.db_stockdia(conn)
        
        #Insertar datos historicos
        print("Insertando datos....")
        dfcompras.to_sql(con=engine, schema="dbo", name="HISCOMPRAS", if_exists="append", index=False, chunksize=1000)
        dfventas.to_sql(con=engine, schema="dbo", name="HISVENTAS", if_exists="append", index=False, chunksize=1000)
        dfstock.to_sql(con=engine, schema="dbo", name="HISSTOCKDIARIO", if_exists="append", index=False, chunksize=5000)
    except IOError as e:
        ferror = open( pathuser + '/' + 'error.log', 'w')
        ferror.write(str(e))
        ferror.close()


## MAIN ##
if __name__ == '__main__':
    try:
        if sys.platform.startswith("linux"):  # could be "linux", "linux2", "linux3", ...
            pathuser = os.environ['HOME'] 
        elif sys.platform ==  "win32":     # Windows (either 32-bit or 64-bit)
            pathuser = os.environ['USERPROFILE'] 
        
        folderapp = os.getcwd() ##carpeta de ejecución de la app
        pathapp = folderapp + '\config.json'
        with open(pathapp, 'r') as file:
            data = json.load(file)
                
        df_config = json_normalize(data['Data'])

        dia = datetime.now()
        fechadia = dia.strftime("%Y%m%d")
    except IOError as e:
        ferror = open( pathuser + '/' + 'error.log', 'w')
        ferror.write(str(e))
        ferror.close()
    else: 
        #ejecutar principal
        
        try:
            
            print("Iniciando carga de datos historicos....")
            cargardatos(data['Data'][0]['source'], data['Data'][0]['dbsource'], data['Data'][0]['destination'], data['Data'][0]['dbdestination'], fechadia, pathuser)
        except IOError as e:
            ferror = open( pathuser + '/' + 'error.log', 'w')
            ferror.write(str(e))
            ferror.close()