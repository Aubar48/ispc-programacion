"""
Registro de Tareas. Crea una clase Tarea que almacene información sobre
tareas pendientes. Implementa los métodos __str__ y __len__ para mostrar
detalles de la tarea y contar cuántas tareas hay en la lista.
"""

class Tarea:
    def __init__(self, descripcion, estado='Pendiente'):
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):
        return f"Tarea: {self.descripcion} - Estado: {self.estado}"

class RegistroTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def __str__(self):
        if not self.tareas:
            return "No hay tareas registradas."
        else:
            return "\n".join(str(tarea) for tarea in self.tareas)

    def __len__(self):
        return len(self.tareas)

# Ejemplo de uso
registro = RegistroTareas()

tarea1 = Tarea("Terminar informe")
tarea2 = Tarea("Comprar víveres", estado="En progreso")
tarea3 = Tarea("Revisar correo electrónico")

registro.agregar_tarea(tarea1)
registro.agregar_tarea(tarea2)
registro.agregar_tarea(tarea3)

print("Detalles de las tareas:")
print(registro)

print("Cantidad de tareas:", len(registro))
