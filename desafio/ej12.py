"""
12- Torneo de Tenis. Escriba un programa para simular un campeonato de tenis.
Primero, debe pedir al usuario que ingrese los nombres de ocho tenistas. A continuación,
debe pedir los resultados de los partidos juntando los jugadores de dos en dos. El
ganador de cada partido avanza a la ronda siguiente.
El programa debe continuar preguntando ganadores de partidos hasta que quede un
único jugador, que es el campeón del torneo.
7

Jugador 1: Nadal
Jugador 2: Melzer
Jugador 3: Murray
Jugador 4: Soderling
Jugador 5: Djokovic
Jugador 6: Berdych
Jugador 7: Federer
Jugador 8: Ferrer
Ronda 1
a.Nadal - b.Melzer: a
a.Murray - b.Soderling: b
a.Djokovic - b.Berdych: a

a.Federer - b.Ferrer: a
Ronda 2
a.Nadal - b.Soderling: a
a.Djokovic - b.Federer: a
Ronda 3
a.Nadal - b.Djokovic: b
Campeon: Djokovic
"""

def solicitar_ganador(partido):
    while True:
        ganador = input(f"{partido}: ")
        if ganador.lower() in ['a', 'b']:
            return ganador.lower()
        else:
            print("Entrada inválida. Por favor, elige 'a' o 'b'.")

# Solicitar nombres de los tenistas
num_jugadores = 8
jugadores = [input(f"Jugador {i+1}: ") for i in range(num_jugadores)]

# Simular torneo
ronda = 1
while len(jugadores) > 1:
    print(f"Ronda {ronda}")
    proxima_ronda = []
    for i in range(0, len(jugadores), 2):
        jugador1 = jugadores[i]
        jugador2 = jugadores[i+1]
        ganador = solicitar_ganador(f"a.{jugador1} - b.{jugador2}")
        proxima_ronda.append(jugador1 if ganador == 'a' else jugador2)
    jugadores = proxima_ronda
    ronda += 1

# Anunciar campeón
print(f"Campeón: {jugadores[0]}")
