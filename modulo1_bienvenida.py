# Función para mostrar un mensaje de bienvenida

def msgBienvenida():
    bienvenida = """
********************************************
*                                          *
*       Bienvenido al Sistema de           *
*        Gestión de Vehículos de           *
*                ULACIT                    *
*                                          *
********************************************
"""
    return bienvenida
print(msgBienvenida())
input()

# Función que muestra un menú de opciones y obtiene la elección del usuario

def msgOpcionEntradaoSalida():
    try:
        print("""
        Por favor ingrese una de las siguiente opciones:
        -------------------------------
        \n""")
        print("====>1 para verificar estado del vehiculo\n")
        print("====>2 para ver, mostrar y modificar parqueos disponibles\n")
        print("====>3 para liberar espacio de parqueos\n")
        print("====>4 para salir de el sistema\n")
        opcion = int(input())
        return opcion
    except ValueError:
        print("Caracter inválido, solo debe digitar el número correspondiente a la opción elegida. Ingrese enter para continuar.")
        input()

# Función que genera y devuelve un mensaje de despedida

def msgDespedida():
    despedida = "*****El sistema se ha cerrado satisfactoriamente.*****"
    return despedida