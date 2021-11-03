# coding= UTF-8
from flask import Flask, render_template, request


app = Flask(__name__)
@app.route('/')

def inicio():
    return render_template('login.html')

@app.route('/datos')
def datos():
    user = {'nombre' : 'david'}
    return render_template('datos.html', title = 'Titulo personalizado', user = user)



@app.route('/validar', methods = ["POST"])
def validar():
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]
        
        resultado = verificar(usuario, password)
        """ if resultado == True:
            return "Bienvenido" """
    return render_template("menu.html", title = "Sistema DABM")        


def verificar(usuario, password):
    pass
    return True
"""     file = open("C:/Users/USUARIO/OneDrive/Documents/DABM/Codigos/flask/bd/users.csv", "r")
    datosArchivo = file.readlines()        
    file.close()

    for dato in datosArchivo:
        usuarioR, passwordR = dato.split(";")
        if usuario == usuarioR and password == passwordR:
            return True
        else:
            return False     """
    




if __name__ == "__main__":
    app.run(debug = True)
