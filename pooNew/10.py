"""
Gestión de Biblioteca. Escribe un programa de consola que simula la gestión de una
biblioteca. Cada libro debe tener un título, un autor y un estado (prestado o
disponible). Crea una clase Libro con los atributos mencionados y métodos para
prestar y devolver libros. Implementa una clase Biblioteca que almacena una lista de
libros y permite buscar libros por título o autor, así como mostrar el estado de un
libro específico
"""

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.estado = "disponible"

    def prestar(self):
        if self.estado == "disponible":
            self.estado = "prestado"
            return True
        else:
            return False

    def devolver(self):
        if self.estado == "prestado":
            self.estado = "disponible"
            return True
        else:
            return False

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Estado: {self.estado}"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_por_titulo(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def buscar_por_autor(self, autor):
        resultados = []
        for libro in self.libros:
            if libro.autor.lower() == autor.lower():
                resultados.append(libro)
        return resultados

    def mostrar_estado_libro(self, titulo):
        libro = self.buscar_por_titulo(titulo)
        if libro:
            return str(libro)
        else:
            return "Libro no encontrado"


# Ejemplo de uso
biblioteca = Biblioteca()

# Agregar libros
biblioteca.agregar_libro(Libro("El Quijote", "Miguel de Cervantes"))
biblioteca.agregar_libro(Libro("Cien años de soledad", "Gabriel García Márquez"))

# Prestar un libro
libro = biblioteca.buscar_por_titulo("El Quijote")
if libro and libro.prestar():
    print(f"Libro '{libro.titulo}' prestado con éxito.")
else:
    print(f"El libro '{libro.titulo}' no está disponible para préstamo.")

# Mostrar estado de un libro
print(biblioteca.mostrar_estado_libro("El Quijote"))

# Devolver un libro
if libro and libro.devolver():
    print(f"Libro '{libro.titulo}' devuelto con éxito.")
else:
    print(f"El libro '{libro.titulo}' no estaba prestado.")

# Mostrar estado de un libro después de devolverlo
print(biblioteca.mostrar_estado_libro("El Quijote"))

# Buscar libros por autor
libros_por_autor = biblioteca.buscar_por_autor("Gabriel García Márquez")
for libro in libros_por_autor:
    print(libro)
