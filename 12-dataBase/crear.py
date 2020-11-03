import sqlite3
import sys

#nos conectamos  a la db
conn=sqlite3.connect("test.db")

#creamos el manejador(handler)
cursor=conn.cursor()

try:
    #realizamos la consulta
    cursor.execute("DROP TABLE IF EXISTS ESTUDIANTES")

#si hay algun error mostramos un mensaje y  terminamos  el programa
except:
    e = sys.exc_info()[0] #para manejar todos los errores
    print('error al crear la tabla',e)
    exit()


#realizamos la consulta
query="""CREATE TABLE STUDIANTES(
        ID INT PRIMARY KEY NOT NULL,
        NOMBRE CHAR(20) NOT NULL, 
        GRADO CHAR(20), 
        DIRECCION CHAR(50), 
        CLASE CHAR(20) )"""

try:
    #ejecutamos la consulta
    cursor.execute(query)
#si hay algun error mostramos un mensaje y  terminamos  el programa
except:
    e = sys.exc_info()[0] #para manejar todos los errores
    print('error al crear campos',e)
    exit()



#guardamos los cambios
conn.commit()
conn.close()
