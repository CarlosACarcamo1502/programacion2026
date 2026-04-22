class: Cliente
  def __init__(self, nombre, precio, interes, meses):
      self.nombre = nombre
      self.precio = precio
      self.interes = interes
      self.meses = meses

  def __stf__(self):
      tmp = "Nombre:" + str(self.nombre)
      tmp += "\nPrecio:" + str(self.precio)
      tmp += "\nEdad:" + str(self.interes)
      tmp += "\nMeses:" + str(self.meses)
  return tmp
