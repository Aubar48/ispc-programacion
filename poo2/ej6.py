"""
Crear una clase base llamada “Personaje”: esta clase contendrá los atributos
y métodos comunes a todos los personajes del juego. Por ej. los atributos
podrían ser nombre, vidas y poder. Los métodos podrían ser: mover, saltar y
caer.
2. Crea clases derivadas para cada personaje específico. Estas clases heredarán
de la clase base “Personaje” y podrán tener atributos y métodos adicionales.
Por ej. la clase Mario podría tener un método adicional lanzar_fuego()
mientras que la clase Luigi podría tener un método adicional usar_hongo().
3. Crea clases base para los enemigos. Esta clase contendrá los atributos y
métodos comunes a todos los enemigos. Por ejemplo, los métodos podrían ser
tipo, daño y, los métodos podrían ser mover, atacar, etc.
4. Crear clases derivadas de la clase enemigo. Estas clases heredarán de la clase
base “Enemigo” y podrán tener atributos y métodos adicionales. Por ej. la
clase “Koopa Troopa” podría tener un método adicional usar_casco(),
mientras que la clase “Goomba” podría tener un método esconder()
Nota: Para la implementación de los métodos simplemente imprime en pantalla un
texto que explique lo que haría el personaje.
"""

class Personaje:
    def __init__(self, nombre, vidas, poder):
        self.nombre = nombre
        self.vidas = vidas
        self.poder = poder

    def mover(self):
        print(f"{self.nombre} se está moviendo.")

    def saltar(self):
        print(f"{self.nombre} está saltando.")

    def caer(self):
        print(f"{self.nombre} está cayendo.")

class Mario(Personaje):
    def lanzar_fuego(self):
        print(f"{self.nombre} está lanzando fuego.")

class Luigi(Personaje):
    def usar_hongo(self):
        print(f"{self.nombre} está usando un hongo.")

class Enemigo:
    def __init__(self, tipo, vidas, daño):
        self.tipo = tipo
        self.vidas = vidas
        self.daño = daño

    def mover(self):
        print(f"{self.tipo} se está moviendo.")

    def atacar(self):
        print(f"{self.tipo} está atacando.")

class KoopaTroopa(Enemigo):
    def usar_casco(self):
        print(f"{self.tipo} ha usado su caparazón para protegerse.")

class Goomba(Enemigo):
    def esconder(self):
        print(f"{self.tipo} se ha escondido en su caparazón.")

# Ejemplo de uso
mario = Mario("Mario", 3, 10)
luigi = Luigi("Luigi", 3, 8)
koopa = KoopaTroopa("Koopa Troopa", 1, 2)
goomba = Goomba("Goomba", 1, 1)

mario.mover()
mario.saltar()
mario.caer()
mario.lanzar_fuego()

luigi.mover()
luigi.saltar()
luigi.caer()
luigi.usar_hongo()

koopa.mover()
koopa.atacar()
koopa.usar_casco()

goomba.mover()
goomba.atacar()
goomba.esconder()
