CREATE DATABASE registro_empleados;
USE registro_empleados;

CREATE TABLE registroDatos (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR (100) NOT NULL,
apellidoPaterno VARCHAR (50) NOT NULL,
apellidoMaterno VARCHAR (50) NOT NULL,
edad INT NOT NULL,
lugarNacimiento VARCHAR (60) NOT NULL,
email VARCHAR (255) NOT NULL,
foto VARCHAR (5000) NOT NULL
);
SELECT * FROM registroDatos;

INSERT INTO registroDatos (nombre, apellidoPaterno, apellidoMaterno, edad, lugarNacimiento, email, foto) VALUES ("Jesús Adrián", "Alcocer", "Dóñez", 23, "Monterrey", "jadrianaldo@outlook.com", "foto.png" );