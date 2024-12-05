import pygame
import componentes.bloque_texto as textBox
import servicios.cartas as ServicioCarta

def dibujar_fondo(pantalla):
    info = pygame.display.Info()
    imagen = pygame.image.load("recursos/fondos/fondo_partida.jpg")
    imagen = pygame.transform.scale(imagen, (info.current_w, info.current_h))
    pantalla.blit(imagen, (0, 0)) 


def inicio(pantalla):
    dibujar_fondo(pantalla)

    textBox.create(pantalla, f"Puntos BOT: {ServicioCarta.puntos_bot}", (165, 211), 24, "black")
    textBox.create(pantalla, f"Puntos USUARIO: {ServicioCarta.puntos_user}", (165, 276), 24, "black")