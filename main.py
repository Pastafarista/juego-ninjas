import pygame
from sys import exit
from ajustes import *
from mundo import Mundo
from jugador import Jugador
from camara import Camara
import time 
import debug

#Iniciar pygame
pygame.init()
pygame.display.set_caption("Juego Ninjas")

pantalla = pygame.display.set_mode(RESOLUCION)

mundo = Mundo()

mapa = mundo.mapas["mundo"]

#Icono de la ventana
icono = pygame.image.load("res/Actor/Animals/Cat/Faceset.png").convert_alpha()
pygame.display.set_icon(icono)

personaje = Jugador(mapa)

mapa.entidades.append(personaje)
camara = Camara(personaje)

last_time = time.time()

while True:
    
    # Carlcar el delta time
    dt = time.time() - last_time
    last_time = time.time()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
                  
    #Limpiar la pantalla
    pantalla.fill((0, 0, 0))       
    
    mundo.actualizar(dt)
    camara.actualizar()
    camara.render(pantalla)
    
    debug.mostar_fps(dt)
    debug.debug("Posición: " + str(personaje.pos_x) + " " +  str(personaje.pos_y), 10, 200)
    pygame.display.update()
    

