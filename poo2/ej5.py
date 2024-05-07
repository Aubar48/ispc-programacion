"""
Agenda de Contactos. Crea una clase Contacto que almacene información
sobre personas en una agenda. Implementa los métodos __str__ y
__setitem__ para mostrar detalles del contacto y modificar sus atributos (por
ejemplo, número de teléfono)
"""

class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}"

    def __setitem__(self, key, value):
        if key == 'telefono':
            self.telefono = value
        else:
            raise KeyError("Atributo no válido")

# Ejemplo de uso
contacto = Contacto("Juan", "123456789")
print("Contacto:", contacto)

# Modificar el número de teléfono
contacto['telefono'] = "987654321"
print("Contacto modificado:", contacto)
