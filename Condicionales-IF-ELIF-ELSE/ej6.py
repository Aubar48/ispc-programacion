"""
Realice un programa donde el usuario ingrese su edad. Si es mayor de
16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.
"""
print("Ingrese su edad para verificar si es mayor de edad y puede votar")
edad = int(input("Edad: "))
if edad >= 16:
    print("Puede votar")
else:
    print("No vota")
