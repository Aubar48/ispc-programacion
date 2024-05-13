from abc import ABC, abstractmethod

class Mando(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

class Television(Mando):
    def encender(self):
        print("La televisión está encendida.")

    def apagar(self):
        print("La televisión está apagada.")

tv = Television()
tv.encender()  # Imprime "La televisión está encendida."
tv.apagar()  # Imprime "La televisión está apagada."
