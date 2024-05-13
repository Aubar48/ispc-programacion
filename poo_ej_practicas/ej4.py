class Operacion:
    def __init__(self, valorA, valorB):
        self.__valorA = valorA
        self.__valorB = valorB

    @property
    def valorA(self):
        return self.__valorA

    @valorA.setter
    def valorA(self, valor):
        self.__valorA = valor

    @property
    def valorB(self):
        return self.__valorB

    @valorB.setter
    def valorB(self, valor):
        self.__valorB = valor

class Suma(Operacion):
    def __init__(self, valorA, valorB):
        super().__init__(valorA, valorB)

    def sumar(self):
        return self.valorA + self.valorB

class Resta(Operacion):
    def __init__(self, valorA, valorB):
        super().__init__(valorA, valorB)

    def restar(self):
        return self.valorA - self.valorB

# Crear una instancia de la clase Suma
mi_suma = Suma(10, 5)
# Llamar al método sumar
resultado = mi_suma.sumar()
# Imprimir el resultado en consola
print("El resultado es:", resultado)

# Crear una instancia de la clase Resta
mi_resta = Resta(10, 5)
# Llamar al método restar
resultado = mi_resta.restar()
# Imprimir el resultado en consola
print("El resultado es:", resultado)
