
from Datos import *

class: Main
  pass



print("Su cuenta mensual será de:")

Datos1 = Datos("Switch 2", 8000, 15, 10)
print(Datos1.nombre)
print(Datos1.precio)
print(Datos1.interes)
print(Datos1.meses)

Datos1.calculo()
print(Datos1.pagomensual)
