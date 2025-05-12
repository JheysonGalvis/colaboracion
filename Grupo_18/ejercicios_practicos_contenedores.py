# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Workspace built by group 18.



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    mensaje  = "Bienvenido a la actividad 4.1 - Ejercicios Prácticos de Contenedores en Python"
    print (mensaje)
    # Creación de la tupla
    mi_tupla = (1, "Python", 3.14)

    # Intento de modificar un elemento
    try:
        mi_tupla[0] = 42
    except TypeError as e:
        print(f"Error: {e}")

    # Creación de la tupla coordenadas
    coordenadas = (40.7128, -74.0060)  # Ejemplo: Latitud y Longitud de Nueva York

    # Desempaquetado
    latitud, longitud = coordenadas

    print(f"Latitud: {latitud}")
    print(f"Longitud: {longitud}")

    # Creación del diccionario con tres pares clave-valor
    mi_diccionario = {"nombre": "Vladimir", "edad": 30, "ciudad": "Bogotá"}

    # Agregar una nueva clave-valor
    mi_diccionario["profesión"] = "Desarrollador"

    # Imprimir solo las claves
    print(mi_diccionario.keys())

    # Creación del diccionario anidado con información de dos personas
    contactos = {
        "persona1": {"nombre": "Ana", "edad": 25, "correo": "ana@email.com"},
        "persona2": {"nombre": "Carlos", "edad": 32, "correo": "carlos@email.com"}
    }

    # Acceder e imprimir información de una persona específica
    print(contactos["persona1"]["nombre"])  # Imprime: Ana
    print(contactos["persona2"]["correo"])  # Imprime: carlos@email.com

    # Bucle para imprimir todas las claves y valores
    for clave, valor in mi_diccionario.items():
        print(f"{clave}: {valor}")

    # Actualizar el valor de una clave
    mi_diccionario["edad"] = 31

    # Imprimir diccionario actualizado
    print(mi_diccionario)

    # Creación de una lista vacía
    mi_lista = []

    # Agregar números del 1 al 5
    mi_lista.extend([1, 2, 3, 4, 5])

    # Imprimir la lista
    print("Lista inicial:", mi_lista)

    # Eliminar el número 3
    mi_lista.remove(3)

    print("Lista después de eliminar el 3:", mi_lista)

    # Rebanado de listas
    # Creación de la lista con números del 1 al 10
    numeros = list(range(1, 11))

    # Imprimir los primeros tres elementos
    print("Primeros tres elementos:", numeros[:3])

    # Imprimir los elementos desde el tercero hasta el sexto
    print("Del tercero al sexto:", numeros[2:6])

    # Imprimir los últimos dos elementos
    print("Últimos dos elementos:", numeros[-2:])

    # Bucle para imprimir cada elemento de mi_lista
    for elemento in mi_lista:
        print("Elemento:", elemento)


if __name__ == '__main__':
    print_hi('Víctor C. Vladimir Cortés A.')
