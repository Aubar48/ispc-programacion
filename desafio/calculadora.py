import math


def suma():
    while True:
        try:
            print("Ingrese dos valores para sumarlos: ")
            num1 = float(input("Valor numero 1: "))
            num2 = float(input("Valor numero 2: "))
            resultado = num1 + num2
            return resultado
        except Exception as e:
            print("Por favor, ingrese un número válido. Error: ", str(e))


def resta():
    while True:
        try:
            print("Ingrese dos valores para restarlos: ")
            num1 = float(input("Valor numero 1: "))
            num2 = float(input("Valor numero 2: "))
            resultado = num1 - num2
            return resultado
        except Exception as e:
            print("Por favor, ingrese un número válido. Error: ", str(e))


def multiplicar():
    while True:
        try:
            print("Ingrese dos valores para multiplicarlos: ")
            num1 = float(input("Valor numero 1: "))
            num2 = float(input("Valor numero 2: "))
            if num1 == 0 or num2 == 0:
                raise ValueError("No se puede multiplicar por cero.")
            else:
                resultado = num1 * num2
                return resultado
        except Exception as e:
            print("Por favor, ingrese un número válido. Error: ", str(e))


def dividir():
    while True:
        try:
            print("Ingrese dos valores para dividirlos: ")
            num1 = float(input("Valor numero 1: "))
            num2 = float(input("Valor numero 2: "))
            if num1 == 0 or num2 == 0:
                raise ValueError("No se puede dividir entre cero.")
            else:
                resultado = num1 / num2
                return resultado
        except Exception as e:
            print("Por favor, ingrese un número válido. Error: ", str(e))


def raiz():
    while True:
        try:
            num1 = float(
                input("Ingrese el valor para conocer su raiz cuadrada: "))
            raiz = math.sqrt(num1)
            return raiz
        except Exception as e:
            print("Por favor, ingrese un número válido. Error: ", str(e))


def potencia():
    while True:
        try:
            print("Ingrese dos valores para saber la potencia: ")
            num1 = float(input("Valor numero 1: "))
            num2 = float(input("Valor numero 2: "))
            if num1 == 0 or num2 == 0:
                raise ValueError("No se puede hacer potencia de cero.")
            else:
                resultado = num1 ** num2
                return resultado
        except Exception as e:
            print("Por favor, ingrese un número válido. Error: ", str(e))


def cociente():
    while True:
        try:
            print("Ingrese dos valores para saber el cociente: ")
            num1 = float(input("Valor numero 1: "))
            num2 = float(input("Valor numero 2: "))
            if num1 == 0 or num2 == 0:
                raise ValueError("No se puede hacer cociente de cero.")
            else:
                resultado = num1 // num2
                return resultado
        except Exception as e:
            print("Por favor, ingrese un número válido. Error: ", str(e))


def menu():
    print("\n\tMENU PRINCIPAL")
    print("1. Sumar numeros.")
    print("2. Restar numeros.")
    print("3. Multiplicar numeros.")
    print("4. Dividir numeros.")
    print("5. Raiz cuadrada de un numero.")
    print("6. Potencia de un numero.")
    print("7. Cociente entre dos numeros.")
    print("0. Salir del codigo. \n")


while True:
    try:
        menu()
        opcion = int(input("Seleccione una opción del menú: "))
        if opcion == 0:
            break
        elif opcion == 1:
            print("La suma es: ", suma())
        elif opcion == 2:
            print("La resta es: ", resta())
        elif opcion == 3:
            print("El producto es: ", multiplicar())
        elif opcion == 4:
            print("La división es: ", dividir())
        elif opcion == 5:
            print("La raíz cuadrada es: ", raiz())
        elif opcion == 6:
            print("La potencia es: ", potencia())
        elif opcion == 7:
            print("El cociente es: ", cociente())
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
    except Exception as e:
        print("Por favor, ingrese un número entero válido. Error: ", str(e))
