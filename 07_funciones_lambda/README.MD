# 07_funciones_lambda λ

Una función lambda en Python es una función anónima y compacta que se define en una sola línea usando la palabra clave lambda. A diferencia de las funciones regulares, no tiene nombre ni requiere la declaración explícita de def. Se usa comúnmente para tareas simples donde necesitas una función rápida y corta, como en expresiones de una sola línea o dentro de funciones como map(), filter(), o reduce().

#### Sintaxis
```python
lambda argumentos: expresión
```

#### Ejemplo

Vamos a definir una peque;a funcion lambda que nos permita sumar dos numeros.

```python
suma_numeros = lambda numero_1, numero_2: numero_1 + numero_2
```
En este caso hemos usado una variable para almacenar una funcion lambda y podemos hacer uso de ella, llamandola por el nombre de la variable y pasandole los parametros como si de una funcion comun se tratara.

```python
suma_numeros(1,5)
```

## Resolvamos algunos ejercicios:

### 1. Definir una función lambda simple: Escribe una función lambda que tome un número y lo multiplique por 2.

```python
multiplicado_por_2 = lambda numero: numero * 2

print(multiplicado_por_2(5))
```

### 2. Lambda con dos argumentos: Define una función lambda que tome dos números y devuelva su suma.
```python
suma_2_numeros = lambda num1, num2: num1 + num2

print(suma_2_numeros(3, 2))
```

### 3. Lambda con condicionales: Escribe una función lambda que devuelva "Par" si un número es divisible por 2 y "Impar" en caso contrario.

```python
par_o_impar = lambda numero: "Es par" if numero % 2 == 0 else "Es Impar"

print(par_o_impar(5))
```

# Lambda que devuelva el mayor de dos números: Define una función lambda que tome dos números y devuelva el mayor de ellos.

mayor_numero = lambda numero1, numero2: "Numero 1 es mayor" if numero1 > numero2 else "Numero 2 es mayor"

print(mayor_numero(5, 6))

# Lambda con tres argumentos: Escribe una función lambda que reciba tres números y devuelva su promedio.

promedio_tres_numeros = lambda numero_1, numero_2, numero_3: (numero_1 + numero_2 + numero_3)/3

print(promedio_tres_numeros(2, 2, 2))

# Lambda que concatene dos cadenas: Define una función lambda que tome dos cadenas y las concatene.

cadenas_concatenadas = lambda cadena_1, cadena_2: str(cadena_1) + str(cadena_2) 

print(cadenas_concatenadas("texto","Texto2"))

# Lambda que use un cálculo matemático: Define una función lambda que tome un número y devuelva su cuadrado más 5.

numer_cuadrado_mas_5 = lambda numero: (numero ** 2) + 5

print(numer_cuadrado_mas_5(2))

# Lambda que devuelva un booleano: Escribe una función lambda que determine si un número es mayor que 10.

numero_mayor_10 = lambda numero: numero > 10

print(numero_mayor_10(23))

# Lambda con múltiples operaciones: Define una función lambda que tome dos números, sume el primero con el cuadrado del segundo y luego reste 3 al resultado.

multiples_operaciones = lambda numero_1, numero_2: (numero_1 + numero_2 **2) - 3

print(multiples_operaciones(2,2))