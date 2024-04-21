"""
8- Este problema apareció en el certamen recuperativo 1 del segundo semestre de 2011
en el campus Vitacura.
Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen
respectivamente $270, $340 y $390. La máquina acepta y da de vuelto monedas de $10,
$50 y $100.
Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las
monedas hasta alcanzar el monto a pagar. Si el monto ingresado es mayor que el precio
del producto, el programa debe entregar las monedas de vuelto, una por una.
"""

# Definir los precios de los productos y los valores de las monedas
precios_productos = {'A': 270, 'B': 340, 'C': 390}
valores_monedas = [100, 50, 10]

# Solicitar al usuario que elija un producto
producto = input("Elija un producto (A, B o C): ").upper()

# Verificar si el producto elegido es válido
if producto not in precios_productos:
    print("Producto no válido.")
else:
    precio_producto = precios_productos[producto]  # Obtener el precio del producto seleccionado
    
    # Solicitar al usuario que ingrese las monedas hasta alcanzar el monto a pagar
    total_ingresado = 0
    print("Ingrese monedas:")
    while total_ingresado < precio_producto:
        moneda = int(input())
        if moneda not in valores_monedas:
            print("Moneda no válida.")
        else:
            total_ingresado += moneda
    
    # Calcular el vuelto si corresponde
    vuelto = total_ingresado - precio_producto
    if vuelto < 0:
        print("Falta dinero para pagar el producto.")
    elif vuelto == 0:
        print("El pago ha sido exacto.")
    else:
        print("Su vuelto:")
        for valor_moneda in valores_monedas:
            while vuelto >= valor_moneda:
                print(valor_moneda)
                vuelto -= valor_moneda
