import pygame
# NEW
def create(screen, text:str, pos:tuple, font_size:int=16, color:str="white"):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)  # True para suavizar bordes (anti-aliasing)
    screen.blit(text_surface, pos)