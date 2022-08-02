from datetime import datetime, timedelta
from funciones.validaciones import ValidarDni, validarEmail, validarFecha, validarSueldo, validarTel, validarUser, validarnombre, validarpasswordRegistro, validarUserv2,validNum3,validNum4
from funciones.menus import menu2, menu3, menu5,menuPrincipal,menu4,menu6
from funciones.base import empleados ,usuarios
from funciones.celular import asdasd
from funciones.correotest import enviarv2
from funciones.base import asistencia
import re
import time
yel = '\033[33m'
rsa = '\033[0;m'
red = '\033[31m'
blu = '\033[34m'
mag = '\033[35m'
cya = '\033[36m'
gre = '\033[32m'

def Login(lista):
    
        t = True
        while t == True:
            print(blu+'--------------------------------'+rsa)
            nom = input("Ingresa tu nombre de usuario: ")
            if nom in lista.keys() and lista[nom]["Estado"] == 1:
                if lista[nom]["type"] == "user":
                    for i in range(3):
                        pwd = input("Ingresa tu contraseña: ")
                        if pwd == lista[nom]["Password"]:
                            type = lista[nom]["type"]
                            return nom, type
                        else:
                            print(red+'╔═══════════════════════╗'+rsa)
                            print(red+"║ Contraseña incorrecta ║"+rsa)
                            print(red+'╚═══════════════════════╝'+rsa)
                        if i == 2:
                            time.sleep(1)
                            print()
                            print(mag+'╔════════════════════════════════════╗'+rsa)
                            print(mag+"║Execediste intentos,cuenta bloqueada║"+rsa)
                            print(mag+'╚════════════════════════════════════╝'+rsa)
                            print()
                            lista[nom]["Estado"] = 0
                            
                else:
                    print(cya+'Cuenta de administrador.'+rsa)
                    pwd = input("Ingresa tu contraseña : ")
                    if pwd == lista[nom]["Password"]:
                            type = lista[nom]["type"]
                            return nom, type
                    else:
                        print(red+'╔═══════════════════════╗'+rsa)
                        print(red+"║ Contraseña incorrecta ║"+rsa)
                        print(red+'╚═══════════════════════╝'+rsa)
            else:
                print(red+'╔═════════════════════════════════════════════════════╗'+rsa)
                print(red+"║ Nombre de usuario no encontrado o usuario Bloqueado ║"+rsa)
                print(red+'╚═════════════════════════════════════════════════════╝'+rsa)
        else:
            print(red+'╔═════════════════════════════════════════════════════╗'+rsa)
            print(red+"║ Nombre de usuario no encontrado o usuario Bloqueado ║"+rsa)
            print(red+'╚═════════════════════════════════════════════════════╝'+rsa)
            
            quit()
            
            
def Registro(lista):
    
    diccuni = {}
    print("Este es el registro")
    Dni = ValidarDni(empleados,lista)
    Nombre = empleados[Dni]["Nombre"]
    User = validarUser()
    Pwd = validarpasswordRegistro()
    Correo = validarEmail()
    Telefono = validarTel()
    
    diccuni["Dni"] = Dni
    diccuni["Nombre"] = Nombre
    diccuni["Correo"] = Correo
    diccuni["Password"] = Pwd
    diccuni["Telefono"] = Telefono
    diccuni["Estado"] = 1
    diccuni["type"] = "user"
    
    lista[User] = diccuni
    
    print(gre+'REGISTRANDO USUARIO ,ESPERE UN MOMENTO ...'+rsa)
    time.sleep(2)
    print(gre+'{:<5}{:<0}'.format('',' ╔════════════════════╗'+rsa))
    print(gre+'{:<5}{:<0}'.format('',' ║ Registro realizado ║'+rsa))
    print(gre+'{:<5}{:<0}'.format('',' ╚════════════════════╝'+rsa))
    
