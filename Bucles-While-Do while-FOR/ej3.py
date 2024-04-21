"""
Ingresar las edades y el sexo de 15 personas y determinar cuántas son
mujeres, cuántos varones, cuántos mayores de edad y cuántos
menores de edad.
"""
def main():
    # Inicializamos las variables para el seguimiento
    cantidad_mujeres = 0
    cantidad_varones = 0
    cantidad_mayores_edad = 0
    cantidad_menores_edad = 0

    # Leer las edades y el sexo de las 15 personas
    for i in range(15):
        edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
        sexo = input(f"Ingrese el sexo de la persona {i+1} (M/F): ").upper()

        # Determinar si la persona es mujer o varón
        if sexo == "M":
            cantidad_varones += 1
        elif sexo == "F":
            cantidad_mujeres += 1

        # Determinar si la persona es mayor o menor de edad
        if edad >= 18:
            cantidad_mayores_edad += 1
        else:
            cantidad_menores_edad += 1

    # Mostrar los resultados
    print(f"Cantidad de mujeres: {cantidad_mujeres}")
    print(f"Cantidad de varones: {cantidad_varones}")
    print(f"Cantidad de mayores de edad: {cantidad_mayores_edad}")
    print(f"Cantidad de menores de edad: {cantidad_menores_edad}")

if __name__ == "__main__":
    main()
