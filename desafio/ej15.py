"""
15- Autores de Libros. Este problema apareció en el certamen 2 del segundo semestre de
2011 en el campus Vitacura.
Escriba las funciones necesarias para que el siguiente programa funcione:
9libros = [
('Papelucho programador', 'Marcela Paz', 1983),
('Don Python de la Mancha', 'Miguel de Cervantes', 1615),
('Raw_input y Julieta', 'William Shakespeare', 1597),
('La tuplamorfosis', 'Franz Kafka', 1915),
# ...
]
autores = {
# autor: nacimiento, defunción, idioma
'William Shakespeare': ((1564, 4, 26), (1616, 5, 3), 'inglés'),
'Franz Kafka': ((1883, 7, 3), (1924, 6, 3), 'alemán'),
'Marcela Paz': ((1902, 2, 28), (1985, 6, 12), 'español'),
'Miguel de Cervantes': ((1547, 9, 29), (1616, 4, 22), 'español'),
# ...
}
titulo = input('Ingrese titulo del libro: ')
print 'El libro fue escrito en', obtener_idioma(titulo),
print 'por', obtener_autor(titulo)
print 'El autor fallecio', calcular_annos_antes_de_morir(titulo), 'años',
print 'después de haber escrito el libro'
"""

libros = [
    ('Papelucho programador', 'Marcela Paz', 1983),
    ('Don Python de la Mancha', 'Miguel de Cervantes', 1615),
    ('Raw_input y Julieta', 'William Shakespeare', 1597),
    ('La tuplamorfosis', 'Franz Kafka', 1915),
    # ...
]

autores = {
    # autor: (nacimiento, defunción, idioma)
    'William Shakespeare': ((1564, 4, 26), (1616, 5, 3), 'inglés'),
    'Franz Kafka': ((1883, 7, 3), (1924, 6, 3), 'alemán'),
    'Marcela Paz': ((1902, 2, 28), (1985, 6, 12), 'español'),
    'Miguel de Cervantes': ((1547, 9, 29), (1616, 4, 22), 'español'),
    # ...
}


def obtener_idioma(titulo):
    for libro in libros:
        if libro[0] == titulo:
            autor = libro[1]
            return autores[autor][2]
    return None

def obtener_autor(titulo):
    for libro in libros:
        if libro[0] == titulo:
            return libro[1]
    return None

def obtener_fecha_escritura(titulo):
    for libro in libros:
        if libro[0] == titulo:
            return libro[2]
    return None

def obtener_fecha_muerte_autor(titulo):
    autor = obtener_autor(titulo)
    if autor is not None:
        fecha_defuncion = autores[autor][1]
        return fecha_defuncion
    return None

def calcular_annos_antes_de_morir(titulo):
    for libro in libros:
        if libro[0] == titulo:
            autor = libro[1]
            fecha_libro = libro[2]
            fecha_defuncion = autores[autor][1]
            annos = fecha_defuncion[0] - fecha_libro
            return annos
    return None

# Mostrar lista de libros y autores disponibles
print("¡Bienvenido al determinador de detalles de libros!")
print("Lista de libros disponibles:")
for libro, autor, _ in libros:
    print(f"{libro} - Autor: {autor}")

# Solicitar al usuario el título del libro
titulo = input('\nIngrese el título del libro para obtener detalles: ')

# Obtener y mostrar información del libro
autor = obtener_autor(titulo)
if autor is not None:
    print(f'\nEl autor del libro "{titulo}" es {autor}.')
else:
    print(f'\nLo siento, el libro "{titulo}" no se encontró en la lista.')

idioma = obtener_idioma(titulo)
if idioma is not None:
    print(f'El libro "{titulo}" fue escrito en {idioma}.')
else:
    print(f'Lo siento, el idioma del libro "{titulo}" no se encontró en la lista.')

fecha_escritura = obtener_fecha_escritura(titulo)
if fecha_escritura is not None:
    print(f'El libro "{titulo}" fue escrito en el año {fecha_escritura}.')
else:
    print(f'Lo siento, no se pudo obtener la fecha de escritura del libro "{titulo}".')

fecha_muerte_autor = obtener_fecha_muerte_autor(titulo)
if fecha_muerte_autor is not None:
    print(f'El autor falleció en el año {fecha_muerte_autor[0]}.')
else:
    print(f'Lo siento, no se pudo obtener la fecha de muerte del autor del libro "{titulo}".')

annos_despues_de_escribir = calcular_annos_antes_de_morir(titulo)
if annos_despues_de_escribir is not None:
    print(f'El autor falleció {annos_despues_de_escribir} años después de haber escrito el libro.')
else:
    print(f'Lo siento, no se pudo calcular la cantidad de años después de haber escrito el libro "{titulo}".')
