#Creación de Tuplas:
mi_tupla = (1, 2, 3)
# Trata de modificar un elemento de la tupla
mi_tupla[0] = 10
# Esto generará un error porque las tuplas son inmutables

#Desempaquetado de Tuplas:
coordenadas = (10.0, 20.0)
latitud = coordenadas[0]
longitud = coordenadas[1]
latitud, longitud = coordenadas;

#Operaciones Básicas con Diccionarios:
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
#agreaga clave y valor
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
print ("profesion de Juan", contacto_2["Juan"]["edad"])