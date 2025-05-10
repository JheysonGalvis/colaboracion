frutas = ["manzana", "plátano", "uva"]
for fruta in frutas:
    print(fruta)
frutas = ["manzana", "plátano", "uva"]

for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")
    
contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1
    
contador = 0

while True:
    print(f"Contador: {contador}")
    contador += 1
    if contador >= 5:
        break
    
contador = 0

while contador < 5:
    contador += 1
    if contador == 3:
        continue
    print(f"Contador: {contador}")
