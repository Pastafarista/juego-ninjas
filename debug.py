import pygame
import herramientas_imagen as hi
from ajustes import *

def mostar_hitbox(entidad, camara, pantalla):
    camara.render_imagen(pantalla, hi.redimensionar_imagen(pygame.Surface((entidad.caja_colision.width, entidad.caja_colision.height)), ESCALA_ZOOM), (entidad.caja_colision.x, entidad.caja_colision.y))

def mostrar_posicion(entidad, pantalla):
    
    fuente = pygame.font.SysFont("Arial", 40)
    
    mensaje = "Pos: " + str(entidad.posicion)
    
    texto = fuente.render(mensaje, True, (255, 255, 255)).convert_alpha()
    borde = fuente.render(mensaje, True, (0, 0, 0)).convert_alpha()
    
    pantalla.blit(borde, (10, 100 - 2))
    pantalla.blit(borde, (10, 100 + 2))
    pantalla.blit(borde, (10 - 2, 100))
    pantalla.blit(borde, (10 + 2, 100))
    
    pantalla.blit(texto, (10, 100))