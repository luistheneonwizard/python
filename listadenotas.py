estudiantes = []
notamision1 = []
notamision2 = []
notamision3 = []
promedio = []
tamano = int(input("ingrese el tamaño de la lista: "))
for i in range(tamano):
    estudiante=input("ingrese el nombre de el estudiante: ")
    nota1=float(input("nota mision 1 "))
    nota2=float(input("nota mision 2 "))
    nota3=float(input("nota mision 3 "))
    promedios = (nota1 + nota2 + nota3)/3 
    estudiantes.append(estudiante)
    notamision1.append(nota1)
    notamision2.append(nota2)
    notamision3.append(nota3)
    promedio.append(promedios)
    
i=0
while i<len(estudiantes):
    print(estudiantes[i], promedio[i], notamision1[i], notamision2[i], notamision3[i])
    i+=1




