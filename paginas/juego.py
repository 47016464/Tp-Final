import pygame
import servicios.cartas as cartas

en_juego = False

def dibujar_fondo(pantalla):
    info = pygame.display.Info()
    imagen = pygame.image.load("recursos/fondos/fondo_partida.jpg")
    imagen = pygame.transform.scale(imagen, (info.current_w, info.current_h))
    pantalla.blit(imagen, (0, 0))

carta_presionada = False
def dibujar_carta(pantalla, coordenadas:tuple, cartas:dict):
    
    w = 80
    h = 60
    
    #Cartas

    carta_obj = pygame.draw.rect(
        pantalla, 
        "#FFFFFF00", 
        pygame.Rect(
            coordenadas[0],
            (coordenadas[1]),
            w, 
            h
            )
        )
    
    archivo = pygame.image.load(cartas["src"]) 
    textura = pygame.transform.scale(archivo, (carta_obj.width, 200))
    pantalla.blit(textura, carta_obj.topleft)
    
    #Clicks

    global carta_presionada
    pos = pygame.mouse.get_pos()
    if carta_obj.collidepoint(pos):
        mouse_buttons = pygame.mouse.get_pressed()
        if carta_presionada == False:
            if mouse_buttons[0]:
                cartas.enviar_carta({"event":"cartas_send", "card":cartas})
                carta_presionada = True
        else:
            if mouse_buttons[0] == False:
                carta_presionada = False

def dibujar_mazo(pantalla, cartas):
    info = pygame.display.Info()
    if len(cartas) == 3:
        dibujar_carta(pantalla, (75, info.current_h - 80 - 60), cartas[0])
        dibujar_carta(pantalla, (75 + 130, info.current_h - 80 - 60), cartas[1])
        dibujar_carta(pantalla, (225 + 110, info.current_h - 80 - 60), cartas[2])


def inicio(pantalla):

    global en_juego
    
    if en_juego == False:
        cartas.mazo_usuario = cartas.cartas_aleatorias()
        cartas.mazo_bot = cartas.cartas_aleatorias()
        en_juego = True

        
    dibujar_fondo(pantalla)
    dibujar_mazo(pantalla, cartas.mazo_usuario)

    #pygame.mixer.init()
    #pygame.mixer.music.load("recursos/sonidos/musica_partida.mp3")
    #pygame.mixer.music.play(-1)
    #pygame.mixer.music.set_volume(0.1)

