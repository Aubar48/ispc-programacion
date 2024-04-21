"""
Realice un programa que lea tres números, muestre cuál es el mayor y
determine si es par o impar.
"""

def determinar_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

def main():
    print("Ingrese tres números:")
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))
    num3 = float(input("Número 3: "))

    mayor = max(num1, num2, num3)

    print(f"El mayor número es: {mayor}")
    print(f"{mayor} es {determinar_par_o_impar(mayor)}")

if __name__ == "__main__":
    main()
