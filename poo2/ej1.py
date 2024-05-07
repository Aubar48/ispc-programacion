"""
Desafío. Intenta crear una clase Dado que cumpla los siguientes
requerimientos:
● el dado debe tener un número de caras (por defecto 6)
● debe ser capaz de lanzarse y devolver un número aleatorio entre 1
y el número de caras.
"""

import random

class Dado:
    def __init__(self, num_caras=6):
        self.num_caras = num_caras

    def lanzar(self):
        return random.randint(1, self.num_caras)

# Ejemplo de uso
dado_normal = Dado()
print("Lanzamiento del dado normal:", dado_normal.lanzar())

dado_personalizado = Dado(12)  # Dado de 10 caras
print("Lanzamiento del dado personalizado:", dado_personalizado.lanzar())
