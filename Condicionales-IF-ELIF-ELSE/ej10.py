"""
Confeccione un programa que pida un número del 1 al 7 y diga el día de
la semana correspondiente.
"""
def obtener_dia_semana(numero):
    dias_semana = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    return dias_semana.get(numero, "Número de día inválido")

def main():
    print("Ingrese un número del 1 al 7 para conocer el día de la semana:")
    numero = int(input("Número: "))

    dia_semana = obtener_dia_semana(numero)
    print(f"El día correspondiente al número {numero} es: {dia_semana}")

if __name__ == "__main__":
    main()
