import herramientas_imagen as hi
from ajustes import *
import math

class Hud():
    def __init__(self, jugador):
        self.jugador = jugador
        self.imagen_vida = None
        self.cargar_assets()
        
    def cargar_assets(self):
        self.assets = hi.redimensionar_imagenes(hi.cargar_spritesheet("res/HUD/Heart.png"), ESCALA_ZOOM)
        
    def render_vida(self, pantalla):
        numero_corazones_completos = int(self.jugador.vida / 4)
        
        #renderizar corazones completos
        for corazon in range(numero_corazones_completos):
            pantalla.blit(self.assets[0], (corazon * TAM_TILE * ESCALA_ZOOM, 0))
            
        #renderizar el corazón incompleto
        if self.jugador.vida % 4 != 0:
            pantalla.blit(self.assets[4 - self.jugador.vida % 4], ((numero_corazones_completos) * TAM_TILE * ESCALA_ZOOM, 0))
        
        #renderizar los corazones incompletos
        numero_corazones = math.ceil(self.jugador.vida / 4)
        numero_corazones_vida_maxima = math.ceil(self.jugador.vida_maxima / 4)
    
        for corazon in range(numero_corazones_vida_maxima - numero_corazones):
            pantalla.blit(self.assets[4], ((numero_corazones + corazon) * TAM_TILE * ESCALA_ZOOM, 0))
    
    def render(self, pantalla):
        self.render_vida(pantalla)