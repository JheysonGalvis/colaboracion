
# Operaciones con Cadenas:
cadena1 = "Hola "
cadena2 = "Cómo estás"
cadena3 = cadena1 + cadena2
print("El tamaño de la cadena resultante es ", len(cadena3))


# Formato Cadenas
nombre = "Ronald"
print(f"Hola {nombre}, bienvenido a la clase de Python")


# Subcadenas y Métodos:
cadena = "Bienvenido a la clase de Python, espero que te guste"
lista_palabras = cadena.split()
print(lista_palabras)
print(cadena.find("Python"))


# Métodos de Mayúsculas y Minúsculas
minusculas = "análisis de datos utilizando python"
mayusculas = "INTELIGENCIA ARTIFICIAL"
print(minusculas.upper())
print(mayusculas.lower())

# Operaciones Aritméticas
a = 25
b = 3
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
exponente = a ** b
print("El resultado de la suma es: ", suma)
print("El resultado de la resta es: ", resta)
print("El resultado de la multiplicación es: ", multiplicacion)
print("El resultado de la división es: ", division)
print("El resultado de la potencia es: ", exponente)

# División y Módulo
num1 = 32
num2 = 5
resultado = num1 / num2
residuo = num1 % num2
print("El resultado de la división es: ", resultado)
print("El residuo de la división es: ", residuo)

# Precisión de Flotantes
entero = 24
flotante = 3.2
print(entero * flotante)
print(entero + flotante)
print(entero / flotante)
print(entero / entero)
print(entero - flotante)
