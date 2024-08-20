"""
2. Verificación de Palíndromos

Este ejercicio verifica si una cadena es un palíndromo, es decir, si se lee igual de adelante hacia atrás,
ignorando espacios, mayúsculas y puntuación.

"""
def es_palindromo(texto):
    # Eliminar espacios, eliminar acentos y convertir a minusculas
    texto_normalizado = texto.replace(" ", "").replace(",", "").replace(".", "").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").lower()
    # Obtener el texto invertido
    texto_invertido = texto_normalizado[::-1]
    
    if texto_invertido == texto_normalizado:
        print("El texto es un palindromo")
    else:
        print("El texto no es un palindromo")

cadena = "Allí por la tropa portado, traído a ese paraje de maniobras, una tipa como capitán usar boina me dejara, pese a odiar toda tropa por tal ropilla"

es_palindromo(cadena)