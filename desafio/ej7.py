"""
7- La secuencia de Collatz de un número entero se construye de la siguiente forma:
● si el número es par, se lo divide por dos;
● si es impar, se le multiplica tres y se le suma uno;
● La sucesión termina al llegar a uno.
Desarrolle un programa que entregue la secuencia de Collatz de un número entero:
"""

def secuencia_collatz(numero):
    secuencia = [numero]  # Inicializar la secuencia con el número inicial

    while numero != 1:  # La secuencia termina cuando llega a 1
        if numero % 2 == 0:  # Si el número es par
            numero //= 2
        else:  # Si el número es impar
            numero = numero * 3 + 1
        secuencia.append(numero)  # Agregar el siguiente número a la secuencia

    return secuencia

while True:
    try:
        numero = int(
            input("Ingrese un número entero para generar la secuencia de Collatz: "))
        if numero <= 0:
            print("Por favor, ingrese un número entero positivo.")
        else:
            resultado = secuencia_collatz(numero)
            print("La secuencia de Collatz para el número", numero, "es:")
            print(resultado)
        break
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
