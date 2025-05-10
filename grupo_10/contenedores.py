#################### LISTA
mi_lista = ['a', 'b', 'c', 1, 2, 3]
primer_elemento = mi_lista[0]  #Resultado: 1
tercer_elemento = mi_lista[2]  #Resultado: 3
print(primer_elemento)
print(tercer_elemento)
print(mi_lista[5])



longitud = len(mi_lista)
print(f'Longitud 1 = {longitud}')

mi_lista[3] = 2025
print(f'Este es el arreglo con modificaciones {mi_lista}')

# Agregar elementos al final de la lista
mi_lista.append(4)
mi_lista.append('grupo_10')

#Eliminar elementos por valor
mi_lista.remove('b')

# Extender la lista con otra lista
otra_lista = [5, 6]
mi_lista.extend(otra_lista)
mi_lista.remove(5)
print(mi_lista)
longitud = len(mi_lista)
print(f'Longitud 2 = {longitud}')

sublista = mi_lista[3:6]
print(f'Sublista = {sublista}')

existe = 'c' in mi_lista
print(f'Existe? {existe}')

#################### TUPLAS

mi_tupla = (1, 2, 3, 'a', 'b', 'c')
print(f'primer_elemento {mi_tupla[0]}')
print(f'tercer_elemento {mi_tupla[2]}')

longitud = len(mi_tupla)

#mi_tupla[0] = 'x'

coordenadas = (10, 20, 30)

x, y, j = coordenadas
print(x)
print(y)
print(j)

tupla_anidada = ((1, 2),('a', 'b'))
print(tupla_anidada[0][1])
#mi_lista.remove(5)
print(mi_lista)

#################### DICCIONARIO
mi_diccionario = {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'}
valor_asociado_a_clave1 = mi_diccionario['clave1']
mi_diccionario = {
    'nombre': 'Juan',
    'edad': 30,
    'ciudad': 'Madrid'
}

#resultado:'valor1'
print (mi_diccionario['ciudad'])
mi_diccionario['clave1'] = 'nuevo_valor'
mi_diccionario['nueva_clave1'] = 'valor_nuevo'
del mi_diccionario['clave1']
print(mi_diccionario)
existe_clave = 'clave1' in mi_diccionario
#Resultado: False (ya que la eliminamos)
print(existe_clave)
cantidad_elementos = len(mi_diccionario)
#Resultado:2 (luego de eliminar una clave)
print(cantidad_elementos)
for clave in mi_diccionario:
    valor= mi_diccionario[clave]
    print(valor)

diccionario_anidado = {'clave1': {'subclave1': 'valor_subclave1'},'clave2': {'subclave2': 'valor_subclave2'}}
print(diccionario_anidado['clave1']['subclave1'])