import socket  
from conect import *
import bcrypt
import threading
import sqlite3

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
s.bind(("127.0.0.1", 5000))
s.send(bytes('00010sinitlogin','utf-8'))
s.listen(1000)

def recibir(sock, addr):
    print("Ingresando a la cuenta de usuario")
    while True:
        datos = sock.recv(4096)
        if datos.decode('utf-8').find('login'):
            datos = datos[10:]
            target = datos.decode()
            data = target.split()          
        consulta = f"SELECT (email,pass) From usuarios"
        respuesta = consultar(consulta)
#--------------------------------------------------------------#
        i=0
        while (i<len(respuesta)):
            comp = respuesta [i][0]
            i=i+1
            mail =[]
            psw = []
            j=0
            k=0
            while (j<len(comp) and comp[j] != ","):
                mail.append(comp[j])
                k = j
                j=j+1
            mail.pop(0)
            email=''.join(mail)
            while (k<len(comp)):
                psw.append(comp[k])
                k=k+1
            psw.pop(0)
            psw.pop(0)
            psw.pop()
            password=''.join(psw)
#-------------------------VALIDANDO--------------------------#
            enchash = password.encode()
            encpass = data[1].encode()
            val=0
            if data[0] == email and bcrypt.checkpw(encpass, enchash):
                val=1
                ok='ok'
                datos = ok
                aux = llenado(len(datos))
                mensaje = aux + datos
        
                print("Ha ingresado con éxito a su cuenta")
                s.send(bytes('ok','utf-8')
                break
#--------------------------------------------------------------#
    if (val!=1):
        print("Contraseña incorrecta")
        
    s.close()
while True:
	sock, addr = s.accept()
	tarea = threading.Thread(target = recibir, args = (sock, addr))
	tarea.start()
