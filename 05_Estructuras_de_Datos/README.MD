# Estructuras de Datos en Python

## Introducción

Las estructuras de datos son fundamentales en la programación, ya que nos permiten organizar, almacenar y manipular datos de manera eficiente. Python ofrece varias estructuras de datos integradas, que incluyen listas, tuplas, conjuntos y diccionarios. Cada una de estas estructuras tiene características y usos específicos que exploraremos en esta lección.

## Listas

Las listas son colecciones ordenadas y mutables de elementos. Pueden contener diferentes tipos de datos y permiten modificaciones después de su creación.

### Ejemplo de Lista

```python
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
```
### Resultado esperado
```plaintext
manzana
['manzana', 'pera', 'naranja']
```

## Tuplas
Las tuplas son similares a las listas, pero son inmutables. Esto significa que una vez que se crean, no se pueden modificar.

### Ejemplo de tuplas
```python
# Definicion de una tupla

colores = ("rojo", "verde", "azul")

# Acceso a elementos
print(colores[1])  # Output: verde

# Intentar modificar una tupla resultará en un error
# colores[0] = "amarillo"  # Error: las tuplas no se pueden modificar
```
## Conjuntos (Sets)

```python
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
```

## Diccionarios

Los diccionarios son colecciones desordenadas de pares clave-valor. Son útiles cuando necesitas asociar elementos de una manera que puedas acceder a ellos mediante una clave.

```python
# Definición de un diccionario
estudiante = {
    "nombre": "Victor",
    "edad": 25,
    "curso": "Python"
}

# Acceso a valores por clave
print(estudiante["nombre"])  # Output: Victor

# Modificación de valores
estudiante["edad"] = 26

# Añadir nuevos pares clave-valor
estudiante["grado"] = "A"

print(estudiante)  # Output: {'nombre': 'Victor', 'edad': 26, 'curso': 'Python', 'grado': 'A'}
```
## Cómo Ejecutar el Programa
1. Guarda el código en un archivo llamado estructuras_de_datos.py.

2. Abre la terminal y navega hasta el directorio donde guardaste estructuras_de_datos.py.

3. Ejecuta el archivo con el siguiente comando:
```bash
python estructuras_de_datos.py
```

## Resultado esperado
```plaintext
manzana
['manzana', 'pera', 'naranja']
verde
{2, 4}
```