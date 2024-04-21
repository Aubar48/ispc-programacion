"""
Realizar un programa que permita ingresar “f” o “m” y determinar si vota
en mesa femenina o masculina.
"""

print("Vamos a verificar si votas en mesa masculina ingresando M o en mesa femenina ingresando F")
voto = input("Ingrese F o M: ").lower()

if voto == "f":
    print("Este usuario debe votar en la mesa femenina.")
elif voto == "m":
    print("Este usuario debe votar en la mesa masculina.")
else:
    print("Error, por favor ingrese solo F o M")
