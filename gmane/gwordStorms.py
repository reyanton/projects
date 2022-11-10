import sqlite3
import time
import string

conn = sqlite3.connect('storms.sqlite')
cur = conn.cursor()

cur.execute('SELECT name, count FROM StormsNames')
storms = dict()
for message_row in cur :
    storms[message_row[0]] = message_row[1]

x = sorted(storms, key=storms.get, reverse=True)
highest = None
lowest = None

#print(x)
for k in x[:100]:
    if highest is None or highest < storms[k] :
        highest = storms[k]
    if lowest is None or lowest > storms[k] :
        lowest = storms[k]
print('Range of storms:',highest,lowest)

# # Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

fhand = open('gwordst.js','w')
fhand.write("gword = [")
first = True
for k in x[:100]:
    if not first : fhand.write( ",\n")
    first = False
    size = storms[k]
    size = (size - lowest) / float(highest - lowest)
    size = int((size * bigsize) + smallsize)
    fhand.write("{text: '"+k+"', size: "+str(size)+"}")
fhand.write( "\n];\n")
fhand.close()

# print("Output written to gword.js")
# print("Open gword.htm in a browser to see the vizualization")
