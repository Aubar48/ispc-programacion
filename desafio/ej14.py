"""
14- Signo zodiacal. El signo zodiacal de una persona está determinado por su día de
nacimiento.
El diccionario de signos asocia a cada signo el período del año que le corresponde. Cada
período es una tupla con la fecha de inicio y la fecha de término, y cada fecha es una
tupla (mes, dia):
signos = {
'aries': (( 3, 21), ( 4, 20)),
'tauro': (( 4, 21), ( 5, 21)),
'geminis': (( 5, 22), ( 6, 21)),
'cancer': (( 6, 22), ( 7, 23)),
'leo': (( 7, 24), ( 8, 23)),
'virgo': (( 8, 24), ( 9, 23)),
'libra': (( 9, 24), (10, 23)),
'escorpio': ((10, 24), (11, 22)),
'sagitario': ((11, 23), (12, 21)),
'capricornio': ((12, 22), ( 1, 20)),
'acuario': (( 1, 21), ( 2, 19)),
'piscis': (( 2, 20), ( 3, 20)),
8 Recuperado de_ https://progra-utfsm.readthedocs.io/en/latest/ejercicios/2/paises.html

6

}
Por ejemplo, para que una persona sea de signo libra debe haber nacido entre el 24 de
septiembre y el 23 de octubre.
Escriba la función determinar_signo(fecha_de_nacimiento) que reciba como
parámetro la fecha de nacimiento de una persona, representada como una tupla (año,
mes, dia), y que retorne el signo zodiacal de la persona:
>>> determinar_signo((1990, 5, 7))
'tauro'
>>> determinar_signo((1904, 11, 24))
'sagitario'
>>> determinar_signo((1998, 12, 28))
'capricornio'
>>> determinar_signo((1999, 1, 11))
'capricornio'

"""

signos = {
    'aries': ((3, 21), (4, 20)),
    'tauro': ((4, 21), (5, 21)),
    'géminis': ((5, 22), (6, 21)),
    'cáncer': ((6, 22), (7, 23)),
    'leo': ((7, 24), (8, 23)),
    'virgo': ((8, 24), (9, 23)),
    'libra': ((9, 24), (10, 23)),
    'escorpio': ((10, 24), (11, 22)),
    'sagitario': ((11, 23), (12, 21)),
    'capricornio': ((12, 22), (1, 20)),
    'acuario': ((1, 21), (2, 19)),
    'piscis': ((2, 20), (3, 20))
}

def determinar_signo(fecha_de_nacimiento):
    mes, dia = fecha_de_nacimiento[1], fecha_de_nacimiento[2]

    for signo, (inicio, fin) in signos.items():
        if (mes == inicio[0] and dia >= inicio[1]) or (mes == fin[0] and dia <= fin[1]):
            return signo

    # Si no se encuentra ningún signo, retornar un mensaje de error
    return "Fecha de nacimiento inválida."

def obtener_fecha_de_nacimiento():
    while True:
        try:
            año = int(input("Ingrese su año de nacimiento (ej. 1990): "))
            mes = int(input("Ingrese el número de mes de su nacimiento (1-12): "))
            dia = int(input("Ingrese el número de día de su nacimiento (1-31): "))
            if mes < 1 or mes > 12 or dia < 1 or dia > 31:
                print("Por favor, ingrese una fecha de nacimiento válida.")
            else:
                return año, mes, dia
        except ValueError:
            print("Por favor, ingrese valores numéricos para el año, el mes y el día.")

def presentar_signo(signo):
    print(f"¡Tu signo zodiacal es {signo.capitalize()}!")

# Obtener la fecha de nacimiento del usuario
print("Bienvenido al determinador de signos zodiacales.")
print("Por favor, ingrese su fecha de nacimiento.")

fecha_nacimiento = obtener_fecha_de_nacimiento()

# Determinar el signo zodiacal y presentarlo al usuario
signo = determinar_signo(fecha_nacimiento)
print()
if signo != "Fecha de nacimiento inválida.":
    presentar_signo(signo)
else:
    print("Lo siento, ha ingresado una fecha de nacimiento inválida.")
