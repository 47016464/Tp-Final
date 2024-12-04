import csv

def crear_archivo(ruta:str, contenido:any):
    with open(ruta, "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(contenido)

def leer_archivo(ruta:str):
    data = []
    with open(ruta, "r") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            data.append(fila)
    return data