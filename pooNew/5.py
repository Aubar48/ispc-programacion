"""
Kilometraje Recorrido. Crea una clase vehículo que permita llevar el kilometraje
recorrido. Agrega atributos para definir color, marca, modelo y patente del vehículo y
métodos para: 1- conducir el auto (debe aceptar la cantidad de kilómetros y sumarlo
al kilometraje recorrido) y 2- muestre en pantalla los datos del vehículo y el
correspondiente kilometraje. Además, escribe una aplicación de consola que permita
al usuario conducir varios kilómetros y mostrar el kilometraje actual hasta que decida
detenerse. Al finalizar deberá mostrar los datos del vehículo y el kilometraje
recorrido.
"""



class Vehiculo:
    def __init__(self, color, marca, modelo, patente):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.kilometraje = 0

    def conducir(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
        else:
            print("La cantidad de kilómetros debe ser positiva.")

    def mostrar_datos(self):
        print(f"Color: {self.color}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Patente: {self.patente}")
        print(f"Kilometraje: {self.kilometraje} km")

# Aplicación de consola
def main():
    color = input("Introduce el color del vehículo: ")
    marca = input("Introduce la marca del vehículo: ")
    modelo = input("Introduce el modelo del vehículo: ")
    patente = input("Introduce la patente del vehículo: ")

    vehiculo = Vehiculo(color, marca, modelo, patente)

    while True:
        opcion = input("¿Quieres conducir el vehículo? (s/n): ").lower()
        if opcion == 's':
            try:
                kilometros = float(input("Introduce la cantidad de kilómetros a conducir: "))
                vehiculo.conducir(kilometros)
                print(f"Kilometraje actual: {vehiculo.kilometraje} km")
            except ValueError:
                print("Por favor, introduce un número válido de kilómetros.")
        elif opcion == 'n':
            break
        else:
            print("Opción no válida. Por favor, introduce 's' o 'n'.")

    print("\nDatos finales del vehículo:")
    vehiculo.mostrar_datos()

if __name__ == "__main__":
    main()
