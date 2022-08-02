import pyautogui, webbrowser
from time import sleep
import random

def asdasd(numero):
    webbrowser.open(f'https://web.whatsapp.com/send?phone="+51{numero}"')
    p = random.randint(9999,99999)
    p = str(p)
    sleep(10)
    for i in range(1):
        pyautogui.typewrite('Su codigo de verificacion es: '+p)
        pyautogui.press("enter")
    return p 
