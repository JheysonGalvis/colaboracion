mi_lista = ['a', 'b', 'c', 1, 2, 3]
primer_elemento = mi_lista[0]  #Resultado: 1
tercer_elemento = mi_lista[2]  #Resultado: 3
print(primer_elemento)
print(tercer_elemento)
print(mi_lista[5])

# Agregar elementos al final de la lista
mi_lista.append(4)
mi_lista.append('grupo_10')

#Eliminar elementos por valor
mi_lista.remove('b')

# Extender la lista con otra lista
otra_lista = [5, 6]
mi_lista.extend(otra_lista)
mi_lista.remove(5)
print(mi_lista)
