"""
Registro de Estudiantes. Escribe un programa que permita registrar estudiantes en
un arreglo. Cada estudiante debe tener un nombre, una edad y una lista de
asignaturas en las que está inscrito. Implementa una clase Estudiante con los
atributos mencionados y métodos para agregar asignaturas, mostrar la información
del estudiante y calcular su promedio de calificaciones.
"""

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.asignaturas = {}  # Diccionario para asignaturas y sus calificaciones
    
    def agregar_asignatura(self, nombre_asignatura, calificacion):
        """Agrega una asignatura y su calificación al estudiante."""
        self.asignaturas[nombre_asignatura] = calificacion
    
    def mostrar_informacion(self):
        """Muestra la información del estudiante."""
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print("Asignaturas:")
        for asignatura, calificacion in self.asignaturas.items():
            print(f"  {asignatura}: {calificacion}")
    
    def calcular_promedio(self):
        """Calcula el promedio de las calificaciones del estudiante."""
        if not self.asignaturas:
            return 0
        total_calificaciones = sum(self.asignaturas.values())
        num_asignaturas = len(self.asignaturas)
        promedio = total_calificaciones / num_asignaturas
        return promedio

# Crear una lista para almacenar estudiantes
estudiantes = []

# Función para registrar un estudiante
def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    estudiante = Estudiante(nombre, edad)
    
    while True:
        nombre_asignatura = input("Ingrese el nombre de la asignatura (o 'fin' para terminar): ")
        if nombre_asignatura.lower() == 'fin':
            break
        calificacion = float(input(f"Ingrese la calificación para {nombre_asignatura}: "))
        estudiante.agregar_asignatura(nombre_asignatura, calificacion)
    
    estudiantes.append(estudiante)
    print("Estudiante registrado exitosamente.")

# Función para mostrar la información de todos los estudiantes
def mostrar_estudiantes():
    for estudiante in estudiantes:
        estudiante.mostrar_informacion()
        print(f"Promedio de calificaciones: {estudiante.calcular_promedio():.2f}")
        print()

# Menú principal
while True:
    print("1. Registrar estudiante")
    print("2. Mostrar información de estudiantes")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        registrar_estudiante()
    elif opcion == '2':
        mostrar_estudiantes()
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Intente de nuevo.")
