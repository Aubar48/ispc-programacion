"""
3- Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no.
"""
numero=int(input("Ingrese un numero: "))

while True:
    try:
        numero = int(input("Ingrese un número entero: "))
        break  # Salir del bucle si se ingresó un número entero
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

def es_primo(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

resultado = es_primo(numero)
if resultado:
    print("El número es primo.")
else:
    print("El número no es primo.")
