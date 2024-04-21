"""
Realice un programa que lea dos números y diga cuál es el mayor.
"""
print("Ingrese dos valores numericos para determinar cual es mayor")
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if numero1 > numero2:
    print("%d El primer numero es mayor que el segundo numero %d" % (numero1, numero2))
else:
    print("%d El segundo numero es mayor que el primer numero %d" % (numero2, numero1))
    
print("Primer numero ingresado: ", numero1)
print("Segundo numero ingresado: ", numero2)
