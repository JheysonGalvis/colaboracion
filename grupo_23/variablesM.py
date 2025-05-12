#1. Ejemplo básico de uso de print
mensaje = "Hola, mundo!"
print(mensaje)

#2. Formateo de cadenas
nombre = "Miguel Ángel"
edad = 26
#Aquí se usa una f-string (f"...") para insertar variables directamente dentro de una cadena de texto.
#Esto nos permite contruir frases dinámicas y más legibles
print(f"Mi nombre es {nombre} y tengo {edad} años")

#Cambiando el carácter al final de la salida
"""En este caso, se imprime "Hola" y al usar end=" ", se evita el salto de línea
y se agrega un espacio en su lugar"""
print("Hola", end=" ")
print("mundo!")

#3. Especificando un separador diferente
nombre = "Miguel"
edad = 26
# La función print() puede imprimir múltiples valores separados por comas.
# Por defecto, separa cada elemento con un espacio.
# Usando el parámetro 'sep', podemos cambiar ese separador. Se imprime "Miguel-26"
print(nombre, edad, sep="-")

#4. Ejemplo de declaración y asignación de variables
nombre = "Miguel" # Una variable de cadena
edad = 26 # Una variable de entero (int)
altura = 1.75 # Una variable de punto flotante (float)
es_estudiante = True # Una variable booleana

#5. Asignación de valores en la declaración
ciudad = "Marinilla"
población = 70390

# Reasignación de valores
ciudad = "Medellín"
población = 2533400

#6. Convenciones de nombres (Uso de la convención snake_case)
nombre_completo = "Miguel Jiménez"
temperatura_actual = 23.5

#7. Tipos de variables dinámicos
variable_diámica = 10
print(variable_diámica) #Salida: 10

variable_diámica = "Hola, cómo estás?"
print(variable_diámica) #Salida: Hola, cómo estás?

#8. Tipos de datos básicos 
#8.1 Enteros (int)
entero_positivo = 10
entero_negativo = -5

#8.2 Flotantes (float)
flotante_1 = 3.14
flotante_2 = -0.5

#Operaciones con enteros y flotantes
resultado_suma = entero_positivo + flotante_1
resultado_multiplicacion = entero_negativo * flotante_2

#Impresión de resultados
print(resultado_suma)
print(resultado_multiplicacion)

#8.3 Cadenas (string)
cadena_simple = "Hola, mundo!"
cadena_doble = "Python es divertido"

#Concatenación de cadenas ()
saludo_completo = cadena_simple + ' ' + cadena_doble
print(saludo_completo)

#9. Ejercicio operaciones con cadenas

#Crea dos variables de cadena llamadas cadena1 y cadena2
cadena_1 = "Aprendamos"
cadena_2 = "Python"

#Concatena las dos cadenas y guarda el resultado en una nueva variable
"""cadena_resultado = f"{cadena_1} {cadena_2}"    (Forma opcional de concatenar)"""
cadena_resultado = cadena_1 + " " + cadena_2

#Imprime la longitud de la cadena resultante
print(len(cadena_resultado))

#10. Ejercicio de formato de cadenas

#Crea una variable con tu nombre
name = "Miguel"

#Utiliza el formato de cadena para imprimir un mensaje de bienvenida personalizado
bienvenida = f"Bienvenido campista, {name}! Listo para seguir repasando ejercicios de variables?"
print(bienvenida)

#11. Ejercicio de subcadenas y métodos

#Crea una cadena larga y utiliza el método split() para dividirla en una lista de palabras
saludo = "Hola Miguel Ángel espero te encuentres listo para resolver este reto"

#Usar split() para dividir la cadena en palabras
palabras = saludo.split()
print("Lista de palabras: ", palabras)

#Encuentra e imprime la posición de una subcadena específica
#Si la encuentra, devuelve la posición del primer carácter; si no, devuelve -1
posicion = saludo.find("resolver")
print("La palabra 'resolver' empieza en la posición: ", posicion)

#12. Ejercicio de métodos de Mayúsculas y Minúsculas

"""Crea una cadena en minúsculas y conviértela a mayúsculas usando los métodos
upper() y lower()"""

cadena_a = "Hola compañeros"
print(cadena_a.upper()) #Convierte la cadena a mayúsculas
print(cadena_a.lower()) #Convierte la cadena a minúsculas
print(cadena_a.title()) #Capitaliza cada palabra de la cadena

#13. Ejercicio operaciones aritméticas

#Crea dos variables, a y b, con valores numéricos.
a = 10
b = 5

"""Realiza operaciones aritméticas básicas (suma, resta, multiplicación, división, exponente)
con estas variables e imprime los resultados"""

suma = a + b
print (f"Suma: {a} + {b} = {suma}")

resta = a - b
print (f"Resta: {a} - {b} = {resta}")

multiplicacion = a * b
print (f"Multiplicación: {a} * {b} = {multiplicacion}")

division = a / b
print (f"División: {a} / {b} = {division}")

exponente = a ** b
print (f"Exponente: {a} ** {b} = {exponente}")

#14. Ejercicio de división y módulo

#Divide dos números enteros y guarda el resultado en una variable llamada resultado
c = 17
d = 4
resultado = c / d
print(f"Resultado de la división: {resultado}")

#Utiliza el operador módulo (%) para obtener el residuo de la división e imprimelo
residuo = c % d
print(f"Residuo de la división: {residuo}")

#15. Ejericio de precisión de flotantes

#Crea una variable c con un valor flotante
a = 15
c = 4.25

#Realiza operaciones aritméticas que involucren flotantes y enteros

operacion_aritmetica = (c / a) * c 
"""Python convierte automáticamente el entero a flotante paramantener la precisión del resultado
Es decir, si mezclas un int con un float, el resultado siempre será float."""

#¿Cómo se maneja las operaciones mixtas?

print(f"Este es el resultado de la operación mixta: (c/a) * c = {operacion_aritmetica}")
#Esto se llama conversión implícita de tipos o type coercion.

#Comprobación
print(f"Tipo de dato de la operación:", type(operacion_aritmetica))





