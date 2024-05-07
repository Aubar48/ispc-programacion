"""
Baraja de Cartas. Crea una clase Carta que represente una carta de la baraja.
Implementa los métodos __str__ y __getitem__ para mostrar la carta y
acceder a sus atributos (por ejemplo, palo y valor)
"""

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        valores_especiales = {1: "As", 11: "J", 12: "Q", 13: "K"}
        valor_str = valores_especiales.get(self.valor, str(self.valor))
        return f"{valor_str} de {self.palo}"

    def __getitem__(self, key):
        if key == 'valor':
            return self.valor
        elif key == 'palo':
            return self.palo
        else:
            raise KeyError("Atributo no válido")

# Ejemplo de uso
carta = Carta(7, "Corazones")
print("Carta:", carta)
print("Valor:", carta['valor'])
print("Palo:", carta['palo'])
