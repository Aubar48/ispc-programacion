"""
10- Torre y Alfil. Un tablero de ajedrez es una grilla de ocho filas y ocho columnas,
numeradas de 1 a 8. Dos de las piezas del juego de ajedrez son el alfil y la torre. El alfil se
desplaza en diagonal, mientras que la torre se desplaza horizontal o verticalmente. Una
pieza puede ser capturada por otra si está en una casilla a la cual la otra puede
desplazarse:
Escriba un programa que reciba como entrada las posiciones en el tablero de un alfil y de
una torre, e indique cuál pieza captura a la otra:

3

5
Fila alfil: 7
Columna alfil: 6
Fila torre: 4
Columna torre: 3
Alfil captura
Fila alfil: 3
Columna alfil: 4
Fila torre: 7
Columna torre: 4
Torre captura
Fila alfil: 3
Columna alfil: 3
Fila torre: 8
Columna torre: 5
Ninguna captura
"""
def es_capturada_por_alfil(fila_alfil, columna_alfil, fila_torre, columna_torre):
    # Verificar si la torre está en la misma diagonal que el alfil
    return abs(fila_alfil - fila_torre) == abs(columna_alfil - columna_torre)

def es_capturada_por_torre(fila_alfil, columna_alfil, fila_torre, columna_torre):
    # Verificar si la torre está en la misma fila o columna que el alfil
    return fila_alfil == fila_torre or columna_alfil == columna_torre

while True:
    try:
        fila_alfil = int(input("Fila alfil: "))
        columna_alfil = int(input("Columna alfil: "))
        fila_torre = int(input("Fila torre: "))
        columna_torre = int(input("Columna torre: "))
        
        if es_capturada_por_alfil(fila_alfil, columna_alfil, fila_torre, columna_torre):
            print("Alfil captura")
        elif es_capturada_por_torre(fila_alfil, columna_alfil, fila_torre, columna_torre):
            print("Torre captura")
        else:
            print("Ninguna captura")
            
    except ValueError:
        print("Entrada inválida. Ingrese valores numéricos para las posiciones.")
