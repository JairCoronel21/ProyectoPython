'''import os
import random
import win32com.client as win32

olApp = win32.Dispatch('Outlook.Application')
olNS = olApp.GetNameSpace('MAPI')

def mensajecorreo(correo):
    k = random.randint(9999, 99999)
    k = str(k)
    
    mailItem = olApp.CreateItem(0)
    mailItem.Subject = 'CODIGO DE QSERVICES'
    mailItem.BodyFormat = 1
    mailItem.Body = "Codigo de seguridad: " + k
    mailItem.To = correo
    mailItem.Display()
    mailItem.Save()
    mailItem.Send()
    
    return k'''