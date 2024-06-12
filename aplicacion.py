from flask import Flask, render_template, request, redirect
import mysql.connector # type: ignore
from datetime import datetime

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
    cursor.execute("SELECT * FROM registroDatos;")
    registroDatos = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('registroEmpleados/index.html', registroDatos=registroDatos)

@app.route('/destroy/<int:id>')
def destroy(id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM registroDatos WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM registroDatos WHERE id = %s", (id,))
    registroDatos = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('registroEmpleados/edit.html', registroDatos=registroDatos)

@app.route('/update', methods=['POST'])
def update():
    _nombre = request.form['txtNombre']
    _apellidoPaterno = request.form['txtApellidoPaterno']
    _apellidoMaterno = request.form['txtApellidoMaterno']
    _edad = request.form['txtEdad']
    _lugarNacimiento = request.form['txtLugarNacimiento']
    _email = request.form['txtEmail']
    id = request.form['txtID']

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    sql = '''UPDATE registroDatos SET 
             nombre=%s, apellidoPaterno=%s, apellidoMaterno=%s, edad=%s, 
             lugarNacimiento=%s, email=%s WHERE id=%s;'''
    datos = (_nombre, _apellidoPaterno, _apellidoMaterno, _edad, _lugarNacimiento, _email, id)

    cursor.execute(sql, datos)
    connection.commit()
    cursor.close()
    connection.close()
    return redirect('/')

@app.route('/create')
def create():
    return render_template('registroEmpleados/create.html')

@app.route('/data', methods=['POST'])
def storage():
    _nombre = request.form['txtNombre']
    _apellidoPaterno = request.form['txtApellidoPaterno']
    _apellidoMaterno = request.form['txtApellidoMaterno']
    _edad = request.form['txtEdad']
    _lugarNacimiento = request.form['txtLugarNacimiento']
    _email = request.form['txtEmail']

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    sql = '''INSERT INTO registroDatos 
             (nombre, apellidoPaterno, apellidoMaterno, edad, lugarNacimiento, email) 
             VALUES (%s, %s, %s, %s, %s, %s);'''
    datos = (_nombre, _apellidoPaterno, _apellidoMaterno, _edad, _lugarNacimiento, _email)
    cursor.execute(sql, datos)
    connection.commit()
    cursor.close()
    connection.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
