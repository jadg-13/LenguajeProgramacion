#listas
lista = [1, 2, 3, "Manzana", 15.6, True]
print(lista)

#imprimir el primer elemento de la lista
print(lista[0])
#tamaño de la lista
tam = len(lista)
print(f"el tamaño es {tam}")
#imprimir el ultimo valor
print(lista[tam-1])

#Imprimir los primeros 3 elementos
print(lista[0:3])

#imprimir los elementos 4 hasta 6
print(lista[3:7])

#agregar un elemento a la lista
lista.append("Duran")
print(lista)

#Imprimir los ultimos tres elementos de la lista
final = len(lista)
inicio = final - 3
print(lista[inicio: final +1])

#Eliminar manzana
lista.remove("Manzana")
lista.remove("Duran")

#ordenar lista
lista.sort()
print(lista)