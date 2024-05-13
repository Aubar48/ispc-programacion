class Forma:
    def __init__(self, nombre):
        self.nombre = nombre

    def dibujar(self):
        return "dibuja forma"  # o pass

class Rectangulo(Forma):
    def dibujar(self):
        return "dibuja un rectángulo!"

class Circulo(Forma):
    def dibujar(self):
        return "dibuja un círculo!"

forma1 = Rectangulo("R1")
forma2 = Circulo("C1")

if __name__ == "__main__":
    print(forma1.dibujar())  # Imprime "dibuja un rectángulo!"
    print(forma2.dibujar())  # Imprime "dibuja un círculo!"
