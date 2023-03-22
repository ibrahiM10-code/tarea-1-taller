from validadores import *
from persona import Persona
import time, os, pwinput

lista_carga = []
diccionario_datos = {}
tabs_texto = 8
tabs_carga = 6
tabs_carga_texto = 9
tabs_texto_menu = 9
tabs_marco_menu = 7


def ingresar():

    global persona

    nombre = input("Ingrese su nombre: ")
    rut = input("Ingrese su R.U.T: ")

    if validaRut(rut):
        pass
    else:
        print("Ingrese un R.U.T válido.")
        time.sleep(1)
        while rut != True:
            rut = input("Ingrese su R.U.T: ")
            if validaRut(rut):
                break
            else:
                print("Ingrese un R.U.T válido.")
            
    fecha_nac = input("Ingrese su fecha de nacimiento: ")
    ciudad = input("Ingrese su ciudad: ")
    estado = input("Ingrese su estado: ")
    email = input("Ingrese su email: ")

    if validaEmail(email):
        pass
    else:
        print("Ingrese un correo válido.")
        time.sleep(1)
        while email != True:
            email = input("Ingrese su email: ")
            if validaEmail(email):
                print("Email correcto!")
                time.sleep(1)
                break
            else:
                continue

    usuario = input("Ingrese nuevamente su usuario: ")
    clave = pwinput.pwinput("Ingrese nuevamente su clave: ", "*")

    persona = Persona(nombre, rut, fecha_nac, ciudad, estado, email, usuario, clave)
    
    diccionario_datos = {"R.U.T": rut, "Nombre":nombre, "Fecha de nacimiento": fecha_nac, "Ciudad": ciudad, "Estado": estado, "Email": email, "Usuario": usuario, "Clave": clave}

    return diccionario_datos

def modificar():
    
    nuevo_nombre = input("Ingrese nuevo nombre: ")
    nuevo_rut = input("Ingrese nuevo R.U.T: ")
    nueva_fecha_nac = input("Ingrese nueva fecha de nacimiento: ")
    nueva_ciudad = input("Ingrese una nueva ciudad: ")
    nuevo_estado = input("Ingrese un nuevo estado: ")
    nuevo_email = input("Ingrese un nuevo email: ")
    nuevo_usuario = input("Ingrese nuevo usuario: ")
    nueva_clave = pwinput.pwinput(prompt="Ingrese nueva clave: ", mask="*")
    
    actualizado = {"R.U.T": nuevo_rut, "Nombre": nuevo_nombre, "Fecha de nacimiento": nueva_fecha_nac, "Ciudad": nueva_ciudad, "Estado": nuevo_estado, "Email": nuevo_email, "Usuario": nuevo_usuario, "Clave": nueva_clave}
    
    return actualizado


os.system("cls")

print("\n \n" + "\t" * tabs_texto + "Autenticarse.")
usuario = input("\n \n" + "\t" * tabs_texto + "Usuario: " )
contrasena = pwinput.pwinput(prompt="\t" * tabs_texto + "Contraseña: ", mask="*")

os.system("cls")

for i in range(100 + 1):
    time.sleep(0.1)
    os.system("cls")
    print("\n \n" + "\t" * tabs_carga_texto + str(i) + "%")
    if i != 0:
        if i % 10 == 0:
            lista_carga.append("🟩")
    print("\n" + "\t" * tabs_carga + str(lista_carga))

#Hacer menu del crud.
while True:
    os.system("cls")
    print("\t" * tabs_marco_menu + "----------------------------------------------")
    print("\t" * tabs_texto_menu + "   Menu")
    print("\t" * tabs_marco_menu + "----------------------------------------------")
    print("\t" * tabs_texto_menu + "1. Ingresar")
    print("\t" * tabs_marco_menu + "----------------------------------------------")
    print("\t" * tabs_texto_menu + "2. Modificar")
    print("\t" * tabs_marco_menu + "----------------------------------------------")
    print("\t" * tabs_texto_menu + "3. Listar")
    print("\t" * tabs_marco_menu + "----------------------------------------------")
    print("\t" * tabs_texto_menu + "4. Eliminar")
    print("\t" * tabs_marco_menu + "----------------------------------------------")
    print("\t" * tabs_texto_menu + "5. Salir")
    print("\t" * tabs_marco_menu + "----------------------------------------------")
    opcion = int(input("\t" * tabs_texto_menu +" Opcion: "))

    if opcion == 1:
        os.system("cls")
        datos_persona = ingresar()
    elif opcion == 2:
        os.system("cls")
        datos_actualizados = modificar()
        datos_persona = persona.actualizar_persona(datos_actualizados, datos_persona)
        input("Presiona enter para continuar.")
    elif opcion == 3:
        os.system("cls")
        persona.mostrar_persona(datos_persona)
        input("\t" * 7 + "Presiona enter para continuar.")
    elif opcion == 4:
        os.system("cls")
        del persona
        input("Usuario eliminado. Presione enter para continuar.")
    else:
        break
