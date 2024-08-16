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