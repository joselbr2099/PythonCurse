import sqlite3
import sys

#nos conectamos  a la db
conn=sqlite3.connect("test.db")

#creamos el manejador(handler)
cursor=conn.cursor()

#iniciamos la captura de errores
try:
    #realizamos la consulta
    conn.execute("DELETE from STUDIANTES where ID = 2;")
    
except :
    e = sys.exc_info()[0] #para manejar todos los errores
    print('error en la consulta',e)
    exit()

#si todo esta bien mostramos los resultados de la consulta
cursor = conn.execute("SELECT * from STUDIANTES")
print(cursor.fetchall())

#guardamos los cambios
conn.commit()
conn.close()

