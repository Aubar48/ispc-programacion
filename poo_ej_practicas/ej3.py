class Personaje:
    def __init__(self, nombre, vidas):
        self.nombre = nombre
        self.vidas = vidas

    def __add__(self, cantidad):
        """Aumenta las vidas del personaje en una cantidad específica."""
        self.vidas += cantidad
        return Personaje(self.nombre, self.vidas)

    def __sub__(self, cantidad):
        """Disminuye las vidas del personaje en una cantidad específica."""
        self.vidas -= cantidad
        return Personaje(self.nombre, self.vidas)

if __name__ == "__main__":
    # Crear un héroe
    heroe = Personaje("Valiente", 10)
    # Aumentar las vidas y el ataque del héroe
    heroe_mejorado = heroe + 10
    print(f"Héroe mejorado: {heroe_mejorado.nombre} (Vidas: {heroe_mejorado.vidas})")
    # Disminuir las vidas y el ataque del héroe
    heroe_debil = heroe - 2
    print(f"Héroe debilitado: {heroe_debil.nombre} (Vidas: {heroe_debil.vidas})")
