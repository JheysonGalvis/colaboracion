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
