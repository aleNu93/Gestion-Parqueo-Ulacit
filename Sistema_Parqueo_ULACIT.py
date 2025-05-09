import modulo1_bienvenida as bienvenida
import modulo2_administracion as administracion
import modulo3_vehiculo as vehiculo
import modulo4_parqueo as parqueo


# Muestra el mensaje de bienvenida, gestiona la autenticación del usuario y proporciona un menú para
#verificar vehículos, modificar espacios de parqueo y liberar espacios. 
#Termina cuando el usuario selecciona la opción de despedida.

def modulo_gestion_vehiculos():
    bienvenida.msgBienvenida()
    administracion.modulo_administracion()
    while True:
        opcion = bienvenida.msgOpcionEntradaoSalida()
        if opcion == 1:
            vehiculo.verificar_vehiculo()
        elif opcion == 2:
            parqueo.mostrar_y_modificar_espacios()
        elif opcion == 3:
            parqueo.liberar_espacio()
        elif opcion == 4:
            print(bienvenida.msgDespedida())
            break
        else:
            print("Opción inválida. Intente nuevamente. Presione enter para continuar")
            input()

modulo_gestion_vehiculos()