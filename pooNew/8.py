"""
Compra de Productos. Escribe un programa de consola para gestionar la compra de
productos. Cada producto se define por: id (autoincremental), nombre, caducidad y
precio que estará sujeto a la la fecha de caducidad como sigue:
● Si le quedan entre 3 y 5 días, se reduce un 40%
● Si le quedan menos de 3 dias, se reduce un 70%
● No se podrán vender productos vencidos.
"""

import datetime

class Producto:
    def __init__(self, id, nombre, caducidad, precio):
        self.id = id
        self.nombre = nombre
        self.caducidad = caducidad
        self.precio = precio

    def precio_con_descuento(self):
        hoy = datetime.date.today()
        dias_restantes = (self.caducidad - hoy).days
        
        if dias_restantes < 0:
            return 0  # Producto vencido
        elif 3 <= dias_restantes <= 5:
            return self.precio * 0.60
        elif dias_restantes < 3:
            return self.precio * 0.30
        else:
            return self.precio

    def __str__(self):
        return f"{self.nombre} (ID: {self.id}) - Caducidad: {self.caducidad} - Precio: {self.precio_con_descuento():.2f}"

class GestionCompra:
    def __init__(self):
        self.productos = []
        self.id_counter = 1

    def agregar_producto(self, nombre, caducidad, precio):
        producto = Producto(self.id_counter, nombre, caducidad, precio)
        self.productos.append(producto)
        self.id_counter += 1

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def comprar_producto(self, id):
        producto = next((p for p in self.productos if p.id == id), None)
        if producto:
            precio = producto.precio_con_descuento()
            if precio > 0:
                print(f"Compraste {producto.nombre} por {precio:.2f}")
                self.productos.remove(producto)
            else:
                print("El producto está vencido y no puede ser comprado.")
        else:
            print("Producto no encontrado.")

def main():
    gestion = GestionCompra()
    
    # Ejemplos de productos
    gestion.agregar_producto("Leche", datetime.date(2024, 8, 10), 1.50)
    gestion.agregar_producto("Pan", datetime.date(2024, 8, 5), 2.00)
    gestion.agregar_producto("Yogur", datetime.date(2024, 8, 2), 1.00)
    
    while True:
        print("\nOpciones:")
        print("1. Mostrar productos")
        print("2. Comprar producto")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            gestion.mostrar_productos()
        elif opcion == '2':
            id = int(input("Introduce el ID del producto a comprar: "))
            gestion.comprar_producto(id)
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
