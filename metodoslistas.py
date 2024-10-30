lista = [1, 2, 3]
print(lista)

lista.append(4) #lista ahora es [1, 2, 3, 4]
print(lista)


lista.extend([5, 6, 7, 8])  # lista ahora es [1, 2, 3, 4, 5, 6]
print(lista)

lista.insert(4, 'nuevo')  # lista ahora es [1, 'nuevo', 2, 3]
print(lista)

lista.remove(2)  # lista ahora es [1, 3] elimina el primer dato de remove que encuentre, si es [1, 2, 3, 2] queda [1, 3, 2]
print(lista)


elemento = lista.pop()  # elemento es 3, lista ahora es [1, 2] elimina el elemento en la última posición si no se le agrega el elemento
print(lista)

#del lista[0] #para borrar un elemento en la posicion indicada
#print(lista)