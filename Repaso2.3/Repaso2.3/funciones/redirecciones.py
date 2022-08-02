from funciones.asistencia import asistenciaUser, generarasistencia
from funciones.utilidades import Login, Recuperar, Registro, actualizarDatos,  bienvenida, bloquear, cambiarContraseña, eliminar, restaurar, validaruserasistencia, verUser,desbloquear,buscar,verdatosuser,asistenciageneral
from funciones.menus import menu2, menu3, menuPrincipal,menu6
from funciones.base import usuarios
from funciones.validaciones import validNum4, validNum3 , validNum6, validarUser, validarUserv2
import time
from funciones.utilidades import verasistencia, verpago
from funciones.video import videofinal
import ascii_magic
yel = '\033[33m'
rsa = '\033[0;m'
red = '\033[31m'
blu = '\033[34m'
mag = '\033[35m'
cya = '\033[36m'
gre = '\033[32m'

us = usuarios

def redirPrincipal(op):
    if op == 1:
        temp = Login(us)
        nom = temp[0]
        type = temp[1]
        bienvenida(us,nom)
        if type == "admin":
            menu3()
            op = validNum6()
            redirOpcionesAdmin(op)
        else:
            menu2(nom)
            op = validNum4()
            redirOpcionesUser(op,nom)
        
    elif op == 2:
        Registro(us)
        menuPrincipal()
        op = validNum4()
        redirPrincipal(op)
    elif op == 3:
        Recuperar(us)
        menuPrincipal()
        op = validNum4()
        redirPrincipal(op)
    elif op == 4:
        print(mag+'Saliendo de la aplicacion ,espere ...'+rsa)
        time.sleep(1)
        print(gre+'{:<25}{:<0}'.format('',' ╔════════════════════════════╗'+rsa))
        print(gre+'{:<25}{:<0}'.format('',' ║ Gracias por su preferencia ║'+rsa))
        print(gre+'{:<25}{:<0}'.format('',' ╚════════════════════════════╝'+rsa))
        time.sleep(1)
        '''print(blu+'█████████████████████████████████████████████'+rsa)
        print(blu+'█████████░░░░░░░░░░░░░▒█▒▒██▒████████████████'+rsa)
        print(blu+'█████████░█▀▀▀▀▀▀▀▀▀▀▀███████─██─█─▄█████████'+rsa)
        print(blu+'█████████░█▒──────────█─▀█─▄██──███─█████████'+rsa)
        print(blu+'█████████░█▒──────────██▀██─█─██─████████████'+rsa)
        print(blu+'█████████░█▒──────────█─██─█─█─██████████████'+rsa)
        print(blu+'█████████░█▄▄▄▄▄▄▄▄▄▄▄████▄██████████████████'+rsa)
        print(blu+'█████████░░░░░░░░░░░░░░░░▒██▒████████████████'+rsa)
        print(blu+'████████████████░░░██░███████████████████████'+rsa)
        print(blu+'████████████████░░░█▒█▒██████████████████████'+rsa)
        print(blu+'███████████████░░██▒█▄██▒████████████████████'+rsa)
        print(blu+'█████████████████████████████████████████████'+rsa)
        print(blu+'████┌───┬───┬───┬───┬┐██┌┬──┬───┬───┬───┐████'+rsa)
        print(blu+'████│┌─┐│┌─┐│┌──┤┌─┐│└┐┌┘├┤├┤┌─┐│┌──┤┌─┐│████'+rsa)
        print(blu+'████││█││└──┤└──┤└─┘├┐││┌┘││││█└┤└──┤└──┐████'+rsa)
        print(blu+'████││█│├──┐│┌──┤┌┐┌┘│└┘│█││││█┌┤┌──┴──┐│████'+rsa)
        print(blu+'████│└─┘│└─┘│└──┤││└┐└┐┌┘┌┤├┤└─┘│└──┤└─┘│████'+rsa)
        print(blu+'████└──┐├───┴───┴┘└─┘█└┘█└──┴───┴───┴───┘████'+rsa)
        print(blu+'███████└┘████████████████████████████████████'+rsa)
        print(blu+'█████████████████████████████████████████████'+rsa)'''
        
        
        #out = ascii_magic.from_image_file("ultimo.jpg",columns=148,char="#")
        #ascii_magic.to_terminal(out)#Error con la imagen
        
        #videofinal()
        
        #quit()
        
