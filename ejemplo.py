# coding= UTF-8
from flask import Flask, render_template, request
import os
import random
rangos = []

class sensorTemp:
    def __init__(self, baja, normal, alta):
        self.baja = baja
        self.normal = normal
        self.alta = alta
        self._file = os.path.join(os.path.dirname(__file__), "bd/parametros.csv")
    
        
    def saveToFile(self):   
        """Esta función crea un archivo csv y añade los pacientes que se creen 
        al archivo pacientes.csv"""
        file = open(self._file, "w")
        datos = "Hipotermia" + ";" + str(self.baja[0]) + ";" + str(self.baja[1]) + "\n" + "Normal" + ";" + str(self.normal[0]) + ";" + str(self.normal[1]) + "\n" + "Fiebre" + ";" + str(self.alta[0]) + ";" + str(self.alta[1]) + "\n"
        file.write(datos)
        file.close()   


app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('login.html')

#@app.route('/datos')
#def datos():
#    user = {'nombre' : 'david'}
#    return render_template('datos.html', title = 'Titulo personalizado', user = user)



@app.route('/validar', methods = ["POST"])
def validar():
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]
        
        resultado = verificar(usuario, password)
        if resultado == True:
            return render_template("menu.html", title = "Sistema DABM")  
        else: 
            return render_template("login.html", title = "Sistema DABM", resultado = resultado)       
        
           

@app.route('/monitor')
def monitor():
    datos = getDatos()
    lectura = random.randint(0,45)
    color = 0
    if lectura >= int(datos[0][1]) and lectura <= int(datos[0][2]):
        color = 1
    if lectura >= int(datos[1][1]) and lectura <= int(datos[1][2]):
        color = 2
    if lectura >= int(datos[2][1]) and lectura <= int(datos[2][2]):
        color = 3

    return render_template("monitor.html", datos = datos, lectura = lectura, color = color)



@app.route('/config', methods = ["GET","POST"])    
def config():
    baja = [0,0]
    normal = [0,0]
    alta = [0,0]
    if request.method == "POST":
        baja[0] = request.form["bajoMin"]
        baja[1] = request.form["bajoMax"]
        normal[0] = request.form["normalMin"]
        normal[1] = request.form["normalMax"]
        alta[0] = request.form["altoMin"]
        alta[1] = request.form["altoMax"]
        s = sensorTemp(baja, normal, alta)
        s.saveToFile()
        rangos.append(s)  
    return render_template("config.html")

    
def getDatos():
    directorio = os.path.dirname(__file__)
    nombreArchivo = "bd/parametros.csv"
    ruta = os.path.join(directorio, nombreArchivo)

    f = open(ruta, "r")
    lineas = f.readlines()
    f.close()

    datos = []
    for l in lineas:
        l = l.replace("\n","")
        l = l.split(";")
        datos.append(l)
    return datos    
           

def verificar(usuario, password):
    directorio = os.path.dirname(__file__)
    nombreArchivo = "bd/users.csv"
    ruta = os.path.join(directorio, nombreArchivo)

    f = open(ruta, "r")
    lineas = f.readlines()
    f.close()
    datos = []
    for l in lineas:
        l = l.replace("\n","")
        l = l.split(";")
        datos.append(l)  
        if (usuario in l) and (password in l):
            return True
    return False       
  
    

if __name__ == "__main__":
    app.run(debug = True)
