while True:
    try:
        numero = int(input("Ingrese un número entero: "))
        if 100 <= numero <= 999:
            # Crear un diccionario con los índices de los dígitos originales
            digitos_originales = {
                0: numero // 100 % 10,
                1: numero // 10 % 10,
                2: numero % 10
            }
            # Construir el número invertido utilizando los índices
            invertido = digitos_originales[2] * 100 + digitos_originales[1] * 10 + digitos_originales[0]
            break  # Salir del bucle si se ingresó un número entero
        else:
            print("Ingrese un número entero distinto, de tres dígitos. Vuelva a intentarlo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Imprimir el número invertido
print("El número invertido es:", invertido)
