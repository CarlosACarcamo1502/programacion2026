"""Lista de compras deseadas"""
# Creación de lista de acuerdo a los productos disponibles

from pt1_productos import *

class ListaDeseos:
    """Creación de la lista de deseos de mi aplicación"""

    def __init__(self):
        self.productos = []

    def agregar_e(self, producto):
        """Agregar un producto a la lista"""
        self.productos.append(producto)

    def eliminar_e(self):
        """Elimina el último elemento de la lista"""
        if self.productos:
            self.productos.pop()
        else:
            print("No hay datos en la lista")

    def borrar_todo(self):
        """Elimina toda la lista añadida"""
        self.productos.clear()

    def mostrar_lista(self):
        if not self.productos:
            print("La lista se encuentra vacia")
        else:
            for producto in self.productos:
                print(producto.obtener_descripcion())
