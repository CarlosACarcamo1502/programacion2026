class Datos:
    def __init__(self, nombre, precio, interes, meses, salario):
        self.nombre = nombre
        self.precio = precio
        self.interes = interes
        self.meses = meses
        self.salario = salario

  def __stf__(self):
        tmp = "Nombre:" + str(self.nombre)
        tmp += "\nPrecio:" + str(self.precio)
        tmp += "\nEdad:" + str(self.interes)
        tmp += "\nMeses:" + str(self.meses)
        tmp += "\nSalario" + str(self.salario)
        return tmp
