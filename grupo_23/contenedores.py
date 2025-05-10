# Creación de Tuplas
tupla = (17, 'a')
#tupla[0] = 19 # Las tuplas son inmutables, esta instrucción generará error

# Desempaquetado de Tuplas
coordenadas = ("41°54'10\"N", "12°27'20\"E")
latitud, longitud = coordenadas
print(latitud)
print(longitud)

# Operaciones Básicas con Diccionarios
diccionario = {'nombre':'Juan', 'apellido':'Pérez', 'edad': '25'}
diccionario.update({'sexo':'masculino'})
for clave in diccionario:
    print(clave)
    
