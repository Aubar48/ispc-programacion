"""
1. Instrumentos Musicales. Crea una clase base llamada Instrumento
con métodos como tocar() y afinar(). Luego, crear subclases para representar
diferentes instrumentos como Guitarra, Piano y Flauta. Implementa métodos
de manera diferente en cada subclase para simular la ejecución y la afinación
de cada instrumento.
"""

class Instrumento:
    def tocar(self):
        pass

    def afinar(self):
        pass

class Guitarra(Instrumento):
    def tocar(self):
        print("Tocando la guitarra: ¡acordes de rock!")

    def afinar(self):
        print("Afinando la guitarra: Mi, La, Re, Sol, Si, Mi.")

class Piano(Instrumento):
    def tocar(self):
        print("Tocando el piano: melodía clásica.")

    def afinar(self):
        print("Afinando el piano: comprobando cada nota una por una.")

class Flauta(Instrumento):
    def tocar(self):
        print("Tocando la flauta: notas suaves y delicadas.")

    def afinar(self):
        print("Afinando la flauta: ajustando las llaves y verificando el tono.")

# Ejemplo de uso
guitarra = Guitarra()
piano = Piano()
flauta = Flauta()

guitarra.tocar()
guitarra.afinar()

piano.tocar()
piano.afinar()

flauta.tocar()
flauta.afinar()
