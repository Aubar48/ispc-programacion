"""
Desafío!. Resolver utilizando funciones con argumentos por omisión.
1. Crea una función para calcular el área de un triángulo. Si no se proporciona la
altura, asumimos una altura de 1.
2. Crea una función para saludar con un mensaje personalizado. Si no se
proporciona el nombre, asumimos “Invitado”
3. Crea una función para proporcionar un porcentaje de descuento. Si no se
proporciona el porcentaje, asumimos 10%
"""

# 1. Calcular área de un triángulo
def area_triangulo(base, altura=1):
    return (base * altura) / 2

# 2. Saludar con un mensaje personalizado
def saludar(nombre="Invitado"):
    return f"Hola, {nombre}!"

# 3. Proporcionar un porcentaje de descuento
def descuento(precio, porcentaje=10):
    return precio * (1 - porcentaje / 100)
