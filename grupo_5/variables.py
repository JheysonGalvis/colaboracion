#Operaciones con cadenas:
cadena1 = "hola que tal"
cadena2 = "¿como va la noche?"

cadena_final = cadena1 +' '+ cadena2

print(cadena_final)

#/////////////////////////////////////////////////////////////////////////////////////////////

#formato de cadenas
nombre = "grupo5"
print (f"¡ Bienvenido a todos, {nombre}!")

#Subcadenas y métodos
Nombres ="el grupo 5 ya termino este ejercicio"
cc=Nombres.split()
print(cc)
subcadena = "termino"
if subcadena in cc: 
    esta_en = cc .index(subcadena)
    print("La subcadena", subcadena, "se encuentra en la posición", esta_en)
else:
    print("La subcadena", subcadena, "no se encuentra en la lista")
    
#/////////////////////////////////////////////////////////////////////////////////////////////
    
#Métodos de mayúsculas y minúsculas

# Crear una cadena en minúsculas
cadena = "hola mundo"

# Convertirla a mayúsculas usando upper()
cadena_mayusculas = cadena.upper()

# Convertirla nuevamente a minúsculas usando lower()
cadena_minusculas = cadena_mayusculas.lower()

# Mostrar los resultados
print("Original:", cadena)
print("En mayúsculas:", cadena_mayusculas)
print("De nuevo en minúsculas:", cadena_minusculas)

#/////////////////////////////////////////////////////////////////////////////////////////////

# Operaciones aritmeticas

variableA = 2
variableB = 4

suma = variableA + variableB
resta = variableA - variableB
multiplicacion = variableA * variableB
division = variableA / variableB
exponente = variableA ** variableB 

print (f" la suma es: {suma}")
print (f" la resta es: {resta}")
print (f" la multplicacion es: {multiplicacion}")
print (f" la division es: {division}")

#/////////////////////////////////////////////////////////////////////////////////////////////

#División y Módulo

numero1 = 10
numero2 = 4

# Dividir los números y guardar el resultado
resultado = numero1 // numero2  # División entera

# Obtener el residuo usando el operador módulo
residuo = numero1 % numero2

# Imprimir el resultado y el residuo
print("Resultado de la división entera:", resultado)
print("Residuo de la división:", residuo)

#/////////////////////////////////////////////////////////////////////////////////////////////

#Precisión de Flotantes:
c = 6.5
entero = 4

#operaciones aritmeticas mixtas osea variables tipo float y enteros
suma = c + entero
resta = c - entero
multiplicacion = c * entero
division = c / entero

print("El resultado de la Suma es:", suma)
print("El resultado de la Resta es:", resta)
print("El resultado de la Multiplicacion es:", multiplicacion)
print("El resultado de la Division es:", division)

suma=33










