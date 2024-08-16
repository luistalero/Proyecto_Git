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

def modificar_sucursal():
    title= """
*******************************************
* SESION DE MODIFICAR DATOS DE SUCURSALES *
*******************************************
"""
    fg.borrar_pantalla
    print(title)
    data = abrirArchivo()
    sucursal_id = int(input("Ingrese el ID del usuario que deseas modificar: "))
    
    #Buscar la sucursal por el id
    sucursal = next((item for item in data["sucursales"] if item["id"] == sucursal_id), None)
    
    if sucursal:
        print("Selecciona el dato que deseas modificar del usuario: ")
        print("1. Nombre")
        print("2. Dirección")
        print("3. Teléfono")
        print("4. Celular")
        print("5. Correo")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            sucursal["nombre"] = input("Ingrese el nuevo nombre para la sucursal: ")
        elif opcion == "2":
            sucursal["direccion"] = input("Ingrese la nueva dirección para la sucursal: ")
        elif opcion == "3":
            sucursal["telefono"] = input("Ingrese el nuevo número de teléfono para la sucursal: ")
        elif opcion == "4":
            sucursal["celular"] = input("Ingrese el nuevo número celular para la sucursal: ")
        elif opcion == "5":
            sucursal["correo"] = input("Ingrese el nuevo correo para la sucursal: ")
        else:
            print("Opción inválida")
        
        guardarArchivo(data)
        print("Datos actualizados correctamente.")
    else:
        print("Sucursal no encontrada.")


modificar_sucursal()
