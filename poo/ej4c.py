"""
● Juego de aventuras, tanto el Guerrero como El brujo son tipos de Personaje.
Todos comparten las características comunes de Personaje, pero también
tienen habilidades únicas.
"""

"""
Juego de aventuras:

+-------------------+            +---------------+            +---------------+
|    JuegoAventura  |            |   Personaje   |            |    Guerrero   |
+-------------------+            +---------------+            +---------------+
|                   |            | - nombre      |            |               |
+-------------------+            +---------------+            |               |
|                   |            | + __init__()  |            | + __init__()  |
|                   |<>----------|               |            |               |
+-------------------+            +---------------+            +---------------+
                                                  \
                                                            +----------------+
                                                    \         |    Brujo       |
                                                     \        +----------------+
                                                      \       |                |
                                                       \      |                |
                                                        \     | + __init__()   |
                                                         \    +----------------+
                                                          \
                                                           \
                                                         +----------------+
                                                         |    Arquero     |
                                                         +----------------+
                                                         |                |
                                                         |                |
                                                         | + __init__()   |
                                                         +----------------+

"""
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)

class Brujo(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)

class Arquero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)

def mostrar_personajes(personajes):
    if personajes:
        print("Personajes:")
        for idx, personaje in enumerate(personajes, start=1):
            print(f"{idx}. {type(personaje).__name__} - {personaje.nombre}")
    else:
        print("No hay personajes registrados.")

def agregar_personaje(personajes):
    nombre = input("Ingrese el nombre del personaje: ")
    print("Seleccione la clase del personaje:")
    print("1. Guerrero")
    print("2. Brujo")
    print("3. Arquero")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        personaje = Guerrero(nombre)
    elif opcion == "2":
        personaje = Brujo(nombre)
    elif opcion == "3":
        personaje = Arquero(nombre)
    else:
        print("Opción inválida.")
        return
    personajes.append(personaje)
    print("Personaje agregado exitosamente.")

def editar_personaje(personajes):
    mostrar_personajes(personajes)
    if personajes:
        try:
            idx = int(input("Seleccione el número del personaje que desea editar: ")) - 1
            personaje = personajes[idx]
            nuevo_nombre = input("Ingrese el nuevo nombre del personaje: ")
            print("Seleccione la nueva clase del personaje:")
            print("1. Guerrero")
            print("2. Brujo")
            print("3. Arquero")
            nueva_clase = input("Seleccione una opción: ")
            if nueva_clase == "1":
                personajes[idx] = Guerrero(nuevo_nombre)
            elif nueva_clase == "2":
                personajes[idx] = Brujo(nuevo_nombre)
            elif nueva_clase == "3":
                personajes[idx] = Arquero(nuevo_nombre)
            else:
                print("Opción inválida.")
                return
            print("Personaje editado exitosamente.")
        except (IndexError, ValueError):
            print("Opción inválida.")

def eliminar_personaje(personajes):
    mostrar_personajes(personajes)
    if personajes:
        try:
            idx = int(input("Seleccione el número del personaje que desea eliminar: ")) - 1
            personaje = personajes.pop(idx)
            print(f"Personaje '{personaje.nombre}' eliminado.")
        except (IndexError, ValueError):
            print("Opción inválida.")

def mostrar_menu():
    print("\nMenú:")
    print("1. Mostrar personajes")
    print("2. Agregar personaje")
    print("3. Editar personaje")
    print("4. Eliminar personaje")
    print("5. Salir")

personajes = [
    Guerrero("Conan"),
    Brujo("Merlín"),
    Arquero("Legolas")
]

opciones_menu = {
    "1": lambda: mostrar_personajes(personajes),
    "2": lambda: agregar_personaje(personajes),
    "3": lambda: editar_personaje(personajes),
    "4": lambda: eliminar_personaje(personajes),
    "5": lambda: print("Saliendo del programa...")
}

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    accion = opciones_menu.get(opcion)
    if accion:
        accion()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
    if opcion == "5":
        break
