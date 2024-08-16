import funciones.globales as fg

def Mainmenu():
    title = """
********************************
* MENU PRINCIPAL DE SUCURSALES *
********************************
"""
    while True:
        
        print(title)
        mainmenuop= "1. Registrar \n2. Editar \n3. Eliminar \n4. Visualización de sucursales \n5. Salir"
        print(mainmenuop)
        try:
            opcion = int(input(':) '))
        except ValueError:
            print("Error en la opcion ingresada. Por favor, ingrese un número válido.")
            fg.pausar_pantalla()
            continue
    
        match (opcion):
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                print("Vuelva pronto...")
                break
            case _:
                print('Esta opción no se encuentra dentro de las indicativos del Menú')
                fg.pausar_pantalla()
Mainmenu()