def Recuperar(lista):
    print(gre+"Entrando a recuperacion de contraseña, espere un momento"+rsa)
    time.sleep(1)
    User = validarUserv2(lista)
    menu4()
    op = validNum3()
    if op == 1:
        codigo = asdasd(lista[User]["Telefono"])
        codigoinput = input("Ingresa el codigo proporcionado a tu telefono: ")
        if codigo == codigoinput:
            print(cya+' ─────────────────────────────────'+rsa)
            print(cya+f"    Tu contraseña es: {lista[User]['Password']}"+rsa)
            print(cya+' ─────────────────────────────────'+rsa)
        else:
            print(red+'{:<5}{:<0}'.format('',' ╔════════════════╗'+rsa))
            print(red+'{:<5}{:<0}'.format('',' ║ Codigo errado  ║'+rsa))
            print(red+'{:<5}{:<0}'.format('',' ╚════════════════╝'+rsa))
    elif op == 2:
        aaa = lista[User]["Correo"].split("@")
        primero = aaa[0]
        correo = primero + "@gmail.com"
        
        codigo = enviarv2(correo)
        codigoinput = input("Ingresa el codigo proporcionado a tu email: ")
        if codigo == codigoinput:
            print(cya+' ─────────────────────────────────'+rsa)
            print(cya+f"    Tu contraseña es: {lista[User]['Password']}"+rsa)
            print(cya+' ─────────────────────────────────'+rsa)
        else:
            print(red+'{:<5}{:<0}'.format('',' ╔════════════════════╗'+rsa))
            print(red+'{:<5}{:<0}'.format('',' ║ Codigo incorrecto  ║'+rsa))
            print(red+'{:<5}{:<0}'.format('',' ╚════════════════════╝'+rsa))
    elif op == 3:
        print('cancelando')
        
def bienvenida(lista,nom):
    print(gre+"-------------------------"+rsa)
    print(gre+f"Bienvenido {lista[nom]['Nombre']}"+rsa)
    print(gre+"-------------------------"+rsa)
    
def verUser(lista):
    print(blu+'╔════════════╦════════════════════╦═════════════╦════════════════════════════════════════╦════════╦═══════════╗'+rsa)
    print(blu+"{:<5}{:<8}{:<8}{:<13}{:<4}{:<10}{:<18}{:<23}{:<2}{:<7}{:<3}{:<9}{:<0}".format('║','DNI','║','NOMBRE','║','USUARIO','║','CORREO','║','ESTADO','║','CELULAR','║'+rsa))
    print(blu+'╠════════════╬════════════════════╬═════════════╬════════════════════════════════════════╬════════╬═══════════╣'+rsa)

    for d in lista.keys():
        pa = (blu+'║'+rsa)
        if lista[d]["type"] == "user":
            
            print("{:<13}{:<10}{:<5}{:<20}{:<5}{:<13}{:<5}{:<40}{:<15}{:<4}{:<12}{:<10}{:<5}".format(pa,lista[d]["Dni"],pa,lista[d]["Nombre"],pa,d,pa,lista[d]["Correo"],pa,lista[d]["Estado"],pa,lista[d]["Telefono"],pa))
            print(blu+'╚════════════╩════════════════════╩═════════════╩════════════════════════════════════════╩════════╩═══════════╝'+rsa)   
            

def bloquear(lista):
    a = True
    while a == True:
            print(blu+'---------------------------------'+rsa)
            x = input("Ingresa nombre de usuario a bloquear: ")
            if x in lista:
                if lista[x]["Estado"] == 1:
                    lista[x]["Estado"]  = 0
                    print(red+'Bloqueando usuario ,espere un momento ...'+rsa)
                    time.sleep(2)
                    print(gre+' ╔═══════════════════╗'+rsa)
                    print(gre+" ║ Usuario bloqueado ║"+rsa)
                    print(gre+' ╚═══════════════════╝'+rsa)
                    a = False
                else:
                    print(red+'Bloqueando usuario ,espere un momento ...'+rsa)
                    time.sleep(2)
                    print(red+' ╔═══════════════════════════════════════════════╗'+rsa)
                    print(red+" ║ Uusario ya ha sido bloqueado con anterioridad ║"+rsa)
                    print(red+' ╚═══════════════════════════════════════════════╝'+rsa)
                    a=True
            else:
                print(red+' ╔═══════════════════════╗'+rsa)
                print(red+" ║ Usuario no encontrado ║"+rsa)
                print(red+' ╚═══════════════════════╝'+rsa)
                a = True

