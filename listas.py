#pregunta tamaño lista
#ingresar uno a uno los elementos de la lista
lista = [1,2,3,4,5,6,7,8,9]
i=0

tamano = input(f"Tamaño de la lista")



lista.append(11) #para agregar otro valor a la lista
#print(len(lista))
while i<len(lista):
    print(lista[i])
    i+=1 #variable de control