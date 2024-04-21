"""
Realice un programa que pida un número del 1 al 12 y diga el nombre
del mes correspondiente.
"""


def obtener_mes(numero):
    mes = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    return mes.get(numero, "Número del mes inválido")


def main():
    print("Ingrese un número del 1 al 12 para conocer el mes:")
    numero = int(input("Número: "))

    mes = obtener_mes(numero)
    print(f"El mes correspondiente al número {numero} es: {mes}")


if __name__ == "__main__":
    main()
