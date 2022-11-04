import pandas as pd
import pyodbc 


def db_connect(servername, dbname, username, passuser):
    try:
        conn = pyodbc.connect('Driver={SQL Server}; Server=' + servername + ';Database=' + dbname + ';UID=' + username + ';PWD=' + passuser + ';')

        return(conn)    
    except Exception as e:
        print("Ocurrió un error al conectar a SQL Server: ", e)

    
def db_stockdia(conn):
    try:
        df = pd.read_sql_query("exec spCargarHistoricoDiario", conn)
        
        return(df)
    except Exception as e:
        print("Ocurrió un error al consultar Stock: ", e)


def db_ventasdia(conn, dia):
    try:
        df = pd.read_sql_query("exec spCargarHistoricoVentas '" + dia + "'", conn)
        
        return(df)
    except Exception as e:
        print("Ocurrió un error al consultar Ventas: ", e)


def db_comprasdia(conn, dia):
    try:
        df = pd.read_sql_query("exec spCargarHistoricoCompras '" + dia + "'", conn)
        
        return(df)
    except Exception as e:
        print("Ocurrió un error al consultar Compras: ", e)

