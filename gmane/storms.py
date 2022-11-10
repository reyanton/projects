import sqlite3
import pandas as pd

conn = sqlite3.connect('storms.sqlite')
cur = conn.cursor()
cur_st = conn.cursor()
cur_stn = conn.cursor()
cur_sty = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Storms ''')
cur.execute('''DROP TABLE IF EXISTS StormsNames ''')
cur.execute('''DROP TABLE IF EXISTS StormsYears ''')

cur.execute('''CREATE TABLE IF NOT EXISTS StormsNames
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE, last_year INTEGER, count INTEGER DEFAULT 1)''')

cur.execute('''CREATE TABLE IF NOT EXISTS StormsYears
    (id INTEGER PRIMARY KEY, year INTEGER UNIQUE, last_name TEXT, count INTEGER DEFAULT 1)''')

		
df = pd.read_csv('storms.csv')
df = df[(df.category >= 0) & (df.year >= 1980)]
df.to_sql("Storms", conn)

cur_st.execute('''SELECT name, year FROM Storms''')

#count storms names
id_storm = 1
for name in cur_st:
    storm_name = name[0]
    storm_year = name[1]

    cur_stn.execute('''SELECT id, last_year, count FROM StormsNames where name = ?''', (str(storm_name), ))
    id_st = cur_stn.fetchone()

    if id_st is None:
        
        cur_stn.execute('''INSERT OR IGNORE INTO StormsNames (id, name, last_year) VALUES ( ?, ?, ? )''', (id_storm, str(storm_name), storm_year) )
        conn.commit()
        id_storm += 1
    else:
        # print('update : ', id_st[0])
        cur_stn.execute('''UPDATE StormsNames SET count = count + 1, last_year = ? where id = ? and last_year <> ?''', (storm_year, id_st[0], storm_year) )
        conn.commit()

cur_st.execute('''SELECT name, year FROM Storms''')
#count storms x years
id_storm = 1
for name in cur_st:
    storm_name = name[0]
    storm_year = name[1]

    cur_sty.execute('''SELECT id, year, count FROM StormsYears where year = ?''', (storm_year, ))
    id_st = cur_sty.fetchone()

    if id_st is None:
        
        cur_stn.execute('''INSERT OR IGNORE INTO StormsYears (id, year, last_name) VALUES ( ?, ?, ? )''', (id_storm, storm_year, str(storm_name)) )
        conn.commit()
        id_storm += 1
    else:
        # print('update : ', id_st[0])
        cur_stn.execute('''UPDATE StormsYears SET count = count + 1, last_name = ? where id = ? and last_name <> ?''', (str(storm_name), id_st[0], str(storm_name)) )
        conn.commit()