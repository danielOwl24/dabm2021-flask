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

def verificar(usuario, resultado):
    pass        



if __name__ == "__main__":
    app.run(debug = True)
