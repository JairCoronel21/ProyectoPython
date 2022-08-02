import time
yel = '\033[33m'
rsa = '\033[0;m'
red = '\033[31m'
blu = '\033[34m'
mag = '\033[35m'
cya = '\033[36m'
gre = '\033[32m'

usuarios = {
    'elsupremo':{"Dni":"00000000","Nombre":"Arturo Huapaya","Correo":"arturo.huapaya.huapaya@qservices.pe","Password":"000","Telefono":"992272784","Estado":1,"type":"admin","Hora":"08:00"},
    'elbicho':{"Dni":"11111111","Nombre":"Fernando Paco","Correo":"fernandopacof@qservices.pe","Password":"212001","Telefono":"946121514","Estado":1,"type":"user","Hora":"08:00"},
    'MrMusculo':{"Dni":"22222222","Nombre":"José Perez","Correo":"joseperez301002@qservices.pe","Password":"joseps","Telefono":"963960534","Estado":0,"type":"user","Hora":"08:00"},
    'padula':{"Dni":"33333333","Nombre":"Osmarth Vargas","Correo":"osmarth18@qservices.pe","Password":"171723","Telefono":"955335705","Estado":1,"type":"user","Hora":"08:00"},
    'sargento':{"Dni":"44444444","Nombre":"Jair Coronel","Correo":"jilmercoronel7@qservices.pe","Password":"jcoronel","Telefono":"900278717","Estado":1,"type":"user","Hora":"08:00"},
    'kiwi':{"Dni":"55555555","Nombre":"Luis Condori","Correo":"luen.cg08@qservices.pe","Password":"1806","Telefono":"936180079","Estado":1,"type":"user","Hora":"14:00"}
}


empleados = {
    '00000000' : {"Nombre": "Arturo Huapaya"},
    '11111111' : {"Nombre": "Fernando Paco"},
    '22222222' : {"Nombre": "José Perez"},
    '33333333' : {"Nombre": "Osmarth Vargas"},
    '44444444' : {"Nombre": "Jair Coronel"},
    '55555555' : {"Nombre": "Luis Condori"},
    '66666666' : {"Nombre": "Sergio Garay"},
    '77777777' : {"Nombre": "Ariana Loayza"},
    '88888888' : {"Nombre": "Juan Perez"}
}

def CrearUsuario():
    usuario = input("Ingrese nombre de usuario: ")
    nombre = input("Ingrese nombre completo: ")
    dni = input("Ingrese el numero de Dni: ")
    correo = input("Ingrese Correo Electronico: ")
    pwd = input("Ingrese contraseña: ")
    token = input("Ingrese token de seguridad: ")
    estado = input("Ingrese estado: ")




def IniciarUsuario():
    user = 'Admin'
    pwdpre = '123'
    contador = 1
    i = 0

    usuario = input("Ingrese su usuario:")
    pwd = input("Ingrese password: ")
    
    if user == usuario and pwd == pwdpre:
        print(gre+'---------------------------'+rsa)
        print(gre+'Bienvenidos Datos Correctos'+rsa)
        print(gre+'---------------------------'+rsa)
    while contador <=3:
        if pwd == pwdpre:
            print(gre+'Contraseña Correcta'+rsa)
        else:
            print('Contraseña Incorrecta' + 'Intento: ', i+1)

        
        


#Mostar la lista de Usuarios
def ListaUsuarios():
	print("{:<10}{:<10}{:<15}".format("Dni", "Nombre", "Correo Electronico2"))
	print("----------------------------------------------------------------")
	for u in usuarios:
		print("{:<10}{:<10}{:<15}".format(u, usuarios[u].get("Nombre"), usuarios[u].get("Correo")))




def EliminarUsuario():
    usuarios.pop(input('Ingrese el Usuario a Eliminar: '))
    print(gre+' ╔═══════════════════╗'+rsa)
    print(gre+" ║ Usuario Eliminado ║"+rsa)
    print(gre+' ╚═══════════════════╝'+rsa)
    
    
#enviar correo por python para admin


asistencia = {
    "elbicho": {
        "Junio":{
            
            }
        
    },
    "MrMusculo": {
        "Junio":{ 
            
            }
        
    },
    "padula": {
        "Junio":{ 
            
            }
        
    },
    "sargento": {
        "Junio":{ 
            
            }
        
    },
    "kiwi": {
        "Junio":{ 
            
            }
        
    }
}