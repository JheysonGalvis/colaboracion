'''
ACTIVIDAD 3
Variables en Python
'''

# Ejemplo basico de uso de print
mensaje = "Hola, mundo"
print(mensaje)

# Formateo de cadenas
nombre = "Eduardo"
edad = 41
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

#Cambiando el caracter al final de la salida
print("Hola", end=" ")
print("mundo!")

# Especificando un separador diferente
nombre = "Eduardo"
edad = 41
print(nombre, edad, sep="-")

#Ejemplo de declaracion y asignacion de variables
nombre = "Eduardo"
edad = 41
altura = 1.86
es_estudiante = True

#Asignacion de valores en la declaracion
ciudad = "Madrid"
poblacion = 3200000

#Reasignacion de valores
ciudad = "Barcelona"
poblacion = 1600000

#Convenciones de nombres
nombre_completo = "Eduardo Garcia"
temperatura_actual = 25.5

# Tipos de variables dinamicos
variable_dianmica = 10
print(variable_dianmica)

variable_dianmica = "Hola"
print(variable_dianmica)

# Enteros
entero_positivo = 42
entero_negativo = -10

# Flotantes
flotante_1 = 3.14
flotante_2 = -2.5

# Operaciones con enteros y flotantes
resultado_suma = entero_positivo + flotante_1
resultado_multiplicacion = entero_negativo * flotante_2

# Impresion de resultados
print(resultado_suma)
print(resultado_multiplicacion)

# Cadenas
cadena_simple = 'Hola, mundo!'
cadena_doble = "Python es divertido"

# Concatenacion de cadenas
saludo_completo = cadena_simple + ' ' + cadena_doble
print(saludo_completo)

# EJERCICIOS
# Ejercicio 1: OPERACIONES CON CADENAS
# Crea dos variables de cadena llamadas
# cadena1 y cadena2.
# Concatena las dos cadenas y guarda el
# resultado en una nueva variable.
# Imprime la longitud de la cadena resultante.
cadena_1 = "Hola"
cadena_2 = "Mundo"
cadena_concatenada = cadena_1 + " " + cadena_2
print(len(cadena_concatenada))

# Ejercicio 2: SUBCADENAS Y METODOS
# Crea una cadena larga y utiliza el método split()
# para dividirla en una lista de palabras.
# Encuentra e imprime la posición de una
# subcadena especíca.
cadena_larga = "Python es un lenguaje de programación muy popular"
lista_palabras = cadena_larga.split()
posicion_subcadena = cadena_larga.find("lenguaje")
print(f"La subcadena 'lenguaje' se encuentra en la posición: {posicion_subcadena}")

# Ejercicio 3: FORMATEO DE CADENAS
# Crea una variable con tu nombre.
# Utiliza el formato de cadena para imprimir un
# mensaje de bienvenida personalizado.
nombre_usuario = "Eduardo"
mensaje_bienvenida = f"¡Bienvenido, {nombre_usuario}!"
print(mensaje_bienvenida)

# EJERCICIO 4: Métodos de Mayúsculas y Minúsculas:
# Crea una cadena en minúsculas y conviértela a
# mayúsculas usando los métodos upper() y lower().
cadena_minusculas = "hola, mundo"
cadena_mayusculas = cadena_minusculas.upper()
print(cadena_mayusculas)

# Ejercicio 5: Operaciones aritmeticas
# Crea dos variables, a y b, con valores numéricos.
# Realiza operaciones aritméticas básicas (suma, resta, multiplicación, división,
# exponente) con estas variables e imprime los resultados.
a = 10
b = 5
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
exponente = a ** b
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"Exponente: {exponente}")

# Ejercicio 6: División y Módulo:
# Divide dos números enteros y guarda el resultado en una variable llamada resultado.
# Utiliza el operador módulo (%) para obtener el residuo de la división e imprímelo.
numero1 = 10
numero2 = 3
resultado = numero1 / numero2
residuo = numero1 % numero2
print(f"Resultado de la división: {resultado}")
print(f"Residuo de la división: {residuo}")

# Ejercicio 7: Precisión de Flotantes:
# Crea una variable c con un valor flotante.
# Realiza operaciones aritméticas que involucren
# flotantes y enteros.
# ¿Cómo se manejan las operaciones mixtas?
c = 3.14
d = 2
resultado_flotante = c + d
resultado_entero = c * d
print(f"Resultado de la suma: {resultado_flotante}")
print(f"Resultado de la multiplicación: {resultado_entero}")
print("Las operaciones mixtas se manejan automáticamente en Python, convirtiendo el resultado al tipo más preciso.")