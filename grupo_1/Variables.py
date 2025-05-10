# Ejemplo basico de uso de print
mensaje = 'Hola equipo'
print(mensaje)

# Formato de cadenas
nombre = 'Angel'
edad = 37
print(f'Mi nombre es {nombre} y tengo {edad} años')

# Cambiando el caracter al final de la salida
print('Hola', end=" ")
print('equipo')

# Especificando un separador diferente
nombre = 'Daniel'
edad = 25
print(nombre, edad, sep='-')

# Ejemplo de declaracion y asignacion de variables
nombre ='Estefania'
edad = 25
altura = 1.75
es_estudiante = True

# Asignacion de valores en la declaracion
ciudad = 'Nueva York'
poblacion = 8500000

# Reasignacion de valores
ciudad = 'Los Angeles'
poblacion = 4000000

# Convenciones de nombres
nombre_completo = 'Jane Doe'
temperatura_actual = 23.5

# Tipos de variables dinamicos

variable_dinamica = 10
print(variable_dinamica) # Salida: 10

variable_dinamica = 'Hola'
print(variable_dinamica) # Salida: Hola

# Tipos de datos basicos

# Enteros
entero_postivo = 10
entero_negativo = -5

# Flotantes
flotante_1 = 3.14
flotante_2 = -0.5

# Operaciones con enteros y flotantes
resultado_suma = entero_postivo + flotante_1
resultado_multiplicacion = entero_negativo * flotante_2

# Impresion de resultados
print(resultado_suma)
print(resultado_multiplicacion)

# Cadenas
cadena_simple = 'Hola, mundo'
cadena_doble = "Python es divertido"


# Concatenacion de cadenas
saludo_completo = cadena_simple + ' ' + cadena_doble
print(saludo_completo)



#--------------------------------------------------------------

# EJERCICIOS

#--------------------------------------------------------------


# Operaciones con cadenas
cadena1 = 'cadena1'
cadena2 = 'cadena2'
concatenacion_cadenas = cadena1 + cadena2
print(len(concatenacion_cadenas))

# Formato de cadenas
nombre = 'Angel'
print(f'Bienvenido {nombre} al mundo de Python')

# Subcadenas y metodos
lista_larga = 'Estos ejercicios proporcionan una variedad de situaciones para trabajar con números'
lista_palabras = lista_larga.split()
print(f'Lista de palabras: {lista_palabras}')
palabra = 'proporcionan'
posicion = lista_larga.find(palabra)
print(f'La palabra {palabra} esta en la posicion {posicion}')

# Metodos de mayusculas y minusculas
cadena_min = 'angel david aristizabal arias'
cadena_may = 'ANGEL DAVID ARISTIZABAL ARIAS'

cadena_min.upper()
cadena_may.lower()

# Operaciones aritmeticas
a = 5
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)

# Division y modulo
resultado = 10 / 3
print(10 % 3)

# Presision de flotantes
c = 5.4234
suma = a + c
resta = a - c
mult = a * c
div = a / c
print(f'el resultado de la suma es: {suma:.1f}')
print(f'el resultado de la resta es: {resta:.1f}')
print(f'el resultado de la multiplicacion es: {mult:.1f}')
print(f'el resultado de la division es: {div:.1f}')


