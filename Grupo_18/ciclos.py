# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Workspace built by group 18.
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    mensaje  = "Bienvenido a la actividad 5 - Ciclos en Python"
    print (mensaje)

    # Estructura básica de un ciclo for
    frutas = ['Manzana', 'Plátano', 'Uvas']
    for fruta in frutas:
        print(fruta)

    for indice, fruta in enumerate(frutas):
        print(f'Índice: {indice}, fruta: {fruta}')

    # While
    contador = 0
    while contador < 5:
        contador += 1
        if contador == 3:
            continue
        print(f'contador:', contador)
        if contador >= 5:
            break

if __name__ == '__main__':
    print_hi('Víctor C. Vladimir Cortés A.')