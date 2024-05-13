class StaticClass:
    @classmethod
    def static_method(cls):
        print("Este es un método estático de la clase.")

# Llamar al método estático directamente desde la clase
StaticClass.static_method()  # Imprime "Este es un método estático de la clase."
