"""
Realice un programa que le permita al usuario simular el pago
ingresando el importe y la forma de pago:
• Contado(1): se aplica un descuento del 10% al importe
• Tarjeta(2): se aplica un interés de 10%
• Débito(3): se aplica un descuento del 5%
Mostrar el importe, el descuento o interés y el importe total.
"""

def calcular_total(importe, forma_pago):
    if forma_pago == 1:  # Contado
        descuento = importe * 0.10
        total = importe - descuento
        return total, descuento
    elif forma_pago == 2:  # Tarjeta
        interes = importe * 0.10
        total = importe + interes
        return total, interes
    elif forma_pago == 3:  # Débito
        descuento = importe * 0.05
        total = importe - descuento
        return total, descuento
    else:
        return None, None

def main():
    print("Simulador de pago")
    importe = float(input("Ingrese el importe a pagar: "))
    forma_pago = int(input("Seleccione la forma de pago (1: Contado, 2: Tarjeta, 3: Débito): "))

    total, ajuste = calcular_total(importe, forma_pago)

    if total is not None and ajuste is not None:
        if forma_pago == 1:
            print(f"Importe: ${importe:.2f}")
            print(f"Descuento: ${ajuste:.2f} (10%)")
            print(f"Total a pagar: ${total:.2f}")
        elif forma_pago == 2:
            print(f"Importe: ${importe:.2f}")
            print(f"Interés: ${ajuste:.2f} (10%)")
            print(f"Total a pagar: ${total:.2f}")
        elif forma_pago == 3:
            print(f"Importe: ${importe:.2f}")
            print(f"Descuento: ${ajuste:.2f} (5%)")
            print(f"Total a pagar: ${total:.2f}")
    else:
        print("Forma de pago no válida. Por favor, seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main()
