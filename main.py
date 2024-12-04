import pygame
import sys

#--------------PAGINAS
import paginas.menu as menu
import paginas.juego as partida
import paginas.anotador as anotador
import paginas.opciones as siuu

pygame.init()
pantalla = pygame.display.set_mode((800,500))
pygame.display.set_caption("Truco Goat")
icono = pygame.image.load("recursos/iconos/icono_juego.jpg")
pygame.display.set_icon(icono)
clock = pygame.time.Clock()

bandera = True
ruta = "menu"

def set_ruta(nueva_ruta:str):
    global ruta
    ruta = nueva_ruta
            
pygame.mixer.music.load("recursos/sonidos/musica_menu.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

Musica = True

while bandera == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            if Musica == True:
                pygame.mixer.music.pause()
                Musica = False
            else:
                pygame.mixer.music.unpause()
                Musica = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            set_ruta("menu")

    lista_btn = [
        {
            "posicion":[526, 138],
            "textura":"jugar",
            "callback": lambda: set_ruta("partida")
        },
        {
            "posicion":[526, 185],
            "textura":"anotador",
            "callback": lambda: set_ruta("anotador")
        },
        {
            "posicion":[526, 231],
            "textura":"siuuuu",
            "callback": lambda: set_ruta("opciones")
        },
        {
            "posicion":[526, 277],
            "textura":"salir",
            "callback": lambda: set_ruta("salir")
        },
    ]

    #Lista de diccionarios, con tuplas


    if ruta == "menu":
        menu.inicio(pantalla, lista_btn)
    elif ruta == "partida":
        partida.inicio(pantalla)
        #if pygame.mixer.music.get_busy():
            #pygame.mixer.music.stop()
    elif ruta == "anotador":
        anotador.inicio(pantalla)
    elif ruta == "opciones":
        siuu.inicio(pantalla)
    elif ruta == "salir":
        #salir.inicio(pantalla)
        sys.exit()


    pygame.display.flip()
    clock.tick(60)

pygame.quit()