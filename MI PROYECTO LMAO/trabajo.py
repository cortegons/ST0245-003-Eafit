import os
import csv  

path1 = "C:/Users/Camilo Ortegon/Desktop/loquesea"
##path2 = ""
sanos = os.listdir(path1)
##enfermos = os.listdir(path2)
matrizSanos = []


for i in sanos:
    with open(str(path1 + "/" + i), 'r') as data:
        entrada = csv.reader(data)
        lista1 = list(entrada)

    arreglo = []
    for line in lista1:
         arreglo.append(line)
    matrizSanos.append(arreglo)
print(matrizSanos)