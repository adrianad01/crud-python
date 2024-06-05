from flask import Flask, render_template, request
import mysql.connector # type: ignore

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    'user': 'root',
    'password': 'YTsFDJaMfO0zJakbd9PJx0UEfBfotoU3neTCwpuWuZeCvWChwWKbU6yK65zRaVCw',
    'host': 'localhost',
    'database': 'registro_empleados'
}

@app.route('/')
def index():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    sql = '''INSERT INTO registroDatos (nombre, apellidoPaterno, apellidoMaterno, edad, lugarNacimiento, email, foto) 
             VALUES ("Jesús Adrián", "Alcocer", "Dóñez", 23, "Monterrey", "jadrianalcocer11@gmail.com", "foto.png");'''
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()

    return render_template('registroEmpleados/index.html')


@app.route('/create')
def create():
    return render_template('registroEmpleados/create.html')

@app.route('/data', methods=['POST'])
def storage():

    _nombre=request.form['txtNombre']
    _apellidoPaterno=request.form['txtApellidoPaterno']
    _apellidoMaterno=request.form['txtApellidoMaterno']
    _edad=request.form['txtEdad']
    _lugarNacimiento=request.form['txtLugarNacimiento']
    _email=request.form['txtEmail']
    _foto=request.files['txtFoto']


    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    sql = '''INSERT INTO registroDatos (nombre, apellidoPaterno, apellidoMaterno, edad, lugarNacimiento, email, foto) 
             VALUES (%s, %s, %s, %s, %s, %s, %s);'''
    datos = (_nombre, _apellidoPaterno, _apellidoMaterno, _edad, _lugarNacimiento, _email, _foto.filename)
    cursor.execute(sql,datos)
    connection.commit()
    cursor.close()
    connection.close()

    return render_template('registroEmpleados/index.html')
    


if __name__ == '__main__':
    app.run(debug=True)
