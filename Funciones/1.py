"""
Desafío!. Resolver utilizando funciones lambda.
1. Crea una función anónima (lambda) que calcule el promedio de un arreglo de
números enteros.
2. Escribe una función anónima que calcule el factorial dado un número entero.
3. Crea una función anónima que permita conocer si un número es par.
4. Dado un arreglo de números enteros, crea una función anónima que retorne una
lista con los números pares.
5. Utiliza una función lambda para elevar al cuadrado cada elemento de una lista de
números.
"""

# 1. Promedio de un arreglo de números enteros
promedio = lambda arreglo: sum(arreglo) / len(arreglo)

# 2. Factorial dado un número entero
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# 3. Función para conocer si un número es par
es_par = lambda n: n % 2 == 0

# 4. Retornar una lista con los números pares de un arreglo
numeros_pares = lambda arreglo: list(filter(lambda x: x % 2 == 0, arreglo))

# 5. Elevar al cuadrado cada elemento de una lista de números
cuadrados = lambda lista: list(map(lambda x: x ** 2, lista))
