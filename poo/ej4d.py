"""
● Sistema de gestión de proyectos dónde el Gerente necesita revisar el
progreso de las tareas de los empleados.
"""

"""
Sistema de gestión de proyectos:
+---------------------+        +-----------------+
|  SistemaGestionProyectos  |        |     Proyecto    |
+---------------------+        +-----------------+
| proyectos: List<Proyecto> |<>----| nombre: str     |
+---------------------+        | gerente: Gerente|
                                +-----------------+
                                         |
                                         |
                                +-----------------+
                                |     Gerente     |
                                +-----------------+
                                | nombre: str     |
                                | cargo: str      |
                                +-----------------+

"""

class Gerente:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo

class Proyecto:
    def __init__(self, nombre, gerente):
        self.nombre = nombre
        self.gerente = gerente

class SistemaGestionProyectos:
    def __init__(self):
        self.proyectos = []

    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)
        print("Proyecto agregado exitosamente.")

    def mostrar_proyectos(self):
        if self.proyectos:
            print("Proyectos:")
            for idx, proyecto in enumerate(self.proyectos, start=1):
                print(f"{idx}. Nombre: {proyecto.nombre} - Gerente: {proyecto.gerente.nombre}")
        else:
            print("No hay proyectos registrados.")

    def editar_proyecto(self):
        self.mostrar_proyectos()
        if self.proyectos:
            try:
                idx = int(input("Seleccione el número del proyecto que desea editar: ")) - 1
                proyecto = self.proyectos[idx]
                nuevo_nombre = input("Ingrese el nuevo nombre del proyecto: ")
                proyecto.nombre = nuevo_nombre
                nuevo_nombre_gerente = input("Ingrese el nuevo nombre del gerente: ")
                proyecto.gerente.nombre = nuevo_nombre_gerente
                print("Proyecto editado exitosamente.")
            except (IndexError, ValueError):
                print("Opción inválida.")

    def eliminar_proyecto(self):
        self.mostrar_proyectos()
        if self.proyectos:
            try:
                idx = int(input("Seleccione el número del proyecto que desea eliminar: ")) - 1
                proyecto = self.proyectos.pop(idx)
                print(f"Proyecto '{proyecto.nombre}' eliminado.")
            except (IndexError, ValueError):
                print("Opción inválida.")

def mostrar_menu():
    print("\nMenú:")
    print("1. Mostrar proyectos")
    print("2. Agregar proyecto")
    print("3. Editar proyecto")
    print("4. Eliminar proyecto")
    print("5. Salir")

sistema_gestion_proyectos = SistemaGestionProyectos()

# Proyectos pre cargados
proyecto_pre_cargado_1 = Proyecto("Desarrollo de Software", Gerente("Juan", "Gerente de Proyecto"))
proyecto_pre_cargado_2 = Proyecto("Implementación de Redes", Gerente("María", "Gerente de Proyecto"))
sistema_gestion_proyectos.agregar_proyecto(proyecto_pre_cargado_1)
sistema_gestion_proyectos.agregar_proyecto(proyecto_pre_cargado_2)

opciones_menu = {
    "1": sistema_gestion_proyectos.mostrar_proyectos,
    "2": lambda: sistema_gestion_proyectos.agregar_proyecto(Proyecto(input("Ingrese el nombre del proyecto: "), Gerente(input("Ingrese el nombre del gerente: "), "Gerente de Proyecto"))),
    "3": sistema_gestion_proyectos.editar_proyecto,
    "4": sistema_gestion_proyectos.eliminar_proyecto,
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
