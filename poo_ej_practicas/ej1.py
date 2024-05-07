class Coche():
    def __init__(self, dueño, largoChasis, ruedas, motor, nafta, enMarcha):
        self.dueño = dueño
        self.largoChasis = largoChasis
        self.ruedas = ruedas
        self.motor = motor
        self.nafta = nafta
        self.enMarcha = enMarcha

    def arrancar(self):
        self.enMarcha = True
        if self.enMarcha:
            print(
                f"{self.dueño} enciende el coche. El coche se ha encendido pr prrrr")

    def detener(self):
        self.enMarcha = False
        if not self.enMarcha:
            print("El Coche se ha detenido...")

    def andando(self):
        if self.enMarcha and self.nafta > 0:
            for cantidad in range(self.nafta, 0, -1):

                if cantidad == 5:
                    print(
                        f"Vamos con muy poca gasolina... cantidad: {cantidad}")
                    continue
                if cantidad == 10:
                    print(f"Queda la mitad del tanque... cantidad: {cantidad}")
                    continue
                print("Queda de nafta: ", cantidad)
                if cantidad == 1:
                    self.detener()
                    break
        else:
            print("El coche no está encendido..")

    def andando2(self):
        if self.enMarcha:
            for cantidad in range(self.nafta):

                if cantidad + 1 == 5:
                    print(f"woooooooow {cantidad+1} km")
                    continue
                if cantidad + 1 == 10:
                    print(f"Increibleee {cantidad + 1} km")
                    continue
                print("Recorrido: ", cantidad+1, " km")
                if cantidad + 1 >= self.nafta:
                    self.detener()
                    break


class GestorCoches:
    def __init__(self):
        self.coches = []

    def agregar_coche(self):
        dueño = input("Ingrese el nombre del dueño del coche: ")
        largoChasis = int(input("Ingrese el largo del chasis del coche: "))
        ruedas = int(input("Ingrese la cantidad de ruedas del coche: "))
        motor = int(input("Ingrese el tamaño del motor del coche: "))
        nafta = int(input("Ingrese la cantidad de nafta del coche: "))
        enMarcha = input(
            "¿El coche está en marcha? (True/False): ").lower() == "true"

        nuevo_coche = Coche(dueño, largoChasis, ruedas, motor, nafta, enMarcha)
        self.coches.append(nuevo_coche)
        print("Coche agregado correctamente.")

    def editar_coche(self):
        self.mostrar_info()
        idx_coche = int(
            input("Ingrese el número de coche que desea editar: ")) - 1
        coche = self.coches[idx_coche]

        print("Ingrese los nuevos datos del coche:")
        coche.dueño = input("Nuevo dueño: ")
        coche.largoChasis = int(input("Nuevo largo del chasis: "))
        coche.ruedas = int(input("Nueva cantidad de ruedas: "))
        coche.motor = int(input("Nuevo tamaño del motor: "))
        coche.nafta = int(input("Nueva cantidad de nafta: "))
        coche.enMarcha = input(
            "¿El coche está en marcha? (True/False): ").lower() == "true"
        print("Coche editado correctamente.")

    def eliminar_coche(self):
        self.mostrar_info()
        idx_coche = int(
            input("Ingrese el número de coche que desea eliminar: ")) - 1
        coche_eliminado = self.coches.pop(idx_coche)
        print(f"Coche de {coche_eliminado.dueño} eliminado correctamente.")

    def mostrar_info(self):
        print("Listado de Coches:")
        for idx, coche in enumerate(self.coches, start=1):
            print(f"Coche {idx}:")
            print(f"  Dueño: {coche.dueño}")
            print(f"  Largo del chasis: {coche.largoChasis}")
            print(f"  Cantidad de ruedas: {coche.ruedas}")
            print(f"  Motor: {coche.motor}")
            print(f"  Nafta: {coche.nafta}")
            print(f"  En marcha: {coche.enMarcha}")
            print("")

    def menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Mostrar información de los coches")
            print("2. Agregar coche")
            print("3. Editar coche")
            print("4. Eliminar coche")
            print("5. Arrancar coche")
            print("6. Detener coche")
            print("7. Sacar a pasear")
            print("8. Cantidad recorrida")
            print("9. Salir")

            opcion = input("Ingrese el número de opción: ")

            switch = {
                "1": self.mostrar_info,
                "2": self.agregar_coche,
                "3": self.editar_coche,
                "4": self.eliminar_coche,
                "5": self.arrancar_coche,
                "6": self.detener_coche,
                "7": self.sacar_a_pasear,
                "8": self.cantidad_recorrida,
                "9": self.salir
            }

            if opcion in switch:
                if opcion == "9":
                    switch[opcion]()
                    break  # Salir del bucle cuando la opción es "9"
                else:
                    switch[opcion]()
            else:
                print("Opción inválida. Inténtelo de nuevo.")

    def arrancar_coche(self):
        self.mostrar_info()
        idx_coche = int(
            input("Ingrese el número de coche que desea arrancar: ")) - 1
        self.coches[idx_coche].arrancar()

    def detener_coche(self):
        self.mostrar_info()
        idx_coche = int(
            input("Ingrese el número de coche que desea detener: ")) - 1
        self.coches[idx_coche].detener()

    def sacar_a_pasear(self):
        self.mostrar_info()
        idx_coche = int(
            input("Ingrese el número que desea sacar a pasear: ")) - 1
        self.coches[idx_coche].andando()

    def cantidad_recorrida(self):
        self.mostrar_info()
        idx_coche = int(
            input("Ingrese el número que desea sacar a pasear: ")) - 1
        self.coches[idx_coche].andando2()

    def salir(self):
        print("¡Hasta luego!")


# Instanciamos el gestor de coches
gestor = GestorCoches()

# Ejecutamos el menú
gestor.menu()
