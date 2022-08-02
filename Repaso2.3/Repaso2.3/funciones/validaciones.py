import re
import time
from datetime import datetime
from funciones.base import usuarios as usuarioz
from funciones.menus import menuPrincipal
yel = '\033[33m'
rsa = '\033[0;m'
red = '\033[31m'
blu = '\033[34m'
mag = '\033[35m'
cya = '\033[36m'
gre = '\033[32m'


#validaciones de numeros
def validNum4():
    d = True
    while d == True:
        x = input("-> ")
        try: 
            x = int(x)
            if x > 0 and x < 7:
                d = False
            else:
                print(red+'{:<10}{:<0}'.format('',' ╔═════════════════╗'+rsa))
                print(red+'{:<10}{:<0}'.format('',' ║ Numero invalido ║'+rsa))
                print(red+'{:<10}{:<0}'.format('',' ╚═════════════════╝'+rsa))
                d = True
        except ValueError:
            print(red+'{:<10}{:<0}'.format('',' ╔═════════════════╗'+rsa))
            print(red+'{:<10}{:<0}'.format('',' ║ Numero invalido ║'+rsa))
            print(red+'{:<10}{:<0}'.format('',' ╚═════════════════╝'+rsa))
            d = True
    return x

def validNum6():
    d = True
    while d == True:
        x = input("-> ")
        try: 
            x = int(x)
            if x > 0 and x < 9:
                d = False
            else:
                print(red+'{:<10}{:<0}'.format('',' ╔═════════════════╗'+rsa))
                print(red+'{:<10}{:<0}'.format('',' ║ Numero invalido ║'+rsa))
                print(red+'{:<10}{:<0}'.format('',' ╚═════════════════╝'+rsa))
                d = True
        except ValueError:
            print(red+'{:<10}{:<0}'.format('',' ╔═════════════════╗'+rsa))
            print(red+'{:<10}{:<0}'.format('',' ║ Numero invalido ║'+rsa))
            print(red+'{:<10}{:<0}'.format('',' ╚═════════════════╝'+rsa))
            d = True
    return x

def validNum3():
    d = True
    while d == True:
        x = input("-> ")
        try: 
            x = int(x)
            if x > 0 and x < 4:
                d = False
            else:
                print(red+'{:<10}{:<0}'.format('',' ╔═════════════════╗'+rsa))
                print(red+'{:<10}{:<0}'.format('',' ║ Numero invalido ║'+rsa))
                print(red+'{:<10}{:<0}'.format('',' ╚═════════════════╝'+rsa))
                d = True
        except ValueError:
            print(red+'{:<5}{:<0}'.format('',' ╔═════════════════╗'+rsa))
            print(red+'{:<5}{:<0}'.format('',' ║ Numero invalido ║'+rsa))
            print(red+'{:<5}{:<0}'.format('',' ╚═════════════════╝'+rsa))
            d = True
    return x
#validaciones de registro # corregir
#validacion email 


def validarEmail():
    is_valid = True
    while is_valid == True:
        email = input("Correo->")
        EMAILREGEX = re.compile(r"^[a-zA-Z0-9.]+@qservices.pe")
        if email == '@qservices.pe':
            print(red+'------------------------'+rsa)
            print(red+" Nombre de usuario vacio"+rsa)
            print(red+'------------------------'+rsa)
        else:
            for i in usuarioz.keys():
                if email in usuarioz[i]["Correo"]:
                    print(red+'------------------------------'+rsa)
                    print(red+" El correo ya esta registrado"+rsa)
                    print(red+'------------------------------'+rsa)
                    is_valid = True
                    break
            else:
                if not EMAILREGEX.match(email):
                    print(red+'----------------------------------------------'+rsa)
                    print(red+" Dominio incorrecto y/o caracteres no validos"+rsa)
                    print(red+'----------------------------------------------'+rsa) # dominio mal y caracteres no validos 
                    is_valid = True
                else:
                    aa = email.split('@')
                    usuario = aa[0]
                    if len(usuario) >= 6 and len(usuario)<=30:
                        if "." in usuario:
                            pp = usuario.split(".")
                            for i in pp:
                                if i == "":
                                    print(red+'--------------------------------------------------------------'+rsa)
                                    print(red+" El nombre de usuario no puede contener 2 puntos consecutivos"+rsa)
                                    print(red+'--------------------------------------------------------------'+rsa) # error dos puntos
                                    is_valid = True
                                    break  
                            else:
                                print(gre+'┌──────────────┐'+rsa)
                                print(gre+"│ Correo valido│"+rsa)
                                print(gre+'└──────────────┘'+rsa)#cartel bonito
                                is_valid = False
                                return email
                        else:
                            print(gre+'┌──────────────┐'+rsa)
                            print(gre+"│ Correo valido│"+rsa)
                            print(gre+'└──────────────┘'+rsa)#cartel bonito
                            is_valid = False
                            return email
                    else:
                        print(red+'----------------------------------------------------------'+rsa)
                        print(red+" El nombre de usuario debe contener entre 6-30 caracteres"+rsa)
                        print(red+'----------------------------------------------------------'+rsa) #error cantidad
                        is_valid = True

