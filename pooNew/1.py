class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni
    
    # Getters y Setters
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            print("Nombre debe ser una cadena de caracteres.")
    
    def get_edad(self):
        return self._edad
    
    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self._edad = edad
        else:
            print("Edad debe ser un número entero no negativo.")
    
    def get_dni(self):
        return self._dni
    
    def set_dni(self, dni):
        if isinstance(dni, str):
            self._dni = dni
        else:
            print("DNI debe ser una cadena de caracteres.")
    
    # Método mostrar
    def mostrar(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}, DNI: {self._dni}")
    
    # Método esMayorDeEdad
    def es_mayor_de_edad(self):
        return self._edad >= 18

# Aplicación de consola
def main():
    personas = []
    
    while True:
        print("\nOpciones:")
        print("1. Ingresar datos de una nueva persona")
        print("2. Mostrar lista de todas las personas")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            dni = input("DNI: ")
            
            persona = Persona(nombre, edad, dni)
            personas.append(persona)
            
            persona.mostrar()
            
            if persona.es_mayor_de_edad():
                print("La persona es mayor de edad.")
            else:
                print("La persona es menor de edad.")
        
        elif opcion == "2":
            print("\nLista de todas las personas:")
            for persona in personas:
                persona.mostrar()
        
        elif opcion == "3":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
