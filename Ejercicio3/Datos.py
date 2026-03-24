
class Datos:
    def __init__(self, nombre, precio, interes, meses):
        self.nombre = nombre
        self.precio = precio
        self.interes = interes
        self.meses = meses

    def calculo(self):
        self.pagomensual = self.precio * (1 + self.interes / 100) / self.meses

    def mostrar(self):
        print(self.pagomensual)

#intento de colocar los nombres de las cosas
  nombre = input("Nombre del producto")
  precio = float(input("¿Qué precio tiene el producto que adquiriste?")) 
  interes = float(input("¿Cuánto es el interes de tu credito?")) 
  meses = int(input("¿En cuántos meses es el pago?")) 

def __str__(self):
    return f"""""
Producto: {self.nombre}
Precio: {self.precio}
Interés: {self.interes}%
Meses: {self.meses}
Pago mensual: {self.pagomensual}
"""""
