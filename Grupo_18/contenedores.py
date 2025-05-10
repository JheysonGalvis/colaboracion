from grupo_10.contenedores import mi_lista


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

















if __name__ == '__main__':
    print_hi('Víctor C. Vladimir Cortés A.')
