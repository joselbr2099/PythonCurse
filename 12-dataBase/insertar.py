import sys
import sqlite3

#nos conectamos  a la db
conn=sqlite3.connect("test.db")

#creamos el manejador(handler)
cursor=conn.cursor()

try:
    #realizamos la consulta sql
    conn.execute("INSERT INTO STUDIANTES (ID,NOMBRE,GRADO,DIRECCION,CLASE) "
                "VALUES (1, 'Jose', '001', 'La Paz', 'primero')")
except:
    e = sys.exc_info()[0] #para manejar todos los errores
    print('erroral crear la db',e)
    exit()

try:
    #realizamos la consulta sql
    conn.execute("INSERT INTO STUDIANTES (ID,NOMBRE,GRADO,DIRECCION,CLASE) "
                "VALUES (2, 'Aaron', '002', 'La Paz', 'primero')")
except:
    e = sys.exc_info()[0] #para manejar todos los errores
    print('erroral crear la db',e)
    exit()

#guardamos los cambios
conn.commit()
conn.close()
