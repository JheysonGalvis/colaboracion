# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Grupo No. 18


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    mensaje  = "Bienvenido al bootcamp de IA Talento Tech2"
    print (mensaje)

    # Formato de Cadenas
    nombre = "Vladimir C."
    edad = 48
    print(f"Mi nombre es {nombre} y tengo {edad} años.")

    # Fin de línea
    print("Hola", end=" ")
    print("Campistas Talento Tech 2!")

    # Especificando un separador diferente
    #Separadores
    nombre = "Vladimir C."
    edad = 48
    print(nombre, edad, sep= "-")

    # Ejemplo de declaración y asignación de variables
    nombre = "Vladimir C."  # Una variable de cadena
    edad = 48   # Una variable de entero
    altura = 1.75   #Una variable de punto flotante
    es_estudiante = True    # Una variable booleana

    # Asociación de valores en la declaración
    ciudad = "Bogotá D.C."
    poblacion = 9000000

    # Reasignación de valores
    ciudad = "Medellin"
    poblacion = 4500000

    # Convenciones de nombres
    nombre_completo = "Vladimir C."
    temperatura_actual = 23.5

    # Tipos de variables dinámicas
    variable_dinamica = 10
    print(variable_dinamica)

    variable_dinamica = "Saludo de bienvenida"
    print(variable_dinamica)

    # Enteros
    entero_postivo = 10
    entero_negativo = -20
    print(entero_postivo, entero_negativo)

    # Flotantes
    flotante_1 = 3.1416
    flotante_2 = -3.1416
    print(flotante_1, flotante_2)

    # Operaciones con enteros y flotantes
    resultado_suma = entero_postivo + entero_negativo + flotante_1 + flotante_2
    resultado_multiplicacion = entero_postivo * entero_negativo * flotante_1 * flotante_2
    print(f"El resultado de la multiplicación es: {resultado_multiplicacion}")
    print(f"El resultado de la suma es: {resultado_suma}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Vladimir Cortés A.')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
