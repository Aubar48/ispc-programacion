"""
Desafío. Considera un sistema de gestión de biblioteca dónde las
instancias posibles son los Libros. Ej. “El principito”. Modela la clase Libro
utilizando los símbolos definidos por el Diagrama de Clases UML
identificando atributos, métodos y sus correspondientes modificadores de
acceso.

"""
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        self.prestado = False  # Nuevo atributo para rastrear si el libro ha sido prestado o no
    
    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.prestado = True  # Actualiza el estado de prestado a True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible para préstamo.")
    
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            self.prestado = False  # Actualiza el estado de prestado a False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya está disponible.")

class Biblioteca:
    def __init__(self):
        self.libros = []  # Inicialmente la biblioteca estará vacía
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"El libro '{libro.titulo}' ha sido agregado a la biblioteca.")
    
    def buscar_por_titulo(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        print(f"No se encontró ningún libro con el título '{titulo}'.")
        return None
    
    def buscar_por_autor(self, autor):
        libros_encontrados = []
        for libro in self.libros:
            if libro.autor == autor:
                libros_encontrados.append(libro)
        if libros_encontrados:
            return libros_encontrados
        else:
            print(f"No se encontró ningún libro del autor '{autor}'.")
            return []

    def editar_libro(self, titulo):
        libro = self.buscar_por_titulo(titulo)
        if libro:
            print(f"Editando libro '{libro.titulo}':")
            nuevo_titulo = input("Nuevo título: ")
            nuevo_autor = input("Nuevo autor: ")
            nuevo_isbn = input("Nuevo ISBN: ")
            libro.titulo = nuevo_titulo
            libro.autor = nuevo_autor
            libro.isbn = nuevo_isbn
            print("Libro editado exitosamente.")
    
    def mostrar_libros(self):
        print("Libros en la biblioteca:")
        for libro in self.libros:
            estado_prestado = "Prestado" if not libro.disponible else "Disponible"
            print(f"- Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}, Estado: {estado_prestado}")
    

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar libro")
    print("2. Editar libro")
    print("3. Eliminar libro")
    print("4. Mostrar libros")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Salir")

def agregar_libro():
    titulo = input("Ingrese el título del nuevo libro: ")
    autor = input("Ingrese el autor del nuevo libro: ")
    isbn = input("Ingrese el ISBN del nuevo libro: ")
    if not titulo or not autor or not isbn:
        raise ValueError("Debe ingresar todos los datos del libro.")
    nuevo_libro = Libro(titulo, autor, isbn)
    biblioteca.agregar_libro(nuevo_libro)
    print("Libro agregado exitosamente.")

def editar_libro():
    titulo = input("Ingrese el título del libro a editar: ")
    if not titulo:
        raise ValueError("Debe ingresar el título del libro a editar.")
    biblioteca.editar_libro(titulo)

def eliminar_libro():
    titulo = input("Ingrese el título del libro a eliminar: ")
    if not titulo:
        raise ValueError("Debe ingresar el título del libro a eliminar.")
    biblioteca.eliminar_libro(titulo)

def mostrar_libros():
    biblioteca.mostrar_libros()

def prestar_libro():
    titulo = input("Ingrese el título del libro a prestar: ")
    libro = biblioteca.buscar_por_titulo(titulo)
    if libro:
        libro.prestar()

def devolver_libro():
    titulo = input("Ingrese el título del libro a devolver: ")
    libro = biblioteca.buscar_por_titulo(titulo)
    if libro:
        libro.devolver()

biblioteca = Biblioteca()
libro1 = Libro("El principito", "Antoine de Saint-Exupéry", "9780156012195",)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "9780307350488")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)


opciones = {
    "1": agregar_libro,
    "2": editar_libro,
    "3": eliminar_libro,
    "4": mostrar_libros,
    "5": prestar_libro,
    "6": devolver_libro,
    "7": lambda: print("Saliendo del programa...")
}

while True:
    try:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        accion = opciones.get(opcion)
        if accion:
            if opcion == "7":  # Si la opción es salir
                accion()  # Ejecuta la acción (imprimir mensaje) y sale del bucle
                break
            accion()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
    
    except Exception as e:
        print(f"Error inesperado: {e}")
