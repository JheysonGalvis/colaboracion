#ejercicios de Ciclos

#ciclo for
#ejemplo practico

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
    
#funcion enumerate
for indice , fruta in enumerate(frutas):
    print(f"Fruta {indice}: {fruta}")

#ciclo while
#ejemplo practico
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1
    
    
#ejemplo de uso de break
while True:
    print(f"Contador: {contador}")
    contador += 1
    if contador >= 5:
        break
    
#ejemplo de uso de continue
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue
    print(f"Contador: {contador}")
    