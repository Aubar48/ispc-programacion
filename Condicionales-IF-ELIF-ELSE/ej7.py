"""
Introducir los lados de un triángulo y visualizar por pantalla si dicho
triángulo es equilátero, isósceles o escaleno.
"""

def tipo_triangulo(a, b, c):
    if a == b == c:
        return "equilátero"
    elif a == b or a == c or b == c:
        return "isósceles"
    else:
        return "escaleno"

def main():
    print("Ingrese las longitudes de los lados del triángulo:")
    lado1 = float(input("Lado 1: "))
    lado2 = float(input("Lado 2: "))
    lado3 = float(input("Lado 3: "))

    tipo = tipo_triangulo(lado1, lado2, lado3)
    print(f"El triángulo es {tipo}.")

if __name__ == "__main__":
    main()