def validarnombre():
    p = True
    while p == True:
        nombre= input("Introduzca el nombre: ") #Entrada del usuario
        a = nombre.split(" ")
        if len(a) == 2:
            nom = a[0]
            ape = a[1]
            if nom.isalpha() and ape.isalpha():
                p = False
                print(gre+'┌───────────────┐'+rsa)
                print(gre+"│ Nombre valido │"+rsa)
                print(gre+'└───────────────┘'+rsa)
                return nombre
            else:
                print(red+'{:<10}{:<0}'.format('',' ╔══════════════════╗'+rsa))
                print(red+'{:<10}{:<0}'.format('',' ║ Ingrese de nuevo ║'+rsa))
                print(red+'{:<10}{:<0}'.format('',' ╚══════════════════╝'+rsa))
                print(cya+' ╔═════════════════════════════════════╗'+rsa)
                print(cya+' ║ Recuerde escribir nombre y apellido ║'+rsa)
                print(cya+' ╚═════════════════════════════════════╝'+rsa)
                print()
                p = True
        else:
            print(red+'{:<10}{:<0}'.format('',' ╔══════════════════╗'+rsa))
            print(red+'{:<10}{:<0}'.format('',' ║ Ingrese de nuevo ║'+rsa))
            print(red+'{:<10}{:<0}'.format('',' ╚══════════════════╝'+rsa))
            print(cya+'{:<0}{:<0}'.format('',' ╔═════════════════════════════════════╗'+rsa))
            print(cya+'{:<0}{:<0}'.format('',' ║ Recuerde escribir nombre y apellido ║'+rsa))
            print(cya+'{:<0}{:<0}'.format('',' ╚═════════════════════════════════════╝'+rsa))
            p = True





#validacion dni
def ValidarDni(empleados,lista):
    a = True
    while a == True:
        dnicr = input("Ingresa tu dni: ")
        if dnicr in empleados:
            if len(dnicr) == 8:
                for d in lista.keys():
                    if lista[d]["Dni"] == dnicr:
                        a = True
                        print(red+'{:<5}{:<0}'.format('',' ╔═══════════════════════╗'+rsa))
                        print(red+'{:<5}{:<0}'.format('',' ║  Ya tienes un usuario ║'+rsa))
                        print(red+'{:<5}{:<0}'.format('',' ╚═══════════════════════╝'+rsa))
                        break
                else:
                    a=False
                    print(gre+'{:<5}{:<0}'.format('',' ╔═════════════════════════════════════════════════╗'+rsa))
                    print(gre+'{:<5}{:<0}'.format('',' ║  Empleado encontrado correctamente en planilla  ║'+rsa))
                    print(gre+'{:<5}{:<0}'.format('',' ╚═════════════════════════════════════════════════╝'+rsa))
                    return dnicr

            else:
                print(red+'El Dni: {dnicr} no es valido'+rsa)
                a = True
        elif not(dnicr in empleados):
            print(red+'{:<10}{:<0}'.format('',' ╔═════════════════════════════════════╗'+rsa))
            print(red+'{:<10}{:<0}'.format('',' ║  Empleado no registrado en planilla ║'+rsa))
            print(red+'{:<10}{:<0}'.format('',' ╚═════════════════════════════════════╝'+rsa))
            a = True

#validaciones contraseña
def validarpasswordRegistro():
    a = True
    while a == True:
        pwd = input("Ingresa tu contraseña: ")
        if 10 <= len(pwd):
            if (re.search('[a-z]', pwd) and re.search('[A-Z]', pwd)):
                if (re.search('[0-9]', pwd)):
                    if  (re.search('[$@#_-]', pwd)):
                        espacio = ' '
                        if not (espacio in pwd):
                            print(gre+'{:<10}{:<0}'.format('',' ╔══════════════════════════════════╗'+rsa))
                            print(gre+'{:<10}{:<0}'.format('',' ║ Contraseña escrita correctamente ║'+rsa))
                            print(gre+'{:<10}{:<0}'.format('',' ╚══════════════════════════════════╝'+rsa))
                            a=False
                            return pwd
                        else:
                            print(red+'-------------------------------------'+rsa)
                            print(red+"La contraseña no debe tener espacios"+rsa)
                            print(red+'-------------------------------------'+rsa)                    
                    else:
                        print(red+'-------------------------------------------------------------'+rsa)
                        print(red+"La contraseña debe tener al menos un carácter especial($@#_-)"+rsa)
                        print(red+'-------------------------------------------------------------'+rsa)
                        a = True
                else:
                    print(red+'--------------------------------------------'+rsa)
                    print(red+"La contraseña debe tener al menos un número" +rsa)
                    print(red+'--------------------------------------------'+rsa)
                    a = True
            else:
                print(red+'-----------------------------------------------------------------------------------'+rsa)
                print(red+"La contraseña no debe tener espacios en blanco y debe tener al menos una Mayuscula" +rsa)
                print(red+'-----------------------------------------------------------------------------------'+rsa)
                a = True
        else:
            print(red+'------------------------------------------------'+rsa)
            print(red+"La contraseña debe tener al menos 10 carcacteres"+rsa)
            print(red+'------------------------------------------------'+rsa)
            a = True

