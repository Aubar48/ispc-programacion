"""
9 - Anagrama. Escribe una función que reciba dos palabras y retorne
verdadero o falso según sean o no anagramas.
● Un Anagrama consiste en formar una palabra reordenando TODAS las letras de
otra palabra inicial.
● NO hace falta comprobar que ambas palabras existen.
● Dos palabras exactamente iguales no son anagrama.
palabra1: Sergio
palabra2: Riesgo
true
"""

def son_anagramas(palabra1, palabra2):
    # Convertir ambas palabras a minúsculas y eliminar espacios en blanco
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")
    
    # Verificar si la longitud de las palabras es la misma
    if len(palabra1) != len(palabra2):
        return False
    
    # Ordenar las letras de ambas palabras y comparar si son iguales
    return sorted(palabra1) == sorted(palabra2)

# Ejemplo de uso
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
print(son_anagramas(palabra1, palabra2))  # Output: True
