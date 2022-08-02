import re

yel = '\033[33m'
rsa = '\033[0;m'
red = '\033[31m'
blu = '\033[34m'
mag = '\033[35m'
cya = '\033[36m'
gre = '\033[32m'

def validarEmail():
    is_valid = True
    while is_valid == True:
        email = input("Correo->")
        EMAILREGEX = re.compile(r"^[A-Za-z0-9.]+@qservices.pe")
        if not EMAILREGEX.match(email):
            print('error')
            is_valid = True
        else:
            aa = email.split('@')
            usuario = aa[0]
            if "." in usuario:
                pp = usuario.split(".")
                print(pp)
                for i in pp:
                    if i == "":
                        print("Error")
                        is_valid = True
                        break  
                else:
                    print("Correcto")
                    is_valid = False
                    return email
            else:
                print("Correcto")
                is_valid = False
                return email



        
        
validarEmail()