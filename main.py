from sys import exit
from ajustes import *
from mundo import *
import herramientas_imagen as hi
from animacion import Animacion
from controles import Controles
from entidad_con_sprite import Entidad_con_sprite
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

personaje = Entidad_con_sprite(0, 0, 0, 0, 16, 16, 5)
nombres = ["andar_abajo", "andar_arriba", "andar_izquierda", "andar_derecha"]
indice = 0

for columna in hi.cargar_spritesheet_por_columnas("res/Actor/Characters/Boy/SeparateAnim/Walk.png"):
    animacion = Animacion(hi.redimensionar_imagenes(columna, 5))
    personaje.agregar_animacion(nombres[indice], animacion)
    indice += 1
    
boleano = False
personaje.cambiar_animacion("andar_abajo")

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
    animacion.siguiente_frame()
    
    if controles.obtener_tecla("w") and boleano == False:
        personaje.cambiar_animacion("andar_arriba")
        boleano = True
    elif controles.obtener_tecla("w") == False:
        boleano = False

    pygame.display.update()
    reloj.tick(60)
