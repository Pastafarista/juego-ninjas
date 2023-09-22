from sys import exit
from ajustes import *
from mundo import *
import herramientas_imagen as hi
from animacion import Animacion
from controles import Controles
from jugador import Jugador
import pygame

#Iniciar pygame
pygame.init()
pygame.display.set_caption("Juego Ninjas")

#Crear pantalla y mundo
reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode(RESOLUCION)
mundo = Mundo()

controles = Controles()

#Icono de la ventana
icono = pygame.image.load("res/Actor/Animals/Cat/Faceset.png").convert_alpha()
pygame.display.set_icon(icono)

personaje = Jugador(controles)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
                  
     #Limpiar la pantalla
    pantalla.fill((0, 0, 0))       
        
    #Recibir input del usuario
    controles.actualizar()
        
    #Actualizar y dibujar el mundo
    mundo.actualizar()
    mundo.dibujar(pantalla)
    
    personaje.actualizar()
    
    pantalla.blit(personaje.obtener_frame_actual(), (0, 0))
   

    pygame.display.update()
    reloj.tick(60)
