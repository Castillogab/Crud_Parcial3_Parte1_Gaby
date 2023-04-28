import mysql.connector
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
from datetime import date
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html

# Declaración de modelo de la tabla de la base de datos
class empleados(BaseModel):
    id: int | None = None
    nombre: str
    salario: int
    categoria: str
    genero: str
    telefono: str
    fecha: str | None = None

# Conexión a la base de datos Parcial3P1_CA100522
conect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Parcial3P1_CA100522"
)

# Instancia de FastAPI, levanta la API en local
app = FastAPI()

# recolecta info de los endpoint /
@app.get("/openapi.json")
async def get_open_api_endpoint():
    return JSONResponse(get_openapi(title="Api Parcial 3 Gaby", version="0.0.2", routes=app.routes))

@app.get("/docs2", include_in_schema=False)
async def get_documentation():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Document")

# Endpoint para obtener todos los empleados
@app.get("/empleado")
async def getEmpleados():
    cursor = conect.cursor()
    query="select * from empleados;"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close
    # Realiza un mapeo de los datos recolectados
    # lambda
    response = list(map(lambda data: {
    "id": data[0],
    "nombre": data[1],
    "salario": str(data[2]),
    "categoria": data[3],
    "genero": data[4],
    "telefono": data[5],
    "fecha":str(data[6])
    }, result))
    return JSONResponse(content=response)

# Endpoint para obtener un  empleado
@app.get("/empleado/{id}")
async def getEmpleado(id: int):
    cursor = conect.cursor()
    query="select * from empleados where id = %s;"
    cursor.execute(query,(id,))
    result = cursor.fetchone()
    cursor.close
    if result is None:
        return JSONResponse(status_code=404, content={"mensaje": "Empleado no encontrado"})
    else:
        response = {
        "id": result[0],
        "nombre": result[1],
        "salario": str(result[2]),
        "categoria": result[3],
        "genero": result[4],
        "telefono": result[5],
        "fecha":str(result[6])
        }
    return JSONResponse(content=response)

# Endpoint para actualizar datos del empleado
@app.put("/empleado/{id}")
async def putEmpleado(id: int, body :empleados):
    cursor = conect.cursor()
    response = { **body.dict() }
    response.update({"id":id})
    today = date.today()
    sql = "UPDATE empleados SET nombre = %s, salario = %s, categoria = %s, genero = %s, telefono = %s, fecha = %s  WHERE id = %s"
    values = (body.nombre,body.salario,body.categoria,body.genero,body.telefono,today,id)
    cursor.execute(sql,values)
    conect.commit()
    cursor.close()
    return JSONResponse(content={"mensaje": f"El empleado con id {id} se ha actualizado"})

# Endpoint para el registro de un empleado
@app.post("/empleado")
async def postEmpleado(body:empleados):
    cursor = conect.cursor()
    today = date.today()   
    sql = "INSERT INTO empleados (nombre, salario, categoria, genero, telefono, fecha) VALUES(%s, %s, %s, %s, %s, %s)"
    values = (body.nombre, body.salario, body.categoria, body.genero, body.telefono, today)
    cursor.execute(sql,values)
    conect.commit()
    cursor.close()
    return JSONResponse(content={"mensaje": f"El empleado se ha registrado con éxito"})

# Endpoint para eliminar un empleado
@app.delete("/empleado/{id}")
async def deteleEmpleado(id : int):  
    cursor = conect.cursor()
    sql = "delete from empleados where id = %s;"
    cursor.execute(sql,(id,))
    conect.commit()
    cursor.close()
    return JSONResponse(content={"mensaje": f"El empleado ha sido eliminado"})