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