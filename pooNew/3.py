"""
Producto. Crea una clase Producto con los siguientes atributos: Nombre, Precio y
Stock siendo obligatorios sólo los atributos Nombre y Precio. El Stock debe comenzar
con 0. Define métodos para actualizar el stock, para calcular el total del inventario y
para ver los datos. Además, escribe una aplicación de consola que permita al usuario:
1- actualizar el stock y 2- calcular inventario hasta que decida detenerse. Al finalizar
deberá mostrar los datos del producto, stock e inventario final
"""

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.stock = 0

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def calcular_inventario(self):
        return self.stock * self.precio

    def ver_datos(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Inventario: {self.calcular_inventario()}"

def main():
    nombre = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio del producto: "))
    
    producto = Producto(nombre, precio)
    
    while True:
        print("\nMenú:")
        print("1. Actualizar stock")
        print("2. Calcular inventario")
        print("3. Ver datos del producto")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            cantidad = int(input("Introduce la cantidad para actualizar el stock: "))
            producto.actualizar_stock(cantidad)
            print(f"Stock actualizado. Nuevo stock: {producto.stock}")
        elif opcion == "2":
            inventario = producto.calcular_inventario()
            print(f"El valor total del inventario es: {inventario}")
        elif opcion == "3":
            datos = producto.ver_datos()
            print(datos)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
    
    # Mostrar datos finales del producto
    datos_finales = producto.ver_datos()
    print("\nDatos finales del producto:")
    print(datos_finales)

if __name__ == "__main__":
    main()
