"""
Hacer un programa que permita decidir si dos palabras son iguales o
diferentes. Mostrar mensaje por pantalla.
"""

def verificar_palabras(palabra1, palabra2):
    if palabra1 == palabra2:
        return "iguales"
    else:
        return "diferentes"

def main():
    print("Vamos a verificar si ambas palabras son iguales")
    palabra1 = input("Ingrese la primera letra: ")
    palabra2 = input("Ingrese la segunda letra: ")

    resultado = verificar_palabras(palabra1, palabra2)
    print(f"Las palabras son {resultado}.")
    print(f"Primera palabra: {palabra1}")
    print(f"Segunda palabra: {palabra2}")

if __name__ == "__main__":
    main()
