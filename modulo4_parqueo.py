import json
import datetime
from modulo5_datos import Espacios_Parqueo as P
from modulo5_datos import nombre_usuarios as NU

#Carga los espacios de parqueo ocupados desde el archivo JSON 'parqueo_verificado.json'.
#Actualiza la lista de espacios de parqueo con la información cargada.
#Muestra mensajes al usuario sobre el estado de la carga de datos.

def cargar_espacios_ocupados():
    print("Analizando base de datos. Actualizando los datos. Presione enter para continuar.")
    input()
    json_parqueo_verificado = "parqueo_verificado.json"
    try:
        with open(json_parqueo_verificado, "r", encoding='utf-8') as parqueo_file:
            parqueo_verificado = json.load(parqueo_file)
            print ("Se encontraron registros. Los registros han sido actualizados con éxito. Presione enter para continuar.")
            input()
    except FileNotFoundError:
        print("No hay datos de parqueos ocupados. Presione enter para continuar")
        input()
        return
    for entry in parqueo_verificado:
        for cadaparqueo in P:
            if list(cadaparqueo.keys())[0] == entry['parqueo']:
                cadaparqueo[entry['espacio']] = entry['placa']
        

#Muestra las opciones disponibles para el usuario para seleccionar un parqueo y modificar los espacios.
#Permite al usuario ingresar el número de parqueo, ver los espacios disponibles, 
#ocupar un espacio con la placa de un vehículo y actualizar el archivo JSON con la nueva información.
   

def mostrar_y_modificar_espacios():
    cargar_espacios_ocupados()
    json_parqueo_verificado = "parqueo_verificado.json"

    try:
        with open(json_parqueo_verificado, "r", encoding='utf-8') as parqueo_file:
            parqueo_verificado = json.load(parqueo_file)
    except FileNotFoundError:
        parqueo_verificado = []

    while True:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("""
        Por favor ingrese una de las siguiente opciones:
        -------------------------------
        \n""")
        print("====>1 para ingresar a Espacios_Parqueo1_Ministerio_Trabajo\n")
        print("====>2 para ingresar a Espacios_Parqueo2_Contiguo_ULACIT\n")
        print("====>3 para ingresar a Espacios_Parqueo3_Posterior_ULACIT\n")
        print("====>4 para ingresar a Espacios_Parqueo4_Falcon_Yard\n")
        print("====>5 para ingresar a Espacios_Parqueo5_Interno_ULACIT\n")
        print("====>6 para ingresar a Espacios_Parqueo6_Museo_Ninos\n")
        print("====>7 para volver al menú principal\n")
        try:
            parqueo_seleccionado= int(input())
            if parqueo_seleccionado == 7:
                break
            if parqueo_seleccionado >= 1 and parqueo_seleccionado <=6:
                parqueo = P[parqueo_seleccionado - 1]
                print("\nEspacios disponibles en el parqueo seleccionado:")
                for key, value in parqueo.items():
                    if value == "Disponible":
                        print(f"{key}: {value}")
                while True:
                    placa = input("\nIngrese la placa del vehículo para ocupar un espacio (o presione Enter para volver): ")
                    if placa.isalnum():
                        espacio_a_ocupar = input("Ingrese el espacio de parqueo que desea ocupar: ")
                        if espacio_a_ocupar in parqueo and parqueo[espacio_a_ocupar] == "Disponible":
                            parqueo[espacio_a_ocupar] = placa
                            current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            parqueo_verificado.append({
                                'fecha': current_date,
                                'parqueo': list(parqueo.keys())[0],  
                                'espacio': espacio_a_ocupar,
                                'placa': placa
                            })
                            with open(json_parqueo_verificado, "w", encoding='utf-8') as file:
                                json.dump(parqueo_verificado, file, indent=3, ensure_ascii=False)
                            print("El espacio de parqueo ha sido actualizado satisfactoriamente.Presione enter para continuar.")
                            input()
                            break
                        else:
                            print("El espacio de parqueo ingresado no está disponible o es inválido. Presione enter para continuar")
                            input()
                    elif placa == input():
                        print("Volviendo al menú principal.")
                        input()
                        break
                    else:
                        print("Opción inválida. Intente nuevamente. Presione enter para continuar")
                        input()
        except ValueError:
            print("Caracter incorrecto. Por favor ingrese el número correspondiente a la opción que desea elegir. Presione enter para continuar.")
            input()

#Permite al usuario liberar un espacio de parqueo previamente ocupado.
#Muestra las opciones disponibles para seleccionar un parqueo,
#permite al usuario seleccionar el espacio a liberar y actualiza el archivo JSON con la nueva información.
    
def liberar_espacio():
    cargar_espacios_ocupados()
    json_parqueo_verificado = "parqueo_verificado.json"

    try:
        with open(json_parqueo_verificado, "r", encoding='utf-8') as parqueo_file:
            parqueo_verificado = json.load(parqueo_file)
    except FileNotFoundError:
        print("No hay datos de parqueos ocupados.")
        return
    while True:
        print("Seleccione el parqueo del cual desea liberar un espacio:")
        print("1. Espacios_Parqueo1_Ministerio_Trabajo")
        print("2. Espacios_Parqueo2_Contiguo_ULACIT")
        print("3. Espacios_Parqueo3_Posterior_ULACIT")
        print("4. Espacios_Parqueo4_Falcon_Yard")
        print("5. Espacios_Parqueo5_Interno_ULACIT")
        print("6. Espacios_Parqueo6_Museo_Ninos")
        print("7. Volver al menú principal")

        try:
            parqueo_seleccionado = int(input())
            if parqueo_seleccionado == 7:
                break
            
            if parqueo_seleccionado >= 1 and parqueo_seleccionado <=6:
                parqueo = P[parqueo_seleccionado - 1]
                print("\nEspacios ocupados en el parqueo seleccionado:")
                for key, value in parqueo.items():
                    if value != "Disponible":
                        print(f"{key}: {value}")

                espacio_a_liberar = input("\nIngrese el espacio de parqueo que desea liberar (o presione Enter para volver): ")
                if espacio_a_liberar:
                    if espacio_a_liberar in parqueo and parqueo[espacio_a_liberar] != "Disponible":
                        placa = parqueo[espacio_a_liberar]
                        parqueo[espacio_a_liberar] = "Disponible"
                        parqueo_verificado = [entry for entry in parqueo_verificado if not (entry['parqueo'] == list(parqueo.keys())[0] and entry['espacio'] == espacio_a_liberar and entry['placa'] == placa)]
                        with open(json_parqueo_verificado, "w", encoding='utf-8') as file:
                            json.dump(parqueo_verificado, file, indent=3, ensure_ascii=False)
                        print("El espacio de parqueo ha sido liberado satisfactoriamente. Presione enter para continuar.")
                        input()
                    else:
                        print("El espacio de parqueo ingresado no está ocupado o es inválido. Presione enter para continuar.")
                        input()
                else:
                    print("Volviendo al menú principal.Presione enter para continuar.")
                    input ()
            else:
                print("Opción inválida. Presione enter para intentar nuevamente.")
                input()
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número de opción válido. Presione enter para continuar")
            input()
