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
