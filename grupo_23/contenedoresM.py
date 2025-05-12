#Declaración de una lista (Utilizando [])

mi_lista = [1, 2, 3, 'a', 'b', 'c']

#índice y acceso a elementos
#Se enumeran desde 0 en adelante, y se puede acceder a un elemento mediante su índice

primer_elemento = mi_lista[0] #Accede al primer elemento
segundo_elemento = mi_lista[2] #Accede al tercer elemento (índice 2)

print(f"El valor del primer elemento de la lista es: {primer_elemento}")
print(f"El valor del tercer elemento de la lista es: {segundo_elemento}")

#Longitud de una lista, con la función len()

longitud = len(mi_lista)
print(f"La longitud de la lista actual es de: {longitud} elementos")

#Modificación de elementos (Las listas son mutables)

mi_lista[3] = 'x'
print(f"La lista queda de la siguiente manera al reemplazar el elemento N°4: {mi_lista}")

#OPERACIONES COMUNES CON LISTAS

#Agregar elementos al final de la lista
mi_lista.append(4) #Resultado: [1, 2, 3, 'x', 'b', 'c', 4]

#Eliminar elemento por valor
mi_lista.remove('b') #Resultado: [1, 2, 3, 'x', 'c', 4]

#Extender la lista con otra lista
otra_lista = [5, 6]
mi_lista.extend(otra_lista) #Resultado: [1, 2, 3, 'x', 'c', 4, 5, 6]

#Ténica de slicing (rebanado)

sublista = mi_lista[1:4] #Resultado: [2, 3, 'x']

#Inclusión de elemento (Verificación de si un elemento está presente en la lista)
existe = 'c' in mi_lista #Resultado: True
print(f"Existe el elemento 'c' en mi lista? {existe}")

#Declaración de una tupla "Se utiliza paréntesis()""

print() #Salto de línea para diferenciar los ejercicios de listas con los de tuplas
mi_tupla = (1, 2, 3, 'a', 'b', 'c')
print(f"Mi tupla es la siguiente: {mi_tupla}")

#índices y acceso de elementos en tuplas

primer_elemento = mi_tupla[0] #Resultado = 1
tercer_elemento = mi_tupla[2] #Resultado = 3

print(f"El valor del primer elemento de la tupla es: {primer_elemento}")
print(f"El valor del tercer elemento de la tupla es: {tercer_elemento}")

#Longitud de una tupla

longitud_tupla = len(mi_tupla)
print(f"La longitud de la tupla actual es de {longitud_tupla} elementos")

#Prueba de inmutabilidad en tuplas

#Esto generará un error, por lo tanto lo dejamos como comentario
""" mi_tupla[0] = 'x' """

#Empaquetado y desempaquetado de tuplas

coordenadas = (10, 20) #Esto es una tupla con 2 valores
x, y = coordenadas #Ahora x es 10, y es 20 (Desempaquetado)
print(x)
print(y)

#Tuplas anidadas

tupla_anidada = ((1, 2), ('a', 'b'))
print(f"La tupla anidada es la siguiente: {tupla_anidada}")

#Declaración de un diccionario

print() #Salto de línea para diferencias los ejercicios con diccionarios
mi_diccionario = {'clave1' : 'valor1', 'clave2' : 'valor2', 'clave3' : 'valor3'}
print(f"El diccionario incial es el siguiente: {mi_diccionario}")

#Acceso a elementos por clave

valor_asociado_a_clave1 = mi_diccionario['clave1']
print(f"El valor asociado a la clave 1 es: {valor_asociado_a_clave1}")

#Modificación y adición de elementos en diccionario

mi_diccionario['clave1'] = 'nuevo_valor' #Se modifica el valor de una clave existente
mi_diccionario['nueva clave'] = 'valor_nuevo' #Se agrega una nueva clave al diccionario al final
print(f"El diccionario modificado es el siguiente: {mi_diccionario}")

#Eliminación de elementos en diccionario

del mi_diccionario['clave1'] #Eliminamos la clave 1 y su valor asociado

#Verificación de existencia de claves en diccionario

existe_clave = 'clave1' in mi_diccionario #Resultado: False (ya que lo eliminamos)
print(f"Existe la clave 1 en nuestro diccionario? {existe_clave}") #Respuesta valor booleano

#Longitud del diccionario

cantidad_elementos = len(mi_diccionario) #Resultado: 3 (luego de eliminar una clave)
print(f"La cantidad de elementos en el diccionario son {len(mi_diccionario)}")

#Iteración a través de claves, valores o elementos

print("Mostrando claves y sus valores:")
for clave in mi_diccionario:
    valor = mi_diccionario[clave]
    print(f"La clave '{clave}' tiene el valor '{valor}'")

#Diccionarios anidados

diccionario_anidado = {'clave1' : {'subclave1': 'valor_subclave1'}, 'clave2': {'subclave2': 'valor_subclave2'}}
print(f"El diccionario anidado es el siguiente: {diccionario_anidado}")

#Ejercicios
#1. Creación de tuplas

