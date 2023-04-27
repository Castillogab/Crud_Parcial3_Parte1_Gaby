CREATE DATABASE Parcial3P1_CA100522
USE Parcial3P1_CA100522

CREATE TABLE empleados(
id INT PRIMARY KEY AUTO_INCREMENT  NOT NULL,
nombre VARCHAR (30),
salario DECIMAL(8,2),
categoria VARCHAR(50),
genero VARCHAR(10),
telefono VARCHAR(9),
fecha datetime
)

INSERT INTO empleados(nombre, salario, categoria, genero, telefono, fecha)
VALUES ('Gaby', 300, 'Programador', 'F', '7912-1212', NOW());

Select * from empleados