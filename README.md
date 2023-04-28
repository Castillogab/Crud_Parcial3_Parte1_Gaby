# Crud_Parcial3_Parte1_Gaby
Parte 1 del parcial 3_ CRUD Fast API

-Se crea la base de datos llamada Parcial3P1_CA100522
    -Tabla llamada empleados
        CREATE TABLE empleados(
        id INT PRIMARY KEY AUTO_INCREMENT  NOT NULL,
        nombre VARCHAR (30),
        salario DECIMAL(8,2),
        categoria VARCHAR(50),
        genero VARCHAR(10),
        telefono VARCHAR(9),
        fecha datetime
        )       

Version de python 3.10.11

-se instala la libreria de fastAPI con el siguiente comando $ pip install fastapi

-Se instala el servidor que nos ayudara a levartar el servicio $ pip install "uvicorn[standard]"

-Se crea un archivo main.py
    -Crear un modelo de la tabla empleados
    -Conexión con la BD
    -Se agrega instancia de FastAPI
    -Definición de ednpoint
    -Endpoint para obtener todos los empleados
    -Endpoint para obtener un  empleado
    -Endpoint para actualizar datos del empleado
    -Endpoint para el registro de un empleado
    -Endpoint para eliminar un empleado

-Nota:Verificar qque la libreria pip este actualizada a la ultima version; si no esta actualizada usar el siguiente comando: $ pip install --upgrade pip

-Se instala el conector de mysql $ pip install mysql-connector-python

-Se instala el inicio del servidor con el siguiente comando: $ uvicorn main:app --reload

