import datetime
import json
import re
from modulo5_datos import vehiculos
from modulo5_datos import nombre_usuarios

#Verifica la información del vehículo asociado a un usuario basado en el número de cédula proporcionado.
#Si el usuario no está registrado, permite registrar un nuevo visitante con la placa del vehículo.
#Actualiza y guarda la información en archivos JSON correspondientes.
  

def verificar_vehiculo():
    json_vehiculo_verificado = "vehiculo_verificado.json"
    json_agregar_visitantes = "visitante_verificado.json"

    try:
        with open(json_vehiculo_verificado, "r", encoding='utf-8') as vehiculo_file:
            vehiculo_verificado = json.load(vehiculo_file)
    except FileNotFoundError:
        vehiculo_verificado = []

    try:
        with open(json_agregar_visitantes, "r", encoding='utf-8') as visitantes_file:
            agregar_visitantes = json.load(visitantes_file)
    except FileNotFoundError:
        agregar_visitantes = []

    while True:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            usuario = int(input("Ingrese el número de cédula del usuario asociado a la placa: "))
            usuario_encontrado = None
            for informacion_usuario in nombre_usuarios:
                if informacion_usuario["Cédula"] == usuario:
                    usuario_encontrado = informacion_usuario
                    break

            if usuario_encontrado:
                print("Bienvenido", usuario_encontrado['Nombre'], "la placa registrada es:", usuario_encontrado["Placa"])
                placa_encontrada = None
                for vehiculo in vehiculos:
                    if vehiculo["Placa"] == usuario_encontrado["Placa"]:
                        placa_encontrada = vehiculo
                        break
                if placa_encontrada:
                    print("Los datos asociados a dicha placa son:\n")
                    print("Tipo de vehículo:", placa_encontrada["tipo"], "\n")
                    print("Marca:", placa_encontrada["marca"], "\n")
                    print("Modelo:", placa_encontrada["modelo"], "\n")
                    print("Tiene marchamo:", placa_encontrada["Marchamo"], "\n")
                    placa_encontrada_json = {
                        'fecha': current_date,
                        'nombre': usuario_encontrado['Nombre'],
                        'Cédula': usuario_encontrado['Cédula'],
                        'Placa': usuario_encontrado['Placa'],
                        'Marchamo': placa_encontrada['Marchamo']
                    }
                    vehiculo_verificado.append(placa_encontrada_json)
                    with open(json_vehiculo_verificado, "w", encoding='utf-8') as file:
                        json.dump(vehiculo_verificado, file, indent=3, ensure_ascii=False)
                        print("Información guardada en archivo JSON satisfactoriamente")
                        input()
                    return
            else:
                print("Usuario no encontrado. Presione enter para continuar.")
                input()
                while True:
                    Nombre = input("Ingrese el nombre del visitante: ")
                    if re.match("^[A-Za-z ]+$", Nombre) and any(char.isalpha() for char in Nombre):
                        Cedula = usuario
                    else:
                        print("Caracter incorrecto. Recuerde que solo puede colocar letras sin caractéres especiales. Presione enter para continuar.")
                        input()
                        continue
                    while True:
                        Placa = input("Digite el número de placa: ")
                        if Placa.isalnum():
                            break
                        else:
                            print("Caracter incorrecto. Recuerde que solo puede colocar letras o números. Presione enter para continuar.")
                            input()
                    visitante = {"Nombre": Nombre, "Cédula": Cedula, "Placa": Placa}
                    agregar_visitantes_json = {
                            'fecha': current_date,
                            'nombre': visitante['Nombre'],
                            'Cédula': visitante['Cédula'],
                            'Placa': visitante['Placa'],
                    }
                    agregar_visitantes.append(agregar_visitantes_json)
                    with open(json_agregar_visitantes, "w", encoding='utf-8') as file:
                            json.dump(agregar_visitantes, file, indent=3, ensure_ascii=False)
                            print("Información guardada en archivo JSON satisfactoriamente. Presione enter para continuar.")
                            input()
                    break
                break
        except:
            print("Caracter incorrecto. Recuerde que solo puede colocar números sin espacios o caractéres. Presione enter para continuar.")
            input()