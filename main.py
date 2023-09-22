from sys import exit
from ajustes import *
from mundo import *
import herramientas_imagen as hi
from animacion import Animacion
import pygame

#Iniciar pygame
pygame.init()
pygame.display.set_caption("Juego")

#Crear pantalla y mundo
reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode(RESOLUCION)
mundo = Mundo()

animacion = Animacion(hi.redimensionar_imagenes(hi.cargar_imagenes("res/Actor/Animals/Cat/SpriteSheet.png"), 5))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
            
     #Limpiar la pantalla
    pantalla.fill((0, 0, 0))       
        
    mundo.actualizar()
    mundo.dibujar(pantalla)
    
    pantalla.blit(animacion.obtener_frame_actual(), (0, 0))
    animacion.siguiente_frame()

    pygame.display.update()
    reloj.tick(60)
