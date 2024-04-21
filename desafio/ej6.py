"""
6- Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo con tantos renglones como indique el
usuario.
"""
while True:
    try:
        n = int(
            input("Ingrese un número entero para el tamaño del triángulo rectángulo: "))
        if n > 0:
            for i in range(1, n + 1):
                print("*" * i)
            break        
        else:
            print("Por favor, ingrese un número entero positivo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
