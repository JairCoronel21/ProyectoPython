import webbrowser,pyautogui
from time import sleep
def videofinal():
    webbrowser.open("https://www.youtube.com/watch?v=HO73gUhiYe0#t=7m57s")
    sleep(7)
    for i in range(1):
        pyautogui.click()
        pyautogui.press("f")
        sleep(22)
        pyautogui.hotkey("ctrl","w")