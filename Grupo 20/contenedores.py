# creacion de tuplas
mi_tupla = (1, 2, 3, 'a', 'b', 'c')
primer_elemento = mi_tupla[0] # resultado: 1
tercer_elemento = mi_tupla[2] # resultado: 3
longitud = len(mi_tupla) # resultado 6
# Modificar un elemento de mi_tupla
# mi_tupla[0] = 'x' - debido a que las tuplas no se pueden modificar aquí nos saldría un error
# Empaquetado de mi_tupla
Coordenadas = (10, 20)
x, y = Coordenadas
# Ahora x es 10 y y es 20
# operaciones básicas con diccionarios
mi_diccionario = {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'}
# Agregue un nuevo valor
mi_diccionario['clave1'] = 'nuevo_valor'
mi_diccionario['nueva_clave'] = 'valor_nuevo'
# imprimir claves de mi diccionario
for clave in mi_diccionario:
    print(clave)  # Imprime cada clave por separado

