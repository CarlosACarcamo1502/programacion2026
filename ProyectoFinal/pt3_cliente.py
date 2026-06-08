"""Datos del cliente"""
#Lista de datos del cliente
#A partir de aqui establezco si vale la pena realizar la compra o no
#de acuerdo a las ganancias que se pueden obtener

class Cliente:
    """Datos personales del cliente"""

    def datos_cliente(self):
        """Esta parte es para ingresar los datos para los calculos"""
        
        self.interes = float(input("Ingresa el interes de tu tarjeta en decimal (Ejemplo: 0.05=5%): "))
        self.salario = float(input("Ingrese su salario: "))
        print("Datos guardados")

    def __str__(self):
        return (
            f"\nInterés: {self.interes}"
            f"\nSalario: {self.salario}"
        )
