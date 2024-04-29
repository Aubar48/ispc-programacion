"""
Desafío. Resolver utilizando funciones con argumentos arbitrarios.
1. Escribe una función que tome una cantidad variable de cadenas y las concatene
en una sola cadena. Ej. “Hola Mundo”
2. Escribe una función que muestre la cantidad de argumentos con nombre
enviados.
3. Escribe una función que calcule el promedio de una cantidad variable de números.

"""

# 1. Concatenar una cantidad variable de cadenas:


def concatenar_cadenas(*args):
    return ' '.join(args)


# Ejemplo de uso:
# Salida: "Hola Mundo desde Python"
print(concatenar_cadenas("Hola", "Mundo", "desde", "Python"))

# 2. Mostrar la cantidad de argumentos con nombre enviados:


def contar_argumentos_con_nombre(**kwargs):
    return len(kwargs)


# Ejemplo de uso:
print(contar_argumentos_con_nombre(
    nombre="Juan", edad=30, ciudad="Madrid"))  # Salida: 3

# 3. Calcular el promedio de una cantidad variable de números:


def promedio(*numeros):
    return sum(numeros) / len(numeros)


# Ejemplo de uso:
print(promedio(5, 8, 12, 3))  # Salida: 7.0
