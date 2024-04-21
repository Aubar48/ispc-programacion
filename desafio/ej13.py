"""
13- El diccionario países asocia cada persona con el conjunto de los países que ha
visitado:
paises = {
'Pepito': {'Chile', 'Argentina'},
'Yayita': {'Francia', 'Suiza', 'Chile'},
'John': {'Chile', 'Italia', 'Francia', 'Peru'},
}
Escriba una función cuantos_en_comun(a, b), que indique cuántos países en común han
visitado la persona a y la persona b:
8
>>> cuantos_en_comun('Pepito', 'John')
1
>>> cuantos_en_comun('John', 'Yayita')
2
"""


def cuantos_en_comun(a, b):
    if a not in paises or b not in paises:
        return "Al menos una de las personas no se encuentra en el diccionario de países."

    # Intersección de los conjuntos de países de a y b
    paises_comunes = paises[a] & paises[b]
    return paises_comunes


paises = {}


def agregar_persona():
    nombre = input("Ingrese el nombre de la persona: ")
    while nombre in paises:
        print("¡Esa persona ya está en la lista!")
        nombre = input("Ingrese otro nombre de persona: ")

    while True:
        try:
            num_paises = int(
                input("¿Cuántos países ha visitado esta persona?: "))
            if num_paises < 0:
                print("Por favor, ingrese un número positivo.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número entero.")

    paises_visitados = set()
    for i in range(num_paises):
        pais = input(f"Ingrese el país {i+1}: ")
        paises_visitados.add(pais)

    paises[nombre] = paises_visitados
    print(f"{nombre} ha sido agregado a la lista con los países visitados: {paises_visitados}")


def consultar_paises_en_comun():
    persona1 = input("Ingrese el nombre de la primera persona: ")
    persona2 = input("Ingrese el nombre de la segunda persona: ")

    if persona1 not in paises or persona2 not in paises:
        print("Al menos una de las personas no se encuentra en el diccionario de países.")
        return

    paises_comunes = cuantos_en_comun(persona1, persona2)
    num_paises_comunes = len(paises_comunes)

    if num_paises_comunes == 0:
        print("Estas personas no tienen países en común.")
    else:
        print(f"{persona1} y {persona2} Estas personas tienen {num_paises_comunes} países en común: {', '.join(paises_comunes)}")


def visualizar_personas_y_paises():
    print("\n------ Personas y Países Visitados ------")
    for persona, paises_visitados in paises.items():
        num_paises_visitados = len(paises_visitados)
        print(f"{persona} ({num_paises_visitados} países): {', '.join(paises_visitados)}")


def editar_persona():
    nombre_original = input(
        "Ingrese el nombre de la persona que desea editar: ")
    if nombre_original not in paises:
        print("¡Esa persona no está en la lista!")
        return

    nuevo_nombre = input("Ingrese el nuevo nombre de la persona: ")
    while nuevo_nombre in paises:
        print("¡Ese nombre ya está en uso!")
        nuevo_nombre = input("Ingrese otro nuevo nombre de persona: ")

    num_paises = int(
        input("¿Cuántos países ha visitado esta persona ahora?: "))
    nuevos_paises_visitados = set()
    for i in range(num_paises):
        pais = input(f"Ingrese el país {i+1}: ")
        nuevos_paises_visitados.add(pais)

    del paises[nombre_original]
    paises[nuevo_nombre] = nuevos_paises_visitados
    print(f"Los datos de {nombre_original} han sido actualizados a {nuevo_nombre} con los países visitados: {nuevos_paises_visitados}")


def borrar_persona():
    nombre = input("Ingrese el nombre de la persona que desea borrar: ")
    if nombre not in paises:
        print("¡Esa persona no está en la lista!")
        return

    del paises[nombre]
    print(f"{nombre} y sus países visitados han sido eliminados de la lista.")


def menu():
    print("\n------ Menú ------")
    print("1. Agregar persona y países visitados")
    print("2. Consultar países en común entre dos personas")
    print("3. Visualizar personas y países visitados")
    print("4. Editar persona y países visitados")
    print("5. Borrar persona y países visitados")
    print("6. Salir")


while True:
    try:
        menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            agregar_persona()
        elif opcion == 2:
            consultar_paises_en_comun()
        elif opcion == 3:
            visualizar_personas_y_paises()
        elif opcion == 4:
            editar_persona()
        elif opcion == 5:
            borrar_persona()
        elif opcion == 6:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
    except Exception as e:
        print("Por favor, ingrese un número entero válido. Error: ", str(e))
