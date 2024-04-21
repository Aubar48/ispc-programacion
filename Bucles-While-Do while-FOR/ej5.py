"""
Leer 15 números negativos y convertirlos a positivos e imprimir dichos
números.
"""
def main():
    print("Ingrese 15 números negativos:")

    # Leer los 15 números negativos
    for i in range(15):
        numero = float(input(f"Ingrese el número {-i}: "))
        
        # Convertir el número negativo a positivo
        numero_positivo = -1 * numero

        # Imprimir el número positivo
        print(numero_positivo)

if __name__ == "__main__":
    main()

