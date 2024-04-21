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