#Creación de Tuplas:

mi_tupla = (1, 2, 3)
# Trata de modificar un elemento de la tupla
#mi_tupla[0] = 10 
# Esto generará un error porque las tuplas son inmutables

#Desempaquetado de Tuplas:
coordenadas = (10.0, 20.0)
latitud = coordenadas[0]
elngitud = coordenadas[1]
latitud, longitud = coordenadas;

#Operaciones Básicas con Diccionarios:
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
#agrega clave y valor
mi_diccionario["profesion"] = "Ingeniero"
#Acceder a claves 
for clave in mi_diccionario:
    print(clave)

#Diccionario anidado de contactos
contacto_1 = {
    "Ximena": {
        "edad": 22,
        "ciudad": "Manizales",
        "profesion": "Quimica"
    }
    }
contacto_2 = {
    "Juan": {
        "edad": 30,
        "ciudad": "Cali",
        "profesion": "Ingeniero"
}
}
print ("profesion de Juan", contacto_2["Juan"]["profesion"])

#Operaciones Básicas: 
#Crear una lista vacia llamada mi_lista: 
mi_lista = []

#Agregar numeros del 1 al 5 a mi_lista
for i in range(1, 5):
    mi_lista.append(i)

#Imprimir la lista
print(f"lista actual: {mi_lista}")

#Eliminar numero 3 de la lista
if 3 in mi_lista :
    mi_lista.remove(3)
    print("se elimino el 3 de la lista")
else:
    print("no se encontro el 3 en la lista") 
    
#Ejecutar lista final
print(f"lista final: {mi_lista}")

#Rebanado de listas
numeros = [1,2,3,4,5,6,7,8,9,10]
#Primeros tres números
print ("Los 3 primeros números", numeros[0],numeros[1], numeros[2])
print ("Los 3 primeros números", numeros[:3])
#Numeros del tercero al sexto
print("Los números del tercero al sexto", numeros[2],numeros[3],numeros[4],numeros[5])
print ("Los números del tercero al sexto ", numeros[2:6])
#Últimos dos elementos
print("Ultimos dos números", numeros[-2], numeros[-1])
print("Ultimos dos números", numeros[-2:])


#Listas y ciclos:

print("Elementos uno por uno:")
for numero in mi_lista:
    print(numero)


#Tuplas Anidadas interacciones 
mi_tupla = ((1, 2), (3, 4), (5, 6))

print("Elementos uno por uno dentro de la tupla anidada:")
for sub_tupla in mi_tupla:
    for numero in sub_tupla:
        print(numero)
        
op = 1
while op != 0:
    print("Saludos")
    op = int(input("Ingrese 0 para salir o 1 para continuar: "))
#Ejemplo de uso de break      