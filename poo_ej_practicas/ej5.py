class Motor:
    def __init__(self, cilindrada, potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia

    def encender(self):
        print("El motor se ha encendido.")

    def apagar(self):
        print("El motor se ha apagado.")

class Auto:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def set_radio(self, radio):
        self.radio = radio

    def arrancar(self):
        print("El auto ha arrancado.")
        self.motor.encender()

    def parar(self):
        print("El auto se ha detenido.")
        self.motor.apagar()

class Radio:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
