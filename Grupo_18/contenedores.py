# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Workspace built by group 18.
from grupo_10.contenedores import tupla_anidada, mi_diccionario, valor_asociado_a_clave1, cantidad_elementos


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    mensaje  = "Bienvenido a la actividad 4 - Contenedores en Python"
    print (mensaje)

    # Listas
    # Declaración de la lista
    mi_lista = [1, 2, 3, 'a', 'b', 'c']

    # Índices y acceso a los elementos
    primer_elemento = mi_lista[0] # Resultado = 1
    ultimo_elemento = mi_lista[-1]
    print(primer_elemento)
    print(ultimo_elemento)
    terceer_elemento = mi_lista[2]
    print(terceer_elemento)

    # Logitud de una lista
    longitud = len(mi_lista)    #Resultado = 6
    print(longitud)
    mi_lista[3]= 'x'
    print(mi_lista)

    # Agregar elementos al final de la lista
    mi_lista.append(4)
    print(mi_lista)

    # Eliminar elemento por valor
    mi_lista.remove('b')
    print(mi_lista)

    # Extender la lista con otra lista
    otra_lista = [5, 6, 7, 8]
    mi_lista.extend(otra_lista)
    print(mi_lista)

    # Slicing (Rebanando)
    sublista = mi_lista[1:4]    #Resultado [2,3,'x']
    print(sublista)

    # Inclusión de Elementos
    existe = 'c' in mi_lista
    print(existe)

    # Tuplas
    mi_tupla = (1,2,3, 'a', 'b', 'c')
    print(mi_tupla)
    # índices y acceso a elementos
    primer_elemento = mi_tupla[0]
    terceer_elemento = mi_tupla[2]
    print(primer_elemento)
    print(terceer_elemento)
    # Longitud de la tupla
    longitud = len(mi_tupla)
    print(longitud)
    # mi_tupla[0] = 'x'   # Esto genere error
    # print(mi_tupla)

    # Empaquetado y desempaquetado
    coordenadas = (10,20)
    x,y = coordenadas   # Ahora x es 10 y y es 20

    # Tuplas anidadas
    tupla_anidada = ((1,2), ('a','b'))

    # Diccionarios
    mi_diccionario = {'clave1':'valor1', 'clave2':'valor2', 'clave3':'valor3'}
    print(mi_diccionario)
    valor_asociado_a_clave1 = mi_diccionario['clave1']
    print(valor_asociado_a_clave1)
    # Modificación y adición de elementos
    mi_diccionario['clave1'] = 'nuevo_valor'
    print(mi_diccionario)
    mi_diccionario['clave4'] = 'valor4'
    print(mi_diccionario)
    # Eliminación de elementos
    del mi_diccionario['clave4']
    print(mi_diccionario)
    # Verificación de existencia de claves
    existe_clave1 = 'clave1' in mi_diccionario
    print(existe_clave1)
    # Longitud del diccionario
    cantidad_elementos = len(mi_diccionario)
    print(cantidad_elementos)
    # Iteración a trvés de claves, valores o elementos
    for clave in mi_diccionario:
        valor = mi_diccionario[clave]
        print(clave, valor)

    # Diccionarios anidados
    diccionario_anidado = {'clave1':{'subclave1':'valor_subclave1'},
                           'clave2':{'subclave2':'valor_subclave2'},
                           'clave3':{'subclave3':'valor_subclave3'}}

























if __name__ == '__main__':
    print_hi('Víctor C. Vladimir Cortés A.')
