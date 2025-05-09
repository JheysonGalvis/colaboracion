# This is a sample Python script.
from Grupo_6.variables import es_estudiante


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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
    población = 9000000

    # Reasignación de valores
    ciudad = "Medellin"
    poblacion = 4500000




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Vladimir Cortés A.')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