def validarUser(): #registro
    a = True
    while a == True:
        user = input("Ingresa nombre de usuario: ")
        if not user in usuarioz:
            if  not(re.search('[$@#_-]', user)):
                if " " in user:
                    print(red+'-----------------------'+rsa)
                    print(red+"No se permiten espacios"+rsa)
                    print(red+'-----------------------'+rsa)
                    a = True
                else:
                    print(gre+'{:<10}{:<0}'.format('',' ╔═══════════════════════════╗'+rsa))
                    print(gre+'{:<10}{:<0}'.format('',' ║  Nombre de usuario valido ║'+rsa))
                    print(gre+'{:<10}{:<0}'.format('',' ╚═══════════════════════════╝'+rsa))
                    a = False
                    return user
            else:
                print(red+'----------------------------------------'+rsa)
                print(red+"No se permite simbolos especiales($@#_-)"+rsa)
                print(red+'----------------------------------------'+rsa)   
        else:
            print(red+'-------------------------------'+rsa)
            print(red+"Nombre de usuario ya registrado"+rsa)
            print(red+'-------------------------------'+rsa)
            
def validarTel():
    a = True
    while a == True:
        tel = input("Ingresa numero de telefono: ")
        for i in usuarioz.keys():
            if tel == usuarioz[i]["Telefono"]:
                print(red+'-----------------------------'+rsa)
                print(red+"Telefono ya asociado"+rsa)
                print(red+'-----------------------------'+rsa)
                a = True
                break
        else:
            if not " " in tel:
                if len(tel) == 9:
                    try:
                        int(tel)
                        a = False
                        return tel
                    except ValueError:
                        print(red+'----------------'+rsa)
                        print(red+"Numero invalido"+rsa)
                        print(red+'----------------'+rsa) 
                        a = True
                else:
                    print(red+'-----------------------------'+rsa)
                    print(red+"Revisa la cantidad de digitos"+rsa)
                    print(red+'-----------------------------'+rsa)
                    a = True
            else:
                print(red+'-----------------------------'+rsa)
                print(red+"No puede contener espacios"+rsa)
                print(red+'-----------------------------'+rsa)
                a = True

def validarUserv2(lista):
    a = True
    while a == True:
        user = input("Ingresa nombre de usuario: ")
        if user in lista:
            print(gre+'{:<5}{:<0}'.format('',' ╔═════════════════════╗'+rsa))
            print(gre+'{:<5}{:<0}'.format('',' ║  Usuario encontrado ║'+rsa))
            print(gre+'{:<5}{:<0}'.format('',' ╚═════════════════════╝'+rsa))
            a = False
            return user
        else:
            print(red+'{:<5}{:<0}'.format('',' ╔═══════════════════════════════════╗'+rsa))
            print(red+'{:<5}{:<0}'.format('',' ║  No estas registrado como usuario ║'+rsa))
            print(red+'{:<5}{:<0}'.format('',' ╚═══════════════════════════════════╝'+rsa))
            a = True            
            
            
def validarFecha():
    a = True
    while a == True:
        fechadehoy = datetime.now().date().day
        fech = input("Ingresa fecha a buscar: ")
        EMAILREGEX = re.compile(r"^[0-9]+/06/2022")
        if EMAILREGEX.match(fech):
            aaa = fech.split("/")
            dia = aaa[0]
            if int(dia) > fechadehoy or int(dia) == 0:
                print("Error")
                a = True
            else:
                if int(dia) < 10:
                    if not('0' in dia):
                        return fech
                    else:
                        print('error con 0')
                else:
                    return fech
        else:
            print("Error")
            a= True
            

def validarSueldo():
    d = True
    while d == True:
        sueldo = input("Ingresa el sueldo del usuario: ")
        try:
            sueldo = float(sueldo)
            sueldo = round(sueldo,2)
            if sueldo > 0:
                return sueldo
            else:
                print("No puede ser 0")
                d = True
        except ValueError:
            print("Error")
            d = True