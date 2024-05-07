"""
1. Conversor de Monedas. Crea una clase Moneda que permita la conversión
entre monedas (ej. dólares a pesos). Implementa los métodos __str__ y
__add__ para mostrar la cantidad convertida y sumar cantidades en
diferentes monedas.
"""

class Moneda:
    # Diccionario de tasas de conversión (1 unidad de moneda extranjera a pesos)
    tasas_conversion = {
        'dolar': 98.5,  # Ejemplo: 1 dólar estadounidense = 98.5 pesos argentinos
        'euro': 115.7,  # Ejemplo: 1 euro = 115.7 pesos argentinos
        'libra': 134.2  # Ejemplo: 1 libra esterlina = 134.2 pesos argentinos
    }

    def __init__(self, cantidad, tipo_moneda):
        self.cantidad = cantidad
        self.tipo_moneda = tipo_moneda.lower()

    def __str__(self):
        return f'{self.cantidad} {self.tipo_moneda.capitalize()}'

    def __add__(self, other):
        if isinstance(other, Moneda):
            cantidad_convertida = other.cantidad * self.tasas_conversion[other.tipo_moneda] / self.tasas_conversion[self.tipo_moneda]
            return Moneda(self.cantidad + cantidad_convertida, self.tipo_moneda)
        else:
            raise TypeError("No se puede sumar un objeto Moneda con otro tipo de objeto.")

# Ejemplo de uso
monto_dolares = Moneda(100, 'dolar')
monto_euros = Moneda(50, 'euro')

print("Monto en dólares:", monto_dolares)
print("Monto en euros:", monto_euros)

monto_total = monto_dolares + monto_euros
print("Monto total en pesos argentinos:", monto_total)