def desbloquear(lista):
    a = True
    while a == True:
            print(blu+'---------------------------------'+rsa)
            x = input("Ingresa nombre de usuario a desbloquear: ")
            if x in lista:
                if lista[x]["Estado"] == 0:
                    lista[x]["Estado"]  = 1
                    print(red+'Desloqueando usuario ,espere un momento ...'+rsa)
                    time.sleep(2)
                    print(gre+' ╔══════════════════════╗'+rsa)
                    print(gre+" ║ Usuario desbloqueado ║"+rsa)
                    print(gre+' ╚══════════════════════╝'+rsa)
                    a = False
                else:
                    print(red+'Desloqueando usuario ,espere un momento ...'+rsa)
                    time.sleep(2)
                    print(gre+' ╔════════════════════════════════╗'+rsa)
                    print(gre+" ║ El usuario estaba desbloqueado ║"+rsa)
                    print(gre+' ╚════════════════════════════════╝'+rsa)
                    a = True
                
            else:
                print(red+' ╔═══════════════════════╗'+rsa)
                print(red+" ║ Usuario no encontrado ║"+rsa)
                print(red+' ╚═══════════════════════╝'+rsa)
                a = True
                
def buscar():
    rp = True
    while rp == True:
        dicc = {}        
        nom = input('Ingrese indicios para buscar: ')
        nom = nom.lower()
        for k in usuarios.keys():
            diccuni = {}
            if nom in k.lower():
                diccuni["Nombre"] = usuarios[k]["Nombre"]
                diccuni["Dni"] = usuarios[k]["Dni"]
                diccuni["Correo"] = usuarios[k]["Correo"]
                diccuni["Telefono"] = usuarios[k]["Telefono"]
                dicc[k] = diccuni
        if len(dicc) == 0:
            print(red+' ╔═════════════════════════════════╗'+rsa)
            print(red+" ║ No se encontraron coincidencias ║"+rsa)
            print(red+' ╚═════════════════════════════════╝'+rsa)
        else:
            print(blu+'╔════════════╦════════════════════╦═════════════╦════════════════════════════════════════╦═══════════╗'+rsa)
            print(blu+"{:<3}{:<10}{:<8}{:<13}{:<4}{:<10}{:<18}{:<23}{:<2}{:<10}{:<0}".format('║','USUARIO','║','NOMBRE','║','DNI','║','CORREO','║','CELULAR','║'+rsa))
            print(blu+'╠════════════╬════════════════════╬═════════════╬════════════════════════════════════════╬═══════════╣'+rsa)

            for d in dicc:
                pa = (blu+'║'+rsa)          
                print("{:<13}{:<10}{:<5}{:<20}{:<5}{:<13}{:<5}{:<40}{:<12}{:<10}{:<12}".format(pa,d,pa,dicc[d]["Nombre"],pa,dicc[d]["Dni"],pa,dicc[d]["Correo"],pa,dicc[d]["Telefono"],pa))
                print(blu+'╚════════════╩════════════════════╩═════════════╩════════════════════════════════════════╩═══════════╝'+rsa)   
                        
            rp = False
        

def eliminar(lista):
    p = True
    while p == True:
        print(blu+'---------------------------------'+rsa)
        x = input("Ingresa nombre de usuario a eliminar: ")
        if x in lista:
            lista.pop(x)
            print(red+'Eliminando usuario ,espere un momento ...'+rsa)
            time.sleep(2)
            print(gre+' ╔═══════════════════╗'+rsa)
            print(gre+" ║ Usuario Eliminado ║"+rsa)
            print(gre+' ╚═══════════════════╝'+rsa)
            p = False
        else:
            print(red+' ╔═══════════════════════╗'+rsa)
            print(red+" ║ Usuario no encontrado ║"+rsa)
            print(red+' ╚═══════════════════════╝'+rsa)
            p = True
            
