
@author: ccarcamo

class Cuenta: 
    def _init_(self, ctd, t):
        self.cantidad=ctd
        self.tipo=t

  def printdetails(self):
      print ("Desde el método")

      print ("cantidad:", self.cantidad)
      print ("tipo:", self.tipo)
