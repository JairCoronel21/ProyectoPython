from datetime import datetime
import random
from re import X
from funciones.base import usuarios
from funciones.base import asistencia

def asistenciaUser(nom):
    if {} == asistencia[nom]["Junio"]:
        #hora_marcada = datetime.now().strftime("%H:%M")
        hora_marcada = "14:30"
        hora_marcada = datetime.strptime(hora_marcada, "%H:%M").time()

        print(f"Marcaste a las: {hora_marcada}")

        tuhora = usuarios[nom]["Hora"]

        tuhora = datetime.strptime(tuhora,"%H:%M").time()


        print("tu hora de llegada es a las: ",tuhora)


        if tuhora.hour < hora_marcada.hour:
            res = hora_marcada.hour - tuhora.hour
            minutos = res * 60 
            if hora_marcada.minute == tuhora.minute:
                print(f"Llegaste a una hora exacta y tardaste {minutos} minutos")
                
                return minutos
            else:
                total = hora_marcada.minute + minutos
                print(f"Llegaste tarde {total}")
                return total

        elif tuhora.hour == hora_marcada.hour:
            if tuhora.minute == hora_marcada.minute:
                print(f"Llegaste justo a las {tuhora.strftime('%H:%M')}")
            else:
                print("Son las 8 pero")
                total = hora_marcada.minute
                print(f"Llegaste {total} minutos tarde")
                return total

        else:
            print("Llegaste antes")
            res = tuhora.hour - hora_marcada.hour
            min = res * 60
            p = 60 - hora_marcada.minute
            total = min + p - 60
            print(f"Llegaste {total} minutos antes")
            return total
    else:
        return False
        


def generarasistencia(nombre, tardanza):
    dias = datetime.now().date().day
    uni = {}
    for i in range(1,dias+1):
        rangomenor = 60 - tardanza
        rangomayor = 60 + tardanza
        minutos = random.randint(rangomenor,rangomayor)
        o = str(i)
        fechadehoy = o+"/06/2022"

        if minutos > 60:
            a = minutos - 60
            uni[fechadehoy] = a
            asistencia[nombre]["Junio"]= uni
            
            
        elif minutos == 60:
            a = 0
            uni[fechadehoy]=a
            asistencia[nombre]["Junio"]= uni
        else:
            a=0
            uni[fechadehoy]=a
            asistencia[nombre]["Junio"]= uni
        if i == dias:
            uni[fechadehoy] = tardanza
            asistencia[nombre]["Junio"] = uni
