lista = ["Nombre", "Apellido", "edad", "ciudad de origen", "país"]
#nos guarde las respuestas 1 2 y 3
respuestas = []

for i in range(len(lista)):
    print(lista[i])
    respuesta = input()
    respuestas.append(respuesta)

print(respuestas)


