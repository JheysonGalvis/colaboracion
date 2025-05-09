#Operaciones con cadenas:
cadena1 = "Hola campistas buenas noches, "
cadena2 = "¿Listos para aprender a programar?"

resultado = cadena1 + cadena2

print(resultado)



#formato de cadenas
nombre = "Camila y Juan"
mensaje = f"¡ {nombre} bienvenidos a nuestra sala !"

print(mensaje)



#Subcadenas y métodos
cadena = "Vamos a dividir esta oración y mostrar cada una de las palabras que contiene"
# dividir la cadena en una lista de palabras
palabras = cadena.split()

print("Lista de palabras:")
print(palabras)

#encontrar la posición de una subcadena especifica
subcadena = "oración"
if subcadena in palabras:
    posición = palabras.index(subcadena)
    print(f"la palabra '{subcadena}' se encuentra en la posición {posición} de la lista de palabras.")
else:
    print(f"la palabra '{subcadena}' no se encuentra en la lista de palabras.")



#Métodos de mayúsculas y minúsculas
cadena = "hola, terricolas"

# convertir a mayúsculas
mayúsculas = cadena.upper()

print("cadena en mayúsculas:", mayúsculas)

# convertir a minusculas nuevamente
minusculas = mayúsculas.lower()
print("cadena en minusculas:", minusculas)










