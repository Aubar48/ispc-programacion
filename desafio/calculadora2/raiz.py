import math
def raiz():
    while True:
        try:
            num1 = float(input("Ingrese el valor para conocer su raiz cuadrada: "))
            raiz = math.sqrt(num1)
            return raiz
        except Exception as e:
            print("Por favor, ingrese un número válido. Error: ", str(e))
