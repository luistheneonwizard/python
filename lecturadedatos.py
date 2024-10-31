# import csv
# respuestas = ()

# with open["datosdechat.csv", "r"] as archivo:
#     lector = csv.DictReader(archivo)
#     for filas in lector:
#         print[filas["pregunta"]]= filas ["respuestas"] 
#         print(respuestas) # Imprime cada fila como un diccionario

# import csv

# with open("datosdechat.csv", "r") as archivo:
#     lector = csv.DictReader(archivo)
#     for fila in lector:
#         print(fila)  # Imprime cada fila como un diccionario

import csv          

with open("salida.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Nombre", "Edad"])  # Escribir encabezados
    escritor.writerow(["Ana", 28])         # Escribir datos
    escritor.writerow(["Luis", 35])