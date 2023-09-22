from sys import exit
from ajustes import *
from mundo import *
import pygame

#Iniciar pygame
pygame.init()
pygame.display.set_caption("Juego")

#Crear pantalla y mundo
reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode(RESOLUCION)
mundo = Mundo()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    mundo.actualizar()
    mundo.dibujar(pantalla)

    pygame.display.update()
    reloj.tick(60)
