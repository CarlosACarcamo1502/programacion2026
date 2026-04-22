class Cuenta:

  def desicion(self, salario, meses, precio):
    if salario*0.2 < precio/meses:
        print("Puedes comprarlo")
    else:
        print("No deberías comprarlo, podrías endeudarte de más")

  def calculo(self):
      self.pagomensual = self.precio * (1 + self.interes / 100) / self.meses

  def mostrar(self):
      print(self.pagomensual)

  def __str__(self):
      return "El pago mensual de tu producto será de:" + str(self.pagomensual)
