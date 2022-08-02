from funciones.utilidades import vertardones
from funciones.validaciones import validarFecha, validarSueldo
#validarFecha()
#validarSueldo()
#vertardones()

usuarios = {
    'elsupremo':{
        "Junio":{ 
                '12':12,
                '15':11,
                '18':5
            }
                },
    'elpito':{
        "Junio":{ 
                '12':10,
                '15':2,
                '18':3
                }
            }
    }


us = input('Ingrese usuario: ')
z = 0
for q in usuarios[us]['Junio']:
    z = z + usuarios[us]['Junio'][q]


        
print(z)