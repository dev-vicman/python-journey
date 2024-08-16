# Funciones

## Introducción
Las funciones en Python son bloques de código reutilizables que realizan una tarea específica. Definir funciones te permite organizar tu código, hacer que sea más modular, y evitar la repetición. Las funciones pueden aceptar entradas (argumentos) y devolver un resultado (valor de retorno).

## Definir una función

Para definir una función en Python, se utiliza la palabra clave `def`, seguida del nombre de la función y paréntesis que pueden contener parámetros.

### Ejemplo de definición de función

```python
def saludo(nombre):
    # Funcion que devuelve un saludo personalizado
    print(f"Hola {nombre}, como estas? ")
```
* `def`: Inicia la definición de la función.
* `saludo`: Nombre de la función.
* `nombre`: Parámetro que recibe la función.
* `print(f"Hola {nombre}, como estas? ")`: Código que se ejecuta cuando la función es llamada.

### Llamada a la función
Una vez definida, puedes llamar a la función por su nombre, pasando los argumentos necesarios.

```python
saludo("Victor")
```
### Resultado esperado
```plaintext
Hola Victor, como estas?
```
## Funciones con Retorno de Valor

Las funciones pueden devolver valores usando la palabra clave `return`, permitiendo que el resultado de la función sea utilizado en otras partes del código.

```python
def suma(a,b):
    return a + b

resultado = suma(4,5)
print(f"El resultado es: {resultado}" )
```
### Resultado esperado
```plaintext
El resultado es: 9
```

## Parámetros con Valores Predeterminados
Puedes asignar valores predeterminados a los parámetros de una función. Si no se proporciona un argumento, se utiliza el valor predeterminado.

```python
def greet(name="Invitado"):
    """Función que saluda, con un valor predeterminado."""
    print(f"Hola, {name}!")

# Llamando a la función greet
greet()          # Usa el valor predeterminado
greet("Victor")  # Usa el argumento proporcionado
```
### Resultado esperado
```plaintext
Hola, Invitado!
Hola, Victor!
```
## Como ejecutar el programa

Para ver estos ejemplos en acción:

1. Guarda el código de cada ejemplo en un archivo llamado `funciones.py`.

2. Abre la terminal y navega hasta el directorio donde guardaste `funciones.py`.

3. Ejecuta el programa con el siguiente comando:
```bash
python funciones.py
```
