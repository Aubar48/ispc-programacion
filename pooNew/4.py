"""
Cuenta Bancaria. Crea una clase CuentaBancaria con los siguientes atributos
obligatorios: número de cuenta, nombre y apellido. El saldo debe comenzar con
100.000. Agrega e implementa métodos para: 1- depositar (debe aceptar un valor
entero y sumarlo al saldo), 2- retirar (debe aceptar un valor entero y restarlo al saldo
sólo si hay dinero suficiente para retirar en la cuenta) y 3- ver saldo. Además, escribe
una aplicación de consola que permita al usuario depositar, retirar o ver saldo hasta
que decida detenerse. Al finalizar deberá mostrar los datos de la cuenta y el saldo.
"""

class CuentaBancaria:
    def __init__(self, numero_cuenta, nombre, apellido):
        self.numero_cuenta = numero_cuenta
        self.nombre = nombre
        self.apellido = apellido
        self.saldo = 100000

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Has depositado {cantidad}. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Has retirado {cantidad}. Saldo actual: {self.saldo}")
        else:
            print("No hay suficiente dinero para retirar o la cantidad es inválida.")

    def ver_saldo(self):
        print(f"Saldo actual: {self.saldo}")

def main():
    numero_cuenta = input("Introduce el número de cuenta: ")
    nombre = input("Introduce el nombre: ")
    apellido = input("Introduce el apellido: ")
    
    cuenta = CuentaBancaria(numero_cuenta, nombre, apellido)
    
    while True:
        print("\nElige una opción:")
        print("1 - Depositar")
        print("2 - Retirar")
        print("3 - Ver saldo")
        print("4 - Salir")
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            cantidad = int(input("Introduce la cantidad a depositar: "))
            cuenta.depositar(cantidad)
        elif opcion == "2":
            cantidad = int(input("Introduce la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        elif opcion == "3":
            cuenta.ver_saldo()
        elif opcion == "4":
            print("\nDatos de la cuenta:")
            print(f"Número de cuenta: {cuenta.numero_cuenta}")
            print(f"Nombre: {cuenta.nombre}")
            print(f"Apellido: {cuenta.apellido}")
            print(f"Saldo final: {cuenta.saldo}")
            break
        else:
            print("Opción no válida, por favor elige de nuevo.")

if __name__ == "__main__":
    main()
