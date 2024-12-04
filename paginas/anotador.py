import pygame

contador_eq1 = 0
contador_eq2 = 0

def dibujar_fondo(pantalla):
    info = pygame.display.Info()
    imagen = pygame.image.load("recursos/fondos/fondo_partida.jpg")
    imagen = pygame.transform.scale(imagen, (info.current_w, info.current_h))
    pantalla.blit(imagen, (0, 0))



    # fuente_menu = pygame.font.SysFont("Georgia",30)
    # mostrar_texto(pantalla, f"{contador_eq1}",(275, 350), fuente_menu, [0,0,0])
    # mostrar_texto(pantalla, "Puntacion EQ2",(450, 400), fuente_menu, [0,0,0])
    # mostrar_texto(pantalla, f"{contador_eq2}",(535, 250), fuente_menu, [0,0,0])

isClicked = False
def btn(pantalla, text, posicion, callback):

    font_size = 30 
    font = pygame.font.Font(None, font_size)
    text_color = "white"
    text_surface = font.render(text, True, text_color)  # True para suavizar bordes (anti-aliasing)
    
    figura = pygame.draw.rect(pantalla, "#2C2C2C", pygame.Rect(posicion[0], posicion[1], 40, 40))

    pantalla.blit(text_surface, (figura.center[0] - text_surface.get_width() / 2, figura.center[1] - text_surface.get_height() / 2))

    pos = pygame.mouse.get_pos()
    global isClicked

    if figura.collidepoint(pos):
        mouse_buttons = pygame.mouse.get_pressed()
        if isClicked == False:
            if mouse_buttons[0]:
                callback()
                isClicked = True
        else:
            if mouse_buttons[0] == False:
                isClicked = False

def sumar_anotador_eq1():
    global contador_eq1
    if contador_eq1 < 30:
        contador_eq1 += 1
def restar_anotador_eq1():
    global contador_eq1
    if contador_eq1 > 0:
        contador_eq1 -= 1

def sumar_anotador_eq2():
    global contador_eq2
    if contador_eq2 < 30:
        contador_eq2 += 1
def restar_anotador_eq2():
    global contador_eq2
    if contador_eq2 > 0:
        contador_eq2 -= 1




def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def inicio(pantalla):
    dibujar_fondo(pantalla)
    
    #Equipo 1 Contador
    fuente_menu = pygame.font.SysFont("Georgia",30)
    mostrar_texto(pantalla, "Puntacion EQ1",(200, 200), fuente_menu, [0,0,0])
    btn(pantalla, "-", (200, 250), lambda: restar_anotador_eq1())
    btn(pantalla, "+", (250, 250), lambda: sumar_anotador_eq1())
    mostrar_texto(pantalla, str(contador_eq1),(320, 250), fuente_menu, [0,0,0])

    #Equipo 2 Contador
    mostrar_texto(pantalla, "Puntacion EQ2",(450, 200), fuente_menu, [0,0,0])
    btn(pantalla, "-", (450, 250), lambda: restar_anotador_eq2())
    btn(pantalla, "+", (500, 250), lambda: sumar_anotador_eq2())
    mostrar_texto(pantalla, str(contador_eq2),(550, 250), fuente_menu, [0,0,0])
