from funciones.menus import icono, menuPrincipal
from funciones.redirecciones import redirPrincipal
from funciones.validaciones import validNum4

icono()
menuPrincipal()

opPrincipal = validNum4()
redirPrincipal(opPrincipal)