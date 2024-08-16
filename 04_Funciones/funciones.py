# Funciones en python

# Definicion de funcion
def saludo(nombre):
    # Funcion que devuelve un saludo personalizado
    print(f"Hola {nombre}, como estas? ")

# Llamada a la funcion
saludo("Victor")

# Funcion con retorno de valor
def suma(a,b):
    return a + b

resultado = suma(4,5)
print(f"El resultado es: {resultado}" )

# Funciones con parametros predeterminados
def greet(name="Invitado"):
    """Función que saluda, con un valor predeterminado."""
    print(f"Hola, {name}!")

# Llamando a la función greet
greet()          # Usa el valor predeterminado
greet("Victor")  # Usa el argumento proporcionado