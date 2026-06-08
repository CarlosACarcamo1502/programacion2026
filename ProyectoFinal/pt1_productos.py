"""Establecimiento de datos de productos"""
# base del código por establecer

class Producto:
    """Datos del producto deseado."""

    def __init__(self):
        self.nombre_p = ""
        self.precio = 0
        self.meses = 0

    def datos_producto(self):
        """ingreso de datos"""
        while True:
            self.nombre_p = input("Ingrese el nombre del producto: ")
            try:
                float(self.nombre_p)
                print("Error: ingrese texto, no un valor númerico")
            except ValueError:
                break
        
        while True:
            try:
                self.precio = float(input("Ingrese el precio del producto: "))
                break
            except ValueError:
                print("Error: intrese un dato númerico, no texto")
        
        while True:
            try:
                self.meses = float(input("Ingrese la cantidad de meses del pago: "))
                break
            except ValueError:
                print("Error: intrese un dato númerico entero, no texto, ni números decimales")

    def obtener_descripcion(self):
        """Devuelve la descripción del producto."""
        
        return f'{self.nombre_p}, ${self.precio}, {self.meses}'

    def calcular_pago_mes(self):
        """Calculo simple del pago mensaul por producto"""
        return self.precio / self.meses
