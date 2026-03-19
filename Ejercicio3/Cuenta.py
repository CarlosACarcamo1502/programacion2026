
class Datos:
    def __init__(self, nombre, precio, interes, meses):
        self.nombre = nombre
        self.precio = precio
        self.interes = interes
        self.meses = meses

#intento de colocar los nombres de las cosas
  input("Nombre del producto") = nombre
  input("¿Qué precio tiene el producto que adquiriste?") = precio
  input("¿Cuánto es el interes de tu credito?") = interes
  input("¿En cuántos meses es el pago?") = meses

    def calculo(self):
        self.pagomensual = self.precio * (1 + self.interes / 100) / self.meses

    def mostrar(self):
        print(self.pagomensual)
