def dividir():
    while True:
        try:
            num1 = float(input("Valor numero 1: "))
            num2 = float(input("Valor numero 2: "))
            resultado = num1 / num2 if num1 != 0 and num2 != 0 else None
            if resultado is None:
                raise ValueError("No se puede dividir entre cero.")
            else:
                return resultado
        except Exception as e:
            print("Por favor, ingrese números válidos. Error:", str(e))


