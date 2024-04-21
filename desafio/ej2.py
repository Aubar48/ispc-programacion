"""
2- Escriba un programa que pregunte al usuario la hora actual t del reloj y un número
entero de horas h, que indique qué hora marcará el reloj dentro de h horas:
"""

while True:
    try:
        hora_actual = int(
            input("Por favor, ingrese una hora (entre 0 y 23): "))
        horas_pasadas = int(
            input("Por favor, ingrese un número positivo de horas: "))
        # Verificar si la hora actual es válida (entre 0 y 23)
        if hora_actual < 0 or hora_actual > 23:
            hora_actual = int(
                input("Por favor, ingrese una hora válida (entre 0 y 23): "))
        # Verificar si las horas pasadas son un entero positivo
        if horas_pasadas <= 0:
            horas_pasadas = int(
                input("Por favor, ingrese un número positivo de horas: "))
        # Calcular la nueva hora
        nueva_hora = (hora_actual + horas_pasadas) % 24
        # Imprimir la nueva hora
        print("La hora del reloj actual es de", hora_actual, "hs",
              "dentro de", horas_pasadas, "horas será de:", nueva_hora, "hs")
        break
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
