import string

def es_pangrama(texto):
    letras = set(texto.lower())
    return all(letra in letras for letra in string.ascii_lowercase)
