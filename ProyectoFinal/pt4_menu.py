"""Seleccionador de opciones a ejecutar"""
#queria que esta parte del código no fuese tan larga, pero al final termine etendiendola 
#por cambios sobre la ultima revisión que hice en VS.Code

from pt1_productos import *
from pt2_lista_deseos import *
from pt3_cliente import *

class Menu:
    """Ejecución del Menú"""

    def __init__(self):
        self.producto = Producto()
        self.lista = ListaDeseos()
        self.cliente = Cliente()
        self.presupuesto = 0

    def cotizar(self):
        """Establecimiento de cotización"""
        print("Llena los datos")
        self.cliente.datos_cliente()
        print(self.cliente)
    
    def ing_producto(self):
        """ Llama al método para ingresar datos de los productos"""
        producto = Producto ()
        producto.datos_producto()
        self.lista.agregar_e(producto)
        print("Se ha añadido correctamente el producto")
    
    def eliminar_producto(self):
        """Eliminación del producto final"""
        self.lista.eliminar_e()
        print("Último producto eliminado")

    def borrar_lista(self):
        """Reseteo de la lista"""
        self.lista.borrar_todo()
        print("Lista eliminada")

    def mostrar_lista(self):
        """mostrar lista""" #este no me quedo del todo bien :( y ya no supe como editarlo de mejor manera sin afectar a las otras partes del código
        if not self.lista.productos:
            print("La lista está vacía")
        else:
            for producto in self.lista.productos:
                print(producto)

    def calcular_pago_total(self):
        """intento de calcular el pago por mes"""
        if not self.lista.productos:
            print("La lista está vacía")
            return

        total_mes = 0
        print("\nPagos mensuales:")

        for producto in self.lista.productos:
            pago = producto.calcular_pago_mes()
            print(f"{producto.nombre_p}: ${pago:.2f}")
            total_mes += pago
        print(f"\nPago mensual total: ${total_mes:.2f}")
        if self.presupuesto == 0:
            print("Primero debes usar la opción 1 para calcular tu presupuesto.")
            return
        if total_mes <= self.presupuesto:
            print("La compra está dentro del presupuesto.")
        else:
            exceso = total_mes - self.presupuesto
            print("La compra excede el presupuesto.")
            print(f"Te excedes por ${exceso:.2f}")
#al final si salio wuuuu

    def seleccionar_opcion(self):
        """Mi operador general, aunque el código esta algo desordenado"""
        while True:
            print("Seleccione que proceso desea realizar")
            print("1. Cotizar cuanta deuda puedo generar con mi salario")
            print("2. Añadir producto a la lista")
            print("3. Eliminar último producto agregado")
            print("4. Eliminar lista")
            print("5. Mostrar lista")
            print("6. Calcular pago por mes")
            print("7. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                    self.cotizar()
                    if self.cliente.salario <= 10000 and self.cliente.interes >= 0.65:
                        self.presupuesto = 1500
                        print("No es recomendable hacer compras con un pago mayor a $1500 pesos al mes por tener el interes muy alto")

                    elif self.cliente.salario <= 6000:
                        self.presupuesto = 0
                        print("No es recomendable hacer compras con deudas")

                    elif self.cliente.salario >= 10000 and self.cliente.interes <= 0.65:
                        self.presupuesto = self.cliente.salario * 0.25
                        print(f"No es recomendable hacer compras con un pago mayor a: {self.presupuesto} pesos al mes")

                    elif self.cliente.salario >= 10000 and self.cliente.interes >= 0.4 and self.cliente.interes <= 0.65:
                        self.presupuesto = self.cliente.salario * 0.25
                        print(f"Tu presupuesto mensual de deuda es de: {self.presupuesto}")

                    elif self.cliente.salario >= 10000 and self.cliente.interes >= 0.65:
                        self.presupuesto = self.cliente.salario * 0.15
                        print(f"Tu presupuesto mensual de deuda es de: {self.presupuesto}")

            elif opcion == "2":
                self.ing_producto()
            
            elif opcion == "3":
                self.eliminar_producto()

            elif opcion == "4":
                self.borrar_lista()

            elif opcion == "5":
                self.mostrar_lista()

            elif opcion == "6":
                self.calcular_pago_total()

            elif opcion == "7":
                print("Gracias por su preferencia al usar la aplicación, ¡suerte con sus finanzas! :) ")
                break

            else:
                print("Opción no válida")

