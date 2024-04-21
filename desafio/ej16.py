"""
16- Código Morse. Crea un programa que sea capaz de transformar texto natural a
código morse y viceversa.

9 Recuperado de: https://progra-utfsm.readthedocs.io/en/latest/ejercicios/2/autores-libros.html
7

● Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
● En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos
espacios entre palabras " ".
● El alfabeto morse soportado será el mostrado en
https://es.wikipedia.org/wiki/Código_morse
"""

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}


def texto_a_morse(texto):
    morse = []
    for char in texto.upper():
        if char == ' ':
            morse.append(' ')
        elif char in MORSE_CODE_DICT:
            morse.append(MORSE_CODE_DICT[char])
        else:
            morse.append('')
    return ' '.join(morse)


def morse_a_texto(morse):
    texto = []
    for word in morse.split('  '):
        for char in word.split(' '):
            if char in MORSE_CODE_DICT.values():
                texto.append(list(MORSE_CODE_DICT.keys())[
                             list(MORSE_CODE_DICT.values()).index(char)])
        texto.append(' ')
    return ''.join(texto).strip()


entrada = input("Ingrese texto o código Morse: ")

# Detectar si la entrada es texto o Morse y realizar la conversión
if any(char in MORSE_CODE_DICT.keys() for char in entrada.upper()):
    resultado = texto_a_morse(entrada)
    print("Texto convertido a código Morse:", resultado)
else:
    resultado = morse_a_texto(entrada)
    print("Código Morse convertido a texto:", resultado)
