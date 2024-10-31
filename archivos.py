import csv

# Abrir el archivo CSV
with open("datosdechat.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)  # Imprime cada fila como una lista

import csv
# Crear un archivo CSV y escribir en él
with open("salida.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Nombre", "Edad"])  # Escribir encabezados
    escritor.writerow(["Ana", 28])         # Escribir datos
    escritor.writerow(["Luis", 35])
            