def cambiarContraseña(lista,nom):
    p = True
    while p == True:
        print(blu+'---------------------------------'+rsa)
        x = input("Ingresa tu contraseña anterior: ")
        if x == lista[nom]["Password"]:
            z = input("Ingresa tu nueva contraseña: ")
            if 10 <= len(z):
                if (re.search('[a-z]', z) and re.search('[A-Z]', z)):
                    if (re.search('[0-9]', z)):
                        if  (re.search('[$@#_-]', z)):
                            espacio = ' '
                            if not (espacio in z):
                                y = input("Repite tu contraseña: ") 
                                if z == y:               
                                    lista[nom]["Password"] = y
                                    print(gre+'ACTUALIZANDO CONTRASEÑA,ESPERE UN MOMENTO'+rsa)
                                    time.sleep(1)
                                    print(gre+' ╔════════════════════════╗'+rsa)
                                    print(gre+" ║ Contraseña actualizada ║"+rsa)
                                    print(gre+' ╚════════════════════════╝'+rsa)
                                    print(blu+'---------------------------------'+rsa)
                                    p = False  
                                else:
                                    print(red+' ╔══════════════════════════╗'+rsa)
                                    print(red+" ║ Contraseñas no coinciden ║"+rsa)
                                    print(red+' ╚══════════════════════════╝'+rsa) 
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
                                                                                            
        else:
            print(red+' ╔══════════════════════════════════╗'+rsa)
            print(red+" ║ Contraseña anterior no coincide  ║"+rsa)
            print(red+' ╚══════════════════════════════════╝'+rsa)

def verdatosuser(lista,nom):
    for d in lista.keys():
        if nom in d:
            pa = (blu+'║'+rsa)
            print(blu+'╔════════════╦════════════════════╦══════════╦════════════════════════════════════════╦═══════════╗'+rsa)
            print(blu+"{:<4}{:<9}{:<8}{:<13}{:<5}{:<6}{:<18}{:<23}{:<3}{:<9}{:<0}".format('║','USUARIO','║','NOMBRE','║','DNI','║','CORREO','║','CELULAR','║'+rsa))
            print(blu+'╠════════════╬════════════════════╬══════════╬════════════════════════════════════════╬═══════════╣'+rsa)
            print("{:<5}{:<12}{:<5}{:<20}{:<12}{:<9}{:<2}{:<40}{:<12}{:<10}{:<0}".format(pa,d,pa,lista[nom]['Nombre'],pa,lista[nom]['Dni'],pa,lista[nom]['Correo'],pa,lista[nom]['Telefono'],pa))
            print(blu+'╚════════════╩════════════════════╩══════════╩════════════════════════════════════════╩═══════════╝'+rsa)
        
def actualizarDatos(lista,nom):
    pa = (blu+'║'+rsa)
    print(red+'{:<30}{:<0}'.format('',' ╔═══════════════════╗'+rsa))
    print(red+'{:<30}{:<0}'.format('',' ║ Datos a modificar ║'+rsa))
    print(red+'{:<30}{:<0}'.format('',' ╚═══════════════════╝'+rsa))
    print(blu+'╔═══════════════════════╦═════════════════════════════════════╦══════════════════╗'    +rsa)
    print(blu+'║        NOMBRE         ║','              CORREO                ║','    TELEFONO     ║'+rsa)
    print(blu+'╠═══════════════════════╬═════════════════════════════════════╬══════════════════╣'    +rsa)
    print('{:<2}{:<23}{:<2}{:<37}{:<15}{:<14}{:<0}'.format(pa,lista[nom]["Nombre"],pa,lista[nom]["Correo"],pa,lista[nom]["Telefono"],pa))
    print(blu+'╚═══════════════════════╩═════════════════════════════════════╩══════════════════╝'+rsa)
    
    p = True
    while p == True:
        menu5()
        op = validNum4()
        
        if op == 1:
            nombre = validarnombre()
            lista[nom]["Nombre"] = nombre
            print(mag+'Espere un momento mientras se actualiza ...'+rsa)
            time.sleep(2)
            print(cya+'************************'+rsa)
            print(cya+'*  NOMBRE ACTUALIZADO  *'+rsa)
            print(cya+'************************'+rsa)
            p = True
        elif op == 2:
            correo = validarEmail() 
            lista[nom]["Correo"] = correo 
            print(mag+'Espere un momento mientras se actualiza ...'+rsa)
            time.sleep(2)
            print(cya+'************************'+rsa)
            print(cya+'*  EMAIL ACTUALIZADO   *'+rsa)
            print(cya+'************************'+rsa)
            p = True
        elif op == 3:
            telefono = validarTel()
            lista[nom]["Telefono"] = telefono
            print(mag+'Espere un momento mientras se actualiza ...'+rsa)
            time.sleep(2)
            print(cya+'**************************'+rsa)
            print(cya+'*  TELEFONO ACTUALIZADO  *'+rsa)
            print(cya+'**************************'+rsa)
            p = True
        elif op == 4:
            p = False
        else:
            print('Opcion incorrecta, ingrese una opcionj correcta')

