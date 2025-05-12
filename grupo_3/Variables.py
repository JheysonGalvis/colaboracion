#Operaciones con cadenas:
cadena1 = "hola compañeros, "
cadena2 = "¿se sienten contentos aprendiendo a programar?"

resultado = cadena1 + cadena2

print(resultado)



#formato de cadenas
nombre = "Juan CM"
mensaje = f"¡ Bienvenido a nuestras clases, {nombre}!"

print(mensaje)



#Subcadenas y métodos
cadena = "la inteligencia artificial es una tecnologia en constante evolución y mejora"
# dividir la cadena en una lista de palabras
palabras = cadena.split()

print("lista de palabras:")
print(palabras)

#encontrar la posición de una subcadena especifica
subcadena = "artificial"
if subcadena in palabras:
    posición = palabras.index(subcadena)
    print(f"la palabra '{subcadena}' se encuentra en la posición {posición} de la lista de palabras.")
else:
    print(f"la palabra '{subcadena}' no se encuentra en la lista de palabras.")



#Métodos de mayúsculas y minúsculas
cadena = "hola, tierra"

# convertir a mayúsculas
mayúsculas = cadena.upper()

print("cadena en mayúsculas:", mayúsculas)

# convertir a minusculas nuevamente
minusculas = mayúsculas.lower()
print("cadena en minusculas:", minusculas)










