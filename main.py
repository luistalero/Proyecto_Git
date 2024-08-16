import funciones.globales as fg
import opciones.registrar as r
import opciones.editar as m
import opciones.eliminar as e

def Mainmenu(op):
    title = """
********************************
* MENU PRINCIPAL DE SUCURSALES *
********************************
"""
    fg.borrar_pantalla()
    mainmenuop= "1. Registrar \n2. Editar \n3. Eliminar \n4. Visualización de sucursales \n5. Salir"
    if(op != 4):
        print(title)
        print(mainmenuop)
        try:
            opcion = int(input(':) '))
        except ValueError:
            print("Error en la opcion ingresada. Por favor, ingrese un número válido.")
            fg.pausar_pantalla()
            Mainmenu(0)
        else:
            match (opcion):
                case 1:
                    r.registro_sucursal(1)
                case 2:
                    m.modificar_sucursal(0)
                case 3:
                    e.eliminar_sucursal(0)
                case 4:
                    pass
                case 5:
                    print("Vuelva pronto...")
                case _:
                    print('Esta opción no se encuentra dentro de las indicativos del Menú')
                    fg.pausar_pantalla()
                    Mainmenu(0)
Mainmenu(0) 