#Cree una tupla llamada mi_tupla con tres elementos de tu elección
mi_tupla = (1, 2, 3, 'm')

#Intente modificar un elmento de mi_tupla. ¿Qué sucede?

"""mi_tupla[0] = 'x'
print(mi_tupla)"""    #Se genera error porque las tuplas son inmutables

#2. Desempaquetado de tuplas

#Cree una tupla de ds elementos llamadas coordenadas con valores de latitud y longitud
coordenadas = ('latitud', 'longitud')

#Utilice el desempaquetado de tuplas para asignar estos valores a dos variables distintas
x, y = coordenadas
print(f"El valor x, representa: {x}")
print(f"El valor y, representa: {y}")

#3. Operaciones básicas con diccionarios:

#Cree un diccionario llamado mi_diccionario con al menos tres pares clave-valor
mi_diccionario = {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'}

#Agregue una nueva clave-valor a mi_diccionario
mi_diccionario['clave4'] = 'valor4'
print(mi_diccionario) #Solo para verificación

#Imprima sólo las claves del diccionario
print("Mostrando solo las claves del diccionario:")
for clave in mi_diccionario:
    print(clave)

#Imprima solo los valores
print("Mostrando solo los valores del diccionario:")
for valor in mi_diccionario.values():
    print(valor)

#Imprimir clave y valor al mismo tiempo
print("Mostrando claves y sus valores:")
for clave, valor in mi_diccionario.items():
    print(f"{clave} => {valor}")

#4. Ejercicio de diccionarios anidados

#Cree un diccionario anidado llamados contactos con información de al menos dos personas (nombre, edad, etc.)

contactos = {'Juan': {'edad': 25, 'altura': 1.75, 'peso': 70}, 'Juliana': {'edad': 30, 'altura': 1.65, 'peso': 60}}
print("Diccionario completo de contactos:")
print(contactos)

#Acceda e imprima información específica de una persona utilizando el diccionario anidado

#Acceder a la información específica de Juan
info_juan = contactos['Juan'] #Esto devuelve otro diccionario
print("\nInformación de Juan: ")
print(info_juan)

#Acceder directamente a la edad de Ana
edad_juliana = contactos['Juliana'] ['edad'] #Accedemos mediante 2 niveles de claves contactos['Juliana']['edad']
print(f"\nLa edad de Juliana es: {edad_juliana} años")

#5. Ejercicio de iteración y actualización

#Utilice un bucle for para todas las claves y valores de mi_diccionario

print(mi_diccionario)
for clave, valor in mi_diccionario.items(): #items devuelve tuplas del tipo (clave, valor)
    #for clave, valor in ---> desempaqueta las tuplas en 2 variables
    print(f"\nLa clave: {clave} tiene el valor: {valor}")

#Actualice el valor de una clave en mi_diccionario
mi_diccionario['clave1'] = 'valor_actualizado'
print(f"El diccionario con la actualización es el siguiente: {mi_diccionario}")

#6. Operaciones básicas de listas

#Cree una lista vacia llamada mi_lista

mi_lista = []
#Otra forma de crear lista vacía sería: mi_lista = list()
print(f"Contenido de mi_lista: {mi_lista}")
print(f"La longitud de mi_lista es: {len(mi_lista)}")  # Debería ser 0

#Agregue los números del 1 al 5 a mi_lista / Imprimima mi_lista

#Forma 1 con el método .append()
mi_lista.append(1)
mi_lista.append(2)
mi_lista.append(3)
mi_lista.append(4)
mi_lista.append(5)
print(f"Mi lista actualizada es: {mi_lista}")

#Forma 2 con el método .extend()
mi_lista = []
mi_lista.extend([1, 2, 3, 4, 5])
print(f"Mi lista actualizada es: {mi_lista}")

#Elimine el número 3 de la lista
mi_lista.remove(3)
print(f"La lista finalmente queda asi: {mi_lista}")

#7. Ejercicio de listas y ciclos

#Utilice un bucle for para imprimir cada elemento de mi_lista creado en el ejercicio anterior
for elemento in mi_lista:
    print(f"Elemento de la lista: {elemento}")

"""Este es un ciclo for que recorre todos los elementos de la lista llamada mi_lista
La palabra 'elemento' es una variable temporal que yo mismo puedo nombrar como quiera.
En cada vuelta del ciclo, 'elemento' toma el valor de un ítem diferente de la lista.
Por ejemplo: si mi_lista = [1, 2, 3], primero elemento = 1, luego 2, luego 3."""

#8. Ejercicio de rebanado de listas

#Cree una lista llamada números del 1 al 10
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Imprima los primeros tres elementos de números
sublista = numeros[0:3]
print(f"Los primeros tres elementos de la lista son: {sublista}")

#Imprima los elementos desde el tercero hasta el sexto
sublista1 = numeros[2:6]
print(f"Los elementos desde el tercero al sexto son: {sublista1}")

#Imprima los últimos dos elementos
sublista2 = numeros[-2:]
print(f"Los útlimos dos elementos son: {sublista2}")