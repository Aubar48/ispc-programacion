class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        """Devuelve una representación legible del libro."""
        return f"{self.titulo} de {self.autor}"

    def __len__(self):
        """Devuelve la cantidad de páginas del libro."""
        return self.paginas


if __name__ == "__main__":
    # Crear una instancia de la clase Libro
    mi_libro = Libro(titulo="Cien años de soledad",
                     autor="Gabriel García Márquez", paginas=432)
# Obtener información sobre el libro
print(f"Libro: {mi_libro}")
print(f"Número de páginas: {len(mi_libro)}")
