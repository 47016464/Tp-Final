import pygame

#Funcion para dibujar imagen del fondo del menu
def dibujar_fondo(pantalla):
    info = pygame.display.Info()
    imagen = pygame.image.load("recursos/fondos/fondo_menu.jpg")
    imagen = pygame.transform.scale(imagen, (info.current_w, info.current_h))
    pantalla.blit(imagen, (0, 0)) 


# Callback: Una funcion por parametro

def btn(pantalla:pygame.Surface, posicion:list, texturaBtn:str, callback)-> None:
    pos = pygame.mouse.get_pos()
    
    figura = pygame.draw.rect(pantalla, "#00000000", pygame.Rect(posicion[0], posicion[1], 195, 40))

    btn_pantalla = pygame.image.load(f"recursos/btns/{texturaBtn}.png")
    btn_pantalla = pygame.transform.scale(btn_pantalla, (195, 40)) # tamaño

    pantalla.blit(btn_pantalla, figura.topleft) # Posicion 

    if figura.collidepoint(pos):
        mouse_buttons = pygame.mouse.get_pressed()
        
        if mouse_buttons[0]:
            print("AAAAAAAAA")
            callback()
        

#-----------------------------------inicio
def inicio(pantalla, btns):
    dibujar_fondo(pantalla)

    for item in btns:

        btn(pantalla, item["posicion"], item["textura"], item["callback"])



