"""
Leer 10 números y mostrar solamente los números positivos, y su
sumatoria.
"""
def main():
    # Inicializamos la sumatoria de números positivos
    sumatoria_positivos = 0

    print("Ingrese 10 números:")

    # Leer los 10 números
    for i in range(10):
        numero = float(input(f"Ingrese el número {i+1}: "))
        
        # Verificar si el número es positivo
        if numero > 0:
            print(numero)
            sumatoria_positivos += numero

    # Mostrar la sumatoria de los números positivos
    print(f"La sumatoria de los números positivos es: {sumatoria_positivos}")

if __name__ == "__main__":
    main()
