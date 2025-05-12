'''
ACTIVIDAD 6
Funciones en Python
'''


def saludar(nombre):
    mensaje = f'Hola, {nombre}!'
    return mensaje


# Llamada a la funcion
resultado_saludo = saludar('Juan')
print(resultado_saludo)


def suma(a, b):
    return a + b


# Llamada a la funcion
resultado_suma = suma(3, 5)
print(resultado_suma)


def saludar(nombre, saludo='Hola'):
    mensaje = f'{saludo}, {nombre}!'
    return mensaje


# Llamada a la funcion
resultado_saludo = saludar('maria', saludo='buenas tardes')
print(resultado_saludo)


longitud = len('Hola')
print(longitud)


# Ejercicio Conversión de Celsius a Fahrenheit
# Crea una función llamada 'celsius_a_fahrenheit' que toma una temperatura en grados Celsius y la
# convierte a Fahrenheit.
# La fórmula es: Fahrenheit = (Celsius * 9/5) + 32.
# Luego, llama a la función con una temperatura e imprime el resultado.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


temperatura_celcius = 25
print(celsius_a_fahrenheit(temperatura_celcius))

# Ejercicio Verificación de Número Primo
# Define una función llamada 'es_primo' que toma un número como parámetro y devuelve
# True si es primo, False si no.
# Luego, llama a la función con un número e imprime el resultado.
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


numero_primo = 7
print(es_primo(numero_primo))


# Ejercicio Suma de Cuadrados
# Crea una función llamada 'suma_cuadrados' que toma dos números como parámetros y devuelve la suma
# de sus cuadrados.
# Luego, llama a la función con dos números e imprime el resultado.
def suma_cuadrados(a, b):
    return a**2 + b**2


numero1 = 3
numero2 = 4
print(suma_cuadrados(numero1, numero2))


# Ejercicio Saludo Personalizado
# Define una función llamada 'saludar' que toma un nombre como parámetro y devuelve un
# saludo personalizado.
# Luego, llama a la función con tu nombre e imprime el resultado.
def saludar(nombre):
    return f'Hola, {nombre}!'


nombre_usuario = 'Eduardo'
print(saludar(nombre_usuario))
