from datetime import *
import csv
from importlib.resources import path
import os
import time
from tkinter import END

#Inicializando Variables
initial_count = 0
completados = 0
contenido = []
auxreader = []
ingreso = []
#mtzConsolidado1 = ["Host","Begin_date","End_date","Duration","Down","UP","UNREACHABLE","SCHEDULED DOWNTIME","UNDETERMINED"]

#Folder Path
path = r"C:\Users\OSP2021\Desktop\prueba"

#Change the directory
os.chdir(path)

#Realiza el conteo de cuantos archivos del tipo a exportar se encuentran en la carpeta.
for file in os.listdir():
    if os.path.isfile(os.path.join(path, file)) and file.endswith(".csv"):
        initial_count += 1
    #endif
#endfor

#Read CSV File
def read_CSV_file(file_path):
    with open(file_path, 'r', encoding="utf8") as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            auxreader.append(row)
            #print(row)
        
        #print(len(auxreader))
        auxcodigoDane = auxreader[1][0]
        codigoDane = auxcodigoDane[0:12]
        nombreSede = auxcodigoDane[13:]
        #print(codigoDane)
        #print(nombreSede)
        
        for i in range(len(auxreader)):
            if i > 15:
                auxFecha = auxreader[i][11]
                auxUP = auxreader[i][2]
                auxDown = auxreader[i][5]
                auxUNRE = auxreader[i][8]
                ingreso.append([codigoDane, nombreSede, auxFecha, auxUP, auxDown, auxUNRE])
            #endif
        #endfor

#iterate through all file
for file in os.listdir():
    #Check whether file is in text format or not
    if file.endswith(".csv"):
        file_path = f"{path}\{file}"
        
        #call read text file funtion
        read_CSV_file(file_path)
        #completados += 1
        #print(f"{completados} de {initial_count}, {file} Completado...")
        #time.sleep(2)
    #endif
#endfor

"""
with open('consolidado.csv', 'w') as csvfile:
    fieldnames = mtzConsolidado1
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n')
    
    writer.writeheader()
    for i in range(len(contenido)):
        writer.writerow({'Host': contenido[i][0],
                        'Begin_date': contenido[i][1],
                        'End_date': contenido[i][2],
                        'Duration': contenido[i][3],
                        'Down': contenido[i][4],
                        'UP': contenido[i][5],
                        'UNREACHABLE': contenido[i][6],
                        'SCHEDULED DOWNTIME': contenido[i][7],
                        'UNDETERMINED': contenido[i][8]})
    #endfor
"""