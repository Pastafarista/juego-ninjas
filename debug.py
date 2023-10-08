import pygame
import herramientas_imagen as hi
from ajustes import *

def mostar_hitbox(entidad, camara, pantalla):
    
    imagen_x = (entidad.caja_colision.x - camara.x) * ESCALA_ZOOM + camara.offset_x
    imagen_y = (entidad.caja_colision.y - camara.y) * ESCALA_ZOOM + camara.offset_y
    
    camara.render_imagen(pantalla, hi.redimensionar_imagen(pygame.Surface((entidad.caja_colision.width, entidad.caja_colision.height)), ESCALA_ZOOM), (imagen_x, imagen_y))

def mostrar_hitbox_mapa(mapa, camara, pantalla):
    for colision in mapa.hitboxes:
        imagen_x = (colision.x - camara.x) * ESCALA_ZOOM + camara.offset_x
        imagen_y = (colision.y - camara.y) * ESCALA_ZOOM + camara.offset_y
        
        camara.render_imagen(pantalla, hi.redimensionar_imagen(pygame.Surface((colision.width, colision.height)), ESCALA_ZOOM), (imagen_x, imagen_y))

pygame.font.init()

fuente = pygame.font.SysFont("Arial", 30)

def debug(mensaje, x, y):
    display_surf = pygame.display.get_surface()
    texto = fuente.render(mensaje, True, (255, 255, 255))
    debug_rect = texto.get_rect(topleft = (x, y))
    display_surf.blit(texto, debug_rect)
    
    
class fps():
    def __init__(self):
        self.fps_media = 0
        self.fps = []
        self.medicion = 50
        
    def actualizar(self, dt):        
        fps_actual = 0
        
        if dt != 0:
            fps_actual = int(1 / dt)
            
        if (len(self.fps) < self.medicion):
            self.fps.append(fps_actual)
        else:
            if len(self.fps) > 0:
                self.fps_media = sum(self.fps) / len(self.fps)
                self.fps = []
            
    def mostar(self, dt):
        self.actualizar(dt)
        debug("FPS: " + str(int(self.fps_media)), 10, 150)