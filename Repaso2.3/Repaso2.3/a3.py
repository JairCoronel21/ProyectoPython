import keyboard
import time
'''a = list()
j = True
numeros = "123456789"
while j == True:
	p = keyboard.read_key()
	if  p == "esc":
		print(p)
		print("You pressed escape")
		j = False
	else:
		if (p.isalpha() or p in numeros) and (not p == "enter") and (not p == "space"):
			print(p)
			a.append(p)
			time.sleep(0.15)
			j = True
		elif p == "enter":
			print(a)
			j = False
		elif p == "space": #no cuenta espacios falta reemplazar cada vez que haya espacio que lo separe osea que si guarde a la lista y cambiarlo dentro de eso, verificar .join .map
			j = True
		else:
			j = True'''
'''
import msvcrt
print("Presione 'esc' para salir...")
key = None
key = msvcrt.getwch()
while key != 'esc':
    p = input("Ingresa algo")
else:
    print()'''

def operation1(param):
  	print("1")
def operation2(param):
  	print("2")
def operation3(param):
  	print("3")

input("Press enter to start operations...")
ret = operation1("Sample Param")
print("\nOperation 1 has been executed successfully.")
input("\n Press enter to start operation 2...")
ret = operation2(ret)
print("Operation 2 has been executed successfully.")
input("\n Press enter to start final operation")
ret = operation3(ret)
print("All operations executed successfully. Returned a value of ", ret)