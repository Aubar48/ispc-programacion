import mysql.connector
from mysql.connector import Error
from datetime import datetime

class Tarea:
    def __init__(self, descripcion, fecha_vencimiento=None, estado="pendiente"):
        self.descripcion = descripcion
        self.estado = estado
        self.fecha_vencimiento = fecha_vencimiento

class GestorTareas:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                database='tareas_db',
                user='root',  # Cambia al nombre de usuario correcto
                password='root'   # Cambia a la contraseña correcta
            )
            if self.conexion.is_connected():
                print("Conexión exitosa a la base de datos")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
    
    def crear_tarea(self, tarea):
        try:
            cursor = self.conexion.cursor()
            sql = "INSERT INTO tareas (descripcion, fecha_vencimiento, estado) VALUES (%s, %s, %s)"
            values = (tarea.descripcion, tarea.fecha_vencimiento, tarea.estado)
            cursor.execute(sql, values)
            self.conexion.commit()
            print(f"Tarea '{tarea.descripcion}' agregada exitosamente.")
        except Error as e:
            print(f"Error al agregar tarea: {e}")
    
    def mostrar_tareas(self, estado=None):
        try:
            cursor = self.conexion.cursor()
            if estado:
                sql = "SELECT * FROM tareas WHERE estado = %s"
                cursor.execute(sql, (estado,))
            else:
                sql = "SELECT * FROM tareas"
                cursor.execute(sql)
            tareas = cursor.fetchall()
            for tarea in tareas:
                print(f"ID: {tarea[0]}, Descripción: {tarea[1]}, Estado: {tarea[2]}, Fecha de vencimiento: {tarea[3]}")
        except Error as e:
            print(f"Error al recuperar tareas: {e}")
    
    def actualizar_tarea(self, tarea_id, nueva_descripcion=None, nuevo_estado=None, nueva_fecha=None):
        try:
            cursor = self.conexion.cursor()
            if nueva_descripcion:
                sql = "UPDATE tareas SET descripcion = %s WHERE id = %s"
                cursor.execute(sql, (nueva_descripcion, tarea_id))
            if nuevo_estado:
                sql = "UPDATE tareas SET estado = %s WHERE id = %s"
                cursor.execute(sql, (nuevo_estado, tarea_id))
            if nueva_fecha:
                sql = "UPDATE tareas SET fecha_vencimiento = %s WHERE id = %s"
                cursor.execute(sql, (nueva_fecha, tarea_id))
            self.conexion.commit()
            print(f"Tarea ID {tarea_id} actualizada correctamente.")
        except Error as e:
            print(f"Error al actualizar tarea: {e}")
    
    def marcar_completada(self, tarea_id):
        self.actualizar_tarea(tarea_id, nuevo_estado="completada")
    
    def eliminar_tarea(self, tarea_id):
        try:
            cursor = self.conexion.cursor()
            sql = "DELETE FROM tareas WHERE id = %s"
            cursor.execute(sql, (tarea_id,))
            self.conexion.commit()
            print(f"Tarea ID {tarea_id} eliminada correctamente.")
        except Error as e:
            print(f"Error al eliminar tarea: {e}")
    
    def cerrar_conexion(self):
        if self.conexion.is_connected():
            self.conexion.close()
            print("Conexión a la base de datos cerrada.")
    
# Ejemplo de uso
if __name__ == "__main__":
    gestor = GestorTareas()

    # Agregar una nueva tarea
    nueva_tarea = Tarea("Estudiar para el examen", "2024-10-10")
    gestor.crear_tarea(nueva_tarea)

    # Mostrar todas las tareas
    print("\nTodas las tareas:")
    gestor.mostrar_tareas()

    # Mostrar solo tareas pendientes
    print("\nTareas pendientes:")
    gestor.mostrar_tareas(estado="pendiente")

    # Actualizar una tarea
    gestor.actualizar_tarea(1, nueva_descripcion="Estudiar para el examen de matemáticas")

    # Marcar una tarea como completada
    gestor.marcar_completada(1)

    # Eliminar una tarea
    gestor.eliminar_tarea(1)

    # Cerrar la conexión
    gestor.cerrar_conexion()