def restaurar():
    p = True
    while p == True:
        time.sleep(2)
        user = validarUserv2(usuarios)
        newpwd = "qservices2022"
        usuarios[user]["Password"] = newpwd
        print(red+' ╔═════════════════════════════════════════╗'+rsa)
        print(red+f"║ Contraseña Restablecida: {newpwd}       ║"+rsa)
        print(red+' ╚═════════════════════════════════════════╝'+rsa)
        p = False

    
def validaruserasistencia(nom):
    if {} == asistencia[nom]["Junio"]:
        return False
    else:
        return True
    
def verasistencia(nom):
    print("{:<20}{:<20}{:<0}".format("Fecha","Estado","Minutos Tarde"))
    for j in asistencia[nom]["Junio"].keys():
        d = asistencia[nom]["Junio"][j]
        if d == 0:
            l = gre+"Puntual"+rsa
        else:
            l = red+"Impuntual"+rsa
        print("{:<20}{:<35}{:<0}".format(j,l,d))
        
def vertardones(): #dividir en tardones y los q esta vacio...
    a = list() #No tienen asistencia
    b = list() #Tardones
    c = list() #puntuales
    fecha = validarFecha()
    for d in asistencia.keys():
        if asistencia[d]["Junio"] == {}:
            a.append(d)
        else:
            for q in asistencia[d]["Junio"]:
                if q == fecha:
                    if asistencia[d]["Junio"][q] > 0:
                        b.append(d)
                        break
                    else:
                        c.append(d)
                
    print("{:<20}{:<20}{:<0}".format("Tardones","Puntuales","No marcaron"))
    for i in b,c,a:
        for y in i:
            print("{:<20}{:<20}{:<0}".format(y))
            
        '''print("{:<20}".format("Tardones")) #CODIGO VERTICAL
        for t in b:
            t = red+t+rsa
            print("{:<20}".format(t))
            
        print("{:<20}".format("Puntuales"))
        for n in c:
            n = red+n+rsa
            print("{:<20}".format(n))
            
        print("{:<20}".format("No han llegado"))
        for k in a:
            k = cya+k+rsa
            print("{:<20}".format(k))'''
        
    '''for d in asistencia.keys():
                    if asistencia[d]["Junio"] == fecha:
                        print("hola")
                    else:
                        print("qqq")'''
                    

def generarPago():
    us = validarUserv2(usuarios)#validar usuario
    if validaruserasistencia(us):
        if len(usuarios[us]) == 8:
            sueldo = validarSueldo()
        
            z = 0
            for q in asistencia[us]['Junio']:
                z = z + asistencia[us]['Junio'][q]
            if z < 15:
                print('TE SALVASTE') # pago sin descuento  
            else:
                porminuto = ((sueldo/26)/8)/60
                print(f"Ganas {porminuto} por minuto")
                print("minutos tarde ",z)
                descuento = porminuto * z
                descuento = round(descuento,2)
                aPagar = sueldo - descuento
                aPagar = round(aPagar,2)
                
                usuarios[us]["Sueldo"] = sueldo
                usuarios[us]["Descuento"] = descuento
                usuarios[us]["aPagar"] = aPagar
                print(f"Sueldo: {sueldo}")
                print(f"Descuento por tardanza: {descuento}")
                print(f"Sueldo a pagar: {aPagar}")
        else:
            print("Ya generaste el sueldo")
    else:
        print("No tiene asistencia")
    # else que haga descuento e imprimia
    #calcular pago por hora (sueldo/30/8 y eso multiplicar por z , eso restar al sueldo e imprimir)


def asistenciageneral(): 
    p = True
    while p == True:
        menu6()
        op = validNum4()        
        if op == 1:
            nom = validarUserv2(usuarios)
            if validaruserasistencia(nom):
                verasistencia(nom)
            else:
                print('No tiene registro')
        elif op == 2:
            vertardones()
        elif op == 3:
            generarPago()
        elif op == 4:
            p = False
        else:
            print('Opcion incorrecta, ingrese una opcionj correcta')
            
def verpago(nom):
    print(f"Tu pago por contrato es: {usuarios[nom]['Sueldo']}")
    print(f"Tu descuento por tardanza es: {usuarios[nom]['Descuento']}")
    print(f"Entonces te pagaremos: {usuarios[nom]['aPagar']}")
    