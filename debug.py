import pygame
import herramientas_imagen as hi
from ajustes import *

def mostar_hitbox(entidad, camara, pantalla):
    camara.render_imagen(pantalla, hi.redimensionar_imagen(pygame.Surface((entidad.caja_colision.width, entidad.caja_colision.height)), ESCALA_ZOOM), (entidad.caja_colision.x, entidad.caja_colision.y))

pygame.font.init()

fuente = pygame.font.SysFont("Arial", 30)

def render_texto(mensaje, x, y):
    display_surf = pygame.display.get_surface()
    texto = fuente.render(mensaje, True, (255, 255, 255))
    debug_rect = texto.get_rect(topleft = (x, y))
    display_surf.blit(texto, debug_rect)
    
    
def mostar_fps(dt):
    if(dt == 0):
        fps = -1
    else:
        fps = 1 / dt
    
    render_texto("FPS: " + str(round(fps)), 10, 70)