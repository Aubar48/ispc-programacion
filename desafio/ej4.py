"""
4- Tiempo de viaje. Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él
tiene la duración en minutos de cada uno de los tramos del viaje.
Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y
entregue como resultado el tiempo total de viaje en formato horas:minutos.
El programa deja de pedir tiempos de viaje cuando se ingresa un 0.
"""

# Inicializar la variable para almacenar el tiempo total de viaje
tiempo_total_minutos = 0

# Bucle para ingresar los tiempos de viaje de los tramos
while True:
    try:
        tiempo_tramo = int(
            input("Ingrese la duración del tramo del viaje en minutos (0 para finalizar): "))

    # Salir del bucle si se ingresa un tiempo de tramo de 0
        if tiempo_tramo == 0:
            break

    # Sumar el tiempo del tramo al tiempo total de viaje
        tiempo_total_minutos += tiempo_tramo

    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Convertir el tiempo total de viaje a horas y minutos
horas = tiempo_total_minutos // 60
minutos = tiempo_total_minutos % 60

# Imprimir el tiempo total de viaje en formato horas:minutos
print("El tiempo total de viaje es:", horas, "horas y", minutos, "minutos.")
