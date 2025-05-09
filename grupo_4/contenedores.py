# Ejemplos de contenedores en Python

# Creacion de tuplas
mi_tupla = (2, 4, 6, 'n', 's', 'a')
#mi_tupla[1] = 5
print(mi_tupla)

# Desempaquetado de tuplas

coordenadas = ('4° 35` 56″ N' , '74° 4` 22″ O')

latitud, longitud = coordenadas
print(f" la latitud es {latitud} y la longitud es {longitud}")

# Operaciones con diccionarios

mi_diccionario = {
    'nombre' : 'Miguel',
    'edad' : 25,
    'ocupacion' : 'Ingeniero'
}

print(mi_diccionario['nombre'])


# Diccionario anidado

contactos = {
    'persona1' : {
        'nombre' : 'Juan',
        'telefono' : '123456789'
    },
    'persona2' : {
        'nombre' : 'Maria',
        'telefono' : '987654321'
    }
}

print(contactos['persona2'])

# Iteracion y actualizacion de diccionarios

for clave in mi_diccionario.items():
    print(clave)

mi_diccionario['edad'] = 41
mi_diccionario['telefono'] = '3156738897'
print(mi_diccionario)