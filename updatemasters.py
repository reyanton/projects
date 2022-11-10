import pyodbc 
import pandas as pd

file_csv = None
data_sql = None

def readcsv():
    global file_csv
    file_csv = pd.read_csv (r'C:\Proyectos\ExcelContab\conceptos.csv')
    #print(file_csv)


def connectSql():
    global data_sql    
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=ING-ICG5;'
                        'Database=contabilidad;'
                        'Trusted_Connection=yes;')
    squery = pd.read_sql_query('''Select id, descripcion, tipo, cuenta_num, calculo_patronal, cardinalidad, visible from conceptos''',  conn)
    data_sql = pd.DataFrame(squery, columns=['id','descripcion', 'tipo', 'cuenta_num', 'calculo_patronal', 'cardinalidad', 'visible'])
    conn.close()

def insdatasql():
    global ins    
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=ING-ICG5;'
                        'Database=contabilidad;'
                        'Trusted_Connection=yes;')
    cursor = conn.cursor()

    for index, row in ins.iterrows():
        cursor.execute("insert into conceptos(id, descripcion, tipo, cuenta_num, calculo_patronal, cardinalidad, visible) values(?, ?, ?, ?, ?, ?, ?)",
                        row['id'], row['descripcion_x'], row['tipo_x'], row['cuenta_num_x'], row['calculo_patronal_x'], row['cardinalidad_x'],row['visible_x'])                       
        #print(row['id'], row['descripcion_x'], row['tipo_x'], row['cuenta_num_x'], row['calculo_patronal_x'], row['cardinalidad_x'],row['visible_x'])
        conn.commit()
        
    cursor.execute("select * from conceptos")
    print(cursor.fetchall())
    cursor.close()
    conn.close()



readcsv()
connectSql()

ins = (file_csv.merge(data_sql, on='id', how='left', indicator=True)
     .query('_merge == "left_only"')
     .drop('_merge', 1))

insdatasql()
