"""
Funciones con argumentos especiales
Como hemos visto los argumentos pueden enviarse en una función por posición o por
palabra clave. Sin embargo, y para ayudar a la legibilidad y el rendimiento identificar cómo
se pueden enviar los argumentos. Así un programador con sólo mirar la definición de la
función podrá determinar si los mismos deben pasarse por posición o por palabra clave.
Para ello, se utilizan los símbolos / y * en la definición de la función como sigue:

donde los símbolos / y * indican cómo debe enviarse el argumento.

Desafío: De lo anterior, podemos inferir que podemos especificar funciones que
admitan argumentos únicamente posicionales o bien, funciones que admitan argumentos
únicamente con palabras claves. Escribe un ejemplo de cada uno y luego intenta romper
la regla especificada en la definición de la función.
"""

# Función con argumentos únicamente posicionales:
def area_rectangulo(base, altura, /):
    return base * altura
# Intento romper la regla pasando un argumento por palabra clave
print(area_rectangulo(base=5, altura=3))  # Esto dará un error


# Función con argumentos únicamente por palabra clave:
def saludar(nombre, *, mensaje="Hola"):
    return f"{mensaje}, {nombre}!"
# Intento romper la regla pasando un argumento posicional
print(saludar("Juan", mensaje="¡Buen día!"))  # Esto dará un error


"""
Argumentos arbitrarios posicionales (*args). Se definen con un asterisco (*)
antes del nombre del parámetro y permiten pasar un número variable de argumentos
posicionales a la función.
Los argumentos se envían en una tupla dentro de la función.
Ejemplo:
"""


def sumatoria(*args):
    total = sum(args)
    return total


if __name__ == "__main__":
    resultado = sumatoria(1, 2, 3, 4)
print(resultado)  # Imprime: 10

"""
Argumentos arbitrarios con palabra clave (kwargs). Se definen con dos
asteriscos (**) antes del nombre del parámetro y permiten pasar un número variable
de argumentos con nombre (clave-valor) a la función.
Los argumentos se agrupan en un diccionario dentro de la función.
"""


def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


if __name__ == "__main__":
    mostrar_info(nombre="Camila", apellido="Alonso",
                 ciudad="Córdoba")
# Imprime:
# nombre: Camila
# apellido: Alonso
# ciudad: Córdoba