def redirOpcionesAdmin(op):
    if op == 1: # ver usuarios
        verUser(us) #funciones
        menu3()
        op = validNum6()
        redirOpcionesAdmin(op)
    elif op == 2: #buscar usuarios
        buscar()
        menu3()
        op = validNum6()
        redirOpcionesAdmin(op)
    elif op == 3: #bloquear
        bloquear(us) #redireccionar
        menu3()
        op = validNum6()
        redirOpcionesAdmin(op)
    elif op == 4: #desbloquear
        desbloquear(us)
        menu3()
        op = validNum6()
        redirOpcionesAdmin(op)
    elif op == 5: #restaurar
        print("restaurar")
        restaurar()
        menu3()
        op = validNum6()
        redirOpcionesAdmin(op)
    elif op == 6: #eliminar
        eliminar(us)
        menu3()
        op = validNum6()
        redirOpcionesAdmin(op)
    elif op == 7:    
        asistenciageneral()
        menu3()  
        op = validNum6()
        redirOpcionesAdmin(op)
    elif op == 8: #cerrar sesion
        print(cya+'CERRANDO SESION ...'+rsa)
        time.sleep(2)
        menuPrincipal()
        op = validNum4()
        redirPrincipal(op)
        
def redirOpcionesUser(op,nom):
    if len(usuarios[nom]) == 8:
        if op == 1:
            print("Aqui marcás asistencia")
            min = asistenciaUser(nom)
            if min == False:
                print("Ya marcaste asistencia")
                
            else:
                generarasistencia(nom, min)
            menu2(nom)
            op = validNum4()
            redirOpcionesUser(op,nom)
            
        elif op == 2:
            verdatosuser(us,nom)
            time.sleep(1)
            menu2(nom)
            op = validNum4()
            redirOpcionesUser(op,nom)
            
        elif op == 3:
            cambiarContraseña(us,nom)
            menu2(nom)
            op = validNum4()
            redirOpcionesUser(op, nom)
            
        elif op == 4:
            actualizarDatos(us,nom)
            menu2(nom)
            op = validNum4()
            redirOpcionesUser(op,nom)
        elif op == 5:
            print(cya+'CERRANDO SESION ...'+rsa)
            time.sleep(2)
            menuPrincipal()
            op = validNum4()
            redirPrincipal(op)
    else:
        if op == 1:
            print("Aqui marcás asistencia")
            min = asistenciaUser(nom)
            if min == False:
                print("Ya marcaste asistencia")
                
            else:
                generarasistencia(nom, min)
                menu2(nom)
                op = validNum4()
                redirOpcionesUser(op,nom)
            
        elif op == 2:
            verdatosuser(us,nom)
            time.sleep(1)
            menu2(nom)
            op = validNum4()
            redirOpcionesUser(op,nom)
            
        elif op == 3:
            cambiarContraseña(us,nom)
            menu2(nom)
            op = validNum4()
            redirOpcionesUser(op, nom)
            
        elif op == 4:
            actualizarDatos(us,nom)
            menu2(nom)
            op = validNum4()
            redirOpcionesUser(op,nom)
        elif op == 5:
            verpago(nom)
            menu2(nom)
            op = validNum4()
            redirOpcionesUser(op,nom)
        elif op == 6:
            print(cya+'CERRANDO SESION ...'+rsa)
            time.sleep(2)
            menuPrincipal()
            op = validNum4()
            redirPrincipal(op)
    
'''def redirOpcrecuperar(op):
    if op == 1:
        Recuperar(us)
    elif op == 2:
        Recuperar(us)
    elif op == 3:
        menu3()
        op = validNum6()
        redirOpcionesAdmin(op)    
    '''
    
'''def rediractualizar(op):
    if op == 1:
        '''