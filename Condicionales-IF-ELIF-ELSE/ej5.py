"""
Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo
el cambio de dólares a pesos y que sea el usuario quién decida qué tipo
de cambio quiere, si de dólares a pesos o viceversa.
"""

def pesos_a_dolares(cantidad):
    return cantidad / 20  # Suponiendo un tipo de cambio de 1 dólar = 20 pesos

def dolares_a_pesos(cantidad):
    return cantidad * 20  # Suponiendo un tipo de cambio de 1 dólar = 20 pesos

def main():
    print("Bienvenido al conversor de moneda")
    opcion = input("¿Qué tipo de cambio desea realizar? (1: Pesos a Dólares, 2: Dólares a Pesos): ")

    if opcion == "1":
        cantidad_pesos = float(input("Ingrese la cantidad de pesos: "))
        cantidad_dolares = pesos_a_dolares(cantidad_pesos)
        print(f"{cantidad_pesos} pesos equivale a {cantidad_dolares} dólares.")
    elif opcion == "2":
        cantidad_dolares = float(input("Ingrese la cantidad de dólares: "))
        cantidad_pesos = dolares_a_pesos(cantidad_dolares)
        print(f"{cantidad_dolares} dólares equivale a {cantidad_pesos} pesos.")
    else:
        print("Opción no válida. Por favor, ingrese 1 o 2.")

if __name__ == "__main__":
    main()
