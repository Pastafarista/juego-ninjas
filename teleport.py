import pygame

class Teleport():
    def __init__(self, x, y, tamX, tamY, mapa_origen, nombre_mapa_destino, destino_x, destino_y):
        self.caja_colision = pygame.Rect(x, y, tamX, tamY)
        
        self.mapa_origen = mapa_origen
        self.nombre_mapa_destino = nombre_mapa_destino
        
        self.destino_x = destino_x
        self.destino_y = destino_y
        
        