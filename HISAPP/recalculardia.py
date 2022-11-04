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
        connext = 'mssql+pyodbc://novelty_reportes:novelty2020@' + source + '/' + dbdata + '?driver=SQL+Server+Native+Client+11.0'
        engineExt = sa.create_engine(connext, connect_args={'connect_timeout': 10}, echo=False)
        sql_df = pd.read_sql("exec spDiaRecalculo '" + dia +"'", con=engineExt)

        #Agregar datos
        print("Insertando datos del día....")
        sql_df.to_sql(con=engineExt, schema="dbo", name="DiaRecalculo", if_exists="replace", index=False, chunksize=1000)

        #conexion local
        connstring = 'mssql+pyodbc://nwduser:nwduser@'  + destination + '/' + dbdestination + '?driver=SQL+Server+Native+Client+11.0'
        engine = sa.create_engine(connstring, connect_args={'connect_timeout': 10}, echo=False)
        
        #Comparar datos
        print("Recalculando día....")
        sql_rec = pd.read_sql("exec spUpdHisVentas '" + dia +"'", con=engine)
        
        fsucces = open( pathuser + '/' + 'succes.log', 'w')
        fsucces.write(str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " - Datos cargados correctamente, recalculo del día : " + dia)
        fsucces.close()

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
            
            cargardatos(data['Data'][0]['source'], data['Data'][0]['dbsource'], data['Data'][0]['destination'], data['Data'][0]['dbdestination'], fechadia, pathuser)
        except IOError as e:
            ferror = open( pathuser + '/' + 'error.log', 'w')
            ferror.write(str(e))
            ferror.close()