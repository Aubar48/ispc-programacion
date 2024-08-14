"""
Control de Volúmen. Crea una clase ControlVolumen que permita establecer el
volumen de un parlante (1 mínimo volumen, 10 máximo volumen). El constructor
establecerá el volumen en un nivel medio. Agrega métodos para: 1- ajustar el
volumen permitiendo que el mismo sume o reste sin salirse de los límites y 2-
mostrar el nivel de volúmen actual. Además, escribe una aplicación de consola que
permita al usuario manipular y consultar el volumen hasta que decida salir. Al
finalizar deberá mostrar el nivel actual de volumen.
"""

class ControlVolumen:
    def __init__(self):
        self.volumen = 5  # Nivel de volumen medio

    def ajustar_volumen(self, cambio):
        self.volumen += cambio
        if self.volumen < 1:
            self.volumen = 1
        elif self.volumen > 10:
            self.volumen = 10

    def mostrar_volumen(self):
        return self.volumen

def aplicacion_consola():
    control = ControlVolumen()
    while True:
        print(f"Nivel de volumen actual: {control.mostrar_volumen()}")
        accion = input("Escribe 'subir', 'bajar' o 'salir': ").lower()
        if accion == 'subir':
            control.ajustar_volumen(1)
        elif accion == 'bajar':
            control.ajustar_volumen(-1)
        elif accion == 'salir':
            break
        else:
            print("Acción no reconocida. Por favor, escribe 'subir', 'bajar' o 'salir'.")
    print(f"Nivel de volumen final: {control.mostrar_volumen()}")

if __name__ == "__main__":
    aplicacion_consola()
