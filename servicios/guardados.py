import csv

def guardar_jugador(nombre: str) -> None:
    with open("jugadores.txt", "a") as archivo:
        archivo.write(f"{nombre}\n")