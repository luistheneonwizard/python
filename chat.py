#pregunta1 = input(f"Cómo estás")

#print(f"Bien y tú?{pregunta1}")



# numero1 = input("ingrese el primer numero")
# numero2 = input("ingrese el segundo numero")

# print(int(numero1) - int(numero2)) 

lista = ["clima", "trafico", "salir"]
#nos guarda las respuestas 1, 2 y 3

for pregunta in lista:
    print(pregunta)

    if pregunta == "clima":
        print(f"el clima hoy es caluroso")
    elif pregunta == "trafico":
        print(f"el trafico esta pesado")
    elif pregunta == "salir":
        #print("saliste")
        break
    else:
        print("no entiendo tu pregunta")
print("Test finalizado")





