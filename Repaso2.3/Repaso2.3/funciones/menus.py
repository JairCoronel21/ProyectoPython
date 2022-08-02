import time
from funciones.base import usuarios
yel = '\033[33m'
rsa = '\033[0;m'
red = '\033[31m'
blu = '\033[34m'
mag = '\033[35m'
cya = '\033[36m'
gre = '\033[32m'

def icono():
    time.sleep(0.8)
    print()
    print(cya+"░██████╗░░██████╗███████╗██████╗░██╗░░░██╗██╗░█████╗░███████╗░██████╗"+rsa)
    print(cya+"██╔═══██╗██╔════╝██╔════╝██╔══██╗██║░░░██║██║██╔══██╗██╔════╝██╔════╝"+rsa)
    print(cya+"██║██╗██║╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝██║██║░░╚═╝█████╗░░╚█████╗░"+rsa)
    print(cya+"╚██████╔╝░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██║██║░░██╗██╔══╝░░░╚═══██╗"+rsa)
    print(cya+"░╚═██╔═╝░██████╔╝███████╗██║░░██║░░╚██╔╝░░██║╚█████╔╝███████╗██████╔╝"+rsa)
    print(cya+"░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚══════╝╚═════╝░"+rsa)
    print()
    
def menuPrincipal():
    print(mag+"CARGANDO MENU ..."+rsa)
    time.sleep(2)
    print()
    print(yel+"[1] LOGIN"+rsa)
    print(yel+"[2] REGISTRO"+rsa)
    print(yel+"[3] RECUPERAR CONTRASEÑA"+rsa)
    print(yel+"[4] SALIR"+rsa)
    print()
    
def menu2(nom):
    print(mag+"CARGANDO MENU ..."+rsa)
    time.sleep(2)
    if len(usuarios[nom]) == 8:
        print()
        print(yel+"[1] MARCAR ASISTENCIA"+rsa)
        print(yel+"[2] VER DATOS"+rsa)
        print(yel+"[3] MODIFICAR CONTRASEÑA"+rsa)
        print(yel+"[4] MODIFICAR DATOS PERSONALES"+rsa) 
        print(yel+"[5] CERRAR SESION"+rsa)
        print()
    else:
        print()
        print(yel+"[1] MARCAR ASISTENCIA"+rsa)
        print(yel+"[2] VER DATOS"+rsa)
        print(yel+"[3] MODIFICAR CONTRASEÑA"+rsa)
        print(yel+"[4] MODIFICAR DATOS PERSONALES"+rsa) 
        print(yel+"[5] VER PAGO"+rsa)
        print(yel+"[6] CERRAR SESION"+rsa)
        print()

def menu3():
    print(mag+"CARGANDO MENU ..."+rsa)
    time.sleep(2)
    
    print()
    print(yel+"[1] VER LISTA DE USUARIOS"+rsa)
    print(yel+"[2] BUSCAR USUARIOS"    +rsa)
    print(yel+"[3] BLOQUEAR USUARIOS"        +rsa)
    print(yel+"[4] DESBLOQUEAR USUARIOS"    +rsa)
    print(yel+"[5] RESTAURAR CONTRASEÑA"        +rsa)
    print(yel+"[6] ELIMINAR USUARIOS"        +rsa)
    print(yel+"[7] VER ASISTENCIA"        +rsa)
    print(yel+"[8] CERRAR SESION"        +rsa)
    print()
    
    
def menu4():
    print(mag+"CARGANDO MENU ..."+rsa)
    time.sleep(2)
    print()
    print(yel+"[1] ENVIAR CODIGO AL WHATSAPP"+rsa)
    print(yel+"[2] ENVIAR CODIGO AL CORREO"+rsa)
    print(yel+"[3] CANCELAR"+rsa)
    print()    
    
def menu5():
    print(mag+"CARGANDO MENU ..."+rsa)
    time.sleep(2)
    print()
    print(yel+"[1] ACTUALIZAR NOMBRE"+rsa)
    print(yel+"[2] ACTUALIZAR CORREO"+rsa)
    print(yel+"[3] ACTUALIZAR TELEFONO"+rsa)
    print(yel+"[4] CANCELAR"+rsa)
    print()

def menu6():
    print(mag+"CARGANDO MENU ..."+rsa)
    time.sleep(2)
    print()
    print(yel+"[1] VER ASISTENCIA POR EMPLEADO"+rsa)
    print(yel+"[2] VER ASISTENCIA POR FECHA"+rsa)
    print(yel+"[3] CALCULAR PAGO"+rsa)
    print(yel+"[4] SALIR"+rsa)
    print()