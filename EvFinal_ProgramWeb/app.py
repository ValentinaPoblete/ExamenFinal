from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        resultado = ''
        nombre = str(request.form['nombre'])
        edad = float(request.form['edad'])
        cantTarros = float(request.form['cantTarros'])
        if edad >= 18 or edad <= 30:
            resultado = (cantTarros * 9000) * 0.85
        elif edad > 30:
            resultado = (cantTarros * 9000) * 0.75
        else:
            resultado = cantTarros * 9000
        return render_template('ejercicio1.html', resultado=resultado, cantTarros=cantTarros,
                               precioTarro=9000, nombre=nombre)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        resultado_usuario = ''
        usuario = str(request.form['usuario'])
        contrasenia = str(request.form['contrasenia'])
        if usuario == "juan" and contrasenia == "admin":
            resultado_usuario = "Bienvenido administrador juan"
        elif usuario == "pepe" and contrasenia == "user":
            resultado_usuario = "Bienvenido usuario pepe"
        else:
            resultado_usuario = "Usuario o contraseña incorrectos"
        return render_template('ejercicio2.html', resultado=resultado_usuario)
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)