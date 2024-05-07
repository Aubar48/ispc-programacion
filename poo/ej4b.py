"""
● Sistema de gestión de cursos, un Profesor puede impartir múltiples Cursos.
Si el Profesor se retira, los Cursos pueden seguir siendo ofrecidos por otros
profesores.

"""

"""
Sistema de gestión de cursos:
+-----------------------+         +-----------+
|  SistemaGestionCursos |         |   Profesor|
+-----------------------+         +-----------+
|                       |         |  - nombre: str|
| - cursos: list        |         +-----------+
+-----------------------+
            |
            |
            |           +------------+
            |<>------- |    Curso   |
            |          +------------+
            |          |  - nombre: str       |
            |          |  - profesor: Profesor|
            |          +------------+
"""
class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

class SistemaGestionCursos:
    def __init__(self):
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)
        print("Curso agregado exitosamente.")

    def mostrar_cursos(self):
        if self.cursos:
            print("Cursos:")
            for idx, curso in enumerate(self.cursos, start=1):
                print(f"{idx}. Curso: {curso.nombre} - Profesor: {curso.profesor.nombre}")
        else:
            print("No hay cursos registrados.")

    def editar_curso(self):
        self.mostrar_cursos()
        if self.cursos:
            try:
                idx = int(input("Seleccione el número del curso que desea editar: ")) - 1
                curso = self.cursos[idx]
                nuevo_nombre_curso = input("Ingrese el nuevo nombre del curso: ")
                nuevo_nombre_profesor = input("Ingrese el nuevo nombre del profesor: ")
                curso.nombre = nuevo_nombre_curso
                curso.profesor.nombre = nuevo_nombre_profesor
                print("Curso editado exitosamente.")
            except (IndexError, ValueError):
                print("Opción inválida.")

    def eliminar_curso(self):
        self.mostrar_cursos()
        if self.cursos:
            try:
                idx = int(input("Seleccione el número del curso que desea eliminar: ")) - 1
                curso = self.cursos.pop(idx)
                print(f"Curso '{curso.nombre}' eliminado.")
            except (IndexError, ValueError):
                print("Opción inválida.")

def mostrar_menu():
    print("\nMenú:")
    print("1. Mostrar cursos")
    print("2. Agregar curso")
    print("3. Editar curso")
    print("4. Eliminar curso")
    print("5. Salir")

sistema_gestion_cursos = SistemaGestionCursos()

# Cursos pre cargados
curso_pre_cargado_1 = Curso("Programación 1", Profesor("Ivana Soledad ROJAS CÓRSICO"))
curso_pre_cargado_2 = Curso("Base de datos 1", Profesor("Martín Alejandro GERLERO"))
curso_pre_cargado_3 = Curso("Ética y deontología profesional", Profesor("Anahí HERNANDEZ "))
sistema_gestion_cursos.agregar_curso(curso_pre_cargado_1)
sistema_gestion_cursos.agregar_curso(curso_pre_cargado_2)
sistema_gestion_cursos.agregar_curso(curso_pre_cargado_3)

opciones_menu = {
    "1": sistema_gestion_cursos.mostrar_cursos,
    "2": lambda: sistema_gestion_cursos.agregar_curso(Curso(input("Ingrese el nombre del curso: "), Profesor(input("Ingrese el nombre del profesor: ")))),
    "3": sistema_gestion_cursos.editar_curso,
    "4": sistema_gestion_cursos.eliminar_curso,
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
