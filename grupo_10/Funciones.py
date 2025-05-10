def saludar(nombre):
    mensaje = f"Hola, {nombre}!"
    return mensaje

# Llamada a la función
resultado_saludo = saludar("Juan")
print(resultado_saludo)
def suma(a, b):
    return a + b

resultado_suma = suma(3, 5)
print(resultado_suma)  # Salida: 8

def saludar(nombre, saludo="Hola"):
    mensaje = f"{saludo}, {nombre}!"
    return mensaje

resultado_saludo = saludar("María", saludo="Buen día")
print(resultado_saludo)

longitud = len("Hola")
print(longitud)  # Salida: 4

def celsius_a_fahrenheit(celsius):
    return(celsius * 9/5)+32

temperatura_celsius=25
print(celsius_a_fahrenheit(temperatura_celsius))