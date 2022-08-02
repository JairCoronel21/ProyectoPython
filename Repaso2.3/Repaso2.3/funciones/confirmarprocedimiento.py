'''import msvcrt
def variable():
    while True:
        print("Para confirmar presiona 'enter' o 'esc' para salir")

        key = msvcrt.getch()
        key = str(key)

        esc = b'\x1b'
        esc = str(esc)

        enter = b'\r'
        enter = str(enter)

        if key == esc:
            print("presionaste escape")
            return False
        elif key == enter:
            print("Presionaste enter")
            return True
        else:
            print("presionaste cualquier cosa")'''