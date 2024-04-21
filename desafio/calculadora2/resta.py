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