""" Listas """

# Definición de una lista
frutas = ["manzana", "banana", "cereza"]

# Acceso a elementos
print(frutas[0])  # Output: manzana

# Modificación de elementos
frutas[1] = "pera"

# Añadir elementos
frutas.append("naranja")

# Remover elementos
frutas.remove("cereza")

print(frutas)

""" Tuplas """
# Definicion de una tupla

colores = ("rojo", "verde", "azul")

# Acceso a elementos
print(colores[1])  # Output: verde

# Intentar modificar una tupla resultará en un error
# colores[0] = "amarillo"  # Error: las tuplas no se pueden modificar

""" Conjuntos (Sets) """

# Definición de un conjunto
numeros = {1, 2, 3, 4}

# Añadir elementos
numeros.add(5)

# Eliminar elementos
numeros.remove(3)

# Operaciones de conjunto
pares = {2, 4, 6, 8}
interseccion = numeros.intersection(pares)

print(interseccion)  # Output: {2, 4}

