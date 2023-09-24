from sys import exit
from ajustes import *
from mapa import Mapa
from controles import Controles
from jugador import Jugador
import pygame

#Iniciar pygame
pygame.init()
pygame.display.set_caption("Juego Ninjas")

#Crear pantalla y mundo
reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode(RESOLUCION)

mapa = Mapa("mapas/mapa.json")

controles = Controles()

#Icono de la ventana
icono = pygame.image.load("res/Actor/Animals/Cat/Faceset.png").convert_alpha()
pygame.display.set_icon(icono)

personaje = Jugador(controles, mapa)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
                  
     #Limpiar la pantalla
    pantalla.fill((0, 0, 0))       
    
    personaje.actualizar()
    
    personaje.camara.render_mapa(pantalla)
    personaje.camara.render_entidad(personaje, pantalla)
    
    pygame.display.update()
    reloj.tick(60)
