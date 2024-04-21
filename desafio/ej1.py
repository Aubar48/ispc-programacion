"""
1- Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el
número con los dígitos en orden inverso:
"""
while True:
    try:
        numero = int(input("Ingrese un número entero: "))
        if 100 <= numero <= 999:
            # Calcular los dígitos y el número invertido
            digitoUno = numero // 100 % 10
            digitoDos = numero // 10 % 10
            digitoTres = numero % 10
            invertido = digitoTres * 100 + digitoDos * 10 + digitoUno
            break  # Salir del bucle si se ingresó un número entero
        else:
            print(
                "Ingrese un número entero distinto, de tres digitos. Vuelva a intentarlo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Imprimir el número invertido
print("El número invertido es:", invertido)
