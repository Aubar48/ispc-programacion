"""
Realice un programa que lea 4 números y diga cuántos son pares y
cuantos impares y devuelva la sumatoria de los pares.
"""


def contar_pares_impares_y_sumatoria(numeros):
    pares = 0
    impares = 0
    sumatoria_pares = 0

    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
            sumatoria_pares += numero
        else:
            impares += 1

    return pares, impares, sumatoria_pares


def main():
    print("Ingrese 4 números:")
    numeros = []
    for i in range(4):
        numero = int(input(f"Número {i+1}: "))
        numeros.append(numero)

    pares, impares, sumatoria_pares = contar_pares_impares_y_sumatoria(numeros)

    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    print(f"Sumatoria de los números pares: {sumatoria_pares}")


if __name__ == "__main__":
    main()
