class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: No se puede dividir entre cero."

if __name__ == "__main__":
    # Crear una instancia de la calculadora
    mi_calculadora = Calculadora()
    # Realizar operaciones
    print("Suma:", mi_calculadora.sumar(5, 3))
    print("Resta:", mi_calculadora.restar(10, 4))
    print("Multiplicación:", mi_calculadora.multiplicar(2, 6))
    print("División:", mi_calculadora.dividir(15, 3))
