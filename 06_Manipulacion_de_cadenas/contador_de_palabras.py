""" 1. Contador de Palabras
Este ejercicio cuenta las palabras que contiene una cadena de texto dada."""

def contar_palabras(texto):
    # Convertimos la cadena a una lista
    lista = texto.split(" ") if texto else [] # Usmaos el condicional if si recibimos una cadena vacia la lista generada este vacia.
    print(len(lista))

contar_palabras("Allí por la tropa portado, traído a ese paraje de maniobras, una tipa como capitán usar boina me dejara, pese a odiar toda tropa por tal ropilla")