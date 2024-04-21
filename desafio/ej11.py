"""
11- Piedra, papel y tijera. En cada ronda del juego del cachipún, los dos competidores
deben elegir entre jugar tijera, papel o piedra.
Las reglas para decidir quién gana la ronda son: tijera le gana a papel, papel le gana a
piedra, piedra le gana a tijera, y todas las demás combinaciones son empates.
El ganador del juego es el primero que gane tres rondas.
Escriba un programa que pregunte a cada jugador cuál es su jugada, muestre cuál es el
marcador después de cada ronda, y termine cuando uno de ellos haya ganado tres
rondas. Los jugadores deben indicar su jugada escribiendo tijera, papel o piedra.

A: tijera
B: papel
1 - 0
A: tijera
B: tijera
1 - 0

A: piedra
B: papel
1 - 1
A: piedra
B: tijera
2 - 1
A: papel
B: papel
2 - 1
A: papel
B: piedra
3 - 1
A es el ganador
"""

def determinar_ganador(jugada_A, jugada_B):
    if jugada_A == jugada_B:
        return "Empate"
    elif (jugada_A == "piedra" and jugada_B == "tijera") or \
         (jugada_A == "papel" and jugada_B == "piedra") or \
         (jugada_A == "tijera" and jugada_B == "papel"):
        return "A"
    else:
        return "B"

puntuacion_A = 0
puntuacion_B = 0

print("Bienvenido al piedra, papel, tijera, al mejor de tres")

while puntuacion_A < 3 and puntuacion_B < 3:
    jugada_A = input("A: ").lower()
    jugada_B = input("B: ").lower()
    
    if jugada_A not in ["piedra", "papel", "tijera"] or jugada_B not in ["piedra", "papel", "tijera"]:
        print("Jugada inválida. Por favor, elige piedra, papel o tijera.")
        continue
    
    ganador = determinar_ganador(jugada_A, jugada_B)
    if ganador == "A":
        puntuacion_A += 1
    elif ganador == "B":
        puntuacion_B += 1
    
    print(f"{puntuacion_A} - {puntuacion_B}")

if puntuacion_A == 3:
    print("A es el ganador")
else:
    print("B es el ganador")
