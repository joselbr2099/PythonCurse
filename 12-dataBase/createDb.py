import sqlite3
import sys

#creamos  una base de datos
dbFile="test.db"#iniciamos la captura de errores
#si la db existe la usa de lo  contrario la usa

try:
    conn=sqlite3.connect(dbFile)
#si hay algun error mostramos un mensaje y  terminamos  el programa
except:
    e = sys.exc_info()[0] #para manejar todos los errores
    print('erroral crear la db',e)
    exit()


