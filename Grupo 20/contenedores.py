# creacion de tuplas
mi_tupla = (1, 2, 3, 'a', 'b', 'c')
primer_elemento = mi_tupla[0] # resultado: 1
tercer_elemento = mi_tupla[2] # resultado: 3
longitud = len(mi_tupla) # resultado 6
# Modificar un elemento de mi_tupla
# mi_tupla[0] = 'x' - debido a que las tuplas no se pueden modificar aquí nos saldría un error

#Desempaquetado de Tuplas
coordenadas = ('longitud', 'latitud')
x, y = coordenadas
print(f'Las coordenadas son {x},{y}')

# operaciones básicas con diccionarios
mi_diccionario = {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'}
# Agregue un nuevo valor
mi_diccionario['clave1'] = 'nuevo_valor'
mi_diccionario['nueva_clave'] = 'valor_nuevo'
# imprimir claves de mi diccionario
for clave in mi_diccionario:
    print(clave)  # Imprime cada clave por separado

#Diccionarios Anidados
contactos = {1: {'nombre': 'Eduardo','edad': 23}, 2:{'nombre': 'Juan','edad':35}, 3:{'nombre': 'Maria','edad':55}}
print(f'Nombre: {contactos[2]['nombre']}, Edad: {contactos[2]['edad']}')

#Iteración y actualización
for i in contactos:
    print(f'''
          Clave: {i}
          Valor: {contactos[i]}''')
contactos[2] = {'nombre': 'Rocío', 'edad': 26}
print(f'el nuevo valor de la clave 2 es: {contactos[2]}')

#Esto es un comentario de Christian Villa