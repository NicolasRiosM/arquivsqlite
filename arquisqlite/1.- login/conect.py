import psycopg2
import sqlite3

con = None
cur = None

def conexion():
    try:
        global con
        global cur
        
        con = sqlite3.connect('arqui.db')
        cur = con.cursor()
        print("Conexión con base de datos establecida")
       
    except:
        print("Error de conexión con base de datos")
    
def consultar(sqlquery):
    cur.execute(sqlquery)
    print(cur.fetchall())
    cur.close()
    con.close()

def modificar(sqlquery):
    cur.execute(sqlquery)
    conec.commit()
    cur.close()
    con.close()
def cerrar():
    try:
        cur.close()
        conec.close()
        print("Conexión con base de datos cerrada")
    except:
        print("Error al cerrar conexión")    

def llenado(largo):
    aux = str(largo)
    while len(aux) < 5:
        aux = '0' + aux
    print(aux)
    return aux

conexion()
