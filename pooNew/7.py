"""
Expocoches. Escribe un programa de consola para gestionar la venta de entradas (no
numeradas) de Expocoches que tiene 3 zonas, la sala principal con 1000 entradas
disponibles, la zona de compra-venta con 200 entradas disponibles y la zona vip con
25 entradas disponibles. Hay que controlar que existen entradas antes de venderlas.
Define las clase Zona con sus atributos y métodos correspondientes y crea un
programa de consola que permita vender las entradas.
El menú del programa debe ser el siguiente: 1- Mostrar número de entradas libres,
2- Vender entradas y 3- Salir
Cuando elegimos la opción 2, se nos debe preguntar para qué zona queremos las
entradas y cuántas queremos. Lógicamente, el programa debe controlar que no se
puedan vender más entradas de la cuenta
"""

class Zona:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.entradas_disponibles = capacidad

    def mostrar_entradas_libres(self):
        return self.entradas_disponibles

    def vender_entradas(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return False
        
        if cantidad > self.entradas_disponibles:
            print(f"No hay suficientes entradas en la zona {self.nombre}. Solo quedan {self.entradas_disponibles} entradas disponibles.")
            return False
        
        self.entradas_disponibles -= cantidad
        print(f"Se han vendido {cantidad} entradas en la zona {self.nombre}.")
        return True


def menu():
    print("1- Mostrar número de entradas libres")
    print("2- Vender entradas")
    print("3- Salir")


def main():
    zona_principal = Zona("Principal", 1000)
    zona_compra_venta = Zona("Compra-Venta", 200)
    zona_vip = Zona("VIP", 25)

    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print(f"Entradas libres en la zona Principal: {zona_principal.mostrar_entradas_libres()}")
            print(f"Entradas libres en la zona Compra-Venta: {zona_compra_venta.mostrar_entradas_libres()}")
            print(f"Entradas libres en la zona VIP: {zona_vip.mostrar_entradas_libres()}")

        elif opcion == "2":
            zona = input("Selecciona la zona (Principal, Compra-Venta, VIP): ")
            cantidad = int(input("¿Cuántas entradas deseas vender?: "))

            if zona == "Principal":
                zona_principal.vender_entradas(cantidad)
            elif zona == "Compra-Venta":
                zona_compra_venta.vender_entradas(cantidad)
            elif zona == "VIP":
                zona_vip.vender_entradas(cantidad)
            else:
                print("Zona no válida.")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción correcta.")

if __name__ == "__main__":
    main()
