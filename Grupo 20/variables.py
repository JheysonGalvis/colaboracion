#Operaciones con cadenas
cadena1 = 'Soy Cadena 1'
cadena2 = 'Soy Cadena 2'
cadena3 = cadena1 + ' y ' + cadena2
print(cadena3)
print(f"la longitud de la cadena3 es: {len(cadena3)}")

# Formato de cadenas
nombre = "Rubén"
edad = 67
print(f"Mi nombre es {nombre} y tengo {edad} años.")

#subcadenas y métodos
cadena_larga = "Hola, estamos haciendo los ejercicios en python"
lista = cadena_larga.split()
print(f"Vamos a imprimir la cadena #5: {lista[4]}")

#Métodos de mayúsculas y minúsculas
minusculas = 'soy minusculas'
mayusculas = 'SOY MAYUSCULAS'
print(f"Ahora soy mayusculas: {minusculas.upper()}")
print(f"Ahora soy minusculas: {mayusculas.lower()}")

#Operaciones aritméticas
#División y módulo
num1 = 56
num2 = 12

resultado = num1%num2
print(resultado)

#Precisión de flotantes
c = 5.5
d = 4
e = c*d
f = c/d
print(f"resultado de la multiplicacion: {e:.1f}")
print(f"resultado de la division: {f:.1f}")