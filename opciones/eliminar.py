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
        
def eliminar_sucursal():
    title = """
*******************************************
* SESION DE ELIMINAR DATOS DE SUCURSALES *
*******************************************
"""
    fg.borrar_pantalla()
    print(title)
    data = abrirArchivo()
    sucursal_id = int(input("Ingrese el ID de la sucursal que deseas eliminar: "))
    
    # Buscar la sucursal por el id
    sucursal = next((item for item in data["sucursales"] if item["id"] == sucursal_id), None)
    
    if sucursal:
        data["sucursales"].remove(sucursal)
        guardarArchivo(data)
        print("Sucursal eliminada correctamente.")
    else:
        print("Sucursal no encontrada.")

eliminar_sucursal()