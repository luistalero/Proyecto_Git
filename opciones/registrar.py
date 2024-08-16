import json
import os
import funciones.globales as fg

def abrirArchivo():
    if os.path.exists("info.json"):
        with open("info.json", encoding="utf-8") as file:
            return json.load(file)
    else:
        return {"sucursales": []}

def guardarArchivo(data):
    with open("info.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def registro_sucursal():
    title= """
************************************
* SESION DE REGISTRO DE SUCURSALES *
************************************
"""
    fg.borrar_pantalla
    print(title)
    sucursal = abrirArchivo()
    id = int(input("Ingrese el ID del gerente o responsable: "))
    nombre = input("Ingrese el nombre de la Sucursal: ")
    direccion = input("Ingrese la dirección de la sucursal: ")
    telefono = input("Ingrese el número de teléfono: ")
    celular = input("Ingrese el número de celular: ")
    correo = input("Ingrese el correo: ")

    sucursal["sucursales"].append(
        {
            "id": id,
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "celular": celular,
            "correo": correo
        }
    )

    guardarArchivo(sucursal)

registro_sucursal()
