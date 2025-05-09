'''
ACTIVIDAD 4
Contenedores en Python
'''

mi_lista = [1, 2, 3, 'a', 'b', 'c']
primer_elemento = mi_lista[0]
tercer_elemento = mi_lista[2]
longitud_lista = len(mi_lista)
mi_lista[3] = 'x'
mi_lista.append(4)
mi_lista.remove('b')
otra_lista = [5, 6]
mi_lista.extend(otra_lista)
sublista = mi_lista[1:4]
existe = 'c' in mi_lista

mi_tupla = (1, 2, 3, 'a', 'b', 'c')
primer_elemento_tupla = mi_tupla[0]
tercer_elemento_tupla = mi_tupla[2]
longitud_tupla = len(mi_tupla)
# mi_tupla[0] = 'x' ESTO GENERA ERROR YA QUE LAS TUPLAS SON INMUTABLES
coordenadas = (10, 20)
x, y = coordenadas
tupla_anidada = ((1, 2), ('a', 'b'))

mi_diccionario = {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'}
valor_asociado_a_clave_1 = mi_diccionario['clave1']
mi_diccionario['clave1'] = 'nuevo_valor'
mi_diccionario['nueva_clave'] = 'valor_nuevo'
del mi_diccionario['clave1']
existe_clave = 'clave1' in mi_diccionario
cantidad_elementos = len(mi_diccionario)
for clave in mi_diccionario:
    valor = mi_diccionario[clave]
    
diccionario_anidado = {'clave1': {'subclave1': 'valor_subclave1'},
                       'clave2': {'subclave2': 'valor_subclave2'}}

# Creación de Tuplas:
# Cree una tupla llamada mi_tupla con tres elementos de tu elección.
# Intente modificar un elemento de mi_tupla. ¿Qué sucede?
mi_tupla = (1, 2, 3)
# mi_tupla[0] = 'x'  # Esto generará un error porque las tuplas son inmutables.


# Desempaquetado de Tuplas:
# Cree una tupla de dos elementos llamada coordenadas con valores de latitud y
# longitud.
# Utilice el desempaquetado de tuplas para asignar estos valores a dos variables
# distintas.
coordenadas = (10, 20)
latitud, longitud = coordenadas
print(latitud) 
print(longitud) 

# Operaciones Básicas con Diccionarios:
# Cree un diccionario llamado mi_diccionario con al menos tres pares clave-valor.
# Agregue una nueva clave-valor a mi_diccionario.
# Imprima sólo las claves del diccionario.
mi_diccionario = {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'}
mi_diccionario['clave1'] = 'eduardo'
print(mi_diccionario.keys())

# Diccionarios Anidados:
# Cree un diccionario anidado llamado contactos con información de al menos dos
# personas (nombre, edad, etc.).
# Acceda e imprima información especíca de una persona utilizando el diccionario anidado.
contactos = {'eduardo': {'edad': '41', 'color_favorito': 'rojo'},
             'marisela': {'edad': '48', 'color_favorito': 'azul'}}
print(contactos['eduardo']['color_favorito'])


# Iteración y Actualización:
# Utilice un bucle for para imprimir todas las claves y valores de mi_diccionario.
# Actualice el valor de una clave en mi_diccionario.
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")
mi_diccionario['clave2'] = 'marisela'
    
# Operaciones Básicas:
# Cree una lista vacía llamada mi_lista.
# Agregue los números del 1 al 5 a mi_lista.
# Imprima mi_lista.
# Elimine el número 3 de la lista.
mi_lista = []
for i in range(1, 6):
    mi_lista.append(i)
print(mi_lista)
mi_lista.remove(3)
print(mi_lista)


# Listas y Ciclos:
# Utilice un bucle for para imprimir cada
# elemento de mi_lista creado en el
# ejercicio 1.
for numero in mi_lista:
    print(numero)

# Rebanado de Listas:
# Cree una lista llamada números del 1 al 10.
# Imprima los primeros tres elementos de números.
# Imprima los elementos desde el tercero hasta el sexto.
# Imprima los últimos dos elementos.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros[:3])
print(numeros[2:6])
print(numeros[-2:])
