"""
Área y Perímetro. Crea una clase Rectángulo que permita calcular su área y su
perímetro. Además, crea en una aplicación de consola que permita al usuario crear
un objeto Perímetro y realizar los cálculos.
"""

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

def main():
    print("Bienvenido a la aplicación de cálculo de área y perímetro de un rectángulo.")
    
    try:
        ancho = float(input("Por favor, introduce el ancho del rectángulo: "))
        alto = float(input("Por favor, introduce el alto del rectángulo: "))
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número.")
        return
    
    rectangulo = Rectangulo(ancho, alto)
    
    area = rectangulo.calcular_area()
    perimetro = rectangulo.calcular_perimetro()
    
    print(f"\nEl área del rectángulo es: {area}")
    print(f"El perímetro del rectángulo es: {perimetro}")

if __name__ == "__main__":
    main()
