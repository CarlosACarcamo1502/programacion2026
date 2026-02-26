@author: ccarcamo

from Cuenta import *

class Main:
    pass


print ("***1. Imprimimos atributos desde el archivo principal")

cuenta1= Cuenta(1000, "debito")

print (cuenta1.cantidad)
print (cuenta1.tipo)

print ("\n\n*** 2. Imprimimos atributos con el método")
cuenta1.printdetails()
