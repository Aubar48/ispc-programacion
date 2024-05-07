"""
Desafío. Realiza el diagrama de clases para los siguientes enunciados
identificando relaciones de herencia, composición y/o agregación o uso:

● Software de gestión de personal, cada Empleado tiene un Rol. El empleado
no puede existir sin tener un rol asignado.

"""





"""
Software de gestión de personal:
+----------------------+        +---------+
|  SoftwareGestionPersonal   |  |   Rol   |
+----------------------+        +---------+
| - nombre: string           |  | - nombre: string |
| - empleados: Empleado[]    |  +---------+
+----------------------+        
| + agregar_empleado()       |
| + mostrar_empleados()      |
| + editar_empleado()        |
| + eliminar_empleado()      |
+----------------------+        

          |
          |     1..*
          |
          |
          V

        +---------+
        | Empleado |
        +---------+
        | - nombre: string |
        | - rol: Rol       |
        +---------+

"""
class Rol:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

class SoftwareGestionPersonal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self):
        nombre = input("Ingrese el nombre del nuevo empleado: ")
        nombre_rol = input("Ingrese el nombre del rol del nuevo empleado: ")
        rol = Rol(nombre_rol)
        nuevo_empleado = Empleado(nombre, rol)
        self.empleados.append(nuevo_empleado)
        print("Empleado agregado exitosamente.")

    def mostrar_empleados(self):
        if self.empleados:
            print("Empleados:")
            for idx, empleado in enumerate(self.empleados, start=1):
                print(f"{idx}. {empleado.nombre} - Rol: {empleado.rol.nombre}")
        else:
            print("No hay empleados registrados.")

    def editar_empleado(self):
        self.mostrar_empleados()
        if self.empleados:
            try:
                idx = int(input("Seleccione el número del empleado que desea editar: ")) - 1
                empleado = self.empleados[idx]
                nuevo_nombre = input("Ingrese el nuevo nombre del empleado: ")
                empleado.nombre = nuevo_nombre
                print("Empleado editado exitosamente.")
            except (IndexError, ValueError):
                print("Opción inválida.")

    def eliminar_empleado(self):
        self.mostrar_empleados()
        if self.empleados:
            try:
                idx = int(input("Seleccione el número del empleado que desea eliminar: ")) - 1
                empleado = self.empleados.pop(idx)
                print(f"Empleado '{empleado.nombre}' eliminado.")
            except (IndexError, ValueError):
                print("Opción inválida.")

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar empleado")
    print("2. Mostrar empleados")
    print("3. Editar empleado")
    print("4. Eliminar empleado")
    print("5. Salir")

software_gestion_personal = SoftwareGestionPersonal("SoftwareGestionPersonal")

# Empleados pre cargados
rol_administrador = Rol("Administrador")
empleado1 = Empleado("Nahuel Argandoña", rol_administrador)
software_gestion_personal.empleados.append(empleado1)



opciones_menu = {
    "1": software_gestion_personal.agregar_empleado,
    "2": software_gestion_personal.mostrar_empleados,
    "3": software_gestion_personal.editar_empleado,
    "4": software_gestion_personal.eliminar_empleado,
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
