from modulo5_datos import guardas
import datetime
import json

# Permite a los guardas acceder al sistema mediante su número de cédula y contraseña.
#Verifica las credenciales del usuario y guarda el registro de acceso en un archivo JSON.

def modulo_administracion ():
    json_registro_guardas= "registro_guardas.json"
    try:
        with open(json_registro_guardas, "r", encoding='utf-8') as guarda_file:
            registro_guardas = json.load(guarda_file)
    except FileNotFoundError:
        registro_guardas= []
    while True:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            usuario = int(input ("Ingrese su número de cédula del usuario:"))
            guarda_encontrado = None
            for guarda in guardas:
                if  guarda ["Cédula"] == usuario:
                    guarda_encontrado = guarda
                    break
            if guarda_encontrado:
                print ("Bienvenido",guarda_encontrado['nombre'])
                while True:
                    contraseña_ingreso = input ("Ingrese su contraseña:")
                    if contraseña_ingreso == guarda_encontrado ['contraseña']:
                        print ("La contraseña es correcta. Bienvenido al sistema. Presione enter para continuar")
                        input ()
                        guarda_encontrado_json = {
                            'fecha': current_date,
                            'nombre': guarda_encontrado['nombre'],
                            'Cédula': guarda_encontrado['Cédula']}
                        registro_guardas.append(guarda_encontrado_json)                  
                        with open(json_registro_guardas, "w", encoding='utf-8') as file:
                            json.dump(registro_guardas, file, indent=3, ensure_ascii=False)
                            print("Información guardada en archivo JSON satisfactoriamente")
                            return
                    else:
                        print ("Contraseña no válida. Inténtelo nuevamente")
            else:
                print ("Usuario no encontrado")
        except ValueError:
            print("Caracter inválido. Recuerde que solo debe escribir números sin espacios u otros elementos. Presion enter para volver a intentarlo.")
            input ()
