from suma import suma
from resta import resta
from multiplicar import multiplicar
from raiz import raiz
from dividir import dividir
from potencia import potencia
from cociente import cociente


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
