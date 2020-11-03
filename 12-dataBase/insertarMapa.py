import sqlite3 
import sys #para el manejo de errores
#nos conectamos  a la db
conn=sqlite3.connect("test.db")

#creamos el manejador(handler)
cursor=conn.cursor()

#realizamos la consulta sql
query = ('INSERT INTO STUDIANTES (ID,NOMBRE,GRADO,DIRECCION,CLASE) '
        'VALUES (:ID, :NOMBRE, :GRADO, :DIRECCION, :CLASE);')

params = {
        'ID': 3,
        'NOMBRE': 'Ana',
        'GRADO': '003',
        'DIRECCION': 'La Paz',
        'CLASE': 'Primero'
    }


#ejecutamos la consulta
try:
    conn.execute(query, params)
except :
    e = sys.exc_info()[0] #para manejar todos los errores
    print('error en la consulta',e)
    exit()
#guardamos los cambios
conn.commit()
conn.close()
