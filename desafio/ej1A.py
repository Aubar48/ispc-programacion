while True:
    try:
        numero = int(input("Ingrese un número entero: "))  # Convertir la entrada a entero
        if 100 <= numero <= 999:  # Comparar con valores enteros
            invertido = int(str(numero)[::-1])  # Invertir la cadena
            break  # Salir del bucle si se ingresó un número entero válido
        else:
            print("Ingrese un número entero de tres dígitos. Vuelve a intentarlo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Imprimir el número invertido
print("El número invertido es:", invertido)
