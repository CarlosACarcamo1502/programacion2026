class Datos:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calculo(self):
        self.pagomensual = self.precio * (1 + self.interes / 100) / self.meses

    def mostrar(self):
        print(self.pagomensual)
