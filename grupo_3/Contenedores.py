# Creamos la tupla
mi_tupla = (1, 2, 3)

# intentamos modificar un elemento
try:
    mi_tupla[0] = 10
except TypeError as e:
    print(e)
    
    
    
    # Creamos la tupla
    mi_tupla = (1, 2, 3)
    
    # Creamos una nueva tupla con el cambio
    mi_nueva_tupla = (10,) + mi_tupla[1:]
    print(mi_nueva_tupla) # salida: (10, 2, 3)
    
    
    
# Desempaquetado de tuplas
# creamos la tupla coordenadas
coordenadas = (4.6097, -74.0817) # Latitud y longitud de Bogotá, Colombia

# Desempaquetamos la tupla en dos variables
latitud, longitud = coordenadas

print(f"Latitud: {latitud}")
print(f"Longitud: {longitud}")



# Operaciones Básicas con Diccionarios
# Creamos el diccionario con tres pares clave-valor
mi_diccionario = {
    "nombre": "Juan",
    "edad": 37,
    "ciudad": "Medellín"
}

# Agregamos un nuevo par clave-valor
mi_diccionario["pais"] = "Colombia"

# Imprimimos solo las claves del diccionario
print("claves del diccionario:")
for clave in mi_diccionario.keys():
    print(clave)
    
    
    


# Diccionarios Anidados
# creamos el diccionario anidado
contactos = {
    "juan": {
        "nombre": "Juan pérez",
        "edad": 30,
        "ciudad": "medellín"
    },
    "maria": {
        "nombre": "Maria Gómez",
        "edad": 25,
        "ciudad": "Bogota"
    }
}

# Accedemos e imprimimos información específica de una persona
print("Información de Juan:")
print(f"Nombre: {contactos['juan']['nombre']}")
print(f"Edad: {contactos['juan']['edad']}")
print(f"Ciudad: {contactos['juan']['ciudad']}")

# Tambien podemos acceder a la información de manera mas general
for clave, valor in contactos["juan"].items():
        print(f"{clave.capitalize()}: {valor}")
        
        
        
# Iteración y actualización
# Creamos el diccionario
mi_diccionario = {
    "nombre": "juan",
    "edad": 30,
    "ciudad": "Medellín"
}

# Imprimimos todas las claves y valores del diccionario
print("Diccionario original:")
for clave, valor in mi_diccionario.items():
    print(f"{clave.capitalize()}: {valor}")
    
    # Actualizamos el valor de una clave
    mi_diccionario["edad"] = 31
    
    # imprimimos el diccionario actualizado
print("\nDiccionario actualizado:")
for clave, valor in mi_diccionario.items():
    print(f"{clave.capitalize()}: {valor}")
    
    
    
    # Operaciónes basicas
    # Creamos la lista vacia
    mi_lista = []
    
    # Agregamos los numeros del 1 al 5 a la lista
    mi_lista.append(1)
    mi_lista.append(2)
    mi_lista.append(3)
    mi_lista.append(4)
    mi_lista.append(5)
    
    # Imprimimos la lista
    print("lista original:", mi_lista)
    
    # Eliminamos el numero 3 de la lista
    mi_lista.remove(3)
    
    # Imprimimos la lista actualizada
    print("Lista actualizada:", mi_lista)
    
    
    
    # Rebanado de listas
    # Creamos la lista de números del 1 al 10
    números = list(range(1, 11))
    
    # Imprimimos los primeros tres elementos
    print("Primeros tres elementos:", números[:3])
    
    # Imprimimos los elementos desde el tercero hasta el sexto
    print("Elementos del tercero al sexto:", números[2:6])
    
    # Imprimimos los ultimos dos elementos
    print("Ultimos dos elementos:", números[-2:])
    
    
    
    # Listas y ciclos
    # Creamos la lista
    mi_lista = [1, 2, 4, 5]
    
    # Imprimimos cada elemento de la lista
    for elemento in mi_lista:
        print(elemento)
        
    
    
    