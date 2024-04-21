"""
Leer 10 números y obtener la cantidad de mayores y la cantidad de
menores a 100, cuál es el número máximo y cuál es el número mínimo.
"""


def main():
    # Inicializamos las variables para el seguimiento
    cantidad_mayores_100 = 0
    cantidad_menores_100 = 0
    # Inicializamos con el valor negativo más grande posible
    numero_maximo = float('-inf')
    # Inicializamos con el valor positivo más grande posible
    numero_minimo = float('inf')

    # Leer los 10 números
    for i in range(10):
        numero = float(input(f"Ingrese el número {i+1}: "))

        # Determinar si el número es mayor o menor que 100
        if numero > 100:
            cantidad_mayores_100 += 1
        elif numero < 100:
            cantidad_menores_100 += 1

        # Actualizar el número máximo y mínimo
        if numero > numero_maximo:
            numero_maximo = numero
        if numero < numero_minimo:
            numero_minimo = numero

    # Mostrar los resultados
    print(f"Cantidad de números mayores a 100: {cantidad_mayores_100}")
    print(f"Cantidad de números menores a 100: {cantidad_menores_100}")
    print(f"Número máximo: {numero_maximo}")
    print(f"Número mínimo: {numero_minimo}")


if __name__ == "__main__":
    main()
