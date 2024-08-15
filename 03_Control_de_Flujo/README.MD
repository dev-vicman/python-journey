# Control de Flujos

## Introduccón

El control de flujo en Python te permite tomar decisiones y ejecutar diferentes partes del código basado en ciertas condiciones. Esto es crucial para hacer que tus programas sean dinámicos y adaptativos. En esta lección, exploraremos cómo usar condicionales y bucles para controlar el flujo de tu programa.

## Condicionales

Los condicionales permiten ejecutar bloques de código basados en si una condición es verdadera o falsa. En Python, se usan las estructuras `if`, `elif`, y `else`.

```python
# Ejemplo de condicionales

edad = 89

if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Acabas de Cumplir la mayoria de edad")
else:
    print("Ya eres un adulto")
```

* `if`: Ejecuta el bloque de código si la condición es verdadera.
* `elif`: Ejecuta el bloque de código si las condiciones anteriores son falsas y esta condición es verdadera.
* `else`: Ejecuta el bloque de código si todas las condiciones anteriores son falsas.

## Bucles
Los bucles permiten ejecutar un bloque de código múltiples veces. En Python, los bucles más comunes son `for` y `while`.

### Ejemplo del Bucle `for`

```python
# Ejemplo del bucle `for`

for i in range(5):
    print("Numero: ", i)
```
`for`: Itera sobre una secuencia (como una lista o un rango) y ejecuta el bloque de código para cada elemento.

### Ejemplo del bucle `while`

```python
# Ejemplo del bucle `while`
contador = 0
while contador < 5:
    print("Contador: ",contador)
    contador += 1
```
`while`: Ejecuta el bloque de código mientras la condición sea verdadera. En este ejemplo, se ejecuta el codigo mientras las variable *contador* es menor que 5

## Como ejecutar el programa

Para ver estos ejemplos en acción:

1. Guarda el código de cada ejemplo en un archivo llamado `control_flujo.py`.

2. Abre la terminal y navega hasta el directorio donde guardaste `control_flujo.py`.

3. Ejecuta el programa con el siguiente comando:
```bash
python control_flujo.py
```

## Resultado Esperado.
Al ejecutar el programa, deberías ver los siguientes outputs:

```plaintext
Ya eres un adulto
Numero:  0
Numero:  1
Numero:  2
Numero:  3
Numero:  4
Contador:  0
Contador:  1
Contador:  2
Contador:  3
Contador:  4
```