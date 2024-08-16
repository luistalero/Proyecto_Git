import json
import os
import funciones.globales as fg

def abrirArchivo():
    if os.path.exists("info.json"):
        with open("info.json", encoding="utf-8") as file:
            return json.load(file)
    else:
        return {"sucursales": []}

def mostrar_sucursales(filtro_nombre=None, filtro_estado=None):
    title= """
************************************
* SESION DE VISUALIZACIÓN DE LISTA *
************************************
"""
    fg.borrar_pantalla
    print(title)
    data = abrirArchivo()
    sucursales = data["sucursales"]
    
    if filtro_nombre:
        sucursales = [sucursal for sucursal in sucursales if filtro_nombre.lower() in sucursal["nombre"].lower()]
    
    if filtro_estado:
        sucursales = [sucursal for sucursal in sucursales if filtro_estado.lower() in sucursal.get("estado", "").lower()]
    
    if sucursales:
        for sucursal in sucursales:
            print(f"ID: {sucursal['id']}")
            print(f"Nombre: {sucursal['nombre']}")
            print(f"Dirección: {sucursal['direccion']}")
            print(f"Teléfono: {sucursal['telefono']}")
            print(f"Celular: {sucursal['celular']}")
            print(f"Correo: {sucursal['correo']}")
            print(f"Estado: {sucursal.get('estado', 'No disponible')}")
            print("-" * 20) #Para imprimir una línea de separación
    else:
        print("No se encontraron sucursales con los filtros aplicados.")

filtro_nombre = input("Ingrese el nombre para filtrar (deje vacío si no desea filtrar por nombre): ")
filtro_estado = input("Ingrese el estado para filtrar (deje vacío si no desea filtrar por estado): ")
mostrar_sucursales(filtro_nombre, filtro_estado)
